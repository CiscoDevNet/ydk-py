""" Cisco_IOS_XR_config_cfgmgr_exec_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR config\-cfgmgr\-exec package operational data.

This module contains definitions
for the following management objects\:
  config\-manager\: Show Configuration <\*> Global path information

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
import sys
from collections import OrderedDict

from ydk.types import Entity as _Entity_
from ydk.types import EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
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


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_cfgmgr_exec_oper as meta
        return meta._meta_table['HistRecord']



class ConfigManager(_Entity_):
    """
    Show Configuration <\*> Global path information
    
    .. attribute:: global_
    
    	Show Configuration <\*> Global path information
    	**type**\:  :py:class:`Global <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_exec_oper.ConfigManager.Global>`
    
    	**config**\: False
    
    

    """

    _prefix = 'config-cfgmgr-exec-oper'
    _revision = '2017-09-07'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(ConfigManager, self).__init__()
        self._top_entity = None

        self.yang_name = "config-manager"
        self.yang_parent_name = "Cisco-IOS-XR-config-cfgmgr-exec-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("global", ("global_", ConfigManager.Global))])
        self._leafs = OrderedDict()

        self.global_ = ConfigManager.Global()
        self.global_.parent = self
        self._children_name_map["global_"] = "global"
        self._segment_path = lambda: "Cisco-IOS-XR-config-cfgmgr-exec-oper:config-manager"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(ConfigManager, [], name, value)


    class Global(_Entity_):
        """
        Show Configuration <\*> Global path information
        
        .. attribute:: config_commit
        
        	Show Configuration Commit <\*> Global path information
        	**type**\:  :py:class:`ConfigCommit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_exec_oper.ConfigManager.Global.ConfigCommit>`
        
        	**config**\: False
        
        .. attribute:: history_tables
        
        	Show Configuration History <\*> Global path information
        	**type**\:  :py:class:`HistoryTables <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_exec_oper.ConfigManager.Global.HistoryTables>`
        
        	**config**\: False
        
        .. attribute:: config_session
        
        	Show Configuration Session <\*> Global path information
        	**type**\:  :py:class:`ConfigSession <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_exec_oper.ConfigManager.Global.ConfigSession>`
        
        	**config**\: False
        
        

        """

        _prefix = 'config-cfgmgr-exec-oper'
        _revision = '2017-09-07'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(ConfigManager.Global, self).__init__()

            self.yang_name = "global"
            self.yang_parent_name = "config-manager"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("config-commit", ("config_commit", ConfigManager.Global.ConfigCommit)), ("history-tables", ("history_tables", ConfigManager.Global.HistoryTables)), ("config-session", ("config_session", ConfigManager.Global.ConfigSession))])
            self._leafs = OrderedDict()

            self.config_commit = ConfigManager.Global.ConfigCommit()
            self.config_commit.parent = self
            self._children_name_map["config_commit"] = "config-commit"

            self.history_tables = ConfigManager.Global.HistoryTables()
            self.history_tables.parent = self
            self._children_name_map["history_tables"] = "history-tables"

            self.config_session = ConfigManager.Global.ConfigSession()
            self.config_session.parent = self
            self._children_name_map["config_session"] = "config-session"
            self._segment_path = lambda: "global"
            self._absolute_path = lambda: "Cisco-IOS-XR-config-cfgmgr-exec-oper:config-manager/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(ConfigManager.Global, [], name, value)


        class ConfigCommit(_Entity_):
            """
            Show Configuration Commit <\*> Global path
            information
            
            .. attribute:: commits
            
            	Show Configuration Commit List Detail
            	**type**\:  :py:class:`Commits <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_exec_oper.ConfigManager.Global.ConfigCommit.Commits>`
            
            	**config**\: False
            
            

            """

            _prefix = 'config-cfgmgr-exec-oper'
            _revision = '2017-09-07'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(ConfigManager.Global.ConfigCommit, self).__init__()

                self.yang_name = "config-commit"
                self.yang_parent_name = "global"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("commits", ("commits", ConfigManager.Global.ConfigCommit.Commits))])
                self._leafs = OrderedDict()

                self.commits = ConfigManager.Global.ConfigCommit.Commits()
                self.commits.parent = self
                self._children_name_map["commits"] = "commits"
                self._segment_path = lambda: "config-commit"
                self._absolute_path = lambda: "Cisco-IOS-XR-config-cfgmgr-exec-oper:config-manager/global/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(ConfigManager.Global.ConfigCommit, [], name, value)


            class Commits(_Entity_):
                """
                Show Configuration Commit List Detail
                
                .. attribute:: commit
                
                	Commit information for a specific commit entry
                	**type**\: list of  		 :py:class:`Commit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_exec_oper.ConfigManager.Global.ConfigCommit.Commits.Commit>`
                
                	**config**\: False
                
                

                """

                _prefix = 'config-cfgmgr-exec-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(ConfigManager.Global.ConfigCommit.Commits, self).__init__()

                    self.yang_name = "commits"
                    self.yang_parent_name = "config-commit"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("commit", ("commit", ConfigManager.Global.ConfigCommit.Commits.Commit))])
                    self._leafs = OrderedDict()

                    self.commit = YList(self)
                    self._segment_path = lambda: "commits"
                    self._absolute_path = lambda: "Cisco-IOS-XR-config-cfgmgr-exec-oper:config-manager/global/config-commit/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(ConfigManager.Global.ConfigCommit.Commits, [], name, value)


                class Commit(_Entity_):
                    """
                    Commit information for a specific commit
                    entry
                    
                    .. attribute:: commit  (key)
                    
                    	Each Session Details
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    	**config**\: False
                    
                    .. attribute:: timestamp
                    
                    	Timestamp
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: commit_id
                    
                    	CommitId
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: user_id
                    
                    	UserId
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: line
                    
                    	Line
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: client_name
                    
                    	Client name
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: label
                    
                    	Label
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: comment
                    
                    	Comment
                    	**type**\: str
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'config-cfgmgr-exec-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(ConfigManager.Global.ConfigCommit.Commits.Commit, self).__init__()

                        self.yang_name = "commit"
                        self.yang_parent_name = "commits"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['commit']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('commit', (YLeaf(YType.str, 'commit'), ['str'])),
                            ('timestamp', (YLeaf(YType.str, 'timestamp'), ['str'])),
                            ('commit_id', (YLeaf(YType.str, 'commit-id'), ['str'])),
                            ('user_id', (YLeaf(YType.str, 'user-id'), ['str'])),
                            ('line', (YLeaf(YType.str, 'line'), ['str'])),
                            ('client_name', (YLeaf(YType.str, 'client-name'), ['str'])),
                            ('label', (YLeaf(YType.str, 'label'), ['str'])),
                            ('comment', (YLeaf(YType.str, 'comment'), ['str'])),
                        ])
                        self.commit = None
                        self.timestamp = None
                        self.commit_id = None
                        self.user_id = None
                        self.line = None
                        self.client_name = None
                        self.label = None
                        self.comment = None
                        self._segment_path = lambda: "commit" + "[commit='" + str(self.commit) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-config-cfgmgr-exec-oper:config-manager/global/config-commit/commits/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(ConfigManager.Global.ConfigCommit.Commits.Commit, ['commit', 'timestamp', 'commit_id', 'user_id', 'line', 'client_name', 'label', 'comment'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_cfgmgr_exec_oper as meta
                        return meta._meta_table['ConfigManager.Global.ConfigCommit.Commits.Commit']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_cfgmgr_exec_oper as meta
                    return meta._meta_table['ConfigManager.Global.ConfigCommit.Commits']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_cfgmgr_exec_oper as meta
                return meta._meta_table['ConfigManager.Global.ConfigCommit']['meta_info']


        class HistoryTables(_Entity_):
            """
            Show Configuration History <\*> Global path
            information
            
            .. attribute:: history_table
            
            	List of possible type of History
            	**type**\: list of  		 :py:class:`HistoryTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_exec_oper.ConfigManager.Global.HistoryTables.HistoryTable>`
            
            	**config**\: False
            
            

            """

            _prefix = 'config-cfgmgr-exec-oper'
            _revision = '2017-09-07'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(ConfigManager.Global.HistoryTables, self).__init__()

                self.yang_name = "history-tables"
                self.yang_parent_name = "global"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("history-table", ("history_table", ConfigManager.Global.HistoryTables.HistoryTable))])
                self._leafs = OrderedDict()

                self.history_table = YList(self)
                self._segment_path = lambda: "history-tables"
                self._absolute_path = lambda: "Cisco-IOS-XR-config-cfgmgr-exec-oper:config-manager/global/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(ConfigManager.Global.HistoryTables, [], name, value)


            class HistoryTable(_Entity_):
                """
                List of possible type of History
                
                .. attribute:: history_type  (key)
                
                	Type of History
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                	**config**\: False
                
                .. attribute:: history
                
                	History summary information for a specific type of history
                	**type**\: list of  		 :py:class:`History <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_exec_oper.ConfigManager.Global.HistoryTables.HistoryTable.History>`
                
                	**config**\: False
                
                

                """

                _prefix = 'config-cfgmgr-exec-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(ConfigManager.Global.HistoryTables.HistoryTable, self).__init__()

                    self.yang_name = "history-table"
                    self.yang_parent_name = "history-tables"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['history_type']
                    self._child_classes = OrderedDict([("history", ("history", ConfigManager.Global.HistoryTables.HistoryTable.History))])
                    self._leafs = OrderedDict([
                        ('history_type', (YLeaf(YType.str, 'history-type'), ['str'])),
                    ])
                    self.history_type = None

                    self.history = YList(self)
                    self._segment_path = lambda: "history-table" + "[history-type='" + str(self.history_type) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-config-cfgmgr-exec-oper:config-manager/global/history-tables/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(ConfigManager.Global.HistoryTables.HistoryTable, ['history_type'], name, value)


                class History(_Entity_):
                    """
                    History summary information for a specific
                    type of history
                    
                    .. attribute:: history  (key)
                    
                    	History Record
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    	**config**\: False
                    
                    .. attribute:: info
                    
                    	Content of the history
                    	**type**\:  :py:class:`Info <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_exec_oper.ConfigManager.Global.HistoryTables.HistoryTable.History.Info>`
                    
                    	**config**\: False
                    
                    .. attribute:: timestamp
                    
                    	Timestamp
                    	**type**\: str
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'config-cfgmgr-exec-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(ConfigManager.Global.HistoryTables.HistoryTable.History, self).__init__()

                        self.yang_name = "history"
                        self.yang_parent_name = "history-table"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['history']
                        self._child_classes = OrderedDict([("info", ("info", ConfigManager.Global.HistoryTables.HistoryTable.History.Info))])
                        self._leafs = OrderedDict([
                            ('history', (YLeaf(YType.str, 'history'), ['str'])),
                            ('timestamp', (YLeaf(YType.str, 'timestamp'), ['str'])),
                        ])
                        self.history = None
                        self.timestamp = None

                        self.info = ConfigManager.Global.HistoryTables.HistoryTable.History.Info()
                        self.info.parent = self
                        self._children_name_map["info"] = "info"
                        self._segment_path = lambda: "history" + "[history='" + str(self.history) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(ConfigManager.Global.HistoryTables.HistoryTable.History, ['history', 'timestamp'], name, value)


                    class Info(_Entity_):
                        """
                        Content of the history
                        
                        .. attribute:: alarm_info
                        
                        	alarm info
                        	**type**\:  :py:class:`AlarmInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_exec_oper.ConfigManager.Global.HistoryTables.HistoryTable.History.Info.AlarmInfo>`
                        
                        	**config**\: False
                        
                        .. attribute:: cfscheck_info
                        
                        	cfscheck info
                        	**type**\:  :py:class:`CfscheckInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_exec_oper.ConfigManager.Global.HistoryTables.HistoryTable.History.Info.CfscheckInfo>`
                        
                        	**config**\: False
                        
                        .. attribute:: commit_info
                        
                        	commit info
                        	**type**\:  :py:class:`CommitInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_exec_oper.ConfigManager.Global.HistoryTables.HistoryTable.History.Info.CommitInfo>`
                        
                        	**config**\: False
                        
                        .. attribute:: oir_info
                        
                        	oir info
                        	**type**\:  :py:class:`OirInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_exec_oper.ConfigManager.Global.HistoryTables.HistoryTable.History.Info.OirInfo>`
                        
                        	**config**\: False
                        
                        .. attribute:: shutdown_info
                        
                        	shutdown info
                        	**type**\:  :py:class:`ShutdownInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_exec_oper.ConfigManager.Global.HistoryTables.HistoryTable.History.Info.ShutdownInfo>`
                        
                        	**config**\: False
                        
                        .. attribute:: startup_info
                        
                        	startup info
                        	**type**\:  :py:class:`StartupInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_exec_oper.ConfigManager.Global.HistoryTables.HistoryTable.History.Info.StartupInfo>`
                        
                        	**config**\: False
                        
                        .. attribute:: backup_info
                        
                        	backup info
                        	**type**\:  :py:class:`BackupInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_exec_oper.ConfigManager.Global.HistoryTables.HistoryTable.History.Info.BackupInfo>`
                        
                        	**config**\: False
                        
                        .. attribute:: type
                        
                        	type
                        	**type**\:  :py:class:`HistRecord <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_exec_oper.HistRecord>`
                        
                        	**config**\: False
                        
                        .. attribute:: a
                        
                        	B
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'config-cfgmgr-exec-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(ConfigManager.Global.HistoryTables.HistoryTable.History.Info, self).__init__()

                            self.yang_name = "info"
                            self.yang_parent_name = "history"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("alarm-info", ("alarm_info", ConfigManager.Global.HistoryTables.HistoryTable.History.Info.AlarmInfo)), ("cfscheck-info", ("cfscheck_info", ConfigManager.Global.HistoryTables.HistoryTable.History.Info.CfscheckInfo)), ("commit-info", ("commit_info", ConfigManager.Global.HistoryTables.HistoryTable.History.Info.CommitInfo)), ("oir-info", ("oir_info", ConfigManager.Global.HistoryTables.HistoryTable.History.Info.OirInfo)), ("shutdown-info", ("shutdown_info", ConfigManager.Global.HistoryTables.HistoryTable.History.Info.ShutdownInfo)), ("startup-info", ("startup_info", ConfigManager.Global.HistoryTables.HistoryTable.History.Info.StartupInfo)), ("backup-info", ("backup_info", ConfigManager.Global.HistoryTables.HistoryTable.History.Info.BackupInfo))])
                            self._leafs = OrderedDict([
                                ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_exec_oper', 'HistRecord', '')])),
                                ('a', (YLeaf(YType.uint32, 'a'), ['int'])),
                            ])
                            self.type = None
                            self.a = None

                            self.alarm_info = ConfigManager.Global.HistoryTables.HistoryTable.History.Info.AlarmInfo()
                            self.alarm_info.parent = self
                            self._children_name_map["alarm_info"] = "alarm-info"

                            self.cfscheck_info = ConfigManager.Global.HistoryTables.HistoryTable.History.Info.CfscheckInfo()
                            self.cfscheck_info.parent = self
                            self._children_name_map["cfscheck_info"] = "cfscheck-info"

                            self.commit_info = ConfigManager.Global.HistoryTables.HistoryTable.History.Info.CommitInfo()
                            self.commit_info.parent = self
                            self._children_name_map["commit_info"] = "commit-info"

                            self.oir_info = ConfigManager.Global.HistoryTables.HistoryTable.History.Info.OirInfo()
                            self.oir_info.parent = self
                            self._children_name_map["oir_info"] = "oir-info"

                            self.shutdown_info = ConfigManager.Global.HistoryTables.HistoryTable.History.Info.ShutdownInfo()
                            self.shutdown_info.parent = self
                            self._children_name_map["shutdown_info"] = "shutdown-info"

                            self.startup_info = ConfigManager.Global.HistoryTables.HistoryTable.History.Info.StartupInfo()
                            self.startup_info.parent = self
                            self._children_name_map["startup_info"] = "startup-info"

                            self.backup_info = ConfigManager.Global.HistoryTables.HistoryTable.History.Info.BackupInfo()
                            self.backup_info.parent = self
                            self._children_name_map["backup_info"] = "backup-info"
                            self._segment_path = lambda: "info"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(ConfigManager.Global.HistoryTables.HistoryTable.History.Info, ['type', 'a'], name, value)


                        class AlarmInfo(_Entity_):
                            """
                            alarm info
                            
                            .. attribute:: state
                            
                            	State
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: where
                            
                            	Where
                            	**type**\: str
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'config-cfgmgr-exec-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(ConfigManager.Global.HistoryTables.HistoryTable.History.Info.AlarmInfo, self).__init__()

                                self.yang_name = "alarm-info"
                                self.yang_parent_name = "info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('state', (YLeaf(YType.str, 'state'), ['str'])),
                                    ('where', (YLeaf(YType.str, 'where'), ['str'])),
                                ])
                                self.state = None
                                self.where = None
                                self._segment_path = lambda: "alarm-info"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(ConfigManager.Global.HistoryTables.HistoryTable.History.Info.AlarmInfo, ['state', 'where'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_cfgmgr_exec_oper as meta
                                return meta._meta_table['ConfigManager.Global.HistoryTables.HistoryTable.History.Info.AlarmInfo']['meta_info']


                        class CfscheckInfo(_Entity_):
                            """
                            cfscheck info
                            
                            .. attribute:: user_id
                            
                            	UserId
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: line
                            
                            	Line
                            	**type**\: str
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'config-cfgmgr-exec-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(ConfigManager.Global.HistoryTables.HistoryTable.History.Info.CfscheckInfo, self).__init__()

                                self.yang_name = "cfscheck-info"
                                self.yang_parent_name = "info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('user_id', (YLeaf(YType.str, 'user-id'), ['str'])),
                                    ('line', (YLeaf(YType.str, 'line'), ['str'])),
                                ])
                                self.user_id = None
                                self.line = None
                                self._segment_path = lambda: "cfscheck-info"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(ConfigManager.Global.HistoryTables.HistoryTable.History.Info.CfscheckInfo, ['user_id', 'line'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_cfgmgr_exec_oper as meta
                                return meta._meta_table['ConfigManager.Global.HistoryTables.HistoryTable.History.Info.CfscheckInfo']['meta_info']


                        class CommitInfo(_Entity_):
                            """
                            commit info
                            
                            .. attribute:: commit_id
                            
                            	CommitId
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: user_id
                            
                            	UserId
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: line
                            
                            	Line
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: client_name
                            
                            	Client name
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: label
                            
                            	Label
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: comment
                            
                            	Comment
                            	**type**\: str
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'config-cfgmgr-exec-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(ConfigManager.Global.HistoryTables.HistoryTable.History.Info.CommitInfo, self).__init__()

                                self.yang_name = "commit-info"
                                self.yang_parent_name = "info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('commit_id', (YLeaf(YType.str, 'commit-id'), ['str'])),
                                    ('user_id', (YLeaf(YType.str, 'user-id'), ['str'])),
                                    ('line', (YLeaf(YType.str, 'line'), ['str'])),
                                    ('client_name', (YLeaf(YType.str, 'client-name'), ['str'])),
                                    ('label', (YLeaf(YType.str, 'label'), ['str'])),
                                    ('comment', (YLeaf(YType.str, 'comment'), ['str'])),
                                ])
                                self.commit_id = None
                                self.user_id = None
                                self.line = None
                                self.client_name = None
                                self.label = None
                                self.comment = None
                                self._segment_path = lambda: "commit-info"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(ConfigManager.Global.HistoryTables.HistoryTable.History.Info.CommitInfo, ['commit_id', 'user_id', 'line', 'client_name', 'label', 'comment'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_cfgmgr_exec_oper as meta
                                return meta._meta_table['ConfigManager.Global.HistoryTables.HistoryTable.History.Info.CommitInfo']['meta_info']


                        class OirInfo(_Entity_):
                            """
                            oir info
                            
                            .. attribute:: config_type
                            
                            	Config Type
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: operation_
                            
                            	Operation
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: config_name
                            
                            	Config Name
                            	**type**\: str
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'config-cfgmgr-exec-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(ConfigManager.Global.HistoryTables.HistoryTable.History.Info.OirInfo, self).__init__()

                                self.yang_name = "oir-info"
                                self.yang_parent_name = "info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('config_type', (YLeaf(YType.str, 'config-type'), ['str'])),
                                    ('operation_', (YLeaf(YType.str, 'operation'), ['str'])),
                                    ('config_name', (YLeaf(YType.str, 'config-name'), ['str'])),
                                ])
                                self.config_type = None
                                self.operation_ = None
                                self.config_name = None
                                self._segment_path = lambda: "oir-info"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(ConfigManager.Global.HistoryTables.HistoryTable.History.Info.OirInfo, ['config_type', 'operation_', 'config_name'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_cfgmgr_exec_oper as meta
                                return meta._meta_table['ConfigManager.Global.HistoryTables.HistoryTable.History.Info.OirInfo']['meta_info']


                        class ShutdownInfo(_Entity_):
                            """
                            shutdown info
                            
                            .. attribute:: comment
                            
                            	Comment
                            	**type**\: str
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'config-cfgmgr-exec-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(ConfigManager.Global.HistoryTables.HistoryTable.History.Info.ShutdownInfo, self).__init__()

                                self.yang_name = "shutdown-info"
                                self.yang_parent_name = "info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('comment', (YLeaf(YType.str, 'comment'), ['str'])),
                                ])
                                self.comment = None
                                self._segment_path = lambda: "shutdown-info"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(ConfigManager.Global.HistoryTables.HistoryTable.History.Info.ShutdownInfo, ['comment'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_cfgmgr_exec_oper as meta
                                return meta._meta_table['ConfigManager.Global.HistoryTables.HistoryTable.History.Info.ShutdownInfo']['meta_info']


                        class StartupInfo(_Entity_):
                            """
                            startup info
                            
                            .. attribute:: how_booted
                            
                            	How Booted
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: boot_path
                            
                            	Boot Path
                            	**type**\: str
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'config-cfgmgr-exec-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(ConfigManager.Global.HistoryTables.HistoryTable.History.Info.StartupInfo, self).__init__()

                                self.yang_name = "startup-info"
                                self.yang_parent_name = "info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('how_booted', (YLeaf(YType.str, 'how-booted'), ['str'])),
                                    ('boot_path', (YLeaf(YType.str, 'boot-path'), ['str'])),
                                ])
                                self.how_booted = None
                                self.boot_path = None
                                self._segment_path = lambda: "startup-info"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(ConfigManager.Global.HistoryTables.HistoryTable.History.Info.StartupInfo, ['how_booted', 'boot_path'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_cfgmgr_exec_oper as meta
                                return meta._meta_table['ConfigManager.Global.HistoryTables.HistoryTable.History.Info.StartupInfo']['meta_info']


                        class BackupInfo(_Entity_):
                            """
                            backup info
                            
                            .. attribute:: comment
                            
                            	Comment
                            	**type**\: str
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'config-cfgmgr-exec-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(ConfigManager.Global.HistoryTables.HistoryTable.History.Info.BackupInfo, self).__init__()

                                self.yang_name = "backup-info"
                                self.yang_parent_name = "info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('comment', (YLeaf(YType.str, 'comment'), ['str'])),
                                ])
                                self.comment = None
                                self._segment_path = lambda: "backup-info"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(ConfigManager.Global.HistoryTables.HistoryTable.History.Info.BackupInfo, ['comment'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_cfgmgr_exec_oper as meta
                                return meta._meta_table['ConfigManager.Global.HistoryTables.HistoryTable.History.Info.BackupInfo']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_cfgmgr_exec_oper as meta
                            return meta._meta_table['ConfigManager.Global.HistoryTables.HistoryTable.History.Info']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_cfgmgr_exec_oper as meta
                        return meta._meta_table['ConfigManager.Global.HistoryTables.HistoryTable.History']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_cfgmgr_exec_oper as meta
                    return meta._meta_table['ConfigManager.Global.HistoryTables.HistoryTable']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_cfgmgr_exec_oper as meta
                return meta._meta_table['ConfigManager.Global.HistoryTables']['meta_info']


        class ConfigSession(_Entity_):
            """
            Show Configuration Session <\*> Global path
            information
            
            .. attribute:: sessions
            
            	Show Configuration Session Detail
            	**type**\:  :py:class:`Sessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_exec_oper.ConfigManager.Global.ConfigSession.Sessions>`
            
            	**config**\: False
            
            

            """

            _prefix = 'config-cfgmgr-exec-oper'
            _revision = '2017-09-07'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(ConfigManager.Global.ConfigSession, self).__init__()

                self.yang_name = "config-session"
                self.yang_parent_name = "global"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("sessions", ("sessions", ConfigManager.Global.ConfigSession.Sessions))])
                self._leafs = OrderedDict()

                self.sessions = ConfigManager.Global.ConfigSession.Sessions()
                self.sessions.parent = self
                self._children_name_map["sessions"] = "sessions"
                self._segment_path = lambda: "config-session"
                self._absolute_path = lambda: "Cisco-IOS-XR-config-cfgmgr-exec-oper:config-manager/global/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(ConfigManager.Global.ConfigSession, [], name, value)


            class Sessions(_Entity_):
                """
                Show Configuration Session Detail
                
                .. attribute:: session
                
                	Session information for a specific session entry
                	**type**\: list of  		 :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_exec_oper.ConfigManager.Global.ConfigSession.Sessions.Session>`
                
                	**config**\: False
                
                

                """

                _prefix = 'config-cfgmgr-exec-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(ConfigManager.Global.ConfigSession.Sessions, self).__init__()

                    self.yang_name = "sessions"
                    self.yang_parent_name = "config-session"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("session", ("session", ConfigManager.Global.ConfigSession.Sessions.Session))])
                    self._leafs = OrderedDict()

                    self.session = YList(self)
                    self._segment_path = lambda: "sessions"
                    self._absolute_path = lambda: "Cisco-IOS-XR-config-cfgmgr-exec-oper:config-manager/global/config-session/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(ConfigManager.Global.ConfigSession.Sessions, [], name, value)


                class Session(_Entity_):
                    """
                    Session information for a specific session
                    entry
                    
                    .. attribute:: session  (key)
                    
                    	Each Session Details
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    	**config**\: False
                    
                    .. attribute:: session_id
                    
                    	Session Id
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: client_name
                    
                    	Client Name
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: user_id
                    
                    	UserId
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: tty_name
                    
                    	TtyName
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: timestamp
                    
                    	Timestamp
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: lock_flag
                    
                    	Lock Flag
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: trial_flag
                    
                    	Trial Flag
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: pid
                    
                    	PID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: process_name
                    
                    	Process Name
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: node_name
                    
                    	Node Name
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: elapsed_time
                    
                    	Elapsed Time
                    	**type**\: str
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'config-cfgmgr-exec-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(ConfigManager.Global.ConfigSession.Sessions.Session, self).__init__()

                        self.yang_name = "session"
                        self.yang_parent_name = "sessions"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['session']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('session', (YLeaf(YType.str, 'session'), ['str'])),
                            ('session_id', (YLeaf(YType.str, 'session-id'), ['str'])),
                            ('client_name', (YLeaf(YType.str, 'client-name'), ['str'])),
                            ('user_id', (YLeaf(YType.str, 'user-id'), ['str'])),
                            ('tty_name', (YLeaf(YType.str, 'tty-name'), ['str'])),
                            ('timestamp', (YLeaf(YType.str, 'timestamp'), ['str'])),
                            ('lock_flag', (YLeaf(YType.str, 'lock-flag'), ['str'])),
                            ('trial_flag', (YLeaf(YType.str, 'trial-flag'), ['str'])),
                            ('pid', (YLeaf(YType.uint32, 'pid'), ['int'])),
                            ('process_name', (YLeaf(YType.str, 'process-name'), ['str'])),
                            ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                            ('elapsed_time', (YLeaf(YType.str, 'elapsed-time'), ['str'])),
                        ])
                        self.session = None
                        self.session_id = None
                        self.client_name = None
                        self.user_id = None
                        self.tty_name = None
                        self.timestamp = None
                        self.lock_flag = None
                        self.trial_flag = None
                        self.pid = None
                        self.process_name = None
                        self.node_name = None
                        self.elapsed_time = None
                        self._segment_path = lambda: "session" + "[session='" + str(self.session) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-config-cfgmgr-exec-oper:config-manager/global/config-session/sessions/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(ConfigManager.Global.ConfigSession.Sessions.Session, ['session', 'session_id', 'client_name', 'user_id', 'tty_name', 'timestamp', 'lock_flag', 'trial_flag', 'pid', 'process_name', 'node_name', 'elapsed_time'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_cfgmgr_exec_oper as meta
                        return meta._meta_table['ConfigManager.Global.ConfigSession.Sessions.Session']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_cfgmgr_exec_oper as meta
                    return meta._meta_table['ConfigManager.Global.ConfigSession.Sessions']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_cfgmgr_exec_oper as meta
                return meta._meta_table['ConfigManager.Global.ConfigSession']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_cfgmgr_exec_oper as meta
            return meta._meta_table['ConfigManager.Global']['meta_info']

    def clone_ptr(self):
        self._top_entity = ConfigManager()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_cfgmgr_exec_oper as meta
        return meta._meta_table['ConfigManager']['meta_info']


