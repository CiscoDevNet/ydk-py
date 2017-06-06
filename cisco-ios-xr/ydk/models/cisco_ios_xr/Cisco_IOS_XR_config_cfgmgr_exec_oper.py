""" Cisco_IOS_XR_config_cfgmgr_exec_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR config\-cfgmgr\-exec package operational data.

This module contains definitions
for the following management objects\:
  cfg\-hist\-gl\: Configuration History Global path information

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class HistRecordEnum(Enum):
    """
    HistRecordEnum

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

    cfghist_bag_record_all = 0

    cfghist_bag_record_alarm = 1

    cfghist_bag_record_cfs_check = 2

    cfghist_bag_record_commit = 3

    cfghist_bag_record_oir = 4

    cfghist_bag_record_shutdown = 5

    cfghist_bag_record_startup = 6

    cfghist_bag_record_backup = 7

    cfghist_bag_record_rebase = 8

    cfghist_bag_record_last = 9


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_cfgmgr_exec_oper as meta
        return meta._meta_table['HistRecordEnum']



class CfgHistGl(object):
    """
    Configuration History Global path information
    
    .. attribute:: record_type
    
    	History summary information for a specific type of history
    	**type**\: list of    :py:class:`RecordType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_exec_oper.CfgHistGl.RecordType>`
    
    

    """

    _prefix = 'config-cfgmgr-exec-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.record_type = YList()
        self.record_type.parent = self
        self.record_type.name = 'record_type'


    class RecordType(object):
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
            self.parent = None
            self.record_type = None
            self.record = YList()
            self.record.parent = self
            self.record.name = 'record'


        class Record(object):
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
            	**type**\:   :py:class:`HistRecordEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_exec_oper.HistRecordEnum>`
            
            .. attribute:: timestamp
            
            	Time stamp for the history
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'config-cfgmgr-exec-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.record = None
                self.info = CfgHistGl.RecordType.Record.Info()
                self.info.parent = self
                self.record_type = None
                self.timestamp = None


            class Info(object):
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
                	**type**\:   :py:class:`HistRecordEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_exec_oper.HistRecordEnum>`
                
                

                """

                _prefix = 'config-cfgmgr-exec-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.a = None
                    self.alarm_info = CfgHistGl.RecordType.Record.Info.AlarmInfo()
                    self.alarm_info.parent = self
                    self.backup_info = CfgHistGl.RecordType.Record.Info.BackupInfo()
                    self.backup_info.parent = self
                    self.cfscheck_info = CfgHistGl.RecordType.Record.Info.CfscheckInfo()
                    self.cfscheck_info.parent = self
                    self.commit_info = CfgHistGl.RecordType.Record.Info.CommitInfo()
                    self.commit_info.parent = self
                    self.oir_info = CfgHistGl.RecordType.Record.Info.OirInfo()
                    self.oir_info.parent = self
                    self.shutdown_info = CfgHistGl.RecordType.Record.Info.ShutdownInfo()
                    self.shutdown_info.parent = self
                    self.startup_info = CfgHistGl.RecordType.Record.Info.StartupInfo()
                    self.startup_info.parent = self
                    self.type = None


                class AlarmInfo(object):
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
                        self.parent = None
                        self.state = None
                        self.where = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-config-cfgmgr-exec-oper:alarm-info'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.state is not None:
                            return True

                        if self.where is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_cfgmgr_exec_oper as meta
                        return meta._meta_table['CfgHistGl.RecordType.Record.Info.AlarmInfo']['meta_info']


                class CfscheckInfo(object):
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
                        self.parent = None
                        self.line = None
                        self.user_id = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-config-cfgmgr-exec-oper:cfscheck-info'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.line is not None:
                            return True

                        if self.user_id is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_cfgmgr_exec_oper as meta
                        return meta._meta_table['CfgHistGl.RecordType.Record.Info.CfscheckInfo']['meta_info']


                class CommitInfo(object):
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
                        self.parent = None
                        self.client_name = None
                        self.comment = None
                        self.commit_id = None
                        self.label = None
                        self.line = None
                        self.user_id = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-config-cfgmgr-exec-oper:commit-info'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.client_name is not None:
                            return True

                        if self.comment is not None:
                            return True

                        if self.commit_id is not None:
                            return True

                        if self.label is not None:
                            return True

                        if self.line is not None:
                            return True

                        if self.user_id is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_cfgmgr_exec_oper as meta
                        return meta._meta_table['CfgHistGl.RecordType.Record.Info.CommitInfo']['meta_info']


                class OirInfo(object):
                    """
                    oir info
                    
                    .. attribute:: config_name
                    
                    	Config Name
                    	**type**\:  str
                    
                    .. attribute:: config_type
                    
                    	Config Type
                    	**type**\:  str
                    
                    .. attribute:: operation
                    
                    	Operation
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'config-cfgmgr-exec-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.config_name = None
                        self.config_type = None
                        self.operation = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-config-cfgmgr-exec-oper:oir-info'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.config_name is not None:
                            return True

                        if self.config_type is not None:
                            return True

                        if self.operation is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_cfgmgr_exec_oper as meta
                        return meta._meta_table['CfgHistGl.RecordType.Record.Info.OirInfo']['meta_info']


                class ShutdownInfo(object):
                    """
                    shutdown info
                    
                    .. attribute:: comment
                    
                    	Comment
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'config-cfgmgr-exec-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.comment = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-config-cfgmgr-exec-oper:shutdown-info'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.comment is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_cfgmgr_exec_oper as meta
                        return meta._meta_table['CfgHistGl.RecordType.Record.Info.ShutdownInfo']['meta_info']


                class StartupInfo(object):
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
                        self.parent = None
                        self.boot_path = None
                        self.how_booted = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-config-cfgmgr-exec-oper:startup-info'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.boot_path is not None:
                            return True

                        if self.how_booted is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_cfgmgr_exec_oper as meta
                        return meta._meta_table['CfgHistGl.RecordType.Record.Info.StartupInfo']['meta_info']


                class BackupInfo(object):
                    """
                    backup info
                    
                    .. attribute:: comment
                    
                    	Comment
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'config-cfgmgr-exec-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.comment = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-config-cfgmgr-exec-oper:backup-info'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.comment is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_cfgmgr_exec_oper as meta
                        return meta._meta_table['CfgHistGl.RecordType.Record.Info.BackupInfo']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-config-cfgmgr-exec-oper:info'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.a is not None:
                        return True

                    if self.alarm_info is not None and self.alarm_info._has_data():
                        return True

                    if self.backup_info is not None and self.backup_info._has_data():
                        return True

                    if self.cfscheck_info is not None and self.cfscheck_info._has_data():
                        return True

                    if self.commit_info is not None and self.commit_info._has_data():
                        return True

                    if self.oir_info is not None and self.oir_info._has_data():
                        return True

                    if self.shutdown_info is not None and self.shutdown_info._has_data():
                        return True

                    if self.startup_info is not None and self.startup_info._has_data():
                        return True

                    if self.type is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_cfgmgr_exec_oper as meta
                    return meta._meta_table['CfgHistGl.RecordType.Record.Info']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')
                if self.record is None:
                    raise YPYModelError('Key property record is None')

                return self.parent._common_path +'/Cisco-IOS-XR-config-cfgmgr-exec-oper:record[Cisco-IOS-XR-config-cfgmgr-exec-oper:record = ' + str(self.record) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.record is not None:
                    return True

                if self.info is not None and self.info._has_data():
                    return True

                if self.record_type is not None:
                    return True

                if self.timestamp is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_cfgmgr_exec_oper as meta
                return meta._meta_table['CfgHistGl.RecordType.Record']['meta_info']

        @property
        def _common_path(self):
            if self.record_type is None:
                raise YPYModelError('Key property record_type is None')

            return '/Cisco-IOS-XR-config-cfgmgr-exec-oper:cfg-hist-gl/Cisco-IOS-XR-config-cfgmgr-exec-oper:record-type[Cisco-IOS-XR-config-cfgmgr-exec-oper:record-type = ' + str(self.record_type) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.record_type is not None:
                return True

            if self.record is not None:
                for child_ref in self.record:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_cfgmgr_exec_oper as meta
            return meta._meta_table['CfgHistGl.RecordType']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-config-cfgmgr-exec-oper:cfg-hist-gl'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.record_type is not None:
            for child_ref in self.record_type:
                if child_ref._has_data():
                    return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_cfgmgr_exec_oper as meta
        return meta._meta_table['CfgHistGl']['meta_info']


