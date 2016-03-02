""" Cisco_IOS_XR_spirit_install_instmgr_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR spirit\-install\-instmgr package operational data.

This module contains definitions
for the following management objects\:
  software\-install\: Install operations info

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class CardTypeEt_Enum(Enum):
    """
    CardTypeEt_Enum

    card type

    """

    """

    Card RP

    """
    CARD_RP = 0

    """

    Card DRP

    """
    CARD_DRP = 1

    """

    Card LC

    """
    CARD_LC = 2

    """

    Card SC

    """
    CARD_SC = 3

    """

    Card SP

    """
    CARD_SP = 4

    """

    Card Other

    """
    CARD_OTHER = 5


    @staticmethod
    def _meta_info():
        from ydk.models.spirit._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
        return meta._meta_table['CardTypeEt_Enum']


class IsdErrorEt_Enum(Enum):
    """
    IsdErrorEt_Enum

    isd error

    """

    """

    ISD ERROR NONE

    """
    NONE = 0

    """

    ISD ERROR NOT COMPATIBLE

    """
    NOT_COMPATIBLE = 1

    """

    ISD ERROR NOT ENOUGH RESOURCE

    """
    NOT_ENOUGH_RESOURCE = 2

    """

    ISD ERROR NOT NSR READY

    """
    NOT_NSR_READY = 3

    """

    ISD ERROR NOT CONNECTED SDR SM

    """
    NOT_CONN_SDRSM = 4

    """

    ISD ERROR INST CMD INVALID

    """
    CMD_INVALID = 5

    """

    ISD ERROR INST LOAD PREP FAILURE

    """
    LOAD_PREP_FAIL = 6

    """

    ISD ERROR TIMEOUT

    """
    ERROR_TIMEOUT = 7

    """

    ISD ERROR NODE DOWN

    """
    ERR_NODE_DOWN = 8

    """

    ISD ERROR NODE NOT READY

    """
    NODE_NOT_READY = 9

    """

    ISD ERROR NODE NEW

    """
    ERR_NODE_NEW = 10

    """

    ISD ERROR CARD OIR

    """
    ERR_CARD_OIR = 11

    """

    ISD ERROR INVALID EVT

    """
    INVALID_EVT = 12

    """

    ISD ERROR DISCONN FROM CALVADOS

    """
    DISCONN_FROM_CALV = 13

    """

    ISD ERROR GSP DOWN

    """
    GSP_DOWN = 14

    """

    ISD ERROR ABORT BY ISM

    """
    ABORT_BY_ISM = 15

    """

    ISD ERROR RPFO

    """
    RPFO = 16

    """

    ISD ERROR PKG NULL

    """
    PKG_NULL = 17

    """

    ISD ERROR GENERAL

    """
    ERROR_GENERAL = 18

    """

    ISD ERROR FSA ERROR

    """
    FSA_ERROR = 19

    """

    ISD ERROR POST ISSU

    """
    ERR_POST_ISSU = 20

    """

    ISD ERROR ISSUDIR RESTART

    """
    ERR_ISSU_DIR_RESTART = 21


    @staticmethod
    def _meta_info():
        from ydk.models.spirit._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
        return meta._meta_table['IsdErrorEt_Enum']


class IsdIssuStatusEt_Enum(Enum):
    """
    IsdIssuStatusEt_Enum

    isd status

    """

    """

    ISSU STATUS OK

    """
    OK = 0

    """

    ISSU STATUS PREP DONE

    """
    PREP_DONE = 1

    """

    ISSU STATUS BIG BANG

    """
    BIG_BANG = 2

    """

    ISSU STATUS DONE

    """
    DONE = 3

    """

    ISSU STATUS ABORT

    """
    ABORT = 4

    """

    ISSU STATUS CMD REJECT

    """
    CMD_REJECT = 5

    """

    ISSU STATUS UNKNOWN

    """
    UNKNOWN = 6


    @staticmethod
    def _meta_info():
        from ydk.models.spirit._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
        return meta._meta_table['IsdIssuStatusEt_Enum']


class IsdStateEt_Enum(Enum):
    """
    IsdStateEt_Enum

    isd state

    """

    """

    ISSU ST NONE

    """
    NONE = 0

    """

    ISSU ST IDLE

    """
    IDLE = 1

    """

    ISSU ST INIT

    """
    INIT = 2

    """

    ISSU ST INIT DONE

    """
    INIT_DONE = 3

    """

    ISSU ST LOAD PREP

    """
    LOAD_PREP = 4

    """

    ISSU ST LOAD EXEC

    """
    LOAD_EXEC = 5

    """

    ISSU ST LOAD ISSU GO

    """
    LOAD_ISSU_GO = 6

    """

    ISSU ST LOAD DONE

    """
    LOAD_DONE = 7

    """

    ISSU ST RUN PREP

    """
    RUN_PREP = 8

    """

    ISSU ST RUN BIG BANG

    """
    BIG_BANG = 9

    """

    ISSU ST RUN DONE

    """
    RUN_DONE = 10

    """

    ISSU ST CLEANUP

    """
    CLEANUP = 11

    """

    ISSU ST CLEANUP DONE

    """
    CLEANUP_DONE = 12

    """

    ISSU ST ABORT

    """
    ABORT = 13

    """

    ISSU UNKNOWN STATE

    """
    UNKNOW_STATE = 14


    @staticmethod
    def _meta_info():
        from ydk.models.spirit._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
        return meta._meta_table['IsdStateEt_Enum']


class IssuNodeRoleEt_Enum(Enum):
    """
    IssuNodeRoleEt_Enum

    ISSU role

    """

    """

    Unknown

    """
    UNKNOWN_ROLE = 0

    """

    Primary

    """
    PRIMARY_ROLE = 1

    """

    Secondary

    """
    SECONDARY_ROLE = 2

    """

    Tertiary

    """
    TERTIARY_ROLE = 3


    @staticmethod
    def _meta_info():
        from ydk.models.spirit._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
        return meta._meta_table['IssuNodeRoleEt_Enum']


class IssudirNodeStatusEt_Enum(Enum):
    """
    IssudirNodeStatusEt_Enum

    ISSU node status

    """

    """

    Not ISSU Ready

    """
    NOT_ISSU_READY = 0

    """

    ISSU Ready

    """
    ISSU_READY = 1

    """

    ISSU Go

    """
    ISUS_GO = 2

    """

    Node Fail

    """
    NODE_FAIL = 3


    @staticmethod
    def _meta_info():
        from ydk.models.spirit._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
        return meta._meta_table['IssudirNodeStatusEt_Enum']


class NodeRoleEt_Enum(Enum):
    """
    NodeRoleEt_Enum

    node role

    """

    """

    Unknown

    """
    NODE_UNKNOWN = 0

    """

    Active

    """
    NODE_ACTIVE = 1

    """

    Standby

    """
    NODE_STANDBY = 2

    """

    Unusable

    """
    NODE_UNUSABLE = 3


    @staticmethod
    def _meta_info():
        from ydk.models.spirit._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
        return meta._meta_table['NodeRoleEt_Enum']



class SoftwareInstall(object):
    """
    Install operations info
    
    .. attribute:: active
    
    	Show active packages installed
    	**type**\: :py:class:`Active <ydk.models.spirit.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.Active>`
    
    .. attribute:: all_operations_log
    
    	Show log file for all operations
    	**type**\: :py:class:`AllOperationsLog <ydk.models.spirit.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.AllOperationsLog>`
    
    .. attribute:: committed
    
    	Show Committed packages installed
    	**type**\: :py:class:`Committed <ydk.models.spirit.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.Committed>`
    
    .. attribute:: files
    
    	Show information about an installed file
    	**type**\: :py:class:`Files <ydk.models.spirit.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.Files>`
    
    .. attribute:: inactive
    
    	Show XR inactive packages
    	**type**\: :py:class:`Inactive <ydk.models.spirit.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.Inactive>`
    
    .. attribute:: issu
    
    	ISSU operation
    	**type**\: :py:class:`Issu <ydk.models.spirit.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.Issu>`
    
    .. attribute:: last_n_operation_logs
    
    	Show log file for last n operations
    	**type**\: :py:class:`LastNOperationLogs <ydk.models.spirit.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.LastNOperationLogs>`
    
    .. attribute:: operation_logs
    
    	Show log file
    	**type**\: :py:class:`OperationLogs <ydk.models.spirit.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.OperationLogs>`
    
    .. attribute:: packages
    
    	Show the list of installed packages
    	**type**\: :py:class:`Packages <ydk.models.spirit.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.Packages>`
    
    .. attribute:: prepare
    
    	Show prepared packages ready for activation
    	**type**\: :py:class:`Prepare <ydk.models.spirit.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.Prepare>`
    
    .. attribute:: repository
    
    	Show packages stored in install software repositories
    	**type**\: :py:class:`Repository <ydk.models.spirit.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.Repository>`
    
    .. attribute:: request
    
    	Show current request
    	**type**\: :py:class:`Request <ydk.models.spirit.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.Request>`
    
    .. attribute:: version
    
    	Show install version
    	**type**\: :py:class:`Version <ydk.models.spirit.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.Version>`
    
    

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


    class Active(object):
        """
        Show active packages installed
        
        .. attribute:: active_package_info
        
        	active package info
        	**type**\: list of :py:class:`ActivePackageInfo <ydk.models.spirit.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.Active.ActivePackageInfo>`
        
        

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
            	**type**\: str
            
            .. attribute:: boot_partition_name
            
            	BootPartitionName
            	**type**\: str
            
            .. attribute:: error_message
            
            	ErrorMessage
            	**type**\: str
            
            .. attribute:: location
            
            	Location
            	**type**\: str
            
            .. attribute:: node_type
            
            	NodeType
            	**type**\: str
            
            .. attribute:: number_of_active_packages
            
            	NumberOfActivePackages
            	**type**\: int
            
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
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
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

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.spirit._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
                return meta._meta_table['SoftwareInstall.Active.ActivePackageInfo']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/Cisco-IOS-XR-spirit-install-instmgr-oper:active'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.active_package_info is not None:
                for child_ref in self.active_package_info:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.spirit._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
            return meta._meta_table['SoftwareInstall.Active']['meta_info']


    class AllOperationsLog(object):
        """
        Show log file for all operations
        
        .. attribute:: detail
        
        	Show detailed log file for all operations
        	**type**\: :py:class:`Detail <ydk.models.spirit.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.AllOperationsLog.Detail>`
        
        .. attribute:: summary
        
        	Show summary log file for all operations
        	**type**\: :py:class:`Summary <ydk.models.spirit.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.AllOperationsLog.Summary>`
        
        

        """

        _prefix = 'spirit-install-instmgr-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.detail = SoftwareInstall.AllOperationsLog.Detail()
            self.detail.parent = self
            self.summary = SoftwareInstall.AllOperationsLog.Summary()
            self.summary.parent = self


        class Detail(object):
            """
            Show detailed log file for all operations
            
            .. attribute:: log
            
            	log
            	**type**\: str
            
            

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
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.log is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.spirit._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
                return meta._meta_table['SoftwareInstall.AllOperationsLog.Detail']['meta_info']


        class Summary(object):
            """
            Show summary log file for all operations
            
            .. attribute:: log
            
            	log
            	**type**\: str
            
            

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
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.log is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.spirit._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
                return meta._meta_table['SoftwareInstall.AllOperationsLog.Summary']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/Cisco-IOS-XR-spirit-install-instmgr-oper:all-operations-log'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.detail is not None and self.detail._has_data():
                return True

            if self.detail is not None and self.detail.is_presence():
                return True

            if self.summary is not None and self.summary._has_data():
                return True

            if self.summary is not None and self.summary.is_presence():
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.spirit._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
            return meta._meta_table['SoftwareInstall.AllOperationsLog']['meta_info']


    class Committed(object):
        """
        Show Committed packages installed
        
        .. attribute:: committed_package_info
        
        	committed package info
        	**type**\: list of :py:class:`CommittedPackageInfo <ydk.models.spirit.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.Committed.CommittedPackageInfo>`
        
        

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
            	**type**\: str
            
            .. attribute:: committed_packages
            
            	CommittedPackages
            	**type**\: str
            
            .. attribute:: error_message
            
            	ErrorMessage
            	**type**\: str
            
            .. attribute:: location
            
            	Location
            	**type**\: str
            
            .. attribute:: node_type
            
            	NodeType
            	**type**\: str
            
            .. attribute:: number_of_committed_packages
            
            	NumberOfCommittedPackages
            	**type**\: int
            
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
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
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

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.spirit._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
                return meta._meta_table['SoftwareInstall.Committed.CommittedPackageInfo']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/Cisco-IOS-XR-spirit-install-instmgr-oper:committed'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.committed_package_info is not None:
                for child_ref in self.committed_package_info:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.spirit._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
            return meta._meta_table['SoftwareInstall.Committed']['meta_info']


    class Files(object):
        """
        Show information about an installed file
        
        .. attribute:: file
        
        	Show information about an installed file
        	**type**\: list of :py:class:`File <ydk.models.spirit.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.Files.File>`
        
        

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
            
            .. attribute:: file_name
            
            	File name
            	**type**\: str
            
            .. attribute:: brief
            
            	Show information about an installed file
            	**type**\: :py:class:`Brief <ydk.models.spirit.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.Files.File.Brief>`
            
            .. attribute:: detail
            
            	Show detail information about an installed file
            	**type**\: :py:class:`Detail <ydk.models.spirit.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.Files.File.Detail>`
            
            

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
                	**type**\: str
                
                

                """

                _prefix = 'spirit-install-instmgr-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.log = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-spirit-install-instmgr-oper:brief'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.log is not None:
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.spirit._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
                    return meta._meta_table['SoftwareInstall.Files.File.Brief']['meta_info']


            class Detail(object):
                """
                Show detail information about an installed
                file
                
                .. attribute:: log
                
                	log
                	**type**\: str
                
                

                """

                _prefix = 'spirit-install-instmgr-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.log = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-spirit-install-instmgr-oper:detail'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.log is not None:
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.spirit._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
                    return meta._meta_table['SoftwareInstall.Files.File.Detail']['meta_info']

            @property
            def _common_path(self):
                if self.file_name is None:
                    raise YPYDataValidationError('Key property file_name is None')

                return '/Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/Cisco-IOS-XR-spirit-install-instmgr-oper:files/Cisco-IOS-XR-spirit-install-instmgr-oper:file[Cisco-IOS-XR-spirit-install-instmgr-oper:file-name = ' + str(self.file_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.file_name is not None:
                    return True

                if self.brief is not None and self.brief._has_data():
                    return True

                if self.brief is not None and self.brief.is_presence():
                    return True

                if self.detail is not None and self.detail._has_data():
                    return True

                if self.detail is not None and self.detail.is_presence():
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.spirit._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
                return meta._meta_table['SoftwareInstall.Files.File']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/Cisco-IOS-XR-spirit-install-instmgr-oper:files'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.file is not None:
                for child_ref in self.file:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.spirit._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
            return meta._meta_table['SoftwareInstall.Files']['meta_info']


    class Inactive(object):
        """
        Show XR inactive packages
        
        .. attribute:: log
        
        	log
        	**type**\: str
        
        

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
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.log is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.spirit._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
            return meta._meta_table['SoftwareInstall.Inactive']['meta_info']


    class Issu(object):
        """
        ISSU operation
        
        .. attribute:: inventory
        
        	Show XR install issu inventory
        	**type**\: :py:class:`Inventory <ydk.models.spirit.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.Issu.Inventory>`
        
        .. attribute:: stage
        
        	Show XR install issu stage
        	**type**\: :py:class:`Stage <ydk.models.spirit.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.Issu.Stage>`
        
        

        """

        _prefix = 'spirit-install-instmgr-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.inventory = SoftwareInstall.Issu.Inventory()
            self.inventory.parent = self
            self.stage = SoftwareInstall.Issu.Stage()
            self.stage.parent = self


        class Inventory(object):
            """
            Show XR install issu inventory
            
            .. attribute:: invinfo
            
            	invinfo
            	**type**\: list of :py:class:`Invinfo <ydk.models.spirit.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.Issu.Inventory.Invinfo>`
            
            

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
                	**type**\: :py:class:`IssuNodeRoleEt_Enum <ydk.models.spirit.Cisco_IOS_XR_spirit_install_instmgr_oper.IssuNodeRoleEt_Enum>`
                
                .. attribute:: node_id
                
                	Node ID
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: node_role
                
                	Node role
                	**type**\: :py:class:`NodeRoleEt_Enum <ydk.models.spirit.Cisco_IOS_XR_spirit_install_instmgr_oper.NodeRoleEt_Enum>`
                
                .. attribute:: node_state
                
                	Node State
                	**type**\: :py:class:`IssudirNodeStatusEt_Enum <ydk.models.spirit.Cisco_IOS_XR_spirit_install_instmgr_oper.IssudirNodeStatusEt_Enum>`
                
                .. attribute:: node_type
                
                	Node Type
                	**type**\: :py:class:`CardTypeEt_Enum <ydk.models.spirit.Cisco_IOS_XR_spirit_install_instmgr_oper.CardTypeEt_Enum>`
                
                

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
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
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

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.spirit._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
                    return meta._meta_table['SoftwareInstall.Issu.Inventory.Invinfo']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/Cisco-IOS-XR-spirit-install-instmgr-oper:issu/Cisco-IOS-XR-spirit-install-instmgr-oper:inventory'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.invinfo is not None:
                    for child_ref in self.invinfo:
                        if child_ref._has_data():
                            return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.spirit._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
                return meta._meta_table['SoftwareInstall.Issu.Inventory']['meta_info']


        class Stage(object):
            """
            Show XR install issu stage
            
            .. attribute:: issu_error
            
            	ISSU Error
            	**type**\: :py:class:`IsdErrorEt_Enum <ydk.models.spirit.Cisco_IOS_XR_spirit_install_instmgr_oper.IsdErrorEt_Enum>`
            
            .. attribute:: issu_node_cnt
            
            	ISSU Node Count
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: issu_ready_node_cnt
            
            	ISSU Ready Node Count
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: issu_status
            
            	Abort Status
            	**type**\: :py:class:`IsdIssuStatusEt_Enum <ydk.models.spirit.Cisco_IOS_XR_spirit_install_instmgr_oper.IsdIssuStatusEt_Enum>`
            
            .. attribute:: percentage
            
            	Percentage
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: state
            
            	State
            	**type**\: :py:class:`IsdStateEt_Enum <ydk.models.spirit.Cisco_IOS_XR_spirit_install_instmgr_oper.IsdStateEt_Enum>`
            
            

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
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
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

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.spirit._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
                return meta._meta_table['SoftwareInstall.Issu.Stage']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/Cisco-IOS-XR-spirit-install-instmgr-oper:issu'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.inventory is not None and self.inventory._has_data():
                return True

            if self.inventory is not None and self.inventory.is_presence():
                return True

            if self.stage is not None and self.stage._has_data():
                return True

            if self.stage is not None and self.stage.is_presence():
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.spirit._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
            return meta._meta_table['SoftwareInstall.Issu']['meta_info']


    class LastNOperationLogs(object):
        """
        Show log file for last n operations
        
        .. attribute:: last_n_operation_log
        
        	Show log file of last n operations
        	**type**\: list of :py:class:`LastNOperationLog <ydk.models.spirit.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.LastNOperationLogs.LastNOperationLog>`
        
        

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
            
            .. attribute:: last_n_logs
            
            	Last N opeartion logs
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: detail
            
            	Show detailed log file for last n operations
            	**type**\: :py:class:`Detail <ydk.models.spirit.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.LastNOperationLogs.LastNOperationLog.Detail>`
            
            .. attribute:: summary
            
            	Show summary log file for last n operations
            	**type**\: :py:class:`Summary <ydk.models.spirit.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.LastNOperationLogs.LastNOperationLog.Summary>`
            
            

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


            class Detail(object):
                """
                Show detailed log file for last n operations
                
                .. attribute:: log
                
                	log
                	**type**\: str
                
                

                """

                _prefix = 'spirit-install-instmgr-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.log = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-spirit-install-instmgr-oper:detail'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.log is not None:
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.spirit._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
                    return meta._meta_table['SoftwareInstall.LastNOperationLogs.LastNOperationLog.Detail']['meta_info']


            class Summary(object):
                """
                Show summary log file for last n operations
                
                .. attribute:: log
                
                	log
                	**type**\: str
                
                

                """

                _prefix = 'spirit-install-instmgr-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.log = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-spirit-install-instmgr-oper:summary'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.log is not None:
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.spirit._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
                    return meta._meta_table['SoftwareInstall.LastNOperationLogs.LastNOperationLog.Summary']['meta_info']

            @property
            def _common_path(self):
                if self.last_n_logs is None:
                    raise YPYDataValidationError('Key property last_n_logs is None')

                return '/Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/Cisco-IOS-XR-spirit-install-instmgr-oper:last-n-operation-logs/Cisco-IOS-XR-spirit-install-instmgr-oper:last-n-operation-log[Cisco-IOS-XR-spirit-install-instmgr-oper:last-n-logs = ' + str(self.last_n_logs) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.last_n_logs is not None:
                    return True

                if self.detail is not None and self.detail._has_data():
                    return True

                if self.detail is not None and self.detail.is_presence():
                    return True

                if self.summary is not None and self.summary._has_data():
                    return True

                if self.summary is not None and self.summary.is_presence():
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.spirit._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
                return meta._meta_table['SoftwareInstall.LastNOperationLogs.LastNOperationLog']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/Cisco-IOS-XR-spirit-install-instmgr-oper:last-n-operation-logs'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.last_n_operation_log is not None:
                for child_ref in self.last_n_operation_log:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.spirit._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
            return meta._meta_table['SoftwareInstall.LastNOperationLogs']['meta_info']


    class OperationLogs(object):
        """
        Show log file
        
        .. attribute:: operation_log
        
        	Show log file for the specified install ID
        	**type**\: list of :py:class:`OperationLog <ydk.models.spirit.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.OperationLogs.OperationLog>`
        
        

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
            
            .. attribute:: log_id
            
            	Log ID number
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: detail
            
            	Show detailed log file for the specified install ID
            	**type**\: :py:class:`Detail <ydk.models.spirit.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.OperationLogs.OperationLog.Detail>`
            
            .. attribute:: summary
            
            	Show summary log file for the specified install ID
            	**type**\: :py:class:`Summary <ydk.models.spirit.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.OperationLogs.OperationLog.Summary>`
            
            

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


            class Detail(object):
                """
                Show detailed log file for the specified
                install ID
                
                .. attribute:: log
                
                	log
                	**type**\: str
                
                

                """

                _prefix = 'spirit-install-instmgr-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.log = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-spirit-install-instmgr-oper:detail'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.log is not None:
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.spirit._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
                    return meta._meta_table['SoftwareInstall.OperationLogs.OperationLog.Detail']['meta_info']


            class Summary(object):
                """
                Show summary log file for the specified
                install ID
                
                .. attribute:: log
                
                	log
                	**type**\: str
                
                

                """

                _prefix = 'spirit-install-instmgr-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.log = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-spirit-install-instmgr-oper:summary'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.log is not None:
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.spirit._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
                    return meta._meta_table['SoftwareInstall.OperationLogs.OperationLog.Summary']['meta_info']

            @property
            def _common_path(self):
                if self.log_id is None:
                    raise YPYDataValidationError('Key property log_id is None')

                return '/Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/Cisco-IOS-XR-spirit-install-instmgr-oper:operation-logs/Cisco-IOS-XR-spirit-install-instmgr-oper:operation-log[Cisco-IOS-XR-spirit-install-instmgr-oper:log-id = ' + str(self.log_id) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.log_id is not None:
                    return True

                if self.detail is not None and self.detail._has_data():
                    return True

                if self.detail is not None and self.detail.is_presence():
                    return True

                if self.summary is not None and self.summary._has_data():
                    return True

                if self.summary is not None and self.summary.is_presence():
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.spirit._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
                return meta._meta_table['SoftwareInstall.OperationLogs.OperationLog']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/Cisco-IOS-XR-spirit-install-instmgr-oper:operation-logs'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.operation_log is not None:
                for child_ref in self.operation_log:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.spirit._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
            return meta._meta_table['SoftwareInstall.OperationLogs']['meta_info']


    class Packages(object):
        """
        Show the list of installed packages
        
        .. attribute:: package
        
        	Show the info for a installed package
        	**type**\: list of :py:class:`Package <ydk.models.spirit.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.Packages.Package>`
        
        

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
            
            .. attribute:: package_name
            
            	Package name
            	**type**\: str
            
            .. attribute:: brief
            
            	Show the info for a installed package
            	**type**\: :py:class:`Brief <ydk.models.spirit.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.Packages.Package.Brief>`
            
            .. attribute:: detail
            
            	Show the deatil info for a installed package
            	**type**\: :py:class:`Detail <ydk.models.spirit.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.Packages.Package.Detail>`
            
            .. attribute:: verbose
            
            	Show the verbose info for a installed package
            	**type**\: :py:class:`Verbose <ydk.models.spirit.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.Packages.Package.Verbose>`
            
            

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


            class Brief(object):
                """
                Show the info for a installed package
                
                .. attribute:: log
                
                	log
                	**type**\: str
                
                

                """

                _prefix = 'spirit-install-instmgr-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.log = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-spirit-install-instmgr-oper:brief'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.log is not None:
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.spirit._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
                    return meta._meta_table['SoftwareInstall.Packages.Package.Brief']['meta_info']


            class Detail(object):
                """
                Show the deatil info for a installed package
                
                .. attribute:: log
                
                	log
                	**type**\: str
                
                

                """

                _prefix = 'spirit-install-instmgr-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.log = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-spirit-install-instmgr-oper:detail'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.log is not None:
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.spirit._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
                    return meta._meta_table['SoftwareInstall.Packages.Package.Detail']['meta_info']


            class Verbose(object):
                """
                Show the verbose info for a installed package
                
                .. attribute:: log
                
                	log
                	**type**\: str
                
                

                """

                _prefix = 'spirit-install-instmgr-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.log = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-spirit-install-instmgr-oper:verbose'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.log is not None:
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.spirit._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
                    return meta._meta_table['SoftwareInstall.Packages.Package.Verbose']['meta_info']

            @property
            def _common_path(self):
                if self.package_name is None:
                    raise YPYDataValidationError('Key property package_name is None')

                return '/Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/Cisco-IOS-XR-spirit-install-instmgr-oper:packages/Cisco-IOS-XR-spirit-install-instmgr-oper:package[Cisco-IOS-XR-spirit-install-instmgr-oper:package-name = ' + str(self.package_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.package_name is not None:
                    return True

                if self.brief is not None and self.brief._has_data():
                    return True

                if self.brief is not None and self.brief.is_presence():
                    return True

                if self.detail is not None and self.detail._has_data():
                    return True

                if self.detail is not None and self.detail.is_presence():
                    return True

                if self.verbose is not None and self.verbose._has_data():
                    return True

                if self.verbose is not None and self.verbose.is_presence():
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.spirit._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
                return meta._meta_table['SoftwareInstall.Packages.Package']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/Cisco-IOS-XR-spirit-install-instmgr-oper:packages'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.package is not None:
                for child_ref in self.package:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.spirit._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
            return meta._meta_table['SoftwareInstall.Packages']['meta_info']


    class Prepare(object):
        """
        Show prepared packages ready for activation
        
        .. attribute:: log
        
        	log
        	**type**\: str
        
        

        """

        _prefix = 'spirit-install-instmgr-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.log = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/Cisco-IOS-XR-spirit-install-instmgr-oper:prepare'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.log is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.spirit._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
            return meta._meta_table['SoftwareInstall.Prepare']['meta_info']


    class Repository(object):
        """
        Show packages stored in install software
        repositories
        
        .. attribute:: all
        
        	Show contents of all install software repositories
        	**type**\: :py:class:`All <ydk.models.spirit.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.Repository.All>`
        
        .. attribute:: xr
        
        	Show install software repository for XR
        	**type**\: :py:class:`Xr <ydk.models.spirit.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.Repository.Xr>`
        
        

        """

        _prefix = 'spirit-install-instmgr-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.all = SoftwareInstall.Repository.All()
            self.all.parent = self
            self.xr = SoftwareInstall.Repository.Xr()
            self.xr.parent = self


        class All(object):
            """
            Show contents of all install software
            repositories
            
            .. attribute:: log
            
            	log
            	**type**\: str
            
            

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
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.log is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.spirit._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
                return meta._meta_table['SoftwareInstall.Repository.All']['meta_info']


        class Xr(object):
            """
            Show install software repository for XR
            
            .. attribute:: log
            
            	log
            	**type**\: str
            
            

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
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.log is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.spirit._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
                return meta._meta_table['SoftwareInstall.Repository.Xr']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/Cisco-IOS-XR-spirit-install-instmgr-oper:repository'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.all is not None and self.all._has_data():
                return True

            if self.all is not None and self.all.is_presence():
                return True

            if self.xr is not None and self.xr._has_data():
                return True

            if self.xr is not None and self.xr.is_presence():
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.spirit._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
            return meta._meta_table['SoftwareInstall.Repository']['meta_info']


    class Request(object):
        """
        Show current request
        
        .. attribute:: log
        
        	log
        	**type**\: str
        
        

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
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.log is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.spirit._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
            return meta._meta_table['SoftwareInstall.Request']['meta_info']


    class Version(object):
        """
        Show install version
        
        .. attribute:: log
        
        	log
        	**type**\: str
        
        

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
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.log is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.spirit._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
            return meta._meta_table['SoftwareInstall.Version']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-spirit-install-instmgr-oper:software-install'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.active is not None and self.active._has_data():
            return True

        if self.active is not None and self.active.is_presence():
            return True

        if self.all_operations_log is not None and self.all_operations_log._has_data():
            return True

        if self.all_operations_log is not None and self.all_operations_log.is_presence():
            return True

        if self.committed is not None and self.committed._has_data():
            return True

        if self.committed is not None and self.committed.is_presence():
            return True

        if self.files is not None and self.files._has_data():
            return True

        if self.files is not None and self.files.is_presence():
            return True

        if self.inactive is not None and self.inactive._has_data():
            return True

        if self.inactive is not None and self.inactive.is_presence():
            return True

        if self.issu is not None and self.issu._has_data():
            return True

        if self.issu is not None and self.issu.is_presence():
            return True

        if self.last_n_operation_logs is not None and self.last_n_operation_logs._has_data():
            return True

        if self.last_n_operation_logs is not None and self.last_n_operation_logs.is_presence():
            return True

        if self.operation_logs is not None and self.operation_logs._has_data():
            return True

        if self.operation_logs is not None and self.operation_logs.is_presence():
            return True

        if self.packages is not None and self.packages._has_data():
            return True

        if self.packages is not None and self.packages.is_presence():
            return True

        if self.prepare is not None and self.prepare._has_data():
            return True

        if self.prepare is not None and self.prepare.is_presence():
            return True

        if self.repository is not None and self.repository._has_data():
            return True

        if self.repository is not None and self.repository.is_presence():
            return True

        if self.request is not None and self.request._has_data():
            return True

        if self.request is not None and self.request.is_presence():
            return True

        if self.version is not None and self.version._has_data():
            return True

        if self.version is not None and self.version.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.spirit._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
        return meta._meta_table['SoftwareInstall']['meta_info']


