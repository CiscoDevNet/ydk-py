""" Cisco_IOS_XR_spirit_install_instmgr_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR spirit\-install\-instmgr package operational data.

This module contains definitions
for the following management objects\:
  software\-install\: Install operations info

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class CardTypeEt(Enum):
    """
    CardTypeEt

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
    IsdErrorEt

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
    IsdIssuStatusEt

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
    IsdStateEt

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

    none = Enum.YLeaf(0, "none")

    idle = Enum.YLeaf(1, "idle")

    init = Enum.YLeaf(2, "init")

    init_done = Enum.YLeaf(3, "init-done")

    load_prep = Enum.YLeaf(4, "load-prep")

    load_exec = Enum.YLeaf(5, "load-exec")

    load_issu_go = Enum.YLeaf(6, "load-issu-go")

    load_done = Enum.YLeaf(7, "load-done")

    run_prep = Enum.YLeaf(8, "run-prep")

    big_bang = Enum.YLeaf(9, "big-bang")

    run_done = Enum.YLeaf(10, "run-done")

    cleanup = Enum.YLeaf(11, "cleanup")

    cleanup_done = Enum.YLeaf(12, "cleanup-done")

    abort = Enum.YLeaf(13, "abort")

    abort_done = Enum.YLeaf(14, "abort-done")

    abort_cleanup = Enum.YLeaf(15, "abort-cleanup")

    unknown_state = Enum.YLeaf(16, "unknown-state")


