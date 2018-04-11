""" Cisco_IOS_XR_config_cfgmgr_exec_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR config\-cfgmgr\-exec package operational data.

This module contains definitions
for the following management objects\:
  cfg\-hist\-gl\: Configuration History Global path information

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class HistRecord(Enum):
    """
    HistRecord (Enum Class)

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
    	**type**\: list of  		 :py:class:`RecordType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_exec_oper.CfgHistGl.RecordType>`
    
    

    """

    _prefix = 'config-cfgmgr-exec-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(CfgHistGl, self).__init__()
        self._top_entity = None

        self.yang_name = "cfg-hist-gl"
        self.yang_parent_name = "Cisco-IOS-XR-config-cfgmgr-exec-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([])
        self._child_list_classes = OrderedDict([("record-type", ("record_type", CfgHistGl.RecordType))])
        self._leafs = OrderedDict()

        self.record_type = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XR-config-cfgmgr-exec-oper:cfg-hist-gl"

    def __setattr__(self, name, value):
        self._perform_setattr(CfgHistGl, [], name, value)


    class RecordType(Entity):
        """
        History summary information for a specific type
        of history
        
        .. attribute:: record_type  (key)
        
        	Record type
        	**type**\: str
        
        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
        
        .. attribute:: record
        
        	History summary information for a specific type of history
        	**type**\: list of  		 :py:class:`Record <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_exec_oper.CfgHistGl.RecordType.Record>`
        
        

        """

        _prefix = 'config-cfgmgr-exec-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(CfgHistGl.RecordType, self).__init__()

            self.yang_name = "record-type"
            self.yang_parent_name = "cfg-hist-gl"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['record_type']
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("record", ("record", CfgHistGl.RecordType.Record))])
            self._leafs = OrderedDict([
                ('record_type', YLeaf(YType.str, 'record-type')),
            ])
            self.record_type = None

            self.record = YList(self)
            self._segment_path = lambda: "record-type" + "[record-type='" + str(self.record_type) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XR-config-cfgmgr-exec-oper:cfg-hist-gl/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CfgHistGl.RecordType, ['record_type'], name, value)


        class Record(Entity):
            """
            History summary information for a specific type
            of history
            
            .. attribute:: record  (key)
            
            	Record
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: info
            
            	Content of the history
            	**type**\:  :py:class:`Info <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_exec_oper.CfgHistGl.RecordType.Record.Info>`
            
            .. attribute:: timestamp
            
            	Time stamp for the history
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: record_type
            
            	Record type
            	**type**\:  :py:class:`HistRecord <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_exec_oper.HistRecord>`
            
            

            """

            _prefix = 'config-cfgmgr-exec-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(CfgHistGl.RecordType.Record, self).__init__()

                self.yang_name = "record"
                self.yang_parent_name = "record-type"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = ['record']
                self._child_container_classes = OrderedDict([("info", ("info", CfgHistGl.RecordType.Record.Info))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('record', YLeaf(YType.int32, 'record')),
                    ('timestamp', YLeaf(YType.uint32, 'timestamp')),
                    ('record_type', YLeaf(YType.enumeration, 'record-type')),
                ])
                self.record = None
                self.timestamp = None
                self.record_type = None

                self.info = CfgHistGl.RecordType.Record.Info()
                self.info.parent = self
                self._children_name_map["info"] = "info"
                self._children_yang_names.add("info")
                self._segment_path = lambda: "record" + "[record='" + str(self.record) + "']"

            def __setattr__(self, name, value):
                self._perform_setattr(CfgHistGl.RecordType.Record, ['record', 'timestamp', 'record_type'], name, value)


            class Info(Entity):
                """
                Content of the history
                
                .. attribute:: alarm_info
                
                	alarm info
                	**type**\:  :py:class:`AlarmInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_exec_oper.CfgHistGl.RecordType.Record.Info.AlarmInfo>`
                
                .. attribute:: cfscheck_info
                
                	cfscheck info
                	**type**\:  :py:class:`CfscheckInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_exec_oper.CfgHistGl.RecordType.Record.Info.CfscheckInfo>`
                
                .. attribute:: commit_info
                
                	commit info
                	**type**\:  :py:class:`CommitInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_exec_oper.CfgHistGl.RecordType.Record.Info.CommitInfo>`
                
                .. attribute:: oir_info
                
                	oir info
                	**type**\:  :py:class:`OirInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_exec_oper.CfgHistGl.RecordType.Record.Info.OirInfo>`
                
                .. attribute:: shutdown_info
                
                	shutdown info
                	**type**\:  :py:class:`ShutdownInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_exec_oper.CfgHistGl.RecordType.Record.Info.ShutdownInfo>`
                
                .. attribute:: startup_info
                
                	startup info
                	**type**\:  :py:class:`StartupInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_exec_oper.CfgHistGl.RecordType.Record.Info.StartupInfo>`
                
                .. attribute:: backup_info
                
                	backup info
                	**type**\:  :py:class:`BackupInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_exec_oper.CfgHistGl.RecordType.Record.Info.BackupInfo>`
                
                .. attribute:: type
                
                	type
                	**type**\:  :py:class:`HistRecord <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_exec_oper.HistRecord>`
                
                .. attribute:: a
                
                	B
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'config-cfgmgr-exec-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(CfgHistGl.RecordType.Record.Info, self).__init__()

                    self.yang_name = "info"
                    self.yang_parent_name = "record"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("alarm-info", ("alarm_info", CfgHistGl.RecordType.Record.Info.AlarmInfo)), ("cfscheck-info", ("cfscheck_info", CfgHistGl.RecordType.Record.Info.CfscheckInfo)), ("commit-info", ("commit_info", CfgHistGl.RecordType.Record.Info.CommitInfo)), ("oir-info", ("oir_info", CfgHistGl.RecordType.Record.Info.OirInfo)), ("shutdown-info", ("shutdown_info", CfgHistGl.RecordType.Record.Info.ShutdownInfo)), ("startup-info", ("startup_info", CfgHistGl.RecordType.Record.Info.StartupInfo)), ("backup-info", ("backup_info", CfgHistGl.RecordType.Record.Info.BackupInfo))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('type', YLeaf(YType.enumeration, 'type')),
                        ('a', YLeaf(YType.uint32, 'a')),
                    ])
                    self.type = None
                    self.a = None

                    self.alarm_info = CfgHistGl.RecordType.Record.Info.AlarmInfo()
                    self.alarm_info.parent = self
                    self._children_name_map["alarm_info"] = "alarm-info"
                    self._children_yang_names.add("alarm-info")

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

                    self.backup_info = CfgHistGl.RecordType.Record.Info.BackupInfo()
                    self.backup_info.parent = self
                    self._children_name_map["backup_info"] = "backup-info"
                    self._children_yang_names.add("backup-info")
                    self._segment_path = lambda: "info"

                def __setattr__(self, name, value):
                    self._perform_setattr(CfgHistGl.RecordType.Record.Info, ['type', 'a'], name, value)


                class AlarmInfo(Entity):
                    """
                    alarm info
                    
                    .. attribute:: state
                    
                    	State
                    	**type**\: str
                    
                    .. attribute:: where
                    
                    	Where
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'config-cfgmgr-exec-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(CfgHistGl.RecordType.Record.Info.AlarmInfo, self).__init__()

                        self.yang_name = "alarm-info"
                        self.yang_parent_name = "info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('state', YLeaf(YType.str, 'state')),
                            ('where', YLeaf(YType.str, 'where')),
                        ])
                        self.state = None
                        self.where = None
                        self._segment_path = lambda: "alarm-info"

                    def __setattr__(self, name, value):
                        self._perform_setattr(CfgHistGl.RecordType.Record.Info.AlarmInfo, ['state', 'where'], name, value)


                class CfscheckInfo(Entity):
                    """
                    cfscheck info
                    
                    .. attribute:: user_id
                    
                    	UserId
                    	**type**\: str
                    
                    .. attribute:: line
                    
                    	Line
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'config-cfgmgr-exec-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(CfgHistGl.RecordType.Record.Info.CfscheckInfo, self).__init__()

                        self.yang_name = "cfscheck-info"
                        self.yang_parent_name = "info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('user_id', YLeaf(YType.str, 'user-id')),
                            ('line', YLeaf(YType.str, 'line')),
                        ])
                        self.user_id = None
                        self.line = None
                        self._segment_path = lambda: "cfscheck-info"

                    def __setattr__(self, name, value):
                        self._perform_setattr(CfgHistGl.RecordType.Record.Info.CfscheckInfo, ['user_id', 'line'], name, value)


                class CommitInfo(Entity):
                    """
                    commit info
                    
                    .. attribute:: commit_id
                    
                    	CommitId
                    	**type**\: str
                    
                    .. attribute:: user_id
                    
                    	UserId
                    	**type**\: str
                    
                    .. attribute:: line
                    
                    	Line
                    	**type**\: str
                    
                    .. attribute:: client_name
                    
                    	Client name
                    	**type**\: str
                    
                    .. attribute:: label
                    
                    	Label
                    	**type**\: str
                    
                    .. attribute:: comment
                    
                    	Comment
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'config-cfgmgr-exec-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(CfgHistGl.RecordType.Record.Info.CommitInfo, self).__init__()

                        self.yang_name = "commit-info"
                        self.yang_parent_name = "info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('commit_id', YLeaf(YType.str, 'commit-id')),
                            ('user_id', YLeaf(YType.str, 'user-id')),
                            ('line', YLeaf(YType.str, 'line')),
                            ('client_name', YLeaf(YType.str, 'client-name')),
                            ('label', YLeaf(YType.str, 'label')),
                            ('comment', YLeaf(YType.str, 'comment')),
                        ])
                        self.commit_id = None
                        self.user_id = None
                        self.line = None
                        self.client_name = None
                        self.label = None
                        self.comment = None
                        self._segment_path = lambda: "commit-info"

                    def __setattr__(self, name, value):
                        self._perform_setattr(CfgHistGl.RecordType.Record.Info.CommitInfo, ['commit_id', 'user_id', 'line', 'client_name', 'label', 'comment'], name, value)


                class OirInfo(Entity):
                    """
                    oir info
                    
                    .. attribute:: config_type
                    
                    	Config Type
                    	**type**\: str
                    
                    .. attribute:: operation_
                    
                    	Operation
                    	**type**\: str
                    
                    .. attribute:: config_name
                    
                    	Config Name
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'config-cfgmgr-exec-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(CfgHistGl.RecordType.Record.Info.OirInfo, self).__init__()

                        self.yang_name = "oir-info"
                        self.yang_parent_name = "info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('config_type', YLeaf(YType.str, 'config-type')),
                            ('operation_', YLeaf(YType.str, 'operation')),
                            ('config_name', YLeaf(YType.str, 'config-name')),
                        ])
                        self.config_type = None
                        self.operation_ = None
                        self.config_name = None
                        self._segment_path = lambda: "oir-info"

                    def __setattr__(self, name, value):
                        self._perform_setattr(CfgHistGl.RecordType.Record.Info.OirInfo, ['config_type', 'operation_', 'config_name'], name, value)


                class ShutdownInfo(Entity):
                    """
                    shutdown info
                    
                    .. attribute:: comment
                    
                    	Comment
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'config-cfgmgr-exec-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(CfgHistGl.RecordType.Record.Info.ShutdownInfo, self).__init__()

                        self.yang_name = "shutdown-info"
                        self.yang_parent_name = "info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('comment', YLeaf(YType.str, 'comment')),
                        ])
                        self.comment = None
                        self._segment_path = lambda: "shutdown-info"

                    def __setattr__(self, name, value):
                        self._perform_setattr(CfgHistGl.RecordType.Record.Info.ShutdownInfo, ['comment'], name, value)


                class StartupInfo(Entity):
                    """
                    startup info
                    
                    .. attribute:: how_booted
                    
                    	How Booted
                    	**type**\: str
                    
                    .. attribute:: boot_path
                    
                    	Boot Path
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'config-cfgmgr-exec-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(CfgHistGl.RecordType.Record.Info.StartupInfo, self).__init__()

                        self.yang_name = "startup-info"
                        self.yang_parent_name = "info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('how_booted', YLeaf(YType.str, 'how-booted')),
                            ('boot_path', YLeaf(YType.str, 'boot-path')),
                        ])
                        self.how_booted = None
                        self.boot_path = None
                        self._segment_path = lambda: "startup-info"

                    def __setattr__(self, name, value):
                        self._perform_setattr(CfgHistGl.RecordType.Record.Info.StartupInfo, ['how_booted', 'boot_path'], name, value)


                class BackupInfo(Entity):
                    """
                    backup info
                    
                    .. attribute:: comment
                    
                    	Comment
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'config-cfgmgr-exec-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(CfgHistGl.RecordType.Record.Info.BackupInfo, self).__init__()

                        self.yang_name = "backup-info"
                        self.yang_parent_name = "info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('comment', YLeaf(YType.str, 'comment')),
                        ])
                        self.comment = None
                        self._segment_path = lambda: "backup-info"

                    def __setattr__(self, name, value):
                        self._perform_setattr(CfgHistGl.RecordType.Record.Info.BackupInfo, ['comment'], name, value)

    def clone_ptr(self):
        self._top_entity = CfgHistGl()
        return self._top_entity

