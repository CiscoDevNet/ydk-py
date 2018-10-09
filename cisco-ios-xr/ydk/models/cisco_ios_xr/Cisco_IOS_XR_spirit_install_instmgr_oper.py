""" Cisco_IOS_XR_spirit_install_instmgr_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR spirit\-install\-instmgr package operational data.

This module contains definitions
for the following management objects\:
  software\-install\: Install operations info

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CardTypeEt(Enum):
    """
    CardTypeEt (Enum Class)

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

    card_rp = Enum.YLeaf(0, "card-rp")

    card_drp = Enum.YLeaf(1, "card-drp")

    card_lc = Enum.YLeaf(2, "card-lc")

    card_sc = Enum.YLeaf(3, "card-sc")

    card_sp = Enum.YLeaf(4, "card-sp")

    card_other = Enum.YLeaf(5, "card-other")


class IsdErrorEt(Enum):
    """
    IsdErrorEt (Enum Class)

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

    none = Enum.YLeaf(0, "none")

    not_compatible = Enum.YLeaf(1, "not-compatible")

    not_enough_resource = Enum.YLeaf(2, "not-enough-resource")

    not_nsr_ready = Enum.YLeaf(3, "not-nsr-ready")

    not_conn_sdrsm = Enum.YLeaf(4, "not-conn-sdrsm")

    cmd_invalid = Enum.YLeaf(5, "cmd-invalid")

    load_prep_fail = Enum.YLeaf(6, "load-prep-fail")

    error_timeout = Enum.YLeaf(7, "error-timeout")

    err_node_down = Enum.YLeaf(8, "err-node-down")

    node_not_ready = Enum.YLeaf(9, "node-not-ready")

    err_node_new = Enum.YLeaf(10, "err-node-new")

    err_card_oir = Enum.YLeaf(11, "err-card-oir")

    invalid_evt = Enum.YLeaf(12, "invalid-evt")

    disconn_from_calv = Enum.YLeaf(13, "disconn-from-calv")

    gsp_down = Enum.YLeaf(14, "gsp-down")

    abort_by_ism = Enum.YLeaf(15, "abort-by-ism")

    rpfo = Enum.YLeaf(16, "rpfo")

    pkg_null = Enum.YLeaf(17, "pkg-null")

    error_general = Enum.YLeaf(18, "error-general")

    fsa_error = Enum.YLeaf(19, "fsa-error")

    err_post_issu = Enum.YLeaf(20, "err-post-issu")

    err_issu_dir_restart = Enum.YLeaf(21, "err-issu-dir-restart")


class IsdIssuStatusEt(Enum):
    """
    IsdIssuStatusEt (Enum Class)

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

    ok = Enum.YLeaf(0, "ok")

    prep_done = Enum.YLeaf(1, "prep-done")

    big_bang = Enum.YLeaf(2, "big-bang")

    done = Enum.YLeaf(3, "done")

    abort = Enum.YLeaf(4, "abort")

    cmd_reject = Enum.YLeaf(5, "cmd-reject")

    unknown = Enum.YLeaf(6, "unknown")

    abort_cleanup = Enum.YLeaf(7, "abort-cleanup")

    abort_cmd_reject = Enum.YLeaf(8, "abort-cmd-reject")


class IsdStateEt(Enum):
    """
    IsdStateEt (Enum Class)

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

    .. data:: run_prep_isd = 8

    	ISSU ST RUN PREP ISD

    .. data:: run_prep_ism = 9

    	ISSU ST RUN PREP ISM

    .. data:: big_bang = 10

    	ISSU ST RUN BIG BANG

    .. data:: run_done = 11

    	ISSU ST RUN DONE

    .. data:: cleanup = 12

    	ISSU ST CLEANUP

    .. data:: cleanup_done = 13

    	ISSU ST CLEANUP DONE

    .. data:: abort = 14

    	ISSU ST ABORT

    .. data:: abort_done = 15

    	ISSU ST ABORT DONE

    .. data:: abort_cleanup = 16

    	ISSU ST ABORT CLEANUP

    .. data:: unknown_state = 17

    	ISSU UNKNOWN STATE

    """

    none = Enum.YLeaf(0, "none")

    idle = Enum.YLeaf(1, "idle")

    init = Enum.YLeaf(2, "init")

    init_done = Enum.YLeaf(3, "init-done")

    load_prep = Enum.YLeaf(4, "load-prep")

    load_exec = Enum.YLeaf(5, "load-exec")

    load_issu_go = Enum.YLeaf(6, "load-issu-go")

    load_done = Enum.YLeaf(7, "load-done")

    run_prep_isd = Enum.YLeaf(8, "run-prep-isd")

    run_prep_ism = Enum.YLeaf(9, "run-prep-ism")

    big_bang = Enum.YLeaf(10, "big-bang")

    run_done = Enum.YLeaf(11, "run-done")

    cleanup = Enum.YLeaf(12, "cleanup")

    cleanup_done = Enum.YLeaf(13, "cleanup-done")

    abort = Enum.YLeaf(14, "abort")

    abort_done = Enum.YLeaf(15, "abort-done")

    abort_cleanup = Enum.YLeaf(16, "abort-cleanup")

    unknown_state = Enum.YLeaf(17, "unknown-state")


class IssuNodeRoleEt(Enum):
    """
    IssuNodeRoleEt (Enum Class)

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

    unknown_role = Enum.YLeaf(0, "unknown-role")

    primary_role = Enum.YLeaf(1, "primary-role")

    secondary_role = Enum.YLeaf(2, "secondary-role")

    tertiary_role = Enum.YLeaf(3, "tertiary-role")


class IssudirNodeStatusEt(Enum):
    """
    IssudirNodeStatusEt (Enum Class)

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

    not_issu_ready = Enum.YLeaf(0, "not-issu-ready")

    issu_ready = Enum.YLeaf(1, "issu-ready")

    isus_go = Enum.YLeaf(2, "isus-go")

    node_fail = Enum.YLeaf(3, "node-fail")