class IssuNodeRoleEt(Enum):
    """
    IssuNodeRoleEt

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
    IssudirNodeStatusEt

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
    NodeRoleEt

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
        super(SoftwareInstall, self).__init__()
        self._top_entity = None

        self.yang_name = "software-install"
        self.yang_parent_name = "Cisco-IOS-XR-spirit-install-instmgr-oper"

        self.active = SoftwareInstall.Active()
        self.active.parent = self
        self._children_name_map["active"] = "active"
        self._children_yang_names.add("active")

        self.all_operations_log = SoftwareInstall.AllOperationsLog()
        self.all_operations_log.parent = self
        self._children_name_map["all_operations_log"] = "all-operations-log"
        self._children_yang_names.add("all-operations-log")

        self.committed = SoftwareInstall.Committed()
        self.committed.parent = self
        self._children_name_map["committed"] = "committed"
        self._children_yang_names.add("committed")

        self.files = SoftwareInstall.Files()
        self.files.parent = self
        self._children_name_map["files"] = "files"
        self._children_yang_names.add("files")

        self.inactive = SoftwareInstall.Inactive()
        self.inactive.parent = self
        self._children_name_map["inactive"] = "inactive"
        self._children_yang_names.add("inactive")

        self.issu = SoftwareInstall.Issu()
        self.issu.parent = self
        self._children_name_map["issu"] = "issu"
        self._children_yang_names.add("issu")

        self.last_n_operation_logs = SoftwareInstall.LastNOperationLogs()
        self.last_n_operation_logs.parent = self
        self._children_name_map["last_n_operation_logs"] = "last-n-operation-logs"
        self._children_yang_names.add("last-n-operation-logs")

        self.operation_logs = SoftwareInstall.OperationLogs()
        self.operation_logs.parent = self
        self._children_name_map["operation_logs"] = "operation-logs"
        self._children_yang_names.add("operation-logs")

        self.packages = SoftwareInstall.Packages()
        self.packages.parent = self
        self._children_name_map["packages"] = "packages"
        self._children_yang_names.add("packages")

        self.prepare = SoftwareInstall.Prepare()
        self.prepare.parent = self
        self._children_name_map["prepare"] = "prepare"
        self._children_yang_names.add("prepare")

        self.repository = SoftwareInstall.Repository()
        self.repository.parent = self
        self._children_name_map["repository"] = "repository"
        self._children_yang_names.add("repository")

        self.request = SoftwareInstall.Request()
        self.request.parent = self
        self._children_name_map["request"] = "request"
        self._children_yang_names.add("request")

        self.version = SoftwareInstall.Version()
        self.version.parent = self
        self._children_name_map["version"] = "version"
        self._children_yang_names.add("version")


    class Files(Entity):
        """
        Show information about an installed file
        
        .. attribute:: file
        
        	Show information about an installed file
        	**type**\: list of    :py:class:`File <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.Files.File>`
        
        

        """

        _prefix = 'spirit-install-instmgr-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(SoftwareInstall.Files, self).__init__()

            self.yang_name = "files"
            self.yang_parent_name = "software-install"

            self.file = YList(self)

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
                        super(SoftwareInstall.Files, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(SoftwareInstall.Files, self).__setattr__(name, value)


        class File(Entity):
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
                super(SoftwareInstall.Files.File, self).__init__()

                self.yang_name = "file"
                self.yang_parent_name = "files"

                self.file_name = YLeaf(YType.str, "file-name")

                self.brief = SoftwareInstall.Files.File.Brief()
                self.brief.parent = self
                self._children_name_map["brief"] = "brief"
                self._children_yang_names.add("brief")

                self.detail = SoftwareInstall.Files.File.Detail()
                self.detail.parent = self
                self._children_name_map["detail"] = "detail"
                self._children_yang_names.add("detail")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("file_name") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(SoftwareInstall.Files.File, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(SoftwareInstall.Files.File, self).__setattr__(name, value)


            class Brief(Entity):
                """
                Show information about an installed file
                
                .. attribute:: log
                
                	log
                	**type**\:  str
                
                

                """

                _prefix = 'spirit-install-instmgr-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(SoftwareInstall.Files.File.Brief, self).__init__()

                    self.yang_name = "brief"
                    self.yang_parent_name = "file"

                    self.log = YLeaf(YType.str, "log")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("log") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(SoftwareInstall.Files.File.Brief, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(SoftwareInstall.Files.File.Brief, self).__setattr__(name, value)

                def has_data(self):
                    return self.log.is_set

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.log.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "brief" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.log.is_set or self.log.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.log.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "log"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "log"):
                        self.log = value
                        self.log.value_namespace = name_space
                        self.log.value_namespace_prefix = name_space_prefix


            class Detail(Entity):
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
                    super(SoftwareInstall.Files.File.Detail, self).__init__()

                    self.yang_name = "detail"
                    self.yang_parent_name = "file"

                    self.log = YLeaf(YType.str, "log")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("log") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(SoftwareInstall.Files.File.Detail, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(SoftwareInstall.Files.File.Detail, self).__setattr__(name, value)

                def has_data(self):
                    return self.log.is_set

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.log.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "detail" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.log.is_set or self.log.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.log.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "log"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "log"):
                        self.log = value
                        self.log.value_namespace = name_space
                        self.log.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.file_name.is_set or
                    (self.brief is not None and self.brief.has_data()) or
                    (self.detail is not None and self.detail.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.file_name.yfilter != YFilter.not_set or
                    (self.brief is not None and self.brief.has_operation()) or
                    (self.detail is not None and self.detail.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "file" + "[file-name='" + self.file_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/files/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.file_name.is_set or self.file_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.file_name.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "brief"):
                    if (self.brief is None):
                        self.brief = SoftwareInstall.Files.File.Brief()
                        self.brief.parent = self
                        self._children_name_map["brief"] = "brief"
                    return self.brief

                if (child_yang_name == "detail"):
                    if (self.detail is None):
                        self.detail = SoftwareInstall.Files.File.Detail()
                        self.detail.parent = self
                        self._children_name_map["detail"] = "detail"
                    return self.detail

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "brief" or name == "detail" or name == "file-name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "file-name"):
                    self.file_name = value
                    self.file_name.value_namespace = name_space
                    self.file_name.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.file:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.file:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "files" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "file"):
                for c in self.file:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = SoftwareInstall.Files.File()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.file.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "file"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class LastNOperationLogs(Entity):
        """
        Show log file for last n operations
        
        .. attribute:: last_n_operation_log
        
        	Show log file of last n operations
        	**type**\: list of    :py:class:`LastNOperationLog <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.LastNOperationLogs.LastNOperationLog>`
        
        

        """

        _prefix = 'spirit-install-instmgr-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(SoftwareInstall.LastNOperationLogs, self).__init__()

            self.yang_name = "last-n-operation-logs"
            self.yang_parent_name = "software-install"

            self.last_n_operation_log = YList(self)

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
                        super(SoftwareInstall.LastNOperationLogs, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(SoftwareInstall.LastNOperationLogs, self).__setattr__(name, value)


        class LastNOperationLog(Entity):
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
                super(SoftwareInstall.LastNOperationLogs.LastNOperationLog, self).__init__()

                self.yang_name = "last-n-operation-log"
                self.yang_parent_name = "last-n-operation-logs"

                self.last_n_logs = YLeaf(YType.int32, "last-n-logs")

                self.detail = SoftwareInstall.LastNOperationLogs.LastNOperationLog.Detail()
                self.detail.parent = self
                self._children_name_map["detail"] = "detail"
                self._children_yang_names.add("detail")

                self.summary = SoftwareInstall.LastNOperationLogs.LastNOperationLog.Summary()
                self.summary.parent = self
                self._children_name_map["summary"] = "summary"
                self._children_yang_names.add("summary")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("last_n_logs") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(SoftwareInstall.LastNOperationLogs.LastNOperationLog, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(SoftwareInstall.LastNOperationLogs.LastNOperationLog, self).__setattr__(name, value)


            class Summary(Entity):
                """
                Show summary log file for last n operations
                
                .. attribute:: log
                
                	log
                	**type**\:  str
                
                

                """

                _prefix = 'spirit-install-instmgr-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(SoftwareInstall.LastNOperationLogs.LastNOperationLog.Summary, self).__init__()

                    self.yang_name = "summary"
                    self.yang_parent_name = "last-n-operation-log"

                    self.log = YLeaf(YType.str, "log")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("log") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(SoftwareInstall.LastNOperationLogs.LastNOperationLog.Summary, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(SoftwareInstall.LastNOperationLogs.LastNOperationLog.Summary, self).__setattr__(name, value)

                def has_data(self):
                    return self.log.is_set

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.log.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "summary" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.log.is_set or self.log.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.log.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "log"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "log"):
                        self.log = value
                        self.log.value_namespace = name_space
                        self.log.value_namespace_prefix = name_space_prefix


            class Detail(Entity):
                """
                Show detailed log file for last n operations
                
                .. attribute:: log
                
                	log
                	**type**\:  str
                
                

                """

                _prefix = 'spirit-install-instmgr-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(SoftwareInstall.LastNOperationLogs.LastNOperationLog.Detail, self).__init__()

                    self.yang_name = "detail"
                    self.yang_parent_name = "last-n-operation-log"

                    self.log = YLeaf(YType.str, "log")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("log") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(SoftwareInstall.LastNOperationLogs.LastNOperationLog.Detail, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(SoftwareInstall.LastNOperationLogs.LastNOperationLog.Detail, self).__setattr__(name, value)

                def has_data(self):
                    return self.log.is_set

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.log.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "detail" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.log.is_set or self.log.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.log.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "log"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "log"):
                        self.log = value
                        self.log.value_namespace = name_space
                        self.log.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.last_n_logs.is_set or
                    (self.detail is not None and self.detail.has_data()) or
                    (self.summary is not None and self.summary.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.last_n_logs.yfilter != YFilter.not_set or
                    (self.detail is not None and self.detail.has_operation()) or
                    (self.summary is not None and self.summary.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "last-n-operation-log" + "[last-n-logs='" + self.last_n_logs.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/last-n-operation-logs/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.last_n_logs.is_set or self.last_n_logs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.last_n_logs.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "detail"):
                    if (self.detail is None):
                        self.detail = SoftwareInstall.LastNOperationLogs.LastNOperationLog.Detail()
                        self.detail.parent = self
                        self._children_name_map["detail"] = "detail"
                    return self.detail

                if (child_yang_name == "summary"):
                    if (self.summary is None):
                        self.summary = SoftwareInstall.LastNOperationLogs.LastNOperationLog.Summary()
                        self.summary.parent = self
                        self._children_name_map["summary"] = "summary"
                    return self.summary

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "detail" or name == "summary" or name == "last-n-logs"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "last-n-logs"):
                    self.last_n_logs = value
                    self.last_n_logs.value_namespace = name_space
                    self.last_n_logs.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.last_n_operation_log:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.last_n_operation_log:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "last-n-operation-logs" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "last-n-operation-log"):
                for c in self.last_n_operation_log:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = SoftwareInstall.LastNOperationLogs.LastNOperationLog()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.last_n_operation_log.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "last-n-operation-log"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Prepare(Entity):
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
            super(SoftwareInstall.Prepare, self).__init__()

            self.yang_name = "prepare"
            self.yang_parent_name = "software-install"

            self.activate_message = YLeaf(YType.str, "activate-message")

            self.no_prepare_done = YLeaf(YType.str, "no-prepare-done")

            self.prepare_clean_message = YLeaf(YType.str, "prepare-clean-message")

            self.prepared_boot_image = YLeaf(YType.str, "prepared-boot-image")

            self.prepared_boot_partition = YLeaf(YType.str, "prepared-boot-partition")

            self.restart_type = YLeaf(YType.str, "restart-type")

            self.package = YList(self)
            self.rpm = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("activate_message",
                            "no_prepare_done",
                            "prepare_clean_message",
                            "prepared_boot_image",
                            "prepared_boot_partition",
                            "restart_type") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(SoftwareInstall.Prepare, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(SoftwareInstall.Prepare, self).__setattr__(name, value)


        class Rpm(Entity):
            """
            rpm
            
            .. attribute:: package
            
            	package
            	**type**\:  str
            
            

            """

            _prefix = 'spirit-install-instmgr-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(SoftwareInstall.Prepare.Rpm, self).__init__()

                self.yang_name = "rpm"
                self.yang_parent_name = "prepare"

                self.package = YLeaf(YType.str, "package")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("package") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(SoftwareInstall.Prepare.Rpm, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(SoftwareInstall.Prepare.Rpm, self).__setattr__(name, value)

            def has_data(self):
                return self.package.is_set

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.package.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "rpm" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/prepare/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.package.is_set or self.package.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.package.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "package"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "package"):
                    self.package = value
                    self.package.value_namespace = name_space
                    self.package.value_namespace_prefix = name_space_prefix


        class Package(Entity):
            """
            package
            
            .. attribute:: package
            
            	package
            	**type**\:  str
            
            

            """

            _prefix = 'spirit-install-instmgr-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(SoftwareInstall.Prepare.Package, self).__init__()

                self.yang_name = "package"
                self.yang_parent_name = "prepare"

                self.package = YLeaf(YType.str, "package")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("package") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(SoftwareInstall.Prepare.Package, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(SoftwareInstall.Prepare.Package, self).__setattr__(name, value)

            def has_data(self):
                return self.package.is_set

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.package.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "package" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/prepare/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.package.is_set or self.package.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.package.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "package"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "package"):
                    self.package = value
                    self.package.value_namespace = name_space
                    self.package.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.package:
                if (c.has_data()):
                    return True
            for c in self.rpm:
                if (c.has_data()):
                    return True
            return (
                self.activate_message.is_set or
                self.no_prepare_done.is_set or
                self.prepare_clean_message.is_set or
                self.prepared_boot_image.is_set or
                self.prepared_boot_partition.is_set or
                self.restart_type.is_set)

        def has_operation(self):
            for c in self.package:
                if (c.has_operation()):
                    return True
            for c in self.rpm:
                if (c.has_operation()):
                    return True
            return (
                self.yfilter != YFilter.not_set or
                self.activate_message.yfilter != YFilter.not_set or
                self.no_prepare_done.yfilter != YFilter.not_set or
                self.prepare_clean_message.yfilter != YFilter.not_set or
                self.prepared_boot_image.yfilter != YFilter.not_set or
                self.prepared_boot_partition.yfilter != YFilter.not_set or
                self.restart_type.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "prepare" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.activate_message.is_set or self.activate_message.yfilter != YFilter.not_set):
                leaf_name_data.append(self.activate_message.get_name_leafdata())
            if (self.no_prepare_done.is_set or self.no_prepare_done.yfilter != YFilter.not_set):
                leaf_name_data.append(self.no_prepare_done.get_name_leafdata())
            if (self.prepare_clean_message.is_set or self.prepare_clean_message.yfilter != YFilter.not_set):
                leaf_name_data.append(self.prepare_clean_message.get_name_leafdata())
            if (self.prepared_boot_image.is_set or self.prepared_boot_image.yfilter != YFilter.not_set):
                leaf_name_data.append(self.prepared_boot_image.get_name_leafdata())
            if (self.prepared_boot_partition.is_set or self.prepared_boot_partition.yfilter != YFilter.not_set):
                leaf_name_data.append(self.prepared_boot_partition.get_name_leafdata())
            if (self.restart_type.is_set or self.restart_type.yfilter != YFilter.not_set):
                leaf_name_data.append(self.restart_type.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "package"):
                for c in self.package:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = SoftwareInstall.Prepare.Package()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.package.append(c)
                return c

            if (child_yang_name == "rpm"):
                for c in self.rpm:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = SoftwareInstall.Prepare.Rpm()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.rpm.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "package" or name == "rpm" or name == "activate-message" or name == "no-prepare-done" or name == "prepare-clean-message" or name == "prepared-boot-image" or name == "prepared-boot-partition" or name == "restart-type"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "activate-message"):
                self.activate_message = value
                self.activate_message.value_namespace = name_space
                self.activate_message.value_namespace_prefix = name_space_prefix
            if(value_path == "no-prepare-done"):
                self.no_prepare_done = value
                self.no_prepare_done.value_namespace = name_space
                self.no_prepare_done.value_namespace_prefix = name_space_prefix
            if(value_path == "prepare-clean-message"):
                self.prepare_clean_message = value
                self.prepare_clean_message.value_namespace = name_space
                self.prepare_clean_message.value_namespace_prefix = name_space_prefix
            if(value_path == "prepared-boot-image"):
                self.prepared_boot_image = value
                self.prepared_boot_image.value_namespace = name_space
                self.prepared_boot_image.value_namespace_prefix = name_space_prefix
            if(value_path == "prepared-boot-partition"):
                self.prepared_boot_partition = value
                self.prepared_boot_partition.value_namespace = name_space
                self.prepared_boot_partition.value_namespace_prefix = name_space_prefix
            if(value_path == "restart-type"):
                self.restart_type = value
                self.restart_type.value_namespace = name_space
                self.restart_type.value_namespace_prefix = name_space_prefix


    class Active(Entity):
        """
        Show active packages installed
        
        .. attribute:: active_package_info
        
        	active package info
        	**type**\: list of    :py:class:`ActivePackageInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.Active.ActivePackageInfo>`
        
        

        """

        _prefix = 'spirit-install-instmgr-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(SoftwareInstall.Active, self).__init__()

            self.yang_name = "active"
            self.yang_parent_name = "software-install"

            self.active_package_info = YList(self)

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
                        super(SoftwareInstall.Active, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(SoftwareInstall.Active, self).__setattr__(name, value)


        class ActivePackageInfo(Entity):
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
                super(SoftwareInstall.Active.ActivePackageInfo, self).__init__()

                self.yang_name = "active-package-info"
                self.yang_parent_name = "active"

                self.active_packages = YLeaf(YType.str, "active-packages")

                self.boot_partition_name = YLeaf(YType.str, "boot-partition-name")

                self.error_message = YLeaf(YType.str, "error-message")

                self.location = YLeaf(YType.str, "location")

                self.node_type = YLeaf(YType.str, "node-type")

                self.number_of_active_packages = YLeaf(YType.uint32, "number-of-active-packages")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("active_packages",
                                "boot_partition_name",
                                "error_message",
                                "location",
                                "node_type",
                                "number_of_active_packages") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(SoftwareInstall.Active.ActivePackageInfo, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(SoftwareInstall.Active.ActivePackageInfo, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.active_packages.is_set or
                    self.boot_partition_name.is_set or
                    self.error_message.is_set or
                    self.location.is_set or
                    self.node_type.is_set or
                    self.number_of_active_packages.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.active_packages.yfilter != YFilter.not_set or
                    self.boot_partition_name.yfilter != YFilter.not_set or
                    self.error_message.yfilter != YFilter.not_set or
                    self.location.yfilter != YFilter.not_set or
                    self.node_type.yfilter != YFilter.not_set or
                    self.number_of_active_packages.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "active-package-info" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/active/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.active_packages.is_set or self.active_packages.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.active_packages.get_name_leafdata())
                if (self.boot_partition_name.is_set or self.boot_partition_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.boot_partition_name.get_name_leafdata())
                if (self.error_message.is_set or self.error_message.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.error_message.get_name_leafdata())
                if (self.location.is_set or self.location.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.location.get_name_leafdata())
                if (self.node_type.is_set or self.node_type.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.node_type.get_name_leafdata())
                if (self.number_of_active_packages.is_set or self.number_of_active_packages.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.number_of_active_packages.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "active-packages" or name == "boot-partition-name" or name == "error-message" or name == "location" or name == "node-type" or name == "number-of-active-packages"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "active-packages"):
                    self.active_packages = value
                    self.active_packages.value_namespace = name_space
                    self.active_packages.value_namespace_prefix = name_space_prefix
                if(value_path == "boot-partition-name"):
                    self.boot_partition_name = value
                    self.boot_partition_name.value_namespace = name_space
                    self.boot_partition_name.value_namespace_prefix = name_space_prefix
                if(value_path == "error-message"):
                    self.error_message = value
                    self.error_message.value_namespace = name_space
                    self.error_message.value_namespace_prefix = name_space_prefix
                if(value_path == "location"):
                    self.location = value
                    self.location.value_namespace = name_space
                    self.location.value_namespace_prefix = name_space_prefix
                if(value_path == "node-type"):
                    self.node_type = value
                    self.node_type.value_namespace = name_space
                    self.node_type.value_namespace_prefix = name_space_prefix
                if(value_path == "number-of-active-packages"):
                    self.number_of_active_packages = value
                    self.number_of_active_packages.value_namespace = name_space
                    self.number_of_active_packages.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.active_package_info:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.active_package_info:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "active" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "active-package-info"):
                for c in self.active_package_info:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = SoftwareInstall.Active.ActivePackageInfo()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.active_package_info.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "active-package-info"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Version(Entity):
        """
        Show install version
        
        .. attribute:: log
        
        	log
        	**type**\:  str
        
        

        """

        _prefix = 'spirit-install-instmgr-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(SoftwareInstall.Version, self).__init__()

            self.yang_name = "version"
            self.yang_parent_name = "software-install"

            self.log = YLeaf(YType.str, "log")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("log") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(SoftwareInstall.Version, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(SoftwareInstall.Version, self).__setattr__(name, value)

        def has_data(self):
            return self.log.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.log.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "version" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.log.is_set or self.log.yfilter != YFilter.not_set):
                leaf_name_data.append(self.log.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "log"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "log"):
                self.log = value
                self.log.value_namespace = name_space
                self.log.value_namespace_prefix = name_space_prefix


    class Inactive(Entity):
        """
        Show XR inactive packages
        
        .. attribute:: log
        
        	log
        	**type**\:  str
        
        

        """

        _prefix = 'spirit-install-instmgr-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(SoftwareInstall.Inactive, self).__init__()

            self.yang_name = "inactive"
            self.yang_parent_name = "software-install"

            self.log = YLeaf(YType.str, "log")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("log") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(SoftwareInstall.Inactive, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(SoftwareInstall.Inactive, self).__setattr__(name, value)

        def has_data(self):
            return self.log.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.log.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "inactive" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.log.is_set or self.log.yfilter != YFilter.not_set):
                leaf_name_data.append(self.log.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "log"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "log"):
                self.log = value
                self.log.value_namespace = name_space
                self.log.value_namespace_prefix = name_space_prefix


    class Request(Entity):
        """
        Show current request
        
        .. attribute:: log
        
        	log
        	**type**\:  str
        
        

        """

        _prefix = 'spirit-install-instmgr-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(SoftwareInstall.Request, self).__init__()

            self.yang_name = "request"
            self.yang_parent_name = "software-install"

            self.log = YLeaf(YType.str, "log")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("log") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(SoftwareInstall.Request, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(SoftwareInstall.Request, self).__setattr__(name, value)

        def has_data(self):
            return self.log.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.log.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "request" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.log.is_set or self.log.yfilter != YFilter.not_set):
                leaf_name_data.append(self.log.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "log"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "log"):
                self.log = value
                self.log.value_namespace = name_space
                self.log.value_namespace_prefix = name_space_prefix


    class Issu(Entity):
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
            super(SoftwareInstall.Issu, self).__init__()

            self.yang_name = "issu"
            self.yang_parent_name = "software-install"

            self.inventory = SoftwareInstall.Issu.Inventory()
            self.inventory.parent = self
            self._children_name_map["inventory"] = "inventory"
            self._children_yang_names.add("inventory")

            self.stage = SoftwareInstall.Issu.Stage()
            self.stage.parent = self
            self._children_name_map["stage"] = "stage"
            self._children_yang_names.add("stage")


        class Stage(Entity):
            """
            Show XR install issu stage
            
            .. attribute:: issu_error
            
            	ISSU Error
            	**type**\:   :py:class:`IsdErrorEt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.IsdErrorEt>`
            
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
            	**type**\:   :py:class:`IsdIssuStatusEt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.IsdIssuStatusEt>`
            
            .. attribute:: percentage
            
            	Percentage
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: percentage
            
            .. attribute:: state
            
            	State
            	**type**\:   :py:class:`IsdStateEt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.IsdStateEt>`
            
            

            """

            _prefix = 'spirit-install-instmgr-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(SoftwareInstall.Issu.Stage, self).__init__()

                self.yang_name = "stage"
                self.yang_parent_name = "issu"

                self.issu_error = YLeaf(YType.enumeration, "issu-error")

                self.issu_node_cnt = YLeaf(YType.int32, "issu-node-cnt")

                self.issu_ready_node_cnt = YLeaf(YType.int32, "issu-ready-node-cnt")

                self.issu_status = YLeaf(YType.enumeration, "issu-status")

                self.percentage = YLeaf(YType.int32, "percentage")

                self.state = YLeaf(YType.enumeration, "state")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("issu_error",
                                "issu_node_cnt",
                                "issu_ready_node_cnt",
                                "issu_status",
                                "percentage",
                                "state") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(SoftwareInstall.Issu.Stage, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(SoftwareInstall.Issu.Stage, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.issu_error.is_set or
                    self.issu_node_cnt.is_set or
                    self.issu_ready_node_cnt.is_set or
                    self.issu_status.is_set or
                    self.percentage.is_set or
                    self.state.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.issu_error.yfilter != YFilter.not_set or
                    self.issu_node_cnt.yfilter != YFilter.not_set or
                    self.issu_ready_node_cnt.yfilter != YFilter.not_set or
                    self.issu_status.yfilter != YFilter.not_set or
                    self.percentage.yfilter != YFilter.not_set or
                    self.state.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "stage" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/issu/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.issu_error.is_set or self.issu_error.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.issu_error.get_name_leafdata())
                if (self.issu_node_cnt.is_set or self.issu_node_cnt.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.issu_node_cnt.get_name_leafdata())
                if (self.issu_ready_node_cnt.is_set or self.issu_ready_node_cnt.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.issu_ready_node_cnt.get_name_leafdata())
                if (self.issu_status.is_set or self.issu_status.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.issu_status.get_name_leafdata())
                if (self.percentage.is_set or self.percentage.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.percentage.get_name_leafdata())
                if (self.state.is_set or self.state.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.state.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "issu-error" or name == "issu-node-cnt" or name == "issu-ready-node-cnt" or name == "issu-status" or name == "percentage" or name == "state"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "issu-error"):
                    self.issu_error = value
                    self.issu_error.value_namespace = name_space
                    self.issu_error.value_namespace_prefix = name_space_prefix
                if(value_path == "issu-node-cnt"):
                    self.issu_node_cnt = value
                    self.issu_node_cnt.value_namespace = name_space
                    self.issu_node_cnt.value_namespace_prefix = name_space_prefix
                if(value_path == "issu-ready-node-cnt"):
                    self.issu_ready_node_cnt = value
                    self.issu_ready_node_cnt.value_namespace = name_space
                    self.issu_ready_node_cnt.value_namespace_prefix = name_space_prefix
                if(value_path == "issu-status"):
                    self.issu_status = value
                    self.issu_status.value_namespace = name_space
                    self.issu_status.value_namespace_prefix = name_space_prefix
                if(value_path == "percentage"):
                    self.percentage = value
                    self.percentage.value_namespace = name_space
                    self.percentage.value_namespace_prefix = name_space_prefix
                if(value_path == "state"):
                    self.state = value
                    self.state.value_namespace = name_space
                    self.state.value_namespace_prefix = name_space_prefix


        class Inventory(Entity):
            """
            Show XR install issu inventory
            
            .. attribute:: invinfo
            
            	invinfo
            	**type**\: list of    :py:class:`Invinfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.Issu.Inventory.Invinfo>`
            
            

            """

            _prefix = 'spirit-install-instmgr-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(SoftwareInstall.Issu.Inventory, self).__init__()

                self.yang_name = "inventory"
                self.yang_parent_name = "issu"

                self.invinfo = YList(self)

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
                            super(SoftwareInstall.Issu.Inventory, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(SoftwareInstall.Issu.Inventory, self).__setattr__(name, value)


            class Invinfo(Entity):
                """
                invinfo
                
                .. attribute:: issu_node_role
                
                	ISSU Node Role
                	**type**\:   :py:class:`IssuNodeRoleEt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.IssuNodeRoleEt>`
                
                .. attribute:: node_id
                
                	Node ID
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: node_role
                
                	Node role
                	**type**\:   :py:class:`NodeRoleEt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.NodeRoleEt>`
                
                .. attribute:: node_state
                
                	Node State
                	**type**\:   :py:class:`IssudirNodeStatusEt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.IssudirNodeStatusEt>`
                
                .. attribute:: node_type
                
                	Node Type
                	**type**\:   :py:class:`CardTypeEt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.CardTypeEt>`
                
                

                """

                _prefix = 'spirit-install-instmgr-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(SoftwareInstall.Issu.Inventory.Invinfo, self).__init__()

                    self.yang_name = "invinfo"
                    self.yang_parent_name = "inventory"

                    self.issu_node_role = YLeaf(YType.enumeration, "issu-node-role")

                    self.node_id = YLeaf(YType.int32, "node-id")

                    self.node_role = YLeaf(YType.enumeration, "node-role")

                    self.node_state = YLeaf(YType.enumeration, "node-state")

                    self.node_type = YLeaf(YType.enumeration, "node-type")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("issu_node_role",
                                    "node_id",
                                    "node_role",
                                    "node_state",
                                    "node_type") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(SoftwareInstall.Issu.Inventory.Invinfo, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(SoftwareInstall.Issu.Inventory.Invinfo, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.issu_node_role.is_set or
                        self.node_id.is_set or
                        self.node_role.is_set or
                        self.node_state.is_set or
                        self.node_type.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.issu_node_role.yfilter != YFilter.not_set or
                        self.node_id.yfilter != YFilter.not_set or
                        self.node_role.yfilter != YFilter.not_set or
                        self.node_state.yfilter != YFilter.not_set or
                        self.node_type.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "invinfo" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/issu/inventory/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.issu_node_role.is_set or self.issu_node_role.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.issu_node_role.get_name_leafdata())
                    if (self.node_id.is_set or self.node_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.node_id.get_name_leafdata())
                    if (self.node_role.is_set or self.node_role.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.node_role.get_name_leafdata())
                    if (self.node_state.is_set or self.node_state.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.node_state.get_name_leafdata())
                    if (self.node_type.is_set or self.node_type.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.node_type.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "issu-node-role" or name == "node-id" or name == "node-role" or name == "node-state" or name == "node-type"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "issu-node-role"):
                        self.issu_node_role = value
                        self.issu_node_role.value_namespace = name_space
                        self.issu_node_role.value_namespace_prefix = name_space_prefix
                    if(value_path == "node-id"):
                        self.node_id = value
                        self.node_id.value_namespace = name_space
                        self.node_id.value_namespace_prefix = name_space_prefix
                    if(value_path == "node-role"):
                        self.node_role = value
                        self.node_role.value_namespace = name_space
                        self.node_role.value_namespace_prefix = name_space_prefix
                    if(value_path == "node-state"):
                        self.node_state = value
                        self.node_state.value_namespace = name_space
                        self.node_state.value_namespace_prefix = name_space_prefix
                    if(value_path == "node-type"):
                        self.node_type = value
                        self.node_type.value_namespace = name_space
                        self.node_type.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.invinfo:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.invinfo:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "inventory" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/issu/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "invinfo"):
                    for c in self.invinfo:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = SoftwareInstall.Issu.Inventory.Invinfo()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.invinfo.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "invinfo"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (
                (self.inventory is not None and self.inventory.has_data()) or
                (self.stage is not None and self.stage.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.inventory is not None and self.inventory.has_operation()) or
                (self.stage is not None and self.stage.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "issu" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "inventory"):
                if (self.inventory is None):
                    self.inventory = SoftwareInstall.Issu.Inventory()
                    self.inventory.parent = self
                    self._children_name_map["inventory"] = "inventory"
                return self.inventory

            if (child_yang_name == "stage"):
                if (self.stage is None):
                    self.stage = SoftwareInstall.Issu.Stage()
                    self.stage.parent = self
                    self._children_name_map["stage"] = "stage"
                return self.stage

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "inventory" or name == "stage"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Committed(Entity):
        """
        Show Committed packages installed
        
        .. attribute:: committed_package_info
        
        	committed package info
        	**type**\: list of    :py:class:`CommittedPackageInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.Committed.CommittedPackageInfo>`
        
        

        """

        _prefix = 'spirit-install-instmgr-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(SoftwareInstall.Committed, self).__init__()

            self.yang_name = "committed"
            self.yang_parent_name = "software-install"

            self.committed_package_info = YList(self)

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
                        super(SoftwareInstall.Committed, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(SoftwareInstall.Committed, self).__setattr__(name, value)


        class CommittedPackageInfo(Entity):
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
                super(SoftwareInstall.Committed.CommittedPackageInfo, self).__init__()

                self.yang_name = "committed-package-info"
                self.yang_parent_name = "committed"

                self.boot_partition_name = YLeaf(YType.str, "boot-partition-name")

                self.committed_packages = YLeaf(YType.str, "committed-packages")

                self.error_message = YLeaf(YType.str, "error-message")

                self.location = YLeaf(YType.str, "location")

                self.node_type = YLeaf(YType.str, "node-type")

                self.number_of_committed_packages = YLeaf(YType.uint32, "number-of-committed-packages")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("boot_partition_name",
                                "committed_packages",
                                "error_message",
                                "location",
                                "node_type",
                                "number_of_committed_packages") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(SoftwareInstall.Committed.CommittedPackageInfo, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(SoftwareInstall.Committed.CommittedPackageInfo, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.boot_partition_name.is_set or
                    self.committed_packages.is_set or
                    self.error_message.is_set or
                    self.location.is_set or
                    self.node_type.is_set or
                    self.number_of_committed_packages.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.boot_partition_name.yfilter != YFilter.not_set or
                    self.committed_packages.yfilter != YFilter.not_set or
                    self.error_message.yfilter != YFilter.not_set or
                    self.location.yfilter != YFilter.not_set or
                    self.node_type.yfilter != YFilter.not_set or
                    self.number_of_committed_packages.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "committed-package-info" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/committed/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.boot_partition_name.is_set or self.boot_partition_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.boot_partition_name.get_name_leafdata())
                if (self.committed_packages.is_set or self.committed_packages.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.committed_packages.get_name_leafdata())
                if (self.error_message.is_set or self.error_message.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.error_message.get_name_leafdata())
                if (self.location.is_set or self.location.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.location.get_name_leafdata())
                if (self.node_type.is_set or self.node_type.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.node_type.get_name_leafdata())
                if (self.number_of_committed_packages.is_set or self.number_of_committed_packages.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.number_of_committed_packages.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "boot-partition-name" or name == "committed-packages" or name == "error-message" or name == "location" or name == "node-type" or name == "number-of-committed-packages"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "boot-partition-name"):
                    self.boot_partition_name = value
                    self.boot_partition_name.value_namespace = name_space
                    self.boot_partition_name.value_namespace_prefix = name_space_prefix
                if(value_path == "committed-packages"):
                    self.committed_packages = value
                    self.committed_packages.value_namespace = name_space
                    self.committed_packages.value_namespace_prefix = name_space_prefix
                if(value_path == "error-message"):
                    self.error_message = value
                    self.error_message.value_namespace = name_space
                    self.error_message.value_namespace_prefix = name_space_prefix
                if(value_path == "location"):
                    self.location = value
                    self.location.value_namespace = name_space
                    self.location.value_namespace_prefix = name_space_prefix
                if(value_path == "node-type"):
                    self.node_type = value
                    self.node_type.value_namespace = name_space
                    self.node_type.value_namespace_prefix = name_space_prefix
                if(value_path == "number-of-committed-packages"):
                    self.number_of_committed_packages = value
                    self.number_of_committed_packages.value_namespace = name_space
                    self.number_of_committed_packages.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.committed_package_info:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.committed_package_info:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "committed" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "committed-package-info"):
                for c in self.committed_package_info:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = SoftwareInstall.Committed.CommittedPackageInfo()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.committed_package_info.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "committed-package-info"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class AllOperationsLog(Entity):
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
            super(SoftwareInstall.AllOperationsLog, self).__init__()

            self.yang_name = "all-operations-log"
            self.yang_parent_name = "software-install"

            self.detail = SoftwareInstall.AllOperationsLog.Detail()
            self.detail.parent = self
            self._children_name_map["detail"] = "detail"
            self._children_yang_names.add("detail")

            self.summary = SoftwareInstall.AllOperationsLog.Summary()
            self.summary.parent = self
            self._children_name_map["summary"] = "summary"
            self._children_yang_names.add("summary")


        class Summary(Entity):
            """
            Show summary log file for all operations
            
            .. attribute:: log
            
            	log
            	**type**\:  str
            
            

            """

            _prefix = 'spirit-install-instmgr-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(SoftwareInstall.AllOperationsLog.Summary, self).__init__()

                self.yang_name = "summary"
                self.yang_parent_name = "all-operations-log"

                self.log = YLeaf(YType.str, "log")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("log") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(SoftwareInstall.AllOperationsLog.Summary, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(SoftwareInstall.AllOperationsLog.Summary, self).__setattr__(name, value)

            def has_data(self):
                return self.log.is_set

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.log.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "summary" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/all-operations-log/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.log.is_set or self.log.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.log.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "log"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "log"):
                    self.log = value
                    self.log.value_namespace = name_space
                    self.log.value_namespace_prefix = name_space_prefix


        class Detail(Entity):
            """
            Show detailed log file for all operations
            
            .. attribute:: log
            
            	log
            	**type**\:  str
            
            

            """

            _prefix = 'spirit-install-instmgr-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(SoftwareInstall.AllOperationsLog.Detail, self).__init__()

                self.yang_name = "detail"
                self.yang_parent_name = "all-operations-log"

                self.log = YLeaf(YType.str, "log")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("log") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(SoftwareInstall.AllOperationsLog.Detail, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(SoftwareInstall.AllOperationsLog.Detail, self).__setattr__(name, value)

            def has_data(self):
                return self.log.is_set

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.log.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "detail" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/all-operations-log/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.log.is_set or self.log.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.log.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "log"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "log"):
                    self.log = value
                    self.log.value_namespace = name_space
                    self.log.value_namespace_prefix = name_space_prefix

        def has_data(self):
            return (
                (self.detail is not None and self.detail.has_data()) or
                (self.summary is not None and self.summary.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.detail is not None and self.detail.has_operation()) or
                (self.summary is not None and self.summary.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "all-operations-log" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "detail"):
                if (self.detail is None):
                    self.detail = SoftwareInstall.AllOperationsLog.Detail()
                    self.detail.parent = self
                    self._children_name_map["detail"] = "detail"
                return self.detail

            if (child_yang_name == "summary"):
                if (self.summary is None):
                    self.summary = SoftwareInstall.AllOperationsLog.Summary()
                    self.summary.parent = self
                    self._children_name_map["summary"] = "summary"
                return self.summary

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "detail" or name == "summary"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Packages(Entity):
        """
        Show the list of installed packages
        
        .. attribute:: package
        
        	Show the info for a installed package
        	**type**\: list of    :py:class:`Package <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.Packages.Package>`
        
        

        """

        _prefix = 'spirit-install-instmgr-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(SoftwareInstall.Packages, self).__init__()

            self.yang_name = "packages"
            self.yang_parent_name = "software-install"

            self.package = YList(self)

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
                        super(SoftwareInstall.Packages, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(SoftwareInstall.Packages, self).__setattr__(name, value)


        class Package(Entity):
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
                super(SoftwareInstall.Packages.Package, self).__init__()

                self.yang_name = "package"
                self.yang_parent_name = "packages"

                self.package_name = YLeaf(YType.str, "package-name")

                self.brief = SoftwareInstall.Packages.Package.Brief()
                self.brief.parent = self
                self._children_name_map["brief"] = "brief"
                self._children_yang_names.add("brief")

                self.detail = SoftwareInstall.Packages.Package.Detail()
                self.detail.parent = self
                self._children_name_map["detail"] = "detail"
                self._children_yang_names.add("detail")

                self.verbose = SoftwareInstall.Packages.Package.Verbose()
                self.verbose.parent = self
                self._children_name_map["verbose"] = "verbose"
                self._children_yang_names.add("verbose")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("package_name") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(SoftwareInstall.Packages.Package, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(SoftwareInstall.Packages.Package, self).__setattr__(name, value)


            class Verbose(Entity):
                """
                Show the verbose info for a installed package
                
                .. attribute:: log
                
                	log
                	**type**\:  str
                
                

                """

                _prefix = 'spirit-install-instmgr-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(SoftwareInstall.Packages.Package.Verbose, self).__init__()

                    self.yang_name = "verbose"
                    self.yang_parent_name = "package"

                    self.log = YLeaf(YType.str, "log")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("log") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(SoftwareInstall.Packages.Package.Verbose, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(SoftwareInstall.Packages.Package.Verbose, self).__setattr__(name, value)

                def has_data(self):
                    return self.log.is_set

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.log.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "verbose" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.log.is_set or self.log.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.log.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "log"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "log"):
                        self.log = value
                        self.log.value_namespace = name_space
                        self.log.value_namespace_prefix = name_space_prefix


            class Brief(Entity):
                """
                Show the info for a installed package
                
                .. attribute:: log
                
                	log
                	**type**\:  str
                
                

                """

                _prefix = 'spirit-install-instmgr-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(SoftwareInstall.Packages.Package.Brief, self).__init__()

                    self.yang_name = "brief"
                    self.yang_parent_name = "package"

                    self.log = YLeaf(YType.str, "log")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("log") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(SoftwareInstall.Packages.Package.Brief, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(SoftwareInstall.Packages.Package.Brief, self).__setattr__(name, value)

                def has_data(self):
                    return self.log.is_set

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.log.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "brief" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.log.is_set or self.log.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.log.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "log"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "log"):
                        self.log = value
                        self.log.value_namespace = name_space
                        self.log.value_namespace_prefix = name_space_prefix


            class Detail(Entity):
                """
                Show the deatil info for a installed package
                
                .. attribute:: log
                
                	log
                	**type**\:  str
                
                

                """

                _prefix = 'spirit-install-instmgr-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(SoftwareInstall.Packages.Package.Detail, self).__init__()

                    self.yang_name = "detail"
                    self.yang_parent_name = "package"

                    self.log = YLeaf(YType.str, "log")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("log") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(SoftwareInstall.Packages.Package.Detail, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(SoftwareInstall.Packages.Package.Detail, self).__setattr__(name, value)

                def has_data(self):
                    return self.log.is_set

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.log.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "detail" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.log.is_set or self.log.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.log.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "log"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "log"):
                        self.log = value
                        self.log.value_namespace = name_space
                        self.log.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.package_name.is_set or
                    (self.brief is not None and self.brief.has_data()) or
                    (self.detail is not None and self.detail.has_data()) or
                    (self.verbose is not None and self.verbose.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.package_name.yfilter != YFilter.not_set or
                    (self.brief is not None and self.brief.has_operation()) or
                    (self.detail is not None and self.detail.has_operation()) or
                    (self.verbose is not None and self.verbose.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "package" + "[package-name='" + self.package_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/packages/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.package_name.is_set or self.package_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.package_name.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "brief"):
                    if (self.brief is None):
                        self.brief = SoftwareInstall.Packages.Package.Brief()
                        self.brief.parent = self
                        self._children_name_map["brief"] = "brief"
                    return self.brief

                if (child_yang_name == "detail"):
                    if (self.detail is None):
                        self.detail = SoftwareInstall.Packages.Package.Detail()
                        self.detail.parent = self
                        self._children_name_map["detail"] = "detail"
                    return self.detail

                if (child_yang_name == "verbose"):
                    if (self.verbose is None):
                        self.verbose = SoftwareInstall.Packages.Package.Verbose()
                        self.verbose.parent = self
                        self._children_name_map["verbose"] = "verbose"
                    return self.verbose

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "brief" or name == "detail" or name == "verbose" or name == "package-name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "package-name"):
                    self.package_name = value
                    self.package_name.value_namespace = name_space
                    self.package_name.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.package:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.package:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "packages" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "package"):
                for c in self.package:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = SoftwareInstall.Packages.Package()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.package.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "package"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class OperationLogs(Entity):
        """
        Show log file
        
        .. attribute:: operation_log
        
        	Show log file for the specified install ID
        	**type**\: list of    :py:class:`OperationLog <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper.SoftwareInstall.OperationLogs.OperationLog>`
        
        

        """

        _prefix = 'spirit-install-instmgr-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(SoftwareInstall.OperationLogs, self).__init__()

            self.yang_name = "operation-logs"
            self.yang_parent_name = "software-install"

            self.operation_log = YList(self)

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
                        super(SoftwareInstall.OperationLogs, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(SoftwareInstall.OperationLogs, self).__setattr__(name, value)


        class OperationLog(Entity):
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
                super(SoftwareInstall.OperationLogs.OperationLog, self).__init__()

                self.yang_name = "operation-log"
                self.yang_parent_name = "operation-logs"

                self.log_id = YLeaf(YType.int32, "log-id")

                self.detail = SoftwareInstall.OperationLogs.OperationLog.Detail()
                self.detail.parent = self
                self._children_name_map["detail"] = "detail"
                self._children_yang_names.add("detail")

                self.summary = SoftwareInstall.OperationLogs.OperationLog.Summary()
                self.summary.parent = self
                self._children_name_map["summary"] = "summary"
                self._children_yang_names.add("summary")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("log_id") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(SoftwareInstall.OperationLogs.OperationLog, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(SoftwareInstall.OperationLogs.OperationLog, self).__setattr__(name, value)


            class Summary(Entity):
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
                    super(SoftwareInstall.OperationLogs.OperationLog.Summary, self).__init__()

                    self.yang_name = "summary"
                    self.yang_parent_name = "operation-log"

                    self.log = YLeaf(YType.str, "log")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("log") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(SoftwareInstall.OperationLogs.OperationLog.Summary, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(SoftwareInstall.OperationLogs.OperationLog.Summary, self).__setattr__(name, value)

                def has_data(self):
                    return self.log.is_set

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.log.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "summary" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.log.is_set or self.log.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.log.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "log"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "log"):
                        self.log = value
                        self.log.value_namespace = name_space
                        self.log.value_namespace_prefix = name_space_prefix


            class Detail(Entity):
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
                    super(SoftwareInstall.OperationLogs.OperationLog.Detail, self).__init__()

                    self.yang_name = "detail"
                    self.yang_parent_name = "operation-log"

                    self.log = YLeaf(YType.str, "log")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("log") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(SoftwareInstall.OperationLogs.OperationLog.Detail, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(SoftwareInstall.OperationLogs.OperationLog.Detail, self).__setattr__(name, value)

                def has_data(self):
                    return self.log.is_set

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.log.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "detail" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.log.is_set or self.log.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.log.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "log"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "log"):
                        self.log = value
                        self.log.value_namespace = name_space
                        self.log.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.log_id.is_set or
                    (self.detail is not None and self.detail.has_data()) or
                    (self.summary is not None and self.summary.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.log_id.yfilter != YFilter.not_set or
                    (self.detail is not None and self.detail.has_operation()) or
                    (self.summary is not None and self.summary.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "operation-log" + "[log-id='" + self.log_id.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/operation-logs/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.log_id.is_set or self.log_id.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.log_id.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "detail"):
                    if (self.detail is None):
                        self.detail = SoftwareInstall.OperationLogs.OperationLog.Detail()
                        self.detail.parent = self
                        self._children_name_map["detail"] = "detail"
                    return self.detail

                if (child_yang_name == "summary"):
                    if (self.summary is None):
                        self.summary = SoftwareInstall.OperationLogs.OperationLog.Summary()
                        self.summary.parent = self
                        self._children_name_map["summary"] = "summary"
                    return self.summary

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "detail" or name == "summary" or name == "log-id"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "log-id"):
                    self.log_id = value
                    self.log_id.value_namespace = name_space
                    self.log_id.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.operation_log:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.operation_log:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "operation-logs" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "operation-log"):
                for c in self.operation_log:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = SoftwareInstall.OperationLogs.OperationLog()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.operation_log.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "operation-log"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Repository(Entity):
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
            super(SoftwareInstall.Repository, self).__init__()

            self.yang_name = "repository"
            self.yang_parent_name = "software-install"

            self.all = SoftwareInstall.Repository.All()
            self.all.parent = self
            self._children_name_map["all"] = "all"
            self._children_yang_names.add("all")

            self.xr = SoftwareInstall.Repository.Xr()
            self.xr.parent = self
            self._children_name_map["xr"] = "xr"
            self._children_yang_names.add("xr")


        class Xr(Entity):
            """
            Show install software repository for XR
            
            .. attribute:: log
            
            	log
            	**type**\:  str
            
            

            """

            _prefix = 'spirit-install-instmgr-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(SoftwareInstall.Repository.Xr, self).__init__()

                self.yang_name = "xr"
                self.yang_parent_name = "repository"

                self.log = YLeaf(YType.str, "log")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("log") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(SoftwareInstall.Repository.Xr, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(SoftwareInstall.Repository.Xr, self).__setattr__(name, value)

            def has_data(self):
                return self.log.is_set

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.log.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "xr" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/repository/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.log.is_set or self.log.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.log.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "log"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "log"):
                    self.log = value
                    self.log.value_namespace = name_space
                    self.log.value_namespace_prefix = name_space_prefix


        class All(Entity):
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
                super(SoftwareInstall.Repository.All, self).__init__()

                self.yang_name = "all"
                self.yang_parent_name = "repository"

                self.log = YLeaf(YType.str, "log")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("log") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(SoftwareInstall.Repository.All, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(SoftwareInstall.Repository.All, self).__setattr__(name, value)

            def has_data(self):
                return self.log.is_set

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.log.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "all" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/repository/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.log.is_set or self.log.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.log.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "log"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "log"):
                    self.log = value
                    self.log.value_namespace = name_space
                    self.log.value_namespace_prefix = name_space_prefix

        def has_data(self):
            return (
                (self.all is not None and self.all.has_data()) or
                (self.xr is not None and self.xr.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.all is not None and self.all.has_operation()) or
                (self.xr is not None and self.xr.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "repository" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-spirit-install-instmgr-oper:software-install/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "all"):
                if (self.all is None):
                    self.all = SoftwareInstall.Repository.All()
                    self.all.parent = self
                    self._children_name_map["all"] = "all"
                return self.all

            if (child_yang_name == "xr"):
                if (self.xr is None):
                    self.xr = SoftwareInstall.Repository.Xr()
                    self.xr.parent = self
                    self._children_name_map["xr"] = "xr"
                return self.xr

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "all" or name == "xr"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.active is not None and self.active.has_data()) or
            (self.all_operations_log is not None and self.all_operations_log.has_data()) or
            (self.committed is not None and self.committed.has_data()) or
            (self.files is not None and self.files.has_data()) or
            (self.inactive is not None and self.inactive.has_data()) or
            (self.issu is not None and self.issu.has_data()) or
            (self.last_n_operation_logs is not None and self.last_n_operation_logs.has_data()) or
            (self.operation_logs is not None and self.operation_logs.has_data()) or
            (self.packages is not None and self.packages.has_data()) or
            (self.prepare is not None and self.prepare.has_data()) or
            (self.repository is not None and self.repository.has_data()) or
            (self.request is not None and self.request.has_data()) or
            (self.version is not None and self.version.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.active is not None and self.active.has_operation()) or
            (self.all_operations_log is not None and self.all_operations_log.has_operation()) or
            (self.committed is not None and self.committed.has_operation()) or
            (self.files is not None and self.files.has_operation()) or
            (self.inactive is not None and self.inactive.has_operation()) or
            (self.issu is not None and self.issu.has_operation()) or
            (self.last_n_operation_logs is not None and self.last_n_operation_logs.has_operation()) or
            (self.operation_logs is not None and self.operation_logs.has_operation()) or
            (self.packages is not None and self.packages.has_operation()) or
            (self.prepare is not None and self.prepare.has_operation()) or
            (self.repository is not None and self.repository.has_operation()) or
            (self.request is not None and self.request.has_operation()) or
            (self.version is not None and self.version.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-spirit-install-instmgr-oper:software-install" + path_buffer

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

        if (child_yang_name == "active"):
            if (self.active is None):
                self.active = SoftwareInstall.Active()
                self.active.parent = self
                self._children_name_map["active"] = "active"
            return self.active

        if (child_yang_name == "all-operations-log"):
            if (self.all_operations_log is None):
                self.all_operations_log = SoftwareInstall.AllOperationsLog()
                self.all_operations_log.parent = self
                self._children_name_map["all_operations_log"] = "all-operations-log"
            return self.all_operations_log

        if (child_yang_name == "committed"):
            if (self.committed is None):
                self.committed = SoftwareInstall.Committed()
                self.committed.parent = self
                self._children_name_map["committed"] = "committed"
            return self.committed

        if (child_yang_name == "files"):
            if (self.files is None):
                self.files = SoftwareInstall.Files()
                self.files.parent = self
                self._children_name_map["files"] = "files"
            return self.files

        if (child_yang_name == "inactive"):
            if (self.inactive is None):
                self.inactive = SoftwareInstall.Inactive()
                self.inactive.parent = self
                self._children_name_map["inactive"] = "inactive"
            return self.inactive

        if (child_yang_name == "issu"):
            if (self.issu is None):
                self.issu = SoftwareInstall.Issu()
                self.issu.parent = self
                self._children_name_map["issu"] = "issu"
            return self.issu

        if (child_yang_name == "last-n-operation-logs"):
            if (self.last_n_operation_logs is None):
                self.last_n_operation_logs = SoftwareInstall.LastNOperationLogs()
                self.last_n_operation_logs.parent = self
                self._children_name_map["last_n_operation_logs"] = "last-n-operation-logs"
            return self.last_n_operation_logs

        if (child_yang_name == "operation-logs"):
            if (self.operation_logs is None):
                self.operation_logs = SoftwareInstall.OperationLogs()
                self.operation_logs.parent = self
                self._children_name_map["operation_logs"] = "operation-logs"
            return self.operation_logs

        if (child_yang_name == "packages"):
            if (self.packages is None):
                self.packages = SoftwareInstall.Packages()
                self.packages.parent = self
                self._children_name_map["packages"] = "packages"
            return self.packages

        if (child_yang_name == "prepare"):
            if (self.prepare is None):
                self.prepare = SoftwareInstall.Prepare()
                self.prepare.parent = self
                self._children_name_map["prepare"] = "prepare"
            return self.prepare

        if (child_yang_name == "repository"):
            if (self.repository is None):
                self.repository = SoftwareInstall.Repository()
                self.repository.parent = self
                self._children_name_map["repository"] = "repository"
            return self.repository

        if (child_yang_name == "request"):
            if (self.request is None):
                self.request = SoftwareInstall.Request()
                self.request.parent = self
                self._children_name_map["request"] = "request"
            return self.request

        if (child_yang_name == "version"):
            if (self.version is None):
                self.version = SoftwareInstall.Version()
                self.version.parent = self
                self._children_name_map["version"] = "version"
            return self.version

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "active" or name == "all-operations-log" or name == "committed" or name == "files" or name == "inactive" or name == "issu" or name == "last-n-operation-logs" or name == "operation-logs" or name == "packages" or name == "prepare" or name == "repository" or name == "request" or name == "version"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = SoftwareInstall()
        return self._top_entity

