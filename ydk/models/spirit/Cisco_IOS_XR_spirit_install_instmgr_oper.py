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



class CardTypeEtEnum(Enum):
    """
    CardTypeEtEnum

    card type

    .. data:: CARD_RP = 0

    	Card RP

    .. data:: CARD_DRP = 1

    	Card DRP

    .. data:: CARD_LC = 2

    	Card LC

    .. data:: CARD_SC = 3

    	Card SC

    .. data:: CARD_SP = 4

    	Card SP

    .. data:: CARD_OTHER = 5

    	Card Other

    """

    CARD_RP = 0

    CARD_DRP = 1

    CARD_LC = 2

    CARD_SC = 3

    CARD_SP = 4

    CARD_OTHER = 5


    @staticmethod
    def _meta_info():
        from ydk.models.spirit._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
        return meta._meta_table['CardTypeEtEnum']


class IsdErrorEtEnum(Enum):
    """
    IsdErrorEtEnum

    isd error

    .. data:: NONE = 0

    	ISD ERROR NONE

    .. data:: NOT_COMPATIBLE = 1

    	ISD ERROR NOT COMPATIBLE

    .. data:: NOT_ENOUGH_RESOURCE = 2

    	ISD ERROR NOT ENOUGH RESOURCE

    .. data:: NOT_NSR_READY = 3

    	ISD ERROR NOT NSR READY

    .. data:: NOT_CONN_SDRSM = 4

    	ISD ERROR NOT CONNECTED SDR SM

    .. data:: CMD_INVALID = 5

    	ISD ERROR INST CMD INVALID

    .. data:: LOAD_PREP_FAIL = 6

    	ISD ERROR INST LOAD PREP FAILURE

    .. data:: ERROR_TIMEOUT = 7

    	ISD ERROR TIMEOUT

    .. data:: ERR_NODE_DOWN = 8

    	ISD ERROR NODE DOWN

    .. data:: NODE_NOT_READY = 9

    	ISD ERROR NODE NOT READY

    .. data:: ERR_NODE_NEW = 10

    	ISD ERROR NODE NEW

    .. data:: ERR_CARD_OIR = 11

    	ISD ERROR CARD OIR

    .. data:: INVALID_EVT = 12

    	ISD ERROR INVALID EVT

    .. data:: DISCONN_FROM_CALV = 13

    	ISD ERROR DISCONN FROM CALVADOS

    .. data:: GSP_DOWN = 14

    	ISD ERROR GSP DOWN

    .. data:: ABORT_BY_ISM = 15

    	ISD ERROR ABORT BY ISM

    .. data:: RPFO = 16

    	ISD ERROR RPFO

    .. data:: PKG_NULL = 17

    	ISD ERROR PKG NULL

    .. data:: ERROR_GENERAL = 18

    	ISD ERROR GENERAL

    .. data:: FSA_ERROR = 19

    	ISD ERROR FSA ERROR

    .. data:: ERR_POST_ISSU = 20

    	ISD ERROR POST ISSU

    .. data:: ERR_ISSU_DIR_RESTART = 21

    	ISD ERROR ISSUDIR RESTART

    """

    NONE = 0

    NOT_COMPATIBLE = 1

    NOT_ENOUGH_RESOURCE = 2

    NOT_NSR_READY = 3

    NOT_CONN_SDRSM = 4

    CMD_INVALID = 5

    LOAD_PREP_FAIL = 6

    ERROR_TIMEOUT = 7

    ERR_NODE_DOWN = 8

    NODE_NOT_READY = 9

    ERR_NODE_NEW = 10

    ERR_CARD_OIR = 11

    INVALID_EVT = 12

    DISCONN_FROM_CALV = 13

    GSP_DOWN = 14

    ABORT_BY_ISM = 15

    RPFO = 16

    PKG_NULL = 17

    ERROR_GENERAL = 18

    FSA_ERROR = 19

    ERR_POST_ISSU = 20

    ERR_ISSU_DIR_RESTART = 21


    @staticmethod
    def _meta_info():
        from ydk.models.spirit._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
        return meta._meta_table['IsdErrorEtEnum']


