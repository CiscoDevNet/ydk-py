""" Cisco_IOS_XR_spirit_install_instmgr_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR spirit\-install\-instmgr package operational data.

This module contains definitions
for the following management objects\:
  software\-install\: Install operations info

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class CardTypeEtEnum(Enum):
    """
    CardTypeEtEnum

    card type

    .. data:: card_rp = 0

    	Card RP

    .. data:: card_drp = 1

    	Card DRP

    .. data:: card_lc = 2

    	Card LC

    .. data:: card_sc = 3

    	Card SC

    .. data:: card_sp = 4

    	Card SP

    .. data:: card_other = 5

    	Card Other

    """

    card_rp = 0

    card_drp = 1

    card_lc = 2

    card_sc = 3

    card_sp = 4

    card_other = 5


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
        return meta._meta_table['CardTypeEtEnum']


class IsdErrorEtEnum(Enum):
    """
    IsdErrorEtEnum

    isd error

    .. data:: none = 0

    	ISD ERROR NONE

    .. data:: not_compatible = 1

    	ISD ERROR NOT COMPATIBLE

    .. data:: not_enough_resource = 2

    	ISD ERROR NOT ENOUGH RESOURCE

    .. data:: not_nsr_ready = 3

    	ISD ERROR NOT NSR READY

    .. data:: not_conn_sdrsm = 4

    	ISD ERROR NOT CONNECTED SDR SM

    .. data:: cmd_invalid = 5

    	ISD ERROR INST CMD INVALID

    .. data:: load_prep_fail = 6

    	ISD ERROR INST LOAD PREP FAILURE

    .. data:: error_timeout = 7

    	ISD ERROR TIMEOUT

    .. data:: err_node_down = 8

    	ISD ERROR NODE DOWN

    .. data:: node_not_ready = 9

    	ISD ERROR NODE NOT READY

    .. data:: err_node_new = 10

    	ISD ERROR NODE NEW

    .. data:: err_card_oir = 11

    	ISD ERROR CARD OIR

    .. data:: invalid_evt = 12

    	ISD ERROR INVALID EVT

    .. data:: disconn_from_calv = 13

    	ISD ERROR DISCONN FROM CALVADOS

    .. data:: gsp_down = 14

    	ISD ERROR GSP DOWN

    .. data:: abort_by_ism = 15

    	ISD ERROR ABORT BY ISM

    .. data:: rpfo = 16

    	ISD ERROR RPFO

    .. data:: pkg_null = 17

    	ISD ERROR PKG NULL

    .. data:: error_general = 18

    	ISD ERROR GENERAL

    .. data:: fsa_error = 19

    	ISD ERROR FSA ERROR

    .. data:: err_post_issu = 20

    	ISD ERROR POST ISSU

    .. data:: err_issu_dir_restart = 21

    	ISD ERROR ISSUDIR RESTART

    """

    none = 0

    not_compatible = 1

    not_enough_resource = 2

    not_nsr_ready = 3

    not_conn_sdrsm = 4

    cmd_invalid = 5

    load_prep_fail = 6

    error_timeout = 7

    err_node_down = 8

    node_not_ready = 9

    err_node_new = 10

    err_card_oir = 11

    invalid_evt = 12

    disconn_from_calv = 13

    gsp_down = 14

    abort_by_ism = 15

    rpfo = 16

    pkg_null = 17

    error_general = 18

    fsa_error = 19

    err_post_issu = 20

    err_issu_dir_restart = 21


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
        return meta._meta_table['IsdErrorEtEnum']


class IsdIssuStatusEtEnum(Enum):
    """
    IsdIssuStatusEtEnum

    isd status

    .. data:: ok = 0

    	ISSU STATUS OK

    .. data:: prep_done = 1

    	ISSU STATUS PREP DONE

    .. data:: big_bang = 2

    	ISSU STATUS BIG BANG

    .. data:: done = 3

    	ISSU STATUS DONE

    .. data:: abort = 4

    	ISSU STATUS ABORT

    .. data:: cmd_reject = 5

    	ISSU STATUS CMD REJECT

    .. data:: unknown = 6

    	ISSU STATUS UNKNOWN

    .. data:: abort_cleanup = 7

    	ISSU STATUS ABORT CLEANUP

    .. data:: abort_cmd_reject = 8

    	ISSU STATUS CMD ABORT REJECT

    """

    ok = 0

    prep_done = 1

    big_bang = 2

    done = 3

    abort = 4

    cmd_reject = 5

    unknown = 6

    abort_cleanup = 7

    abort_cmd_reject = 8


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
        return meta._meta_table['IsdIssuStatusEtEnum']


class IsdStateEtEnum(Enum):
    """
    IsdStateEtEnum

    isd state

    .. data:: none = 0

    	ISSU ST NONE

    .. data:: idle = 1

    	ISSU ST IDLE

    .. data:: init = 2

    	ISSU ST INIT

    .. data:: init_done = 3

    	ISSU ST INIT DONE

    .. data:: load_prep = 4

    	ISSU ST LOAD PREP

    .. data:: load_exec = 5

    	ISSU ST LOAD EXEC

    .. data:: load_issu_go = 6

    	ISSU ST LOAD ISSU GO

    .. data:: load_done = 7

    	ISSU ST LOAD DONE

    .. data:: run_prep = 8

    	ISSU ST RUN PREP

    .. data:: big_bang = 9

    	ISSU ST RUN BIG BANG

    .. data:: run_done = 10

    	ISSU ST RUN DONE

    .. data:: cleanup = 11

    	ISSU ST CLEANUP

    .. data:: cleanup_done = 12

    	ISSU ST CLEANUP DONE

    .. data:: abort = 13

    	ISSU ST ABORT

    .. data:: abort_done = 14

    	ISSU ST ABORT DONE

    .. data:: abort_cleanup = 15

    	ISSU ST ABORT CLEANUP

    .. data:: unknown_state = 16

    	ISSU UNKNOWN STATE

    """

    none = 0

    idle = 1

    init = 2

    init_done = 3

    load_prep = 4

    load_exec = 5

    load_issu_go = 6

    load_done = 7

    run_prep = 8

    big_bang = 9

    run_done = 10

    cleanup = 11

    cleanup_done = 12

    abort = 13

    abort_done = 14

    abort_cleanup = 15

    unknown_state = 16


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
        return meta._meta_table['IsdStateEtEnum']


class IssuNodeRoleEtEnum(Enum):
    """
    IssuNodeRoleEtEnum

    ISSU role

    .. data:: unknown_role = 0

    	Unknown

    .. data:: primary_role = 1

    	Primary

    .. data:: secondary_role = 2

    	Secondary

    .. data:: tertiary_role = 3

    	Tertiary

    """

    unknown_role = 0

    primary_role = 1

    secondary_role = 2

    tertiary_role = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
        return meta._meta_table['IssuNodeRoleEtEnum']


class IssudirNodeStatusEtEnum(Enum):
    """
    IssudirNodeStatusEtEnum

    ISSU node status

    .. data:: not_issu_ready = 0

    	Not ISSU Ready

    .. data:: issu_ready = 1

    	ISSU Ready

    .. data:: isus_go = 2

    	ISSU Go

    .. data:: node_fail = 3

    	Node Fail

    """

    not_issu_ready = 0

    issu_ready = 1

    isus_go = 2

    node_fail = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
        return meta._meta_table['IssudirNodeStatusEtEnum']


class NodeRoleEtEnum(Enum):
    """
    NodeRoleEtEnum

    node role

    .. data:: node_unknown = 0

    	Unknown

    .. data:: node_active = 1

    	Active

    .. data:: node_standby = 2

    	Standby

    .. data:: node_unusable = 3

    	Unusable

    """

    node_unknown = 0

    node_active = 1

    node_standby = 2

    node_unusable = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
        return meta._meta_table['NodeRoleEtEnum']



class SoftwareInstall(object):
    """
    Install operations info
    
    .. attribute:: active
    
    	Show active packages installed
    	**type**\:   :py:class:`Active <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.Active>`
    
    .. attribute:: all_operations_log
    
    	Show log file for all operations
    	**type**\:   :py:class:`AllOperationsLog <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.AllOperationsLog>`
    
    .. attribute:: committed
    
    	Show Committed packages installed
    	**type**\:   :py:class:`Committed <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.Committed>`
    
    .. attribute:: files
    
    	Show information about an installed file
    	**type**\:   :py:class:`Files <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.Files>`
    
    .. attribute:: inactive
    
    	Show XR inactive packages
    	**type**\:   :py:class:`Inactive <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.Inactive>`
    
    .. attribute:: issu
    
    	ISSU operation
    	**type**\:   :py:class:`Issu <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.Issu>`
    
    .. attribute:: last_n_operation_logs
    
    	Show log file for last n operations
    	**type**\:   :py:class:`LastNOperationLogs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.LastNOperationLogs>`
    
    .. attribute:: operation_logs
    
    	Show log file
    	**type**\:   :py:class:`OperationLogs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.OperationLogs>`
    
    .. attribute:: packages
    
    	Show the list of installed packages
    	**type**\:   :py:class:`Packages <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.Packages>`
    
    .. attribute:: prepare
    
    	Show prepared packages ready for activation
    	**type**\:   :py:class:`Prepare <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.Prepare>`
    
    .. attribute:: repository
    
    	Show packages stored in install software repositories
    	**type**\:   :py:class:`Repository <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.Repository>`
    
    .. attribute:: request
    
    	Show current request
    	**type**\:   :py:class:`Request <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.Request>`
    
    .. attribute:: version
    
    	Show install version
    	**type**\:   :py:class:`Version <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.Version>`
    
    

    """

    _prefix = 'spirit-install-instmgr-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.active = SoftwareInstall.Active()
        self.active.parent = self
        self.all_operations_log = SoftwareInstall.AllOperationsLog()
        self.all_operations_log.parent = self
        self.committed = SoftwareInstall.Committed()
        self.committed.parent = self
        self.files = SoftwareInstall.Files()
        self.files.parent = self
        self.inactive = SoftwareInstall.Inactive()
        self.inactive.parent = self
        self.issu = SoftwareInstall.Issu()
        self.issu.parent = self
        self.last_n_operation_logs = SoftwareInstall.LastNOperationLogs()
        self.last_n_operation_logs.parent = self
        self.operation_logs = SoftwareInstall.OperationLogs()
        self.operation_logs.parent = self
        self.packages = SoftwareInstall.Packages()
        self.packages.parent = self
        self.prepare = SoftwareInstall.Prepare()
        self.prepare.parent = self
        self.repository = SoftwareInstall.Repository()
        self.repository.parent = self
        self.request = SoftwareInstall.Request()
        self.request.parent = self
        self.version = SoftwareInstall.Version()
        self.version.parent = self


    class Files(object):
        """
        Show information about an installed file
        
        .. attribute:: file
        
        	Show information about an installed file
        	**type**\: list of    :py:class:`File <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.Files.File>`
        
        

        """

        _prefix = 'spirit-install-instmgr-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.file = YList()
            self.file.parent = self
            self.file.name = 'file'


        class File(object):
            """
            Show information about an installed file
            
            .. attribute:: file_name  <key>
            
            	File name
            	**type**\:  str
            
            .. attribute:: brief
            
            	Show information about an installed file
            	**type**\:   :py:class:`Brief <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.Files.File.Brief>`
            
            .. attribute:: detail
            
            	Show detail information about an installed file
            	**type**\:   :py:class:`Detail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.Files.File.Detail>`
            
            

            """

            _prefix = 'spirit-install-instmgr-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.file_name = None
                self.brief = SoftwareInstall.Files.File.Brief()
                self.brief.parent = self
                self.detail = SoftwareInstall.Files.File.Detail()
                self.detail.parent = self


            class Brief(object):
                """
                Show information about an installed file
                
                .. attribute:: log
                
                	log
                	**type**\:  str
                
                

                """

                _prefix = 'spirit-install-instmgr-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.log = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-spirit-install-instmgr-oper:brief'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.log is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
                    return meta._meta_table['SoftwareInstall.Files.File.Brief']['meta_info']


            class Detail(object):
                """
                Show detail information about an installed
                file
                
                .. attribute:: log
                
                	log
                	**type**\:  str
                
                

                """

                _prefix = 'spirit-install-instmgr-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.log = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-spirit-install-instmgr-oper:detail'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.log is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
                    return meta._meta_table['SoftwareInstall.Files.File.Detail']['meta_info']

            @property
            def _common_path(self):
                if self.file_name is None:
                    raise YPYModelError('Key property file_name is None')

                return '/Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/Cisco-IOS-XR-spirit-install-instmgr-oper:files/Cisco-IOS-XR-spirit-install-instmgr-oper:file[Cisco-IOS-XR-spirit-install-instmgr-oper:file-name = ' + str(self.file_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.file_name is not None:
                    return True

                if self.brief is not None and self.brief._has_data():
                    return True

                if self.detail is not None and self.detail._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
                return meta._meta_table['SoftwareInstall.Files.File']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/Cisco-IOS-XR-spirit-install-instmgr-oper:files'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.file is not None:
                for child_ref in self.file:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
            return meta._meta_table['SoftwareInstall.Files']['meta_info']


    class LastNOperationLogs(object):
        """
        Show log file for last n operations
        
        .. attribute:: last_n_operation_log
        
        	Show log file of last n operations
        	**type**\: list of    :py:class:`LastNOperationLog <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.LastNOperationLogs.LastNOperationLog>`
        
        

        """

        _prefix = 'spirit-install-instmgr-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.last_n_operation_log = YList()
            self.last_n_operation_log.parent = self
            self.last_n_operation_log.name = 'last_n_operation_log'


        class LastNOperationLog(object):
            """
            Show log file of last n operations
            
            .. attribute:: last_n_logs  <key>
            
            	Last N opeartion logs
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: detail
            
            	Show detailed log file for last n operations
            	**type**\:   :py:class:`Detail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.LastNOperationLogs.LastNOperationLog.Detail>`
            
            .. attribute:: summary
            
            	Show summary log file for last n operations
            	**type**\:   :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.LastNOperationLogs.LastNOperationLog.Summary>`
            
            

            """

            _prefix = 'spirit-install-instmgr-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.last_n_logs = None
                self.detail = SoftwareInstall.LastNOperationLogs.LastNOperationLog.Detail()
                self.detail.parent = self
                self.summary = SoftwareInstall.LastNOperationLogs.LastNOperationLog.Summary()
                self.summary.parent = self


            class Summary(object):
                """
                Show summary log file for last n operations
                
                .. attribute:: log
                
                	log
                	**type**\:  str
                
                

                """

                _prefix = 'spirit-install-instmgr-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.log = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-spirit-install-instmgr-oper:summary'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.log is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
                    return meta._meta_table['SoftwareInstall.LastNOperationLogs.LastNOperationLog.Summary']['meta_info']


            class Detail(object):
                """
                Show detailed log file for last n operations
                
                .. attribute:: log
                
                	log
                	**type**\:  str
                
                

                """

                _prefix = 'spirit-install-instmgr-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.log = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-spirit-install-instmgr-oper:detail'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.log is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
                    return meta._meta_table['SoftwareInstall.LastNOperationLogs.LastNOperationLog.Detail']['meta_info']

            @property
            def _common_path(self):
                if self.last_n_logs is None:
                    raise YPYModelError('Key property last_n_logs is None')

                return '/Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/Cisco-IOS-XR-spirit-install-instmgr-oper:last-n-operation-logs/Cisco-IOS-XR-spirit-install-instmgr-oper:last-n-operation-log[Cisco-IOS-XR-spirit-install-instmgr-oper:last-n-logs = ' + str(self.last_n_logs) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.last_n_logs is not None:
                    return True

                if self.detail is not None and self.detail._has_data():
                    return True

                if self.summary is not None and self.summary._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
                return meta._meta_table['SoftwareInstall.LastNOperationLogs.LastNOperationLog']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/Cisco-IOS-XR-spirit-install-instmgr-oper:last-n-operation-logs'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.last_n_operation_log is not None:
                for child_ref in self.last_n_operation_log:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
            return meta._meta_table['SoftwareInstall.LastNOperationLogs']['meta_info']


    class Prepare(object):
        """
        Show prepared packages ready for activation
        
        .. attribute:: activate_message
        
        	ActivateMessage
        	**type**\:  str
        
        .. attribute:: no_prepare_done
        
        	NoPrepareDone
        	**type**\:  str
        
        .. attribute:: package
        
        	package
        	**type**\: list of    :py:class:`Package <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.Prepare.Package>`
        
        .. attribute:: prepare_clean_message
        
        	PrepareCleanMessage
        	**type**\:  str
        
        .. attribute:: prepared_boot_image
        
        	PreparedBootImage
        	**type**\:  str
        
        .. attribute:: prepared_boot_partition
        
        	PreparedBootPartition
        	**type**\:  str
        
        .. attribute:: restart_type
        
        	RestartType
        	**type**\:  str
        
        .. attribute:: rpm
        
        	rpm
        	**type**\: list of    :py:class:`Rpm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.Prepare.Rpm>`
        
        

        """

        _prefix = 'spirit-install-instmgr-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.activate_message = None
            self.no_prepare_done = None
            self.package = YList()
            self.package.parent = self
            self.package.name = 'package'
            self.prepare_clean_message = None
            self.prepared_boot_image = None
            self.prepared_boot_partition = None
            self.restart_type = None
            self.rpm = YList()
            self.rpm.parent = self
            self.rpm.name = 'rpm'


        class Rpm(object):
            """
            rpm
            
            .. attribute:: package
            
            	package
            	**type**\:  str
            
            

            """

            _prefix = 'spirit-install-instmgr-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.package = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/Cisco-IOS-XR-spirit-install-instmgr-oper:prepare/Cisco-IOS-XR-spirit-install-instmgr-oper:rpm'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.package is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
                return meta._meta_table['SoftwareInstall.Prepare.Rpm']['meta_info']


        class Package(object):
            """
            package
            
            .. attribute:: package
            
            	package
            	**type**\:  str
            
            

            """

            _prefix = 'spirit-install-instmgr-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.package = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/Cisco-IOS-XR-spirit-install-instmgr-oper:prepare/Cisco-IOS-XR-spirit-install-instmgr-oper:package'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.package is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
                return meta._meta_table['SoftwareInstall.Prepare.Package']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/Cisco-IOS-XR-spirit-install-instmgr-oper:prepare'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.activate_message is not None:
                return True

            if self.no_prepare_done is not None:
                return True

            if self.package is not None:
                for child_ref in self.package:
                    if child_ref._has_data():
                        return True

            if self.prepare_clean_message is not None:
                return True

            if self.prepared_boot_image is not None:
                return True

            if self.prepared_boot_partition is not None:
                return True

            if self.restart_type is not None:
                return True

            if self.rpm is not None:
                for child_ref in self.rpm:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
            return meta._meta_table['SoftwareInstall.Prepare']['meta_info']


    class Active(object):
        """
        Show active packages installed
        
        .. attribute:: active_package_info
        
        	active package info
        	**type**\: list of    :py:class:`ActivePackageInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.Active.ActivePackageInfo>`
        
        

        """

        _prefix = 'spirit-install-instmgr-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.active_package_info = YList()
            self.active_package_info.parent = self
            self.active_package_info.name = 'active_package_info'


        class ActivePackageInfo(object):
            """
            active package info
            
            .. attribute:: active_packages
            
            	ActivePackages
            	**type**\:  str
            
            .. attribute:: boot_partition_name
            
            	BootPartitionName
            	**type**\:  str
            
            .. attribute:: error_message
            
            	ErrorMessage
            	**type**\:  str
            
            .. attribute:: location
            
            	Location
            	**type**\:  str
            
            .. attribute:: node_type
            
            	NodeType
            	**type**\:  str
            
            .. attribute:: number_of_active_packages
            
            	NumberOfActivePackages
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'spirit-install-instmgr-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.active_packages = None
                self.boot_partition_name = None
                self.error_message = None
                self.location = None
                self.node_type = None
                self.number_of_active_packages = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/Cisco-IOS-XR-spirit-install-instmgr-oper:active/Cisco-IOS-XR-spirit-install-instmgr-oper:active-package-info'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.active_packages is not None:
                    return True

                if self.boot_partition_name is not None:
                    return True

                if self.error_message is not None:
                    return True

                if self.location is not None:
                    return True

                if self.node_type is not None:
                    return True

                if self.number_of_active_packages is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
                return meta._meta_table['SoftwareInstall.Active.ActivePackageInfo']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/Cisco-IOS-XR-spirit-install-instmgr-oper:active'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.active_package_info is not None:
                for child_ref in self.active_package_info:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
            return meta._meta_table['SoftwareInstall.Active']['meta_info']


    class Version(object):
        """
        Show install version
        
        .. attribute:: log
        
        	log
        	**type**\:  str
        
        

        """

        _prefix = 'spirit-install-instmgr-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.log = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/Cisco-IOS-XR-spirit-install-instmgr-oper:version'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.log is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
            return meta._meta_table['SoftwareInstall.Version']['meta_info']


    class Inactive(object):
        """
        Show XR inactive packages
        
        .. attribute:: log
        
        	log
        	**type**\:  str
        
        

        """

        _prefix = 'spirit-install-instmgr-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.log = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/Cisco-IOS-XR-spirit-install-instmgr-oper:inactive'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.log is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
            return meta._meta_table['SoftwareInstall.Inactive']['meta_info']


    class Request(object):
        """
        Show current request
        
        .. attribute:: log
        
        	log
        	**type**\:  str
        
        

        """

        _prefix = 'spirit-install-instmgr-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.log = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/Cisco-IOS-XR-spirit-install-instmgr-oper:request'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.log is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
            return meta._meta_table['SoftwareInstall.Request']['meta_info']


    class Issu(object):
        """
        ISSU operation
        
        .. attribute:: inventory
        
        	Show XR install issu inventory
        	**type**\:   :py:class:`Inventory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.Issu.Inventory>`
        
        .. attribute:: stage
        
        	Show XR install issu stage
        	**type**\:   :py:class:`Stage <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.Issu.Stage>`
        
        

        """

        _prefix = 'spirit-install-instmgr-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.inventory = SoftwareInstall.Issu.Inventory()
            self.inventory.parent = self
            self.stage = SoftwareInstall.Issu.Stage()
            self.stage.parent = self


        class Stage(object):
            """
            Show XR install issu stage
            
            .. attribute:: issu_error
            
            	ISSU Error
            	**type**\:   :py:class:`IsdErrorEtEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.IsdErrorEtEnum>`
            
            .. attribute:: issu_node_cnt
            
            	ISSU Node Count
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: issu_ready_node_cnt
            
            	ISSU Ready Node Count
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: issu_status
            
            	Abort Status
            	**type**\:   :py:class:`IsdIssuStatusEtEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.IsdIssuStatusEtEnum>`
            
            .. attribute:: percentage
            
            	Percentage
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: percentage
            
            .. attribute:: state
            
            	State
            	**type**\:   :py:class:`IsdStateEtEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.IsdStateEtEnum>`
            
            

            """

            _prefix = 'spirit-install-instmgr-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.issu_error = None
                self.issu_node_cnt = None
                self.issu_ready_node_cnt = None
                self.issu_status = None
                self.percentage = None
                self.state = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/Cisco-IOS-XR-spirit-install-instmgr-oper:issu/Cisco-IOS-XR-spirit-install-instmgr-oper:stage'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.issu_error is not None:
                    return True

                if self.issu_node_cnt is not None:
                    return True

                if self.issu_ready_node_cnt is not None:
                    return True

                if self.issu_status is not None:
                    return True

                if self.percentage is not None:
                    return True

                if self.state is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
                return meta._meta_table['SoftwareInstall.Issu.Stage']['meta_info']


        class Inventory(object):
            """
            Show XR install issu inventory
            
            .. attribute:: invinfo
            
            	invinfo
            	**type**\: list of    :py:class:`Invinfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.Issu.Inventory.Invinfo>`
            
            

            """

            _prefix = 'spirit-install-instmgr-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.invinfo = YList()
                self.invinfo.parent = self
                self.invinfo.name = 'invinfo'


            class Invinfo(object):
                """
                invinfo
                
                .. attribute:: issu_node_role
                
                	ISSU Node Role
                	**type**\:   :py:class:`IssuNodeRoleEtEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.IssuNodeRoleEtEnum>`
                
                .. attribute:: node_id
                
                	Node ID
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: node_role
                
                	Node role
                	**type**\:   :py:class:`NodeRoleEtEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.NodeRoleEtEnum>`
                
                .. attribute:: node_state
                
                	Node State
                	**type**\:   :py:class:`IssudirNodeStatusEtEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.IssudirNodeStatusEtEnum>`
                
                .. attribute:: node_type
                
                	Node Type
                	**type**\:   :py:class:`CardTypeEtEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.CardTypeEtEnum>`
                
                

                """

                _prefix = 'spirit-install-instmgr-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.issu_node_role = None
                    self.node_id = None
                    self.node_role = None
                    self.node_state = None
                    self.node_type = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/Cisco-IOS-XR-spirit-install-instmgr-oper:issu/Cisco-IOS-XR-spirit-install-instmgr-oper:inventory/Cisco-IOS-XR-spirit-install-instmgr-oper:invinfo'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.issu_node_role is not None:
                        return True

                    if self.node_id is not None:
                        return True

                    if self.node_role is not None:
                        return True

                    if self.node_state is not None:
                        return True

                    if self.node_type is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
                    return meta._meta_table['SoftwareInstall.Issu.Inventory.Invinfo']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/Cisco-IOS-XR-spirit-install-instmgr-oper:issu/Cisco-IOS-XR-spirit-install-instmgr-oper:inventory'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.invinfo is not None:
                    for child_ref in self.invinfo:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
                return meta._meta_table['SoftwareInstall.Issu.Inventory']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/Cisco-IOS-XR-spirit-install-instmgr-oper:issu'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.inventory is not None and self.inventory._has_data():
                return True

            if self.stage is not None and self.stage._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
            return meta._meta_table['SoftwareInstall.Issu']['meta_info']


    class Committed(object):
        """
        Show Committed packages installed
        
        .. attribute:: committed_package_info
        
        	committed package info
        	**type**\: list of    :py:class:`CommittedPackageInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.Committed.CommittedPackageInfo>`
        
        

        """

        _prefix = 'spirit-install-instmgr-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.committed_package_info = YList()
            self.committed_package_info.parent = self
            self.committed_package_info.name = 'committed_package_info'


        class CommittedPackageInfo(object):
            """
            committed package info
            
            .. attribute:: boot_partition_name
            
            	BootPartitionName
            	**type**\:  str
            
            .. attribute:: committed_packages
            
            	CommittedPackages
            	**type**\:  str
            
            .. attribute:: error_message
            
            	ErrorMessage
            	**type**\:  str
            
            .. attribute:: location
            
            	Location
            	**type**\:  str
            
            .. attribute:: node_type
            
            	NodeType
            	**type**\:  str
            
            .. attribute:: number_of_committed_packages
            
            	NumberOfCommittedPackages
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'spirit-install-instmgr-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.boot_partition_name = None
                self.committed_packages = None
                self.error_message = None
                self.location = None
                self.node_type = None
                self.number_of_committed_packages = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/Cisco-IOS-XR-spirit-install-instmgr-oper:committed/Cisco-IOS-XR-spirit-install-instmgr-oper:committed-package-info'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.boot_partition_name is not None:
                    return True

                if self.committed_packages is not None:
                    return True

                if self.error_message is not None:
                    return True

                if self.location is not None:
                    return True

                if self.node_type is not None:
                    return True

                if self.number_of_committed_packages is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
                return meta._meta_table['SoftwareInstall.Committed.CommittedPackageInfo']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/Cisco-IOS-XR-spirit-install-instmgr-oper:committed'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.committed_package_info is not None:
                for child_ref in self.committed_package_info:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
            return meta._meta_table['SoftwareInstall.Committed']['meta_info']


    class AllOperationsLog(object):
        """
        Show log file for all operations
        
        .. attribute:: detail
        
        	Show detailed log file for all operations
        	**type**\:   :py:class:`Detail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.AllOperationsLog.Detail>`
        
        .. attribute:: summary
        
        	Show summary log file for all operations
        	**type**\:   :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.AllOperationsLog.Summary>`
        
        

        """

        _prefix = 'spirit-install-instmgr-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.detail = SoftwareInstall.AllOperationsLog.Detail()
            self.detail.parent = self
            self.summary = SoftwareInstall.AllOperationsLog.Summary()
            self.summary.parent = self


        class Summary(object):
            """
            Show summary log file for all operations
            
            .. attribute:: log
            
            	log
            	**type**\:  str
            
            

            """

            _prefix = 'spirit-install-instmgr-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.log = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/Cisco-IOS-XR-spirit-install-instmgr-oper:all-operations-log/Cisco-IOS-XR-spirit-install-instmgr-oper:summary'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.log is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
                return meta._meta_table['SoftwareInstall.AllOperationsLog.Summary']['meta_info']


        class Detail(object):
            """
            Show detailed log file for all operations
            
            .. attribute:: log
            
            	log
            	**type**\:  str
            
            

            """

            _prefix = 'spirit-install-instmgr-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.log = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/Cisco-IOS-XR-spirit-install-instmgr-oper:all-operations-log/Cisco-IOS-XR-spirit-install-instmgr-oper:detail'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.log is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
                return meta._meta_table['SoftwareInstall.AllOperationsLog.Detail']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/Cisco-IOS-XR-spirit-install-instmgr-oper:all-operations-log'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.detail is not None and self.detail._has_data():
                return True

            if self.summary is not None and self.summary._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
            return meta._meta_table['SoftwareInstall.AllOperationsLog']['meta_info']


    class Packages(object):
        """
        Show the list of installed packages
        
        .. attribute:: package
        
        	Show the info for a installed package
        	**type**\: list of    :py:class:`Package <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.Packages.Package>`
        
        

        """

        _prefix = 'spirit-install-instmgr-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.package = YList()
            self.package.parent = self
            self.package.name = 'package'


        class Package(object):
            """
            Show the info for a installed package
            
            .. attribute:: package_name  <key>
            
            	Package name
            	**type**\:  str
            
            .. attribute:: brief
            
            	Show the info for a installed package
            	**type**\:   :py:class:`Brief <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.Packages.Package.Brief>`
            
            .. attribute:: detail
            
            	Show the deatil info for a installed package
            	**type**\:   :py:class:`Detail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.Packages.Package.Detail>`
            
            .. attribute:: verbose
            
            	Show the verbose info for a installed package
            	**type**\:   :py:class:`Verbose <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.Packages.Package.Verbose>`
            
            

            """

            _prefix = 'spirit-install-instmgr-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.package_name = None
                self.brief = SoftwareInstall.Packages.Package.Brief()
                self.brief.parent = self
                self.detail = SoftwareInstall.Packages.Package.Detail()
                self.detail.parent = self
                self.verbose = SoftwareInstall.Packages.Package.Verbose()
                self.verbose.parent = self


            class Verbose(object):
                """
                Show the verbose info for a installed package
                
                .. attribute:: log
                
                	log
                	**type**\:  str
                
                

                """

                _prefix = 'spirit-install-instmgr-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.log = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-spirit-install-instmgr-oper:verbose'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.log is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
                    return meta._meta_table['SoftwareInstall.Packages.Package.Verbose']['meta_info']


            class Brief(object):
                """
                Show the info for a installed package
                
                .. attribute:: log
                
                	log
                	**type**\:  str
                
                

                """

                _prefix = 'spirit-install-instmgr-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.log = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-spirit-install-instmgr-oper:brief'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.log is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
                    return meta._meta_table['SoftwareInstall.Packages.Package.Brief']['meta_info']


            class Detail(object):
                """
                Show the deatil info for a installed package
                
                .. attribute:: log
                
                	log
                	**type**\:  str
                
                

                """

                _prefix = 'spirit-install-instmgr-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.log = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-spirit-install-instmgr-oper:detail'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.log is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
                    return meta._meta_table['SoftwareInstall.Packages.Package.Detail']['meta_info']

            @property
            def _common_path(self):
                if self.package_name is None:
                    raise YPYModelError('Key property package_name is None')

                return '/Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/Cisco-IOS-XR-spirit-install-instmgr-oper:packages/Cisco-IOS-XR-spirit-install-instmgr-oper:package[Cisco-IOS-XR-spirit-install-instmgr-oper:package-name = ' + str(self.package_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.package_name is not None:
                    return True

                if self.brief is not None and self.brief._has_data():
                    return True

                if self.detail is not None and self.detail._has_data():
                    return True

                if self.verbose is not None and self.verbose._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
                return meta._meta_table['SoftwareInstall.Packages.Package']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/Cisco-IOS-XR-spirit-install-instmgr-oper:packages'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.package is not None:
                for child_ref in self.package:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
            return meta._meta_table['SoftwareInstall.Packages']['meta_info']


    class OperationLogs(object):
        """
        Show log file
        
        .. attribute:: operation_log
        
        	Show log file for the specified install ID
        	**type**\: list of    :py:class:`OperationLog <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.OperationLogs.OperationLog>`
        
        

        """

        _prefix = 'spirit-install-instmgr-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.operation_log = YList()
            self.operation_log.parent = self
            self.operation_log.name = 'operation_log'


        class OperationLog(object):
            """
            Show log file for the specified install ID
            
            .. attribute:: log_id  <key>
            
            	Log ID number
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: detail
            
            	Show detailed log file for the specified install ID
            	**type**\:   :py:class:`Detail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.OperationLogs.OperationLog.Detail>`
            
            .. attribute:: summary
            
            	Show summary log file for the specified install ID
            	**type**\:   :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.OperationLogs.OperationLog.Summary>`
            
            

            """

            _prefix = 'spirit-install-instmgr-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.log_id = None
                self.detail = SoftwareInstall.OperationLogs.OperationLog.Detail()
                self.detail.parent = self
                self.summary = SoftwareInstall.OperationLogs.OperationLog.Summary()
                self.summary.parent = self


            class Summary(object):
                """
                Show summary log file for the specified
                install ID
                
                .. attribute:: log
                
                	log
                	**type**\:  str
                
                

                """

                _prefix = 'spirit-install-instmgr-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.log = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-spirit-install-instmgr-oper:summary'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.log is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
                    return meta._meta_table['SoftwareInstall.OperationLogs.OperationLog.Summary']['meta_info']


            class Detail(object):
                """
                Show detailed log file for the specified
                install ID
                
                .. attribute:: log
                
                	log
                	**type**\:  str
                
                

                """

                _prefix = 'spirit-install-instmgr-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.log = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-spirit-install-instmgr-oper:detail'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.log is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
                    return meta._meta_table['SoftwareInstall.OperationLogs.OperationLog.Detail']['meta_info']

            @property
            def _common_path(self):
                if self.log_id is None:
                    raise YPYModelError('Key property log_id is None')

                return '/Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/Cisco-IOS-XR-spirit-install-instmgr-oper:operation-logs/Cisco-IOS-XR-spirit-install-instmgr-oper:operation-log[Cisco-IOS-XR-spirit-install-instmgr-oper:log-id = ' + str(self.log_id) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.log_id is not None:
                    return True

                if self.detail is not None and self.detail._has_data():
                    return True

                if self.summary is not None and self.summary._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
                return meta._meta_table['SoftwareInstall.OperationLogs.OperationLog']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/Cisco-IOS-XR-spirit-install-instmgr-oper:operation-logs'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.operation_log is not None:
                for child_ref in self.operation_log:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
            return meta._meta_table['SoftwareInstall.OperationLogs']['meta_info']


    class Repository(object):
        """
        Show packages stored in install software
        repositories
        
        .. attribute:: all
        
        	Show contents of all install software repositories
        	**type**\:   :py:class:`All <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.Repository.All>`
        
        .. attribute:: xr
        
        	Show install software repository for XR
        	**type**\:   :py:class:`Xr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.Repository.Xr>`
        
        

        """

        _prefix = 'spirit-install-instmgr-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.all = SoftwareInstall.Repository.All()
            self.all.parent = self
            self.xr = SoftwareInstall.Repository.Xr()
            self.xr.parent = self


        class Xr(object):
            """
            Show install software repository for XR
            
            .. attribute:: log
            
            	log
            	**type**\:  str
            
            

            """

            _prefix = 'spirit-install-instmgr-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.log = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/Cisco-IOS-XR-spirit-install-instmgr-oper:repository/Cisco-IOS-XR-spirit-install-instmgr-oper:xr'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.log is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
                return meta._meta_table['SoftwareInstall.Repository.Xr']['meta_info']


        class All(object):
            """
            Show contents of all install software
            repositories
            
            .. attribute:: log
            
            	log
            	**type**\:  str
            
            

            """

            _prefix = 'spirit-install-instmgr-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.log = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/Cisco-IOS-XR-spirit-install-instmgr-oper:repository/Cisco-IOS-XR-spirit-install-instmgr-oper:all'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.log is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
                return meta._meta_table['SoftwareInstall.Repository.All']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/Cisco-IOS-XR-spirit-install-instmgr-oper:repository'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.all is not None and self.all._has_data():
                return True

            if self.xr is not None and self.xr._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
            return meta._meta_table['SoftwareInstall.Repository']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-spirit-install-instmgr-oper:software-install'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.active is not None and self.active._has_data():
            return True

        if self.all_operations_log is not None and self.all_operations_log._has_data():
            return True

        if self.committed is not None and self.committed._has_data():
            return True

        if self.files is not None and self.files._has_data():
            return True

        if self.inactive is not None and self.inactive._has_data():
            return True

        if self.issu is not None and self.issu._has_data():
            return True

        if self.last_n_operation_logs is not None and self.last_n_operation_logs._has_data():
            return True

        if self.operation_logs is not None and self.operation_logs._has_data():
            return True

        if self.packages is not None and self.packages._has_data():
            return True

        if self.prepare is not None and self.prepare._has_data():
            return True

        if self.repository is not None and self.repository._has_data():
            return True

        if self.request is not None and self.request._has_data():
            return True

        if self.version is not None and self.version._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
        return meta._meta_table['SoftwareInstall']['meta_info']


