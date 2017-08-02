""" Cisco_IOS_XR_config_cfgmgr_exec_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR config\-cfgmgr\-exec package operational data.

This module contains definitions
for the following management objects\:
  cfg\-hist\-gl\: Configuration History Global path information

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class HistRecord(Enum):
    """
    HistRecord

    Possible types of history

    .. data:: cfghist_bag_record_all = 0

    	All history

    .. data:: cfghist_bag_record_alarm = 1

    	Alarm history

    .. data:: cfghist_bag_record_cfs_check = 2

    	CfgCheck history

    .. data:: cfghist_bag_record_commit = 3

    	Commit history

    .. data:: cfghist_bag_record_oir = 4

    	OIR history

    .. data:: cfghist_bag_record_shutdown = 5

    	Shutdown history

    .. data:: cfghist_bag_record_startup = 6

    	Bootup history

    .. data:: cfghist_bag_record_backup = 7

    	Backup history

    .. data:: cfghist_bag_record_rebase = 8

    	Rebase history

    .. data:: cfghist_bag_record_last = 9

    	Last history

    """

    cfghist_bag_record_all = Enum.YLeaf(0, "cfghist-bag-record-all")

    cfghist_bag_record_alarm = Enum.YLeaf(1, "cfghist-bag-record-alarm")

    cfghist_bag_record_cfs_check = Enum.YLeaf(2, "cfghist-bag-record-cfs-check")

    cfghist_bag_record_commit = Enum.YLeaf(3, "cfghist-bag-record-commit")

    cfghist_bag_record_oir = Enum.YLeaf(4, "cfghist-bag-record-oir")

    cfghist_bag_record_shutdown = Enum.YLeaf(5, "cfghist-bag-record-shutdown")

    cfghist_bag_record_startup = Enum.YLeaf(6, "cfghist-bag-record-startup")

    cfghist_bag_record_backup = Enum.YLeaf(7, "cfghist-bag-record-backup")

    cfghist_bag_record_rebase = Enum.YLeaf(8, "cfghist-bag-record-rebase")

    cfghist_bag_record_last = Enum.YLeaf(9, "cfghist-bag-record-last")



class CfgHistGl(Entity):
    """
    Configuration History Global path information
    
    .. attribute:: record_type
    
    	History summary information for a specific type of history
    	**type**\: list of    :py:class:`RecordType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_exec_oper.CfgHistGl.RecordType>`
    
    

    """

    _prefix = 'config-cfgmgr-exec-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(CfgHistGl, self).__init__()
        self._top_entity = None

        self.yang_name = "cfg-hist-gl"
        self.yang_parent_name = "Cisco-IOS-XR-config-cfgmgr-exec-oper"

        self.record_type = YList(self)

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
                    super(CfgHistGl, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(CfgHistGl, self).__setattr__(name, value)


    class RecordType(Entity):
        """
        History summary information for a specific type
        of history
        
        .. attribute:: record_type  <key>
        
        	Record type
        	**type**\:  str
        
        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
        
        .. attribute:: record
        
        	History summary information for a specific type of history
        	**type**\: list of    :py:class:`Record <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_exec_oper.CfgHistGl.RecordType.Record>`
        
        

        """

        _prefix = 'config-cfgmgr-exec-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(CfgHistGl.RecordType, self).__init__()

            self.yang_name = "record-type"
            self.yang_parent_name = "cfg-hist-gl"

            self.record_type = YLeaf(YType.str, "record-type")

            self.record = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("record_type") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CfgHistGl.RecordType, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CfgHistGl.RecordType, self).__setattr__(name, value)


        class Record(Entity):
            """
            History summary information for a specific type
            of history
            
            .. attribute:: record  <key>
            
            	Record
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: info
            
            	Content of the history
            	**type**\:   :py:class:`Info <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_exec_oper.CfgHistGl.RecordType.Record.Info>`
            
            .. attribute:: record_type
            
            	Record type
            	**type**\:   :py:class:`HistRecord <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_exec_oper.HistRecord>`
            
            .. attribute:: timestamp
            
            	Time stamp for the history
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'config-cfgmgr-exec-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(CfgHistGl.RecordType.Record, self).__init__()

                self.yang_name = "record"
                self.yang_parent_name = "record-type"

                self.record = YLeaf(YType.int32, "record")

                self.record_type = YLeaf(YType.enumeration, "record-type")

                self.timestamp = YLeaf(YType.uint32, "timestamp")

                self.info = CfgHistGl.RecordType.Record.Info()
                self.info.parent = self
                self._children_name_map["info"] = "info"
                self._children_yang_names.add("info")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("record",
                                "record_type",
                                "timestamp") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CfgHistGl.RecordType.Record, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CfgHistGl.RecordType.Record, self).__setattr__(name, value)


            class Info(Entity):
                """
                Content of the history
                
                .. attribute:: a
                
                	B
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: alarm_info
                
                	alarm info
                	**type**\:   :py:class:`AlarmInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_exec_oper.CfgHistGl.RecordType.Record.Info.AlarmInfo>`
                
                .. attribute:: backup_info
                
                	backup info
                	**type**\:   :py:class:`BackupInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_exec_oper.CfgHistGl.RecordType.Record.Info.BackupInfo>`
                
                .. attribute:: cfscheck_info
                
                	cfscheck info
                	**type**\:   :py:class:`CfscheckInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_exec_oper.CfgHistGl.RecordType.Record.Info.CfscheckInfo>`
                
                .. attribute:: commit_info
                
                	commit info
                	**type**\:   :py:class:`CommitInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_exec_oper.CfgHistGl.RecordType.Record.Info.CommitInfo>`
                
                .. attribute:: oir_info
                
                	oir info
                	**type**\:   :py:class:`OirInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_exec_oper.CfgHistGl.RecordType.Record.Info.OirInfo>`
                
                .. attribute:: shutdown_info
                
                	shutdown info
                	**type**\:   :py:class:`ShutdownInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_exec_oper.CfgHistGl.RecordType.Record.Info.ShutdownInfo>`
                
                .. attribute:: startup_info
                
                	startup info
                	**type**\:   :py:class:`StartupInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_exec_oper.CfgHistGl.RecordType.Record.Info.StartupInfo>`
                
                .. attribute:: type
                
                	type
                	**type**\:   :py:class:`HistRecord <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_exec_oper.HistRecord>`
                
                

                """

                _prefix = 'config-cfgmgr-exec-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(CfgHistGl.RecordType.Record.Info, self).__init__()

                    self.yang_name = "info"
                    self.yang_parent_name = "record"

                    self.a = YLeaf(YType.uint32, "a")

                    self.type = YLeaf(YType.enumeration, "type")

                    self.alarm_info = CfgHistGl.RecordType.Record.Info.AlarmInfo()
                    self.alarm_info.parent = self
                    self._children_name_map["alarm_info"] = "alarm-info"
                    self._children_yang_names.add("alarm-info")

                    self.backup_info = CfgHistGl.RecordType.Record.Info.BackupInfo()
                    self.backup_info.parent = self
                    self._children_name_map["backup_info"] = "backup-info"
                    self._children_yang_names.add("backup-info")

                    self.cfscheck_info = CfgHistGl.RecordType.Record.Info.CfscheckInfo()
                    self.cfscheck_info.parent = self
                    self._children_name_map["cfscheck_info"] = "cfscheck-info"
                    self._children_yang_names.add("cfscheck-info")

                    self.commit_info = CfgHistGl.RecordType.Record.Info.CommitInfo()
                    self.commit_info.parent = self
                    self._children_name_map["commit_info"] = "commit-info"
                    self._children_yang_names.add("commit-info")

                    self.oir_info = CfgHistGl.RecordType.Record.Info.OirInfo()
                    self.oir_info.parent = self
                    self._children_name_map["oir_info"] = "oir-info"
                    self._children_yang_names.add("oir-info")

                    self.shutdown_info = CfgHistGl.RecordType.Record.Info.ShutdownInfo()
                    self.shutdown_info.parent = self
                    self._children_name_map["shutdown_info"] = "shutdown-info"
                    self._children_yang_names.add("shutdown-info")

                    self.startup_info = CfgHistGl.RecordType.Record.Info.StartupInfo()
                    self.startup_info.parent = self
                    self._children_name_map["startup_info"] = "startup-info"
                    self._children_yang_names.add("startup-info")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("a",
                                    "type") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(CfgHistGl.RecordType.Record.Info, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(CfgHistGl.RecordType.Record.Info, self).__setattr__(name, value)


                class AlarmInfo(Entity):
                    """
                    alarm info
                    
                    .. attribute:: state
                    
                    	State
                    	**type**\:  str
                    
                    .. attribute:: where
                    
                    	Where
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'config-cfgmgr-exec-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(CfgHistGl.RecordType.Record.Info.AlarmInfo, self).__init__()

                        self.yang_name = "alarm-info"
                        self.yang_parent_name = "info"

                        self.state = YLeaf(YType.str, "state")

                        self.where = YLeaf(YType.str, "where")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("state",
                                        "where") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(CfgHistGl.RecordType.Record.Info.AlarmInfo, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(CfgHistGl.RecordType.Record.Info.AlarmInfo, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.state.is_set or
                            self.where.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.state.yfilter != YFilter.not_set or
                            self.where.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "alarm-info" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.state.is_set or self.state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.state.get_name_leafdata())
                        if (self.where.is_set or self.where.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.where.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "state" or name == "where"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "state"):
                            self.state = value
                            self.state.value_namespace = name_space
                            self.state.value_namespace_prefix = name_space_prefix
                        if(value_path == "where"):
                            self.where = value
                            self.where.value_namespace = name_space
                            self.where.value_namespace_prefix = name_space_prefix


                class CfscheckInfo(Entity):
                    """
                    cfscheck info
                    
                    .. attribute:: line
                    
                    	Line
                    	**type**\:  str
                    
                    .. attribute:: user_id
                    
                    	UserId
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'config-cfgmgr-exec-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(CfgHistGl.RecordType.Record.Info.CfscheckInfo, self).__init__()

                        self.yang_name = "cfscheck-info"
                        self.yang_parent_name = "info"

                        self.line = YLeaf(YType.str, "line")

                        self.user_id = YLeaf(YType.str, "user-id")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("line",
                                        "user_id") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(CfgHistGl.RecordType.Record.Info.CfscheckInfo, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(CfgHistGl.RecordType.Record.Info.CfscheckInfo, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.line.is_set or
                            self.user_id.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.line.yfilter != YFilter.not_set or
                            self.user_id.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "cfscheck-info" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.line.is_set or self.line.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.line.get_name_leafdata())
                        if (self.user_id.is_set or self.user_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.user_id.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "line" or name == "user-id"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "line"):
                            self.line = value
                            self.line.value_namespace = name_space
                            self.line.value_namespace_prefix = name_space_prefix
                        if(value_path == "user-id"):
                            self.user_id = value
                            self.user_id.value_namespace = name_space
                            self.user_id.value_namespace_prefix = name_space_prefix


                class CommitInfo(Entity):
                    """
                    commit info
                    
                    .. attribute:: client_name
                    
                    	Client name
                    	**type**\:  str
                    
                    .. attribute:: comment
                    
                    	Comment
                    	**type**\:  str
                    
                    .. attribute:: commit_id
                    
                    	CommitId
                    	**type**\:  str
                    
                    .. attribute:: label
                    
                    	Label
                    	**type**\:  str
                    
                    .. attribute:: line
                    
                    	Line
                    	**type**\:  str
                    
                    .. attribute:: user_id
                    
                    	UserId
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'config-cfgmgr-exec-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(CfgHistGl.RecordType.Record.Info.CommitInfo, self).__init__()

                        self.yang_name = "commit-info"
                        self.yang_parent_name = "info"

                        self.client_name = YLeaf(YType.str, "client-name")

                        self.comment = YLeaf(YType.str, "comment")

                        self.commit_id = YLeaf(YType.str, "commit-id")

                        self.label = YLeaf(YType.str, "label")

                        self.line = YLeaf(YType.str, "line")

                        self.user_id = YLeaf(YType.str, "user-id")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("client_name",
                                        "comment",
                                        "commit_id",
                                        "label",
                                        "line",
                                        "user_id") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(CfgHistGl.RecordType.Record.Info.CommitInfo, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(CfgHistGl.RecordType.Record.Info.CommitInfo, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.client_name.is_set or
                            self.comment.is_set or
                            self.commit_id.is_set or
                            self.label.is_set or
                            self.line.is_set or
                            self.user_id.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.client_name.yfilter != YFilter.not_set or
                            self.comment.yfilter != YFilter.not_set or
                            self.commit_id.yfilter != YFilter.not_set or
                            self.label.yfilter != YFilter.not_set or
                            self.line.yfilter != YFilter.not_set or
                            self.user_id.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "commit-info" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.client_name.is_set or self.client_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.client_name.get_name_leafdata())
                        if (self.comment.is_set or self.comment.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.comment.get_name_leafdata())
                        if (self.commit_id.is_set or self.commit_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.commit_id.get_name_leafdata())
                        if (self.label.is_set or self.label.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.label.get_name_leafdata())
                        if (self.line.is_set or self.line.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.line.get_name_leafdata())
                        if (self.user_id.is_set or self.user_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.user_id.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "client-name" or name == "comment" or name == "commit-id" or name == "label" or name == "line" or name == "user-id"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "client-name"):
                            self.client_name = value
                            self.client_name.value_namespace = name_space
                            self.client_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "comment"):
                            self.comment = value
                            self.comment.value_namespace = name_space
                            self.comment.value_namespace_prefix = name_space_prefix
                        if(value_path == "commit-id"):
                            self.commit_id = value
                            self.commit_id.value_namespace = name_space
                            self.commit_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "label"):
                            self.label = value
                            self.label.value_namespace = name_space
                            self.label.value_namespace_prefix = name_space_prefix
                        if(value_path == "line"):
                            self.line = value
                            self.line.value_namespace = name_space
                            self.line.value_namespace_prefix = name_space_prefix
                        if(value_path == "user-id"):
                            self.user_id = value
                            self.user_id.value_namespace = name_space
                            self.user_id.value_namespace_prefix = name_space_prefix


                class OirInfo(Entity):
                    """
                    oir info
                    
                    .. attribute:: config_name
                    
                    	Config Name
                    	**type**\:  str
                    
                    .. attribute:: config_type
                    
                    	Config Type
                    	**type**\:  str
                    
                    .. attribute:: operation_
                    
                    	Operation
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'config-cfgmgr-exec-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(CfgHistGl.RecordType.Record.Info.OirInfo, self).__init__()

                        self.yang_name = "oir-info"
                        self.yang_parent_name = "info"

                        self.config_name = YLeaf(YType.str, "config-name")

                        self.config_type = YLeaf(YType.str, "config-type")

                        self.operation_ = YLeaf(YType.str, "operation")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("config_name",
                                        "config_type",
                                        "operation_") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(CfgHistGl.RecordType.Record.Info.OirInfo, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(CfgHistGl.RecordType.Record.Info.OirInfo, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.config_name.is_set or
                            self.config_type.is_set or
                            self.operation_.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.config_name.yfilter != YFilter.not_set or
                            self.config_type.yfilter != YFilter.not_set or
                            self.operation_.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "oir-info" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.config_name.is_set or self.config_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.config_name.get_name_leafdata())
                        if (self.config_type.is_set or self.config_type.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.config_type.get_name_leafdata())
                        if (self.operation_.is_set or self.operation_.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.operation_.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "config-name" or name == "config-type" or name == "operation"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "config-name"):
                            self.config_name = value
                            self.config_name.value_namespace = name_space
                            self.config_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "config-type"):
                            self.config_type = value
                            self.config_type.value_namespace = name_space
                            self.config_type.value_namespace_prefix = name_space_prefix
                        if(value_path == "operation"):
                            self.operation_ = value
                            self.operation_.value_namespace = name_space
                            self.operation_.value_namespace_prefix = name_space_prefix


                class ShutdownInfo(Entity):
                    """
                    shutdown info
                    
                    .. attribute:: comment
                    
                    	Comment
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'config-cfgmgr-exec-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(CfgHistGl.RecordType.Record.Info.ShutdownInfo, self).__init__()

                        self.yang_name = "shutdown-info"
                        self.yang_parent_name = "info"

                        self.comment = YLeaf(YType.str, "comment")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("comment") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(CfgHistGl.RecordType.Record.Info.ShutdownInfo, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(CfgHistGl.RecordType.Record.Info.ShutdownInfo, self).__setattr__(name, value)

                    def has_data(self):
                        return self.comment.is_set

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.comment.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "shutdown-info" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.comment.is_set or self.comment.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.comment.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "comment"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "comment"):
                            self.comment = value
                            self.comment.value_namespace = name_space
                            self.comment.value_namespace_prefix = name_space_prefix


                class StartupInfo(Entity):
                    """
                    startup info
                    
                    .. attribute:: boot_path
                    
                    	Boot Path
                    	**type**\:  str
                    
                    .. attribute:: how_booted
                    
                    	How Booted
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'config-cfgmgr-exec-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(CfgHistGl.RecordType.Record.Info.StartupInfo, self).__init__()

                        self.yang_name = "startup-info"
                        self.yang_parent_name = "info"

                        self.boot_path = YLeaf(YType.str, "boot-path")

                        self.how_booted = YLeaf(YType.str, "how-booted")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("boot_path",
                                        "how_booted") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(CfgHistGl.RecordType.Record.Info.StartupInfo, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(CfgHistGl.RecordType.Record.Info.StartupInfo, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.boot_path.is_set or
                            self.how_booted.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.boot_path.yfilter != YFilter.not_set or
                            self.how_booted.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "startup-info" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.boot_path.is_set or self.boot_path.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.boot_path.get_name_leafdata())
                        if (self.how_booted.is_set or self.how_booted.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.how_booted.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "boot-path" or name == "how-booted"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "boot-path"):
                            self.boot_path = value
                            self.boot_path.value_namespace = name_space
                            self.boot_path.value_namespace_prefix = name_space_prefix
                        if(value_path == "how-booted"):
                            self.how_booted = value
                            self.how_booted.value_namespace = name_space
                            self.how_booted.value_namespace_prefix = name_space_prefix


                class BackupInfo(Entity):
                    """
                    backup info
                    
                    .. attribute:: comment
                    
                    	Comment
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'config-cfgmgr-exec-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(CfgHistGl.RecordType.Record.Info.BackupInfo, self).__init__()

                        self.yang_name = "backup-info"
                        self.yang_parent_name = "info"

                        self.comment = YLeaf(YType.str, "comment")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("comment") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(CfgHistGl.RecordType.Record.Info.BackupInfo, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(CfgHistGl.RecordType.Record.Info.BackupInfo, self).__setattr__(name, value)

                    def has_data(self):
                        return self.comment.is_set

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.comment.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "backup-info" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.comment.is_set or self.comment.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.comment.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "comment"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "comment"):
                            self.comment = value
                            self.comment.value_namespace = name_space
                            self.comment.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.a.is_set or
                        self.type.is_set or
                        (self.alarm_info is not None and self.alarm_info.has_data()) or
                        (self.backup_info is not None and self.backup_info.has_data()) or
                        (self.cfscheck_info is not None and self.cfscheck_info.has_data()) or
                        (self.commit_info is not None and self.commit_info.has_data()) or
                        (self.oir_info is not None and self.oir_info.has_data()) or
                        (self.shutdown_info is not None and self.shutdown_info.has_data()) or
                        (self.startup_info is not None and self.startup_info.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.a.yfilter != YFilter.not_set or
                        self.type.yfilter != YFilter.not_set or
                        (self.alarm_info is not None and self.alarm_info.has_operation()) or
                        (self.backup_info is not None and self.backup_info.has_operation()) or
                        (self.cfscheck_info is not None and self.cfscheck_info.has_operation()) or
                        (self.commit_info is not None and self.commit_info.has_operation()) or
                        (self.oir_info is not None and self.oir_info.has_operation()) or
                        (self.shutdown_info is not None and self.shutdown_info.has_operation()) or
                        (self.startup_info is not None and self.startup_info.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "info" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.a.is_set or self.a.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.a.get_name_leafdata())
                    if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.type.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "alarm-info"):
                        if (self.alarm_info is None):
                            self.alarm_info = CfgHistGl.RecordType.Record.Info.AlarmInfo()
                            self.alarm_info.parent = self
                            self._children_name_map["alarm_info"] = "alarm-info"
                        return self.alarm_info

                    if (child_yang_name == "backup-info"):
                        if (self.backup_info is None):
                            self.backup_info = CfgHistGl.RecordType.Record.Info.BackupInfo()
                            self.backup_info.parent = self
                            self._children_name_map["backup_info"] = "backup-info"
                        return self.backup_info

                    if (child_yang_name == "cfscheck-info"):
                        if (self.cfscheck_info is None):
                            self.cfscheck_info = CfgHistGl.RecordType.Record.Info.CfscheckInfo()
                            self.cfscheck_info.parent = self
                            self._children_name_map["cfscheck_info"] = "cfscheck-info"
                        return self.cfscheck_info

                    if (child_yang_name == "commit-info"):
                        if (self.commit_info is None):
                            self.commit_info = CfgHistGl.RecordType.Record.Info.CommitInfo()
                            self.commit_info.parent = self
                            self._children_name_map["commit_info"] = "commit-info"
                        return self.commit_info

                    if (child_yang_name == "oir-info"):
                        if (self.oir_info is None):
                            self.oir_info = CfgHistGl.RecordType.Record.Info.OirInfo()
                            self.oir_info.parent = self
                            self._children_name_map["oir_info"] = "oir-info"
                        return self.oir_info

                    if (child_yang_name == "shutdown-info"):
                        if (self.shutdown_info is None):
                            self.shutdown_info = CfgHistGl.RecordType.Record.Info.ShutdownInfo()
                            self.shutdown_info.parent = self
                            self._children_name_map["shutdown_info"] = "shutdown-info"
                        return self.shutdown_info

                    if (child_yang_name == "startup-info"):
                        if (self.startup_info is None):
                            self.startup_info = CfgHistGl.RecordType.Record.Info.StartupInfo()
                            self.startup_info.parent = self
                            self._children_name_map["startup_info"] = "startup-info"
                        return self.startup_info

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "alarm-info" or name == "backup-info" or name == "cfscheck-info" or name == "commit-info" or name == "oir-info" or name == "shutdown-info" or name == "startup-info" or name == "a" or name == "type"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "a"):
                        self.a = value
                        self.a.value_namespace = name_space
                        self.a.value_namespace_prefix = name_space_prefix
                    if(value_path == "type"):
                        self.type = value
                        self.type.value_namespace = name_space
                        self.type.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.record.is_set or
                    self.record_type.is_set or
                    self.timestamp.is_set or
                    (self.info is not None and self.info.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.record.yfilter != YFilter.not_set or
                    self.record_type.yfilter != YFilter.not_set or
                    self.timestamp.yfilter != YFilter.not_set or
                    (self.info is not None and self.info.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "record" + "[record='" + self.record.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.record.is_set or self.record.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.record.get_name_leafdata())
                if (self.record_type.is_set or self.record_type.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.record_type.get_name_leafdata())
                if (self.timestamp.is_set or self.timestamp.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.timestamp.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "info"):
                    if (self.info is None):
                        self.info = CfgHistGl.RecordType.Record.Info()
                        self.info.parent = self
                        self._children_name_map["info"] = "info"
                    return self.info

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "info" or name == "record" or name == "record-type" or name == "timestamp"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "record"):
                    self.record = value
                    self.record.value_namespace = name_space
                    self.record.value_namespace_prefix = name_space_prefix
                if(value_path == "record-type"):
                    self.record_type = value
                    self.record_type.value_namespace = name_space
                    self.record_type.value_namespace_prefix = name_space_prefix
                if(value_path == "timestamp"):
                    self.timestamp = value
                    self.timestamp.value_namespace = name_space
                    self.timestamp.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.record:
                if (c.has_data()):
                    return True
            return self.record_type.is_set

        def has_operation(self):
            for c in self.record:
                if (c.has_operation()):
                    return True
            return (
                self.yfilter != YFilter.not_set or
                self.record_type.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "record-type" + "[record-type='" + self.record_type.get() + "']" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-config-cfgmgr-exec-oper:cfg-hist-gl/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.record_type.is_set or self.record_type.yfilter != YFilter.not_set):
                leaf_name_data.append(self.record_type.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "record"):
                for c in self.record:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CfgHistGl.RecordType.Record()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.record.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "record" or name == "record-type"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "record-type"):
                self.record_type = value
                self.record_type.value_namespace = name_space
                self.record_type.value_namespace_prefix = name_space_prefix

    def has_data(self):
        for c in self.record_type:
            if (c.has_data()):
                return True
        return False

    def has_operation(self):
        for c in self.record_type:
            if (c.has_operation()):
                return True
        return self.yfilter != YFilter.not_set

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-config-cfgmgr-exec-oper:cfg-hist-gl" + path_buffer

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

        if (child_yang_name == "record-type"):
            for c in self.record_type:
                segment = c.get_segment_path()
                if (segment_path == segment):
                    return c
            c = CfgHistGl.RecordType()
            c.parent = self
            local_reference_key = "ydk::seg::%s" % segment_path
            self._local_refs[local_reference_key] = c
            self.record_type.append(c)
            return c

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "record-type"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CfgHistGl()
        return self._top_entity