class IsdIssuStatusEtEnum(Enum):
    """
    IsdIssuStatusEtEnum

    isd status

    .. data:: OK = 0

    	ISSU STATUS OK

    .. data:: PREP_DONE = 1

    	ISSU STATUS PREP DONE

    .. data:: BIG_BANG = 2

    	ISSU STATUS BIG BANG

    .. data:: DONE = 3

    	ISSU STATUS DONE

    .. data:: ABORT = 4

    	ISSU STATUS ABORT

    .. data:: CMD_REJECT = 5

    	ISSU STATUS CMD REJECT

    .. data:: UNKNOWN = 6

    	ISSU STATUS UNKNOWN

    """

    OK = 0

    PREP_DONE = 1

    BIG_BANG = 2

    DONE = 3

    ABORT = 4

    CMD_REJECT = 5

    UNKNOWN = 6


    @staticmethod
    def _meta_info():
        from ydk.models.spirit._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
        return meta._meta_table['IsdIssuStatusEtEnum']


class IsdStateEtEnum(Enum):
    """
    IsdStateEtEnum

    isd state

    .. data:: NONE = 0

    	ISSU ST NONE

    .. data:: IDLE = 1

    	ISSU ST IDLE

    .. data:: INIT = 2

    	ISSU ST INIT

    .. data:: INIT_DONE = 3

    	ISSU ST INIT DONE

    .. data:: LOAD_PREP = 4

    	ISSU ST LOAD PREP

    .. data:: LOAD_EXEC = 5

    	ISSU ST LOAD EXEC

    .. data:: LOAD_ISSU_GO = 6

    	ISSU ST LOAD ISSU GO

    .. data:: LOAD_DONE = 7

    	ISSU ST LOAD DONE

    .. data:: RUN_PREP = 8

    	ISSU ST RUN PREP

    .. data:: BIG_BANG = 9

    	ISSU ST RUN BIG BANG

    .. data:: RUN_DONE = 10

    	ISSU ST RUN DONE

    .. data:: CLEANUP = 11

    	ISSU ST CLEANUP

    .. data:: CLEANUP_DONE = 12

    	ISSU ST CLEANUP DONE

    .. data:: ABORT = 13

    	ISSU ST ABORT

    .. data:: UNKNOW_STATE = 14

    	ISSU UNKNOWN STATE

    """

    NONE = 0

    IDLE = 1

    INIT = 2

    INIT_DONE = 3

    LOAD_PREP = 4

    LOAD_EXEC = 5

    LOAD_ISSU_GO = 6

    LOAD_DONE = 7

    RUN_PREP = 8

    BIG_BANG = 9

    RUN_DONE = 10

    CLEANUP = 11

    CLEANUP_DONE = 12

    ABORT = 13

    UNKNOW_STATE = 14


    @staticmethod
    def _meta_info():
        from ydk.models.spirit._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
        return meta._meta_table['IsdStateEtEnum']


class IssuNodeRoleEtEnum(Enum):
    """
    IssuNodeRoleEtEnum

    ISSU role

    .. data:: UNKNOWN_ROLE = 0

    	Unknown

    .. data:: PRIMARY_ROLE = 1

    	Primary

    .. data:: SECONDARY_ROLE = 2

    	Secondary

    .. data:: TERTIARY_ROLE = 3

    	Tertiary

    """

    UNKNOWN_ROLE = 0

    PRIMARY_ROLE = 1

    SECONDARY_ROLE = 2

    TERTIARY_ROLE = 3


    @staticmethod
    def _meta_info():
        from ydk.models.spirit._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
        return meta._meta_table['IssuNodeRoleEtEnum']


class IssudirNodeStatusEtEnum(Enum):
    """
    IssudirNodeStatusEtEnum

    ISSU node status

    .. data:: NOT_ISSU_READY = 0

    	Not ISSU Ready

    .. data:: ISSU_READY = 1

    	ISSU Ready

    .. data:: ISUS_GO = 2

    	ISSU Go

    .. data:: NODE_FAIL = 3

    	Node Fail

    """

    NOT_ISSU_READY = 0

    ISSU_READY = 1

    ISUS_GO = 2

    NODE_FAIL = 3


    @staticmethod
    def _meta_info():
        from ydk.models.spirit._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
        return meta._meta_table['IssudirNodeStatusEtEnum']


