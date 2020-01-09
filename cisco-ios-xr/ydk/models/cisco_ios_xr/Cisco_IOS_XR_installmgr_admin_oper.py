""" Cisco_IOS_XR_installmgr_admin_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR installmgr package
admin\-plane operational data.

This module contains definitions
for the following management objects\:
  install\: Information of software packages and install
    operations

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



class InstallmgrIsmNodeConforming(Enum):
    """
    InstallmgrIsmNodeConforming (Enum Class)

    ISSU manage node inventory type

    .. data:: conforming = 0

    	Conforming Nodes

    .. data:: none_conforming = 1

    	Non-conforming nodes

    .. data:: upgrade_fail = 2

    	Node Upgrade failed

    .. data:: none_conforming_spa = 3

    	Non-conforming SPAs

    .. data:: spa_upgrade_fail = 4

    	SPA Upgrade failed

    """

    conforming = Enum.YLeaf(0, "conforming")

    none_conforming = Enum.YLeaf(1, "none-conforming")

    upgrade_fail = Enum.YLeaf(2, "upgrade-fail")

    none_conforming_spa = Enum.YLeaf(3, "none-conforming-spa")

    spa_upgrade_fail = Enum.YLeaf(4, "spa-upgrade-fail")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
        return meta._meta_table['InstallmgrIsmNodeConforming']


class InstmgrBagAbortState(Enum):
    """
    InstmgrBagAbortState (Enum Class)

    The abortable state of an install command

    .. data:: abortable = 1

    	Operation can be aborted

    .. data:: no_longer_abortable = 2

    	Operation can no longer be aborted

    .. data:: never_abortable = 3

    	Operation cannot be aborted

    .. data:: already_aborted = 4

    	Operation has been aborted

    """

    abortable = Enum.YLeaf(1, "abortable")

    no_longer_abortable = Enum.YLeaf(2, "no-longer-abortable")

    never_abortable = Enum.YLeaf(3, "never-abortable")

    already_aborted = Enum.YLeaf(4, "already-aborted")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
        return meta._meta_table['InstmgrBagAbortState']


class InstmgrBagIiDirection(Enum):
    """
    InstmgrBagIiDirection (Enum Class)

    The Incremental Install direction

    .. data:: not_incremental = 0

    	Not incremental install operation

    .. data:: installing = 1

    	Installing

    .. data:: unwinding = 2

    	Unwinding

    """

    not_incremental = Enum.YLeaf(0, "not-incremental")

    installing = Enum.YLeaf(1, "installing")

    unwinding = Enum.YLeaf(2, "unwinding")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
        return meta._meta_table['InstmgrBagIiDirection']


class InstmgrBagIiState(Enum):
    """
    InstmgrBagIiState (Enum Class)

    The Incremental Install state of an install

    .. data:: idle = 1

    	Node to be upraded

    .. data:: in_progress = 2

    	Node is being upraded

    .. data:: completed = 3

    	Node upgraded successfully

    .. data:: aborted = 4

    	Node reverted to the old S/W

    .. data:: rebooted = 5

    	Node rebooted and held in MBI

    """

    idle = Enum.YLeaf(1, "idle")

    in_progress = Enum.YLeaf(2, "in-progress")

    completed = Enum.YLeaf(3, "completed")

    aborted = Enum.YLeaf(4, "aborted")

    rebooted = Enum.YLeaf(5, "rebooted")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
        return meta._meta_table['InstmgrBagIiState']


class InstmgrBagLogEntryUserMsgCategory(Enum):
    """
    InstmgrBagLogEntryUserMsgCategory (Enum Class)

    Category type

    .. data:: user_error = 1

    	User error

    .. data:: non_specific = 2

    	Non-specific message

    .. data:: warning = 3

    	Warning message

    .. data:: information = 4

    	Information message

    .. data:: user_prompt = 5

    	User prompt

    .. data:: log = 6

    	Log message

    .. data:: system_error = 7

    	System error

    .. data:: user_response = 8

    	User response

    """

    user_error = Enum.YLeaf(1, "user-error")

    non_specific = Enum.YLeaf(2, "non-specific")

    warning = Enum.YLeaf(3, "warning")

    information = Enum.YLeaf(4, "information")

    user_prompt = Enum.YLeaf(5, "user-prompt")

    log = Enum.YLeaf(6, "log")

    system_error = Enum.YLeaf(7, "system-error")

    user_response = Enum.YLeaf(8, "user-response")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
        return meta._meta_table['InstmgrBagLogEntryUserMsgCategory']


class InstmgrBagRequestTrigger(Enum):
    """
    InstmgrBagRequestTrigger (Enum Class)

    The trigger type of an install request

    .. data:: cli = 1

    	Request triggered by CLI

    .. data:: xr_xml = 2

    	Request triggered by XML

    """

    cli = Enum.YLeaf(1, "cli")

    xr_xml = Enum.YLeaf(2, "xr-xml")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
        return meta._meta_table['InstmgrBagRequestTrigger']


class InstmgrBagUserMsgCategory(Enum):
    """
    InstmgrBagUserMsgCategory (Enum Class)

    Instmgr bag user msg category

    .. data:: user_error = 1

    	User error

    .. data:: non_specific = 2

    	Non-specific message

    .. data:: warning = 3

    	Warning message

    .. data:: information = 4

    	Information message

    .. data:: user_prompt = 5

    	User prompt

    .. data:: log = 6

    	Log message

    .. data:: system_error = 7

    	System error

    .. data:: user_response = 8

    	User response

    """

    user_error = Enum.YLeaf(1, "user-error")

    non_specific = Enum.YLeaf(2, "non-specific")

    warning = Enum.YLeaf(3, "warning")

    information = Enum.YLeaf(4, "information")

    user_prompt = Enum.YLeaf(5, "user-prompt")

    log = Enum.YLeaf(6, "log")

    system_error = Enum.YLeaf(7, "system-error")

    user_response = Enum.YLeaf(8, "user-response")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
        return meta._meta_table['InstmgrBagUserMsgCategory']


class InstmgrCardState(Enum):
    """
    InstmgrCardState (Enum Class)

    Instmgr card state

    .. data:: instmgr_card_not_present = 0

    	instmgr card not present

    .. data:: instmgr_card_present = 1

    	instmgr card present

    .. data:: instmgr_card_reset = 2

    	instmgr card reset

    .. data:: instmgr_card_booting = 3

    	instmgr card booting

    .. data:: instmgr_card_mbi_booting = 4

    	instmgr card mbi booting

    .. data:: instmgr_card_running_mbi = 5

    	instmgr card running mbi

    .. data:: instmgr_card_running_ena = 6

    	instmgr card running ena

    .. data:: instmgr_card_bring_down = 7

    	instmgr card bring down

    .. data:: instmgr_card_ena_failure = 8

    	instmgr card ena failure

    .. data:: instmgr_card_f_diag_run = 9

    	instmgr card f diag run

    .. data:: instmgr_card_f_diag_failure = 10

    	instmgr card f diag failure

    .. data:: instmgr_card_powered = 11

    	instmgr card powered

    .. data:: instmgr_card_unpowered = 12

    	instmgr card unpowered

    .. data:: instmgr_card_mdr = 13

    	instmgr card mdr

    .. data:: instmgr_card_mdr_running_mbi = 14

    	instmgr card mdr running mbi

    .. data:: instmgr_card_main_t_mode = 15

    	instmgr card main t mode

    .. data:: instmgr_card_admin_down = 16

    	instmgr card admin down

    .. data:: instmgr_card_no_mon = 17

    	instmgr card no mon

    .. data:: instmgr_card_unknown = 18

    	instmgr card unknown

    .. data:: instmgr_card_failed = 19

    	instmgr card failed

    .. data:: instmgr_card_ok = 20

    	instmgr card ok

    .. data:: instmgr_card_missing = 21

    	instmgr card missing

    .. data:: instmgr_card_field_diag_downloading = 22

    	instmgr card field diag downloading

    .. data:: instmgr_card_field_diag_unmonitor = 23

    	instmgr card field diag unmonitor

    .. data:: instmgr_card_fabric_field_diag_unmonitor = 24

    	instmgr card fabric field diag unmonitor

    .. data:: instmgr_card_field_diag_rp_launching = 25

    	instmgr card field diag rp launching

    .. data:: instmgr_card_field_diag_running = 26

    	instmgr card field diag running

    .. data:: instmgr_card_field_diag_pass = 27

    	instmgr card field diag pass

    .. data:: instmgr_card_field_diag_fail = 28

    	instmgr card field diag fail

    .. data:: instmgr_card_field_diag_timeout = 29

    	instmgr card field diag timeout

    .. data:: instmgr_card_disabled = 30

    	instmgr card disabled

    .. data:: instmgr_card_spa_booting = 31

    	instmgr card spa booting

    .. data:: instmgr_card_not_allowed_online = 32

    	instmgr card not allowed online

    .. data:: instmgr_card_stopped = 33

    	instmgr card stopped

    .. data:: instmgr_card_incompatible_fw_ver = 34

    	instmgr card incompatible fw ver

    .. data:: instmgr_card_fpd_hold = 35

    	instmgr card fpd hold

    .. data:: instmgr_card_updating_fpd = 37

    	instmgr card updating fpd

    .. data:: instmgr_card_num_states = 38

    	instmgr card num states

    """

    instmgr_card_not_present = Enum.YLeaf(0, "instmgr-card-not-present")

    instmgr_card_present = Enum.YLeaf(1, "instmgr-card-present")

    instmgr_card_reset = Enum.YLeaf(2, "instmgr-card-reset")

    instmgr_card_booting = Enum.YLeaf(3, "instmgr-card-booting")

    instmgr_card_mbi_booting = Enum.YLeaf(4, "instmgr-card-mbi-booting")

    instmgr_card_running_mbi = Enum.YLeaf(5, "instmgr-card-running-mbi")

    instmgr_card_running_ena = Enum.YLeaf(6, "instmgr-card-running-ena")

    instmgr_card_bring_down = Enum.YLeaf(7, "instmgr-card-bring-down")

    instmgr_card_ena_failure = Enum.YLeaf(8, "instmgr-card-ena-failure")

    instmgr_card_f_diag_run = Enum.YLeaf(9, "instmgr-card-f-diag-run")

    instmgr_card_f_diag_failure = Enum.YLeaf(10, "instmgr-card-f-diag-failure")

    instmgr_card_powered = Enum.YLeaf(11, "instmgr-card-powered")

    instmgr_card_unpowered = Enum.YLeaf(12, "instmgr-card-unpowered")

    instmgr_card_mdr = Enum.YLeaf(13, "instmgr-card-mdr")

    instmgr_card_mdr_running_mbi = Enum.YLeaf(14, "instmgr-card-mdr-running-mbi")

    instmgr_card_main_t_mode = Enum.YLeaf(15, "instmgr-card-main-t-mode")

    instmgr_card_admin_down = Enum.YLeaf(16, "instmgr-card-admin-down")

    instmgr_card_no_mon = Enum.YLeaf(17, "instmgr-card-no-mon")

    instmgr_card_unknown = Enum.YLeaf(18, "instmgr-card-unknown")

    instmgr_card_failed = Enum.YLeaf(19, "instmgr-card-failed")

    instmgr_card_ok = Enum.YLeaf(20, "instmgr-card-ok")

    instmgr_card_missing = Enum.YLeaf(21, "instmgr-card-missing")

    instmgr_card_field_diag_downloading = Enum.YLeaf(22, "instmgr-card-field-diag-downloading")

    instmgr_card_field_diag_unmonitor = Enum.YLeaf(23, "instmgr-card-field-diag-unmonitor")

    instmgr_card_fabric_field_diag_unmonitor = Enum.YLeaf(24, "instmgr-card-fabric-field-diag-unmonitor")

    instmgr_card_field_diag_rp_launching = Enum.YLeaf(25, "instmgr-card-field-diag-rp-launching")

    instmgr_card_field_diag_running = Enum.YLeaf(26, "instmgr-card-field-diag-running")

    instmgr_card_field_diag_pass = Enum.YLeaf(27, "instmgr-card-field-diag-pass")

    instmgr_card_field_diag_fail = Enum.YLeaf(28, "instmgr-card-field-diag-fail")

    instmgr_card_field_diag_timeout = Enum.YLeaf(29, "instmgr-card-field-diag-timeout")

    instmgr_card_disabled = Enum.YLeaf(30, "instmgr-card-disabled")

    instmgr_card_spa_booting = Enum.YLeaf(31, "instmgr-card-spa-booting")

    instmgr_card_not_allowed_online = Enum.YLeaf(32, "instmgr-card-not-allowed-online")

    instmgr_card_stopped = Enum.YLeaf(33, "instmgr-card-stopped")

    instmgr_card_incompatible_fw_ver = Enum.YLeaf(34, "instmgr-card-incompatible-fw-ver")

    instmgr_card_fpd_hold = Enum.YLeaf(35, "instmgr-card-fpd-hold")

    instmgr_card_updating_fpd = Enum.YLeaf(37, "instmgr-card-updating-fpd")

    instmgr_card_num_states = Enum.YLeaf(38, "instmgr-card-num-states")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
        return meta._meta_table['InstmgrCardState']


class InstmgrGroup(Enum):
    """
    InstmgrGroup (Enum Class)

    Group type

    .. data:: inst_pkg_group_undefined = 0

    	Undefined grouping

    .. data:: inst_pkg_group_grouped = 1

    	Packages are grouped

    .. data:: inst_pkg_group_individual = 2

    	Packages are all individual

    """

    inst_pkg_group_undefined = Enum.YLeaf(0, "inst-pkg-group-undefined")

    inst_pkg_group_grouped = Enum.YLeaf(1, "inst-pkg-group-grouped")

    inst_pkg_group_individual = Enum.YLeaf(2, "inst-pkg-group-individual")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
        return meta._meta_table['InstmgrGroup']


class InstmgrInstallPhase(Enum):
    """
    InstmgrInstallPhase (Enum Class)

    Current operation phase

    .. data:: inst_phase_unknown = 0

    	Unknown operational phase

    .. data:: inst_phase_download = 10

    	Downloading

    .. data:: inst_phase_sw_change = 50

    	Performing software changes

    .. data:: inst_phase_cleaning_up = 1000

    	Cleaning up after op

    """

    inst_phase_unknown = Enum.YLeaf(0, "inst-phase-unknown")

    inst_phase_download = Enum.YLeaf(10, "inst-phase-download")

    inst_phase_sw_change = Enum.YLeaf(50, "inst-phase-sw-change")

    inst_phase_cleaning_up = Enum.YLeaf(1000, "inst-phase-cleaning-up")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
        return meta._meta_table['InstmgrInstallPhase']


class InstmgrIsmFsmState(Enum):
    """
    InstmgrIsmFsmState (Enum Class)

    Install manager FSM state

    .. data:: idle = 0

    	No ISSU in progress

    .. data:: init_done = 1

    	LOAD init

    .. data:: load_shut = 2

    	LOAD preparation

    .. data:: load_wait = 3

    	LOAD wait

    .. data:: load_stp_root_before = 4

    	LOAD root SC FO

    .. data:: load_standby_root_sc_upgrade = 5

    	LOAD standby ROOT SC Upgrade

    .. data:: load_standby_management_upgrade = 6

    	LOAD standby management upgrade

    .. data:: load_stp_root_after = 7

    	LOAD NDSC FO

    .. data:: load_fabric_upgrade = 8

    	LOAD fabric upgrade

    .. data:: load_management_issu_ready = 9

    	LOAD ISSU ready

    .. data:: load_done = 10

    	LOAD done

    .. data:: run_prep = 11

    	RUN preparation

    .. data:: run_wait = 12

    	RUN wait

    .. data:: runi_mdr_prep = 13

    	RUN iMDR preparation

    .. data:: runi_mdr_start = 14

    	RUN iMDR start

    .. data:: runi_mdr_complete = 15

    	RUN iMDR complete

    .. data:: run_make_standby_ready = 16

    	RUN make standby ready

    .. data:: run_root_scfo = 17

    	RUN root SC FO

    .. data:: run_ndscfo = 18

    	RUN NDSC FO

    .. data:: run_transient1 = 19

    	RUN transient1

    .. data:: run_dscfo = 20

    	RUN DSC FO

    .. data:: run_fo_complete = 21

    	RUN FO compelte

    .. data:: run_stp_root_return = 22

    	Run STP Root Return

    .. data:: runi_mdr_continue = 23

    	RUN iMDR continue

    .. data:: run_am_i_ready_afteri_mdr = 24

    	RUN I am ready after iMDR

    .. data:: run_nsf_ready = 25

    	RUN NSF ready

    .. data:: run_nsf_begin = 26

    	RUN iMDR begin

    .. data:: runi_mdr_done = 27

    	RUN iMDR done

    .. data:: run_management_issu_ready = 28

    	RUN mgmt issu ready

    .. data:: run_un_shut = 29

    	RUN unshut

    .. data:: run_is_done = 30

    	RUN done

    .. data:: state_max = 31

    	Max ISSU state

    """

    idle = Enum.YLeaf(0, "idle")

    init_done = Enum.YLeaf(1, "init-done")

    load_shut = Enum.YLeaf(2, "load-shut")

    load_wait = Enum.YLeaf(3, "load-wait")

    load_stp_root_before = Enum.YLeaf(4, "load-stp-root-before")

    load_standby_root_sc_upgrade = Enum.YLeaf(5, "load-standby-root-sc-upgrade")

    load_standby_management_upgrade = Enum.YLeaf(6, "load-standby-management-upgrade")

    load_stp_root_after = Enum.YLeaf(7, "load-stp-root-after")

    load_fabric_upgrade = Enum.YLeaf(8, "load-fabric-upgrade")

    load_management_issu_ready = Enum.YLeaf(9, "load-management-issu-ready")

    load_done = Enum.YLeaf(10, "load-done")

    run_prep = Enum.YLeaf(11, "run-prep")

    run_wait = Enum.YLeaf(12, "run-wait")

    runi_mdr_prep = Enum.YLeaf(13, "runi-mdr-prep")

    runi_mdr_start = Enum.YLeaf(14, "runi-mdr-start")

    runi_mdr_complete = Enum.YLeaf(15, "runi-mdr-complete")

    run_make_standby_ready = Enum.YLeaf(16, "run-make-standby-ready")

    run_root_scfo = Enum.YLeaf(17, "run-root-scfo")

    run_ndscfo = Enum.YLeaf(18, "run-ndscfo")

    run_transient1 = Enum.YLeaf(19, "run-transient1")

    run_dscfo = Enum.YLeaf(20, "run-dscfo")

    run_fo_complete = Enum.YLeaf(21, "run-fo-complete")

    run_stp_root_return = Enum.YLeaf(22, "run-stp-root-return")

    runi_mdr_continue = Enum.YLeaf(23, "runi-mdr-continue")

    run_am_i_ready_afteri_mdr = Enum.YLeaf(24, "run-am-i-ready-afteri-mdr")

    run_nsf_ready = Enum.YLeaf(25, "run-nsf-ready")

    run_nsf_begin = Enum.YLeaf(26, "run-nsf-begin")

    runi_mdr_done = Enum.YLeaf(27, "runi-mdr-done")

    run_management_issu_ready = Enum.YLeaf(28, "run-management-issu-ready")

    run_un_shut = Enum.YLeaf(29, "run-un-shut")

    run_is_done = Enum.YLeaf(30, "run-is-done")

    state_max = Enum.YLeaf(31, "state-max")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
        return meta._meta_table['InstmgrIsmFsmState']


class InstmgrIsmNodeState(Enum):
    """
    InstmgrIsmNodeState (Enum Class)

    ISSU manager node state

    .. data:: none = 0

    	No ISSU in progress

    .. data:: issu_node_gsp_ready = 1

    	Node GSP ready

    .. data:: load_shut_done = 2

    	Load shut done

    .. data:: standby_management_upgrade_done = 3

    	Standby management nodes upgrade done

    .. data:: fabric_upgrade_done = 4

    	Fabric nodes upgrade done

    .. data:: imdr_preparation_ack_received = 5

    	iMDR preparation ACK received

    .. data:: imdr_preparation_failed = 6

    	iMDR preparation ACK failed

    .. data:: imdr_start_ack_received = 7

    	iMDR start AVK received

    .. data:: imdr_start_failed = 8

    	iMDR start failed

    .. data:: imdr_complete_ack_received = 9

    	iMDR complete ACK received

    .. data:: imdr_complete_failed = 10

    	iMDR complete failed

    .. data:: standby_management_ready = 11

    	Standby management nodes ready

    .. data:: fo_acknowledged = 12

    	FO acked

    .. data:: fo_complete = 13

    	FO complete

    .. data:: standby_ready_after_fo = 14

    	Standby nodes ready after FO

    .. data:: iam_ready_afteri_mdr = 15

    	Node is ready after iMDR

    .. data:: nsf_ready = 16

    	NSF ready

    .. data:: nsf_begin_ack_received = 17

    	NSF begin ACK received

    .. data:: imdr_done = 18

    	iMDR done

    .. data:: unshut_done = 19

    	Unshut done

    .. data:: run_done = 20

    	Run done

    .. data:: imdr_abort_sent = 21

    	iMDR abort sent

    .. data:: imdr_abort_ack_received = 22

    	iMDR abort ACK Received

    .. data:: imdr_abort_failed = 23

    	iMDR abort failed

    .. data:: standby_management_downgrade_done = 24

    	Standby management nodes downgrade done

    .. data:: fabric_downgrade_done = 25

    	Fabric nodes downgrade done

    .. data:: reload_during_issu = 26

    	Node reloaded during ISSU

    .. data:: timneout = 27

    	Node time out

    .. data:: fabric_upgrade_failed = 28

    	Fabric upgrade failed

    .. data:: unsupported_hw = 29

    	Unsupported hardware

    .. data:: not_reachable = 30

    	Node unreachable

    .. data:: max = 32

    	Max node state

    """

    none = Enum.YLeaf(0, "none")

    issu_node_gsp_ready = Enum.YLeaf(1, "issu-node-gsp-ready")

    load_shut_done = Enum.YLeaf(2, "load-shut-done")

    standby_management_upgrade_done = Enum.YLeaf(3, "standby-management-upgrade-done")

    fabric_upgrade_done = Enum.YLeaf(4, "fabric-upgrade-done")

    imdr_preparation_ack_received = Enum.YLeaf(5, "imdr-preparation-ack-received")

    imdr_preparation_failed = Enum.YLeaf(6, "imdr-preparation-failed")

    imdr_start_ack_received = Enum.YLeaf(7, "imdr-start-ack-received")

    imdr_start_failed = Enum.YLeaf(8, "imdr-start-failed")

    imdr_complete_ack_received = Enum.YLeaf(9, "imdr-complete-ack-received")

    imdr_complete_failed = Enum.YLeaf(10, "imdr-complete-failed")

    standby_management_ready = Enum.YLeaf(11, "standby-management-ready")

    fo_acknowledged = Enum.YLeaf(12, "fo-acknowledged")

    fo_complete = Enum.YLeaf(13, "fo-complete")

    standby_ready_after_fo = Enum.YLeaf(14, "standby-ready-after-fo")

    iam_ready_afteri_mdr = Enum.YLeaf(15, "iam-ready-afteri-mdr")

    nsf_ready = Enum.YLeaf(16, "nsf-ready")

    nsf_begin_ack_received = Enum.YLeaf(17, "nsf-begin-ack-received")

    imdr_done = Enum.YLeaf(18, "imdr-done")

    unshut_done = Enum.YLeaf(19, "unshut-done")

    run_done = Enum.YLeaf(20, "run-done")

    imdr_abort_sent = Enum.YLeaf(21, "imdr-abort-sent")

    imdr_abort_ack_received = Enum.YLeaf(22, "imdr-abort-ack-received")

    imdr_abort_failed = Enum.YLeaf(23, "imdr-abort-failed")

    standby_management_downgrade_done = Enum.YLeaf(24, "standby-management-downgrade-done")

    fabric_downgrade_done = Enum.YLeaf(25, "fabric-downgrade-done")

    reload_during_issu = Enum.YLeaf(26, "reload-during-issu")

    timneout = Enum.YLeaf(27, "timneout")

    fabric_upgrade_failed = Enum.YLeaf(28, "fabric-upgrade-failed")

    unsupported_hw = Enum.YLeaf(29, "unsupported-hw")

    not_reachable = Enum.YLeaf(30, "not-reachable")

    max = Enum.YLeaf(32, "max")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
        return meta._meta_table['InstmgrIsmNodeState']


class InstmgrIssuAbortImpact(Enum):
    """
    InstmgrIssuAbortImpact (Enum Class)

    Abort impact

    .. data:: undefined = 0

    	Unknown abort impact

    .. data:: hitless = 1

    	Abort is hitless

    .. data:: traffic_outage = 2

    	Abort will not affect traffic

    .. data:: not_applicable = 3

    	Abort impact: n/a

    """

    undefined = Enum.YLeaf(0, "undefined")

    hitless = Enum.YLeaf(1, "hitless")

    traffic_outage = Enum.YLeaf(2, "traffic-outage")

    not_applicable = Enum.YLeaf(3, "not-applicable")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
        return meta._meta_table['InstmgrIssuAbortImpact']


class InstmgrIssuAbortMethod(Enum):
    """
    InstmgrIssuAbortMethod (Enum Class)

    Abort method

    .. data:: method_undefined = 0

    	Unknown abort method

    .. data:: method_no_operation = 1

    	No abort is required

    .. data:: method_standby_reload = 2

    	Abort will reload standby nodes

    .. data:: method_system_reload = 3

    	Abort will reload the whole system

    .. data:: method_rollback = 4

    	Abort will rollback

    .. data:: method_not_possible = 5

    	Abort is not possible

    .. data:: method_admin_only = 6

    	Abort is not possible by SDR user

    """

    method_undefined = Enum.YLeaf(0, "method-undefined")

    method_no_operation = Enum.YLeaf(1, "method-no-operation")

    method_standby_reload = Enum.YLeaf(2, "method-standby-reload")

    method_system_reload = Enum.YLeaf(3, "method-system-reload")

    method_rollback = Enum.YLeaf(4, "method-rollback")

    method_not_possible = Enum.YLeaf(5, "method-not-possible")

    method_admin_only = Enum.YLeaf(6, "method-admin-only")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
        return meta._meta_table['InstmgrIssuAbortMethod']


class InstmgrNodeRole(Enum):
    """
    InstmgrNodeRole (Enum Class)

    Node role

    .. data:: redundency_unknown = 0

    	Redundency unknown

    .. data:: redundency_active = 1

    	Redundency active

    .. data:: redundency_standby = 2

    	Redundency standby

    .. data:: redundency_unusable = 3

    	Redundency unusable

    """

    redundency_unknown = Enum.YLeaf(0, "redundency-unknown")

    redundency_active = Enum.YLeaf(1, "redundency-active")

    redundency_standby = Enum.YLeaf(2, "redundency-standby")

    redundency_unusable = Enum.YLeaf(3, "redundency-unusable")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
        return meta._meta_table['InstmgrNodeRole']


class InstmgrPiCard(Enum):
    """
    InstmgrPiCard (Enum Class)

    PI card types

    .. data:: type_rp = 0

    	Card type RP

    .. data:: type_drp = 1

    	Card Type DRP

    .. data:: type_lc = 2

    	Card type  LC

    .. data:: type_sc = 3

    	Card type SC

    .. data:: type_sp = 4

    	Card type SP

    .. data:: type_other = 5

    	Card type other

    """

    type_rp = Enum.YLeaf(0, "type-rp")

    type_drp = Enum.YLeaf(1, "type-drp")

    type_lc = Enum.YLeaf(2, "type-lc")

    type_sc = Enum.YLeaf(3, "type-sc")

    type_sp = Enum.YLeaf(4, "type-sp")

    type_other = Enum.YLeaf(5, "type-other")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
        return meta._meta_table['InstmgrPiCard']


class InstmgrPkg(Enum):
    """
    InstmgrPkg (Enum Class)

    Package type

    .. data:: inst_pkg_type_undefined = 0

    	Undefined package

    .. data:: inst_pkg_type_root = 1

    	Root package

    .. data:: inst_pkg_type_standard = 2

    	Standard package

    .. data:: inst_pkg_type_internal = 3

    	Internal package

    """

    inst_pkg_type_undefined = Enum.YLeaf(0, "inst-pkg-type-undefined")

    inst_pkg_type_root = Enum.YLeaf(1, "inst-pkg-type-root")

    inst_pkg_type_standard = Enum.YLeaf(2, "inst-pkg-type-standard")

    inst_pkg_type_internal = Enum.YLeaf(3, "inst-pkg-type-internal")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
        return meta._meta_table['InstmgrPkg']


class InstmgrRequest(Enum):
    """
    InstmgrRequest (Enum Class)

    Instmgr request

    .. data:: add = 1

    	install add

    .. data:: accept = 2

    	install accept

    .. data:: clean = 3

    	install clean

    .. data:: activate = 4

    	install activate

    .. data:: deactivate = 5

    	install deactivate

    .. data:: commit = 6

    	install commit

    .. data:: verify = 7

    	install verify

    .. data:: rollback = 8

    	install rollback

    .. data:: clear_rollback = 9

    	install clear rollback oldest

    .. data:: clear_log = 10

    	install clear historylog

    .. data:: health_check = 11

    	(Deprecated) install healthcheck

    .. data:: operation_ = 12

    	install run/accept/complete

    .. data:: stop_timer = 13

    	install auto-abort-timer stop

    .. data:: label = 14

    	install label

    .. data:: clear_label = 15

    	clear install label

    .. data:: extend = 16

    	install extend

    """

    add = Enum.YLeaf(1, "add")

    accept = Enum.YLeaf(2, "accept")

    clean = Enum.YLeaf(3, "clean")

    activate = Enum.YLeaf(4, "activate")

    deactivate = Enum.YLeaf(5, "deactivate")

    commit = Enum.YLeaf(6, "commit")

    verify = Enum.YLeaf(7, "verify")

    rollback = Enum.YLeaf(8, "rollback")

    clear_rollback = Enum.YLeaf(9, "clear-rollback")

    clear_log = Enum.YLeaf(10, "clear-log")

    health_check = Enum.YLeaf(11, "health-check")

    operation_ = Enum.YLeaf(12, "operation")

    stop_timer = Enum.YLeaf(13, "stop-timer")

    label = Enum.YLeaf(14, "label")

    clear_label = Enum.YLeaf(15, "clear-label")

    extend = Enum.YLeaf(16, "extend")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
        return meta._meta_table['InstmgrRequest']


class IsmCardTypeFamily(Enum):
    """
    IsmCardTypeFamily (Enum Class)

    Ism card type family

    .. data:: ndsc_active_rp = 1

    	Active NDSC RPs

    .. data:: ndsc_standby_rp = 2

    	Standby NDSC RPs

    .. data:: active_drp = 3

    	Active DRP

    .. data:: standby_drp = 4

    	Standby DRP

    .. data:: dsc_active_rp = 5

    	Active dSC

    .. data:: dsc_standby_rp = 6

    	Standby dSC

    .. data:: active_sc = 7

    	Active non-root SC

    .. data:: standby_sc = 8

    	Standby non-root SC

    .. data:: root_active_sc = 9

    	Active root SC

    .. data:: root_standby_sc = 10

    	Standby root SC

    .. data:: lc = 11

    	Line card

    .. data:: sp = 12

    	Non-Fabric SP

    .. data:: fabric_sp = 13

    	Fabric SP

    .. data:: spa = 14

    	SPA

    """

    ndsc_active_rp = Enum.YLeaf(1, "ndsc-active-rp")

    ndsc_standby_rp = Enum.YLeaf(2, "ndsc-standby-rp")

    active_drp = Enum.YLeaf(3, "active-drp")

    standby_drp = Enum.YLeaf(4, "standby-drp")

    dsc_active_rp = Enum.YLeaf(5, "dsc-active-rp")

    dsc_standby_rp = Enum.YLeaf(6, "dsc-standby-rp")

    active_sc = Enum.YLeaf(7, "active-sc")

    standby_sc = Enum.YLeaf(8, "standby-sc")

    root_active_sc = Enum.YLeaf(9, "root-active-sc")

    root_standby_sc = Enum.YLeaf(10, "root-standby-sc")

    lc = Enum.YLeaf(11, "lc")

    sp = Enum.YLeaf(12, "sp")

    fabric_sp = Enum.YLeaf(13, "fabric-sp")

    spa = Enum.YLeaf(14, "spa")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
        return meta._meta_table['IsmCardTypeFamily']



class Install(_Entity_):
    """
    Information of software packages and install
    operations
    
    .. attribute:: configuration_registers
    
    	Configuration register (confreg) information
    	**type**\:  :py:class:`ConfigurationRegisters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.ConfigurationRegisters>`
    
    	**config**\: False
    
    .. attribute:: request_statuses
    
    	Install operation request status
    	**type**\:  :py:class:`RequestStatuses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.RequestStatuses>`
    
    	**config**\: False
    
    .. attribute:: boot_variables
    
    	Boot variable information
    	**type**\:  :py:class:`BootVariables <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.BootVariables>`
    
    	**config**\: False
    
    .. attribute:: software
    
    	Software package,component and alias information
    	**type**\:  :py:class:`Software <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Software>`
    
    	**config**\: False
    
    .. attribute:: software_inventory
    
    	Information of install operations
    	**type**\:  :py:class:`SoftwareInventory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory>`
    
    	**config**\: False
    
    .. attribute:: issu
    
    	Information of install ISSU operations
    	**type**\:  :py:class:`Issu <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Issu>`
    
    	**config**\: False
    
    .. attribute:: boot_image
    
    	System Boot Image
    	**type**\:  :py:class:`BootImage <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.BootImage>`
    
    	**config**\: False
    
    .. attribute:: logs
    
    	Install operation log
    	**type**\:  :py:class:`Logs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Logs>`
    
    	**config**\: False
    
    .. attribute:: log_size
    
    	Install operation log history size
    	**type**\: int
    
    	**range:** 0..4294967295
    
    	**config**\: False
    
    

    """

    _prefix = 'installmgr-admin-oper'
    _revision = '2015-11-09'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(Install, self).__init__()
        self._top_entity = None

        self.yang_name = "install"
        self.yang_parent_name = "Cisco-IOS-XR-installmgr-admin-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("configuration-registers", ("configuration_registers", Install.ConfigurationRegisters)), ("request-statuses", ("request_statuses", Install.RequestStatuses)), ("boot-variables", ("boot_variables", Install.BootVariables)), ("software", ("software", Install.Software)), ("software-inventory", ("software_inventory", Install.SoftwareInventory)), ("issu", ("issu", Install.Issu)), ("boot-image", ("boot_image", Install.BootImage)), ("logs", ("logs", Install.Logs))])
        self._leafs = OrderedDict([
            ('log_size', (YLeaf(YType.uint32, 'log-size'), ['int'])),
        ])
        self.log_size = None

        self.configuration_registers = Install.ConfigurationRegisters()
        self.configuration_registers.parent = self
        self._children_name_map["configuration_registers"] = "configuration-registers"

        self.request_statuses = Install.RequestStatuses()
        self.request_statuses.parent = self
        self._children_name_map["request_statuses"] = "request-statuses"

        self.boot_variables = Install.BootVariables()
        self.boot_variables.parent = self
        self._children_name_map["boot_variables"] = "boot-variables"

        self.software = Install.Software()
        self.software.parent = self
        self._children_name_map["software"] = "software"

        self.software_inventory = Install.SoftwareInventory()
        self.software_inventory.parent = self
        self._children_name_map["software_inventory"] = "software-inventory"

        self.issu = Install.Issu()
        self.issu.parent = self
        self._children_name_map["issu"] = "issu"

        self.boot_image = Install.BootImage()
        self.boot_image.parent = self
        self._children_name_map["boot_image"] = "boot-image"

        self.logs = Install.Logs()
        self.logs.parent = self
        self._children_name_map["logs"] = "logs"
        self._segment_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Install, ['log_size'], name, value)


    class ConfigurationRegisters(_Entity_):
        """
        Configuration register (confreg) information
        
        .. attribute:: configuration_register
        
        	Configuration register for specific node
        	**type**\: list of  		 :py:class:`ConfigurationRegister <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.ConfigurationRegisters.ConfigurationRegister>`
        
        	**config**\: False
        
        

        """

        _prefix = 'installmgr-admin-oper'
        _revision = '2015-11-09'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Install.ConfigurationRegisters, self).__init__()

            self.yang_name = "configuration-registers"
            self.yang_parent_name = "install"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("configuration-register", ("configuration_register", Install.ConfigurationRegisters.ConfigurationRegister))])
            self._leafs = OrderedDict()

            self.configuration_register = YList(self)
            self._segment_path = lambda: "configuration-registers"
            self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Install.ConfigurationRegisters, [], name, value)


        class ConfigurationRegister(_Entity_):
            """
            Configuration register for specific node
            
            .. attribute:: node_name  (key)
            
            	Node name
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            	**config**\: False
            
            .. attribute:: config_register
            
            	Configuration register value
            	**type**\: str
            
            	**pattern:** [0\-9a\-fA\-F]{1,8}
            
            	**mandatory**\: True
            
            	**config**\: False
            
            

            """

            _prefix = 'installmgr-admin-oper'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Install.ConfigurationRegisters.ConfigurationRegister, self).__init__()

                self.yang_name = "configuration-register"
                self.yang_parent_name = "configuration-registers"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_name']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                    ('config_register', (YLeaf(YType.str, 'config-register'), ['str'])),
                ])
                self.node_name = None
                self.config_register = None
                self._segment_path = lambda: "configuration-register" + "[node-name='" + str(self.node_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/configuration-registers/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Install.ConfigurationRegisters.ConfigurationRegister, ['node_name', 'config_register'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                return meta._meta_table['Install.ConfigurationRegisters.ConfigurationRegister']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
            return meta._meta_table['Install.ConfigurationRegisters']['meta_info']


    class RequestStatuses(_Entity_):
        """
        Install operation request status
        
        .. attribute:: request_status
        
        	Request status Information
        	**type**\: list of  		 :py:class:`RequestStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.RequestStatuses.RequestStatus>`
        
        	**config**\: False
        
        

        """

        _prefix = 'installmgr-admin-oper'
        _revision = '2015-11-09'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Install.RequestStatuses, self).__init__()

            self.yang_name = "request-statuses"
            self.yang_parent_name = "install"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("request-status", ("request_status", Install.RequestStatuses.RequestStatus))])
            self._leafs = OrderedDict()

            self.request_status = YList(self)
            self._segment_path = lambda: "request-statuses"
            self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Install.RequestStatuses, [], name, value)


        class RequestStatus(_Entity_):
            """
            Request status Information
            
            .. attribute:: request_id  (key)
            
            	Install operation request ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: request_information
            
            	Requested install operation
            	**type**\:  :py:class:`RequestInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.RequestStatuses.RequestStatus.RequestInformation>`
            
            	**config**\: False
            
            .. attribute:: abort_status
            
            	How the abort will occur
            	**type**\:  :py:class:`AbortStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.RequestStatuses.RequestStatus.AbortStatus>`
            
            	**config**\: False
            
            .. attribute:: incremental_install_information
            
            	Incremental Install information
            	**type**\:  :py:class:`IncrementalInstallInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.RequestStatuses.RequestStatus.IncrementalInstallInformation>`
            
            	**config**\: False
            
            .. attribute:: percentage
            
            	Percentage completed
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            	**units**\: percentage
            
            .. attribute:: abort_state
            
            	Abort state
            	**type**\:  :py:class:`InstmgrBagAbortState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.InstmgrBagAbortState>`
            
            	**config**\: False
            
            .. attribute:: downloaded_bytes
            
            	Downloaded bytes
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: byte
            
            .. attribute:: unanswered_query
            
            	Whether the operation is blocked waiting for a response from the user
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: operation_phase
            
            	Phase of the operation
            	**type**\:  :py:class:`InstmgrInstallPhase <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.InstmgrInstallPhase>`
            
            	**config**\: False
            
            .. attribute:: issu_message
            
            	Messages related to ISSU operations
            	**type**\: list of  		 :py:class:`IssuMessage <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.RequestStatuses.RequestStatus.IssuMessage>`
            
            	**config**\: False
            
            .. attribute:: message
            
            	Messages output to the user
            	**type**\: list of  		 :py:class:`Message <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.RequestStatuses.RequestStatus.Message>`
            
            	**config**\: False
            
            

            """

            _prefix = 'installmgr-admin-oper'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Install.RequestStatuses.RequestStatus, self).__init__()

                self.yang_name = "request-status"
                self.yang_parent_name = "request-statuses"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['request_id']
                self._child_classes = OrderedDict([("request-information", ("request_information", Install.RequestStatuses.RequestStatus.RequestInformation)), ("abort-status", ("abort_status", Install.RequestStatuses.RequestStatus.AbortStatus)), ("incremental-install-information", ("incremental_install_information", Install.RequestStatuses.RequestStatus.IncrementalInstallInformation)), ("issu-message", ("issu_message", Install.RequestStatuses.RequestStatus.IssuMessage)), ("message", ("message", Install.RequestStatuses.RequestStatus.Message))])
                self._leafs = OrderedDict([
                    ('request_id', (YLeaf(YType.uint32, 'request-id'), ['int'])),
                    ('percentage', (YLeaf(YType.uint8, 'percentage'), ['int'])),
                    ('abort_state', (YLeaf(YType.enumeration, 'abort-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'InstmgrBagAbortState', '')])),
                    ('downloaded_bytes', (YLeaf(YType.uint32, 'downloaded-bytes'), ['int'])),
                    ('unanswered_query', (YLeaf(YType.boolean, 'unanswered-query'), ['bool'])),
                    ('operation_phase', (YLeaf(YType.enumeration, 'operation-phase'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'InstmgrInstallPhase', '')])),
                ])
                self.request_id = None
                self.percentage = None
                self.abort_state = None
                self.downloaded_bytes = None
                self.unanswered_query = None
                self.operation_phase = None

                self.request_information = Install.RequestStatuses.RequestStatus.RequestInformation()
                self.request_information.parent = self
                self._children_name_map["request_information"] = "request-information"

                self.abort_status = Install.RequestStatuses.RequestStatus.AbortStatus()
                self.abort_status.parent = self
                self._children_name_map["abort_status"] = "abort-status"

                self.incremental_install_information = Install.RequestStatuses.RequestStatus.IncrementalInstallInformation()
                self.incremental_install_information.parent = self
                self._children_name_map["incremental_install_information"] = "incremental-install-information"

                self.issu_message = YList(self)
                self.message = YList(self)
                self._segment_path = lambda: "request-status" + "[request-id='" + str(self.request_id) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/request-statuses/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Install.RequestStatuses.RequestStatus, ['request_id', 'percentage', 'abort_state', 'downloaded_bytes', 'unanswered_query', 'operation_phase'], name, value)


            class RequestInformation(_Entity_):
                """
                Requested install operation
                
                .. attribute:: request_id
                
                	Install id of operation
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: user_id
                
                	User ID that started the reqeust
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: trigger_type
                
                	Request trigger type
                	**type**\:  :py:class:`InstmgrBagRequestTrigger <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.InstmgrBagRequestTrigger>`
                
                	**config**\: False
                
                .. attribute:: request_option
                
                	Options affecting processing of install requests
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                	**config**\: False
                
                .. attribute:: operation_type
                
                	Requested operation type
                	**type**\:  :py:class:`InstmgrRequest <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.InstmgrRequest>`
                
                	**config**\: False
                
                .. attribute:: operation_detail
                
                	Detail operation information
                	**type**\: str
                
                	**config**\: False
                
                

                """

                _prefix = 'installmgr-admin-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Install.RequestStatuses.RequestStatus.RequestInformation, self).__init__()

                    self.yang_name = "request-information"
                    self.yang_parent_name = "request-status"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('request_id', (YLeaf(YType.uint32, 'request-id'), ['int'])),
                        ('user_id', (YLeaf(YType.str, 'user-id'), ['str'])),
                        ('trigger_type', (YLeaf(YType.enumeration, 'trigger-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'InstmgrBagRequestTrigger', '')])),
                        ('request_option', (YLeaf(YType.int32, 'request-option'), ['int'])),
                        ('operation_type', (YLeaf(YType.enumeration, 'operation-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'InstmgrRequest', '')])),
                        ('operation_detail', (YLeaf(YType.str, 'operation-detail'), ['str'])),
                    ])
                    self.request_id = None
                    self.user_id = None
                    self.trigger_type = None
                    self.request_option = None
                    self.operation_type = None
                    self.operation_detail = None
                    self._segment_path = lambda: "request-information"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Install.RequestStatuses.RequestStatus.RequestInformation, ['request_id', 'user_id', 'trigger_type', 'request_option', 'operation_type', 'operation_detail'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                    return meta._meta_table['Install.RequestStatuses.RequestStatus.RequestInformation']['meta_info']


            class AbortStatus(_Entity_):
                """
                How the abort will occur
                
                .. attribute:: abort_method
                
                	Method of abort
                	**type**\:  :py:class:`InstmgrIssuAbortMethod <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.InstmgrIssuAbortMethod>`
                
                	**config**\: False
                
                .. attribute:: abort_impact
                
                	Impact of abort
                	**type**\:  :py:class:`InstmgrIssuAbortImpact <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.InstmgrIssuAbortImpact>`
                
                	**config**\: False
                
                

                """

                _prefix = 'installmgr-admin-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Install.RequestStatuses.RequestStatus.AbortStatus, self).__init__()

                    self.yang_name = "abort-status"
                    self.yang_parent_name = "request-status"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('abort_method', (YLeaf(YType.enumeration, 'abort-method'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'InstmgrIssuAbortMethod', '')])),
                        ('abort_impact', (YLeaf(YType.enumeration, 'abort-impact'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'InstmgrIssuAbortImpact', '')])),
                    ])
                    self.abort_method = None
                    self.abort_impact = None
                    self._segment_path = lambda: "abort-status"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Install.RequestStatuses.RequestStatus.AbortStatus, ['abort_method', 'abort_impact'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                    return meta._meta_table['Install.RequestStatuses.RequestStatus.AbortStatus']['meta_info']


            class IncrementalInstallInformation(_Entity_):
                """
                Incremental Install information
                
                .. attribute:: direction
                
                	Install direction
                	**type**\:  :py:class:`InstmgrBagIiDirection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.InstmgrBagIiDirection>`
                
                	**config**\: False
                
                .. attribute:: ii_error
                
                	First error during incremental install
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: nodes
                
                	Participating nodes
                	**type**\: list of  		 :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.RequestStatuses.RequestStatus.IncrementalInstallInformation.Nodes>`
                
                	**config**\: False
                
                

                """

                _prefix = 'installmgr-admin-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Install.RequestStatuses.RequestStatus.IncrementalInstallInformation, self).__init__()

                    self.yang_name = "incremental-install-information"
                    self.yang_parent_name = "request-status"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("nodes", ("nodes", Install.RequestStatuses.RequestStatus.IncrementalInstallInformation.Nodes))])
                    self._leafs = OrderedDict([
                        ('direction', (YLeaf(YType.enumeration, 'direction'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'InstmgrBagIiDirection', '')])),
                        ('ii_error', (YLeaf(YType.str, 'ii-error'), ['str'])),
                    ])
                    self.direction = None
                    self.ii_error = None

                    self.nodes = YList(self)
                    self._segment_path = lambda: "incremental-install-information"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Install.RequestStatuses.RequestStatus.IncrementalInstallInformation, ['direction', 'ii_error'], name, value)


                class Nodes(_Entity_):
                    """
                    Participating nodes
                    
                    .. attribute:: node_name
                    
                    	Node identifier
                    	**type**\: str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    	**config**\: False
                    
                    .. attribute:: state
                    
                    	State
                    	**type**\:  :py:class:`InstmgrBagIiState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.InstmgrBagIiState>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'installmgr-admin-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Install.RequestStatuses.RequestStatus.IncrementalInstallInformation.Nodes, self).__init__()

                        self.yang_name = "nodes"
                        self.yang_parent_name = "incremental-install-information"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                            ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'InstmgrBagIiState', '')])),
                        ])
                        self.node_name = None
                        self.state = None
                        self._segment_path = lambda: "nodes"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Install.RequestStatuses.RequestStatus.IncrementalInstallInformation.Nodes, ['node_name', 'state'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                        return meta._meta_table['Install.RequestStatuses.RequestStatus.IncrementalInstallInformation.Nodes']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                    return meta._meta_table['Install.RequestStatuses.RequestStatus.IncrementalInstallInformation']['meta_info']


            class IssuMessage(_Entity_):
                """
                Messages related to ISSU operations
                
                .. attribute:: scope
                
                	Scope of the message
                	**type**\:  :py:class:`Scope <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.RequestStatuses.RequestStatus.IssuMessage.Scope>`
                
                	**config**\: False
                
                .. attribute:: category
                
                	Category of the message
                	**type**\:  :py:class:`InstmgrBagUserMsgCategory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.InstmgrBagUserMsgCategory>`
                
                	**config**\: False
                
                .. attribute:: message
                
                	Message
                	**type**\: str
                
                	**config**\: False
                
                

                """

                _prefix = 'installmgr-admin-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Install.RequestStatuses.RequestStatus.IssuMessage, self).__init__()

                    self.yang_name = "issu-message"
                    self.yang_parent_name = "request-status"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("scope", ("scope", Install.RequestStatuses.RequestStatus.IssuMessage.Scope))])
                    self._leafs = OrderedDict([
                        ('category', (YLeaf(YType.enumeration, 'category'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'InstmgrBagUserMsgCategory', '')])),
                        ('message', (YLeaf(YType.str, 'message'), ['str'])),
                    ])
                    self.category = None
                    self.message = None

                    self.scope = Install.RequestStatuses.RequestStatus.IssuMessage.Scope()
                    self.scope.parent = self
                    self._children_name_map["scope"] = "scope"
                    self._segment_path = lambda: "issu-message"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Install.RequestStatuses.RequestStatus.IssuMessage, ['category', 'message'], name, value)


                class Scope(_Entity_):
                    """
                    Scope of the message
                    
                    .. attribute:: admin_read
                    
                    	Does the admin want to read this?
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: affected_sd_rs
                    
                    	Which LRs are affected by the message
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'installmgr-admin-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Install.RequestStatuses.RequestStatus.IssuMessage.Scope, self).__init__()

                        self.yang_name = "scope"
                        self.yang_parent_name = "issu-message"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('admin_read', (YLeaf(YType.boolean, 'admin-read'), ['bool'])),
                            ('affected_sd_rs', (YLeaf(YType.uint32, 'affected-sd-rs'), ['int'])),
                        ])
                        self.admin_read = None
                        self.affected_sd_rs = None
                        self._segment_path = lambda: "scope"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Install.RequestStatuses.RequestStatus.IssuMessage.Scope, ['admin_read', 'affected_sd_rs'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                        return meta._meta_table['Install.RequestStatuses.RequestStatus.IssuMessage.Scope']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                    return meta._meta_table['Install.RequestStatuses.RequestStatus.IssuMessage']['meta_info']


            class Message(_Entity_):
                """
                Messages output to the user
                
                .. attribute:: scope
                
                	Scope of the message
                	**type**\:  :py:class:`Scope <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.RequestStatuses.RequestStatus.Message.Scope>`
                
                	**config**\: False
                
                .. attribute:: category
                
                	Category of the message
                	**type**\:  :py:class:`InstmgrBagUserMsgCategory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.InstmgrBagUserMsgCategory>`
                
                	**config**\: False
                
                .. attribute:: message
                
                	Message
                	**type**\: str
                
                	**config**\: False
                
                

                """

                _prefix = 'installmgr-admin-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Install.RequestStatuses.RequestStatus.Message, self).__init__()

                    self.yang_name = "message"
                    self.yang_parent_name = "request-status"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("scope", ("scope", Install.RequestStatuses.RequestStatus.Message.Scope))])
                    self._leafs = OrderedDict([
                        ('category', (YLeaf(YType.enumeration, 'category'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'InstmgrBagUserMsgCategory', '')])),
                        ('message', (YLeaf(YType.str, 'message'), ['str'])),
                    ])
                    self.category = None
                    self.message = None

                    self.scope = Install.RequestStatuses.RequestStatus.Message.Scope()
                    self.scope.parent = self
                    self._children_name_map["scope"] = "scope"
                    self._segment_path = lambda: "message"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Install.RequestStatuses.RequestStatus.Message, ['category', 'message'], name, value)


                class Scope(_Entity_):
                    """
                    Scope of the message
                    
                    .. attribute:: admin_read
                    
                    	Does the admin want to read this?
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: affected_sd_rs
                    
                    	Which LRs are affected by the message
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'installmgr-admin-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Install.RequestStatuses.RequestStatus.Message.Scope, self).__init__()

                        self.yang_name = "scope"
                        self.yang_parent_name = "message"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('admin_read', (YLeaf(YType.boolean, 'admin-read'), ['bool'])),
                            ('affected_sd_rs', (YLeaf(YType.uint32, 'affected-sd-rs'), ['int'])),
                        ])
                        self.admin_read = None
                        self.affected_sd_rs = None
                        self._segment_path = lambda: "scope"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Install.RequestStatuses.RequestStatus.Message.Scope, ['admin_read', 'affected_sd_rs'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                        return meta._meta_table['Install.RequestStatuses.RequestStatus.Message.Scope']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                    return meta._meta_table['Install.RequestStatuses.RequestStatus.Message']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                return meta._meta_table['Install.RequestStatuses.RequestStatus']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
            return meta._meta_table['Install.RequestStatuses']['meta_info']


    class BootVariables(_Entity_):
        """
        Boot variable information
        
        .. attribute:: boot_variable
        
        	Boot variable for specific node
        	**type**\: list of  		 :py:class:`BootVariable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.BootVariables.BootVariable>`
        
        	**config**\: False
        
        

        """

        _prefix = 'installmgr-admin-oper'
        _revision = '2015-11-09'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Install.BootVariables, self).__init__()

            self.yang_name = "boot-variables"
            self.yang_parent_name = "install"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("boot-variable", ("boot_variable", Install.BootVariables.BootVariable))])
            self._leafs = OrderedDict()

            self.boot_variable = YList(self)
            self._segment_path = lambda: "boot-variables"
            self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Install.BootVariables, [], name, value)


        class BootVariable(_Entity_):
            """
            Boot variable for specific node
            
            .. attribute:: node_name  (key)
            
            	Node name
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            	**config**\: False
            
            .. attribute:: boot_variable
            
            	Boot variable value
            	**type**\: str
            
            	**mandatory**\: True
            
            	**config**\: False
            
            

            """

            _prefix = 'installmgr-admin-oper'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Install.BootVariables.BootVariable, self).__init__()

                self.yang_name = "boot-variable"
                self.yang_parent_name = "boot-variables"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_name']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                    ('boot_variable', (YLeaf(YType.str, 'boot-variable'), ['str'])),
                ])
                self.node_name = None
                self.boot_variable = None
                self._segment_path = lambda: "boot-variable" + "[node-name='" + str(self.node_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/boot-variables/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Install.BootVariables.BootVariable, ['node_name', 'boot_variable'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                return meta._meta_table['Install.BootVariables.BootVariable']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
            return meta._meta_table['Install.BootVariables']['meta_info']


    class Software(_Entity_):
        """
        Software package,component and alias information
        
        .. attribute:: alias_devices
        
        	Package alias information
        	**type**\:  :py:class:`AliasDevices <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Software.AliasDevices>`
        
        	**config**\: False
        
        .. attribute:: package_devices
        
        	Package information
        	**type**\:  :py:class:`PackageDevices <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Software.PackageDevices>`
        
        	**config**\: False
        
        .. attribute:: component_devices
        
        	Software component information
        	**type**\:  :py:class:`ComponentDevices <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Software.ComponentDevices>`
        
        	**config**\: False
        
        

        """

        _prefix = 'installmgr-admin-oper'
        _revision = '2015-11-09'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Install.Software, self).__init__()

            self.yang_name = "software"
            self.yang_parent_name = "install"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("alias-devices", ("alias_devices", Install.Software.AliasDevices)), ("package-devices", ("package_devices", Install.Software.PackageDevices)), ("component-devices", ("component_devices", Install.Software.ComponentDevices))])
            self._leafs = OrderedDict()

            self.alias_devices = Install.Software.AliasDevices()
            self.alias_devices.parent = self
            self._children_name_map["alias_devices"] = "alias-devices"

            self.package_devices = Install.Software.PackageDevices()
            self.package_devices.parent = self
            self._children_name_map["package_devices"] = "package-devices"

            self.component_devices = Install.Software.ComponentDevices()
            self.component_devices.parent = self
            self._children_name_map["component_devices"] = "component-devices"
            self._segment_path = lambda: "software"
            self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Install.Software, [], name, value)


        class AliasDevices(_Entity_):
            """
            Package alias information
            
            .. attribute:: alias_device
            
            	Package alias information for specific device
            	**type**\: list of  		 :py:class:`AliasDevice <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Software.AliasDevices.AliasDevice>`
            
            	**config**\: False
            
            

            """

            _prefix = 'installmgr-admin-oper'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Install.Software.AliasDevices, self).__init__()

                self.yang_name = "alias-devices"
                self.yang_parent_name = "software"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("alias-device", ("alias_device", Install.Software.AliasDevices.AliasDevice))])
                self._leafs = OrderedDict()

                self.alias_device = YList(self)
                self._segment_path = lambda: "alias-devices"
                self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/software/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Install.Software.AliasDevices, [], name, value)


            class AliasDevice(_Entity_):
                """
                Package alias information for specific device
                
                .. attribute:: device_name  (key)
                
                	Device Name
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                	**config**\: False
                
                .. attribute:: aliases
                
                	alias information
                	**type**\:  :py:class:`Aliases <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Software.AliasDevices.AliasDevice.Aliases>`
                
                	**config**\: False
                
                

                """

                _prefix = 'installmgr-admin-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Install.Software.AliasDevices.AliasDevice, self).__init__()

                    self.yang_name = "alias-device"
                    self.yang_parent_name = "alias-devices"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['device_name']
                    self._child_classes = OrderedDict([("aliases", ("aliases", Install.Software.AliasDevices.AliasDevice.Aliases))])
                    self._leafs = OrderedDict([
                        ('device_name', (YLeaf(YType.str, 'device-name'), ['str'])),
                    ])
                    self.device_name = None

                    self.aliases = Install.Software.AliasDevices.AliasDevice.Aliases()
                    self.aliases.parent = self
                    self._children_name_map["aliases"] = "aliases"
                    self._segment_path = lambda: "alias-device" + "[device-name='" + str(self.device_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/software/alias-devices/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Install.Software.AliasDevices.AliasDevice, ['device_name'], name, value)


                class Aliases(_Entity_):
                    """
                    alias information
                    
                    .. attribute:: alias
                    
                    	Aliases for specific package
                    	**type**\: list of  		 :py:class:`Alias <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Software.AliasDevices.AliasDevice.Aliases.Alias>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'installmgr-admin-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Install.Software.AliasDevices.AliasDevice.Aliases, self).__init__()

                        self.yang_name = "aliases"
                        self.yang_parent_name = "alias-device"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("alias", ("alias", Install.Software.AliasDevices.AliasDevice.Aliases.Alias))])
                        self._leafs = OrderedDict()

                        self.alias = YList(self)
                        self._segment_path = lambda: "aliases"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Install.Software.AliasDevices.AliasDevice.Aliases, [], name, value)


                    class Alias(_Entity_):
                        """
                        Aliases for specific package
                        
                        .. attribute:: package_name  (key)
                        
                        	Package Name
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: alias_names
                        
                        	Alias names
                        	**type**\: str
                        
                        	**mandatory**\: True
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'installmgr-admin-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Install.Software.AliasDevices.AliasDevice.Aliases.Alias, self).__init__()

                            self.yang_name = "alias"
                            self.yang_parent_name = "aliases"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['package_name']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('package_name', (YLeaf(YType.str, 'package-name'), ['str'])),
                                ('alias_names', (YLeaf(YType.str, 'alias-names'), ['str'])),
                            ])
                            self.package_name = None
                            self.alias_names = None
                            self._segment_path = lambda: "alias" + "[package-name='" + str(self.package_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Install.Software.AliasDevices.AliasDevice.Aliases.Alias, ['package_name', 'alias_names'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                            return meta._meta_table['Install.Software.AliasDevices.AliasDevice.Aliases.Alias']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                        return meta._meta_table['Install.Software.AliasDevices.AliasDevice.Aliases']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                    return meta._meta_table['Install.Software.AliasDevices.AliasDevice']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                return meta._meta_table['Install.Software.AliasDevices']['meta_info']


        class PackageDevices(_Entity_):
            """
            Package information
            
            .. attribute:: package_device
            
            	Package information for specific device
            	**type**\: list of  		 :py:class:`PackageDevice <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Software.PackageDevices.PackageDevice>`
            
            	**config**\: False
            
            

            """

            _prefix = 'installmgr-admin-oper'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Install.Software.PackageDevices, self).__init__()

                self.yang_name = "package-devices"
                self.yang_parent_name = "software"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("package-device", ("package_device", Install.Software.PackageDevices.PackageDevice))])
                self._leafs = OrderedDict()

                self.package_device = YList(self)
                self._segment_path = lambda: "package-devices"
                self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/software/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Install.Software.PackageDevices, [], name, value)


            class PackageDevice(_Entity_):
                """
                Package information for specific device
                
                .. attribute:: device_name  (key)
                
                	Device Name
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                	**config**\: False
                
                .. attribute:: packages
                
                	Package information for specific package
                	**type**\:  :py:class:`Packages <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Software.PackageDevices.PackageDevice.Packages>`
                
                	**config**\: False
                
                

                """

                _prefix = 'installmgr-admin-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Install.Software.PackageDevices.PackageDevice, self).__init__()

                    self.yang_name = "package-device"
                    self.yang_parent_name = "package-devices"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['device_name']
                    self._child_classes = OrderedDict([("packages", ("packages", Install.Software.PackageDevices.PackageDevice.Packages))])
                    self._leafs = OrderedDict([
                        ('device_name', (YLeaf(YType.str, 'device-name'), ['str'])),
                    ])
                    self.device_name = None

                    self.packages = Install.Software.PackageDevices.PackageDevice.Packages()
                    self.packages.parent = self
                    self._children_name_map["packages"] = "packages"
                    self._segment_path = lambda: "package-device" + "[device-name='" + str(self.device_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/software/package-devices/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Install.Software.PackageDevices.PackageDevice, ['device_name'], name, value)


                class Packages(_Entity_):
                    """
                    Package information for specific package
                    
                    .. attribute:: package
                    
                    	Package information
                    	**type**\: list of  		 :py:class:`Package <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Software.PackageDevices.PackageDevice.Packages.Package>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'installmgr-admin-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Install.Software.PackageDevices.PackageDevice.Packages, self).__init__()

                        self.yang_name = "packages"
                        self.yang_parent_name = "package-device"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("package", ("package", Install.Software.PackageDevices.PackageDevice.Packages.Package))])
                        self._leafs = OrderedDict()

                        self.package = YList(self)
                        self._segment_path = lambda: "packages"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Install.Software.PackageDevices.PackageDevice.Packages, [], name, value)


                    class Package(_Entity_):
                        """
                        Package information
                        
                        .. attribute:: package_name  (key)
                        
                        	Package Name
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: name
                        
                        	Name of the package
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: version
                        
                        	Version of the package
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: description
                        
                        	Description of the package
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: release
                        
                        	Release that the package belongs to
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: vendor
                        
                        	Information about the vendor that supplied the package
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: date
                        
                        	Time and date that the package was built
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: source
                        
                        	Identifies the provider of the package
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: base
                        
                        	Identifies the base bundle that the package is for
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: bootable
                        
                        	TRUE if package has BOOTIMAGE tag set
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: composite
                        
                        	TRUE if package is a composite package
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: restart_info
                        
                        	Restart info of the package
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: package_type
                        
                        	Type of the package
                        	**type**\:  :py:class:`InstmgrPkg <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.InstmgrPkg>`
                        
                        	**config**\: False
                        
                        .. attribute:: group_type
                        
                        	Group type of the package
                        	**type**\:  :py:class:`InstmgrGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.InstmgrGroup>`
                        
                        	**config**\: False
                        
                        .. attribute:: depth
                        
                        	Number of layers of parent packages
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: uncompressed_size
                        
                        	Uncompressed size of package
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: compressed_size
                        
                        	Compressed size of package
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: cards
                        
                        	Card types that the package should be installed on
                        	**type**\: list of str
                        
                        	**config**\: False
                        
                        .. attribute:: sub_pkg
                        
                        	Sub\-package info of the package
                        	**type**\: list of  		 :py:class:`SubPkg <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Software.PackageDevices.PackageDevice.Packages.Package.SubPkg>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'installmgr-admin-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Install.Software.PackageDevices.PackageDevice.Packages.Package, self).__init__()

                            self.yang_name = "package"
                            self.yang_parent_name = "packages"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['package_name']
                            self._child_classes = OrderedDict([("sub-pkg", ("sub_pkg", Install.Software.PackageDevices.PackageDevice.Packages.Package.SubPkg))])
                            self._leafs = OrderedDict([
                                ('package_name', (YLeaf(YType.str, 'package-name'), ['str'])),
                                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                ('version', (YLeaf(YType.str, 'version'), ['str'])),
                                ('description', (YLeaf(YType.str, 'description'), ['str'])),
                                ('release', (YLeaf(YType.str, 'release'), ['str'])),
                                ('vendor', (YLeaf(YType.str, 'vendor'), ['str'])),
                                ('date', (YLeaf(YType.str, 'date'), ['str'])),
                                ('source', (YLeaf(YType.str, 'source'), ['str'])),
                                ('base', (YLeaf(YType.str, 'base'), ['str'])),
                                ('bootable', (YLeaf(YType.boolean, 'bootable'), ['bool'])),
                                ('composite', (YLeaf(YType.boolean, 'composite'), ['bool'])),
                                ('restart_info', (YLeaf(YType.str, 'restart-info'), ['str'])),
                                ('package_type', (YLeaf(YType.enumeration, 'package-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'InstmgrPkg', '')])),
                                ('group_type', (YLeaf(YType.enumeration, 'group-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'InstmgrGroup', '')])),
                                ('depth', (YLeaf(YType.uint32, 'depth'), ['int'])),
                                ('uncompressed_size', (YLeaf(YType.uint32, 'uncompressed-size'), ['int'])),
                                ('compressed_size', (YLeaf(YType.uint32, 'compressed-size'), ['int'])),
                                ('cards', (YLeafList(YType.str, 'cards'), ['str'])),
                            ])
                            self.package_name = None
                            self.name = None
                            self.version = None
                            self.description = None
                            self.release = None
                            self.vendor = None
                            self.date = None
                            self.source = None
                            self.base = None
                            self.bootable = None
                            self.composite = None
                            self.restart_info = None
                            self.package_type = None
                            self.group_type = None
                            self.depth = None
                            self.uncompressed_size = None
                            self.compressed_size = None
                            self.cards = []

                            self.sub_pkg = YList(self)
                            self._segment_path = lambda: "package" + "[package-name='" + str(self.package_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Install.Software.PackageDevices.PackageDevice.Packages.Package, ['package_name', 'name', 'version', 'description', 'release', 'vendor', 'date', 'source', 'base', 'bootable', 'composite', 'restart_info', 'package_type', 'group_type', 'depth', 'uncompressed_size', 'compressed_size', 'cards'], name, value)


                        class SubPkg(_Entity_):
                            """
                            Sub\-package info of the package
                            
                            .. attribute:: name
                            
                            	Name of the sub\-package
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: node_types
                            
                            	Node types of the package
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'installmgr-admin-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Install.Software.PackageDevices.PackageDevice.Packages.Package.SubPkg, self).__init__()

                                self.yang_name = "sub-pkg"
                                self.yang_parent_name = "package"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                    ('node_types', (YLeaf(YType.uint64, 'node-types'), ['int'])),
                                ])
                                self.name = None
                                self.node_types = None
                                self._segment_path = lambda: "sub-pkg"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Install.Software.PackageDevices.PackageDevice.Packages.Package.SubPkg, ['name', 'node_types'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                                return meta._meta_table['Install.Software.PackageDevices.PackageDevice.Packages.Package.SubPkg']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                            return meta._meta_table['Install.Software.PackageDevices.PackageDevice.Packages.Package']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                        return meta._meta_table['Install.Software.PackageDevices.PackageDevice.Packages']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                    return meta._meta_table['Install.Software.PackageDevices.PackageDevice']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                return meta._meta_table['Install.Software.PackageDevices']['meta_info']


        class ComponentDevices(_Entity_):
            """
            Software component information
            
            .. attribute:: component_device
            
            	Component information for specific device
            	**type**\: list of  		 :py:class:`ComponentDevice <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Software.ComponentDevices.ComponentDevice>`
            
            	**config**\: False
            
            

            """

            _prefix = 'installmgr-admin-oper'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Install.Software.ComponentDevices, self).__init__()

                self.yang_name = "component-devices"
                self.yang_parent_name = "software"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("component-device", ("component_device", Install.Software.ComponentDevices.ComponentDevice))])
                self._leafs = OrderedDict()

                self.component_device = YList(self)
                self._segment_path = lambda: "component-devices"
                self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/software/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Install.Software.ComponentDevices, [], name, value)


            class ComponentDevice(_Entity_):
                """
                Component information for specific device
                
                .. attribute:: device_name  (key)
                
                	Device Name
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                	**config**\: False
                
                .. attribute:: component_packages
                
                	Software package information
                	**type**\:  :py:class:`ComponentPackages <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Software.ComponentDevices.ComponentDevice.ComponentPackages>`
                
                	**config**\: False
                
                

                """

                _prefix = 'installmgr-admin-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Install.Software.ComponentDevices.ComponentDevice, self).__init__()

                    self.yang_name = "component-device"
                    self.yang_parent_name = "component-devices"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['device_name']
                    self._child_classes = OrderedDict([("component-packages", ("component_packages", Install.Software.ComponentDevices.ComponentDevice.ComponentPackages))])
                    self._leafs = OrderedDict([
                        ('device_name', (YLeaf(YType.str, 'device-name'), ['str'])),
                    ])
                    self.device_name = None

                    self.component_packages = Install.Software.ComponentDevices.ComponentDevice.ComponentPackages()
                    self.component_packages.parent = self
                    self._children_name_map["component_packages"] = "component-packages"
                    self._segment_path = lambda: "component-device" + "[device-name='" + str(self.device_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/software/component-devices/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Install.Software.ComponentDevices.ComponentDevice, ['device_name'], name, value)


                class ComponentPackages(_Entity_):
                    """
                    Software package information
                    
                    .. attribute:: component_package
                    
                    	Component information for specific package
                    	**type**\: list of  		 :py:class:`ComponentPackage <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Software.ComponentDevices.ComponentDevice.ComponentPackages.ComponentPackage>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'installmgr-admin-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Install.Software.ComponentDevices.ComponentDevice.ComponentPackages, self).__init__()

                        self.yang_name = "component-packages"
                        self.yang_parent_name = "component-device"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("component-package", ("component_package", Install.Software.ComponentDevices.ComponentDevice.ComponentPackages.ComponentPackage))])
                        self._leafs = OrderedDict()

                        self.component_package = YList(self)
                        self._segment_path = lambda: "component-packages"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Install.Software.ComponentDevices.ComponentDevice.ComponentPackages, [], name, value)


                    class ComponentPackage(_Entity_):
                        """
                        Component information for specific package
                        
                        .. attribute:: package_name  (key)
                        
                        	Package Name
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: component
                        
                        	Component information
                        	**type**\: list of  		 :py:class:`Component <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Software.ComponentDevices.ComponentDevice.ComponentPackages.ComponentPackage.Component>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'installmgr-admin-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Install.Software.ComponentDevices.ComponentDevice.ComponentPackages.ComponentPackage, self).__init__()

                            self.yang_name = "component-package"
                            self.yang_parent_name = "component-packages"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['package_name']
                            self._child_classes = OrderedDict([("component", ("component", Install.Software.ComponentDevices.ComponentDevice.ComponentPackages.ComponentPackage.Component))])
                            self._leafs = OrderedDict([
                                ('package_name', (YLeaf(YType.str, 'package-name'), ['str'])),
                            ])
                            self.package_name = None

                            self.component = YList(self)
                            self._segment_path = lambda: "component-package" + "[package-name='" + str(self.package_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Install.Software.ComponentDevices.ComponentDevice.ComponentPackages.ComponentPackage, ['package_name'], name, value)


                        class Component(_Entity_):
                            """
                            Component information
                            
                            .. attribute:: component_name  (key)
                            
                            	Component Name
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: name
                            
                            	Name of the component
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: version
                            
                            	Version of the component
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: release
                            
                            	Release that the component belongs to
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: description
                            
                            	Description of the component
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: files
                            
                            	The set of files belonging to the component
                            	**type**\: list of str
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'installmgr-admin-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Install.Software.ComponentDevices.ComponentDevice.ComponentPackages.ComponentPackage.Component, self).__init__()

                                self.yang_name = "component"
                                self.yang_parent_name = "component-package"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['component_name']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('component_name', (YLeaf(YType.str, 'component-name'), ['str'])),
                                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                    ('version', (YLeaf(YType.str, 'version'), ['str'])),
                                    ('release', (YLeaf(YType.str, 'release'), ['str'])),
                                    ('description', (YLeaf(YType.str, 'description'), ['str'])),
                                    ('files', (YLeafList(YType.str, 'files'), ['str'])),
                                ])
                                self.component_name = None
                                self.name = None
                                self.version = None
                                self.release = None
                                self.description = None
                                self.files = []
                                self._segment_path = lambda: "component" + "[component-name='" + str(self.component_name) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Install.Software.ComponentDevices.ComponentDevice.ComponentPackages.ComponentPackage.Component, ['component_name', 'name', 'version', 'release', 'description', 'files'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                                return meta._meta_table['Install.Software.ComponentDevices.ComponentDevice.ComponentPackages.ComponentPackage.Component']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                            return meta._meta_table['Install.Software.ComponentDevices.ComponentDevice.ComponentPackages.ComponentPackage']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                        return meta._meta_table['Install.Software.ComponentDevices.ComponentDevice.ComponentPackages']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                    return meta._meta_table['Install.Software.ComponentDevices.ComponentDevice']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                return meta._meta_table['Install.Software.ComponentDevices']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
            return meta._meta_table['Install.Software']['meta_info']


    class SoftwareInventory(_Entity_):
        """
        Information of install operations
        
        .. attribute:: committed
        
        	Committed inventory information
        	**type**\:  :py:class:`Committed <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Committed>`
        
        	**config**\: False
        
        .. attribute:: inactive
        
        	Inactive inventory information
        	**type**\:  :py:class:`Inactive <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Inactive>`
        
        	**config**\: False
        
        .. attribute:: requests
        
        	Install operation requests
        	**type**\:  :py:class:`Requests <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Requests>`
        
        	**config**\: False
        
        .. attribute:: active
        
        	Active inventory information
        	**type**\:  :py:class:`Active <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Active>`
        
        	**config**\: False
        
        

        """

        _prefix = 'installmgr-admin-oper'
        _revision = '2015-11-09'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Install.SoftwareInventory, self).__init__()

            self.yang_name = "software-inventory"
            self.yang_parent_name = "install"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("committed", ("committed", Install.SoftwareInventory.Committed)), ("inactive", ("inactive", Install.SoftwareInventory.Inactive)), ("requests", ("requests", Install.SoftwareInventory.Requests)), ("active", ("active", Install.SoftwareInventory.Active))])
            self._leafs = OrderedDict()

            self.committed = Install.SoftwareInventory.Committed()
            self.committed.parent = self
            self._children_name_map["committed"] = "committed"

            self.inactive = Install.SoftwareInventory.Inactive()
            self.inactive.parent = self
            self._children_name_map["inactive"] = "inactive"

            self.requests = Install.SoftwareInventory.Requests()
            self.requests.parent = self
            self._children_name_map["requests"] = "requests"

            self.active = Install.SoftwareInventory.Active()
            self.active.parent = self
            self._children_name_map["active"] = "active"
            self._segment_path = lambda: "software-inventory"
            self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Install.SoftwareInventory, [], name, value)


        class Committed(_Entity_):
            """
            Committed inventory information
            
            .. attribute:: summary
            
            	Summarized inventory information
            	**type**\:  :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Committed.Summary>`
            
            	**config**\: False
            
            .. attribute:: inventories
            
            	Software inventory
            	**type**\:  :py:class:`Inventories <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Committed.Inventories>`
            
            	**config**\: False
            
            

            """

            _prefix = 'installmgr-admin-oper'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Install.SoftwareInventory.Committed, self).__init__()

                self.yang_name = "committed"
                self.yang_parent_name = "software-inventory"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("summary", ("summary", Install.SoftwareInventory.Committed.Summary)), ("inventories", ("inventories", Install.SoftwareInventory.Committed.Inventories))])
                self._leafs = OrderedDict()

                self.summary = Install.SoftwareInventory.Committed.Summary()
                self.summary.parent = self
                self._children_name_map["summary"] = "summary"

                self.inventories = Install.SoftwareInventory.Committed.Inventories()
                self.inventories.parent = self
                self._children_name_map["inventories"] = "inventories"
                self._segment_path = lambda: "committed"
                self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/software-inventory/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Install.SoftwareInventory.Committed, [], name, value)


            class Summary(_Entity_):
                """
                Summarized inventory information
                
                .. attribute:: default_load_path
                
                	Default load path
                	**type**\:  :py:class:`DefaultLoadPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Committed.Summary.DefaultLoadPath>`
                
                	**config**\: False
                
                .. attribute:: admin_load_path
                
                	Admin Resources load path
                	**type**\:  :py:class:`AdminLoadPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Committed.Summary.AdminLoadPath>`
                
                	**config**\: False
                
                .. attribute:: sdr_load_path
                
                	SDR load paths
                	**type**\: list of  		 :py:class:`SdrLoadPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Committed.Summary.SdrLoadPath>`
                
                	**config**\: False
                
                .. attribute:: location_load_path
                
                	Location load paths
                	**type**\: list of  		 :py:class:`LocationLoadPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Committed.Summary.LocationLoadPath>`
                
                	**config**\: False
                
                

                """

                _prefix = 'installmgr-admin-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Install.SoftwareInventory.Committed.Summary, self).__init__()

                    self.yang_name = "summary"
                    self.yang_parent_name = "committed"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("default-load-path", ("default_load_path", Install.SoftwareInventory.Committed.Summary.DefaultLoadPath)), ("admin-load-path", ("admin_load_path", Install.SoftwareInventory.Committed.Summary.AdminLoadPath)), ("sdr-load-path", ("sdr_load_path", Install.SoftwareInventory.Committed.Summary.SdrLoadPath)), ("location-load-path", ("location_load_path", Install.SoftwareInventory.Committed.Summary.LocationLoadPath))])
                    self._leafs = OrderedDict()

                    self.default_load_path = Install.SoftwareInventory.Committed.Summary.DefaultLoadPath()
                    self.default_load_path.parent = self
                    self._children_name_map["default_load_path"] = "default-load-path"

                    self.admin_load_path = Install.SoftwareInventory.Committed.Summary.AdminLoadPath()
                    self.admin_load_path.parent = self
                    self._children_name_map["admin_load_path"] = "admin-load-path"

                    self.sdr_load_path = YList(self)
                    self.location_load_path = YList(self)
                    self._segment_path = lambda: "summary"
                    self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/software-inventory/committed/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Install.SoftwareInventory.Committed.Summary, [], name, value)


                class DefaultLoadPath(_Entity_):
                    """
                    Default load path
                    
                    .. attribute:: request_id
                    
                    	Install op affecting scope
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: admin_match
                    
                    	Does this match the Admin Resources load path?
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: secure_domain_router_name
                    
                    	Names of SDRs this applies to
                    	**type**\: list of str
                    
                    	**config**\: False
                    
                    .. attribute:: load_path
                    
                    	Default load path
                    	**type**\: list of  		 :py:class:`LoadPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Committed.Summary.DefaultLoadPath.LoadPath>`
                    
                    	**config**\: False
                    
                    .. attribute:: standby_load_path
                    
                    	Load paths for standby nodes
                    	**type**\: list of  		 :py:class:`StandbyLoadPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Committed.Summary.DefaultLoadPath.StandbyLoadPath>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'installmgr-admin-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Install.SoftwareInventory.Committed.Summary.DefaultLoadPath, self).__init__()

                        self.yang_name = "default-load-path"
                        self.yang_parent_name = "summary"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("load-path", ("load_path", Install.SoftwareInventory.Committed.Summary.DefaultLoadPath.LoadPath)), ("standby-load-path", ("standby_load_path", Install.SoftwareInventory.Committed.Summary.DefaultLoadPath.StandbyLoadPath))])
                        self._leafs = OrderedDict([
                            ('request_id', (YLeaf(YType.uint32, 'request-id'), ['int'])),
                            ('admin_match', (YLeaf(YType.boolean, 'admin-match'), ['bool'])),
                            ('secure_domain_router_name', (YLeafList(YType.str, 'secure-domain-router-name'), ['str'])),
                        ])
                        self.request_id = None
                        self.admin_match = None
                        self.secure_domain_router_name = []

                        self.load_path = YList(self)
                        self.standby_load_path = YList(self)
                        self._segment_path = lambda: "default-load-path"
                        self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/software-inventory/committed/summary/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Install.SoftwareInventory.Committed.Summary.DefaultLoadPath, ['request_id', 'admin_match', 'secure_domain_router_name'], name, value)


                    class LoadPath(_Entity_):
                        """
                        Default load path
                        
                        .. attribute:: package
                        
                        	Package
                        	**type**\:  :py:class:`Package <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Committed.Summary.DefaultLoadPath.LoadPath.Package>`
                        
                        	**config**\: False
                        
                        .. attribute:: version
                        
                        	Version
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: build_information
                        
                        	Build information
                        	**type**\: str
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'installmgr-admin-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Install.SoftwareInventory.Committed.Summary.DefaultLoadPath.LoadPath, self).__init__()

                            self.yang_name = "load-path"
                            self.yang_parent_name = "default-load-path"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("package", ("package", Install.SoftwareInventory.Committed.Summary.DefaultLoadPath.LoadPath.Package))])
                            self._leafs = OrderedDict([
                                ('version', (YLeaf(YType.str, 'version'), ['str'])),
                                ('build_information', (YLeaf(YType.str, 'build-information'), ['str'])),
                            ])
                            self.version = None
                            self.build_information = None

                            self.package = Install.SoftwareInventory.Committed.Summary.DefaultLoadPath.LoadPath.Package()
                            self.package.parent = self
                            self._children_name_map["package"] = "package"
                            self._segment_path = lambda: "load-path"
                            self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/software-inventory/committed/summary/default-load-path/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Install.SoftwareInventory.Committed.Summary.DefaultLoadPath.LoadPath, ['version', 'build_information'], name, value)


                        class Package(_Entity_):
                            """
                            Package
                            
                            .. attribute:: device_name
                            
                            	Device name
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: name
                            
                            	Package group name
                            	**type**\: str
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'installmgr-admin-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Install.SoftwareInventory.Committed.Summary.DefaultLoadPath.LoadPath.Package, self).__init__()

                                self.yang_name = "package"
                                self.yang_parent_name = "load-path"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('device_name', (YLeaf(YType.str, 'device-name'), ['str'])),
                                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                ])
                                self.device_name = None
                                self.name = None
                                self._segment_path = lambda: "package"
                                self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/software-inventory/committed/summary/default-load-path/load-path/%s" % self._segment_path()
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Install.SoftwareInventory.Committed.Summary.DefaultLoadPath.LoadPath.Package, ['device_name', 'name'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                                return meta._meta_table['Install.SoftwareInventory.Committed.Summary.DefaultLoadPath.LoadPath.Package']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                            return meta._meta_table['Install.SoftwareInventory.Committed.Summary.DefaultLoadPath.LoadPath']['meta_info']


                    class StandbyLoadPath(_Entity_):
                        """
                        Load paths for standby nodes
                        
                        .. attribute:: package
                        
                        	Package
                        	**type**\:  :py:class:`Package <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Committed.Summary.DefaultLoadPath.StandbyLoadPath.Package>`
                        
                        	**config**\: False
                        
                        .. attribute:: version
                        
                        	Version
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: build_information
                        
                        	Build information
                        	**type**\: str
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'installmgr-admin-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Install.SoftwareInventory.Committed.Summary.DefaultLoadPath.StandbyLoadPath, self).__init__()

                            self.yang_name = "standby-load-path"
                            self.yang_parent_name = "default-load-path"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("package", ("package", Install.SoftwareInventory.Committed.Summary.DefaultLoadPath.StandbyLoadPath.Package))])
                            self._leafs = OrderedDict([
                                ('version', (YLeaf(YType.str, 'version'), ['str'])),
                                ('build_information', (YLeaf(YType.str, 'build-information'), ['str'])),
                            ])
                            self.version = None
                            self.build_information = None

                            self.package = Install.SoftwareInventory.Committed.Summary.DefaultLoadPath.StandbyLoadPath.Package()
                            self.package.parent = self
                            self._children_name_map["package"] = "package"
                            self._segment_path = lambda: "standby-load-path"
                            self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/software-inventory/committed/summary/default-load-path/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Install.SoftwareInventory.Committed.Summary.DefaultLoadPath.StandbyLoadPath, ['version', 'build_information'], name, value)


                        class Package(_Entity_):
                            """
                            Package
                            
                            .. attribute:: device_name
                            
                            	Device name
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: name
                            
                            	Package group name
                            	**type**\: str
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'installmgr-admin-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Install.SoftwareInventory.Committed.Summary.DefaultLoadPath.StandbyLoadPath.Package, self).__init__()

                                self.yang_name = "package"
                                self.yang_parent_name = "standby-load-path"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('device_name', (YLeaf(YType.str, 'device-name'), ['str'])),
                                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                ])
                                self.device_name = None
                                self.name = None
                                self._segment_path = lambda: "package"
                                self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/software-inventory/committed/summary/default-load-path/standby-load-path/%s" % self._segment_path()
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Install.SoftwareInventory.Committed.Summary.DefaultLoadPath.StandbyLoadPath.Package, ['device_name', 'name'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                                return meta._meta_table['Install.SoftwareInventory.Committed.Summary.DefaultLoadPath.StandbyLoadPath.Package']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                            return meta._meta_table['Install.SoftwareInventory.Committed.Summary.DefaultLoadPath.StandbyLoadPath']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                        return meta._meta_table['Install.SoftwareInventory.Committed.Summary.DefaultLoadPath']['meta_info']


                class AdminLoadPath(_Entity_):
                    """
                    Admin Resources load path
                    
                    .. attribute:: request_id
                    
                    	Install op affecting scope
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: load_path
                    
                    	Admin Resources load path
                    	**type**\: list of  		 :py:class:`LoadPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Committed.Summary.AdminLoadPath.LoadPath>`
                    
                    	**config**\: False
                    
                    .. attribute:: standby_load_path
                    
                    	Load paths for standby nodes
                    	**type**\: list of  		 :py:class:`StandbyLoadPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Committed.Summary.AdminLoadPath.StandbyLoadPath>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'installmgr-admin-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Install.SoftwareInventory.Committed.Summary.AdminLoadPath, self).__init__()

                        self.yang_name = "admin-load-path"
                        self.yang_parent_name = "summary"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("load-path", ("load_path", Install.SoftwareInventory.Committed.Summary.AdminLoadPath.LoadPath)), ("standby-load-path", ("standby_load_path", Install.SoftwareInventory.Committed.Summary.AdminLoadPath.StandbyLoadPath))])
                        self._leafs = OrderedDict([
                            ('request_id', (YLeaf(YType.uint32, 'request-id'), ['int'])),
                        ])
                        self.request_id = None

                        self.load_path = YList(self)
                        self.standby_load_path = YList(self)
                        self._segment_path = lambda: "admin-load-path"
                        self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/software-inventory/committed/summary/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Install.SoftwareInventory.Committed.Summary.AdminLoadPath, ['request_id'], name, value)


                    class LoadPath(_Entity_):
                        """
                        Admin Resources load path
                        
                        .. attribute:: package
                        
                        	Package
                        	**type**\:  :py:class:`Package <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Committed.Summary.AdminLoadPath.LoadPath.Package>`
                        
                        	**config**\: False
                        
                        .. attribute:: version
                        
                        	Version
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: build_information
                        
                        	Build information
                        	**type**\: str
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'installmgr-admin-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Install.SoftwareInventory.Committed.Summary.AdminLoadPath.LoadPath, self).__init__()

                            self.yang_name = "load-path"
                            self.yang_parent_name = "admin-load-path"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("package", ("package", Install.SoftwareInventory.Committed.Summary.AdminLoadPath.LoadPath.Package))])
                            self._leafs = OrderedDict([
                                ('version', (YLeaf(YType.str, 'version'), ['str'])),
                                ('build_information', (YLeaf(YType.str, 'build-information'), ['str'])),
                            ])
                            self.version = None
                            self.build_information = None

                            self.package = Install.SoftwareInventory.Committed.Summary.AdminLoadPath.LoadPath.Package()
                            self.package.parent = self
                            self._children_name_map["package"] = "package"
                            self._segment_path = lambda: "load-path"
                            self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/software-inventory/committed/summary/admin-load-path/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Install.SoftwareInventory.Committed.Summary.AdminLoadPath.LoadPath, ['version', 'build_information'], name, value)


                        class Package(_Entity_):
                            """
                            Package
                            
                            .. attribute:: device_name
                            
                            	Device name
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: name
                            
                            	Package group name
                            	**type**\: str
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'installmgr-admin-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Install.SoftwareInventory.Committed.Summary.AdminLoadPath.LoadPath.Package, self).__init__()

                                self.yang_name = "package"
                                self.yang_parent_name = "load-path"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('device_name', (YLeaf(YType.str, 'device-name'), ['str'])),
                                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                ])
                                self.device_name = None
                                self.name = None
                                self._segment_path = lambda: "package"
                                self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/software-inventory/committed/summary/admin-load-path/load-path/%s" % self._segment_path()
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Install.SoftwareInventory.Committed.Summary.AdminLoadPath.LoadPath.Package, ['device_name', 'name'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                                return meta._meta_table['Install.SoftwareInventory.Committed.Summary.AdminLoadPath.LoadPath.Package']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                            return meta._meta_table['Install.SoftwareInventory.Committed.Summary.AdminLoadPath.LoadPath']['meta_info']


                    class StandbyLoadPath(_Entity_):
                        """
                        Load paths for standby nodes
                        
                        .. attribute:: package
                        
                        	Package
                        	**type**\:  :py:class:`Package <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Committed.Summary.AdminLoadPath.StandbyLoadPath.Package>`
                        
                        	**config**\: False
                        
                        .. attribute:: version
                        
                        	Version
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: build_information
                        
                        	Build information
                        	**type**\: str
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'installmgr-admin-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Install.SoftwareInventory.Committed.Summary.AdminLoadPath.StandbyLoadPath, self).__init__()

                            self.yang_name = "standby-load-path"
                            self.yang_parent_name = "admin-load-path"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("package", ("package", Install.SoftwareInventory.Committed.Summary.AdminLoadPath.StandbyLoadPath.Package))])
                            self._leafs = OrderedDict([
                                ('version', (YLeaf(YType.str, 'version'), ['str'])),
                                ('build_information', (YLeaf(YType.str, 'build-information'), ['str'])),
                            ])
                            self.version = None
                            self.build_information = None

                            self.package = Install.SoftwareInventory.Committed.Summary.AdminLoadPath.StandbyLoadPath.Package()
                            self.package.parent = self
                            self._children_name_map["package"] = "package"
                            self._segment_path = lambda: "standby-load-path"
                            self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/software-inventory/committed/summary/admin-load-path/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Install.SoftwareInventory.Committed.Summary.AdminLoadPath.StandbyLoadPath, ['version', 'build_information'], name, value)


                        class Package(_Entity_):
                            """
                            Package
                            
                            .. attribute:: device_name
                            
                            	Device name
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: name
                            
                            	Package group name
                            	**type**\: str
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'installmgr-admin-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Install.SoftwareInventory.Committed.Summary.AdminLoadPath.StandbyLoadPath.Package, self).__init__()

                                self.yang_name = "package"
                                self.yang_parent_name = "standby-load-path"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('device_name', (YLeaf(YType.str, 'device-name'), ['str'])),
                                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                ])
                                self.device_name = None
                                self.name = None
                                self._segment_path = lambda: "package"
                                self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/software-inventory/committed/summary/admin-load-path/standby-load-path/%s" % self._segment_path()
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Install.SoftwareInventory.Committed.Summary.AdminLoadPath.StandbyLoadPath.Package, ['device_name', 'name'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                                return meta._meta_table['Install.SoftwareInventory.Committed.Summary.AdminLoadPath.StandbyLoadPath.Package']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                            return meta._meta_table['Install.SoftwareInventory.Committed.Summary.AdminLoadPath.StandbyLoadPath']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                        return meta._meta_table['Install.SoftwareInventory.Committed.Summary.AdminLoadPath']['meta_info']


                class SdrLoadPath(_Entity_):
                    """
                    SDR load paths
                    
                    .. attribute:: request_id
                    
                    	Install op affecting scope
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: secure_domain_router_name
                    
                    	SDR name
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: load_path
                    
                    	Load path
                    	**type**\: list of  		 :py:class:`LoadPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Committed.Summary.SdrLoadPath.LoadPath>`
                    
                    	**config**\: False
                    
                    .. attribute:: standby_load_path
                    
                    	Load paths for standby nodes
                    	**type**\: list of  		 :py:class:`StandbyLoadPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Committed.Summary.SdrLoadPath.StandbyLoadPath>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'installmgr-admin-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Install.SoftwareInventory.Committed.Summary.SdrLoadPath, self).__init__()

                        self.yang_name = "sdr-load-path"
                        self.yang_parent_name = "summary"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("load-path", ("load_path", Install.SoftwareInventory.Committed.Summary.SdrLoadPath.LoadPath)), ("standby-load-path", ("standby_load_path", Install.SoftwareInventory.Committed.Summary.SdrLoadPath.StandbyLoadPath))])
                        self._leafs = OrderedDict([
                            ('request_id', (YLeaf(YType.uint32, 'request-id'), ['int'])),
                            ('secure_domain_router_name', (YLeaf(YType.str, 'secure-domain-router-name'), ['str'])),
                        ])
                        self.request_id = None
                        self.secure_domain_router_name = None

                        self.load_path = YList(self)
                        self.standby_load_path = YList(self)
                        self._segment_path = lambda: "sdr-load-path"
                        self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/software-inventory/committed/summary/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Install.SoftwareInventory.Committed.Summary.SdrLoadPath, ['request_id', 'secure_domain_router_name'], name, value)


                    class LoadPath(_Entity_):
                        """
                        Load path
                        
                        .. attribute:: package
                        
                        	Package
                        	**type**\:  :py:class:`Package <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Committed.Summary.SdrLoadPath.LoadPath.Package>`
                        
                        	**config**\: False
                        
                        .. attribute:: version
                        
                        	Version
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: build_information
                        
                        	Build information
                        	**type**\: str
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'installmgr-admin-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Install.SoftwareInventory.Committed.Summary.SdrLoadPath.LoadPath, self).__init__()

                            self.yang_name = "load-path"
                            self.yang_parent_name = "sdr-load-path"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("package", ("package", Install.SoftwareInventory.Committed.Summary.SdrLoadPath.LoadPath.Package))])
                            self._leafs = OrderedDict([
                                ('version', (YLeaf(YType.str, 'version'), ['str'])),
                                ('build_information', (YLeaf(YType.str, 'build-information'), ['str'])),
                            ])
                            self.version = None
                            self.build_information = None

                            self.package = Install.SoftwareInventory.Committed.Summary.SdrLoadPath.LoadPath.Package()
                            self.package.parent = self
                            self._children_name_map["package"] = "package"
                            self._segment_path = lambda: "load-path"
                            self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/software-inventory/committed/summary/sdr-load-path/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Install.SoftwareInventory.Committed.Summary.SdrLoadPath.LoadPath, ['version', 'build_information'], name, value)


                        class Package(_Entity_):
                            """
                            Package
                            
                            .. attribute:: device_name
                            
                            	Device name
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: name
                            
                            	Package group name
                            	**type**\: str
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'installmgr-admin-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Install.SoftwareInventory.Committed.Summary.SdrLoadPath.LoadPath.Package, self).__init__()

                                self.yang_name = "package"
                                self.yang_parent_name = "load-path"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('device_name', (YLeaf(YType.str, 'device-name'), ['str'])),
                                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                ])
                                self.device_name = None
                                self.name = None
                                self._segment_path = lambda: "package"
                                self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/software-inventory/committed/summary/sdr-load-path/load-path/%s" % self._segment_path()
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Install.SoftwareInventory.Committed.Summary.SdrLoadPath.LoadPath.Package, ['device_name', 'name'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                                return meta._meta_table['Install.SoftwareInventory.Committed.Summary.SdrLoadPath.LoadPath.Package']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                            return meta._meta_table['Install.SoftwareInventory.Committed.Summary.SdrLoadPath.LoadPath']['meta_info']


                    class StandbyLoadPath(_Entity_):
                        """
                        Load paths for standby nodes
                        
                        .. attribute:: package
                        
                        	Package
                        	**type**\:  :py:class:`Package <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Committed.Summary.SdrLoadPath.StandbyLoadPath.Package>`
                        
                        	**config**\: False
                        
                        .. attribute:: version
                        
                        	Version
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: build_information
                        
                        	Build information
                        	**type**\: str
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'installmgr-admin-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Install.SoftwareInventory.Committed.Summary.SdrLoadPath.StandbyLoadPath, self).__init__()

                            self.yang_name = "standby-load-path"
                            self.yang_parent_name = "sdr-load-path"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("package", ("package", Install.SoftwareInventory.Committed.Summary.SdrLoadPath.StandbyLoadPath.Package))])
                            self._leafs = OrderedDict([
                                ('version', (YLeaf(YType.str, 'version'), ['str'])),
                                ('build_information', (YLeaf(YType.str, 'build-information'), ['str'])),
                            ])
                            self.version = None
                            self.build_information = None

                            self.package = Install.SoftwareInventory.Committed.Summary.SdrLoadPath.StandbyLoadPath.Package()
                            self.package.parent = self
                            self._children_name_map["package"] = "package"
                            self._segment_path = lambda: "standby-load-path"
                            self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/software-inventory/committed/summary/sdr-load-path/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Install.SoftwareInventory.Committed.Summary.SdrLoadPath.StandbyLoadPath, ['version', 'build_information'], name, value)


                        class Package(_Entity_):
                            """
                            Package
                            
                            .. attribute:: device_name
                            
                            	Device name
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: name
                            
                            	Package group name
                            	**type**\: str
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'installmgr-admin-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Install.SoftwareInventory.Committed.Summary.SdrLoadPath.StandbyLoadPath.Package, self).__init__()

                                self.yang_name = "package"
                                self.yang_parent_name = "standby-load-path"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('device_name', (YLeaf(YType.str, 'device-name'), ['str'])),
                                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                ])
                                self.device_name = None
                                self.name = None
                                self._segment_path = lambda: "package"
                                self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/software-inventory/committed/summary/sdr-load-path/standby-load-path/%s" % self._segment_path()
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Install.SoftwareInventory.Committed.Summary.SdrLoadPath.StandbyLoadPath.Package, ['device_name', 'name'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                                return meta._meta_table['Install.SoftwareInventory.Committed.Summary.SdrLoadPath.StandbyLoadPath.Package']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                            return meta._meta_table['Install.SoftwareInventory.Committed.Summary.SdrLoadPath.StandbyLoadPath']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                        return meta._meta_table['Install.SoftwareInventory.Committed.Summary.SdrLoadPath']['meta_info']


                class LocationLoadPath(_Entity_):
                    """
                    Location load paths
                    
                    .. attribute:: request_id
                    
                    	Install op affecting scope
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: secure_domain_router_name
                    
                    	SDR name
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: node_name
                    
                    	Node identifier
                    	**type**\: str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    	**config**\: False
                    
                    .. attribute:: load_path
                    
                    	Load path
                    	**type**\: list of  		 :py:class:`LoadPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Committed.Summary.LocationLoadPath.LoadPath>`
                    
                    	**config**\: False
                    
                    .. attribute:: standby_load_path
                    
                    	Load paths for standby nodes
                    	**type**\: list of  		 :py:class:`StandbyLoadPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Committed.Summary.LocationLoadPath.StandbyLoadPath>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'installmgr-admin-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Install.SoftwareInventory.Committed.Summary.LocationLoadPath, self).__init__()

                        self.yang_name = "location-load-path"
                        self.yang_parent_name = "summary"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("load-path", ("load_path", Install.SoftwareInventory.Committed.Summary.LocationLoadPath.LoadPath)), ("standby-load-path", ("standby_load_path", Install.SoftwareInventory.Committed.Summary.LocationLoadPath.StandbyLoadPath))])
                        self._leafs = OrderedDict([
                            ('request_id', (YLeaf(YType.uint32, 'request-id'), ['int'])),
                            ('secure_domain_router_name', (YLeaf(YType.str, 'secure-domain-router-name'), ['str'])),
                            ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                        ])
                        self.request_id = None
                        self.secure_domain_router_name = None
                        self.node_name = None

                        self.load_path = YList(self)
                        self.standby_load_path = YList(self)
                        self._segment_path = lambda: "location-load-path"
                        self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/software-inventory/committed/summary/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Install.SoftwareInventory.Committed.Summary.LocationLoadPath, ['request_id', 'secure_domain_router_name', 'node_name'], name, value)


                    class LoadPath(_Entity_):
                        """
                        Load path
                        
                        .. attribute:: package
                        
                        	Package
                        	**type**\:  :py:class:`Package <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Committed.Summary.LocationLoadPath.LoadPath.Package>`
                        
                        	**config**\: False
                        
                        .. attribute:: version
                        
                        	Version
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: build_information
                        
                        	Build information
                        	**type**\: str
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'installmgr-admin-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Install.SoftwareInventory.Committed.Summary.LocationLoadPath.LoadPath, self).__init__()

                            self.yang_name = "load-path"
                            self.yang_parent_name = "location-load-path"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("package", ("package", Install.SoftwareInventory.Committed.Summary.LocationLoadPath.LoadPath.Package))])
                            self._leafs = OrderedDict([
                                ('version', (YLeaf(YType.str, 'version'), ['str'])),
                                ('build_information', (YLeaf(YType.str, 'build-information'), ['str'])),
                            ])
                            self.version = None
                            self.build_information = None

                            self.package = Install.SoftwareInventory.Committed.Summary.LocationLoadPath.LoadPath.Package()
                            self.package.parent = self
                            self._children_name_map["package"] = "package"
                            self._segment_path = lambda: "load-path"
                            self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/software-inventory/committed/summary/location-load-path/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Install.SoftwareInventory.Committed.Summary.LocationLoadPath.LoadPath, ['version', 'build_information'], name, value)


                        class Package(_Entity_):
                            """
                            Package
                            
                            .. attribute:: device_name
                            
                            	Device name
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: name
                            
                            	Package group name
                            	**type**\: str
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'installmgr-admin-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Install.SoftwareInventory.Committed.Summary.LocationLoadPath.LoadPath.Package, self).__init__()

                                self.yang_name = "package"
                                self.yang_parent_name = "load-path"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('device_name', (YLeaf(YType.str, 'device-name'), ['str'])),
                                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                ])
                                self.device_name = None
                                self.name = None
                                self._segment_path = lambda: "package"
                                self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/software-inventory/committed/summary/location-load-path/load-path/%s" % self._segment_path()
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Install.SoftwareInventory.Committed.Summary.LocationLoadPath.LoadPath.Package, ['device_name', 'name'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                                return meta._meta_table['Install.SoftwareInventory.Committed.Summary.LocationLoadPath.LoadPath.Package']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                            return meta._meta_table['Install.SoftwareInventory.Committed.Summary.LocationLoadPath.LoadPath']['meta_info']


                    class StandbyLoadPath(_Entity_):
                        """
                        Load paths for standby nodes
                        
                        .. attribute:: package
                        
                        	Package
                        	**type**\:  :py:class:`Package <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Committed.Summary.LocationLoadPath.StandbyLoadPath.Package>`
                        
                        	**config**\: False
                        
                        .. attribute:: version
                        
                        	Version
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: build_information
                        
                        	Build information
                        	**type**\: str
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'installmgr-admin-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Install.SoftwareInventory.Committed.Summary.LocationLoadPath.StandbyLoadPath, self).__init__()

                            self.yang_name = "standby-load-path"
                            self.yang_parent_name = "location-load-path"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("package", ("package", Install.SoftwareInventory.Committed.Summary.LocationLoadPath.StandbyLoadPath.Package))])
                            self._leafs = OrderedDict([
                                ('version', (YLeaf(YType.str, 'version'), ['str'])),
                                ('build_information', (YLeaf(YType.str, 'build-information'), ['str'])),
                            ])
                            self.version = None
                            self.build_information = None

                            self.package = Install.SoftwareInventory.Committed.Summary.LocationLoadPath.StandbyLoadPath.Package()
                            self.package.parent = self
                            self._children_name_map["package"] = "package"
                            self._segment_path = lambda: "standby-load-path"
                            self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/software-inventory/committed/summary/location-load-path/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Install.SoftwareInventory.Committed.Summary.LocationLoadPath.StandbyLoadPath, ['version', 'build_information'], name, value)


                        class Package(_Entity_):
                            """
                            Package
                            
                            .. attribute:: device_name
                            
                            	Device name
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: name
                            
                            	Package group name
                            	**type**\: str
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'installmgr-admin-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Install.SoftwareInventory.Committed.Summary.LocationLoadPath.StandbyLoadPath.Package, self).__init__()

                                self.yang_name = "package"
                                self.yang_parent_name = "standby-load-path"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('device_name', (YLeaf(YType.str, 'device-name'), ['str'])),
                                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                ])
                                self.device_name = None
                                self.name = None
                                self._segment_path = lambda: "package"
                                self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/software-inventory/committed/summary/location-load-path/standby-load-path/%s" % self._segment_path()
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Install.SoftwareInventory.Committed.Summary.LocationLoadPath.StandbyLoadPath.Package, ['device_name', 'name'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                                return meta._meta_table['Install.SoftwareInventory.Committed.Summary.LocationLoadPath.StandbyLoadPath.Package']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                            return meta._meta_table['Install.SoftwareInventory.Committed.Summary.LocationLoadPath.StandbyLoadPath']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                        return meta._meta_table['Install.SoftwareInventory.Committed.Summary.LocationLoadPath']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                    return meta._meta_table['Install.SoftwareInventory.Committed.Summary']['meta_info']


            class Inventories(_Entity_):
                """
                Software inventory
                
                .. attribute:: inventory
                
                	Inventory information for specific node
                	**type**\: list of  		 :py:class:`Inventory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Committed.Inventories.Inventory>`
                
                	**config**\: False
                
                

                """

                _prefix = 'installmgr-admin-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Install.SoftwareInventory.Committed.Inventories, self).__init__()

                    self.yang_name = "inventories"
                    self.yang_parent_name = "committed"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("inventory", ("inventory", Install.SoftwareInventory.Committed.Inventories.Inventory))])
                    self._leafs = OrderedDict()

                    self.inventory = YList(self)
                    self._segment_path = lambda: "inventories"
                    self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/software-inventory/committed/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Install.SoftwareInventory.Committed.Inventories, [], name, value)


                class Inventory(_Entity_):
                    """
                    Inventory information for specific node
                    
                    .. attribute:: node_name  (key)
                    
                    	Node name
                    	**type**\: str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    	**config**\: False
                    
                    .. attribute:: major
                    
                    	Major data version number
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: minor
                    
                    	Minor data version number
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: boot_image_name
                    
                    	Name of the boot image
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: node_type
                    
                    	Node's type
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: secure_domain_router_name
                    
                    	SDR name
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: load_path
                    
                    	Load path
                    	**type**\: list of  		 :py:class:`LoadPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Committed.Inventories.Inventory.LoadPath>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'installmgr-admin-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Install.SoftwareInventory.Committed.Inventories.Inventory, self).__init__()

                        self.yang_name = "inventory"
                        self.yang_parent_name = "inventories"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['node_name']
                        self._child_classes = OrderedDict([("load-path", ("load_path", Install.SoftwareInventory.Committed.Inventories.Inventory.LoadPath))])
                        self._leafs = OrderedDict([
                            ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                            ('major', (YLeaf(YType.uint32, 'major'), ['int'])),
                            ('minor', (YLeaf(YType.uint32, 'minor'), ['int'])),
                            ('boot_image_name', (YLeaf(YType.str, 'boot-image-name'), ['str'])),
                            ('node_type', (YLeaf(YType.uint64, 'node-type'), ['int'])),
                            ('secure_domain_router_name', (YLeaf(YType.str, 'secure-domain-router-name'), ['str'])),
                        ])
                        self.node_name = None
                        self.major = None
                        self.minor = None
                        self.boot_image_name = None
                        self.node_type = None
                        self.secure_domain_router_name = None

                        self.load_path = YList(self)
                        self._segment_path = lambda: "inventory" + "[node-name='" + str(self.node_name) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/software-inventory/committed/inventories/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Install.SoftwareInventory.Committed.Inventories.Inventory, ['node_name', 'major', 'minor', 'boot_image_name', 'node_type', 'secure_domain_router_name'], name, value)


                    class LoadPath(_Entity_):
                        """
                        Load path
                        
                        .. attribute:: package
                        
                        	Package
                        	**type**\:  :py:class:`Package <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Committed.Inventories.Inventory.LoadPath.Package>`
                        
                        	**config**\: False
                        
                        .. attribute:: version
                        
                        	Version
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: build_information
                        
                        	Build information
                        	**type**\: str
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'installmgr-admin-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Install.SoftwareInventory.Committed.Inventories.Inventory.LoadPath, self).__init__()

                            self.yang_name = "load-path"
                            self.yang_parent_name = "inventory"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("package", ("package", Install.SoftwareInventory.Committed.Inventories.Inventory.LoadPath.Package))])
                            self._leafs = OrderedDict([
                                ('version', (YLeaf(YType.str, 'version'), ['str'])),
                                ('build_information', (YLeaf(YType.str, 'build-information'), ['str'])),
                            ])
                            self.version = None
                            self.build_information = None

                            self.package = Install.SoftwareInventory.Committed.Inventories.Inventory.LoadPath.Package()
                            self.package.parent = self
                            self._children_name_map["package"] = "package"
                            self._segment_path = lambda: "load-path"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Install.SoftwareInventory.Committed.Inventories.Inventory.LoadPath, ['version', 'build_information'], name, value)


                        class Package(_Entity_):
                            """
                            Package
                            
                            .. attribute:: device_name
                            
                            	Device name
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: name
                            
                            	Package group name
                            	**type**\: str
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'installmgr-admin-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Install.SoftwareInventory.Committed.Inventories.Inventory.LoadPath.Package, self).__init__()

                                self.yang_name = "package"
                                self.yang_parent_name = "load-path"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('device_name', (YLeaf(YType.str, 'device-name'), ['str'])),
                                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                ])
                                self.device_name = None
                                self.name = None
                                self._segment_path = lambda: "package"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Install.SoftwareInventory.Committed.Inventories.Inventory.LoadPath.Package, ['device_name', 'name'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                                return meta._meta_table['Install.SoftwareInventory.Committed.Inventories.Inventory.LoadPath.Package']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                            return meta._meta_table['Install.SoftwareInventory.Committed.Inventories.Inventory.LoadPath']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                        return meta._meta_table['Install.SoftwareInventory.Committed.Inventories.Inventory']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                    return meta._meta_table['Install.SoftwareInventory.Committed.Inventories']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                return meta._meta_table['Install.SoftwareInventory.Committed']['meta_info']


        class Inactive(_Entity_):
            """
            Inactive inventory information
            
            .. attribute:: summary
            
            	Summarized inventory information
            	**type**\:  :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Inactive.Summary>`
            
            	**config**\: False
            
            .. attribute:: inventories
            
            	Software inventory
            	**type**\:  :py:class:`Inventories <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Inactive.Inventories>`
            
            	**config**\: False
            
            

            """

            _prefix = 'installmgr-admin-oper'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Install.SoftwareInventory.Inactive, self).__init__()

                self.yang_name = "inactive"
                self.yang_parent_name = "software-inventory"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("summary", ("summary", Install.SoftwareInventory.Inactive.Summary)), ("inventories", ("inventories", Install.SoftwareInventory.Inactive.Inventories))])
                self._leafs = OrderedDict()

                self.summary = Install.SoftwareInventory.Inactive.Summary()
                self.summary.parent = self
                self._children_name_map["summary"] = "summary"

                self.inventories = Install.SoftwareInventory.Inactive.Inventories()
                self.inventories.parent = self
                self._children_name_map["inventories"] = "inventories"
                self._segment_path = lambda: "inactive"
                self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/software-inventory/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Install.SoftwareInventory.Inactive, [], name, value)


            class Summary(_Entity_):
                """
                Summarized inventory information
                
                .. attribute:: default_load_path
                
                	Default load path
                	**type**\:  :py:class:`DefaultLoadPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Inactive.Summary.DefaultLoadPath>`
                
                	**config**\: False
                
                .. attribute:: admin_load_path
                
                	Admin Resources load path
                	**type**\:  :py:class:`AdminLoadPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Inactive.Summary.AdminLoadPath>`
                
                	**config**\: False
                
                .. attribute:: sdr_load_path
                
                	SDR load paths
                	**type**\: list of  		 :py:class:`SdrLoadPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Inactive.Summary.SdrLoadPath>`
                
                	**config**\: False
                
                .. attribute:: location_load_path
                
                	Location load paths
                	**type**\: list of  		 :py:class:`LocationLoadPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Inactive.Summary.LocationLoadPath>`
                
                	**config**\: False
                
                

                """

                _prefix = 'installmgr-admin-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Install.SoftwareInventory.Inactive.Summary, self).__init__()

                    self.yang_name = "summary"
                    self.yang_parent_name = "inactive"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("default-load-path", ("default_load_path", Install.SoftwareInventory.Inactive.Summary.DefaultLoadPath)), ("admin-load-path", ("admin_load_path", Install.SoftwareInventory.Inactive.Summary.AdminLoadPath)), ("sdr-load-path", ("sdr_load_path", Install.SoftwareInventory.Inactive.Summary.SdrLoadPath)), ("location-load-path", ("location_load_path", Install.SoftwareInventory.Inactive.Summary.LocationLoadPath))])
                    self._leafs = OrderedDict()

                    self.default_load_path = Install.SoftwareInventory.Inactive.Summary.DefaultLoadPath()
                    self.default_load_path.parent = self
                    self._children_name_map["default_load_path"] = "default-load-path"

                    self.admin_load_path = Install.SoftwareInventory.Inactive.Summary.AdminLoadPath()
                    self.admin_load_path.parent = self
                    self._children_name_map["admin_load_path"] = "admin-load-path"

                    self.sdr_load_path = YList(self)
                    self.location_load_path = YList(self)
                    self._segment_path = lambda: "summary"
                    self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/software-inventory/inactive/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Install.SoftwareInventory.Inactive.Summary, [], name, value)


                class DefaultLoadPath(_Entity_):
                    """
                    Default load path
                    
                    .. attribute:: request_id
                    
                    	Install op affecting scope
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: admin_match
                    
                    	Does this match the Admin Resources load path?
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: secure_domain_router_name
                    
                    	Names of SDRs this applies to
                    	**type**\: list of str
                    
                    	**config**\: False
                    
                    .. attribute:: load_path
                    
                    	Default load path
                    	**type**\: list of  		 :py:class:`LoadPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Inactive.Summary.DefaultLoadPath.LoadPath>`
                    
                    	**config**\: False
                    
                    .. attribute:: standby_load_path
                    
                    	Load paths for standby nodes
                    	**type**\: list of  		 :py:class:`StandbyLoadPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Inactive.Summary.DefaultLoadPath.StandbyLoadPath>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'installmgr-admin-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Install.SoftwareInventory.Inactive.Summary.DefaultLoadPath, self).__init__()

                        self.yang_name = "default-load-path"
                        self.yang_parent_name = "summary"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("load-path", ("load_path", Install.SoftwareInventory.Inactive.Summary.DefaultLoadPath.LoadPath)), ("standby-load-path", ("standby_load_path", Install.SoftwareInventory.Inactive.Summary.DefaultLoadPath.StandbyLoadPath))])
                        self._leafs = OrderedDict([
                            ('request_id', (YLeaf(YType.uint32, 'request-id'), ['int'])),
                            ('admin_match', (YLeaf(YType.boolean, 'admin-match'), ['bool'])),
                            ('secure_domain_router_name', (YLeafList(YType.str, 'secure-domain-router-name'), ['str'])),
                        ])
                        self.request_id = None
                        self.admin_match = None
                        self.secure_domain_router_name = []

                        self.load_path = YList(self)
                        self.standby_load_path = YList(self)
                        self._segment_path = lambda: "default-load-path"
                        self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/software-inventory/inactive/summary/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Install.SoftwareInventory.Inactive.Summary.DefaultLoadPath, ['request_id', 'admin_match', 'secure_domain_router_name'], name, value)


                    class LoadPath(_Entity_):
                        """
                        Default load path
                        
                        .. attribute:: package
                        
                        	Package
                        	**type**\:  :py:class:`Package <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Inactive.Summary.DefaultLoadPath.LoadPath.Package>`
                        
                        	**config**\: False
                        
                        .. attribute:: version
                        
                        	Version
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: build_information
                        
                        	Build information
                        	**type**\: str
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'installmgr-admin-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Install.SoftwareInventory.Inactive.Summary.DefaultLoadPath.LoadPath, self).__init__()

                            self.yang_name = "load-path"
                            self.yang_parent_name = "default-load-path"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("package", ("package", Install.SoftwareInventory.Inactive.Summary.DefaultLoadPath.LoadPath.Package))])
                            self._leafs = OrderedDict([
                                ('version', (YLeaf(YType.str, 'version'), ['str'])),
                                ('build_information', (YLeaf(YType.str, 'build-information'), ['str'])),
                            ])
                            self.version = None
                            self.build_information = None

                            self.package = Install.SoftwareInventory.Inactive.Summary.DefaultLoadPath.LoadPath.Package()
                            self.package.parent = self
                            self._children_name_map["package"] = "package"
                            self._segment_path = lambda: "load-path"
                            self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/software-inventory/inactive/summary/default-load-path/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Install.SoftwareInventory.Inactive.Summary.DefaultLoadPath.LoadPath, ['version', 'build_information'], name, value)


                        class Package(_Entity_):
                            """
                            Package
                            
                            .. attribute:: device_name
                            
                            	Device name
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: name
                            
                            	Package group name
                            	**type**\: str
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'installmgr-admin-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Install.SoftwareInventory.Inactive.Summary.DefaultLoadPath.LoadPath.Package, self).__init__()

                                self.yang_name = "package"
                                self.yang_parent_name = "load-path"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('device_name', (YLeaf(YType.str, 'device-name'), ['str'])),
                                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                ])
                                self.device_name = None
                                self.name = None
                                self._segment_path = lambda: "package"
                                self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/software-inventory/inactive/summary/default-load-path/load-path/%s" % self._segment_path()
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Install.SoftwareInventory.Inactive.Summary.DefaultLoadPath.LoadPath.Package, ['device_name', 'name'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                                return meta._meta_table['Install.SoftwareInventory.Inactive.Summary.DefaultLoadPath.LoadPath.Package']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                            return meta._meta_table['Install.SoftwareInventory.Inactive.Summary.DefaultLoadPath.LoadPath']['meta_info']


                    class StandbyLoadPath(_Entity_):
                        """
                        Load paths for standby nodes
                        
                        .. attribute:: package
                        
                        	Package
                        	**type**\:  :py:class:`Package <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Inactive.Summary.DefaultLoadPath.StandbyLoadPath.Package>`
                        
                        	**config**\: False
                        
                        .. attribute:: version
                        
                        	Version
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: build_information
                        
                        	Build information
                        	**type**\: str
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'installmgr-admin-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Install.SoftwareInventory.Inactive.Summary.DefaultLoadPath.StandbyLoadPath, self).__init__()

                            self.yang_name = "standby-load-path"
                            self.yang_parent_name = "default-load-path"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("package", ("package", Install.SoftwareInventory.Inactive.Summary.DefaultLoadPath.StandbyLoadPath.Package))])
                            self._leafs = OrderedDict([
                                ('version', (YLeaf(YType.str, 'version'), ['str'])),
                                ('build_information', (YLeaf(YType.str, 'build-information'), ['str'])),
                            ])
                            self.version = None
                            self.build_information = None

                            self.package = Install.SoftwareInventory.Inactive.Summary.DefaultLoadPath.StandbyLoadPath.Package()
                            self.package.parent = self
                            self._children_name_map["package"] = "package"
                            self._segment_path = lambda: "standby-load-path"
                            self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/software-inventory/inactive/summary/default-load-path/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Install.SoftwareInventory.Inactive.Summary.DefaultLoadPath.StandbyLoadPath, ['version', 'build_information'], name, value)


                        class Package(_Entity_):
                            """
                            Package
                            
                            .. attribute:: device_name
                            
                            	Device name
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: name
                            
                            	Package group name
                            	**type**\: str
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'installmgr-admin-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Install.SoftwareInventory.Inactive.Summary.DefaultLoadPath.StandbyLoadPath.Package, self).__init__()

                                self.yang_name = "package"
                                self.yang_parent_name = "standby-load-path"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('device_name', (YLeaf(YType.str, 'device-name'), ['str'])),
                                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                ])
                                self.device_name = None
                                self.name = None
                                self._segment_path = lambda: "package"
                                self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/software-inventory/inactive/summary/default-load-path/standby-load-path/%s" % self._segment_path()
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Install.SoftwareInventory.Inactive.Summary.DefaultLoadPath.StandbyLoadPath.Package, ['device_name', 'name'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                                return meta._meta_table['Install.SoftwareInventory.Inactive.Summary.DefaultLoadPath.StandbyLoadPath.Package']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                            return meta._meta_table['Install.SoftwareInventory.Inactive.Summary.DefaultLoadPath.StandbyLoadPath']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                        return meta._meta_table['Install.SoftwareInventory.Inactive.Summary.DefaultLoadPath']['meta_info']


                class AdminLoadPath(_Entity_):
                    """
                    Admin Resources load path
                    
                    .. attribute:: request_id
                    
                    	Install op affecting scope
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: load_path
                    
                    	Admin Resources load path
                    	**type**\: list of  		 :py:class:`LoadPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Inactive.Summary.AdminLoadPath.LoadPath>`
                    
                    	**config**\: False
                    
                    .. attribute:: standby_load_path
                    
                    	Load paths for standby nodes
                    	**type**\: list of  		 :py:class:`StandbyLoadPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Inactive.Summary.AdminLoadPath.StandbyLoadPath>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'installmgr-admin-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Install.SoftwareInventory.Inactive.Summary.AdminLoadPath, self).__init__()

                        self.yang_name = "admin-load-path"
                        self.yang_parent_name = "summary"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("load-path", ("load_path", Install.SoftwareInventory.Inactive.Summary.AdminLoadPath.LoadPath)), ("standby-load-path", ("standby_load_path", Install.SoftwareInventory.Inactive.Summary.AdminLoadPath.StandbyLoadPath))])
                        self._leafs = OrderedDict([
                            ('request_id', (YLeaf(YType.uint32, 'request-id'), ['int'])),
                        ])
                        self.request_id = None

                        self.load_path = YList(self)
                        self.standby_load_path = YList(self)
                        self._segment_path = lambda: "admin-load-path"
                        self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/software-inventory/inactive/summary/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Install.SoftwareInventory.Inactive.Summary.AdminLoadPath, ['request_id'], name, value)


                    class LoadPath(_Entity_):
                        """
                        Admin Resources load path
                        
                        .. attribute:: package
                        
                        	Package
                        	**type**\:  :py:class:`Package <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Inactive.Summary.AdminLoadPath.LoadPath.Package>`
                        
                        	**config**\: False
                        
                        .. attribute:: version
                        
                        	Version
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: build_information
                        
                        	Build information
                        	**type**\: str
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'installmgr-admin-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Install.SoftwareInventory.Inactive.Summary.AdminLoadPath.LoadPath, self).__init__()

                            self.yang_name = "load-path"
                            self.yang_parent_name = "admin-load-path"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("package", ("package", Install.SoftwareInventory.Inactive.Summary.AdminLoadPath.LoadPath.Package))])
                            self._leafs = OrderedDict([
                                ('version', (YLeaf(YType.str, 'version'), ['str'])),
                                ('build_information', (YLeaf(YType.str, 'build-information'), ['str'])),
                            ])
                            self.version = None
                            self.build_information = None

                            self.package = Install.SoftwareInventory.Inactive.Summary.AdminLoadPath.LoadPath.Package()
                            self.package.parent = self
                            self._children_name_map["package"] = "package"
                            self._segment_path = lambda: "load-path"
                            self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/software-inventory/inactive/summary/admin-load-path/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Install.SoftwareInventory.Inactive.Summary.AdminLoadPath.LoadPath, ['version', 'build_information'], name, value)


                        class Package(_Entity_):
                            """
                            Package
                            
                            .. attribute:: device_name
                            
                            	Device name
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: name
                            
                            	Package group name
                            	**type**\: str
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'installmgr-admin-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Install.SoftwareInventory.Inactive.Summary.AdminLoadPath.LoadPath.Package, self).__init__()

                                self.yang_name = "package"
                                self.yang_parent_name = "load-path"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('device_name', (YLeaf(YType.str, 'device-name'), ['str'])),
                                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                ])
                                self.device_name = None
                                self.name = None
                                self._segment_path = lambda: "package"
                                self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/software-inventory/inactive/summary/admin-load-path/load-path/%s" % self._segment_path()
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Install.SoftwareInventory.Inactive.Summary.AdminLoadPath.LoadPath.Package, ['device_name', 'name'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                                return meta._meta_table['Install.SoftwareInventory.Inactive.Summary.AdminLoadPath.LoadPath.Package']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                            return meta._meta_table['Install.SoftwareInventory.Inactive.Summary.AdminLoadPath.LoadPath']['meta_info']


                    class StandbyLoadPath(_Entity_):
                        """
                        Load paths for standby nodes
                        
                        .. attribute:: package
                        
                        	Package
                        	**type**\:  :py:class:`Package <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Inactive.Summary.AdminLoadPath.StandbyLoadPath.Package>`
                        
                        	**config**\: False
                        
                        .. attribute:: version
                        
                        	Version
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: build_information
                        
                        	Build information
                        	**type**\: str
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'installmgr-admin-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Install.SoftwareInventory.Inactive.Summary.AdminLoadPath.StandbyLoadPath, self).__init__()

                            self.yang_name = "standby-load-path"
                            self.yang_parent_name = "admin-load-path"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("package", ("package", Install.SoftwareInventory.Inactive.Summary.AdminLoadPath.StandbyLoadPath.Package))])
                            self._leafs = OrderedDict([
                                ('version', (YLeaf(YType.str, 'version'), ['str'])),
                                ('build_information', (YLeaf(YType.str, 'build-information'), ['str'])),
                            ])
                            self.version = None
                            self.build_information = None

                            self.package = Install.SoftwareInventory.Inactive.Summary.AdminLoadPath.StandbyLoadPath.Package()
                            self.package.parent = self
                            self._children_name_map["package"] = "package"
                            self._segment_path = lambda: "standby-load-path"
                            self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/software-inventory/inactive/summary/admin-load-path/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Install.SoftwareInventory.Inactive.Summary.AdminLoadPath.StandbyLoadPath, ['version', 'build_information'], name, value)


                        class Package(_Entity_):
                            """
                            Package
                            
                            .. attribute:: device_name
                            
                            	Device name
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: name
                            
                            	Package group name
                            	**type**\: str
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'installmgr-admin-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Install.SoftwareInventory.Inactive.Summary.AdminLoadPath.StandbyLoadPath.Package, self).__init__()

                                self.yang_name = "package"
                                self.yang_parent_name = "standby-load-path"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('device_name', (YLeaf(YType.str, 'device-name'), ['str'])),
                                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                ])
                                self.device_name = None
                                self.name = None
                                self._segment_path = lambda: "package"
                                self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/software-inventory/inactive/summary/admin-load-path/standby-load-path/%s" % self._segment_path()
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Install.SoftwareInventory.Inactive.Summary.AdminLoadPath.StandbyLoadPath.Package, ['device_name', 'name'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                                return meta._meta_table['Install.SoftwareInventory.Inactive.Summary.AdminLoadPath.StandbyLoadPath.Package']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                            return meta._meta_table['Install.SoftwareInventory.Inactive.Summary.AdminLoadPath.StandbyLoadPath']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                        return meta._meta_table['Install.SoftwareInventory.Inactive.Summary.AdminLoadPath']['meta_info']


                class SdrLoadPath(_Entity_):
                    """
                    SDR load paths
                    
                    .. attribute:: request_id
                    
                    	Install op affecting scope
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: secure_domain_router_name
                    
                    	SDR name
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: load_path
                    
                    	Load path
                    	**type**\: list of  		 :py:class:`LoadPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Inactive.Summary.SdrLoadPath.LoadPath>`
                    
                    	**config**\: False
                    
                    .. attribute:: standby_load_path
                    
                    	Load paths for standby nodes
                    	**type**\: list of  		 :py:class:`StandbyLoadPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Inactive.Summary.SdrLoadPath.StandbyLoadPath>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'installmgr-admin-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Install.SoftwareInventory.Inactive.Summary.SdrLoadPath, self).__init__()

                        self.yang_name = "sdr-load-path"
                        self.yang_parent_name = "summary"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("load-path", ("load_path", Install.SoftwareInventory.Inactive.Summary.SdrLoadPath.LoadPath)), ("standby-load-path", ("standby_load_path", Install.SoftwareInventory.Inactive.Summary.SdrLoadPath.StandbyLoadPath))])
                        self._leafs = OrderedDict([
                            ('request_id', (YLeaf(YType.uint32, 'request-id'), ['int'])),
                            ('secure_domain_router_name', (YLeaf(YType.str, 'secure-domain-router-name'), ['str'])),
                        ])
                        self.request_id = None
                        self.secure_domain_router_name = None

                        self.load_path = YList(self)
                        self.standby_load_path = YList(self)
                        self._segment_path = lambda: "sdr-load-path"
                        self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/software-inventory/inactive/summary/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Install.SoftwareInventory.Inactive.Summary.SdrLoadPath, ['request_id', 'secure_domain_router_name'], name, value)


                    class LoadPath(_Entity_):
                        """
                        Load path
                        
                        .. attribute:: package
                        
                        	Package
                        	**type**\:  :py:class:`Package <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Inactive.Summary.SdrLoadPath.LoadPath.Package>`
                        
                        	**config**\: False
                        
                        .. attribute:: version
                        
                        	Version
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: build_information
                        
                        	Build information
                        	**type**\: str
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'installmgr-admin-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Install.SoftwareInventory.Inactive.Summary.SdrLoadPath.LoadPath, self).__init__()

                            self.yang_name = "load-path"
                            self.yang_parent_name = "sdr-load-path"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("package", ("package", Install.SoftwareInventory.Inactive.Summary.SdrLoadPath.LoadPath.Package))])
                            self._leafs = OrderedDict([
                                ('version', (YLeaf(YType.str, 'version'), ['str'])),
                                ('build_information', (YLeaf(YType.str, 'build-information'), ['str'])),
                            ])
                            self.version = None
                            self.build_information = None

                            self.package = Install.SoftwareInventory.Inactive.Summary.SdrLoadPath.LoadPath.Package()
                            self.package.parent = self
                            self._children_name_map["package"] = "package"
                            self._segment_path = lambda: "load-path"
                            self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/software-inventory/inactive/summary/sdr-load-path/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Install.SoftwareInventory.Inactive.Summary.SdrLoadPath.LoadPath, ['version', 'build_information'], name, value)


                        class Package(_Entity_):
                            """
                            Package
                            
                            .. attribute:: device_name
                            
                            	Device name
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: name
                            
                            	Package group name
                            	**type**\: str
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'installmgr-admin-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Install.SoftwareInventory.Inactive.Summary.SdrLoadPath.LoadPath.Package, self).__init__()

                                self.yang_name = "package"
                                self.yang_parent_name = "load-path"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('device_name', (YLeaf(YType.str, 'device-name'), ['str'])),
                                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                ])
                                self.device_name = None
                                self.name = None
                                self._segment_path = lambda: "package"
                                self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/software-inventory/inactive/summary/sdr-load-path/load-path/%s" % self._segment_path()
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Install.SoftwareInventory.Inactive.Summary.SdrLoadPath.LoadPath.Package, ['device_name', 'name'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                                return meta._meta_table['Install.SoftwareInventory.Inactive.Summary.SdrLoadPath.LoadPath.Package']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                            return meta._meta_table['Install.SoftwareInventory.Inactive.Summary.SdrLoadPath.LoadPath']['meta_info']


                    class StandbyLoadPath(_Entity_):
                        """
                        Load paths for standby nodes
                        
                        .. attribute:: package
                        
                        	Package
                        	**type**\:  :py:class:`Package <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Inactive.Summary.SdrLoadPath.StandbyLoadPath.Package>`
                        
                        	**config**\: False
                        
                        .. attribute:: version
                        
                        	Version
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: build_information
                        
                        	Build information
                        	**type**\: str
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'installmgr-admin-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Install.SoftwareInventory.Inactive.Summary.SdrLoadPath.StandbyLoadPath, self).__init__()

                            self.yang_name = "standby-load-path"
                            self.yang_parent_name = "sdr-load-path"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("package", ("package", Install.SoftwareInventory.Inactive.Summary.SdrLoadPath.StandbyLoadPath.Package))])
                            self._leafs = OrderedDict([
                                ('version', (YLeaf(YType.str, 'version'), ['str'])),
                                ('build_information', (YLeaf(YType.str, 'build-information'), ['str'])),
                            ])
                            self.version = None
                            self.build_information = None

                            self.package = Install.SoftwareInventory.Inactive.Summary.SdrLoadPath.StandbyLoadPath.Package()
                            self.package.parent = self
                            self._children_name_map["package"] = "package"
                            self._segment_path = lambda: "standby-load-path"
                            self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/software-inventory/inactive/summary/sdr-load-path/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Install.SoftwareInventory.Inactive.Summary.SdrLoadPath.StandbyLoadPath, ['version', 'build_information'], name, value)


                        class Package(_Entity_):
                            """
                            Package
                            
                            .. attribute:: device_name
                            
                            	Device name
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: name
                            
                            	Package group name
                            	**type**\: str
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'installmgr-admin-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Install.SoftwareInventory.Inactive.Summary.SdrLoadPath.StandbyLoadPath.Package, self).__init__()

                                self.yang_name = "package"
                                self.yang_parent_name = "standby-load-path"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('device_name', (YLeaf(YType.str, 'device-name'), ['str'])),
                                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                ])
                                self.device_name = None
                                self.name = None
                                self._segment_path = lambda: "package"
                                self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/software-inventory/inactive/summary/sdr-load-path/standby-load-path/%s" % self._segment_path()
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Install.SoftwareInventory.Inactive.Summary.SdrLoadPath.StandbyLoadPath.Package, ['device_name', 'name'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                                return meta._meta_table['Install.SoftwareInventory.Inactive.Summary.SdrLoadPath.StandbyLoadPath.Package']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                            return meta._meta_table['Install.SoftwareInventory.Inactive.Summary.SdrLoadPath.StandbyLoadPath']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                        return meta._meta_table['Install.SoftwareInventory.Inactive.Summary.SdrLoadPath']['meta_info']


                class LocationLoadPath(_Entity_):
                    """
                    Location load paths
                    
                    .. attribute:: request_id
                    
                    	Install op affecting scope
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: secure_domain_router_name
                    
                    	SDR name
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: node_name
                    
                    	Node identifier
                    	**type**\: str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    	**config**\: False
                    
                    .. attribute:: load_path
                    
                    	Load path
                    	**type**\: list of  		 :py:class:`LoadPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Inactive.Summary.LocationLoadPath.LoadPath>`
                    
                    	**config**\: False
                    
                    .. attribute:: standby_load_path
                    
                    	Load paths for standby nodes
                    	**type**\: list of  		 :py:class:`StandbyLoadPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Inactive.Summary.LocationLoadPath.StandbyLoadPath>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'installmgr-admin-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Install.SoftwareInventory.Inactive.Summary.LocationLoadPath, self).__init__()

                        self.yang_name = "location-load-path"
                        self.yang_parent_name = "summary"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("load-path", ("load_path", Install.SoftwareInventory.Inactive.Summary.LocationLoadPath.LoadPath)), ("standby-load-path", ("standby_load_path", Install.SoftwareInventory.Inactive.Summary.LocationLoadPath.StandbyLoadPath))])
                        self._leafs = OrderedDict([
                            ('request_id', (YLeaf(YType.uint32, 'request-id'), ['int'])),
                            ('secure_domain_router_name', (YLeaf(YType.str, 'secure-domain-router-name'), ['str'])),
                            ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                        ])
                        self.request_id = None
                        self.secure_domain_router_name = None
                        self.node_name = None

                        self.load_path = YList(self)
                        self.standby_load_path = YList(self)
                        self._segment_path = lambda: "location-load-path"
                        self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/software-inventory/inactive/summary/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Install.SoftwareInventory.Inactive.Summary.LocationLoadPath, ['request_id', 'secure_domain_router_name', 'node_name'], name, value)


                    class LoadPath(_Entity_):
                        """
                        Load path
                        
                        .. attribute:: package
                        
                        	Package
                        	**type**\:  :py:class:`Package <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Inactive.Summary.LocationLoadPath.LoadPath.Package>`
                        
                        	**config**\: False
                        
                        .. attribute:: version
                        
                        	Version
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: build_information
                        
                        	Build information
                        	**type**\: str
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'installmgr-admin-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Install.SoftwareInventory.Inactive.Summary.LocationLoadPath.LoadPath, self).__init__()

                            self.yang_name = "load-path"
                            self.yang_parent_name = "location-load-path"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("package", ("package", Install.SoftwareInventory.Inactive.Summary.LocationLoadPath.LoadPath.Package))])
                            self._leafs = OrderedDict([
                                ('version', (YLeaf(YType.str, 'version'), ['str'])),
                                ('build_information', (YLeaf(YType.str, 'build-information'), ['str'])),
                            ])
                            self.version = None
                            self.build_information = None

                            self.package = Install.SoftwareInventory.Inactive.Summary.LocationLoadPath.LoadPath.Package()
                            self.package.parent = self
                            self._children_name_map["package"] = "package"
                            self._segment_path = lambda: "load-path"
                            self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/software-inventory/inactive/summary/location-load-path/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Install.SoftwareInventory.Inactive.Summary.LocationLoadPath.LoadPath, ['version', 'build_information'], name, value)


                        class Package(_Entity_):
                            """
                            Package
                            
                            .. attribute:: device_name
                            
                            	Device name
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: name
                            
                            	Package group name
                            	**type**\: str
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'installmgr-admin-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Install.SoftwareInventory.Inactive.Summary.LocationLoadPath.LoadPath.Package, self).__init__()

                                self.yang_name = "package"
                                self.yang_parent_name = "load-path"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('device_name', (YLeaf(YType.str, 'device-name'), ['str'])),
                                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                ])
                                self.device_name = None
                                self.name = None
                                self._segment_path = lambda: "package"
                                self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/software-inventory/inactive/summary/location-load-path/load-path/%s" % self._segment_path()
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Install.SoftwareInventory.Inactive.Summary.LocationLoadPath.LoadPath.Package, ['device_name', 'name'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                                return meta._meta_table['Install.SoftwareInventory.Inactive.Summary.LocationLoadPath.LoadPath.Package']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                            return meta._meta_table['Install.SoftwareInventory.Inactive.Summary.LocationLoadPath.LoadPath']['meta_info']


                    class StandbyLoadPath(_Entity_):
                        """
                        Load paths for standby nodes
                        
                        .. attribute:: package
                        
                        	Package
                        	**type**\:  :py:class:`Package <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Inactive.Summary.LocationLoadPath.StandbyLoadPath.Package>`
                        
                        	**config**\: False
                        
                        .. attribute:: version
                        
                        	Version
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: build_information
                        
                        	Build information
                        	**type**\: str
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'installmgr-admin-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Install.SoftwareInventory.Inactive.Summary.LocationLoadPath.StandbyLoadPath, self).__init__()

                            self.yang_name = "standby-load-path"
                            self.yang_parent_name = "location-load-path"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("package", ("package", Install.SoftwareInventory.Inactive.Summary.LocationLoadPath.StandbyLoadPath.Package))])
                            self._leafs = OrderedDict([
                                ('version', (YLeaf(YType.str, 'version'), ['str'])),
                                ('build_information', (YLeaf(YType.str, 'build-information'), ['str'])),
                            ])
                            self.version = None
                            self.build_information = None

                            self.package = Install.SoftwareInventory.Inactive.Summary.LocationLoadPath.StandbyLoadPath.Package()
                            self.package.parent = self
                            self._children_name_map["package"] = "package"
                            self._segment_path = lambda: "standby-load-path"
                            self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/software-inventory/inactive/summary/location-load-path/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Install.SoftwareInventory.Inactive.Summary.LocationLoadPath.StandbyLoadPath, ['version', 'build_information'], name, value)


                        class Package(_Entity_):
                            """
                            Package
                            
                            .. attribute:: device_name
                            
                            	Device name
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: name
                            
                            	Package group name
                            	**type**\: str
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'installmgr-admin-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Install.SoftwareInventory.Inactive.Summary.LocationLoadPath.StandbyLoadPath.Package, self).__init__()

                                self.yang_name = "package"
                                self.yang_parent_name = "standby-load-path"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('device_name', (YLeaf(YType.str, 'device-name'), ['str'])),
                                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                ])
                                self.device_name = None
                                self.name = None
                                self._segment_path = lambda: "package"
                                self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/software-inventory/inactive/summary/location-load-path/standby-load-path/%s" % self._segment_path()
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Install.SoftwareInventory.Inactive.Summary.LocationLoadPath.StandbyLoadPath.Package, ['device_name', 'name'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                                return meta._meta_table['Install.SoftwareInventory.Inactive.Summary.LocationLoadPath.StandbyLoadPath.Package']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                            return meta._meta_table['Install.SoftwareInventory.Inactive.Summary.LocationLoadPath.StandbyLoadPath']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                        return meta._meta_table['Install.SoftwareInventory.Inactive.Summary.LocationLoadPath']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                    return meta._meta_table['Install.SoftwareInventory.Inactive.Summary']['meta_info']


            class Inventories(_Entity_):
                """
                Software inventory
                
                .. attribute:: inventory
                
                	Inventory information for specific node
                	**type**\: list of  		 :py:class:`Inventory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Inactive.Inventories.Inventory>`
                
                	**config**\: False
                
                

                """

                _prefix = 'installmgr-admin-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Install.SoftwareInventory.Inactive.Inventories, self).__init__()

                    self.yang_name = "inventories"
                    self.yang_parent_name = "inactive"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("inventory", ("inventory", Install.SoftwareInventory.Inactive.Inventories.Inventory))])
                    self._leafs = OrderedDict()

                    self.inventory = YList(self)
                    self._segment_path = lambda: "inventories"
                    self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/software-inventory/inactive/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Install.SoftwareInventory.Inactive.Inventories, [], name, value)


                class Inventory(_Entity_):
                    """
                    Inventory information for specific node
                    
                    .. attribute:: node_name  (key)
                    
                    	Node name
                    	**type**\: str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    	**config**\: False
                    
                    .. attribute:: major
                    
                    	Major data version number
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: minor
                    
                    	Minor data version number
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: boot_image_name
                    
                    	Name of the boot image
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: node_type
                    
                    	Node's type
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: secure_domain_router_name
                    
                    	SDR name
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: load_path
                    
                    	Load path
                    	**type**\: list of  		 :py:class:`LoadPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Inactive.Inventories.Inventory.LoadPath>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'installmgr-admin-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Install.SoftwareInventory.Inactive.Inventories.Inventory, self).__init__()

                        self.yang_name = "inventory"
                        self.yang_parent_name = "inventories"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['node_name']
                        self._child_classes = OrderedDict([("load-path", ("load_path", Install.SoftwareInventory.Inactive.Inventories.Inventory.LoadPath))])
                        self._leafs = OrderedDict([
                            ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                            ('major', (YLeaf(YType.uint32, 'major'), ['int'])),
                            ('minor', (YLeaf(YType.uint32, 'minor'), ['int'])),
                            ('boot_image_name', (YLeaf(YType.str, 'boot-image-name'), ['str'])),
                            ('node_type', (YLeaf(YType.uint64, 'node-type'), ['int'])),
                            ('secure_domain_router_name', (YLeaf(YType.str, 'secure-domain-router-name'), ['str'])),
                        ])
                        self.node_name = None
                        self.major = None
                        self.minor = None
                        self.boot_image_name = None
                        self.node_type = None
                        self.secure_domain_router_name = None

                        self.load_path = YList(self)
                        self._segment_path = lambda: "inventory" + "[node-name='" + str(self.node_name) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/software-inventory/inactive/inventories/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Install.SoftwareInventory.Inactive.Inventories.Inventory, ['node_name', 'major', 'minor', 'boot_image_name', 'node_type', 'secure_domain_router_name'], name, value)


                    class LoadPath(_Entity_):
                        """
                        Load path
                        
                        .. attribute:: package
                        
                        	Package
                        	**type**\:  :py:class:`Package <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Inactive.Inventories.Inventory.LoadPath.Package>`
                        
                        	**config**\: False
                        
                        .. attribute:: version
                        
                        	Version
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: build_information
                        
                        	Build information
                        	**type**\: str
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'installmgr-admin-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Install.SoftwareInventory.Inactive.Inventories.Inventory.LoadPath, self).__init__()

                            self.yang_name = "load-path"
                            self.yang_parent_name = "inventory"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("package", ("package", Install.SoftwareInventory.Inactive.Inventories.Inventory.LoadPath.Package))])
                            self._leafs = OrderedDict([
                                ('version', (YLeaf(YType.str, 'version'), ['str'])),
                                ('build_information', (YLeaf(YType.str, 'build-information'), ['str'])),
                            ])
                            self.version = None
                            self.build_information = None

                            self.package = Install.SoftwareInventory.Inactive.Inventories.Inventory.LoadPath.Package()
                            self.package.parent = self
                            self._children_name_map["package"] = "package"
                            self._segment_path = lambda: "load-path"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Install.SoftwareInventory.Inactive.Inventories.Inventory.LoadPath, ['version', 'build_information'], name, value)


                        class Package(_Entity_):
                            """
                            Package
                            
                            .. attribute:: device_name
                            
                            	Device name
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: name
                            
                            	Package group name
                            	**type**\: str
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'installmgr-admin-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Install.SoftwareInventory.Inactive.Inventories.Inventory.LoadPath.Package, self).__init__()

                                self.yang_name = "package"
                                self.yang_parent_name = "load-path"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('device_name', (YLeaf(YType.str, 'device-name'), ['str'])),
                                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                ])
                                self.device_name = None
                                self.name = None
                                self._segment_path = lambda: "package"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Install.SoftwareInventory.Inactive.Inventories.Inventory.LoadPath.Package, ['device_name', 'name'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                                return meta._meta_table['Install.SoftwareInventory.Inactive.Inventories.Inventory.LoadPath.Package']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                            return meta._meta_table['Install.SoftwareInventory.Inactive.Inventories.Inventory.LoadPath']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                        return meta._meta_table['Install.SoftwareInventory.Inactive.Inventories.Inventory']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                    return meta._meta_table['Install.SoftwareInventory.Inactive.Inventories']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                return meta._meta_table['Install.SoftwareInventory.Inactive']['meta_info']


        class Requests(_Entity_):
            """
            Install operation requests
            
            .. attribute:: requests
            
            	Install operation request history
            	**type**\:  :py:class:`Requests_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Requests.Requests_>`
            
            	**config**\: False
            
            

            """

            _prefix = 'installmgr-admin-oper'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Install.SoftwareInventory.Requests, self).__init__()

                self.yang_name = "requests"
                self.yang_parent_name = "software-inventory"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("requests", ("requests", Install.SoftwareInventory.Requests.Requests_))])
                self._leafs = OrderedDict()

                self.requests = Install.SoftwareInventory.Requests.Requests_()
                self.requests.parent = self
                self._children_name_map["requests"] = "requests"
                self._segment_path = lambda: "requests"
                self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/software-inventory/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Install.SoftwareInventory.Requests, [], name, value)


            class Requests_(_Entity_):
                """
                Install operation request history
                
                .. attribute:: request
                
                	Install operation request information
                	**type**\: list of  		 :py:class:`Request <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Requests.Requests_.Request>`
                
                	**config**\: False
                
                

                """

                _prefix = 'installmgr-admin-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Install.SoftwareInventory.Requests.Requests_, self).__init__()

                    self.yang_name = "requests"
                    self.yang_parent_name = "requests"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("request", ("request", Install.SoftwareInventory.Requests.Requests_.Request))])
                    self._leafs = OrderedDict()

                    self.request = YList(self)
                    self._segment_path = lambda: "requests"
                    self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/software-inventory/requests/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Install.SoftwareInventory.Requests.Requests_, [], name, value)


                class Request(_Entity_):
                    """
                    Install operation request information
                    
                    .. attribute:: request_id  (key)
                    
                    	Install operation request ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: inventories
                    
                    	Inventory information of install operation request
                    	**type**\:  :py:class:`Inventories <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Requests.Requests_.Request.Inventories>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'installmgr-admin-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Install.SoftwareInventory.Requests.Requests_.Request, self).__init__()

                        self.yang_name = "request"
                        self.yang_parent_name = "requests"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['request_id']
                        self._child_classes = OrderedDict([("inventories", ("inventories", Install.SoftwareInventory.Requests.Requests_.Request.Inventories))])
                        self._leafs = OrderedDict([
                            ('request_id', (YLeaf(YType.uint32, 'request-id'), ['int'])),
                        ])
                        self.request_id = None

                        self.inventories = Install.SoftwareInventory.Requests.Requests_.Request.Inventories()
                        self.inventories.parent = self
                        self._children_name_map["inventories"] = "inventories"
                        self._segment_path = lambda: "request" + "[request-id='" + str(self.request_id) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/software-inventory/requests/requests/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Install.SoftwareInventory.Requests.Requests_.Request, ['request_id'], name, value)


                    class Inventories(_Entity_):
                        """
                        Inventory information of install operation
                        request
                        
                        .. attribute:: inventory
                        
                        	Inventory information
                        	**type**\: list of  		 :py:class:`Inventory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Requests.Requests_.Request.Inventories.Inventory>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'installmgr-admin-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Install.SoftwareInventory.Requests.Requests_.Request.Inventories, self).__init__()

                            self.yang_name = "inventories"
                            self.yang_parent_name = "request"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("inventory", ("inventory", Install.SoftwareInventory.Requests.Requests_.Request.Inventories.Inventory))])
                            self._leafs = OrderedDict()

                            self.inventory = YList(self)
                            self._segment_path = lambda: "inventories"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Install.SoftwareInventory.Requests.Requests_.Request.Inventories, [], name, value)


                        class Inventory(_Entity_):
                            """
                            Inventory information
                            
                            .. attribute:: node_name  (key)
                            
                            	Node name
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            	**config**\: False
                            
                            .. attribute:: major
                            
                            	Major data version number
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: minor
                            
                            	Minor data version number
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: boot_image_name
                            
                            	Name of the boot image
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: node_type
                            
                            	Node's type
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: secure_domain_router_name
                            
                            	SDR name
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: load_path
                            
                            	Load path
                            	**type**\: list of  		 :py:class:`LoadPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Requests.Requests_.Request.Inventories.Inventory.LoadPath>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'installmgr-admin-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Install.SoftwareInventory.Requests.Requests_.Request.Inventories.Inventory, self).__init__()

                                self.yang_name = "inventory"
                                self.yang_parent_name = "inventories"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['node_name']
                                self._child_classes = OrderedDict([("load-path", ("load_path", Install.SoftwareInventory.Requests.Requests_.Request.Inventories.Inventory.LoadPath))])
                                self._leafs = OrderedDict([
                                    ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                                    ('major', (YLeaf(YType.uint32, 'major'), ['int'])),
                                    ('minor', (YLeaf(YType.uint32, 'minor'), ['int'])),
                                    ('boot_image_name', (YLeaf(YType.str, 'boot-image-name'), ['str'])),
                                    ('node_type', (YLeaf(YType.uint64, 'node-type'), ['int'])),
                                    ('secure_domain_router_name', (YLeaf(YType.str, 'secure-domain-router-name'), ['str'])),
                                ])
                                self.node_name = None
                                self.major = None
                                self.minor = None
                                self.boot_image_name = None
                                self.node_type = None
                                self.secure_domain_router_name = None

                                self.load_path = YList(self)
                                self._segment_path = lambda: "inventory" + "[node-name='" + str(self.node_name) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Install.SoftwareInventory.Requests.Requests_.Request.Inventories.Inventory, ['node_name', 'major', 'minor', 'boot_image_name', 'node_type', 'secure_domain_router_name'], name, value)


                            class LoadPath(_Entity_):
                                """
                                Load path
                                
                                .. attribute:: package
                                
                                	Package
                                	**type**\:  :py:class:`Package <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Requests.Requests_.Request.Inventories.Inventory.LoadPath.Package>`
                                
                                	**config**\: False
                                
                                .. attribute:: version
                                
                                	Version
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: build_information
                                
                                	Build information
                                	**type**\: str
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'installmgr-admin-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(Install.SoftwareInventory.Requests.Requests_.Request.Inventories.Inventory.LoadPath, self).__init__()

                                    self.yang_name = "load-path"
                                    self.yang_parent_name = "inventory"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("package", ("package", Install.SoftwareInventory.Requests.Requests_.Request.Inventories.Inventory.LoadPath.Package))])
                                    self._leafs = OrderedDict([
                                        ('version', (YLeaf(YType.str, 'version'), ['str'])),
                                        ('build_information', (YLeaf(YType.str, 'build-information'), ['str'])),
                                    ])
                                    self.version = None
                                    self.build_information = None

                                    self.package = Install.SoftwareInventory.Requests.Requests_.Request.Inventories.Inventory.LoadPath.Package()
                                    self.package.parent = self
                                    self._children_name_map["package"] = "package"
                                    self._segment_path = lambda: "load-path"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Install.SoftwareInventory.Requests.Requests_.Request.Inventories.Inventory.LoadPath, ['version', 'build_information'], name, value)


                                class Package(_Entity_):
                                    """
                                    Package
                                    
                                    .. attribute:: device_name
                                    
                                    	Device name
                                    	**type**\: str
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: name
                                    
                                    	Package group name
                                    	**type**\: str
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'installmgr-admin-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(Install.SoftwareInventory.Requests.Requests_.Request.Inventories.Inventory.LoadPath.Package, self).__init__()

                                        self.yang_name = "package"
                                        self.yang_parent_name = "load-path"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('device_name', (YLeaf(YType.str, 'device-name'), ['str'])),
                                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                        ])
                                        self.device_name = None
                                        self.name = None
                                        self._segment_path = lambda: "package"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Install.SoftwareInventory.Requests.Requests_.Request.Inventories.Inventory.LoadPath.Package, ['device_name', 'name'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                                        return meta._meta_table['Install.SoftwareInventory.Requests.Requests_.Request.Inventories.Inventory.LoadPath.Package']['meta_info']

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                                    return meta._meta_table['Install.SoftwareInventory.Requests.Requests_.Request.Inventories.Inventory.LoadPath']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                                return meta._meta_table['Install.SoftwareInventory.Requests.Requests_.Request.Inventories.Inventory']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                            return meta._meta_table['Install.SoftwareInventory.Requests.Requests_.Request.Inventories']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                        return meta._meta_table['Install.SoftwareInventory.Requests.Requests_.Request']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                    return meta._meta_table['Install.SoftwareInventory.Requests.Requests_']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                return meta._meta_table['Install.SoftwareInventory.Requests']['meta_info']


        class Active(_Entity_):
            """
            Active inventory information
            
            .. attribute:: summary
            
            	Summarized inventory information
            	**type**\:  :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Active.Summary>`
            
            	**config**\: False
            
            .. attribute:: inventories
            
            	Software inventory
            	**type**\:  :py:class:`Inventories <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Active.Inventories>`
            
            	**config**\: False
            
            

            """

            _prefix = 'installmgr-admin-oper'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Install.SoftwareInventory.Active, self).__init__()

                self.yang_name = "active"
                self.yang_parent_name = "software-inventory"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("summary", ("summary", Install.SoftwareInventory.Active.Summary)), ("inventories", ("inventories", Install.SoftwareInventory.Active.Inventories))])
                self._leafs = OrderedDict()

                self.summary = Install.SoftwareInventory.Active.Summary()
                self.summary.parent = self
                self._children_name_map["summary"] = "summary"

                self.inventories = Install.SoftwareInventory.Active.Inventories()
                self.inventories.parent = self
                self._children_name_map["inventories"] = "inventories"
                self._segment_path = lambda: "active"
                self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/software-inventory/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Install.SoftwareInventory.Active, [], name, value)


            class Summary(_Entity_):
                """
                Summarized inventory information
                
                .. attribute:: default_load_path
                
                	Default load path
                	**type**\:  :py:class:`DefaultLoadPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Active.Summary.DefaultLoadPath>`
                
                	**config**\: False
                
                .. attribute:: admin_load_path
                
                	Admin Resources load path
                	**type**\:  :py:class:`AdminLoadPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Active.Summary.AdminLoadPath>`
                
                	**config**\: False
                
                .. attribute:: sdr_load_path
                
                	SDR load paths
                	**type**\: list of  		 :py:class:`SdrLoadPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Active.Summary.SdrLoadPath>`
                
                	**config**\: False
                
                .. attribute:: location_load_path
                
                	Location load paths
                	**type**\: list of  		 :py:class:`LocationLoadPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Active.Summary.LocationLoadPath>`
                
                	**config**\: False
                
                

                """

                _prefix = 'installmgr-admin-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Install.SoftwareInventory.Active.Summary, self).__init__()

                    self.yang_name = "summary"
                    self.yang_parent_name = "active"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("default-load-path", ("default_load_path", Install.SoftwareInventory.Active.Summary.DefaultLoadPath)), ("admin-load-path", ("admin_load_path", Install.SoftwareInventory.Active.Summary.AdminLoadPath)), ("sdr-load-path", ("sdr_load_path", Install.SoftwareInventory.Active.Summary.SdrLoadPath)), ("location-load-path", ("location_load_path", Install.SoftwareInventory.Active.Summary.LocationLoadPath))])
                    self._leafs = OrderedDict()

                    self.default_load_path = Install.SoftwareInventory.Active.Summary.DefaultLoadPath()
                    self.default_load_path.parent = self
                    self._children_name_map["default_load_path"] = "default-load-path"

                    self.admin_load_path = Install.SoftwareInventory.Active.Summary.AdminLoadPath()
                    self.admin_load_path.parent = self
                    self._children_name_map["admin_load_path"] = "admin-load-path"

                    self.sdr_load_path = YList(self)
                    self.location_load_path = YList(self)
                    self._segment_path = lambda: "summary"
                    self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/software-inventory/active/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Install.SoftwareInventory.Active.Summary, [], name, value)


                class DefaultLoadPath(_Entity_):
                    """
                    Default load path
                    
                    .. attribute:: request_id
                    
                    	Install op affecting scope
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: admin_match
                    
                    	Does this match the Admin Resources load path?
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: secure_domain_router_name
                    
                    	Names of SDRs this applies to
                    	**type**\: list of str
                    
                    	**config**\: False
                    
                    .. attribute:: load_path
                    
                    	Default load path
                    	**type**\: list of  		 :py:class:`LoadPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Active.Summary.DefaultLoadPath.LoadPath>`
                    
                    	**config**\: False
                    
                    .. attribute:: standby_load_path
                    
                    	Load paths for standby nodes
                    	**type**\: list of  		 :py:class:`StandbyLoadPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Active.Summary.DefaultLoadPath.StandbyLoadPath>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'installmgr-admin-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Install.SoftwareInventory.Active.Summary.DefaultLoadPath, self).__init__()

                        self.yang_name = "default-load-path"
                        self.yang_parent_name = "summary"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("load-path", ("load_path", Install.SoftwareInventory.Active.Summary.DefaultLoadPath.LoadPath)), ("standby-load-path", ("standby_load_path", Install.SoftwareInventory.Active.Summary.DefaultLoadPath.StandbyLoadPath))])
                        self._leafs = OrderedDict([
                            ('request_id', (YLeaf(YType.uint32, 'request-id'), ['int'])),
                            ('admin_match', (YLeaf(YType.boolean, 'admin-match'), ['bool'])),
                            ('secure_domain_router_name', (YLeafList(YType.str, 'secure-domain-router-name'), ['str'])),
                        ])
                        self.request_id = None
                        self.admin_match = None
                        self.secure_domain_router_name = []

                        self.load_path = YList(self)
                        self.standby_load_path = YList(self)
                        self._segment_path = lambda: "default-load-path"
                        self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/software-inventory/active/summary/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Install.SoftwareInventory.Active.Summary.DefaultLoadPath, ['request_id', 'admin_match', 'secure_domain_router_name'], name, value)


                    class LoadPath(_Entity_):
                        """
                        Default load path
                        
                        .. attribute:: package
                        
                        	Package
                        	**type**\:  :py:class:`Package <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Active.Summary.DefaultLoadPath.LoadPath.Package>`
                        
                        	**config**\: False
                        
                        .. attribute:: version
                        
                        	Version
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: build_information
                        
                        	Build information
                        	**type**\: str
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'installmgr-admin-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Install.SoftwareInventory.Active.Summary.DefaultLoadPath.LoadPath, self).__init__()

                            self.yang_name = "load-path"
                            self.yang_parent_name = "default-load-path"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("package", ("package", Install.SoftwareInventory.Active.Summary.DefaultLoadPath.LoadPath.Package))])
                            self._leafs = OrderedDict([
                                ('version', (YLeaf(YType.str, 'version'), ['str'])),
                                ('build_information', (YLeaf(YType.str, 'build-information'), ['str'])),
                            ])
                            self.version = None
                            self.build_information = None

                            self.package = Install.SoftwareInventory.Active.Summary.DefaultLoadPath.LoadPath.Package()
                            self.package.parent = self
                            self._children_name_map["package"] = "package"
                            self._segment_path = lambda: "load-path"
                            self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/software-inventory/active/summary/default-load-path/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Install.SoftwareInventory.Active.Summary.DefaultLoadPath.LoadPath, ['version', 'build_information'], name, value)


                        class Package(_Entity_):
                            """
                            Package
                            
                            .. attribute:: device_name
                            
                            	Device name
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: name
                            
                            	Package group name
                            	**type**\: str
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'installmgr-admin-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Install.SoftwareInventory.Active.Summary.DefaultLoadPath.LoadPath.Package, self).__init__()

                                self.yang_name = "package"
                                self.yang_parent_name = "load-path"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('device_name', (YLeaf(YType.str, 'device-name'), ['str'])),
                                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                ])
                                self.device_name = None
                                self.name = None
                                self._segment_path = lambda: "package"
                                self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/software-inventory/active/summary/default-load-path/load-path/%s" % self._segment_path()
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Install.SoftwareInventory.Active.Summary.DefaultLoadPath.LoadPath.Package, ['device_name', 'name'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                                return meta._meta_table['Install.SoftwareInventory.Active.Summary.DefaultLoadPath.LoadPath.Package']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                            return meta._meta_table['Install.SoftwareInventory.Active.Summary.DefaultLoadPath.LoadPath']['meta_info']


                    class StandbyLoadPath(_Entity_):
                        """
                        Load paths for standby nodes
                        
                        .. attribute:: package
                        
                        	Package
                        	**type**\:  :py:class:`Package <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Active.Summary.DefaultLoadPath.StandbyLoadPath.Package>`
                        
                        	**config**\: False
                        
                        .. attribute:: version
                        
                        	Version
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: build_information
                        
                        	Build information
                        	**type**\: str
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'installmgr-admin-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Install.SoftwareInventory.Active.Summary.DefaultLoadPath.StandbyLoadPath, self).__init__()

                            self.yang_name = "standby-load-path"
                            self.yang_parent_name = "default-load-path"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("package", ("package", Install.SoftwareInventory.Active.Summary.DefaultLoadPath.StandbyLoadPath.Package))])
                            self._leafs = OrderedDict([
                                ('version', (YLeaf(YType.str, 'version'), ['str'])),
                                ('build_information', (YLeaf(YType.str, 'build-information'), ['str'])),
                            ])
                            self.version = None
                            self.build_information = None

                            self.package = Install.SoftwareInventory.Active.Summary.DefaultLoadPath.StandbyLoadPath.Package()
                            self.package.parent = self
                            self._children_name_map["package"] = "package"
                            self._segment_path = lambda: "standby-load-path"
                            self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/software-inventory/active/summary/default-load-path/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Install.SoftwareInventory.Active.Summary.DefaultLoadPath.StandbyLoadPath, ['version', 'build_information'], name, value)


                        class Package(_Entity_):
                            """
                            Package
                            
                            .. attribute:: device_name
                            
                            	Device name
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: name
                            
                            	Package group name
                            	**type**\: str
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'installmgr-admin-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Install.SoftwareInventory.Active.Summary.DefaultLoadPath.StandbyLoadPath.Package, self).__init__()

                                self.yang_name = "package"
                                self.yang_parent_name = "standby-load-path"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('device_name', (YLeaf(YType.str, 'device-name'), ['str'])),
                                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                ])
                                self.device_name = None
                                self.name = None
                                self._segment_path = lambda: "package"
                                self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/software-inventory/active/summary/default-load-path/standby-load-path/%s" % self._segment_path()
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Install.SoftwareInventory.Active.Summary.DefaultLoadPath.StandbyLoadPath.Package, ['device_name', 'name'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                                return meta._meta_table['Install.SoftwareInventory.Active.Summary.DefaultLoadPath.StandbyLoadPath.Package']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                            return meta._meta_table['Install.SoftwareInventory.Active.Summary.DefaultLoadPath.StandbyLoadPath']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                        return meta._meta_table['Install.SoftwareInventory.Active.Summary.DefaultLoadPath']['meta_info']


                class AdminLoadPath(_Entity_):
                    """
                    Admin Resources load path
                    
                    .. attribute:: request_id
                    
                    	Install op affecting scope
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: load_path
                    
                    	Admin Resources load path
                    	**type**\: list of  		 :py:class:`LoadPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Active.Summary.AdminLoadPath.LoadPath>`
                    
                    	**config**\: False
                    
                    .. attribute:: standby_load_path
                    
                    	Load paths for standby nodes
                    	**type**\: list of  		 :py:class:`StandbyLoadPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Active.Summary.AdminLoadPath.StandbyLoadPath>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'installmgr-admin-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Install.SoftwareInventory.Active.Summary.AdminLoadPath, self).__init__()

                        self.yang_name = "admin-load-path"
                        self.yang_parent_name = "summary"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("load-path", ("load_path", Install.SoftwareInventory.Active.Summary.AdminLoadPath.LoadPath)), ("standby-load-path", ("standby_load_path", Install.SoftwareInventory.Active.Summary.AdminLoadPath.StandbyLoadPath))])
                        self._leafs = OrderedDict([
                            ('request_id', (YLeaf(YType.uint32, 'request-id'), ['int'])),
                        ])
                        self.request_id = None

                        self.load_path = YList(self)
                        self.standby_load_path = YList(self)
                        self._segment_path = lambda: "admin-load-path"
                        self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/software-inventory/active/summary/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Install.SoftwareInventory.Active.Summary.AdminLoadPath, ['request_id'], name, value)


                    class LoadPath(_Entity_):
                        """
                        Admin Resources load path
                        
                        .. attribute:: package
                        
                        	Package
                        	**type**\:  :py:class:`Package <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Active.Summary.AdminLoadPath.LoadPath.Package>`
                        
                        	**config**\: False
                        
                        .. attribute:: version
                        
                        	Version
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: build_information
                        
                        	Build information
                        	**type**\: str
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'installmgr-admin-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Install.SoftwareInventory.Active.Summary.AdminLoadPath.LoadPath, self).__init__()

                            self.yang_name = "load-path"
                            self.yang_parent_name = "admin-load-path"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("package", ("package", Install.SoftwareInventory.Active.Summary.AdminLoadPath.LoadPath.Package))])
                            self._leafs = OrderedDict([
                                ('version', (YLeaf(YType.str, 'version'), ['str'])),
                                ('build_information', (YLeaf(YType.str, 'build-information'), ['str'])),
                            ])
                            self.version = None
                            self.build_information = None

                            self.package = Install.SoftwareInventory.Active.Summary.AdminLoadPath.LoadPath.Package()
                            self.package.parent = self
                            self._children_name_map["package"] = "package"
                            self._segment_path = lambda: "load-path"
                            self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/software-inventory/active/summary/admin-load-path/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Install.SoftwareInventory.Active.Summary.AdminLoadPath.LoadPath, ['version', 'build_information'], name, value)


                        class Package(_Entity_):
                            """
                            Package
                            
                            .. attribute:: device_name
                            
                            	Device name
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: name
                            
                            	Package group name
                            	**type**\: str
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'installmgr-admin-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Install.SoftwareInventory.Active.Summary.AdminLoadPath.LoadPath.Package, self).__init__()

                                self.yang_name = "package"
                                self.yang_parent_name = "load-path"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('device_name', (YLeaf(YType.str, 'device-name'), ['str'])),
                                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                ])
                                self.device_name = None
                                self.name = None
                                self._segment_path = lambda: "package"
                                self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/software-inventory/active/summary/admin-load-path/load-path/%s" % self._segment_path()
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Install.SoftwareInventory.Active.Summary.AdminLoadPath.LoadPath.Package, ['device_name', 'name'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                                return meta._meta_table['Install.SoftwareInventory.Active.Summary.AdminLoadPath.LoadPath.Package']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                            return meta._meta_table['Install.SoftwareInventory.Active.Summary.AdminLoadPath.LoadPath']['meta_info']


                    class StandbyLoadPath(_Entity_):
                        """
                        Load paths for standby nodes
                        
                        .. attribute:: package
                        
                        	Package
                        	**type**\:  :py:class:`Package <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Active.Summary.AdminLoadPath.StandbyLoadPath.Package>`
                        
                        	**config**\: False
                        
                        .. attribute:: version
                        
                        	Version
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: build_information
                        
                        	Build information
                        	**type**\: str
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'installmgr-admin-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Install.SoftwareInventory.Active.Summary.AdminLoadPath.StandbyLoadPath, self).__init__()

                            self.yang_name = "standby-load-path"
                            self.yang_parent_name = "admin-load-path"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("package", ("package", Install.SoftwareInventory.Active.Summary.AdminLoadPath.StandbyLoadPath.Package))])
                            self._leafs = OrderedDict([
                                ('version', (YLeaf(YType.str, 'version'), ['str'])),
                                ('build_information', (YLeaf(YType.str, 'build-information'), ['str'])),
                            ])
                            self.version = None
                            self.build_information = None

                            self.package = Install.SoftwareInventory.Active.Summary.AdminLoadPath.StandbyLoadPath.Package()
                            self.package.parent = self
                            self._children_name_map["package"] = "package"
                            self._segment_path = lambda: "standby-load-path"
                            self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/software-inventory/active/summary/admin-load-path/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Install.SoftwareInventory.Active.Summary.AdminLoadPath.StandbyLoadPath, ['version', 'build_information'], name, value)


                        class Package(_Entity_):
                            """
                            Package
                            
                            .. attribute:: device_name
                            
                            	Device name
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: name
                            
                            	Package group name
                            	**type**\: str
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'installmgr-admin-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Install.SoftwareInventory.Active.Summary.AdminLoadPath.StandbyLoadPath.Package, self).__init__()

                                self.yang_name = "package"
                                self.yang_parent_name = "standby-load-path"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('device_name', (YLeaf(YType.str, 'device-name'), ['str'])),
                                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                ])
                                self.device_name = None
                                self.name = None
                                self._segment_path = lambda: "package"
                                self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/software-inventory/active/summary/admin-load-path/standby-load-path/%s" % self._segment_path()
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Install.SoftwareInventory.Active.Summary.AdminLoadPath.StandbyLoadPath.Package, ['device_name', 'name'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                                return meta._meta_table['Install.SoftwareInventory.Active.Summary.AdminLoadPath.StandbyLoadPath.Package']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                            return meta._meta_table['Install.SoftwareInventory.Active.Summary.AdminLoadPath.StandbyLoadPath']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                        return meta._meta_table['Install.SoftwareInventory.Active.Summary.AdminLoadPath']['meta_info']


                class SdrLoadPath(_Entity_):
                    """
                    SDR load paths
                    
                    .. attribute:: request_id
                    
                    	Install op affecting scope
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: secure_domain_router_name
                    
                    	SDR name
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: load_path
                    
                    	Load path
                    	**type**\: list of  		 :py:class:`LoadPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Active.Summary.SdrLoadPath.LoadPath>`
                    
                    	**config**\: False
                    
                    .. attribute:: standby_load_path
                    
                    	Load paths for standby nodes
                    	**type**\: list of  		 :py:class:`StandbyLoadPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Active.Summary.SdrLoadPath.StandbyLoadPath>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'installmgr-admin-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Install.SoftwareInventory.Active.Summary.SdrLoadPath, self).__init__()

                        self.yang_name = "sdr-load-path"
                        self.yang_parent_name = "summary"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("load-path", ("load_path", Install.SoftwareInventory.Active.Summary.SdrLoadPath.LoadPath)), ("standby-load-path", ("standby_load_path", Install.SoftwareInventory.Active.Summary.SdrLoadPath.StandbyLoadPath))])
                        self._leafs = OrderedDict([
                            ('request_id', (YLeaf(YType.uint32, 'request-id'), ['int'])),
                            ('secure_domain_router_name', (YLeaf(YType.str, 'secure-domain-router-name'), ['str'])),
                        ])
                        self.request_id = None
                        self.secure_domain_router_name = None

                        self.load_path = YList(self)
                        self.standby_load_path = YList(self)
                        self._segment_path = lambda: "sdr-load-path"
                        self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/software-inventory/active/summary/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Install.SoftwareInventory.Active.Summary.SdrLoadPath, ['request_id', 'secure_domain_router_name'], name, value)


                    class LoadPath(_Entity_):
                        """
                        Load path
                        
                        .. attribute:: package
                        
                        	Package
                        	**type**\:  :py:class:`Package <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Active.Summary.SdrLoadPath.LoadPath.Package>`
                        
                        	**config**\: False
                        
                        .. attribute:: version
                        
                        	Version
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: build_information
                        
                        	Build information
                        	**type**\: str
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'installmgr-admin-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Install.SoftwareInventory.Active.Summary.SdrLoadPath.LoadPath, self).__init__()

                            self.yang_name = "load-path"
                            self.yang_parent_name = "sdr-load-path"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("package", ("package", Install.SoftwareInventory.Active.Summary.SdrLoadPath.LoadPath.Package))])
                            self._leafs = OrderedDict([
                                ('version', (YLeaf(YType.str, 'version'), ['str'])),
                                ('build_information', (YLeaf(YType.str, 'build-information'), ['str'])),
                            ])
                            self.version = None
                            self.build_information = None

                            self.package = Install.SoftwareInventory.Active.Summary.SdrLoadPath.LoadPath.Package()
                            self.package.parent = self
                            self._children_name_map["package"] = "package"
                            self._segment_path = lambda: "load-path"
                            self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/software-inventory/active/summary/sdr-load-path/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Install.SoftwareInventory.Active.Summary.SdrLoadPath.LoadPath, ['version', 'build_information'], name, value)


                        class Package(_Entity_):
                            """
                            Package
                            
                            .. attribute:: device_name
                            
                            	Device name
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: name
                            
                            	Package group name
                            	**type**\: str
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'installmgr-admin-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Install.SoftwareInventory.Active.Summary.SdrLoadPath.LoadPath.Package, self).__init__()

                                self.yang_name = "package"
                                self.yang_parent_name = "load-path"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('device_name', (YLeaf(YType.str, 'device-name'), ['str'])),
                                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                ])
                                self.device_name = None
                                self.name = None
                                self._segment_path = lambda: "package"
                                self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/software-inventory/active/summary/sdr-load-path/load-path/%s" % self._segment_path()
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Install.SoftwareInventory.Active.Summary.SdrLoadPath.LoadPath.Package, ['device_name', 'name'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                                return meta._meta_table['Install.SoftwareInventory.Active.Summary.SdrLoadPath.LoadPath.Package']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                            return meta._meta_table['Install.SoftwareInventory.Active.Summary.SdrLoadPath.LoadPath']['meta_info']


                    class StandbyLoadPath(_Entity_):
                        """
                        Load paths for standby nodes
                        
                        .. attribute:: package
                        
                        	Package
                        	**type**\:  :py:class:`Package <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Active.Summary.SdrLoadPath.StandbyLoadPath.Package>`
                        
                        	**config**\: False
                        
                        .. attribute:: version
                        
                        	Version
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: build_information
                        
                        	Build information
                        	**type**\: str
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'installmgr-admin-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Install.SoftwareInventory.Active.Summary.SdrLoadPath.StandbyLoadPath, self).__init__()

                            self.yang_name = "standby-load-path"
                            self.yang_parent_name = "sdr-load-path"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("package", ("package", Install.SoftwareInventory.Active.Summary.SdrLoadPath.StandbyLoadPath.Package))])
                            self._leafs = OrderedDict([
                                ('version', (YLeaf(YType.str, 'version'), ['str'])),
                                ('build_information', (YLeaf(YType.str, 'build-information'), ['str'])),
                            ])
                            self.version = None
                            self.build_information = None

                            self.package = Install.SoftwareInventory.Active.Summary.SdrLoadPath.StandbyLoadPath.Package()
                            self.package.parent = self
                            self._children_name_map["package"] = "package"
                            self._segment_path = lambda: "standby-load-path"
                            self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/software-inventory/active/summary/sdr-load-path/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Install.SoftwareInventory.Active.Summary.SdrLoadPath.StandbyLoadPath, ['version', 'build_information'], name, value)


                        class Package(_Entity_):
                            """
                            Package
                            
                            .. attribute:: device_name
                            
                            	Device name
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: name
                            
                            	Package group name
                            	**type**\: str
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'installmgr-admin-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Install.SoftwareInventory.Active.Summary.SdrLoadPath.StandbyLoadPath.Package, self).__init__()

                                self.yang_name = "package"
                                self.yang_parent_name = "standby-load-path"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('device_name', (YLeaf(YType.str, 'device-name'), ['str'])),
                                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                ])
                                self.device_name = None
                                self.name = None
                                self._segment_path = lambda: "package"
                                self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/software-inventory/active/summary/sdr-load-path/standby-load-path/%s" % self._segment_path()
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Install.SoftwareInventory.Active.Summary.SdrLoadPath.StandbyLoadPath.Package, ['device_name', 'name'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                                return meta._meta_table['Install.SoftwareInventory.Active.Summary.SdrLoadPath.StandbyLoadPath.Package']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                            return meta._meta_table['Install.SoftwareInventory.Active.Summary.SdrLoadPath.StandbyLoadPath']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                        return meta._meta_table['Install.SoftwareInventory.Active.Summary.SdrLoadPath']['meta_info']


                class LocationLoadPath(_Entity_):
                    """
                    Location load paths
                    
                    .. attribute:: request_id
                    
                    	Install op affecting scope
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: secure_domain_router_name
                    
                    	SDR name
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: node_name
                    
                    	Node identifier
                    	**type**\: str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    	**config**\: False
                    
                    .. attribute:: load_path
                    
                    	Load path
                    	**type**\: list of  		 :py:class:`LoadPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Active.Summary.LocationLoadPath.LoadPath>`
                    
                    	**config**\: False
                    
                    .. attribute:: standby_load_path
                    
                    	Load paths for standby nodes
                    	**type**\: list of  		 :py:class:`StandbyLoadPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Active.Summary.LocationLoadPath.StandbyLoadPath>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'installmgr-admin-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Install.SoftwareInventory.Active.Summary.LocationLoadPath, self).__init__()

                        self.yang_name = "location-load-path"
                        self.yang_parent_name = "summary"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("load-path", ("load_path", Install.SoftwareInventory.Active.Summary.LocationLoadPath.LoadPath)), ("standby-load-path", ("standby_load_path", Install.SoftwareInventory.Active.Summary.LocationLoadPath.StandbyLoadPath))])
                        self._leafs = OrderedDict([
                            ('request_id', (YLeaf(YType.uint32, 'request-id'), ['int'])),
                            ('secure_domain_router_name', (YLeaf(YType.str, 'secure-domain-router-name'), ['str'])),
                            ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                        ])
                        self.request_id = None
                        self.secure_domain_router_name = None
                        self.node_name = None

                        self.load_path = YList(self)
                        self.standby_load_path = YList(self)
                        self._segment_path = lambda: "location-load-path"
                        self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/software-inventory/active/summary/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Install.SoftwareInventory.Active.Summary.LocationLoadPath, ['request_id', 'secure_domain_router_name', 'node_name'], name, value)


                    class LoadPath(_Entity_):
                        """
                        Load path
                        
                        .. attribute:: package
                        
                        	Package
                        	**type**\:  :py:class:`Package <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Active.Summary.LocationLoadPath.LoadPath.Package>`
                        
                        	**config**\: False
                        
                        .. attribute:: version
                        
                        	Version
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: build_information
                        
                        	Build information
                        	**type**\: str
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'installmgr-admin-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Install.SoftwareInventory.Active.Summary.LocationLoadPath.LoadPath, self).__init__()

                            self.yang_name = "load-path"
                            self.yang_parent_name = "location-load-path"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("package", ("package", Install.SoftwareInventory.Active.Summary.LocationLoadPath.LoadPath.Package))])
                            self._leafs = OrderedDict([
                                ('version', (YLeaf(YType.str, 'version'), ['str'])),
                                ('build_information', (YLeaf(YType.str, 'build-information'), ['str'])),
                            ])
                            self.version = None
                            self.build_information = None

                            self.package = Install.SoftwareInventory.Active.Summary.LocationLoadPath.LoadPath.Package()
                            self.package.parent = self
                            self._children_name_map["package"] = "package"
                            self._segment_path = lambda: "load-path"
                            self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/software-inventory/active/summary/location-load-path/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Install.SoftwareInventory.Active.Summary.LocationLoadPath.LoadPath, ['version', 'build_information'], name, value)


                        class Package(_Entity_):
                            """
                            Package
                            
                            .. attribute:: device_name
                            
                            	Device name
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: name
                            
                            	Package group name
                            	**type**\: str
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'installmgr-admin-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Install.SoftwareInventory.Active.Summary.LocationLoadPath.LoadPath.Package, self).__init__()

                                self.yang_name = "package"
                                self.yang_parent_name = "load-path"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('device_name', (YLeaf(YType.str, 'device-name'), ['str'])),
                                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                ])
                                self.device_name = None
                                self.name = None
                                self._segment_path = lambda: "package"
                                self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/software-inventory/active/summary/location-load-path/load-path/%s" % self._segment_path()
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Install.SoftwareInventory.Active.Summary.LocationLoadPath.LoadPath.Package, ['device_name', 'name'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                                return meta._meta_table['Install.SoftwareInventory.Active.Summary.LocationLoadPath.LoadPath.Package']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                            return meta._meta_table['Install.SoftwareInventory.Active.Summary.LocationLoadPath.LoadPath']['meta_info']


                    class StandbyLoadPath(_Entity_):
                        """
                        Load paths for standby nodes
                        
                        .. attribute:: package
                        
                        	Package
                        	**type**\:  :py:class:`Package <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Active.Summary.LocationLoadPath.StandbyLoadPath.Package>`
                        
                        	**config**\: False
                        
                        .. attribute:: version
                        
                        	Version
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: build_information
                        
                        	Build information
                        	**type**\: str
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'installmgr-admin-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Install.SoftwareInventory.Active.Summary.LocationLoadPath.StandbyLoadPath, self).__init__()

                            self.yang_name = "standby-load-path"
                            self.yang_parent_name = "location-load-path"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("package", ("package", Install.SoftwareInventory.Active.Summary.LocationLoadPath.StandbyLoadPath.Package))])
                            self._leafs = OrderedDict([
                                ('version', (YLeaf(YType.str, 'version'), ['str'])),
                                ('build_information', (YLeaf(YType.str, 'build-information'), ['str'])),
                            ])
                            self.version = None
                            self.build_information = None

                            self.package = Install.SoftwareInventory.Active.Summary.LocationLoadPath.StandbyLoadPath.Package()
                            self.package.parent = self
                            self._children_name_map["package"] = "package"
                            self._segment_path = lambda: "standby-load-path"
                            self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/software-inventory/active/summary/location-load-path/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Install.SoftwareInventory.Active.Summary.LocationLoadPath.StandbyLoadPath, ['version', 'build_information'], name, value)


                        class Package(_Entity_):
                            """
                            Package
                            
                            .. attribute:: device_name
                            
                            	Device name
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: name
                            
                            	Package group name
                            	**type**\: str
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'installmgr-admin-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Install.SoftwareInventory.Active.Summary.LocationLoadPath.StandbyLoadPath.Package, self).__init__()

                                self.yang_name = "package"
                                self.yang_parent_name = "standby-load-path"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('device_name', (YLeaf(YType.str, 'device-name'), ['str'])),
                                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                ])
                                self.device_name = None
                                self.name = None
                                self._segment_path = lambda: "package"
                                self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/software-inventory/active/summary/location-load-path/standby-load-path/%s" % self._segment_path()
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Install.SoftwareInventory.Active.Summary.LocationLoadPath.StandbyLoadPath.Package, ['device_name', 'name'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                                return meta._meta_table['Install.SoftwareInventory.Active.Summary.LocationLoadPath.StandbyLoadPath.Package']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                            return meta._meta_table['Install.SoftwareInventory.Active.Summary.LocationLoadPath.StandbyLoadPath']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                        return meta._meta_table['Install.SoftwareInventory.Active.Summary.LocationLoadPath']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                    return meta._meta_table['Install.SoftwareInventory.Active.Summary']['meta_info']


            class Inventories(_Entity_):
                """
                Software inventory
                
                .. attribute:: inventory
                
                	Inventory information for specific node
                	**type**\: list of  		 :py:class:`Inventory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Active.Inventories.Inventory>`
                
                	**config**\: False
                
                

                """

                _prefix = 'installmgr-admin-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Install.SoftwareInventory.Active.Inventories, self).__init__()

                    self.yang_name = "inventories"
                    self.yang_parent_name = "active"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("inventory", ("inventory", Install.SoftwareInventory.Active.Inventories.Inventory))])
                    self._leafs = OrderedDict()

                    self.inventory = YList(self)
                    self._segment_path = lambda: "inventories"
                    self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/software-inventory/active/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Install.SoftwareInventory.Active.Inventories, [], name, value)


                class Inventory(_Entity_):
                    """
                    Inventory information for specific node
                    
                    .. attribute:: node_name  (key)
                    
                    	Node name
                    	**type**\: str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    	**config**\: False
                    
                    .. attribute:: major
                    
                    	Major data version number
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: minor
                    
                    	Minor data version number
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: boot_image_name
                    
                    	Name of the boot image
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: node_type
                    
                    	Node's type
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: secure_domain_router_name
                    
                    	SDR name
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: load_path
                    
                    	Load path
                    	**type**\: list of  		 :py:class:`LoadPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Active.Inventories.Inventory.LoadPath>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'installmgr-admin-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Install.SoftwareInventory.Active.Inventories.Inventory, self).__init__()

                        self.yang_name = "inventory"
                        self.yang_parent_name = "inventories"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['node_name']
                        self._child_classes = OrderedDict([("load-path", ("load_path", Install.SoftwareInventory.Active.Inventories.Inventory.LoadPath))])
                        self._leafs = OrderedDict([
                            ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                            ('major', (YLeaf(YType.uint32, 'major'), ['int'])),
                            ('minor', (YLeaf(YType.uint32, 'minor'), ['int'])),
                            ('boot_image_name', (YLeaf(YType.str, 'boot-image-name'), ['str'])),
                            ('node_type', (YLeaf(YType.uint64, 'node-type'), ['int'])),
                            ('secure_domain_router_name', (YLeaf(YType.str, 'secure-domain-router-name'), ['str'])),
                        ])
                        self.node_name = None
                        self.major = None
                        self.minor = None
                        self.boot_image_name = None
                        self.node_type = None
                        self.secure_domain_router_name = None

                        self.load_path = YList(self)
                        self._segment_path = lambda: "inventory" + "[node-name='" + str(self.node_name) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/software-inventory/active/inventories/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Install.SoftwareInventory.Active.Inventories.Inventory, ['node_name', 'major', 'minor', 'boot_image_name', 'node_type', 'secure_domain_router_name'], name, value)


                    class LoadPath(_Entity_):
                        """
                        Load path
                        
                        .. attribute:: package
                        
                        	Package
                        	**type**\:  :py:class:`Package <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Active.Inventories.Inventory.LoadPath.Package>`
                        
                        	**config**\: False
                        
                        .. attribute:: version
                        
                        	Version
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: build_information
                        
                        	Build information
                        	**type**\: str
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'installmgr-admin-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Install.SoftwareInventory.Active.Inventories.Inventory.LoadPath, self).__init__()

                            self.yang_name = "load-path"
                            self.yang_parent_name = "inventory"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("package", ("package", Install.SoftwareInventory.Active.Inventories.Inventory.LoadPath.Package))])
                            self._leafs = OrderedDict([
                                ('version', (YLeaf(YType.str, 'version'), ['str'])),
                                ('build_information', (YLeaf(YType.str, 'build-information'), ['str'])),
                            ])
                            self.version = None
                            self.build_information = None

                            self.package = Install.SoftwareInventory.Active.Inventories.Inventory.LoadPath.Package()
                            self.package.parent = self
                            self._children_name_map["package"] = "package"
                            self._segment_path = lambda: "load-path"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Install.SoftwareInventory.Active.Inventories.Inventory.LoadPath, ['version', 'build_information'], name, value)


                        class Package(_Entity_):
                            """
                            Package
                            
                            .. attribute:: device_name
                            
                            	Device name
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: name
                            
                            	Package group name
                            	**type**\: str
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'installmgr-admin-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Install.SoftwareInventory.Active.Inventories.Inventory.LoadPath.Package, self).__init__()

                                self.yang_name = "package"
                                self.yang_parent_name = "load-path"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('device_name', (YLeaf(YType.str, 'device-name'), ['str'])),
                                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                ])
                                self.device_name = None
                                self.name = None
                                self._segment_path = lambda: "package"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Install.SoftwareInventory.Active.Inventories.Inventory.LoadPath.Package, ['device_name', 'name'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                                return meta._meta_table['Install.SoftwareInventory.Active.Inventories.Inventory.LoadPath.Package']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                            return meta._meta_table['Install.SoftwareInventory.Active.Inventories.Inventory.LoadPath']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                        return meta._meta_table['Install.SoftwareInventory.Active.Inventories.Inventory']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                    return meta._meta_table['Install.SoftwareInventory.Active.Inventories']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                return meta._meta_table['Install.SoftwareInventory.Active']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
            return meta._meta_table['Install.SoftwareInventory']['meta_info']


    class Issu(_Entity_):
        """
        Information of install ISSU operations
        
        .. attribute:: card_inventories
        
        	ISSU manager card inventory table
        	**type**\:  :py:class:`CardInventories <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Issu.CardInventories>`
        
        	**config**\: False
        
        .. attribute:: stage
        
        	Summarized ISSU stage information
        	**type**\:  :py:class:`Stage <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Issu.Stage>`
        
        	**config**\: False
        
        

        """

        _prefix = 'installmgr-admin-oper'
        _revision = '2015-11-09'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Install.Issu, self).__init__()

            self.yang_name = "issu"
            self.yang_parent_name = "install"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("card-inventories", ("card_inventories", Install.Issu.CardInventories)), ("stage", ("stage", Install.Issu.Stage))])
            self._leafs = OrderedDict()

            self.card_inventories = Install.Issu.CardInventories()
            self.card_inventories.parent = self
            self._children_name_map["card_inventories"] = "card-inventories"

            self.stage = Install.Issu.Stage()
            self.stage.parent = self
            self._children_name_map["stage"] = "stage"
            self._segment_path = lambda: "issu"
            self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Install.Issu, [], name, value)


        class CardInventories(_Entity_):
            """
            ISSU manager card inventory table
            
            .. attribute:: card_inventory
            
            	ISSU manager inventory summary of the same card type
            	**type**\: list of  		 :py:class:`CardInventory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Issu.CardInventories.CardInventory>`
            
            	**config**\: False
            
            

            """

            _prefix = 'installmgr-admin-oper'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Install.Issu.CardInventories, self).__init__()

                self.yang_name = "card-inventories"
                self.yang_parent_name = "issu"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("card-inventory", ("card_inventory", Install.Issu.CardInventories.CardInventory))])
                self._leafs = OrderedDict()

                self.card_inventory = YList(self)
                self._segment_path = lambda: "card-inventories"
                self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/issu/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Install.Issu.CardInventories, [], name, value)


            class CardInventory(_Entity_):
                """
                ISSU manager inventory summary of the same
                card type
                
                .. attribute:: card_type_id  (key)
                
                	ISSU manager card type ID
                	**type**\:  :py:class:`IsmCardTypeFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.IsmCardTypeFamily>`
                
                	**config**\: False
                
                .. attribute:: summary
                
                	node state for all nodes
                	**type**\: list of  		 :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Issu.CardInventories.CardInventory.Summary>`
                
                	**config**\: False
                
                

                """

                _prefix = 'installmgr-admin-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Install.Issu.CardInventories.CardInventory, self).__init__()

                    self.yang_name = "card-inventory"
                    self.yang_parent_name = "card-inventories"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['card_type_id']
                    self._child_classes = OrderedDict([("summary", ("summary", Install.Issu.CardInventories.CardInventory.Summary))])
                    self._leafs = OrderedDict([
                        ('card_type_id', (YLeaf(YType.enumeration, 'card-type-id'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'IsmCardTypeFamily', '')])),
                    ])
                    self.card_type_id = None

                    self.summary = YList(self)
                    self._segment_path = lambda: "card-inventory" + "[card-type-id='" + str(self.card_type_id) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/issu/card-inventories/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Install.Issu.CardInventories.CardInventory, ['card_type_id'], name, value)


                class Summary(_Entity_):
                    """
                    node state for all nodes
                    
                    .. attribute:: node_name
                    
                    	Node identifier
                    	**type**\: str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    	**config**\: False
                    
                    .. attribute:: partner_node_name
                    
                    	Partner Node IDs
                    	**type**\: str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    	**config**\: False
                    
                    .. attribute:: node_state
                    
                    	Node state
                    	**type**\:  :py:class:`InstmgrCardState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.InstmgrCardState>`
                    
                    	**config**\: False
                    
                    .. attribute:: node_role
                    
                    	Node roll
                    	**type**\:  :py:class:`InstmgrNodeRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.InstmgrNodeRole>`
                    
                    	**config**\: False
                    
                    .. attribute:: node_type_pi
                    
                    	PI Node type
                    	**type**\:  :py:class:`InstmgrPiCard <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.InstmgrPiCard>`
                    
                    	**config**\: False
                    
                    .. attribute:: node_type_issu
                    
                    	ISSU node type
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: node_current_state
                    
                    	Current node ISSU state
                    	**type**\:  :py:class:`InstmgrIsmNodeState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.InstmgrIsmNodeState>`
                    
                    	**config**\: False
                    
                    .. attribute:: node_expected_state
                    
                    	Expected ISSU state
                    	**type**\:  :py:class:`InstmgrIsmNodeState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.InstmgrIsmNodeState>`
                    
                    	**config**\: False
                    
                    .. attribute:: node_failure_reason
                    
                    	Node failure reason
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: is_conforming_node
                    
                    	Node none\-cnforming
                    	**type**\:  :py:class:`InstallmgrIsmNodeConforming <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.InstallmgrIsmNodeConforming>`
                    
                    	**config**\: False
                    
                    .. attribute:: attempts
                    
                    	Number of attempts made
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: is_node_upgraded
                    
                    	Is node upgraded?
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'installmgr-admin-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Install.Issu.CardInventories.CardInventory.Summary, self).__init__()

                        self.yang_name = "summary"
                        self.yang_parent_name = "card-inventory"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                            ('partner_node_name', (YLeaf(YType.str, 'partner-node-name'), ['str'])),
                            ('node_state', (YLeaf(YType.enumeration, 'node-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'InstmgrCardState', '')])),
                            ('node_role', (YLeaf(YType.enumeration, 'node-role'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'InstmgrNodeRole', '')])),
                            ('node_type_pi', (YLeaf(YType.enumeration, 'node-type-pi'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'InstmgrPiCard', '')])),
                            ('node_type_issu', (YLeaf(YType.str, 'node-type-issu'), ['str'])),
                            ('node_current_state', (YLeaf(YType.enumeration, 'node-current-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'InstmgrIsmNodeState', '')])),
                            ('node_expected_state', (YLeaf(YType.enumeration, 'node-expected-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'InstmgrIsmNodeState', '')])),
                            ('node_failure_reason', (YLeaf(YType.str, 'node-failure-reason'), ['str'])),
                            ('is_conforming_node', (YLeaf(YType.enumeration, 'is-conforming-node'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'InstallmgrIsmNodeConforming', '')])),
                            ('attempts', (YLeaf(YType.uint32, 'attempts'), ['int'])),
                            ('is_node_upgraded', (YLeaf(YType.boolean, 'is-node-upgraded'), ['bool'])),
                        ])
                        self.node_name = None
                        self.partner_node_name = None
                        self.node_state = None
                        self.node_role = None
                        self.node_type_pi = None
                        self.node_type_issu = None
                        self.node_current_state = None
                        self.node_expected_state = None
                        self.node_failure_reason = None
                        self.is_conforming_node = None
                        self.attempts = None
                        self.is_node_upgraded = None
                        self._segment_path = lambda: "summary"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Install.Issu.CardInventories.CardInventory.Summary, ['node_name', 'partner_node_name', 'node_state', 'node_role', 'node_type_pi', 'node_type_issu', 'node_current_state', 'node_expected_state', 'node_failure_reason', 'is_conforming_node', 'attempts', 'is_node_upgraded'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                        return meta._meta_table['Install.Issu.CardInventories.CardInventory.Summary']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                    return meta._meta_table['Install.Issu.CardInventories.CardInventory']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                return meta._meta_table['Install.Issu.CardInventories']['meta_info']


        class Stage(_Entity_):
            """
            Summarized ISSU stage information
            
            .. attribute:: node_in_progress
            
            	Nodes in progress
            	**type**\:  :py:class:`NodeInProgress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Issu.Stage.NodeInProgress>`
            
            	**config**\: False
            
            .. attribute:: nodes_in_load
            
            	Node in LOAD phase
            	**type**\:  :py:class:`NodesInLoad <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Issu.Stage.NodesInLoad>`
            
            	**config**\: False
            
            .. attribute:: nodes_in_run
            
            	Node in RUN phase
            	**type**\:  :py:class:`NodesInRun <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Issu.Stage.NodesInRun>`
            
            	**config**\: False
            
            .. attribute:: nc_nodes
            
            	None\-conforming nodes
            	**type**\:  :py:class:`NcNodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Issu.Stage.NcNodes>`
            
            	**config**\: False
            
            .. attribute:: issu_state
            
            	Current ISSU state
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: issu_op_id
            
            	ISSU operational ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: percentage
            
            	ISSU progress percentage
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: percentage
            
            .. attribute:: is_issu_aborted
            
            	ISSU aborted?
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: is_issu_aborted_by_ism
            
            	ISSU aborted by ISM?
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: issu_manager_fsm_state
            
            	ISM FSM state
            	**type**\:  :py:class:`InstmgrIsmFsmState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.InstmgrIsmFsmState>`
            
            	**config**\: False
            
            .. attribute:: participating_node_all
            
            	Number of participating nodes
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: num_nodes_in_progress
            
            	Number of node in progress
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: num_of_nodes_in_load
            
            	Number of nodes in LOAD phase
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: num_of_nodes_in_run
            
            	Number of nodes in RUN phase
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: numof_nc_nodes
            
            	Number of none\-conforming nodes
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'installmgr-admin-oper'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Install.Issu.Stage, self).__init__()

                self.yang_name = "stage"
                self.yang_parent_name = "issu"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("node-in-progress", ("node_in_progress", Install.Issu.Stage.NodeInProgress)), ("nodes-in-load", ("nodes_in_load", Install.Issu.Stage.NodesInLoad)), ("nodes-in-run", ("nodes_in_run", Install.Issu.Stage.NodesInRun)), ("nc-nodes", ("nc_nodes", Install.Issu.Stage.NcNodes))])
                self._leafs = OrderedDict([
                    ('issu_state', (YLeaf(YType.str, 'issu-state'), ['str'])),
                    ('issu_op_id', (YLeaf(YType.uint32, 'issu-op-id'), ['int'])),
                    ('percentage', (YLeaf(YType.uint32, 'percentage'), ['int'])),
                    ('is_issu_aborted', (YLeaf(YType.boolean, 'is-issu-aborted'), ['bool'])),
                    ('is_issu_aborted_by_ism', (YLeaf(YType.boolean, 'is-issu-aborted-by-ism'), ['bool'])),
                    ('issu_manager_fsm_state', (YLeaf(YType.enumeration, 'issu-manager-fsm-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'InstmgrIsmFsmState', '')])),
                    ('participating_node_all', (YLeaf(YType.uint32, 'participating-node-all'), ['int'])),
                    ('num_nodes_in_progress', (YLeaf(YType.uint32, 'num-nodes-in-progress'), ['int'])),
                    ('num_of_nodes_in_load', (YLeaf(YType.uint32, 'num-of-nodes-in-load'), ['int'])),
                    ('num_of_nodes_in_run', (YLeaf(YType.uint32, 'num-of-nodes-in-run'), ['int'])),
                    ('numof_nc_nodes', (YLeaf(YType.uint32, 'numof-nc-nodes'), ['int'])),
                ])
                self.issu_state = None
                self.issu_op_id = None
                self.percentage = None
                self.is_issu_aborted = None
                self.is_issu_aborted_by_ism = None
                self.issu_manager_fsm_state = None
                self.participating_node_all = None
                self.num_nodes_in_progress = None
                self.num_of_nodes_in_load = None
                self.num_of_nodes_in_run = None
                self.numof_nc_nodes = None

                self.node_in_progress = Install.Issu.Stage.NodeInProgress()
                self.node_in_progress.parent = self
                self._children_name_map["node_in_progress"] = "node-in-progress"

                self.nodes_in_load = Install.Issu.Stage.NodesInLoad()
                self.nodes_in_load.parent = self
                self._children_name_map["nodes_in_load"] = "nodes-in-load"

                self.nodes_in_run = Install.Issu.Stage.NodesInRun()
                self.nodes_in_run.parent = self
                self._children_name_map["nodes_in_run"] = "nodes-in-run"

                self.nc_nodes = Install.Issu.Stage.NcNodes()
                self.nc_nodes.parent = self
                self._children_name_map["nc_nodes"] = "nc-nodes"
                self._segment_path = lambda: "stage"
                self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/issu/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Install.Issu.Stage, ['issu_state', 'issu_op_id', 'percentage', 'is_issu_aborted', 'is_issu_aborted_by_ism', 'issu_manager_fsm_state', 'participating_node_all', 'num_nodes_in_progress', 'num_of_nodes_in_load', 'num_of_nodes_in_run', 'numof_nc_nodes'], name, value)


            class NodeInProgress(_Entity_):
                """
                Nodes in progress
                
                .. attribute:: node
                
                	node
                	**type**\: list of str
                
                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                
                	**config**\: False
                
                

                """

                _prefix = 'installmgr-admin-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Install.Issu.Stage.NodeInProgress, self).__init__()

                    self.yang_name = "node-in-progress"
                    self.yang_parent_name = "stage"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('node', (YLeafList(YType.str, 'node'), ['str'])),
                    ])
                    self.node = []
                    self._segment_path = lambda: "node-in-progress"
                    self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/issu/stage/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Install.Issu.Stage.NodeInProgress, ['node'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                    return meta._meta_table['Install.Issu.Stage.NodeInProgress']['meta_info']


            class NodesInLoad(_Entity_):
                """
                Node in LOAD phase
                
                .. attribute:: node
                
                	node
                	**type**\: list of str
                
                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                
                	**config**\: False
                
                

                """

                _prefix = 'installmgr-admin-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Install.Issu.Stage.NodesInLoad, self).__init__()

                    self.yang_name = "nodes-in-load"
                    self.yang_parent_name = "stage"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('node', (YLeafList(YType.str, 'node'), ['str'])),
                    ])
                    self.node = []
                    self._segment_path = lambda: "nodes-in-load"
                    self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/issu/stage/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Install.Issu.Stage.NodesInLoad, ['node'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                    return meta._meta_table['Install.Issu.Stage.NodesInLoad']['meta_info']


            class NodesInRun(_Entity_):
                """
                Node in RUN phase
                
                .. attribute:: node
                
                	node
                	**type**\: list of str
                
                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                
                	**config**\: False
                
                

                """

                _prefix = 'installmgr-admin-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Install.Issu.Stage.NodesInRun, self).__init__()

                    self.yang_name = "nodes-in-run"
                    self.yang_parent_name = "stage"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('node', (YLeafList(YType.str, 'node'), ['str'])),
                    ])
                    self.node = []
                    self._segment_path = lambda: "nodes-in-run"
                    self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/issu/stage/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Install.Issu.Stage.NodesInRun, ['node'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                    return meta._meta_table['Install.Issu.Stage.NodesInRun']['meta_info']


            class NcNodes(_Entity_):
                """
                None\-conforming nodes
                
                .. attribute:: node
                
                	node
                	**type**\: list of str
                
                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                
                	**config**\: False
                
                

                """

                _prefix = 'installmgr-admin-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Install.Issu.Stage.NcNodes, self).__init__()

                    self.yang_name = "nc-nodes"
                    self.yang_parent_name = "stage"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('node', (YLeafList(YType.str, 'node'), ['str'])),
                    ])
                    self.node = []
                    self._segment_path = lambda: "nc-nodes"
                    self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/issu/stage/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Install.Issu.Stage.NcNodes, ['node'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                    return meta._meta_table['Install.Issu.Stage.NcNodes']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                return meta._meta_table['Install.Issu.Stage']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
            return meta._meta_table['Install.Issu']['meta_info']


    class BootImage(_Entity_):
        """
        System Boot Image
        
        .. attribute:: system_image_file
        
        	The boot image
        	**type**\: str
        
        	**config**\: False
        
        

        """

        _prefix = 'installmgr-admin-oper'
        _revision = '2015-11-09'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Install.BootImage, self).__init__()

            self.yang_name = "boot-image"
            self.yang_parent_name = "install"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('system_image_file', (YLeaf(YType.str, 'system-image-file'), ['str'])),
            ])
            self.system_image_file = None
            self._segment_path = lambda: "boot-image"
            self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Install.BootImage, ['system_image_file'], name, value)

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
            return meta._meta_table['Install.BootImage']['meta_info']


    class Logs(_Entity_):
        """
        Install operation log
        
        .. attribute:: log
        
        	Log information
        	**type**\: list of  		 :py:class:`Log <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Logs.Log>`
        
        	**config**\: False
        
        

        """

        _prefix = 'installmgr-admin-oper'
        _revision = '2015-11-09'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Install.Logs, self).__init__()

            self.yang_name = "logs"
            self.yang_parent_name = "install"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("log", ("log", Install.Logs.Log))])
            self._leafs = OrderedDict()

            self.log = YList(self)
            self._segment_path = lambda: "logs"
            self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Install.Logs, [], name, value)


        class Log(_Entity_):
            """
            Log information
            
            .. attribute:: request_id  (key)
            
            	Install operation request ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: header
            
            	Header information
            	**type**\: list of  		 :py:class:`Header <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Logs.Log.Header>`
            
            	**config**\: False
            
            .. attribute:: summary
            
            	Summary information
            	**type**\: list of  		 :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Logs.Log.Summary>`
            
            	**config**\: False
            
            .. attribute:: message
            
            	Status Information Logs
            	**type**\: list of  		 :py:class:`Message <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Logs.Log.Message>`
            
            	**config**\: False
            
            .. attribute:: change
            
            	Install changes
            	**type**\: list of  		 :py:class:`Change <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Logs.Log.Change>`
            
            	**config**\: False
            
            .. attribute:: detail
            
            	Install details
            	**type**\: list of  		 :py:class:`Detail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Logs.Log.Detail>`
            
            	**config**\: False
            
            .. attribute:: communication
            
            	Install communications
            	**type**\: list of  		 :py:class:`Communication <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Logs.Log.Communication>`
            
            	**config**\: False
            
            

            """

            _prefix = 'installmgr-admin-oper'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Install.Logs.Log, self).__init__()

                self.yang_name = "log"
                self.yang_parent_name = "logs"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['request_id']
                self._child_classes = OrderedDict([("header", ("header", Install.Logs.Log.Header)), ("summary", ("summary", Install.Logs.Log.Summary)), ("message", ("message", Install.Logs.Log.Message)), ("change", ("change", Install.Logs.Log.Change)), ("detail", ("detail", Install.Logs.Log.Detail)), ("communication", ("communication", Install.Logs.Log.Communication))])
                self._leafs = OrderedDict([
                    ('request_id', (YLeaf(YType.uint32, 'request-id'), ['int'])),
                ])
                self.request_id = None

                self.header = YList(self)
                self.summary = YList(self)
                self.message = YList(self)
                self.change = YList(self)
                self.detail = YList(self)
                self.communication = YList(self)
                self._segment_path = lambda: "log" + "[request-id='" + str(self.request_id) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-installmgr-admin-oper:install/logs/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Install.Logs.Log, ['request_id'], name, value)


            class Header(_Entity_):
                """
                Header information
                
                .. attribute:: log_contents
                
                	Log contents
                	**type**\:  :py:class:`LogContents <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Logs.Log.Header.LogContents>`
                
                	**config**\: False
                
                

                """

                _prefix = 'installmgr-admin-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Install.Logs.Log.Header, self).__init__()

                    self.yang_name = "header"
                    self.yang_parent_name = "log"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("log-contents", ("log_contents", Install.Logs.Log.Header.LogContents))])
                    self._leafs = OrderedDict()

                    self.log_contents = Install.Logs.Log.Header.LogContents()
                    self.log_contents.parent = self
                    self._children_name_map["log_contents"] = "log-contents"
                    self._segment_path = lambda: "header"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Install.Logs.Log.Header, [], name, value)


                class LogContents(_Entity_):
                    """
                    Log contents
                    
                    .. attribute:: v3
                    
                    	v3
                    	**type**\:  :py:class:`V3 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Logs.Log.Header.LogContents.V3>`
                    
                    	**config**\: False
                    
                    .. attribute:: version
                    
                    	Version
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'installmgr-admin-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Install.Logs.Log.Header.LogContents, self).__init__()

                        self.yang_name = "log-contents"
                        self.yang_parent_name = "header"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("v3", ("v3", Install.Logs.Log.Header.LogContents.V3))])
                        self._leafs = OrderedDict([
                            ('version', (YLeaf(YType.uint32, 'version'), ['int'])),
                        ])
                        self.version = None

                        self.v3 = Install.Logs.Log.Header.LogContents.V3()
                        self.v3.parent = self
                        self._children_name_map["v3"] = "v3"
                        self._segment_path = lambda: "log-contents"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Install.Logs.Log.Header.LogContents, ['version'], name, value)


                    class V3(_Entity_):
                        """
                        v3
                        
                        .. attribute:: scope
                        
                        	Scope of the message
                        	**type**\:  :py:class:`Scope <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Logs.Log.Header.LogContents.V3.Scope>`
                        
                        	**config**\: False
                        
                        .. attribute:: category
                        
                        	Category of the message
                        	**type**\:  :py:class:`InstmgrBagLogEntryUserMsgCategory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.InstmgrBagLogEntryUserMsgCategory>`
                        
                        	**config**\: False
                        
                        .. attribute:: message
                        
                        	Message
                        	**type**\: str
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'installmgr-admin-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Install.Logs.Log.Header.LogContents.V3, self).__init__()

                            self.yang_name = "v3"
                            self.yang_parent_name = "log-contents"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("scope", ("scope", Install.Logs.Log.Header.LogContents.V3.Scope))])
                            self._leafs = OrderedDict([
                                ('category', (YLeaf(YType.enumeration, 'category'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'InstmgrBagLogEntryUserMsgCategory', '')])),
                                ('message', (YLeaf(YType.str, 'message'), ['str'])),
                            ])
                            self.category = None
                            self.message = None

                            self.scope = Install.Logs.Log.Header.LogContents.V3.Scope()
                            self.scope.parent = self
                            self._children_name_map["scope"] = "scope"
                            self._segment_path = lambda: "v3"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Install.Logs.Log.Header.LogContents.V3, ['category', 'message'], name, value)


                        class Scope(_Entity_):
                            """
                            Scope of the message
                            
                            .. attribute:: admin_read
                            
                            	Does the admin want to read this?
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            .. attribute:: affected_sd_rs
                            
                            	Which SDRs are affected by the message
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'installmgr-admin-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Install.Logs.Log.Header.LogContents.V3.Scope, self).__init__()

                                self.yang_name = "scope"
                                self.yang_parent_name = "v3"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('admin_read', (YLeaf(YType.boolean, 'admin-read'), ['bool'])),
                                    ('affected_sd_rs', (YLeaf(YType.uint32, 'affected-sd-rs'), ['int'])),
                                ])
                                self.admin_read = None
                                self.affected_sd_rs = None
                                self._segment_path = lambda: "scope"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Install.Logs.Log.Header.LogContents.V3.Scope, ['admin_read', 'affected_sd_rs'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                                return meta._meta_table['Install.Logs.Log.Header.LogContents.V3.Scope']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                            return meta._meta_table['Install.Logs.Log.Header.LogContents.V3']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                        return meta._meta_table['Install.Logs.Log.Header.LogContents']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                    return meta._meta_table['Install.Logs.Log.Header']['meta_info']


            class Summary(_Entity_):
                """
                Summary information
                
                .. attribute:: log_contents
                
                	Log contents
                	**type**\:  :py:class:`LogContents <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Logs.Log.Summary.LogContents>`
                
                	**config**\: False
                
                

                """

                _prefix = 'installmgr-admin-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Install.Logs.Log.Summary, self).__init__()

                    self.yang_name = "summary"
                    self.yang_parent_name = "log"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("log-contents", ("log_contents", Install.Logs.Log.Summary.LogContents))])
                    self._leafs = OrderedDict()

                    self.log_contents = Install.Logs.Log.Summary.LogContents()
                    self.log_contents.parent = self
                    self._children_name_map["log_contents"] = "log-contents"
                    self._segment_path = lambda: "summary"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Install.Logs.Log.Summary, [], name, value)


                class LogContents(_Entity_):
                    """
                    Log contents
                    
                    .. attribute:: v3
                    
                    	v3
                    	**type**\:  :py:class:`V3 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Logs.Log.Summary.LogContents.V3>`
                    
                    	**config**\: False
                    
                    .. attribute:: version
                    
                    	Version
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'installmgr-admin-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Install.Logs.Log.Summary.LogContents, self).__init__()

                        self.yang_name = "log-contents"
                        self.yang_parent_name = "summary"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("v3", ("v3", Install.Logs.Log.Summary.LogContents.V3))])
                        self._leafs = OrderedDict([
                            ('version', (YLeaf(YType.uint32, 'version'), ['int'])),
                        ])
                        self.version = None

                        self.v3 = Install.Logs.Log.Summary.LogContents.V3()
                        self.v3.parent = self
                        self._children_name_map["v3"] = "v3"
                        self._segment_path = lambda: "log-contents"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Install.Logs.Log.Summary.LogContents, ['version'], name, value)


                    class V3(_Entity_):
                        """
                        v3
                        
                        .. attribute:: scope
                        
                        	Scope of the message
                        	**type**\:  :py:class:`Scope <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Logs.Log.Summary.LogContents.V3.Scope>`
                        
                        	**config**\: False
                        
                        .. attribute:: category
                        
                        	Category of the message
                        	**type**\:  :py:class:`InstmgrBagLogEntryUserMsgCategory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.InstmgrBagLogEntryUserMsgCategory>`
                        
                        	**config**\: False
                        
                        .. attribute:: message
                        
                        	Message
                        	**type**\: str
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'installmgr-admin-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Install.Logs.Log.Summary.LogContents.V3, self).__init__()

                            self.yang_name = "v3"
                            self.yang_parent_name = "log-contents"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("scope", ("scope", Install.Logs.Log.Summary.LogContents.V3.Scope))])
                            self._leafs = OrderedDict([
                                ('category', (YLeaf(YType.enumeration, 'category'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'InstmgrBagLogEntryUserMsgCategory', '')])),
                                ('message', (YLeaf(YType.str, 'message'), ['str'])),
                            ])
                            self.category = None
                            self.message = None

                            self.scope = Install.Logs.Log.Summary.LogContents.V3.Scope()
                            self.scope.parent = self
                            self._children_name_map["scope"] = "scope"
                            self._segment_path = lambda: "v3"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Install.Logs.Log.Summary.LogContents.V3, ['category', 'message'], name, value)


                        class Scope(_Entity_):
                            """
                            Scope of the message
                            
                            .. attribute:: admin_read
                            
                            	Does the admin want to read this?
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            .. attribute:: affected_sd_rs
                            
                            	Which SDRs are affected by the message
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'installmgr-admin-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Install.Logs.Log.Summary.LogContents.V3.Scope, self).__init__()

                                self.yang_name = "scope"
                                self.yang_parent_name = "v3"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('admin_read', (YLeaf(YType.boolean, 'admin-read'), ['bool'])),
                                    ('affected_sd_rs', (YLeaf(YType.uint32, 'affected-sd-rs'), ['int'])),
                                ])
                                self.admin_read = None
                                self.affected_sd_rs = None
                                self._segment_path = lambda: "scope"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Install.Logs.Log.Summary.LogContents.V3.Scope, ['admin_read', 'affected_sd_rs'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                                return meta._meta_table['Install.Logs.Log.Summary.LogContents.V3.Scope']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                            return meta._meta_table['Install.Logs.Log.Summary.LogContents.V3']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                        return meta._meta_table['Install.Logs.Log.Summary.LogContents']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                    return meta._meta_table['Install.Logs.Log.Summary']['meta_info']


            class Message(_Entity_):
                """
                Status Information Logs
                
                .. attribute:: log_contents
                
                	Log contents
                	**type**\:  :py:class:`LogContents <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Logs.Log.Message.LogContents>`
                
                	**config**\: False
                
                

                """

                _prefix = 'installmgr-admin-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Install.Logs.Log.Message, self).__init__()

                    self.yang_name = "message"
                    self.yang_parent_name = "log"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("log-contents", ("log_contents", Install.Logs.Log.Message.LogContents))])
                    self._leafs = OrderedDict()

                    self.log_contents = Install.Logs.Log.Message.LogContents()
                    self.log_contents.parent = self
                    self._children_name_map["log_contents"] = "log-contents"
                    self._segment_path = lambda: "message"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Install.Logs.Log.Message, [], name, value)


                class LogContents(_Entity_):
                    """
                    Log contents
                    
                    .. attribute:: v3
                    
                    	v3
                    	**type**\:  :py:class:`V3 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Logs.Log.Message.LogContents.V3>`
                    
                    	**config**\: False
                    
                    .. attribute:: version
                    
                    	Version
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'installmgr-admin-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Install.Logs.Log.Message.LogContents, self).__init__()

                        self.yang_name = "log-contents"
                        self.yang_parent_name = "message"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("v3", ("v3", Install.Logs.Log.Message.LogContents.V3))])
                        self._leafs = OrderedDict([
                            ('version', (YLeaf(YType.uint32, 'version'), ['int'])),
                        ])
                        self.version = None

                        self.v3 = Install.Logs.Log.Message.LogContents.V3()
                        self.v3.parent = self
                        self._children_name_map["v3"] = "v3"
                        self._segment_path = lambda: "log-contents"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Install.Logs.Log.Message.LogContents, ['version'], name, value)


                    class V3(_Entity_):
                        """
                        v3
                        
                        .. attribute:: scope
                        
                        	Scope of the message
                        	**type**\:  :py:class:`Scope <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Logs.Log.Message.LogContents.V3.Scope>`
                        
                        	**config**\: False
                        
                        .. attribute:: category
                        
                        	Category of the message
                        	**type**\:  :py:class:`InstmgrBagLogEntryUserMsgCategory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.InstmgrBagLogEntryUserMsgCategory>`
                        
                        	**config**\: False
                        
                        .. attribute:: message
                        
                        	Message
                        	**type**\: str
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'installmgr-admin-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Install.Logs.Log.Message.LogContents.V3, self).__init__()

                            self.yang_name = "v3"
                            self.yang_parent_name = "log-contents"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("scope", ("scope", Install.Logs.Log.Message.LogContents.V3.Scope))])
                            self._leafs = OrderedDict([
                                ('category', (YLeaf(YType.enumeration, 'category'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'InstmgrBagLogEntryUserMsgCategory', '')])),
                                ('message', (YLeaf(YType.str, 'message'), ['str'])),
                            ])
                            self.category = None
                            self.message = None

                            self.scope = Install.Logs.Log.Message.LogContents.V3.Scope()
                            self.scope.parent = self
                            self._children_name_map["scope"] = "scope"
                            self._segment_path = lambda: "v3"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Install.Logs.Log.Message.LogContents.V3, ['category', 'message'], name, value)


                        class Scope(_Entity_):
                            """
                            Scope of the message
                            
                            .. attribute:: admin_read
                            
                            	Does the admin want to read this?
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            .. attribute:: affected_sd_rs
                            
                            	Which SDRs are affected by the message
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'installmgr-admin-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Install.Logs.Log.Message.LogContents.V3.Scope, self).__init__()

                                self.yang_name = "scope"
                                self.yang_parent_name = "v3"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('admin_read', (YLeaf(YType.boolean, 'admin-read'), ['bool'])),
                                    ('affected_sd_rs', (YLeaf(YType.uint32, 'affected-sd-rs'), ['int'])),
                                ])
                                self.admin_read = None
                                self.affected_sd_rs = None
                                self._segment_path = lambda: "scope"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Install.Logs.Log.Message.LogContents.V3.Scope, ['admin_read', 'affected_sd_rs'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                                return meta._meta_table['Install.Logs.Log.Message.LogContents.V3.Scope']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                            return meta._meta_table['Install.Logs.Log.Message.LogContents.V3']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                        return meta._meta_table['Install.Logs.Log.Message.LogContents']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                    return meta._meta_table['Install.Logs.Log.Message']['meta_info']


            class Change(_Entity_):
                """
                Install changes
                
                .. attribute:: log_contents
                
                	Log contents
                	**type**\:  :py:class:`LogContents <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Logs.Log.Change.LogContents>`
                
                	**config**\: False
                
                

                """

                _prefix = 'installmgr-admin-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Install.Logs.Log.Change, self).__init__()

                    self.yang_name = "change"
                    self.yang_parent_name = "log"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("log-contents", ("log_contents", Install.Logs.Log.Change.LogContents))])
                    self._leafs = OrderedDict()

                    self.log_contents = Install.Logs.Log.Change.LogContents()
                    self.log_contents.parent = self
                    self._children_name_map["log_contents"] = "log-contents"
                    self._segment_path = lambda: "change"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Install.Logs.Log.Change, [], name, value)


                class LogContents(_Entity_):
                    """
                    Log contents
                    
                    .. attribute:: v3
                    
                    	v3
                    	**type**\:  :py:class:`V3 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Logs.Log.Change.LogContents.V3>`
                    
                    	**config**\: False
                    
                    .. attribute:: version
                    
                    	Version
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'installmgr-admin-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Install.Logs.Log.Change.LogContents, self).__init__()

                        self.yang_name = "log-contents"
                        self.yang_parent_name = "change"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("v3", ("v3", Install.Logs.Log.Change.LogContents.V3))])
                        self._leafs = OrderedDict([
                            ('version', (YLeaf(YType.uint32, 'version'), ['int'])),
                        ])
                        self.version = None

                        self.v3 = Install.Logs.Log.Change.LogContents.V3()
                        self.v3.parent = self
                        self._children_name_map["v3"] = "v3"
                        self._segment_path = lambda: "log-contents"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Install.Logs.Log.Change.LogContents, ['version'], name, value)


                    class V3(_Entity_):
                        """
                        v3
                        
                        .. attribute:: scope
                        
                        	Scope of the message
                        	**type**\:  :py:class:`Scope <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Logs.Log.Change.LogContents.V3.Scope>`
                        
                        	**config**\: False
                        
                        .. attribute:: category
                        
                        	Category of the message
                        	**type**\:  :py:class:`InstmgrBagLogEntryUserMsgCategory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.InstmgrBagLogEntryUserMsgCategory>`
                        
                        	**config**\: False
                        
                        .. attribute:: message
                        
                        	Message
                        	**type**\: str
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'installmgr-admin-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Install.Logs.Log.Change.LogContents.V3, self).__init__()

                            self.yang_name = "v3"
                            self.yang_parent_name = "log-contents"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("scope", ("scope", Install.Logs.Log.Change.LogContents.V3.Scope))])
                            self._leafs = OrderedDict([
                                ('category', (YLeaf(YType.enumeration, 'category'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'InstmgrBagLogEntryUserMsgCategory', '')])),
                                ('message', (YLeaf(YType.str, 'message'), ['str'])),
                            ])
                            self.category = None
                            self.message = None

                            self.scope = Install.Logs.Log.Change.LogContents.V3.Scope()
                            self.scope.parent = self
                            self._children_name_map["scope"] = "scope"
                            self._segment_path = lambda: "v3"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Install.Logs.Log.Change.LogContents.V3, ['category', 'message'], name, value)


                        class Scope(_Entity_):
                            """
                            Scope of the message
                            
                            .. attribute:: admin_read
                            
                            	Does the admin want to read this?
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            .. attribute:: affected_sd_rs
                            
                            	Which SDRs are affected by the message
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'installmgr-admin-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Install.Logs.Log.Change.LogContents.V3.Scope, self).__init__()

                                self.yang_name = "scope"
                                self.yang_parent_name = "v3"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('admin_read', (YLeaf(YType.boolean, 'admin-read'), ['bool'])),
                                    ('affected_sd_rs', (YLeaf(YType.uint32, 'affected-sd-rs'), ['int'])),
                                ])
                                self.admin_read = None
                                self.affected_sd_rs = None
                                self._segment_path = lambda: "scope"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Install.Logs.Log.Change.LogContents.V3.Scope, ['admin_read', 'affected_sd_rs'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                                return meta._meta_table['Install.Logs.Log.Change.LogContents.V3.Scope']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                            return meta._meta_table['Install.Logs.Log.Change.LogContents.V3']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                        return meta._meta_table['Install.Logs.Log.Change.LogContents']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                    return meta._meta_table['Install.Logs.Log.Change']['meta_info']


            class Detail(_Entity_):
                """
                Install details
                
                .. attribute:: log_contents
                
                	Log contents
                	**type**\:  :py:class:`LogContents <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Logs.Log.Detail.LogContents>`
                
                	**config**\: False
                
                

                """

                _prefix = 'installmgr-admin-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Install.Logs.Log.Detail, self).__init__()

                    self.yang_name = "detail"
                    self.yang_parent_name = "log"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("log-contents", ("log_contents", Install.Logs.Log.Detail.LogContents))])
                    self._leafs = OrderedDict()

                    self.log_contents = Install.Logs.Log.Detail.LogContents()
                    self.log_contents.parent = self
                    self._children_name_map["log_contents"] = "log-contents"
                    self._segment_path = lambda: "detail"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Install.Logs.Log.Detail, [], name, value)


                class LogContents(_Entity_):
                    """
                    Log contents
                    
                    .. attribute:: v3
                    
                    	v3
                    	**type**\:  :py:class:`V3 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Logs.Log.Detail.LogContents.V3>`
                    
                    	**config**\: False
                    
                    .. attribute:: version
                    
                    	Version
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'installmgr-admin-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Install.Logs.Log.Detail.LogContents, self).__init__()

                        self.yang_name = "log-contents"
                        self.yang_parent_name = "detail"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("v3", ("v3", Install.Logs.Log.Detail.LogContents.V3))])
                        self._leafs = OrderedDict([
                            ('version', (YLeaf(YType.uint32, 'version'), ['int'])),
                        ])
                        self.version = None

                        self.v3 = Install.Logs.Log.Detail.LogContents.V3()
                        self.v3.parent = self
                        self._children_name_map["v3"] = "v3"
                        self._segment_path = lambda: "log-contents"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Install.Logs.Log.Detail.LogContents, ['version'], name, value)


                    class V3(_Entity_):
                        """
                        v3
                        
                        .. attribute:: scope
                        
                        	Scope of the message
                        	**type**\:  :py:class:`Scope <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Logs.Log.Detail.LogContents.V3.Scope>`
                        
                        	**config**\: False
                        
                        .. attribute:: category
                        
                        	Category of the message
                        	**type**\:  :py:class:`InstmgrBagLogEntryUserMsgCategory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.InstmgrBagLogEntryUserMsgCategory>`
                        
                        	**config**\: False
                        
                        .. attribute:: message
                        
                        	Message
                        	**type**\: str
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'installmgr-admin-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Install.Logs.Log.Detail.LogContents.V3, self).__init__()

                            self.yang_name = "v3"
                            self.yang_parent_name = "log-contents"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("scope", ("scope", Install.Logs.Log.Detail.LogContents.V3.Scope))])
                            self._leafs = OrderedDict([
                                ('category', (YLeaf(YType.enumeration, 'category'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'InstmgrBagLogEntryUserMsgCategory', '')])),
                                ('message', (YLeaf(YType.str, 'message'), ['str'])),
                            ])
                            self.category = None
                            self.message = None

                            self.scope = Install.Logs.Log.Detail.LogContents.V3.Scope()
                            self.scope.parent = self
                            self._children_name_map["scope"] = "scope"
                            self._segment_path = lambda: "v3"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Install.Logs.Log.Detail.LogContents.V3, ['category', 'message'], name, value)


                        class Scope(_Entity_):
                            """
                            Scope of the message
                            
                            .. attribute:: admin_read
                            
                            	Does the admin want to read this?
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            .. attribute:: affected_sd_rs
                            
                            	Which SDRs are affected by the message
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'installmgr-admin-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Install.Logs.Log.Detail.LogContents.V3.Scope, self).__init__()

                                self.yang_name = "scope"
                                self.yang_parent_name = "v3"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('admin_read', (YLeaf(YType.boolean, 'admin-read'), ['bool'])),
                                    ('affected_sd_rs', (YLeaf(YType.uint32, 'affected-sd-rs'), ['int'])),
                                ])
                                self.admin_read = None
                                self.affected_sd_rs = None
                                self._segment_path = lambda: "scope"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Install.Logs.Log.Detail.LogContents.V3.Scope, ['admin_read', 'affected_sd_rs'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                                return meta._meta_table['Install.Logs.Log.Detail.LogContents.V3.Scope']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                            return meta._meta_table['Install.Logs.Log.Detail.LogContents.V3']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                        return meta._meta_table['Install.Logs.Log.Detail.LogContents']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                    return meta._meta_table['Install.Logs.Log.Detail']['meta_info']


            class Communication(_Entity_):
                """
                Install communications
                
                .. attribute:: log_contents
                
                	Log contents
                	**type**\:  :py:class:`LogContents <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Logs.Log.Communication.LogContents>`
                
                	**config**\: False
                
                

                """

                _prefix = 'installmgr-admin-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Install.Logs.Log.Communication, self).__init__()

                    self.yang_name = "communication"
                    self.yang_parent_name = "log"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("log-contents", ("log_contents", Install.Logs.Log.Communication.LogContents))])
                    self._leafs = OrderedDict()

                    self.log_contents = Install.Logs.Log.Communication.LogContents()
                    self.log_contents.parent = self
                    self._children_name_map["log_contents"] = "log-contents"
                    self._segment_path = lambda: "communication"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Install.Logs.Log.Communication, [], name, value)


                class LogContents(_Entity_):
                    """
                    Log contents
                    
                    .. attribute:: v3
                    
                    	v3
                    	**type**\:  :py:class:`V3 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Logs.Log.Communication.LogContents.V3>`
                    
                    	**config**\: False
                    
                    .. attribute:: version
                    
                    	Version
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'installmgr-admin-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Install.Logs.Log.Communication.LogContents, self).__init__()

                        self.yang_name = "log-contents"
                        self.yang_parent_name = "communication"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("v3", ("v3", Install.Logs.Log.Communication.LogContents.V3))])
                        self._leafs = OrderedDict([
                            ('version', (YLeaf(YType.uint32, 'version'), ['int'])),
                        ])
                        self.version = None

                        self.v3 = Install.Logs.Log.Communication.LogContents.V3()
                        self.v3.parent = self
                        self._children_name_map["v3"] = "v3"
                        self._segment_path = lambda: "log-contents"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Install.Logs.Log.Communication.LogContents, ['version'], name, value)


                    class V3(_Entity_):
                        """
                        v3
                        
                        .. attribute:: scope
                        
                        	Scope of the message
                        	**type**\:  :py:class:`Scope <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Logs.Log.Communication.LogContents.V3.Scope>`
                        
                        	**config**\: False
                        
                        .. attribute:: category
                        
                        	Category of the message
                        	**type**\:  :py:class:`InstmgrBagLogEntryUserMsgCategory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.InstmgrBagLogEntryUserMsgCategory>`
                        
                        	**config**\: False
                        
                        .. attribute:: message
                        
                        	Message
                        	**type**\: str
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'installmgr-admin-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Install.Logs.Log.Communication.LogContents.V3, self).__init__()

                            self.yang_name = "v3"
                            self.yang_parent_name = "log-contents"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("scope", ("scope", Install.Logs.Log.Communication.LogContents.V3.Scope))])
                            self._leafs = OrderedDict([
                                ('category', (YLeaf(YType.enumeration, 'category'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'InstmgrBagLogEntryUserMsgCategory', '')])),
                                ('message', (YLeaf(YType.str, 'message'), ['str'])),
                            ])
                            self.category = None
                            self.message = None

                            self.scope = Install.Logs.Log.Communication.LogContents.V3.Scope()
                            self.scope.parent = self
                            self._children_name_map["scope"] = "scope"
                            self._segment_path = lambda: "v3"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Install.Logs.Log.Communication.LogContents.V3, ['category', 'message'], name, value)


                        class Scope(_Entity_):
                            """
                            Scope of the message
                            
                            .. attribute:: admin_read
                            
                            	Does the admin want to read this?
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            .. attribute:: affected_sd_rs
                            
                            	Which SDRs are affected by the message
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'installmgr-admin-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Install.Logs.Log.Communication.LogContents.V3.Scope, self).__init__()

                                self.yang_name = "scope"
                                self.yang_parent_name = "v3"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('admin_read', (YLeaf(YType.boolean, 'admin-read'), ['bool'])),
                                    ('affected_sd_rs', (YLeaf(YType.uint32, 'affected-sd-rs'), ['int'])),
                                ])
                                self.admin_read = None
                                self.affected_sd_rs = None
                                self._segment_path = lambda: "scope"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Install.Logs.Log.Communication.LogContents.V3.Scope, ['admin_read', 'affected_sd_rs'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                                return meta._meta_table['Install.Logs.Log.Communication.LogContents.V3.Scope']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                            return meta._meta_table['Install.Logs.Log.Communication.LogContents.V3']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                        return meta._meta_table['Install.Logs.Log.Communication.LogContents']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                    return meta._meta_table['Install.Logs.Log.Communication']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                return meta._meta_table['Install.Logs.Log']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
            return meta._meta_table['Install.Logs']['meta_info']

    def clone_ptr(self):
        self._top_entity = Install()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
        return meta._meta_table['Install']['meta_info']


