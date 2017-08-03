""" cisco_ia 

DMI self\-management YANG module for IOS
Copyright (c) 2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class CiaLogLevel(Enum):
    """
    CiaLogLevel

    Logging levels for DMI

    .. data:: none = 0

    	No logging

    .. data:: error = 1

    	Log errors only

    .. data:: warning = 2

    	Log errors and warnings only

    .. data:: information = 3

    	Log errors, warnings, and information only

    .. data:: debug = 4

    	Log errors, warnings, information,

    	and debug messages

    """

    none = Enum.YLeaf(0, "none")

    error = Enum.YLeaf(1, "error")

    warning = Enum.YLeaf(2, "warning")

    information = Enum.YLeaf(3, "information")

    debug = Enum.YLeaf(4, "debug")


class CiaSyncType(Enum):
    """
    CiaSyncType

    Controls the elements sent to the DMI 

    database from the Network Element

    .. data:: disabled = 0

    	Do no synchronize the DMI

    	database from the Network Element

    .. data:: without_defaults = 1

    	Collect "show running" from 

    	the Network Element

    .. data:: include_defaults = 2

    	Collect "show running all" from 

    	the Network Element

    """

    disabled = Enum.YLeaf(0, "disabled")

    without_defaults = Enum.YLeaf(1, "without-defaults")

    include_defaults = Enum.YLeaf(2, "include-defaults")


class OnepLogLevel(Enum):
    """
    OnepLogLevel

    Logging levels for Onep

    .. data:: none = 0

    	No logging

    .. data:: fatal = 1

    	Log fatal events only

    .. data:: error = 2

    	Log fatal events and errors only

    .. data:: warning = 3

    	Log fatal events, errors, and warnings only

    .. data:: information = 4

    	Log fatal events, errors, warnings, 

    	and information only

    .. data:: debug = 5

    	Log fatal events, errors, warnings, information,

    	and debug messages

    .. data:: trace = 6

    	Log all messages

    """

    none = Enum.YLeaf(0, "none")

    fatal = Enum.YLeaf(1, "fatal")

    error = Enum.YLeaf(2, "error")

    warning = Enum.YLeaf(3, "warning")

    information = Enum.YLeaf(4, "information")

    debug = Enum.YLeaf(5, "debug")

    trace = Enum.YLeaf(6, "trace")


class SyslogSeverity(Enum):
    """
    SyslogSeverity

    Standard Syslog logging levels)

    .. data:: none = 8

    	No logging

    .. data:: emergency = 0

    	Emergency Level Msg

    .. data:: alert = 1

    	Alert Level Msg

    .. data:: critical = 2

    	Critical Level Msg

    .. data:: error = 3

    	Error Level Msg

    .. data:: warning = 4

    	Warning Level Msg

    .. data:: notice = 5

    	Notification Level Msg

    .. data:: info = 6

    	Informational Level Msg

    .. data:: debug = 7

    	Debugging Level Msg

    """

    none = Enum.YLeaf(8, "none")

    emergency = Enum.YLeaf(0, "emergency")

    alert = Enum.YLeaf(1, "alert")

    critical = Enum.YLeaf(2, "critical")

    error = Enum.YLeaf(3, "error")

    warning = Enum.YLeaf(4, "warning")

    notice = Enum.YLeaf(5, "notice")

    info = Enum.YLeaf(6, "info")

    debug = Enum.YLeaf(7, "debug")



class SyncFrom(Entity):
    """
    Synchronize the network element's 
    running\-configuration to ConfD.
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xe.cisco_ia.SyncFrom.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:   :py:class:`Output <ydk.models.cisco_ios_xe.cisco_ia.SyncFrom.Output>`
    
    

    """

    _prefix = 'cisco-ia'
    _revision = '2017-03-02'

    def __init__(self):
        super(SyncFrom, self).__init__()
        self._top_entity = None

        self.yang_name = "sync-from"
        self.yang_parent_name = "cisco-ia"

        self.input = SyncFrom.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")

        self.output = SyncFrom.Output()
        self.output.parent = self
        self._children_name_map["output"] = "output"
        self._children_yang_names.add("output")


    class Input(Entity):
        """
        
        
        .. attribute:: ignore_presrv_paths
        
        	Sync everything under /native. Ignore any preserve paths
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: sync_defaults
        
        	Sends the output of  "show running all" line by line to Confd
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'cisco-ia'
        _revision = '2017-03-02'

        def __init__(self):
            super(SyncFrom.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "sync-from"

            self.ignore_presrv_paths = YLeaf(YType.empty, "ignore-presrv-paths")

            self.sync_defaults = YLeaf(YType.empty, "sync-defaults")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("ignore_presrv_paths",
                            "sync_defaults") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(SyncFrom.Input, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(SyncFrom.Input, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.ignore_presrv_paths.is_set or
                self.sync_defaults.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.ignore_presrv_paths.yfilter != YFilter.not_set or
                self.sync_defaults.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "input" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "cisco-ia:sync-from/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.ignore_presrv_paths.is_set or self.ignore_presrv_paths.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ignore_presrv_paths.get_name_leafdata())
            if (self.sync_defaults.is_set or self.sync_defaults.yfilter != YFilter.not_set):
                leaf_name_data.append(self.sync_defaults.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ignore-presrv-paths" or name == "sync-defaults"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "ignore-presrv-paths"):
                self.ignore_presrv_paths = value
                self.ignore_presrv_paths.value_namespace = name_space
                self.ignore_presrv_paths.value_namespace_prefix = name_space_prefix
            if(value_path == "sync-defaults"):
                self.sync_defaults = value
                self.sync_defaults.value_namespace = name_space
                self.sync_defaults.value_namespace_prefix = name_space_prefix


    class Output(Entity):
        """
        
        
        .. attribute:: result
        
        	Output returned by the network element
        	**type**\:  str
        
        

        """

        _prefix = 'cisco-ia'
        _revision = '2017-03-02'

        def __init__(self):
            super(SyncFrom.Output, self).__init__()

            self.yang_name = "output"
            self.yang_parent_name = "sync-from"

            self.result = YLeaf(YType.str, "result")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("result") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(SyncFrom.Output, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(SyncFrom.Output, self).__setattr__(name, value)

        def has_data(self):
            return self.result.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.result.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "output" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "cisco-ia:sync-from/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.result.is_set or self.result.yfilter != YFilter.not_set):
                leaf_name_data.append(self.result.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "result"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "result"):
                self.result = value
                self.result.value_namespace = name_space
                self.result.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (
            (self.input is not None and self.input.has_data()) or
            (self.output is not None and self.output.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.input is not None and self.input.has_operation()) or
            (self.output is not None and self.output.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "cisco-ia:sync-from" + path_buffer

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
                self.input = SyncFrom.Input()
                self.input.parent = self
                self._children_name_map["input"] = "input"
            return self.input

        if (child_yang_name == "output"):
            if (self.output is None):
                self.output = SyncFrom.Output()
                self.output.parent = self
                self._children_name_map["output"] = "output"
            return self.output

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "input" or name == "output"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = SyncFrom()
        return self._top_entity

class SaveConfig(Entity):
    """
    Copy the running\-config to 
    startup\-config on the Network
    Element.
    
    .. attribute:: output
    
    	
    	**type**\:   :py:class:`Output <ydk.models.cisco_ios_xe.cisco_ia.SaveConfig.Output>`
    
    

    """

    _prefix = 'cisco-ia'
    _revision = '2017-03-02'

    def __init__(self):
        super(SaveConfig, self).__init__()
        self._top_entity = None

        self.yang_name = "save-config"
        self.yang_parent_name = "cisco-ia"

        self.output = SaveConfig.Output()
        self.output.parent = self
        self._children_name_map["output"] = "output"
        self._children_yang_names.add("output")


    class Output(Entity):
        """
        
        
        .. attribute:: result
        
        	Output returned by the network element
        	**type**\:  str
        
        

        """

        _prefix = 'cisco-ia'
        _revision = '2017-03-02'

        def __init__(self):
            super(SaveConfig.Output, self).__init__()

            self.yang_name = "output"
            self.yang_parent_name = "save-config"

            self.result = YLeaf(YType.str, "result")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("result") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(SaveConfig.Output, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(SaveConfig.Output, self).__setattr__(name, value)

        def has_data(self):
            return self.result.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.result.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "output" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "cisco-ia:save-config/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.result.is_set or self.result.yfilter != YFilter.not_set):
                leaf_name_data.append(self.result.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "result"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "result"):
                self.result = value
                self.result.value_namespace = name_space
                self.result.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (self.output is not None and self.output.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.output is not None and self.output.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "cisco-ia:save-config" + path_buffer

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

        if (child_yang_name == "output"):
            if (self.output is None):
                self.output = SaveConfig.Output()
                self.output.parent = self
                self._children_name_map["output"] = "output"
            return self.output

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "output"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = SaveConfig()
        return self._top_entity

class IsSyncing(Entity):
    """
    Checks to see if sync from the
    network element to the running data store
    is in progress.
    
    .. attribute:: output
    
    	
    	**type**\:   :py:class:`Output <ydk.models.cisco_ios_xe.cisco_ia.IsSyncing.Output>`
    
    

    """

    _prefix = 'cisco-ia'
    _revision = '2017-03-02'

    def __init__(self):
        super(IsSyncing, self).__init__()
        self._top_entity = None

        self.yang_name = "is-syncing"
        self.yang_parent_name = "cisco-ia"

        self.output = IsSyncing.Output()
        self.output.parent = self
        self._children_name_map["output"] = "output"
        self._children_yang_names.add("output")


    class Output(Entity):
        """
        
        
        .. attribute:: result
        
        	Output returned by the network element
        	**type**\:  str
        
        

        """

        _prefix = 'cisco-ia'
        _revision = '2017-03-02'

        def __init__(self):
            super(IsSyncing.Output, self).__init__()

            self.yang_name = "output"
            self.yang_parent_name = "is-syncing"

            self.result = YLeaf(YType.str, "result")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("result") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(IsSyncing.Output, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(IsSyncing.Output, self).__setattr__(name, value)

        def has_data(self):
            return self.result.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.result.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "output" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "cisco-ia:is-syncing/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.result.is_set or self.result.yfilter != YFilter.not_set):
                leaf_name_data.append(self.result.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "result"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "result"):
                self.result = value
                self.result.value_namespace = name_space
                self.result.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (self.output is not None and self.output.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.output is not None and self.output.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "cisco-ia:is-syncing" + path_buffer

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

        if (child_yang_name == "output"):
            if (self.output is None):
                self.output = IsSyncing.Output()
                self.output.parent = self
                self._children_name_map["output"] = "output"
            return self.output

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "output"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = IsSyncing()
        return self._top_entity

class Checkpoint(Entity):
    """
    Create a configuration rollback checkpoint.
    Equivalent to the "archive config" CLI
    
    .. attribute:: output
    
    	
    	**type**\:   :py:class:`Output <ydk.models.cisco_ios_xe.cisco_ia.Checkpoint.Output>`
    
    

    """

    _prefix = 'cisco-ia'
    _revision = '2017-03-02'

    def __init__(self):
        super(Checkpoint, self).__init__()
        self._top_entity = None

        self.yang_name = "checkpoint"
        self.yang_parent_name = "cisco-ia"

        self.output = Checkpoint.Output()
        self.output.parent = self
        self._children_name_map["output"] = "output"
        self._children_yang_names.add("output")


    class Output(Entity):
        """
        
        
        .. attribute:: result
        
        	Output returned by the network element
        	**type**\:  str
        
        

        """

        _prefix = 'cisco-ia'
        _revision = '2017-03-02'

        def __init__(self):
            super(Checkpoint.Output, self).__init__()

            self.yang_name = "output"
            self.yang_parent_name = "checkpoint"

            self.result = YLeaf(YType.str, "result")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("result") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Checkpoint.Output, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Checkpoint.Output, self).__setattr__(name, value)

        def has_data(self):
            return self.result.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.result.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "output" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "cisco-ia:checkpoint/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.result.is_set or self.result.yfilter != YFilter.not_set):
                leaf_name_data.append(self.result.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "result"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "result"):
                self.result = value
                self.result.value_namespace = name_space
                self.result.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (self.output is not None and self.output.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.output is not None and self.output.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "cisco-ia:checkpoint" + path_buffer

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

        if (child_yang_name == "output"):
            if (self.output is None):
                self.output = Checkpoint.Output()
                self.output.parent = self
                self._children_name_map["output"] = "output"
            return self.output

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "output"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Checkpoint()
        return self._top_entity

class Revert(Entity):
    """
    Cancel the timed rollback and trigger the
    rollback immediately, or to reset parameters 
    for the timed rollback
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xe.cisco_ia.Revert.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:   :py:class:`Output <ydk.models.cisco_ios_xe.cisco_ia.Revert.Output>`
    
    

    """

    _prefix = 'cisco-ia'
    _revision = '2017-03-02'

    def __init__(self):
        super(Revert, self).__init__()
        self._top_entity = None

        self.yang_name = "revert"
        self.yang_parent_name = "cisco-ia"

        self.input = Revert.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")

        self.output = Revert.Output()
        self.output.parent = self
        self._children_name_map["output"] = "output"
        self._children_yang_names.add("output")


    class Input(Entity):
        """
        
        
        .. attribute:: idle
        
        	Maximum allowable time period of no activity before reverting to the saved configuration
        	**type**\:  int
        
        	**range:** 1..120
        
        .. attribute:: now
        
        	To cancel the timed rollback and  trigger the rollback immediately
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: timer
        
        	Reset parameters for the timed rollback
        	**type**\:  int
        
        	**range:** 1..120
        
        

        """

        _prefix = 'cisco-ia'
        _revision = '2017-03-02'

        def __init__(self):
            super(Revert.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "revert"

            self.idle = YLeaf(YType.int16, "idle")

            self.now = YLeaf(YType.empty, "now")

            self.timer = YLeaf(YType.int16, "timer")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("idle",
                            "now",
                            "timer") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Revert.Input, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Revert.Input, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.idle.is_set or
                self.now.is_set or
                self.timer.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.idle.yfilter != YFilter.not_set or
                self.now.yfilter != YFilter.not_set or
                self.timer.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "input" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "cisco-ia:revert/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.idle.is_set or self.idle.yfilter != YFilter.not_set):
                leaf_name_data.append(self.idle.get_name_leafdata())
            if (self.now.is_set or self.now.yfilter != YFilter.not_set):
                leaf_name_data.append(self.now.get_name_leafdata())
            if (self.timer.is_set or self.timer.yfilter != YFilter.not_set):
                leaf_name_data.append(self.timer.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "idle" or name == "now" or name == "timer"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "idle"):
                self.idle = value
                self.idle.value_namespace = name_space
                self.idle.value_namespace_prefix = name_space_prefix
            if(value_path == "now"):
                self.now = value
                self.now.value_namespace = name_space
                self.now.value_namespace_prefix = name_space_prefix
            if(value_path == "timer"):
                self.timer = value
                self.timer.value_namespace = name_space
                self.timer.value_namespace_prefix = name_space_prefix


    class Output(Entity):
        """
        
        
        .. attribute:: result
        
        	Output returned by the network element
        	**type**\:  str
        
        

        """

        _prefix = 'cisco-ia'
        _revision = '2017-03-02'

        def __init__(self):
            super(Revert.Output, self).__init__()

            self.yang_name = "output"
            self.yang_parent_name = "revert"

            self.result = YLeaf(YType.str, "result")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("result") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Revert.Output, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Revert.Output, self).__setattr__(name, value)

        def has_data(self):
            return self.result.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.result.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "output" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "cisco-ia:revert/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.result.is_set or self.result.yfilter != YFilter.not_set):
                leaf_name_data.append(self.result.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "result"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "result"):
                self.result = value
                self.result.value_namespace = name_space
                self.result.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (
            (self.input is not None and self.input.has_data()) or
            (self.output is not None and self.output.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.input is not None and self.input.has_operation()) or
            (self.output is not None and self.output.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "cisco-ia:revert" + path_buffer

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
                self.input = Revert.Input()
                self.input.parent = self
                self._children_name_map["input"] = "input"
            return self.input

        if (child_yang_name == "output"):
            if (self.output is None):
                self.output = Revert.Output()
                self.output.parent = self
                self._children_name_map["output"] = "output"
            return self.output

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "input" or name == "output"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Revert()
        return self._top_entity

class Rollback(Entity):
    """
    Replaces the current running configuration 
    file with a saved Cisco IOS XE configuration file.
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xe.cisco_ia.Rollback.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:   :py:class:`Output <ydk.models.cisco_ios_xe.cisco_ia.Rollback.Output>`
    
    

    """

    _prefix = 'cisco-ia'
    _revision = '2017-03-02'

    def __init__(self):
        super(Rollback, self).__init__()
        self._top_entity = None

        self.yang_name = "rollback"
        self.yang_parent_name = "cisco-ia"

        self.input = Rollback.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")

        self.output = Rollback.Output()
        self.output.parent = self
        self._children_name_map["output"] = "output"
        self._children_yang_names.add("output")


    class Input(Entity):
        """
        
        
        .. attribute:: nolock
        
        	Disables the locking of the running  configuration file that prevents other users from changing the running configuration  during a configuration replace operation
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: revert_on_error
        
        	Reverts to the original configuration upon error
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: revert_timer
        
        	Reverts to the original configuration if  specified time elapses
        	**type**\:  int
        
        	**range:** 1..120
        
        .. attribute:: target_url
        
        	Cisco IOS XE configuration file that is to  replace the current running configuration
        	**type**\:  str
        
        	**mandatory**\: True
        
        .. attribute:: verbose
        
        	Display a list of the command lines applied by  the Cisco IOS XE software parser during each pass  of the configuration replace operation. The total  number of passes performed is also displayed
        	**type**\:  bool
        
        	**default value**\: false
        
        

        """

        _prefix = 'cisco-ia'
        _revision = '2017-03-02'

        def __init__(self):
            super(Rollback.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "rollback"

            self.nolock = YLeaf(YType.boolean, "nolock")

            self.revert_on_error = YLeaf(YType.empty, "revert-on-error")

            self.revert_timer = YLeaf(YType.int16, "revert-timer")

            self.target_url = YLeaf(YType.str, "target-url")

            self.verbose = YLeaf(YType.boolean, "verbose")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("nolock",
                            "revert_on_error",
                            "revert_timer",
                            "target_url",
                            "verbose") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Rollback.Input, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Rollback.Input, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.nolock.is_set or
                self.revert_on_error.is_set or
                self.revert_timer.is_set or
                self.target_url.is_set or
                self.verbose.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.nolock.yfilter != YFilter.not_set or
                self.revert_on_error.yfilter != YFilter.not_set or
                self.revert_timer.yfilter != YFilter.not_set or
                self.target_url.yfilter != YFilter.not_set or
                self.verbose.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "input" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "cisco-ia:rollback/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.nolock.is_set or self.nolock.yfilter != YFilter.not_set):
                leaf_name_data.append(self.nolock.get_name_leafdata())
            if (self.revert_on_error.is_set or self.revert_on_error.yfilter != YFilter.not_set):
                leaf_name_data.append(self.revert_on_error.get_name_leafdata())
            if (self.revert_timer.is_set or self.revert_timer.yfilter != YFilter.not_set):
                leaf_name_data.append(self.revert_timer.get_name_leafdata())
            if (self.target_url.is_set or self.target_url.yfilter != YFilter.not_set):
                leaf_name_data.append(self.target_url.get_name_leafdata())
            if (self.verbose.is_set or self.verbose.yfilter != YFilter.not_set):
                leaf_name_data.append(self.verbose.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "nolock" or name == "revert-on-error" or name == "revert-timer" or name == "target-url" or name == "verbose"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "nolock"):
                self.nolock = value
                self.nolock.value_namespace = name_space
                self.nolock.value_namespace_prefix = name_space_prefix
            if(value_path == "revert-on-error"):
                self.revert_on_error = value
                self.revert_on_error.value_namespace = name_space
                self.revert_on_error.value_namespace_prefix = name_space_prefix
            if(value_path == "revert-timer"):
                self.revert_timer = value
                self.revert_timer.value_namespace = name_space
                self.revert_timer.value_namespace_prefix = name_space_prefix
            if(value_path == "target-url"):
                self.target_url = value
                self.target_url.value_namespace = name_space
                self.target_url.value_namespace_prefix = name_space_prefix
            if(value_path == "verbose"):
                self.verbose = value
                self.verbose.value_namespace = name_space
                self.verbose.value_namespace_prefix = name_space_prefix


    class Output(Entity):
        """
        
        
        .. attribute:: result
        
        	Output returned by the network element
        	**type**\:  str
        
        

        """

        _prefix = 'cisco-ia'
        _revision = '2017-03-02'

        def __init__(self):
            super(Rollback.Output, self).__init__()

            self.yang_name = "output"
            self.yang_parent_name = "rollback"

            self.result = YLeaf(YType.str, "result")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("result") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Rollback.Output, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Rollback.Output, self).__setattr__(name, value)

        def has_data(self):
            return self.result.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.result.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "output" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "cisco-ia:rollback/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.result.is_set or self.result.yfilter != YFilter.not_set):
                leaf_name_data.append(self.result.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "result"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "result"):
                self.result = value
                self.result.value_namespace = name_space
                self.result.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (
            (self.input is not None and self.input.has_data()) or
            (self.output is not None and self.output.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.input is not None and self.input.has_operation()) or
            (self.output is not None and self.output.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "cisco-ia:rollback" + path_buffer

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
                self.input = Rollback.Input()
                self.input.parent = self
                self._children_name_map["input"] = "input"
            return self.input

        if (child_yang_name == "output"):
            if (self.output is None):
                self.output = Rollback.Output()
                self.output.parent = self
                self._children_name_map["output"] = "output"
            return self.output

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "input" or name == "output"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Rollback()
        return self._top_entity