class NodeRoleEtEnum(Enum):
    """
    NodeRoleEtEnum

    node role

    .. data:: NODE_UNKNOWN = 0

    	Unknown

    .. data:: NODE_ACTIVE = 1

    	Active

    .. data:: NODE_STANDBY = 2

    	Standby

    .. data:: NODE_UNUSABLE = 3

    	Unusable

    """

    NODE_UNKNOWN = 0

    NODE_ACTIVE = 1

    NODE_STANDBY = 2

    NODE_UNUSABLE = 3


    @staticmethod
    def _meta_info():
        from ydk.models.spirit._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
        return meta._meta_table['NodeRoleEtEnum']



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
            if self.active_package_info is not None:
                for child_ref in self.active_package_info:
                    if child_ref._has_data():
                        return True

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
                if self.log is not None:
                    return True

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
                if self.log is not None:
                    return True

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
            if self.detail is not None and self.detail._has_data():
                return True

            if self.summary is not None and self.summary._has_data():
                return True

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
            if self.committed_package_info is not None:
                for child_ref in self.committed_package_info:
                    if child_ref._has_data():
                        return True

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
                    if self.log is not None:
                        return True

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
                    if self.log is not None:
                        return True

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
                if self.file_name is not None:
                    return True

                if self.brief is not None and self.brief._has_data():
                    return True

                if self.detail is not None and self.detail._has_data():
                    return True

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
            if self.file is not None:
                for child_ref in self.file:
                    if child_ref._has_data():
                        return True

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
            if self.log is not None:
                return True

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
                	**type**\: :py:class:`IssuNodeRoleEtEnum <ydk.models.spirit.Cisco_IOS_XR_spirit_install_instmgr_oper.IssuNodeRoleEtEnum>`
                
                .. attribute:: node_id
                
                	Node ID
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: node_role
                
                	Node role
                	**type**\: :py:class:`NodeRoleEtEnum <ydk.models.spirit.Cisco_IOS_XR_spirit_install_instmgr_oper.NodeRoleEtEnum>`
                
                .. attribute:: node_state
                
                	Node State
                	**type**\: :py:class:`IssudirNodeStatusEtEnum <ydk.models.spirit.Cisco_IOS_XR_spirit_install_instmgr_oper.IssudirNodeStatusEtEnum>`
                
                .. attribute:: node_type
                
                	Node Type
                	**type**\: :py:class:`CardTypeEtEnum <ydk.models.spirit.Cisco_IOS_XR_spirit_install_instmgr_oper.CardTypeEtEnum>`
                
                

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
                if self.invinfo is not None:
                    for child_ref in self.invinfo:
                        if child_ref._has_data():
                            return True

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
            	**type**\: :py:class:`IsdErrorEtEnum <ydk.models.spirit.Cisco_IOS_XR_spirit_install_instmgr_oper.IsdErrorEtEnum>`
            
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
            	**type**\: :py:class:`IsdIssuStatusEtEnum <ydk.models.spirit.Cisco_IOS_XR_spirit_install_instmgr_oper.IsdIssuStatusEtEnum>`
            
            .. attribute:: percentage
            
            	Percentage
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: state
            
            	State
            	**type**\: :py:class:`IsdStateEtEnum <ydk.models.spirit.Cisco_IOS_XR_spirit_install_instmgr_oper.IsdStateEtEnum>`
            
            

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
            if self.inventory is not None and self.inventory._has_data():
                return True

            if self.stage is not None and self.stage._has_data():
                return True

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
                    if self.log is not None:
                        return True

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
                    if self.log is not None:
                        return True

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
                if self.last_n_logs is not None:
                    return True

                if self.detail is not None and self.detail._has_data():
                    return True

                if self.summary is not None and self.summary._has_data():
                    return True

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
            if self.last_n_operation_log is not None:
                for child_ref in self.last_n_operation_log:
                    if child_ref._has_data():
                        return True

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
                    if self.log is not None:
                        return True

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
                    if self.log is not None:
                        return True

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
                if self.log_id is not None:
                    return True

                if self.detail is not None and self.detail._has_data():
                    return True

                if self.summary is not None and self.summary._has_data():
                    return True

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
            if self.operation_log is not None:
                for child_ref in self.operation_log:
                    if child_ref._has_data():
                        return True

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
                    if self.log is not None:
                        return True

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
                    if self.log is not None:
                        return True

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
                    if self.log is not None:
                        return True

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
            if self.package is not None:
                for child_ref in self.package:
                    if child_ref._has_data():
                        return True

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
            if self.log is not None:
                return True

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
                if self.log is not None:
                    return True

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
                if self.log is not None:
                    return True

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
            if self.all is not None and self.all._has_data():
                return True

            if self.xr is not None and self.xr._has_data():
                return True

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
            if self.log is not None:
                return True

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
            if self.log is not None:
                return True

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
        from ydk.models.spirit._meta import _Cisco_IOS_XR_spirit_install_instmgr_oper as meta
        return meta._meta_table['SoftwareInstall']['meta_info']