class NodeRoleEt(Enum):
    """
    NodeRoleEt (Enum Class)

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

    node_unknown = Enum.YLeaf(0, "node-unknown")

    node_active = Enum.YLeaf(1, "node-active")

    node_standby = Enum.YLeaf(2, "node-standby")

    node_unusable = Enum.YLeaf(3, "node-unusable")



class SoftwareInstall(Entity):
    """
    Install operations info
    
    .. attribute:: superseded
    
    	Show superseded packages
    	**type**\:  :py:class:`Superseded <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.Superseded>`
    
    .. attribute:: committed_summary
    
    	Show Committed packages installed
    	**type**\:  :py:class:`CommittedSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.CommittedSummary>`
    
    .. attribute:: active_summary
    
    	Show active packages installed
    	**type**\:  :py:class:`ActiveSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.ActiveSummary>`
    
    .. attribute:: inactive_summary
    
    	Show XR inactive packages
    	**type**\:  :py:class:`InactiveSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.InactiveSummary>`
    
    .. attribute:: prepare
    
    	Show prepared packages ready for activation
    	**type**\:  :py:class:`Prepare <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.Prepare>`
    
    .. attribute:: active
    
    	Show active packages installed
    	**type**\:  :py:class:`Active <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.Active>`
    
    .. attribute:: version
    
    	Show install version
    	**type**\:  :py:class:`Version <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.Version>`
    
    .. attribute:: inactive
    
    	Show XR inactive packages
    	**type**\:  :py:class:`Inactive <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.Inactive>`
    
    .. attribute:: request
    
    	Show current request
    	**type**\:  :py:class:`Request <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.Request>`
    
    .. attribute:: superseded_summary
    
    	Show superseded packages
    	**type**\:  :py:class:`SupersededSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.SupersededSummary>`
    
    .. attribute:: issu
    
    	ISSU operation
    	**type**\:  :py:class:`Issu <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.Issu>`
    
    .. attribute:: committed
    
    	Show Committed packages installed
    	**type**\:  :py:class:`Committed <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.Committed>`
    
    .. attribute:: all_operations_log
    
    	Show log file for all operations
    	**type**\:  :py:class:`AllOperationsLog <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.AllOperationsLog>`
    
    .. attribute:: packages
    
    	Show the list of installed packages
    	**type**\:  :py:class:`Packages <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.Packages>`
    
    .. attribute:: operation_logs
    
    	Show log file
    	**type**\:  :py:class:`OperationLogs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.OperationLogs>`
    
    .. attribute:: repository
    
    	Show packages stored in install software repositories
    	**type**\:  :py:class:`Repository <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.Repository>`
    
    

    """

    _prefix = 'spirit-install-instmgr-oper'
    _revision = '2017-09-07'

    def __init__(self):
        super(SoftwareInstall, self).__init__()
        self._top_entity = None

        self.yang_name = "software-install"
        self.yang_parent_name = "Cisco-IOS-XR-spirit-install-instmgr-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("superseded", ("superseded", SoftwareInstall.Superseded)), ("committed-summary", ("committed_summary", SoftwareInstall.CommittedSummary)), ("active-summary", ("active_summary", SoftwareInstall.ActiveSummary)), ("inactive-summary", ("inactive_summary", SoftwareInstall.InactiveSummary)), ("prepare", ("prepare", SoftwareInstall.Prepare)), ("active", ("active", SoftwareInstall.Active)), ("version", ("version", SoftwareInstall.Version)), ("inactive", ("inactive", SoftwareInstall.Inactive)), ("request", ("request", SoftwareInstall.Request)), ("superseded-summary", ("superseded_summary", SoftwareInstall.SupersededSummary)), ("issu", ("issu", SoftwareInstall.Issu)), ("committed", ("committed", SoftwareInstall.Committed)), ("all-operations-log", ("all_operations_log", SoftwareInstall.AllOperationsLog)), ("packages", ("packages", SoftwareInstall.Packages)), ("operation-logs", ("operation_logs", SoftwareInstall.OperationLogs)), ("repository", ("repository", SoftwareInstall.Repository))])
        self._leafs = OrderedDict()

        self.superseded = SoftwareInstall.Superseded()
        self.superseded.parent = self
        self._children_name_map["superseded"] = "superseded"

        self.committed_summary = SoftwareInstall.CommittedSummary()
        self.committed_summary.parent = self
        self._children_name_map["committed_summary"] = "committed-summary"

        self.active_summary = SoftwareInstall.ActiveSummary()
        self.active_summary.parent = self
        self._children_name_map["active_summary"] = "active-summary"

        self.inactive_summary = SoftwareInstall.InactiveSummary()
        self.inactive_summary.parent = self
        self._children_name_map["inactive_summary"] = "inactive-summary"

        self.prepare = SoftwareInstall.Prepare()
        self.prepare.parent = self
        self._children_name_map["prepare"] = "prepare"

        self.active = SoftwareInstall.Active()
        self.active.parent = self
        self._children_name_map["active"] = "active"

        self.version = SoftwareInstall.Version()
        self.version.parent = self
        self._children_name_map["version"] = "version"

        self.inactive = SoftwareInstall.Inactive()
        self.inactive.parent = self
        self._children_name_map["inactive"] = "inactive"

        self.request = SoftwareInstall.Request()
        self.request.parent = self
        self._children_name_map["request"] = "request"

        self.superseded_summary = SoftwareInstall.SupersededSummary()
        self.superseded_summary.parent = self
        self._children_name_map["superseded_summary"] = "superseded-summary"

        self.issu = SoftwareInstall.Issu()
        self.issu.parent = self
        self._children_name_map["issu"] = "issu"

        self.committed = SoftwareInstall.Committed()
        self.committed.parent = self
        self._children_name_map["committed"] = "committed"

        self.all_operations_log = SoftwareInstall.AllOperationsLog()
        self.all_operations_log.parent = self
        self._children_name_map["all_operations_log"] = "all-operations-log"

        self.packages = SoftwareInstall.Packages()
        self.packages.parent = self
        self._children_name_map["packages"] = "packages"

        self.operation_logs = SoftwareInstall.OperationLogs()
        self.operation_logs.parent = self
        self._children_name_map["operation_logs"] = "operation-logs"

        self.repository = SoftwareInstall.Repository()
        self.repository.parent = self
        self._children_name_map["repository"] = "repository"
        self._segment_path = lambda: "Cisco-IOS-XR-spirit-install-instmgr-oper:software-install"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(SoftwareInstall, [], name, value)


    class Superseded(Entity):
        """
        Show superseded packages
        
        .. attribute:: superseded_package_info
        
        	superseded package info
        	**type**\: list of  		 :py:class:`SupersededPackageInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.Superseded.SupersededPackageInfo>`
        
        

        """

        _prefix = 'spirit-install-instmgr-oper'
        _revision = '2017-09-07'

        def __init__(self):
            super(SoftwareInstall.Superseded, self).__init__()

            self.yang_name = "superseded"
            self.yang_parent_name = "software-install"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("superseded-package-info", ("superseded_package_info", SoftwareInstall.Superseded.SupersededPackageInfo))])
            self._leafs = OrderedDict()

            self.superseded_package_info = YList(self)
            self._segment_path = lambda: "superseded"
            self._absolute_path = lambda: "Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(SoftwareInstall.Superseded, [], name, value)


        class SupersededPackageInfo(Entity):
            """
            superseded package info
            
            .. attribute:: error_message
            
            	ErrorMessage
            	**type**\: str
            
            .. attribute:: location
            
            	Location
            	**type**\: str
            
            .. attribute:: node_type
            
            	NodeType
            	**type**\: str
            
            .. attribute:: boot_partition_name
            
            	BootPartitionName
            	**type**\: str
            
            .. attribute:: superseded_packages
            
            	SupersededPackages
            	**type**\: str
            
            

            """

            _prefix = 'spirit-install-instmgr-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(SoftwareInstall.Superseded.SupersededPackageInfo, self).__init__()

                self.yang_name = "superseded-package-info"
                self.yang_parent_name = "superseded"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('error_message', (YLeaf(YType.str, 'error-message'), ['str'])),
                    ('location', (YLeaf(YType.str, 'location'), ['str'])),
                    ('node_type', (YLeaf(YType.str, 'node-type'), ['str'])),
                    ('boot_partition_name', (YLeaf(YType.str, 'boot-partition-name'), ['str'])),
                    ('superseded_packages', (YLeaf(YType.str, 'superseded-packages'), ['str'])),
                ])
                self.error_message = None
                self.location = None
                self.node_type = None
                self.boot_partition_name = None
                self.superseded_packages = None
                self._segment_path = lambda: "superseded-package-info"
                self._absolute_path = lambda: "Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/superseded/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(SoftwareInstall.Superseded.SupersededPackageInfo, [u'error_message', u'location', u'node_type', u'boot_partition_name', u'superseded_packages'], name, value)


    class CommittedSummary(Entity):
        """
        Show Committed packages installed
        
        .. attribute:: committed_package_info
        
        	committed package info
        	**type**\: list of  		 :py:class:`CommittedPackageInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.CommittedSummary.CommittedPackageInfo>`
        
        

        """

        _prefix = 'spirit-install-instmgr-oper'
        _revision = '2017-09-07'

        def __init__(self):
            super(SoftwareInstall.CommittedSummary, self).__init__()

            self.yang_name = "committed-summary"
            self.yang_parent_name = "software-install"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("committed-package-info", ("committed_package_info", SoftwareInstall.CommittedSummary.CommittedPackageInfo))])
            self._leafs = OrderedDict()

            self.committed_package_info = YList(self)
            self._segment_path = lambda: "committed-summary"
            self._absolute_path = lambda: "Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(SoftwareInstall.CommittedSummary, [], name, value)


        class CommittedPackageInfo(Entity):
            """
            committed package info
            
            .. attribute:: error_message
            
            	ErrorMessage
            	**type**\: str
            
            .. attribute:: location
            
            	Location
            	**type**\: str
            
            .. attribute:: node_type
            
            	NodeType
            	**type**\: str
            
            .. attribute:: boot_partition_name
            
            	BootPartitionName
            	**type**\: str
            
            .. attribute:: number_of_committed_packages
            
            	NumberOfCommittedPackages
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: committed_packages
            
            	CommittedPackages
            	**type**\: str
            
            

            """

            _prefix = 'spirit-install-instmgr-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(SoftwareInstall.CommittedSummary.CommittedPackageInfo, self).__init__()

                self.yang_name = "committed-package-info"
                self.yang_parent_name = "committed-summary"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('error_message', (YLeaf(YType.str, 'error-message'), ['str'])),
                    ('location', (YLeaf(YType.str, 'location'), ['str'])),
                    ('node_type', (YLeaf(YType.str, 'node-type'), ['str'])),
                    ('boot_partition_name', (YLeaf(YType.str, 'boot-partition-name'), ['str'])),
                    ('number_of_committed_packages', (YLeaf(YType.uint32, 'number-of-committed-packages'), ['int'])),
                    ('committed_packages', (YLeaf(YType.str, 'committed-packages'), ['str'])),
                ])
                self.error_message = None
                self.location = None
                self.node_type = None
                self.boot_partition_name = None
                self.number_of_committed_packages = None
                self.committed_packages = None
                self._segment_path = lambda: "committed-package-info"
                self._absolute_path = lambda: "Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/committed-summary/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(SoftwareInstall.CommittedSummary.CommittedPackageInfo, [u'error_message', u'location', u'node_type', u'boot_partition_name', u'number_of_committed_packages', u'committed_packages'], name, value)


    class ActiveSummary(Entity):
        """
        Show active packages installed
        
        .. attribute:: active_package_info
        
        	active package info
        	**type**\: list of  		 :py:class:`ActivePackageInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.ActiveSummary.ActivePackageInfo>`
        
        

        """

        _prefix = 'spirit-install-instmgr-oper'
        _revision = '2017-09-07'

        def __init__(self):
            super(SoftwareInstall.ActiveSummary, self).__init__()

            self.yang_name = "active-summary"
            self.yang_parent_name = "software-install"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("active-package-info", ("active_package_info", SoftwareInstall.ActiveSummary.ActivePackageInfo))])
            self._leafs = OrderedDict()

            self.active_package_info = YList(self)
            self._segment_path = lambda: "active-summary"
            self._absolute_path = lambda: "Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(SoftwareInstall.ActiveSummary, [], name, value)


        class ActivePackageInfo(Entity):
            """
            active package info
            
            .. attribute:: error_message
            
            	ErrorMessage
            	**type**\: str
            
            .. attribute:: location
            
            	Location
            	**type**\: str
            
            .. attribute:: node_type
            
            	NodeType
            	**type**\: str
            
            .. attribute:: boot_partition_name
            
            	BootPartitionName
            	**type**\: str
            
            .. attribute:: number_of_active_packages
            
            	NumberOfActivePackages
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: active_packages
            
            	ActivePackages
            	**type**\: str
            
            

            """

            _prefix = 'spirit-install-instmgr-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(SoftwareInstall.ActiveSummary.ActivePackageInfo, self).__init__()

                self.yang_name = "active-package-info"
                self.yang_parent_name = "active-summary"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('error_message', (YLeaf(YType.str, 'error-message'), ['str'])),
                    ('location', (YLeaf(YType.str, 'location'), ['str'])),
                    ('node_type', (YLeaf(YType.str, 'node-type'), ['str'])),
                    ('boot_partition_name', (YLeaf(YType.str, 'boot-partition-name'), ['str'])),
                    ('number_of_active_packages', (YLeaf(YType.uint32, 'number-of-active-packages'), ['int'])),
                    ('active_packages', (YLeaf(YType.str, 'active-packages'), ['str'])),
                ])
                self.error_message = None
                self.location = None
                self.node_type = None
                self.boot_partition_name = None
                self.number_of_active_packages = None
                self.active_packages = None
                self._segment_path = lambda: "active-package-info"
                self._absolute_path = lambda: "Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/active-summary/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(SoftwareInstall.ActiveSummary.ActivePackageInfo, [u'error_message', u'location', u'node_type', u'boot_partition_name', u'number_of_active_packages', u'active_packages'], name, value)


    class InactiveSummary(Entity):
        """
        Show XR inactive packages
        
        .. attribute:: log
        
        	log
        	**type**\: str
        
        

        """

        _prefix = 'spirit-install-instmgr-oper'
        _revision = '2017-09-07'

        def __init__(self):
            super(SoftwareInstall.InactiveSummary, self).__init__()

            self.yang_name = "inactive-summary"
            self.yang_parent_name = "software-install"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('log', (YLeaf(YType.str, 'log'), ['str'])),
            ])
            self.log = None
            self._segment_path = lambda: "inactive-summary"
            self._absolute_path = lambda: "Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(SoftwareInstall.InactiveSummary, [u'log'], name, value)


    class Prepare(Entity):
        """
        Show prepared packages ready for activation
        
        .. attribute:: no_prepare_done
        
        	NoPrepareDone
        	**type**\: str
        
        .. attribute:: prepared_boot_image
        
        	PreparedBootImage
        	**type**\: str
        
        .. attribute:: prepared_boot_partition
        
        	PreparedBootPartition
        	**type**\: str
        
        .. attribute:: restart_type
        
        	RestartType
        	**type**\: str
        
        .. attribute:: activate_message
        
        	ActivateMessage
        	**type**\: str
        
        .. attribute:: prepare_clean_message
        
        	PrepareCleanMessage
        	**type**\: str
        
        .. attribute:: rpm
        
        	rpm
        	**type**\: list of  		 :py:class:`Rpm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.Prepare.Rpm>`
        
        .. attribute:: package
        
        	package
        	**type**\: list of  		 :py:class:`Package <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.Prepare.Package>`
        
        

        """

        _prefix = 'spirit-install-instmgr-oper'
        _revision = '2017-09-07'

        def __init__(self):
            super(SoftwareInstall.Prepare, self).__init__()

            self.yang_name = "prepare"
            self.yang_parent_name = "software-install"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("rpm", ("rpm", SoftwareInstall.Prepare.Rpm)), ("package", ("package", SoftwareInstall.Prepare.Package))])
            self._leafs = OrderedDict([
                ('no_prepare_done', (YLeaf(YType.str, 'no-prepare-done'), ['str'])),
                ('prepared_boot_image', (YLeaf(YType.str, 'prepared-boot-image'), ['str'])),
                ('prepared_boot_partition', (YLeaf(YType.str, 'prepared-boot-partition'), ['str'])),
                ('restart_type', (YLeaf(YType.str, 'restart-type'), ['str'])),
                ('activate_message', (YLeaf(YType.str, 'activate-message'), ['str'])),
                ('prepare_clean_message', (YLeaf(YType.str, 'prepare-clean-message'), ['str'])),
            ])
            self.no_prepare_done = None
            self.prepared_boot_image = None
            self.prepared_boot_partition = None
            self.restart_type = None
            self.activate_message = None
            self.prepare_clean_message = None

            self.rpm = YList(self)
            self.package = YList(self)
            self._segment_path = lambda: "prepare"
            self._absolute_path = lambda: "Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(SoftwareInstall.Prepare, [u'no_prepare_done', u'prepared_boot_image', u'prepared_boot_partition', u'restart_type', u'activate_message', u'prepare_clean_message'], name, value)


        class Rpm(Entity):
            """
            rpm
            
            .. attribute:: package
            
            	package
            	**type**\: str
            
            

            """

            _prefix = 'spirit-install-instmgr-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(SoftwareInstall.Prepare.Rpm, self).__init__()

                self.yang_name = "rpm"
                self.yang_parent_name = "prepare"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('package', (YLeaf(YType.str, 'package'), ['str'])),
                ])
                self.package = None
                self._segment_path = lambda: "rpm"
                self._absolute_path = lambda: "Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/prepare/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(SoftwareInstall.Prepare.Rpm, [u'package'], name, value)


        class Package(Entity):
            """
            package
            
            .. attribute:: package
            
            	package
            	**type**\: str
            
            

            """

            _prefix = 'spirit-install-instmgr-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(SoftwareInstall.Prepare.Package, self).__init__()

                self.yang_name = "package"
                self.yang_parent_name = "prepare"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('package', (YLeaf(YType.str, 'package'), ['str'])),
                ])
                self.package = None
                self._segment_path = lambda: "package"
                self._absolute_path = lambda: "Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/prepare/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(SoftwareInstall.Prepare.Package, [u'package'], name, value)


    class Active(Entity):
        """
        Show active packages installed
        
        .. attribute:: active_package_info
        
        	active package info
        	**type**\: list of  		 :py:class:`ActivePackageInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.Active.ActivePackageInfo>`
        
        

        """

        _prefix = 'spirit-install-instmgr-oper'
        _revision = '2017-09-07'

        def __init__(self):
            super(SoftwareInstall.Active, self).__init__()

            self.yang_name = "active"
            self.yang_parent_name = "software-install"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("active-package-info", ("active_package_info", SoftwareInstall.Active.ActivePackageInfo))])
            self._leafs = OrderedDict()

            self.active_package_info = YList(self)
            self._segment_path = lambda: "active"
            self._absolute_path = lambda: "Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(SoftwareInstall.Active, [], name, value)


        class ActivePackageInfo(Entity):
            """
            active package info
            
            .. attribute:: error_message
            
            	ErrorMessage
            	**type**\: str
            
            .. attribute:: location
            
            	Location
            	**type**\: str
            
            .. attribute:: node_type
            
            	NodeType
            	**type**\: str
            
            .. attribute:: boot_partition_name
            
            	BootPartitionName
            	**type**\: str
            
            .. attribute:: number_of_active_packages
            
            	NumberOfActivePackages
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: active_packages
            
            	ActivePackages
            	**type**\: str
            
            

            """

            _prefix = 'spirit-install-instmgr-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(SoftwareInstall.Active.ActivePackageInfo, self).__init__()

                self.yang_name = "active-package-info"
                self.yang_parent_name = "active"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('error_message', (YLeaf(YType.str, 'error-message'), ['str'])),
                    ('location', (YLeaf(YType.str, 'location'), ['str'])),
                    ('node_type', (YLeaf(YType.str, 'node-type'), ['str'])),
                    ('boot_partition_name', (YLeaf(YType.str, 'boot-partition-name'), ['str'])),
                    ('number_of_active_packages', (YLeaf(YType.uint32, 'number-of-active-packages'), ['int'])),
                    ('active_packages', (YLeaf(YType.str, 'active-packages'), ['str'])),
                ])
                self.error_message = None
                self.location = None
                self.node_type = None
                self.boot_partition_name = None
                self.number_of_active_packages = None
                self.active_packages = None
                self._segment_path = lambda: "active-package-info"
                self._absolute_path = lambda: "Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/active/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(SoftwareInstall.Active.ActivePackageInfo, [u'error_message', u'location', u'node_type', u'boot_partition_name', u'number_of_active_packages', u'active_packages'], name, value)


    class Version(Entity):
        """
        Show install version
        
        .. attribute:: location
        
        	Path where all cisco packages are installed
        	**type**\: str
        
        .. attribute:: label
        
        	label name
        	**type**\: str
        
        .. attribute:: copyright_info
        
        	copyright info
        	**type**\: str
        
        .. attribute:: hardware_info
        
        	hardware info of the router
        	**type**\: str
        
        .. attribute:: system_uptime
        
        	duration since when system is up
        	**type**\: str
        
        .. attribute:: package
        
        	package
        	**type**\: list of  		 :py:class:`Package <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.Version.Package>`
        
        

        """

        _prefix = 'spirit-install-instmgr-oper'
        _revision = '2017-09-07'

        def __init__(self):
            super(SoftwareInstall.Version, self).__init__()

            self.yang_name = "version"
            self.yang_parent_name = "software-install"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("package", ("package", SoftwareInstall.Version.Package))])
            self._leafs = OrderedDict([
                ('location', (YLeaf(YType.str, 'location'), ['str'])),
                ('label', (YLeaf(YType.str, 'label'), ['str'])),
                ('copyright_info', (YLeaf(YType.str, 'copyright-info'), ['str'])),
                ('hardware_info', (YLeaf(YType.str, 'hardware-info'), ['str'])),
                ('system_uptime', (YLeaf(YType.str, 'system-uptime'), ['str'])),
            ])
            self.location = None
            self.label = None
            self.copyright_info = None
            self.hardware_info = None
            self.system_uptime = None

            self.package = YList(self)
            self._segment_path = lambda: "version"
            self._absolute_path = lambda: "Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(SoftwareInstall.Version, [u'location', u'label', u'copyright_info', u'hardware_info', u'system_uptime'], name, value)


        class Package(Entity):
            """
            package
            
            .. attribute:: name
            
            	Name
            	**type**\: str
            
            .. attribute:: version
            
            	Running version
            	**type**\: str
            
            .. attribute:: built_by
            
            	User built by
            	**type**\: str
            
            .. attribute:: built_on
            
            	Time built
            	**type**\: str
            
            .. attribute:: build_host
            
            	Build host
            	**type**\: str
            
            .. attribute:: workspace
            
            	Workspace built in
            	**type**\: str
            
            

            """

            _prefix = 'spirit-install-instmgr-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(SoftwareInstall.Version.Package, self).__init__()

                self.yang_name = "package"
                self.yang_parent_name = "version"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                    ('version', (YLeaf(YType.str, 'version'), ['str'])),
                    ('built_by', (YLeaf(YType.str, 'built-by'), ['str'])),
                    ('built_on', (YLeaf(YType.str, 'built-on'), ['str'])),
                    ('build_host', (YLeaf(YType.str, 'build-host'), ['str'])),
                    ('workspace', (YLeaf(YType.str, 'workspace'), ['str'])),
                ])
                self.name = None
                self.version = None
                self.built_by = None
                self.built_on = None
                self.build_host = None
                self.workspace = None
                self._segment_path = lambda: "package"
                self._absolute_path = lambda: "Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/version/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(SoftwareInstall.Version.Package, [u'name', u'version', u'built_by', u'built_on', u'build_host', u'workspace'], name, value)


    class Inactive(Entity):
        """
        Show XR inactive packages
        
        .. attribute:: log
        
        	log
        	**type**\: str
        
        

        """

        _prefix = 'spirit-install-instmgr-oper'
        _revision = '2017-09-07'

        def __init__(self):
            super(SoftwareInstall.Inactive, self).__init__()

            self.yang_name = "inactive"
            self.yang_parent_name = "software-install"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('log', (YLeaf(YType.str, 'log'), ['str'])),
            ])
            self.log = None
            self._segment_path = lambda: "inactive"
            self._absolute_path = lambda: "Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(SoftwareInstall.Inactive, [u'log'], name, value)


    class Request(Entity):
        """
        Show current request
        
        .. attribute:: curr_inst_oper
        
        	CurrInstOper
        	**type**\: str
        
        

        """

        _prefix = 'spirit-install-instmgr-oper'
        _revision = '2017-09-07'

        def __init__(self):
            super(SoftwareInstall.Request, self).__init__()

            self.yang_name = "request"
            self.yang_parent_name = "software-install"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('curr_inst_oper', (YLeaf(YType.str, 'curr-inst-oper'), ['str'])),
            ])
            self.curr_inst_oper = None
            self._segment_path = lambda: "request"
            self._absolute_path = lambda: "Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(SoftwareInstall.Request, [u'curr_inst_oper'], name, value)


    class SupersededSummary(Entity):
        """
        Show superseded packages
        
        .. attribute:: log
        
        	log
        	**type**\: str
        
        

        """

        _prefix = 'spirit-install-instmgr-oper'
        _revision = '2017-09-07'

        def __init__(self):
            super(SoftwareInstall.SupersededSummary, self).__init__()

            self.yang_name = "superseded-summary"
            self.yang_parent_name = "software-install"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('log', (YLeaf(YType.str, 'log'), ['str'])),
            ])
            self.log = None
            self._segment_path = lambda: "superseded-summary"
            self._absolute_path = lambda: "Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(SoftwareInstall.SupersededSummary, [u'log'], name, value)


    class Issu(Entity):
        """
        ISSU operation
        
        .. attribute:: stage
        
        	Show XR install issu stage
        	**type**\:  :py:class:`Stage <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.Issu.Stage>`
        
        .. attribute:: inventory
        
        	Show XR install issu inventory
        	**type**\:  :py:class:`Inventory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.Issu.Inventory>`
        
        

        """

        _prefix = 'spirit-install-instmgr-oper'
        _revision = '2017-09-07'

        def __init__(self):
            super(SoftwareInstall.Issu, self).__init__()

            self.yang_name = "issu"
            self.yang_parent_name = "software-install"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("stage", ("stage", SoftwareInstall.Issu.Stage)), ("inventory", ("inventory", SoftwareInstall.Issu.Inventory))])
            self._leafs = OrderedDict()

            self.stage = SoftwareInstall.Issu.Stage()
            self.stage.parent = self
            self._children_name_map["stage"] = "stage"

            self.inventory = SoftwareInstall.Issu.Inventory()
            self.inventory.parent = self
            self._children_name_map["inventory"] = "inventory"
            self._segment_path = lambda: "issu"
            self._absolute_path = lambda: "Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(SoftwareInstall.Issu, [], name, value)


        class Stage(Entity):
            """
            Show XR install issu stage
            
            .. attribute:: state
            
            	State
            	**type**\:  :py:class:`IsdStateEt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.IsdStateEt>`
            
            .. attribute:: issu_node_cnt
            
            	ISSU Node Count
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: issu_ready_node_cnt
            
            	ISSU Ready Node Count
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: percentage
            
            	Percentage
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: percentage
            
            .. attribute:: issu_status
            
            	Abort Status
            	**type**\:  :py:class:`IsdIssuStatusEt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.IsdIssuStatusEt>`
            
            .. attribute:: issu_error
            
            	ISSU Error
            	**type**\:  :py:class:`IsdErrorEt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.IsdErrorEt>`
            
            

            """

            _prefix = 'spirit-install-instmgr-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(SoftwareInstall.Issu.Stage, self).__init__()

                self.yang_name = "stage"
                self.yang_parent_name = "issu"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper', 'IsdStateEt', '')])),
                    ('issu_node_cnt', (YLeaf(YType.int32, 'issu-node-cnt'), ['int'])),
                    ('issu_ready_node_cnt', (YLeaf(YType.int32, 'issu-ready-node-cnt'), ['int'])),
                    ('percentage', (YLeaf(YType.int32, 'percentage'), ['int'])),
                    ('issu_status', (YLeaf(YType.enumeration, 'issu-status'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper', 'IsdIssuStatusEt', '')])),
                    ('issu_error', (YLeaf(YType.enumeration, 'issu-error'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper', 'IsdErrorEt', '')])),
                ])
                self.state = None
                self.issu_node_cnt = None
                self.issu_ready_node_cnt = None
                self.percentage = None
                self.issu_status = None
                self.issu_error = None
                self._segment_path = lambda: "stage"
                self._absolute_path = lambda: "Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/issu/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(SoftwareInstall.Issu.Stage, [u'state', u'issu_node_cnt', u'issu_ready_node_cnt', u'percentage', u'issu_status', u'issu_error'], name, value)


        class Inventory(Entity):
            """
            Show XR install issu inventory
            
            .. attribute:: invinfo
            
            	invinfo
            	**type**\: list of  		 :py:class:`Invinfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.Issu.Inventory.Invinfo>`
            
            

            """

            _prefix = 'spirit-install-instmgr-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(SoftwareInstall.Issu.Inventory, self).__init__()

                self.yang_name = "inventory"
                self.yang_parent_name = "issu"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("invinfo", ("invinfo", SoftwareInstall.Issu.Inventory.Invinfo))])
                self._leafs = OrderedDict()

                self.invinfo = YList(self)
                self._segment_path = lambda: "inventory"
                self._absolute_path = lambda: "Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/issu/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(SoftwareInstall.Issu.Inventory, [], name, value)


            class Invinfo(Entity):
                """
                invinfo
                
                .. attribute:: node_id
                
                	Node ID
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: node_type
                
                	Node Type
                	**type**\:  :py:class:`CardTypeEt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.CardTypeEt>`
                
                .. attribute:: issu_node_role
                
                	ISSU Node Role
                	**type**\:  :py:class:`IssuNodeRoleEt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.IssuNodeRoleEt>`
                
                .. attribute:: node_state
                
                	Node State
                	**type**\:  :py:class:`IssudirNodeStatusEt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.IssudirNodeStatusEt>`
                
                .. attribute:: node_role
                
                	Node role
                	**type**\:  :py:class:`NodeRoleEt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.NodeRoleEt>`
                
                

                """

                _prefix = 'spirit-install-instmgr-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(SoftwareInstall.Issu.Inventory.Invinfo, self).__init__()

                    self.yang_name = "invinfo"
                    self.yang_parent_name = "inventory"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('node_id', (YLeaf(YType.int32, 'node-id'), ['int'])),
                        ('node_type', (YLeaf(YType.enumeration, 'node-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper', 'CardTypeEt', '')])),
                        ('issu_node_role', (YLeaf(YType.enumeration, 'issu-node-role'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper', 'IssuNodeRoleEt', '')])),
                        ('node_state', (YLeaf(YType.enumeration, 'node-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper', 'IssudirNodeStatusEt', '')])),
                        ('node_role', (YLeaf(YType.enumeration, 'node-role'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper', 'NodeRoleEt', '')])),
                    ])
                    self.node_id = None
                    self.node_type = None
                    self.issu_node_role = None
                    self.node_state = None
                    self.node_role = None
                    self._segment_path = lambda: "invinfo"
                    self._absolute_path = lambda: "Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/issu/inventory/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(SoftwareInstall.Issu.Inventory.Invinfo, [u'node_id', u'node_type', u'issu_node_role', u'node_state', u'node_role'], name, value)


    class Committed(Entity):
        """
        Show Committed packages installed
        
        .. attribute:: committed_package_info
        
        	committed package info
        	**type**\: list of  		 :py:class:`CommittedPackageInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.Committed.CommittedPackageInfo>`
        
        

        """

        _prefix = 'spirit-install-instmgr-oper'
        _revision = '2017-09-07'

        def __init__(self):
            super(SoftwareInstall.Committed, self).__init__()

            self.yang_name = "committed"
            self.yang_parent_name = "software-install"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("committed-package-info", ("committed_package_info", SoftwareInstall.Committed.CommittedPackageInfo))])
            self._leafs = OrderedDict()

            self.committed_package_info = YList(self)
            self._segment_path = lambda: "committed"
            self._absolute_path = lambda: "Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(SoftwareInstall.Committed, [], name, value)


        class CommittedPackageInfo(Entity):
            """
            committed package info
            
            .. attribute:: error_message
            
            	ErrorMessage
            	**type**\: str
            
            .. attribute:: location
            
            	Location
            	**type**\: str
            
            .. attribute:: node_type
            
            	NodeType
            	**type**\: str
            
            .. attribute:: boot_partition_name
            
            	BootPartitionName
            	**type**\: str
            
            .. attribute:: number_of_committed_packages
            
            	NumberOfCommittedPackages
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: committed_packages
            
            	CommittedPackages
            	**type**\: str
            
            

            """

            _prefix = 'spirit-install-instmgr-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(SoftwareInstall.Committed.CommittedPackageInfo, self).__init__()

                self.yang_name = "committed-package-info"
                self.yang_parent_name = "committed"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('error_message', (YLeaf(YType.str, 'error-message'), ['str'])),
                    ('location', (YLeaf(YType.str, 'location'), ['str'])),
                    ('node_type', (YLeaf(YType.str, 'node-type'), ['str'])),
                    ('boot_partition_name', (YLeaf(YType.str, 'boot-partition-name'), ['str'])),
                    ('number_of_committed_packages', (YLeaf(YType.uint32, 'number-of-committed-packages'), ['int'])),
                    ('committed_packages', (YLeaf(YType.str, 'committed-packages'), ['str'])),
                ])
                self.error_message = None
                self.location = None
                self.node_type = None
                self.boot_partition_name = None
                self.number_of_committed_packages = None
                self.committed_packages = None
                self._segment_path = lambda: "committed-package-info"
                self._absolute_path = lambda: "Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/committed/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(SoftwareInstall.Committed.CommittedPackageInfo, [u'error_message', u'location', u'node_type', u'boot_partition_name', u'number_of_committed_packages', u'committed_packages'], name, value)


    class AllOperationsLog(Entity):
        """
        Show log file for all operations
        
        .. attribute:: reverse_detail
        
        	Show detailed log file for all operations \- reverse
        	**type**\:  :py:class:`ReverseDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.AllOperationsLog.ReverseDetail>`
        
        .. attribute:: reverse
        
        	Show log file for all operations \- reverse
        	**type**\:  :py:class:`Reverse <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.AllOperationsLog.Reverse>`
        
        .. attribute:: summary
        
        	Show summary log file for all operations
        	**type**\:  :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.AllOperationsLog.Summary>`
        
        .. attribute:: detail
        
        	Show detailed log file for all operations
        	**type**\:  :py:class:`Detail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.AllOperationsLog.Detail>`
        
        

        """

        _prefix = 'spirit-install-instmgr-oper'
        _revision = '2017-09-07'

        def __init__(self):
            super(SoftwareInstall.AllOperationsLog, self).__init__()

            self.yang_name = "all-operations-log"
            self.yang_parent_name = "software-install"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("reverse-detail", ("reverse_detail", SoftwareInstall.AllOperationsLog.ReverseDetail)), ("reverse", ("reverse", SoftwareInstall.AllOperationsLog.Reverse)), ("summary", ("summary", SoftwareInstall.AllOperationsLog.Summary)), ("detail", ("detail", SoftwareInstall.AllOperationsLog.Detail))])
            self._leafs = OrderedDict()

            self.reverse_detail = SoftwareInstall.AllOperationsLog.ReverseDetail()
            self.reverse_detail.parent = self
            self._children_name_map["reverse_detail"] = "reverse-detail"

            self.reverse = SoftwareInstall.AllOperationsLog.Reverse()
            self.reverse.parent = self
            self._children_name_map["reverse"] = "reverse"

            self.summary = SoftwareInstall.AllOperationsLog.Summary()
            self.summary.parent = self
            self._children_name_map["summary"] = "summary"

            self.detail = SoftwareInstall.AllOperationsLog.Detail()
            self.detail.parent = self
            self._children_name_map["detail"] = "detail"
            self._segment_path = lambda: "all-operations-log"
            self._absolute_path = lambda: "Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(SoftwareInstall.AllOperationsLog, [], name, value)


        class ReverseDetail(Entity):
            """
            Show detailed log file for all operations \-
            reverse
            
            .. attribute:: log
            
            	log
            	**type**\: str
            
            

            """

            _prefix = 'spirit-install-instmgr-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(SoftwareInstall.AllOperationsLog.ReverseDetail, self).__init__()

                self.yang_name = "reverse-detail"
                self.yang_parent_name = "all-operations-log"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('log', (YLeaf(YType.str, 'log'), ['str'])),
                ])
                self.log = None
                self._segment_path = lambda: "reverse-detail"
                self._absolute_path = lambda: "Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/all-operations-log/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(SoftwareInstall.AllOperationsLog.ReverseDetail, [u'log'], name, value)


        class Reverse(Entity):
            """
            Show log file for all operations \- reverse
            
            .. attribute:: log
            
            	log
            	**type**\: str
            
            

            """

            _prefix = 'spirit-install-instmgr-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(SoftwareInstall.AllOperationsLog.Reverse, self).__init__()

                self.yang_name = "reverse"
                self.yang_parent_name = "all-operations-log"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('log', (YLeaf(YType.str, 'log'), ['str'])),
                ])
                self.log = None
                self._segment_path = lambda: "reverse"
                self._absolute_path = lambda: "Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/all-operations-log/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(SoftwareInstall.AllOperationsLog.Reverse, [u'log'], name, value)


        class Summary(Entity):
            """
            Show summary log file for all operations
            
            .. attribute:: log
            
            	log
            	**type**\: str
            
            

            """

            _prefix = 'spirit-install-instmgr-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(SoftwareInstall.AllOperationsLog.Summary, self).__init__()

                self.yang_name = "summary"
                self.yang_parent_name = "all-operations-log"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('log', (YLeaf(YType.str, 'log'), ['str'])),
                ])
                self.log = None
                self._segment_path = lambda: "summary"
                self._absolute_path = lambda: "Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/all-operations-log/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(SoftwareInstall.AllOperationsLog.Summary, [u'log'], name, value)


        class Detail(Entity):
            """
            Show detailed log file for all operations
            
            .. attribute:: log
            
            	log
            	**type**\: str
            
            

            """

            _prefix = 'spirit-install-instmgr-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(SoftwareInstall.AllOperationsLog.Detail, self).__init__()

                self.yang_name = "detail"
                self.yang_parent_name = "all-operations-log"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('log', (YLeaf(YType.str, 'log'), ['str'])),
                ])
                self.log = None
                self._segment_path = lambda: "detail"
                self._absolute_path = lambda: "Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/all-operations-log/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(SoftwareInstall.AllOperationsLog.Detail, [u'log'], name, value)


    class Packages(Entity):
        """
        Show the list of installed packages
        
        .. attribute:: package
        
        	Show the info for a installed package
        	**type**\: list of  		 :py:class:`Package <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.Packages.Package>`
        
        

        """

        _prefix = 'spirit-install-instmgr-oper'
        _revision = '2017-09-07'

        def __init__(self):
            super(SoftwareInstall.Packages, self).__init__()

            self.yang_name = "packages"
            self.yang_parent_name = "software-install"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("package", ("package", SoftwareInstall.Packages.Package))])
            self._leafs = OrderedDict()

            self.package = YList(self)
            self._segment_path = lambda: "packages"
            self._absolute_path = lambda: "Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(SoftwareInstall.Packages, [], name, value)


        class Package(Entity):
            """
            Show the info for a installed package
            
            .. attribute:: package_name  (key)
            
            	Package name
            	**type**\: str
            
            .. attribute:: verbose
            
            	Show the verbose info for a installed package
            	**type**\:  :py:class:`Verbose <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.Packages.Package.Verbose>`
            
            .. attribute:: brief
            
            	Show the info for a installed package
            	**type**\:  :py:class:`Brief <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.Packages.Package.Brief>`
            
            .. attribute:: detail
            
            	Show the deatil info for a installed package
            	**type**\:  :py:class:`Detail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.Packages.Package.Detail>`
            
            

            """

            _prefix = 'spirit-install-instmgr-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(SoftwareInstall.Packages.Package, self).__init__()

                self.yang_name = "package"
                self.yang_parent_name = "packages"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['package_name']
                self._child_classes = OrderedDict([("verbose", ("verbose", SoftwareInstall.Packages.Package.Verbose)), ("brief", ("brief", SoftwareInstall.Packages.Package.Brief)), ("detail", ("detail", SoftwareInstall.Packages.Package.Detail))])
                self._leafs = OrderedDict([
                    ('package_name', (YLeaf(YType.str, 'package-name'), ['str'])),
                ])
                self.package_name = None

                self.verbose = SoftwareInstall.Packages.Package.Verbose()
                self.verbose.parent = self
                self._children_name_map["verbose"] = "verbose"

                self.brief = SoftwareInstall.Packages.Package.Brief()
                self.brief.parent = self
                self._children_name_map["brief"] = "brief"

                self.detail = SoftwareInstall.Packages.Package.Detail()
                self.detail.parent = self
                self._children_name_map["detail"] = "detail"
                self._segment_path = lambda: "package" + "[package-name='" + str(self.package_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/packages/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(SoftwareInstall.Packages.Package, ['package_name'], name, value)


            class Verbose(Entity):
                """
                Show the verbose info for a installed package
                
                .. attribute:: log
                
                	log
                	**type**\: str
                
                

                """

                _prefix = 'spirit-install-instmgr-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(SoftwareInstall.Packages.Package.Verbose, self).__init__()

                    self.yang_name = "verbose"
                    self.yang_parent_name = "package"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('log', (YLeaf(YType.str, 'log'), ['str'])),
                    ])
                    self.log = None
                    self._segment_path = lambda: "verbose"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(SoftwareInstall.Packages.Package.Verbose, [u'log'], name, value)


            class Brief(Entity):
                """
                Show the info for a installed package
                
                .. attribute:: log
                
                	log
                	**type**\: str
                
                

                """

                _prefix = 'spirit-install-instmgr-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(SoftwareInstall.Packages.Package.Brief, self).__init__()

                    self.yang_name = "brief"
                    self.yang_parent_name = "package"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('log', (YLeaf(YType.str, 'log'), ['str'])),
                    ])
                    self.log = None
                    self._segment_path = lambda: "brief"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(SoftwareInstall.Packages.Package.Brief, [u'log'], name, value)


            class Detail(Entity):
                """
                Show the deatil info for a installed package
                
                .. attribute:: log
                
                	log
                	**type**\: str
                
                

                """

                _prefix = 'spirit-install-instmgr-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(SoftwareInstall.Packages.Package.Detail, self).__init__()

                    self.yang_name = "detail"
                    self.yang_parent_name = "package"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('log', (YLeaf(YType.str, 'log'), ['str'])),
                    ])
                    self.log = None
                    self._segment_path = lambda: "detail"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(SoftwareInstall.Packages.Package.Detail, [u'log'], name, value)


    class OperationLogs(Entity):
        """
        Show log file
        
        .. attribute:: operation_log
        
        	Show log file for the specified install ID
        	**type**\: list of  		 :py:class:`OperationLog <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.OperationLogs.OperationLog>`
        
        

        """

        _prefix = 'spirit-install-instmgr-oper'
        _revision = '2017-09-07'

        def __init__(self):
            super(SoftwareInstall.OperationLogs, self).__init__()

            self.yang_name = "operation-logs"
            self.yang_parent_name = "software-install"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("operation-log", ("operation_log", SoftwareInstall.OperationLogs.OperationLog))])
            self._leafs = OrderedDict()

            self.operation_log = YList(self)
            self._segment_path = lambda: "operation-logs"
            self._absolute_path = lambda: "Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(SoftwareInstall.OperationLogs, [], name, value)


        class OperationLog(Entity):
            """
            Show log file for the specified install ID
            
            .. attribute:: log_id  (key)
            
            	Log ID number
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: summary
            
            	Show summary log file for the specified install ID
            	**type**\:  :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.OperationLogs.OperationLog.Summary>`
            
            .. attribute:: detail
            
            	Show detailed log file for the specified install ID
            	**type**\:  :py:class:`Detail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.OperationLogs.OperationLog.Detail>`
            
            

            """

            _prefix = 'spirit-install-instmgr-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(SoftwareInstall.OperationLogs.OperationLog, self).__init__()

                self.yang_name = "operation-log"
                self.yang_parent_name = "operation-logs"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['log_id']
                self._child_classes = OrderedDict([("summary", ("summary", SoftwareInstall.OperationLogs.OperationLog.Summary)), ("detail", ("detail", SoftwareInstall.OperationLogs.OperationLog.Detail))])
                self._leafs = OrderedDict([
                    ('log_id', (YLeaf(YType.uint32, 'log-id'), ['int'])),
                ])
                self.log_id = None

                self.summary = SoftwareInstall.OperationLogs.OperationLog.Summary()
                self.summary.parent = self
                self._children_name_map["summary"] = "summary"

                self.detail = SoftwareInstall.OperationLogs.OperationLog.Detail()
                self.detail.parent = self
                self._children_name_map["detail"] = "detail"
                self._segment_path = lambda: "operation-log" + "[log-id='" + str(self.log_id) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/operation-logs/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(SoftwareInstall.OperationLogs.OperationLog, ['log_id'], name, value)


            class Summary(Entity):
                """
                Show summary log file for the specified
                install ID
                
                .. attribute:: log
                
                	log
                	**type**\: str
                
                

                """

                _prefix = 'spirit-install-instmgr-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(SoftwareInstall.OperationLogs.OperationLog.Summary, self).__init__()

                    self.yang_name = "summary"
                    self.yang_parent_name = "operation-log"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('log', (YLeaf(YType.str, 'log'), ['str'])),
                    ])
                    self.log = None
                    self._segment_path = lambda: "summary"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(SoftwareInstall.OperationLogs.OperationLog.Summary, [u'log'], name, value)


            class Detail(Entity):
                """
                Show detailed log file for the specified
                install ID
                
                .. attribute:: log
                
                	log
                	**type**\: str
                
                

                """

                _prefix = 'spirit-install-instmgr-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(SoftwareInstall.OperationLogs.OperationLog.Detail, self).__init__()

                    self.yang_name = "detail"
                    self.yang_parent_name = "operation-log"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('log', (YLeaf(YType.str, 'log'), ['str'])),
                    ])
                    self.log = None
                    self._segment_path = lambda: "detail"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(SoftwareInstall.OperationLogs.OperationLog.Detail, [u'log'], name, value)


    class Repository(Entity):
        """
        Show packages stored in install software
        repositories
        
        .. attribute:: xr
        
        	Show install software repository for XR
        	**type**\:  :py:class:`Xr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.Repository.Xr>`
        
        .. attribute:: all
        
        	Show contents of all install software repositories
        	**type**\:  :py:class:`All <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.Repository.All>`
        
        

        """

        _prefix = 'spirit-install-instmgr-oper'
        _revision = '2017-09-07'

        def __init__(self):
            super(SoftwareInstall.Repository, self).__init__()

            self.yang_name = "repository"
            self.yang_parent_name = "software-install"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("xr", ("xr", SoftwareInstall.Repository.Xr)), ("all", ("all", SoftwareInstall.Repository.All))])
            self._leafs = OrderedDict()

            self.xr = SoftwareInstall.Repository.Xr()
            self.xr.parent = self
            self._children_name_map["xr"] = "xr"

            self.all = SoftwareInstall.Repository.All()
            self.all.parent = self
            self._children_name_map["all"] = "all"
            self._segment_path = lambda: "repository"
            self._absolute_path = lambda: "Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(SoftwareInstall.Repository, [], name, value)


        class Xr(Entity):
            """
            Show install software repository for XR
            
            .. attribute:: log
            
            	log
            	**type**\: str
            
            

            """

            _prefix = 'spirit-install-instmgr-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(SoftwareInstall.Repository.Xr, self).__init__()

                self.yang_name = "xr"
                self.yang_parent_name = "repository"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('log', (YLeaf(YType.str, 'log'), ['str'])),
                ])
                self.log = None
                self._segment_path = lambda: "xr"
                self._absolute_path = lambda: "Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/repository/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(SoftwareInstall.Repository.Xr, [u'log'], name, value)


        class All(Entity):
            """
            Show contents of all install software
            repositories
            
            .. attribute:: log
            
            	log
            	**type**\: str
            
            

            """

            _prefix = 'spirit-install-instmgr-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(SoftwareInstall.Repository.All, self).__init__()

                self.yang_name = "all"
                self.yang_parent_name = "repository"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('log', (YLeaf(YType.str, 'log'), ['str'])),
                ])
                self.log = None
                self._segment_path = lambda: "all"
                self._absolute_path = lambda: "Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/repository/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(SoftwareInstall.Repository.All, [u'log'], name, value)

    def clone_ptr(self):
        self._top_entity = SoftwareInstall()
        return self._top_entity

