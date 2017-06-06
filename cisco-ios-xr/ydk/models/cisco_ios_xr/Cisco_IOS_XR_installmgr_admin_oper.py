""" Cisco_IOS_XR_installmgr_admin_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR installmgr package
admin\-plane operational data.

This module contains definitions
for the following management objects\:
  install\: Information of software packages and install
    operations

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class InstallmgrIsmNodeConformingEnum(Enum):
    """
    InstallmgrIsmNodeConformingEnum

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

    conforming = 0

    none_conforming = 1

    upgrade_fail = 2

    none_conforming_spa = 3

    spa_upgrade_fail = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
        return meta._meta_table['InstallmgrIsmNodeConformingEnum']


class InstmgrBagAbortStateEnum(Enum):
    """
    InstmgrBagAbortStateEnum

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

    abortable = 1

    no_longer_abortable = 2

    never_abortable = 3

    already_aborted = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
        return meta._meta_table['InstmgrBagAbortStateEnum']


class InstmgrBagIiDirectionEnum(Enum):
    """
    InstmgrBagIiDirectionEnum

    The Incremental Install direction

    .. data:: not_incremental = 0

    	Not incremental install operation

    .. data:: installing = 1

    	Installing

    .. data:: unwinding = 2

    	Unwinding

    """

    not_incremental = 0

    installing = 1

    unwinding = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
        return meta._meta_table['InstmgrBagIiDirectionEnum']


class InstmgrBagIiStateEnum(Enum):
    """
    InstmgrBagIiStateEnum

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

    idle = 1

    in_progress = 2

    completed = 3

    aborted = 4

    rebooted = 5


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
        return meta._meta_table['InstmgrBagIiStateEnum']


class InstmgrBagLogEntryUserMsgCategoryEnum(Enum):
    """
    InstmgrBagLogEntryUserMsgCategoryEnum

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

    user_error = 1

    non_specific = 2

    warning = 3

    information = 4

    user_prompt = 5

    log = 6

    system_error = 7

    user_response = 8


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
        return meta._meta_table['InstmgrBagLogEntryUserMsgCategoryEnum']


class InstmgrBagRequestTriggerEnum(Enum):
    """
    InstmgrBagRequestTriggerEnum

    The trigger type of an install request

    .. data:: cli = 1

    	Request triggered by CLI

    .. data:: xr_xml = 2

    	Request triggered by XML

    """

    cli = 1

    xr_xml = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
        return meta._meta_table['InstmgrBagRequestTriggerEnum']


class InstmgrBagUserMsgCategoryEnum(Enum):
    """
    InstmgrBagUserMsgCategoryEnum

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

    user_error = 1

    non_specific = 2

    warning = 3

    information = 4

    user_prompt = 5

    log = 6

    system_error = 7

    user_response = 8


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
        return meta._meta_table['InstmgrBagUserMsgCategoryEnum']


class InstmgrCardStateEnum(Enum):
    """
    InstmgrCardStateEnum

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

    instmgr_card_not_present = 0

    instmgr_card_present = 1

    instmgr_card_reset = 2

    instmgr_card_booting = 3

    instmgr_card_mbi_booting = 4

    instmgr_card_running_mbi = 5

    instmgr_card_running_ena = 6

    instmgr_card_bring_down = 7

    instmgr_card_ena_failure = 8

    instmgr_card_f_diag_run = 9

    instmgr_card_f_diag_failure = 10

    instmgr_card_powered = 11

    instmgr_card_unpowered = 12

    instmgr_card_mdr = 13

    instmgr_card_mdr_running_mbi = 14

    instmgr_card_main_t_mode = 15

    instmgr_card_admin_down = 16

    instmgr_card_no_mon = 17

    instmgr_card_unknown = 18

    instmgr_card_failed = 19

    instmgr_card_ok = 20

    instmgr_card_missing = 21

    instmgr_card_field_diag_downloading = 22

    instmgr_card_field_diag_unmonitor = 23

    instmgr_card_fabric_field_diag_unmonitor = 24

    instmgr_card_field_diag_rp_launching = 25

    instmgr_card_field_diag_running = 26

    instmgr_card_field_diag_pass = 27

    instmgr_card_field_diag_fail = 28

    instmgr_card_field_diag_timeout = 29

    instmgr_card_disabled = 30

    instmgr_card_spa_booting = 31

    instmgr_card_not_allowed_online = 32

    instmgr_card_stopped = 33

    instmgr_card_incompatible_fw_ver = 34

    instmgr_card_fpd_hold = 35

    instmgr_card_updating_fpd = 37

    instmgr_card_num_states = 38


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
        return meta._meta_table['InstmgrCardStateEnum']


class InstmgrGroupEnum(Enum):
    """
    InstmgrGroupEnum

    Group type

    .. data:: inst_pkg_group_undefined = 0

    	Undefined grouping

    .. data:: inst_pkg_group_grouped = 1

    	Packages are grouped

    .. data:: inst_pkg_group_individual = 2

    	Packages are all individual

    """

    inst_pkg_group_undefined = 0

    inst_pkg_group_grouped = 1

    inst_pkg_group_individual = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
        return meta._meta_table['InstmgrGroupEnum']


class InstmgrInstallPhaseEnum(Enum):
    """
    InstmgrInstallPhaseEnum

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

    inst_phase_unknown = 0

    inst_phase_download = 10

    inst_phase_sw_change = 50

    inst_phase_cleaning_up = 1000


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
        return meta._meta_table['InstmgrInstallPhaseEnum']


class InstmgrIsmFsmStateEnum(Enum):
    """
    InstmgrIsmFsmStateEnum

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

    idle = 0

    init_done = 1

    load_shut = 2

    load_wait = 3

    load_stp_root_before = 4

    load_standby_root_sc_upgrade = 5

    load_standby_management_upgrade = 6

    load_stp_root_after = 7

    load_fabric_upgrade = 8

    load_management_issu_ready = 9

    load_done = 10

    run_prep = 11

    run_wait = 12

    runi_mdr_prep = 13

    runi_mdr_start = 14

    runi_mdr_complete = 15

    run_make_standby_ready = 16

    run_root_scfo = 17

    run_ndscfo = 18

    run_transient1 = 19

    run_dscfo = 20

    run_fo_complete = 21

    run_stp_root_return = 22

    runi_mdr_continue = 23

    run_am_i_ready_afteri_mdr = 24

    run_nsf_ready = 25

    run_nsf_begin = 26

    runi_mdr_done = 27

    run_management_issu_ready = 28

    run_un_shut = 29

    run_is_done = 30

    state_max = 31


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
        return meta._meta_table['InstmgrIsmFsmStateEnum']


class InstmgrIsmNodeStateEnum(Enum):
    """
    InstmgrIsmNodeStateEnum

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

    none = 0

    issu_node_gsp_ready = 1

    load_shut_done = 2

    standby_management_upgrade_done = 3

    fabric_upgrade_done = 4

    imdr_preparation_ack_received = 5

    imdr_preparation_failed = 6

    imdr_start_ack_received = 7

    imdr_start_failed = 8

    imdr_complete_ack_received = 9

    imdr_complete_failed = 10

    standby_management_ready = 11

    fo_acknowledged = 12

    fo_complete = 13

    standby_ready_after_fo = 14

    iam_ready_afteri_mdr = 15

    nsf_ready = 16

    nsf_begin_ack_received = 17

    imdr_done = 18

    unshut_done = 19

    run_done = 20

    imdr_abort_sent = 21

    imdr_abort_ack_received = 22

    imdr_abort_failed = 23

    standby_management_downgrade_done = 24

    fabric_downgrade_done = 25

    reload_during_issu = 26

    timneout = 27

    fabric_upgrade_failed = 28

    unsupported_hw = 29

    not_reachable = 30

    max = 32


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
        return meta._meta_table['InstmgrIsmNodeStateEnum']


class InstmgrIssuAbortImpactEnum(Enum):
    """
    InstmgrIssuAbortImpactEnum

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

    undefined = 0

    hitless = 1

    traffic_outage = 2

    not_applicable = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
        return meta._meta_table['InstmgrIssuAbortImpactEnum']


class InstmgrIssuAbortMethodEnum(Enum):
    """
    InstmgrIssuAbortMethodEnum

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

    method_undefined = 0

    method_no_operation = 1

    method_standby_reload = 2

    method_system_reload = 3

    method_rollback = 4

    method_not_possible = 5

    method_admin_only = 6


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
        return meta._meta_table['InstmgrIssuAbortMethodEnum']


class InstmgrNodeRoleEnum(Enum):
    """
    InstmgrNodeRoleEnum

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

    redundency_unknown = 0

    redundency_active = 1

    redundency_standby = 2

    redundency_unusable = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
        return meta._meta_table['InstmgrNodeRoleEnum']


class InstmgrPiCardEnum(Enum):
    """
    InstmgrPiCardEnum

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

    type_rp = 0

    type_drp = 1

    type_lc = 2

    type_sc = 3

    type_sp = 4

    type_other = 5


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
        return meta._meta_table['InstmgrPiCardEnum']


class InstmgrPkgEnum(Enum):
    """
    InstmgrPkgEnum

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

    inst_pkg_type_undefined = 0

    inst_pkg_type_root = 1

    inst_pkg_type_standard = 2

    inst_pkg_type_internal = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
        return meta._meta_table['InstmgrPkgEnum']


class InstmgrRequestEnum(Enum):
    """
    InstmgrRequestEnum

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

    .. data:: operation = 12

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

    add = 1

    accept = 2

    clean = 3

    activate = 4

    deactivate = 5

    commit = 6

    verify = 7

    rollback = 8

    clear_rollback = 9

    clear_log = 10

    health_check = 11

    operation = 12

    stop_timer = 13

    label = 14

    clear_label = 15

    extend = 16


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
        return meta._meta_table['InstmgrRequestEnum']


class IsmCardTypeFamilyEnum(Enum):
    """
    IsmCardTypeFamilyEnum

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

    ndsc_active_rp = 1

    ndsc_standby_rp = 2

    active_drp = 3

    standby_drp = 4

    dsc_active_rp = 5

    dsc_standby_rp = 6

    active_sc = 7

    standby_sc = 8

    root_active_sc = 9

    root_standby_sc = 10

    lc = 11

    sp = 12

    fabric_sp = 13

    spa = 14


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
        return meta._meta_table['IsmCardTypeFamilyEnum']



class Install(object):
    """
    Information of software packages and install
    operations
    
    .. attribute:: boot_image
    
    	System Boot Image
    	**type**\:   :py:class:`BootImage <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.BootImage>`
    
    .. attribute:: boot_variables
    
    	Boot variable information
    	**type**\:   :py:class:`BootVariables <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.BootVariables>`
    
    .. attribute:: configuration_registers
    
    	Configuration register (confreg) information
    	**type**\:   :py:class:`ConfigurationRegisters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.ConfigurationRegisters>`
    
    .. attribute:: issu
    
    	Information of install ISSU operations
    	**type**\:   :py:class:`Issu <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Issu>`
    
    .. attribute:: log_size
    
    	Install operation log history size
    	**type**\:  int
    
    	**range:** \-2147483648..2147483647
    
    .. attribute:: logs
    
    	Install operation log
    	**type**\:   :py:class:`Logs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Logs>`
    
    .. attribute:: request_statuses
    
    	Install operation request status
    	**type**\:   :py:class:`RequestStatuses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.RequestStatuses>`
    
    .. attribute:: software
    
    	Software package,component and alias information
    	**type**\:   :py:class:`Software <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Software>`
    
    .. attribute:: software_inventory
    
    	Information of install operations
    	**type**\:   :py:class:`SoftwareInventory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory>`
    
    

    """

    _prefix = 'installmgr-admin-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.boot_image = Install.BootImage()
        self.boot_image.parent = self
        self.boot_variables = Install.BootVariables()
        self.boot_variables.parent = self
        self.configuration_registers = Install.ConfigurationRegisters()
        self.configuration_registers.parent = self
        self.issu = Install.Issu()
        self.issu.parent = self
        self.log_size = None
        self.logs = Install.Logs()
        self.logs.parent = self
        self.request_statuses = Install.RequestStatuses()
        self.request_statuses.parent = self
        self.software = Install.Software()
        self.software.parent = self
        self.software_inventory = Install.SoftwareInventory()
        self.software_inventory.parent = self


    class ConfigurationRegisters(object):
        """
        Configuration register (confreg) information
        
        .. attribute:: configuration_register
        
        	Configuration register for specific node
        	**type**\: list of    :py:class:`ConfigurationRegister <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.ConfigurationRegisters.ConfigurationRegister>`
        
        

        """

        _prefix = 'installmgr-admin-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.configuration_register = YList()
            self.configuration_register.parent = self
            self.configuration_register.name = 'configuration_register'


        class ConfigurationRegister(object):
            """
            Configuration register for specific node
            
            .. attribute:: node_name  <key>
            
            	Node name
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: config_register
            
            	Configuration register value
            	**type**\:  str
            
            	**pattern:** [0\-9a\-fA\-F]{1,8}
            
            	**mandatory**\: True
            
            

            """

            _prefix = 'installmgr-admin-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.node_name = None
                self.config_register = None

            @property
            def _common_path(self):
                if self.node_name is None:
                    raise YPYModelError('Key property node_name is None')

                return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:configuration-registers/Cisco-IOS-XR-installmgr-admin-oper:configuration-register[Cisco-IOS-XR-installmgr-admin-oper:node-name = ' + str(self.node_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.node_name is not None:
                    return True

                if self.config_register is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                return meta._meta_table['Install.ConfigurationRegisters.ConfigurationRegister']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:configuration-registers'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.configuration_register is not None:
                for child_ref in self.configuration_register:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
            return meta._meta_table['Install.ConfigurationRegisters']['meta_info']


    class RequestStatuses(object):
        """
        Install operation request status
        
        .. attribute:: request_status
        
        	Request status Information
        	**type**\: list of    :py:class:`RequestStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.RequestStatuses.RequestStatus>`
        
        

        """

        _prefix = 'installmgr-admin-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.request_status = YList()
            self.request_status.parent = self
            self.request_status.name = 'request_status'


        class RequestStatus(object):
            """
            Request status Information
            
            .. attribute:: request_id  <key>
            
            	Install operation request ID
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: abort_state
            
            	Abort state
            	**type**\:   :py:class:`InstmgrBagAbortStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.InstmgrBagAbortStateEnum>`
            
            .. attribute:: abort_status
            
            	How the abort will occur
            	**type**\:   :py:class:`AbortStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.RequestStatuses.RequestStatus.AbortStatus>`
            
            .. attribute:: downloaded_bytes
            
            	Downloaded bytes
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: byte
            
            .. attribute:: incremental_install_information
            
            	Incremental Install information
            	**type**\:   :py:class:`IncrementalInstallInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.RequestStatuses.RequestStatus.IncrementalInstallInformation>`
            
            .. attribute:: issu_message
            
            	Messages related to ISSU operations
            	**type**\: list of    :py:class:`IssuMessage <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.RequestStatuses.RequestStatus.IssuMessage>`
            
            .. attribute:: message
            
            	Messages output to the user
            	**type**\: list of    :py:class:`Message <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.RequestStatuses.RequestStatus.Message>`
            
            .. attribute:: operation_phase
            
            	Phase of the operation
            	**type**\:   :py:class:`InstmgrInstallPhaseEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.InstmgrInstallPhaseEnum>`
            
            .. attribute:: percentage
            
            	Percentage completed
            	**type**\:  int
            
            	**range:** 0..255
            
            	**units**\: percentage
            
            .. attribute:: request_information
            
            	Requested install operation
            	**type**\:   :py:class:`RequestInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.RequestStatuses.RequestStatus.RequestInformation>`
            
            .. attribute:: unanswered_query
            
            	Whether the operation is blocked waiting for a response from the user
            	**type**\:  bool
            
            

            """

            _prefix = 'installmgr-admin-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.request_id = None
                self.abort_state = None
                self.abort_status = Install.RequestStatuses.RequestStatus.AbortStatus()
                self.abort_status.parent = self
                self.downloaded_bytes = None
                self.incremental_install_information = Install.RequestStatuses.RequestStatus.IncrementalInstallInformation()
                self.incremental_install_information.parent = self
                self.issu_message = YList()
                self.issu_message.parent = self
                self.issu_message.name = 'issu_message'
                self.message = YList()
                self.message.parent = self
                self.message.name = 'message'
                self.operation_phase = None
                self.percentage = None
                self.request_information = Install.RequestStatuses.RequestStatus.RequestInformation()
                self.request_information.parent = self
                self.unanswered_query = None


            class RequestInformation(object):
                """
                Requested install operation
                
                .. attribute:: operation_detail
                
                	Detail operation information
                	**type**\:  str
                
                .. attribute:: operation_type
                
                	Requested operation type
                	**type**\:   :py:class:`InstmgrRequestEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.InstmgrRequestEnum>`
                
                .. attribute:: request_id
                
                	Install id of operation
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: request_option
                
                	Options affecting processing of install requests
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: trigger_type
                
                	Request trigger type
                	**type**\:   :py:class:`InstmgrBagRequestTriggerEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.InstmgrBagRequestTriggerEnum>`
                
                .. attribute:: user_id
                
                	User ID that started the reqeust
                	**type**\:  str
                
                

                """

                _prefix = 'installmgr-admin-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.operation_detail = None
                    self.operation_type = None
                    self.request_id = None
                    self.request_option = None
                    self.trigger_type = None
                    self.user_id = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-installmgr-admin-oper:request-information'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.operation_detail is not None:
                        return True

                    if self.operation_type is not None:
                        return True

                    if self.request_id is not None:
                        return True

                    if self.request_option is not None:
                        return True

                    if self.trigger_type is not None:
                        return True

                    if self.user_id is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                    return meta._meta_table['Install.RequestStatuses.RequestStatus.RequestInformation']['meta_info']


            class AbortStatus(object):
                """
                How the abort will occur
                
                .. attribute:: abort_impact
                
                	Impact of abort
                	**type**\:   :py:class:`InstmgrIssuAbortImpactEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.InstmgrIssuAbortImpactEnum>`
                
                .. attribute:: abort_method
                
                	Method of abort
                	**type**\:   :py:class:`InstmgrIssuAbortMethodEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.InstmgrIssuAbortMethodEnum>`
                
                

                """

                _prefix = 'installmgr-admin-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.abort_impact = None
                    self.abort_method = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-installmgr-admin-oper:abort-status'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.abort_impact is not None:
                        return True

                    if self.abort_method is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                    return meta._meta_table['Install.RequestStatuses.RequestStatus.AbortStatus']['meta_info']


            class IncrementalInstallInformation(object):
                """
                Incremental Install information
                
                .. attribute:: direction
                
                	Install direction
                	**type**\:   :py:class:`InstmgrBagIiDirectionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.InstmgrBagIiDirectionEnum>`
                
                .. attribute:: ii_error
                
                	First error during incremental install
                	**type**\:  str
                
                .. attribute:: nodes
                
                	Participating nodes
                	**type**\: list of    :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.RequestStatuses.RequestStatus.IncrementalInstallInformation.Nodes>`
                
                

                """

                _prefix = 'installmgr-admin-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.direction = None
                    self.ii_error = None
                    self.nodes = YList()
                    self.nodes.parent = self
                    self.nodes.name = 'nodes'


                class Nodes(object):
                    """
                    Participating nodes
                    
                    .. attribute:: node_name
                    
                    	Node identifier
                    	**type**\:  str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    .. attribute:: state
                    
                    	State
                    	**type**\:   :py:class:`InstmgrBagIiStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.InstmgrBagIiStateEnum>`
                    
                    

                    """

                    _prefix = 'installmgr-admin-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.node_name = None
                        self.state = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-installmgr-admin-oper:nodes'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.node_name is not None:
                            return True

                        if self.state is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                        return meta._meta_table['Install.RequestStatuses.RequestStatus.IncrementalInstallInformation.Nodes']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-installmgr-admin-oper:incremental-install-information'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.direction is not None:
                        return True

                    if self.ii_error is not None:
                        return True

                    if self.nodes is not None:
                        for child_ref in self.nodes:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                    return meta._meta_table['Install.RequestStatuses.RequestStatus.IncrementalInstallInformation']['meta_info']


            class IssuMessage(object):
                """
                Messages related to ISSU operations
                
                .. attribute:: category
                
                	Category of the message
                	**type**\:   :py:class:`InstmgrBagUserMsgCategoryEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.InstmgrBagUserMsgCategoryEnum>`
                
                .. attribute:: message
                
                	Message
                	**type**\:  str
                
                .. attribute:: scope
                
                	Scope of the message
                	**type**\:   :py:class:`Scope <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.RequestStatuses.RequestStatus.IssuMessage.Scope>`
                
                

                """

                _prefix = 'installmgr-admin-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.category = None
                    self.message = None
                    self.scope = Install.RequestStatuses.RequestStatus.IssuMessage.Scope()
                    self.scope.parent = self


                class Scope(object):
                    """
                    Scope of the message
                    
                    .. attribute:: admin_read
                    
                    	Does the admin want to read this?
                    	**type**\:  bool
                    
                    .. attribute:: affected_sd_rs
                    
                    	Which LRs are affected by the message
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'installmgr-admin-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.admin_read = None
                        self.affected_sd_rs = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-installmgr-admin-oper:scope'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.admin_read is not None:
                            return True

                        if self.affected_sd_rs is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                        return meta._meta_table['Install.RequestStatuses.RequestStatus.IssuMessage.Scope']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-installmgr-admin-oper:issu-message'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.category is not None:
                        return True

                    if self.message is not None:
                        return True

                    if self.scope is not None and self.scope._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                    return meta._meta_table['Install.RequestStatuses.RequestStatus.IssuMessage']['meta_info']


            class Message(object):
                """
                Messages output to the user
                
                .. attribute:: category
                
                	Category of the message
                	**type**\:   :py:class:`InstmgrBagUserMsgCategoryEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.InstmgrBagUserMsgCategoryEnum>`
                
                .. attribute:: message
                
                	Message
                	**type**\:  str
                
                .. attribute:: scope
                
                	Scope of the message
                	**type**\:   :py:class:`Scope <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.RequestStatuses.RequestStatus.Message.Scope>`
                
                

                """

                _prefix = 'installmgr-admin-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.category = None
                    self.message = None
                    self.scope = Install.RequestStatuses.RequestStatus.Message.Scope()
                    self.scope.parent = self


                class Scope(object):
                    """
                    Scope of the message
                    
                    .. attribute:: admin_read
                    
                    	Does the admin want to read this?
                    	**type**\:  bool
                    
                    .. attribute:: affected_sd_rs
                    
                    	Which LRs are affected by the message
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'installmgr-admin-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.admin_read = None
                        self.affected_sd_rs = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-installmgr-admin-oper:scope'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.admin_read is not None:
                            return True

                        if self.affected_sd_rs is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                        return meta._meta_table['Install.RequestStatuses.RequestStatus.Message.Scope']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-installmgr-admin-oper:message'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.category is not None:
                        return True

                    if self.message is not None:
                        return True

                    if self.scope is not None and self.scope._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                    return meta._meta_table['Install.RequestStatuses.RequestStatus.Message']['meta_info']

            @property
            def _common_path(self):
                if self.request_id is None:
                    raise YPYModelError('Key property request_id is None')

                return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:request-statuses/Cisco-IOS-XR-installmgr-admin-oper:request-status[Cisco-IOS-XR-installmgr-admin-oper:request-id = ' + str(self.request_id) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.request_id is not None:
                    return True

                if self.abort_state is not None:
                    return True

                if self.abort_status is not None and self.abort_status._has_data():
                    return True

                if self.downloaded_bytes is not None:
                    return True

                if self.incremental_install_information is not None and self.incremental_install_information._has_data():
                    return True

                if self.issu_message is not None:
                    for child_ref in self.issu_message:
                        if child_ref._has_data():
                            return True

                if self.message is not None:
                    for child_ref in self.message:
                        if child_ref._has_data():
                            return True

                if self.operation_phase is not None:
                    return True

                if self.percentage is not None:
                    return True

                if self.request_information is not None and self.request_information._has_data():
                    return True

                if self.unanswered_query is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                return meta._meta_table['Install.RequestStatuses.RequestStatus']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:request-statuses'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.request_status is not None:
                for child_ref in self.request_status:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
            return meta._meta_table['Install.RequestStatuses']['meta_info']


    class BootVariables(object):
        """
        Boot variable information
        
        .. attribute:: boot_variable
        
        	Boot variable for specific node
        	**type**\: list of    :py:class:`BootVariable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.BootVariables.BootVariable>`
        
        

        """

        _prefix = 'installmgr-admin-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.boot_variable = YList()
            self.boot_variable.parent = self
            self.boot_variable.name = 'boot_variable'


        class BootVariable(object):
            """
            Boot variable for specific node
            
            .. attribute:: node_name  <key>
            
            	Node name
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: boot_variable
            
            	Boot variable value
            	**type**\:  str
            
            	**mandatory**\: True
            
            

            """

            _prefix = 'installmgr-admin-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.node_name = None
                self.boot_variable = None

            @property
            def _common_path(self):
                if self.node_name is None:
                    raise YPYModelError('Key property node_name is None')

                return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:boot-variables/Cisco-IOS-XR-installmgr-admin-oper:boot-variable[Cisco-IOS-XR-installmgr-admin-oper:node-name = ' + str(self.node_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.node_name is not None:
                    return True

                if self.boot_variable is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                return meta._meta_table['Install.BootVariables.BootVariable']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:boot-variables'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.boot_variable is not None:
                for child_ref in self.boot_variable:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
            return meta._meta_table['Install.BootVariables']['meta_info']


    class Software(object):
        """
        Software package,component and alias information
        
        .. attribute:: alias_devices
        
        	Package alias information
        	**type**\:   :py:class:`AliasDevices <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Software.AliasDevices>`
        
        .. attribute:: component_devices
        
        	Software component information
        	**type**\:   :py:class:`ComponentDevices <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Software.ComponentDevices>`
        
        .. attribute:: package_devices
        
        	Package information
        	**type**\:   :py:class:`PackageDevices <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Software.PackageDevices>`
        
        

        """

        _prefix = 'installmgr-admin-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.alias_devices = Install.Software.AliasDevices()
            self.alias_devices.parent = self
            self.component_devices = Install.Software.ComponentDevices()
            self.component_devices.parent = self
            self.package_devices = Install.Software.PackageDevices()
            self.package_devices.parent = self


        class AliasDevices(object):
            """
            Package alias information
            
            .. attribute:: alias_device
            
            	Package alias information for specific device
            	**type**\: list of    :py:class:`AliasDevice <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Software.AliasDevices.AliasDevice>`
            
            

            """

            _prefix = 'installmgr-admin-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.alias_device = YList()
                self.alias_device.parent = self
                self.alias_device.name = 'alias_device'


            class AliasDevice(object):
                """
                Package alias information for specific device
                
                .. attribute:: device_name  <key>
                
                	Device Name
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: aliases
                
                	alias information
                	**type**\:   :py:class:`Aliases <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Software.AliasDevices.AliasDevice.Aliases>`
                
                

                """

                _prefix = 'installmgr-admin-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.device_name = None
                    self.aliases = Install.Software.AliasDevices.AliasDevice.Aliases()
                    self.aliases.parent = self


                class Aliases(object):
                    """
                    alias information
                    
                    .. attribute:: alias
                    
                    	Aliases for specific package
                    	**type**\: list of    :py:class:`Alias <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Software.AliasDevices.AliasDevice.Aliases.Alias>`
                    
                    

                    """

                    _prefix = 'installmgr-admin-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.alias = YList()
                        self.alias.parent = self
                        self.alias.name = 'alias'


                    class Alias(object):
                        """
                        Aliases for specific package
                        
                        .. attribute:: package_name  <key>
                        
                        	Package Name
                        	**type**\:  str
                        
                        .. attribute:: alias_names
                        
                        	Alias names
                        	**type**\:  str
                        
                        	**mandatory**\: True
                        
                        

                        """

                        _prefix = 'installmgr-admin-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.package_name = None
                            self.alias_names = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.package_name is None:
                                raise YPYModelError('Key property package_name is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-installmgr-admin-oper:alias[Cisco-IOS-XR-installmgr-admin-oper:package-name = ' + str(self.package_name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.package_name is not None:
                                return True

                            if self.alias_names is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                            return meta._meta_table['Install.Software.AliasDevices.AliasDevice.Aliases.Alias']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-installmgr-admin-oper:aliases'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.alias is not None:
                            for child_ref in self.alias:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                        return meta._meta_table['Install.Software.AliasDevices.AliasDevice.Aliases']['meta_info']

                @property
                def _common_path(self):
                    if self.device_name is None:
                        raise YPYModelError('Key property device_name is None')

                    return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:software/Cisco-IOS-XR-installmgr-admin-oper:alias-devices/Cisco-IOS-XR-installmgr-admin-oper:alias-device[Cisco-IOS-XR-installmgr-admin-oper:device-name = ' + str(self.device_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.device_name is not None:
                        return True

                    if self.aliases is not None and self.aliases._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                    return meta._meta_table['Install.Software.AliasDevices.AliasDevice']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:software/Cisco-IOS-XR-installmgr-admin-oper:alias-devices'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.alias_device is not None:
                    for child_ref in self.alias_device:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                return meta._meta_table['Install.Software.AliasDevices']['meta_info']


        class PackageDevices(object):
            """
            Package information
            
            .. attribute:: package_device
            
            	Package information for specific device
            	**type**\: list of    :py:class:`PackageDevice <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Software.PackageDevices.PackageDevice>`
            
            

            """

            _prefix = 'installmgr-admin-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.package_device = YList()
                self.package_device.parent = self
                self.package_device.name = 'package_device'


            class PackageDevice(object):
                """
                Package information for specific device
                
                .. attribute:: device_name  <key>
                
                	Device Name
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: packages
                
                	Package information for specific package
                	**type**\:   :py:class:`Packages <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Software.PackageDevices.PackageDevice.Packages>`
                
                

                """

                _prefix = 'installmgr-admin-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.device_name = None
                    self.packages = Install.Software.PackageDevices.PackageDevice.Packages()
                    self.packages.parent = self


                class Packages(object):
                    """
                    Package information for specific package
                    
                    .. attribute:: package
                    
                    	Package information
                    	**type**\: list of    :py:class:`Package <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Software.PackageDevices.PackageDevice.Packages.Package>`
                    
                    

                    """

                    _prefix = 'installmgr-admin-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.package = YList()
                        self.package.parent = self
                        self.package.name = 'package'


                    class Package(object):
                        """
                        Package information
                        
                        .. attribute:: package_name  <key>
                        
                        	Package Name
                        	**type**\:  str
                        
                        .. attribute:: base
                        
                        	Identifies the base bundle that the package is for
                        	**type**\:  str
                        
                        .. attribute:: bootable
                        
                        	TRUE if package has BOOTIMAGE tag set
                        	**type**\:  bool
                        
                        .. attribute:: cards
                        
                        	Card types that the package should be installed on
                        	**type**\:  list of str
                        
                        .. attribute:: composite
                        
                        	TRUE if package is a composite package
                        	**type**\:  bool
                        
                        .. attribute:: compressed_size
                        
                        	Compressed size of package
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: date
                        
                        	Time and date that the package was built
                        	**type**\:  str
                        
                        .. attribute:: depth
                        
                        	Number of layers of parent packages
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: description
                        
                        	Description of the package
                        	**type**\:  str
                        
                        .. attribute:: group_type
                        
                        	Group type of the package
                        	**type**\:   :py:class:`InstmgrGroupEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.InstmgrGroupEnum>`
                        
                        .. attribute:: name
                        
                        	Name of the package
                        	**type**\:  str
                        
                        .. attribute:: package_type
                        
                        	Type of the package
                        	**type**\:   :py:class:`InstmgrPkgEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.InstmgrPkgEnum>`
                        
                        .. attribute:: release
                        
                        	Release that the package belongs to
                        	**type**\:  str
                        
                        .. attribute:: restart_info
                        
                        	Restart info of the package
                        	**type**\:  str
                        
                        .. attribute:: source
                        
                        	Identifies the provider of the package
                        	**type**\:  str
                        
                        .. attribute:: sub_pkg
                        
                        	Sub\-package info of the package
                        	**type**\: list of    :py:class:`SubPkg <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Software.PackageDevices.PackageDevice.Packages.Package.SubPkg>`
                        
                        .. attribute:: uncompressed_size
                        
                        	Uncompressed size of package
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: vendor
                        
                        	Information about the vendor that supplied the package
                        	**type**\:  str
                        
                        .. attribute:: version
                        
                        	Version of the package
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'installmgr-admin-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.package_name = None
                            self.base = None
                            self.bootable = None
                            self.cards = YLeafList()
                            self.cards.parent = self
                            self.cards.name = 'cards'
                            self.composite = None
                            self.compressed_size = None
                            self.date = None
                            self.depth = None
                            self.description = None
                            self.group_type = None
                            self.name = None
                            self.package_type = None
                            self.release = None
                            self.restart_info = None
                            self.source = None
                            self.sub_pkg = YList()
                            self.sub_pkg.parent = self
                            self.sub_pkg.name = 'sub_pkg'
                            self.uncompressed_size = None
                            self.vendor = None
                            self.version = None


                        class SubPkg(object):
                            """
                            Sub\-package info of the package
                            
                            .. attribute:: name
                            
                            	Name of the sub\-package
                            	**type**\:  str
                            
                            .. attribute:: node_types
                            
                            	Node types of the package
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'installmgr-admin-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.name = None
                                self.node_types = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-installmgr-admin-oper:sub-pkg'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.name is not None:
                                    return True

                                if self.node_types is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                                return meta._meta_table['Install.Software.PackageDevices.PackageDevice.Packages.Package.SubPkg']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.package_name is None:
                                raise YPYModelError('Key property package_name is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-installmgr-admin-oper:package[Cisco-IOS-XR-installmgr-admin-oper:package-name = ' + str(self.package_name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.package_name is not None:
                                return True

                            if self.base is not None:
                                return True

                            if self.bootable is not None:
                                return True

                            if self.cards is not None:
                                for child in self.cards:
                                    if child is not None:
                                        return True

                            if self.composite is not None:
                                return True

                            if self.compressed_size is not None:
                                return True

                            if self.date is not None:
                                return True

                            if self.depth is not None:
                                return True

                            if self.description is not None:
                                return True

                            if self.group_type is not None:
                                return True

                            if self.name is not None:
                                return True

                            if self.package_type is not None:
                                return True

                            if self.release is not None:
                                return True

                            if self.restart_info is not None:
                                return True

                            if self.source is not None:
                                return True

                            if self.sub_pkg is not None:
                                for child_ref in self.sub_pkg:
                                    if child_ref._has_data():
                                        return True

                            if self.uncompressed_size is not None:
                                return True

                            if self.vendor is not None:
                                return True

                            if self.version is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                            return meta._meta_table['Install.Software.PackageDevices.PackageDevice.Packages.Package']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-installmgr-admin-oper:packages'

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
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                        return meta._meta_table['Install.Software.PackageDevices.PackageDevice.Packages']['meta_info']

                @property
                def _common_path(self):
                    if self.device_name is None:
                        raise YPYModelError('Key property device_name is None')

                    return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:software/Cisco-IOS-XR-installmgr-admin-oper:package-devices/Cisco-IOS-XR-installmgr-admin-oper:package-device[Cisco-IOS-XR-installmgr-admin-oper:device-name = ' + str(self.device_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.device_name is not None:
                        return True

                    if self.packages is not None and self.packages._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                    return meta._meta_table['Install.Software.PackageDevices.PackageDevice']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:software/Cisco-IOS-XR-installmgr-admin-oper:package-devices'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.package_device is not None:
                    for child_ref in self.package_device:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                return meta._meta_table['Install.Software.PackageDevices']['meta_info']


        class ComponentDevices(object):
            """
            Software component information
            
            .. attribute:: component_device
            
            	Component information for specific device
            	**type**\: list of    :py:class:`ComponentDevice <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Software.ComponentDevices.ComponentDevice>`
            
            

            """

            _prefix = 'installmgr-admin-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.component_device = YList()
                self.component_device.parent = self
                self.component_device.name = 'component_device'


            class ComponentDevice(object):
                """
                Component information for specific device
                
                .. attribute:: device_name  <key>
                
                	Device Name
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: component_packages
                
                	Software package information
                	**type**\:   :py:class:`ComponentPackages <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Software.ComponentDevices.ComponentDevice.ComponentPackages>`
                
                

                """

                _prefix = 'installmgr-admin-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.device_name = None
                    self.component_packages = Install.Software.ComponentDevices.ComponentDevice.ComponentPackages()
                    self.component_packages.parent = self


                class ComponentPackages(object):
                    """
                    Software package information
                    
                    .. attribute:: component_package
                    
                    	Component information for specific package
                    	**type**\: list of    :py:class:`ComponentPackage <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Software.ComponentDevices.ComponentDevice.ComponentPackages.ComponentPackage>`
                    
                    

                    """

                    _prefix = 'installmgr-admin-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.component_package = YList()
                        self.component_package.parent = self
                        self.component_package.name = 'component_package'


                    class ComponentPackage(object):
                        """
                        Component information for specific package
                        
                        .. attribute:: package_name  <key>
                        
                        	Package Name
                        	**type**\:  str
                        
                        .. attribute:: component
                        
                        	Component information
                        	**type**\: list of    :py:class:`Component <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Software.ComponentDevices.ComponentDevice.ComponentPackages.ComponentPackage.Component>`
                        
                        

                        """

                        _prefix = 'installmgr-admin-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.package_name = None
                            self.component = YList()
                            self.component.parent = self
                            self.component.name = 'component'


                        class Component(object):
                            """
                            Component information
                            
                            .. attribute:: component_name  <key>
                            
                            	Component Name
                            	**type**\:  str
                            
                            .. attribute:: description
                            
                            	Description of the component
                            	**type**\:  str
                            
                            .. attribute:: files
                            
                            	The set of files belonging to the component
                            	**type**\:  list of str
                            
                            .. attribute:: name
                            
                            	Name of the component
                            	**type**\:  str
                            
                            .. attribute:: release
                            
                            	Release that the component belongs to
                            	**type**\:  str
                            
                            .. attribute:: version
                            
                            	Version of the component
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'installmgr-admin-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.component_name = None
                                self.description = None
                                self.files = YLeafList()
                                self.files.parent = self
                                self.files.name = 'files'
                                self.name = None
                                self.release = None
                                self.version = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.component_name is None:
                                    raise YPYModelError('Key property component_name is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-installmgr-admin-oper:component[Cisco-IOS-XR-installmgr-admin-oper:component-name = ' + str(self.component_name) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.component_name is not None:
                                    return True

                                if self.description is not None:
                                    return True

                                if self.files is not None:
                                    for child in self.files:
                                        if child is not None:
                                            return True

                                if self.name is not None:
                                    return True

                                if self.release is not None:
                                    return True

                                if self.version is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                                return meta._meta_table['Install.Software.ComponentDevices.ComponentDevice.ComponentPackages.ComponentPackage.Component']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.package_name is None:
                                raise YPYModelError('Key property package_name is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-installmgr-admin-oper:component-package[Cisco-IOS-XR-installmgr-admin-oper:package-name = ' + str(self.package_name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.package_name is not None:
                                return True

                            if self.component is not None:
                                for child_ref in self.component:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                            return meta._meta_table['Install.Software.ComponentDevices.ComponentDevice.ComponentPackages.ComponentPackage']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-installmgr-admin-oper:component-packages'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.component_package is not None:
                            for child_ref in self.component_package:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                        return meta._meta_table['Install.Software.ComponentDevices.ComponentDevice.ComponentPackages']['meta_info']

                @property
                def _common_path(self):
                    if self.device_name is None:
                        raise YPYModelError('Key property device_name is None')

                    return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:software/Cisco-IOS-XR-installmgr-admin-oper:component-devices/Cisco-IOS-XR-installmgr-admin-oper:component-device[Cisco-IOS-XR-installmgr-admin-oper:device-name = ' + str(self.device_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.device_name is not None:
                        return True

                    if self.component_packages is not None and self.component_packages._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                    return meta._meta_table['Install.Software.ComponentDevices.ComponentDevice']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:software/Cisco-IOS-XR-installmgr-admin-oper:component-devices'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.component_device is not None:
                    for child_ref in self.component_device:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                return meta._meta_table['Install.Software.ComponentDevices']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:software'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.alias_devices is not None and self.alias_devices._has_data():
                return True

            if self.component_devices is not None and self.component_devices._has_data():
                return True

            if self.package_devices is not None and self.package_devices._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
            return meta._meta_table['Install.Software']['meta_info']


    class SoftwareInventory(object):
        """
        Information of install operations
        
        .. attribute:: active
        
        	Active inventory information
        	**type**\:   :py:class:`Active <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Active>`
        
        .. attribute:: committed
        
        	Committed inventory information
        	**type**\:   :py:class:`Committed <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Committed>`
        
        .. attribute:: inactive
        
        	Inactive inventory information
        	**type**\:   :py:class:`Inactive <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Inactive>`
        
        .. attribute:: requests
        
        	Install operation requests
        	**type**\:   :py:class:`Requests <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Requests>`
        
        

        """

        _prefix = 'installmgr-admin-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.active = Install.SoftwareInventory.Active()
            self.active.parent = self
            self.committed = Install.SoftwareInventory.Committed()
            self.committed.parent = self
            self.inactive = Install.SoftwareInventory.Inactive()
            self.inactive.parent = self
            self.requests = Install.SoftwareInventory.Requests()
            self.requests.parent = self


        class Committed(object):
            """
            Committed inventory information
            
            .. attribute:: inventories
            
            	Software inventory
            	**type**\:   :py:class:`Inventories <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Committed.Inventories>`
            
            .. attribute:: summary
            
            	Summarized inventory information
            	**type**\:   :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Committed.Summary>`
            
            

            """

            _prefix = 'installmgr-admin-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.inventories = Install.SoftwareInventory.Committed.Inventories()
                self.inventories.parent = self
                self.summary = Install.SoftwareInventory.Committed.Summary()
                self.summary.parent = self


            class Summary(object):
                """
                Summarized inventory information
                
                .. attribute:: admin_load_path
                
                	Admin Resources load path
                	**type**\:   :py:class:`AdminLoadPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Committed.Summary.AdminLoadPath>`
                
                .. attribute:: default_load_path
                
                	Default load path
                	**type**\:   :py:class:`DefaultLoadPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Committed.Summary.DefaultLoadPath>`
                
                .. attribute:: location_load_path
                
                	Location load paths
                	**type**\: list of    :py:class:`LocationLoadPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Committed.Summary.LocationLoadPath>`
                
                .. attribute:: sdr_load_path
                
                	SDR load paths
                	**type**\: list of    :py:class:`SdrLoadPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Committed.Summary.SdrLoadPath>`
                
                

                """

                _prefix = 'installmgr-admin-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.admin_load_path = Install.SoftwareInventory.Committed.Summary.AdminLoadPath()
                    self.admin_load_path.parent = self
                    self.default_load_path = Install.SoftwareInventory.Committed.Summary.DefaultLoadPath()
                    self.default_load_path.parent = self
                    self.location_load_path = YList()
                    self.location_load_path.parent = self
                    self.location_load_path.name = 'location_load_path'
                    self.sdr_load_path = YList()
                    self.sdr_load_path.parent = self
                    self.sdr_load_path.name = 'sdr_load_path'


                class DefaultLoadPath(object):
                    """
                    Default load path
                    
                    .. attribute:: admin_match
                    
                    	Does this match the Admin Resources load path?
                    	**type**\:  bool
                    
                    .. attribute:: load_path
                    
                    	Default load path
                    	**type**\: list of    :py:class:`LoadPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Committed.Summary.DefaultLoadPath.LoadPath>`
                    
                    .. attribute:: request_id
                    
                    	Install op affecting scope
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: secure_domain_router_name
                    
                    	Names of SDRs this applies to
                    	**type**\:  list of str
                    
                    .. attribute:: standby_load_path
                    
                    	Load paths for standby nodes
                    	**type**\: list of    :py:class:`StandbyLoadPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Committed.Summary.DefaultLoadPath.StandbyLoadPath>`
                    
                    

                    """

                    _prefix = 'installmgr-admin-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.admin_match = None
                        self.load_path = YList()
                        self.load_path.parent = self
                        self.load_path.name = 'load_path'
                        self.request_id = None
                        self.secure_domain_router_name = YLeafList()
                        self.secure_domain_router_name.parent = self
                        self.secure_domain_router_name.name = 'secure_domain_router_name'
                        self.standby_load_path = YList()
                        self.standby_load_path.parent = self
                        self.standby_load_path.name = 'standby_load_path'


                    class LoadPath(object):
                        """
                        Default load path
                        
                        .. attribute:: build_information
                        
                        	Build information
                        	**type**\:  str
                        
                        .. attribute:: package
                        
                        	Package
                        	**type**\:   :py:class:`Package <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Committed.Summary.DefaultLoadPath.LoadPath.Package>`
                        
                        .. attribute:: version
                        
                        	Version
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'installmgr-admin-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.build_information = None
                            self.package = Install.SoftwareInventory.Committed.Summary.DefaultLoadPath.LoadPath.Package()
                            self.package.parent = self
                            self.version = None


                        class Package(object):
                            """
                            Package
                            
                            .. attribute:: device_name
                            
                            	Device name
                            	**type**\:  str
                            
                            .. attribute:: name
                            
                            	Package group name
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'installmgr-admin-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.device_name = None
                                self.name = None

                            @property
                            def _common_path(self):

                                return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:software-inventory/Cisco-IOS-XR-installmgr-admin-oper:committed/Cisco-IOS-XR-installmgr-admin-oper:summary/Cisco-IOS-XR-installmgr-admin-oper:default-load-path/Cisco-IOS-XR-installmgr-admin-oper:load-path/Cisco-IOS-XR-installmgr-admin-oper:package'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.device_name is not None:
                                    return True

                                if self.name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                                return meta._meta_table['Install.SoftwareInventory.Committed.Summary.DefaultLoadPath.LoadPath.Package']['meta_info']

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:software-inventory/Cisco-IOS-XR-installmgr-admin-oper:committed/Cisco-IOS-XR-installmgr-admin-oper:summary/Cisco-IOS-XR-installmgr-admin-oper:default-load-path/Cisco-IOS-XR-installmgr-admin-oper:load-path'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.build_information is not None:
                                return True

                            if self.package is not None and self.package._has_data():
                                return True

                            if self.version is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                            return meta._meta_table['Install.SoftwareInventory.Committed.Summary.DefaultLoadPath.LoadPath']['meta_info']


                    class StandbyLoadPath(object):
                        """
                        Load paths for standby nodes
                        
                        .. attribute:: build_information
                        
                        	Build information
                        	**type**\:  str
                        
                        .. attribute:: package
                        
                        	Package
                        	**type**\:   :py:class:`Package <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Committed.Summary.DefaultLoadPath.StandbyLoadPath.Package>`
                        
                        .. attribute:: version
                        
                        	Version
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'installmgr-admin-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.build_information = None
                            self.package = Install.SoftwareInventory.Committed.Summary.DefaultLoadPath.StandbyLoadPath.Package()
                            self.package.parent = self
                            self.version = None


                        class Package(object):
                            """
                            Package
                            
                            .. attribute:: device_name
                            
                            	Device name
                            	**type**\:  str
                            
                            .. attribute:: name
                            
                            	Package group name
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'installmgr-admin-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.device_name = None
                                self.name = None

                            @property
                            def _common_path(self):

                                return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:software-inventory/Cisco-IOS-XR-installmgr-admin-oper:committed/Cisco-IOS-XR-installmgr-admin-oper:summary/Cisco-IOS-XR-installmgr-admin-oper:default-load-path/Cisco-IOS-XR-installmgr-admin-oper:standby-load-path/Cisco-IOS-XR-installmgr-admin-oper:package'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.device_name is not None:
                                    return True

                                if self.name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                                return meta._meta_table['Install.SoftwareInventory.Committed.Summary.DefaultLoadPath.StandbyLoadPath.Package']['meta_info']

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:software-inventory/Cisco-IOS-XR-installmgr-admin-oper:committed/Cisco-IOS-XR-installmgr-admin-oper:summary/Cisco-IOS-XR-installmgr-admin-oper:default-load-path/Cisco-IOS-XR-installmgr-admin-oper:standby-load-path'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.build_information is not None:
                                return True

                            if self.package is not None and self.package._has_data():
                                return True

                            if self.version is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                            return meta._meta_table['Install.SoftwareInventory.Committed.Summary.DefaultLoadPath.StandbyLoadPath']['meta_info']

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:software-inventory/Cisco-IOS-XR-installmgr-admin-oper:committed/Cisco-IOS-XR-installmgr-admin-oper:summary/Cisco-IOS-XR-installmgr-admin-oper:default-load-path'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.admin_match is not None:
                            return True

                        if self.load_path is not None:
                            for child_ref in self.load_path:
                                if child_ref._has_data():
                                    return True

                        if self.request_id is not None:
                            return True

                        if self.secure_domain_router_name is not None:
                            for child in self.secure_domain_router_name:
                                if child is not None:
                                    return True

                        if self.standby_load_path is not None:
                            for child_ref in self.standby_load_path:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                        return meta._meta_table['Install.SoftwareInventory.Committed.Summary.DefaultLoadPath']['meta_info']


                class AdminLoadPath(object):
                    """
                    Admin Resources load path
                    
                    .. attribute:: load_path
                    
                    	Admin Resources load path
                    	**type**\: list of    :py:class:`LoadPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Committed.Summary.AdminLoadPath.LoadPath>`
                    
                    .. attribute:: request_id
                    
                    	Install op affecting scope
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: standby_load_path
                    
                    	Load paths for standby nodes
                    	**type**\: list of    :py:class:`StandbyLoadPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Committed.Summary.AdminLoadPath.StandbyLoadPath>`
                    
                    

                    """

                    _prefix = 'installmgr-admin-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.load_path = YList()
                        self.load_path.parent = self
                        self.load_path.name = 'load_path'
                        self.request_id = None
                        self.standby_load_path = YList()
                        self.standby_load_path.parent = self
                        self.standby_load_path.name = 'standby_load_path'


                    class LoadPath(object):
                        """
                        Admin Resources load path
                        
                        .. attribute:: build_information
                        
                        	Build information
                        	**type**\:  str
                        
                        .. attribute:: package
                        
                        	Package
                        	**type**\:   :py:class:`Package <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Committed.Summary.AdminLoadPath.LoadPath.Package>`
                        
                        .. attribute:: version
                        
                        	Version
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'installmgr-admin-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.build_information = None
                            self.package = Install.SoftwareInventory.Committed.Summary.AdminLoadPath.LoadPath.Package()
                            self.package.parent = self
                            self.version = None


                        class Package(object):
                            """
                            Package
                            
                            .. attribute:: device_name
                            
                            	Device name
                            	**type**\:  str
                            
                            .. attribute:: name
                            
                            	Package group name
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'installmgr-admin-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.device_name = None
                                self.name = None

                            @property
                            def _common_path(self):

                                return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:software-inventory/Cisco-IOS-XR-installmgr-admin-oper:committed/Cisco-IOS-XR-installmgr-admin-oper:summary/Cisco-IOS-XR-installmgr-admin-oper:admin-load-path/Cisco-IOS-XR-installmgr-admin-oper:load-path/Cisco-IOS-XR-installmgr-admin-oper:package'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.device_name is not None:
                                    return True

                                if self.name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                                return meta._meta_table['Install.SoftwareInventory.Committed.Summary.AdminLoadPath.LoadPath.Package']['meta_info']

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:software-inventory/Cisco-IOS-XR-installmgr-admin-oper:committed/Cisco-IOS-XR-installmgr-admin-oper:summary/Cisco-IOS-XR-installmgr-admin-oper:admin-load-path/Cisco-IOS-XR-installmgr-admin-oper:load-path'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.build_information is not None:
                                return True

                            if self.package is not None and self.package._has_data():
                                return True

                            if self.version is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                            return meta._meta_table['Install.SoftwareInventory.Committed.Summary.AdminLoadPath.LoadPath']['meta_info']


                    class StandbyLoadPath(object):
                        """
                        Load paths for standby nodes
                        
                        .. attribute:: build_information
                        
                        	Build information
                        	**type**\:  str
                        
                        .. attribute:: package
                        
                        	Package
                        	**type**\:   :py:class:`Package <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Committed.Summary.AdminLoadPath.StandbyLoadPath.Package>`
                        
                        .. attribute:: version
                        
                        	Version
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'installmgr-admin-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.build_information = None
                            self.package = Install.SoftwareInventory.Committed.Summary.AdminLoadPath.StandbyLoadPath.Package()
                            self.package.parent = self
                            self.version = None


                        class Package(object):
                            """
                            Package
                            
                            .. attribute:: device_name
                            
                            	Device name
                            	**type**\:  str
                            
                            .. attribute:: name
                            
                            	Package group name
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'installmgr-admin-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.device_name = None
                                self.name = None

                            @property
                            def _common_path(self):

                                return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:software-inventory/Cisco-IOS-XR-installmgr-admin-oper:committed/Cisco-IOS-XR-installmgr-admin-oper:summary/Cisco-IOS-XR-installmgr-admin-oper:admin-load-path/Cisco-IOS-XR-installmgr-admin-oper:standby-load-path/Cisco-IOS-XR-installmgr-admin-oper:package'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.device_name is not None:
                                    return True

                                if self.name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                                return meta._meta_table['Install.SoftwareInventory.Committed.Summary.AdminLoadPath.StandbyLoadPath.Package']['meta_info']

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:software-inventory/Cisco-IOS-XR-installmgr-admin-oper:committed/Cisco-IOS-XR-installmgr-admin-oper:summary/Cisco-IOS-XR-installmgr-admin-oper:admin-load-path/Cisco-IOS-XR-installmgr-admin-oper:standby-load-path'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.build_information is not None:
                                return True

                            if self.package is not None and self.package._has_data():
                                return True

                            if self.version is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                            return meta._meta_table['Install.SoftwareInventory.Committed.Summary.AdminLoadPath.StandbyLoadPath']['meta_info']

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:software-inventory/Cisco-IOS-XR-installmgr-admin-oper:committed/Cisco-IOS-XR-installmgr-admin-oper:summary/Cisco-IOS-XR-installmgr-admin-oper:admin-load-path'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.load_path is not None:
                            for child_ref in self.load_path:
                                if child_ref._has_data():
                                    return True

                        if self.request_id is not None:
                            return True

                        if self.standby_load_path is not None:
                            for child_ref in self.standby_load_path:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                        return meta._meta_table['Install.SoftwareInventory.Committed.Summary.AdminLoadPath']['meta_info']


                class SdrLoadPath(object):
                    """
                    SDR load paths
                    
                    .. attribute:: load_path
                    
                    	Load path
                    	**type**\: list of    :py:class:`LoadPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Committed.Summary.SdrLoadPath.LoadPath>`
                    
                    .. attribute:: request_id
                    
                    	Install op affecting scope
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: secure_domain_router_name
                    
                    	SDR name
                    	**type**\:  str
                    
                    .. attribute:: standby_load_path
                    
                    	Load paths for standby nodes
                    	**type**\: list of    :py:class:`StandbyLoadPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Committed.Summary.SdrLoadPath.StandbyLoadPath>`
                    
                    

                    """

                    _prefix = 'installmgr-admin-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.load_path = YList()
                        self.load_path.parent = self
                        self.load_path.name = 'load_path'
                        self.request_id = None
                        self.secure_domain_router_name = None
                        self.standby_load_path = YList()
                        self.standby_load_path.parent = self
                        self.standby_load_path.name = 'standby_load_path'


                    class LoadPath(object):
                        """
                        Load path
                        
                        .. attribute:: build_information
                        
                        	Build information
                        	**type**\:  str
                        
                        .. attribute:: package
                        
                        	Package
                        	**type**\:   :py:class:`Package <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Committed.Summary.SdrLoadPath.LoadPath.Package>`
                        
                        .. attribute:: version
                        
                        	Version
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'installmgr-admin-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.build_information = None
                            self.package = Install.SoftwareInventory.Committed.Summary.SdrLoadPath.LoadPath.Package()
                            self.package.parent = self
                            self.version = None


                        class Package(object):
                            """
                            Package
                            
                            .. attribute:: device_name
                            
                            	Device name
                            	**type**\:  str
                            
                            .. attribute:: name
                            
                            	Package group name
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'installmgr-admin-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.device_name = None
                                self.name = None

                            @property
                            def _common_path(self):

                                return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:software-inventory/Cisco-IOS-XR-installmgr-admin-oper:committed/Cisco-IOS-XR-installmgr-admin-oper:summary/Cisco-IOS-XR-installmgr-admin-oper:sdr-load-path/Cisco-IOS-XR-installmgr-admin-oper:load-path/Cisco-IOS-XR-installmgr-admin-oper:package'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.device_name is not None:
                                    return True

                                if self.name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                                return meta._meta_table['Install.SoftwareInventory.Committed.Summary.SdrLoadPath.LoadPath.Package']['meta_info']

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:software-inventory/Cisco-IOS-XR-installmgr-admin-oper:committed/Cisco-IOS-XR-installmgr-admin-oper:summary/Cisco-IOS-XR-installmgr-admin-oper:sdr-load-path/Cisco-IOS-XR-installmgr-admin-oper:load-path'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.build_information is not None:
                                return True

                            if self.package is not None and self.package._has_data():
                                return True

                            if self.version is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                            return meta._meta_table['Install.SoftwareInventory.Committed.Summary.SdrLoadPath.LoadPath']['meta_info']


                    class StandbyLoadPath(object):
                        """
                        Load paths for standby nodes
                        
                        .. attribute:: build_information
                        
                        	Build information
                        	**type**\:  str
                        
                        .. attribute:: package
                        
                        	Package
                        	**type**\:   :py:class:`Package <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Committed.Summary.SdrLoadPath.StandbyLoadPath.Package>`
                        
                        .. attribute:: version
                        
                        	Version
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'installmgr-admin-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.build_information = None
                            self.package = Install.SoftwareInventory.Committed.Summary.SdrLoadPath.StandbyLoadPath.Package()
                            self.package.parent = self
                            self.version = None


                        class Package(object):
                            """
                            Package
                            
                            .. attribute:: device_name
                            
                            	Device name
                            	**type**\:  str
                            
                            .. attribute:: name
                            
                            	Package group name
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'installmgr-admin-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.device_name = None
                                self.name = None

                            @property
                            def _common_path(self):

                                return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:software-inventory/Cisco-IOS-XR-installmgr-admin-oper:committed/Cisco-IOS-XR-installmgr-admin-oper:summary/Cisco-IOS-XR-installmgr-admin-oper:sdr-load-path/Cisco-IOS-XR-installmgr-admin-oper:standby-load-path/Cisco-IOS-XR-installmgr-admin-oper:package'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.device_name is not None:
                                    return True

                                if self.name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                                return meta._meta_table['Install.SoftwareInventory.Committed.Summary.SdrLoadPath.StandbyLoadPath.Package']['meta_info']

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:software-inventory/Cisco-IOS-XR-installmgr-admin-oper:committed/Cisco-IOS-XR-installmgr-admin-oper:summary/Cisco-IOS-XR-installmgr-admin-oper:sdr-load-path/Cisco-IOS-XR-installmgr-admin-oper:standby-load-path'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.build_information is not None:
                                return True

                            if self.package is not None and self.package._has_data():
                                return True

                            if self.version is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                            return meta._meta_table['Install.SoftwareInventory.Committed.Summary.SdrLoadPath.StandbyLoadPath']['meta_info']

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:software-inventory/Cisco-IOS-XR-installmgr-admin-oper:committed/Cisco-IOS-XR-installmgr-admin-oper:summary/Cisco-IOS-XR-installmgr-admin-oper:sdr-load-path'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.load_path is not None:
                            for child_ref in self.load_path:
                                if child_ref._has_data():
                                    return True

                        if self.request_id is not None:
                            return True

                        if self.secure_domain_router_name is not None:
                            return True

                        if self.standby_load_path is not None:
                            for child_ref in self.standby_load_path:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                        return meta._meta_table['Install.SoftwareInventory.Committed.Summary.SdrLoadPath']['meta_info']


                class LocationLoadPath(object):
                    """
                    Location load paths
                    
                    .. attribute:: load_path
                    
                    	Load path
                    	**type**\: list of    :py:class:`LoadPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Committed.Summary.LocationLoadPath.LoadPath>`
                    
                    .. attribute:: node_name
                    
                    	Node identifier
                    	**type**\:  str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    .. attribute:: request_id
                    
                    	Install op affecting scope
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: secure_domain_router_name
                    
                    	SDR name
                    	**type**\:  str
                    
                    .. attribute:: standby_load_path
                    
                    	Load paths for standby nodes
                    	**type**\: list of    :py:class:`StandbyLoadPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Committed.Summary.LocationLoadPath.StandbyLoadPath>`
                    
                    

                    """

                    _prefix = 'installmgr-admin-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.load_path = YList()
                        self.load_path.parent = self
                        self.load_path.name = 'load_path'
                        self.node_name = None
                        self.request_id = None
                        self.secure_domain_router_name = None
                        self.standby_load_path = YList()
                        self.standby_load_path.parent = self
                        self.standby_load_path.name = 'standby_load_path'


                    class LoadPath(object):
                        """
                        Load path
                        
                        .. attribute:: build_information
                        
                        	Build information
                        	**type**\:  str
                        
                        .. attribute:: package
                        
                        	Package
                        	**type**\:   :py:class:`Package <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Committed.Summary.LocationLoadPath.LoadPath.Package>`
                        
                        .. attribute:: version
                        
                        	Version
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'installmgr-admin-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.build_information = None
                            self.package = Install.SoftwareInventory.Committed.Summary.LocationLoadPath.LoadPath.Package()
                            self.package.parent = self
                            self.version = None


                        class Package(object):
                            """
                            Package
                            
                            .. attribute:: device_name
                            
                            	Device name
                            	**type**\:  str
                            
                            .. attribute:: name
                            
                            	Package group name
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'installmgr-admin-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.device_name = None
                                self.name = None

                            @property
                            def _common_path(self):

                                return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:software-inventory/Cisco-IOS-XR-installmgr-admin-oper:committed/Cisco-IOS-XR-installmgr-admin-oper:summary/Cisco-IOS-XR-installmgr-admin-oper:location-load-path/Cisco-IOS-XR-installmgr-admin-oper:load-path/Cisco-IOS-XR-installmgr-admin-oper:package'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.device_name is not None:
                                    return True

                                if self.name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                                return meta._meta_table['Install.SoftwareInventory.Committed.Summary.LocationLoadPath.LoadPath.Package']['meta_info']

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:software-inventory/Cisco-IOS-XR-installmgr-admin-oper:committed/Cisco-IOS-XR-installmgr-admin-oper:summary/Cisco-IOS-XR-installmgr-admin-oper:location-load-path/Cisco-IOS-XR-installmgr-admin-oper:load-path'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.build_information is not None:
                                return True

                            if self.package is not None and self.package._has_data():
                                return True

                            if self.version is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                            return meta._meta_table['Install.SoftwareInventory.Committed.Summary.LocationLoadPath.LoadPath']['meta_info']


                    class StandbyLoadPath(object):
                        """
                        Load paths for standby nodes
                        
                        .. attribute:: build_information
                        
                        	Build information
                        	**type**\:  str
                        
                        .. attribute:: package
                        
                        	Package
                        	**type**\:   :py:class:`Package <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Committed.Summary.LocationLoadPath.StandbyLoadPath.Package>`
                        
                        .. attribute:: version
                        
                        	Version
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'installmgr-admin-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.build_information = None
                            self.package = Install.SoftwareInventory.Committed.Summary.LocationLoadPath.StandbyLoadPath.Package()
                            self.package.parent = self
                            self.version = None


                        class Package(object):
                            """
                            Package
                            
                            .. attribute:: device_name
                            
                            	Device name
                            	**type**\:  str
                            
                            .. attribute:: name
                            
                            	Package group name
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'installmgr-admin-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.device_name = None
                                self.name = None

                            @property
                            def _common_path(self):

                                return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:software-inventory/Cisco-IOS-XR-installmgr-admin-oper:committed/Cisco-IOS-XR-installmgr-admin-oper:summary/Cisco-IOS-XR-installmgr-admin-oper:location-load-path/Cisco-IOS-XR-installmgr-admin-oper:standby-load-path/Cisco-IOS-XR-installmgr-admin-oper:package'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.device_name is not None:
                                    return True

                                if self.name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                                return meta._meta_table['Install.SoftwareInventory.Committed.Summary.LocationLoadPath.StandbyLoadPath.Package']['meta_info']

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:software-inventory/Cisco-IOS-XR-installmgr-admin-oper:committed/Cisco-IOS-XR-installmgr-admin-oper:summary/Cisco-IOS-XR-installmgr-admin-oper:location-load-path/Cisco-IOS-XR-installmgr-admin-oper:standby-load-path'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.build_information is not None:
                                return True

                            if self.package is not None and self.package._has_data():
                                return True

                            if self.version is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                            return meta._meta_table['Install.SoftwareInventory.Committed.Summary.LocationLoadPath.StandbyLoadPath']['meta_info']

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:software-inventory/Cisco-IOS-XR-installmgr-admin-oper:committed/Cisco-IOS-XR-installmgr-admin-oper:summary/Cisco-IOS-XR-installmgr-admin-oper:location-load-path'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.load_path is not None:
                            for child_ref in self.load_path:
                                if child_ref._has_data():
                                    return True

                        if self.node_name is not None:
                            return True

                        if self.request_id is not None:
                            return True

                        if self.secure_domain_router_name is not None:
                            return True

                        if self.standby_load_path is not None:
                            for child_ref in self.standby_load_path:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                        return meta._meta_table['Install.SoftwareInventory.Committed.Summary.LocationLoadPath']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:software-inventory/Cisco-IOS-XR-installmgr-admin-oper:committed/Cisco-IOS-XR-installmgr-admin-oper:summary'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.admin_load_path is not None and self.admin_load_path._has_data():
                        return True

                    if self.default_load_path is not None and self.default_load_path._has_data():
                        return True

                    if self.location_load_path is not None:
                        for child_ref in self.location_load_path:
                            if child_ref._has_data():
                                return True

                    if self.sdr_load_path is not None:
                        for child_ref in self.sdr_load_path:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                    return meta._meta_table['Install.SoftwareInventory.Committed.Summary']['meta_info']


            class Inventories(object):
                """
                Software inventory
                
                .. attribute:: inventory
                
                	Inventory information for specific node
                	**type**\: list of    :py:class:`Inventory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Committed.Inventories.Inventory>`
                
                

                """

                _prefix = 'installmgr-admin-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.inventory = YList()
                    self.inventory.parent = self
                    self.inventory.name = 'inventory'


                class Inventory(object):
                    """
                    Inventory information for specific node
                    
                    .. attribute:: node_name  <key>
                    
                    	Node name
                    	**type**\:  str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    .. attribute:: boot_image_name
                    
                    	Name of the boot image
                    	**type**\:  str
                    
                    .. attribute:: load_path
                    
                    	Load path
                    	**type**\: list of    :py:class:`LoadPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Committed.Inventories.Inventory.LoadPath>`
                    
                    .. attribute:: major
                    
                    	Major data version number
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: minor
                    
                    	Minor data version number
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: node_type
                    
                    	Node's type
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: secure_domain_router_name
                    
                    	SDR name
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'installmgr-admin-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.node_name = None
                        self.boot_image_name = None
                        self.load_path = YList()
                        self.load_path.parent = self
                        self.load_path.name = 'load_path'
                        self.major = None
                        self.minor = None
                        self.node_type = None
                        self.secure_domain_router_name = None


                    class LoadPath(object):
                        """
                        Load path
                        
                        .. attribute:: build_information
                        
                        	Build information
                        	**type**\:  str
                        
                        .. attribute:: package
                        
                        	Package
                        	**type**\:   :py:class:`Package <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Committed.Inventories.Inventory.LoadPath.Package>`
                        
                        .. attribute:: version
                        
                        	Version
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'installmgr-admin-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.build_information = None
                            self.package = Install.SoftwareInventory.Committed.Inventories.Inventory.LoadPath.Package()
                            self.package.parent = self
                            self.version = None


                        class Package(object):
                            """
                            Package
                            
                            .. attribute:: device_name
                            
                            	Device name
                            	**type**\:  str
                            
                            .. attribute:: name
                            
                            	Package group name
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'installmgr-admin-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.device_name = None
                                self.name = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-installmgr-admin-oper:package'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.device_name is not None:
                                    return True

                                if self.name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                                return meta._meta_table['Install.SoftwareInventory.Committed.Inventories.Inventory.LoadPath.Package']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-installmgr-admin-oper:load-path'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.build_information is not None:
                                return True

                            if self.package is not None and self.package._has_data():
                                return True

                            if self.version is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                            return meta._meta_table['Install.SoftwareInventory.Committed.Inventories.Inventory.LoadPath']['meta_info']

                    @property
                    def _common_path(self):
                        if self.node_name is None:
                            raise YPYModelError('Key property node_name is None')

                        return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:software-inventory/Cisco-IOS-XR-installmgr-admin-oper:committed/Cisco-IOS-XR-installmgr-admin-oper:inventories/Cisco-IOS-XR-installmgr-admin-oper:inventory[Cisco-IOS-XR-installmgr-admin-oper:node-name = ' + str(self.node_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.node_name is not None:
                            return True

                        if self.boot_image_name is not None:
                            return True

                        if self.load_path is not None:
                            for child_ref in self.load_path:
                                if child_ref._has_data():
                                    return True

                        if self.major is not None:
                            return True

                        if self.minor is not None:
                            return True

                        if self.node_type is not None:
                            return True

                        if self.secure_domain_router_name is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                        return meta._meta_table['Install.SoftwareInventory.Committed.Inventories.Inventory']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:software-inventory/Cisco-IOS-XR-installmgr-admin-oper:committed/Cisco-IOS-XR-installmgr-admin-oper:inventories'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.inventory is not None:
                        for child_ref in self.inventory:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                    return meta._meta_table['Install.SoftwareInventory.Committed.Inventories']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:software-inventory/Cisco-IOS-XR-installmgr-admin-oper:committed'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.inventories is not None and self.inventories._has_data():
                    return True

                if self.summary is not None and self.summary._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                return meta._meta_table['Install.SoftwareInventory.Committed']['meta_info']


        class Inactive(object):
            """
            Inactive inventory information
            
            .. attribute:: inventories
            
            	Software inventory
            	**type**\:   :py:class:`Inventories <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Inactive.Inventories>`
            
            .. attribute:: summary
            
            	Summarized inventory information
            	**type**\:   :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Inactive.Summary>`
            
            

            """

            _prefix = 'installmgr-admin-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.inventories = Install.SoftwareInventory.Inactive.Inventories()
                self.inventories.parent = self
                self.summary = Install.SoftwareInventory.Inactive.Summary()
                self.summary.parent = self


            class Summary(object):
                """
                Summarized inventory information
                
                .. attribute:: admin_load_path
                
                	Admin Resources load path
                	**type**\:   :py:class:`AdminLoadPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Inactive.Summary.AdminLoadPath>`
                
                .. attribute:: default_load_path
                
                	Default load path
                	**type**\:   :py:class:`DefaultLoadPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Inactive.Summary.DefaultLoadPath>`
                
                .. attribute:: location_load_path
                
                	Location load paths
                	**type**\: list of    :py:class:`LocationLoadPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Inactive.Summary.LocationLoadPath>`
                
                .. attribute:: sdr_load_path
                
                	SDR load paths
                	**type**\: list of    :py:class:`SdrLoadPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Inactive.Summary.SdrLoadPath>`
                
                

                """

                _prefix = 'installmgr-admin-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.admin_load_path = Install.SoftwareInventory.Inactive.Summary.AdminLoadPath()
                    self.admin_load_path.parent = self
                    self.default_load_path = Install.SoftwareInventory.Inactive.Summary.DefaultLoadPath()
                    self.default_load_path.parent = self
                    self.location_load_path = YList()
                    self.location_load_path.parent = self
                    self.location_load_path.name = 'location_load_path'
                    self.sdr_load_path = YList()
                    self.sdr_load_path.parent = self
                    self.sdr_load_path.name = 'sdr_load_path'


                class DefaultLoadPath(object):
                    """
                    Default load path
                    
                    .. attribute:: admin_match
                    
                    	Does this match the Admin Resources load path?
                    	**type**\:  bool
                    
                    .. attribute:: load_path
                    
                    	Default load path
                    	**type**\: list of    :py:class:`LoadPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Inactive.Summary.DefaultLoadPath.LoadPath>`
                    
                    .. attribute:: request_id
                    
                    	Install op affecting scope
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: secure_domain_router_name
                    
                    	Names of SDRs this applies to
                    	**type**\:  list of str
                    
                    .. attribute:: standby_load_path
                    
                    	Load paths for standby nodes
                    	**type**\: list of    :py:class:`StandbyLoadPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Inactive.Summary.DefaultLoadPath.StandbyLoadPath>`
                    
                    

                    """

                    _prefix = 'installmgr-admin-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.admin_match = None
                        self.load_path = YList()
                        self.load_path.parent = self
                        self.load_path.name = 'load_path'
                        self.request_id = None
                        self.secure_domain_router_name = YLeafList()
                        self.secure_domain_router_name.parent = self
                        self.secure_domain_router_name.name = 'secure_domain_router_name'
                        self.standby_load_path = YList()
                        self.standby_load_path.parent = self
                        self.standby_load_path.name = 'standby_load_path'


                    class LoadPath(object):
                        """
                        Default load path
                        
                        .. attribute:: build_information
                        
                        	Build information
                        	**type**\:  str
                        
                        .. attribute:: package
                        
                        	Package
                        	**type**\:   :py:class:`Package <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Inactive.Summary.DefaultLoadPath.LoadPath.Package>`
                        
                        .. attribute:: version
                        
                        	Version
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'installmgr-admin-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.build_information = None
                            self.package = Install.SoftwareInventory.Inactive.Summary.DefaultLoadPath.LoadPath.Package()
                            self.package.parent = self
                            self.version = None


                        class Package(object):
                            """
                            Package
                            
                            .. attribute:: device_name
                            
                            	Device name
                            	**type**\:  str
                            
                            .. attribute:: name
                            
                            	Package group name
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'installmgr-admin-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.device_name = None
                                self.name = None

                            @property
                            def _common_path(self):

                                return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:software-inventory/Cisco-IOS-XR-installmgr-admin-oper:inactive/Cisco-IOS-XR-installmgr-admin-oper:summary/Cisco-IOS-XR-installmgr-admin-oper:default-load-path/Cisco-IOS-XR-installmgr-admin-oper:load-path/Cisco-IOS-XR-installmgr-admin-oper:package'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.device_name is not None:
                                    return True

                                if self.name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                                return meta._meta_table['Install.SoftwareInventory.Inactive.Summary.DefaultLoadPath.LoadPath.Package']['meta_info']

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:software-inventory/Cisco-IOS-XR-installmgr-admin-oper:inactive/Cisco-IOS-XR-installmgr-admin-oper:summary/Cisco-IOS-XR-installmgr-admin-oper:default-load-path/Cisco-IOS-XR-installmgr-admin-oper:load-path'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.build_information is not None:
                                return True

                            if self.package is not None and self.package._has_data():
                                return True

                            if self.version is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                            return meta._meta_table['Install.SoftwareInventory.Inactive.Summary.DefaultLoadPath.LoadPath']['meta_info']


                    class StandbyLoadPath(object):
                        """
                        Load paths for standby nodes
                        
                        .. attribute:: build_information
                        
                        	Build information
                        	**type**\:  str
                        
                        .. attribute:: package
                        
                        	Package
                        	**type**\:   :py:class:`Package <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Inactive.Summary.DefaultLoadPath.StandbyLoadPath.Package>`
                        
                        .. attribute:: version
                        
                        	Version
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'installmgr-admin-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.build_information = None
                            self.package = Install.SoftwareInventory.Inactive.Summary.DefaultLoadPath.StandbyLoadPath.Package()
                            self.package.parent = self
                            self.version = None


                        class Package(object):
                            """
                            Package
                            
                            .. attribute:: device_name
                            
                            	Device name
                            	**type**\:  str
                            
                            .. attribute:: name
                            
                            	Package group name
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'installmgr-admin-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.device_name = None
                                self.name = None

                            @property
                            def _common_path(self):

                                return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:software-inventory/Cisco-IOS-XR-installmgr-admin-oper:inactive/Cisco-IOS-XR-installmgr-admin-oper:summary/Cisco-IOS-XR-installmgr-admin-oper:default-load-path/Cisco-IOS-XR-installmgr-admin-oper:standby-load-path/Cisco-IOS-XR-installmgr-admin-oper:package'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.device_name is not None:
                                    return True

                                if self.name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                                return meta._meta_table['Install.SoftwareInventory.Inactive.Summary.DefaultLoadPath.StandbyLoadPath.Package']['meta_info']

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:software-inventory/Cisco-IOS-XR-installmgr-admin-oper:inactive/Cisco-IOS-XR-installmgr-admin-oper:summary/Cisco-IOS-XR-installmgr-admin-oper:default-load-path/Cisco-IOS-XR-installmgr-admin-oper:standby-load-path'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.build_information is not None:
                                return True

                            if self.package is not None and self.package._has_data():
                                return True

                            if self.version is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                            return meta._meta_table['Install.SoftwareInventory.Inactive.Summary.DefaultLoadPath.StandbyLoadPath']['meta_info']

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:software-inventory/Cisco-IOS-XR-installmgr-admin-oper:inactive/Cisco-IOS-XR-installmgr-admin-oper:summary/Cisco-IOS-XR-installmgr-admin-oper:default-load-path'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.admin_match is not None:
                            return True

                        if self.load_path is not None:
                            for child_ref in self.load_path:
                                if child_ref._has_data():
                                    return True

                        if self.request_id is not None:
                            return True

                        if self.secure_domain_router_name is not None:
                            for child in self.secure_domain_router_name:
                                if child is not None:
                                    return True

                        if self.standby_load_path is not None:
                            for child_ref in self.standby_load_path:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                        return meta._meta_table['Install.SoftwareInventory.Inactive.Summary.DefaultLoadPath']['meta_info']


                class AdminLoadPath(object):
                    """
                    Admin Resources load path
                    
                    .. attribute:: load_path
                    
                    	Admin Resources load path
                    	**type**\: list of    :py:class:`LoadPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Inactive.Summary.AdminLoadPath.LoadPath>`
                    
                    .. attribute:: request_id
                    
                    	Install op affecting scope
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: standby_load_path
                    
                    	Load paths for standby nodes
                    	**type**\: list of    :py:class:`StandbyLoadPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Inactive.Summary.AdminLoadPath.StandbyLoadPath>`
                    
                    

                    """

                    _prefix = 'installmgr-admin-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.load_path = YList()
                        self.load_path.parent = self
                        self.load_path.name = 'load_path'
                        self.request_id = None
                        self.standby_load_path = YList()
                        self.standby_load_path.parent = self
                        self.standby_load_path.name = 'standby_load_path'


                    class LoadPath(object):
                        """
                        Admin Resources load path
                        
                        .. attribute:: build_information
                        
                        	Build information
                        	**type**\:  str
                        
                        .. attribute:: package
                        
                        	Package
                        	**type**\:   :py:class:`Package <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Inactive.Summary.AdminLoadPath.LoadPath.Package>`
                        
                        .. attribute:: version
                        
                        	Version
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'installmgr-admin-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.build_information = None
                            self.package = Install.SoftwareInventory.Inactive.Summary.AdminLoadPath.LoadPath.Package()
                            self.package.parent = self
                            self.version = None


                        class Package(object):
                            """
                            Package
                            
                            .. attribute:: device_name
                            
                            	Device name
                            	**type**\:  str
                            
                            .. attribute:: name
                            
                            	Package group name
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'installmgr-admin-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.device_name = None
                                self.name = None

                            @property
                            def _common_path(self):

                                return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:software-inventory/Cisco-IOS-XR-installmgr-admin-oper:inactive/Cisco-IOS-XR-installmgr-admin-oper:summary/Cisco-IOS-XR-installmgr-admin-oper:admin-load-path/Cisco-IOS-XR-installmgr-admin-oper:load-path/Cisco-IOS-XR-installmgr-admin-oper:package'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.device_name is not None:
                                    return True

                                if self.name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                                return meta._meta_table['Install.SoftwareInventory.Inactive.Summary.AdminLoadPath.LoadPath.Package']['meta_info']

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:software-inventory/Cisco-IOS-XR-installmgr-admin-oper:inactive/Cisco-IOS-XR-installmgr-admin-oper:summary/Cisco-IOS-XR-installmgr-admin-oper:admin-load-path/Cisco-IOS-XR-installmgr-admin-oper:load-path'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.build_information is not None:
                                return True

                            if self.package is not None and self.package._has_data():
                                return True

                            if self.version is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                            return meta._meta_table['Install.SoftwareInventory.Inactive.Summary.AdminLoadPath.LoadPath']['meta_info']


                    class StandbyLoadPath(object):
                        """
                        Load paths for standby nodes
                        
                        .. attribute:: build_information
                        
                        	Build information
                        	**type**\:  str
                        
                        .. attribute:: package
                        
                        	Package
                        	**type**\:   :py:class:`Package <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Inactive.Summary.AdminLoadPath.StandbyLoadPath.Package>`
                        
                        .. attribute:: version
                        
                        	Version
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'installmgr-admin-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.build_information = None
                            self.package = Install.SoftwareInventory.Inactive.Summary.AdminLoadPath.StandbyLoadPath.Package()
                            self.package.parent = self
                            self.version = None


                        class Package(object):
                            """
                            Package
                            
                            .. attribute:: device_name
                            
                            	Device name
                            	**type**\:  str
                            
                            .. attribute:: name
                            
                            	Package group name
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'installmgr-admin-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.device_name = None
                                self.name = None

                            @property
                            def _common_path(self):

                                return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:software-inventory/Cisco-IOS-XR-installmgr-admin-oper:inactive/Cisco-IOS-XR-installmgr-admin-oper:summary/Cisco-IOS-XR-installmgr-admin-oper:admin-load-path/Cisco-IOS-XR-installmgr-admin-oper:standby-load-path/Cisco-IOS-XR-installmgr-admin-oper:package'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.device_name is not None:
                                    return True

                                if self.name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                                return meta._meta_table['Install.SoftwareInventory.Inactive.Summary.AdminLoadPath.StandbyLoadPath.Package']['meta_info']

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:software-inventory/Cisco-IOS-XR-installmgr-admin-oper:inactive/Cisco-IOS-XR-installmgr-admin-oper:summary/Cisco-IOS-XR-installmgr-admin-oper:admin-load-path/Cisco-IOS-XR-installmgr-admin-oper:standby-load-path'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.build_information is not None:
                                return True

                            if self.package is not None and self.package._has_data():
                                return True

                            if self.version is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                            return meta._meta_table['Install.SoftwareInventory.Inactive.Summary.AdminLoadPath.StandbyLoadPath']['meta_info']

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:software-inventory/Cisco-IOS-XR-installmgr-admin-oper:inactive/Cisco-IOS-XR-installmgr-admin-oper:summary/Cisco-IOS-XR-installmgr-admin-oper:admin-load-path'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.load_path is not None:
                            for child_ref in self.load_path:
                                if child_ref._has_data():
                                    return True

                        if self.request_id is not None:
                            return True

                        if self.standby_load_path is not None:
                            for child_ref in self.standby_load_path:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                        return meta._meta_table['Install.SoftwareInventory.Inactive.Summary.AdminLoadPath']['meta_info']


                class SdrLoadPath(object):
                    """
                    SDR load paths
                    
                    .. attribute:: load_path
                    
                    	Load path
                    	**type**\: list of    :py:class:`LoadPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Inactive.Summary.SdrLoadPath.LoadPath>`
                    
                    .. attribute:: request_id
                    
                    	Install op affecting scope
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: secure_domain_router_name
                    
                    	SDR name
                    	**type**\:  str
                    
                    .. attribute:: standby_load_path
                    
                    	Load paths for standby nodes
                    	**type**\: list of    :py:class:`StandbyLoadPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Inactive.Summary.SdrLoadPath.StandbyLoadPath>`
                    
                    

                    """

                    _prefix = 'installmgr-admin-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.load_path = YList()
                        self.load_path.parent = self
                        self.load_path.name = 'load_path'
                        self.request_id = None
                        self.secure_domain_router_name = None
                        self.standby_load_path = YList()
                        self.standby_load_path.parent = self
                        self.standby_load_path.name = 'standby_load_path'


                    class LoadPath(object):
                        """
                        Load path
                        
                        .. attribute:: build_information
                        
                        	Build information
                        	**type**\:  str
                        
                        .. attribute:: package
                        
                        	Package
                        	**type**\:   :py:class:`Package <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Inactive.Summary.SdrLoadPath.LoadPath.Package>`
                        
                        .. attribute:: version
                        
                        	Version
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'installmgr-admin-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.build_information = None
                            self.package = Install.SoftwareInventory.Inactive.Summary.SdrLoadPath.LoadPath.Package()
                            self.package.parent = self
                            self.version = None


                        class Package(object):
                            """
                            Package
                            
                            .. attribute:: device_name
                            
                            	Device name
                            	**type**\:  str
                            
                            .. attribute:: name
                            
                            	Package group name
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'installmgr-admin-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.device_name = None
                                self.name = None

                            @property
                            def _common_path(self):

                                return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:software-inventory/Cisco-IOS-XR-installmgr-admin-oper:inactive/Cisco-IOS-XR-installmgr-admin-oper:summary/Cisco-IOS-XR-installmgr-admin-oper:sdr-load-path/Cisco-IOS-XR-installmgr-admin-oper:load-path/Cisco-IOS-XR-installmgr-admin-oper:package'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.device_name is not None:
                                    return True

                                if self.name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                                return meta._meta_table['Install.SoftwareInventory.Inactive.Summary.SdrLoadPath.LoadPath.Package']['meta_info']

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:software-inventory/Cisco-IOS-XR-installmgr-admin-oper:inactive/Cisco-IOS-XR-installmgr-admin-oper:summary/Cisco-IOS-XR-installmgr-admin-oper:sdr-load-path/Cisco-IOS-XR-installmgr-admin-oper:load-path'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.build_information is not None:
                                return True

                            if self.package is not None and self.package._has_data():
                                return True

                            if self.version is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                            return meta._meta_table['Install.SoftwareInventory.Inactive.Summary.SdrLoadPath.LoadPath']['meta_info']


                    class StandbyLoadPath(object):
                        """
                        Load paths for standby nodes
                        
                        .. attribute:: build_information
                        
                        	Build information
                        	**type**\:  str
                        
                        .. attribute:: package
                        
                        	Package
                        	**type**\:   :py:class:`Package <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Inactive.Summary.SdrLoadPath.StandbyLoadPath.Package>`
                        
                        .. attribute:: version
                        
                        	Version
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'installmgr-admin-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.build_information = None
                            self.package = Install.SoftwareInventory.Inactive.Summary.SdrLoadPath.StandbyLoadPath.Package()
                            self.package.parent = self
                            self.version = None


                        class Package(object):
                            """
                            Package
                            
                            .. attribute:: device_name
                            
                            	Device name
                            	**type**\:  str
                            
                            .. attribute:: name
                            
                            	Package group name
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'installmgr-admin-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.device_name = None
                                self.name = None

                            @property
                            def _common_path(self):

                                return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:software-inventory/Cisco-IOS-XR-installmgr-admin-oper:inactive/Cisco-IOS-XR-installmgr-admin-oper:summary/Cisco-IOS-XR-installmgr-admin-oper:sdr-load-path/Cisco-IOS-XR-installmgr-admin-oper:standby-load-path/Cisco-IOS-XR-installmgr-admin-oper:package'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.device_name is not None:
                                    return True

                                if self.name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                                return meta._meta_table['Install.SoftwareInventory.Inactive.Summary.SdrLoadPath.StandbyLoadPath.Package']['meta_info']

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:software-inventory/Cisco-IOS-XR-installmgr-admin-oper:inactive/Cisco-IOS-XR-installmgr-admin-oper:summary/Cisco-IOS-XR-installmgr-admin-oper:sdr-load-path/Cisco-IOS-XR-installmgr-admin-oper:standby-load-path'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.build_information is not None:
                                return True

                            if self.package is not None and self.package._has_data():
                                return True

                            if self.version is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                            return meta._meta_table['Install.SoftwareInventory.Inactive.Summary.SdrLoadPath.StandbyLoadPath']['meta_info']

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:software-inventory/Cisco-IOS-XR-installmgr-admin-oper:inactive/Cisco-IOS-XR-installmgr-admin-oper:summary/Cisco-IOS-XR-installmgr-admin-oper:sdr-load-path'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.load_path is not None:
                            for child_ref in self.load_path:
                                if child_ref._has_data():
                                    return True

                        if self.request_id is not None:
                            return True

                        if self.secure_domain_router_name is not None:
                            return True

                        if self.standby_load_path is not None:
                            for child_ref in self.standby_load_path:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                        return meta._meta_table['Install.SoftwareInventory.Inactive.Summary.SdrLoadPath']['meta_info']


                class LocationLoadPath(object):
                    """
                    Location load paths
                    
                    .. attribute:: load_path
                    
                    	Load path
                    	**type**\: list of    :py:class:`LoadPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Inactive.Summary.LocationLoadPath.LoadPath>`
                    
                    .. attribute:: node_name
                    
                    	Node identifier
                    	**type**\:  str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    .. attribute:: request_id
                    
                    	Install op affecting scope
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: secure_domain_router_name
                    
                    	SDR name
                    	**type**\:  str
                    
                    .. attribute:: standby_load_path
                    
                    	Load paths for standby nodes
                    	**type**\: list of    :py:class:`StandbyLoadPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Inactive.Summary.LocationLoadPath.StandbyLoadPath>`
                    
                    

                    """

                    _prefix = 'installmgr-admin-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.load_path = YList()
                        self.load_path.parent = self
                        self.load_path.name = 'load_path'
                        self.node_name = None
                        self.request_id = None
                        self.secure_domain_router_name = None
                        self.standby_load_path = YList()
                        self.standby_load_path.parent = self
                        self.standby_load_path.name = 'standby_load_path'


                    class LoadPath(object):
                        """
                        Load path
                        
                        .. attribute:: build_information
                        
                        	Build information
                        	**type**\:  str
                        
                        .. attribute:: package
                        
                        	Package
                        	**type**\:   :py:class:`Package <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Inactive.Summary.LocationLoadPath.LoadPath.Package>`
                        
                        .. attribute:: version
                        
                        	Version
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'installmgr-admin-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.build_information = None
                            self.package = Install.SoftwareInventory.Inactive.Summary.LocationLoadPath.LoadPath.Package()
                            self.package.parent = self
                            self.version = None


                        class Package(object):
                            """
                            Package
                            
                            .. attribute:: device_name
                            
                            	Device name
                            	**type**\:  str
                            
                            .. attribute:: name
                            
                            	Package group name
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'installmgr-admin-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.device_name = None
                                self.name = None

                            @property
                            def _common_path(self):

                                return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:software-inventory/Cisco-IOS-XR-installmgr-admin-oper:inactive/Cisco-IOS-XR-installmgr-admin-oper:summary/Cisco-IOS-XR-installmgr-admin-oper:location-load-path/Cisco-IOS-XR-installmgr-admin-oper:load-path/Cisco-IOS-XR-installmgr-admin-oper:package'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.device_name is not None:
                                    return True

                                if self.name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                                return meta._meta_table['Install.SoftwareInventory.Inactive.Summary.LocationLoadPath.LoadPath.Package']['meta_info']

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:software-inventory/Cisco-IOS-XR-installmgr-admin-oper:inactive/Cisco-IOS-XR-installmgr-admin-oper:summary/Cisco-IOS-XR-installmgr-admin-oper:location-load-path/Cisco-IOS-XR-installmgr-admin-oper:load-path'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.build_information is not None:
                                return True

                            if self.package is not None and self.package._has_data():
                                return True

                            if self.version is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                            return meta._meta_table['Install.SoftwareInventory.Inactive.Summary.LocationLoadPath.LoadPath']['meta_info']


                    class StandbyLoadPath(object):
                        """
                        Load paths for standby nodes
                        
                        .. attribute:: build_information
                        
                        	Build information
                        	**type**\:  str
                        
                        .. attribute:: package
                        
                        	Package
                        	**type**\:   :py:class:`Package <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Inactive.Summary.LocationLoadPath.StandbyLoadPath.Package>`
                        
                        .. attribute:: version
                        
                        	Version
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'installmgr-admin-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.build_information = None
                            self.package = Install.SoftwareInventory.Inactive.Summary.LocationLoadPath.StandbyLoadPath.Package()
                            self.package.parent = self
                            self.version = None


                        class Package(object):
                            """
                            Package
                            
                            .. attribute:: device_name
                            
                            	Device name
                            	**type**\:  str
                            
                            .. attribute:: name
                            
                            	Package group name
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'installmgr-admin-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.device_name = None
                                self.name = None

                            @property
                            def _common_path(self):

                                return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:software-inventory/Cisco-IOS-XR-installmgr-admin-oper:inactive/Cisco-IOS-XR-installmgr-admin-oper:summary/Cisco-IOS-XR-installmgr-admin-oper:location-load-path/Cisco-IOS-XR-installmgr-admin-oper:standby-load-path/Cisco-IOS-XR-installmgr-admin-oper:package'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.device_name is not None:
                                    return True

                                if self.name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                                return meta._meta_table['Install.SoftwareInventory.Inactive.Summary.LocationLoadPath.StandbyLoadPath.Package']['meta_info']

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:software-inventory/Cisco-IOS-XR-installmgr-admin-oper:inactive/Cisco-IOS-XR-installmgr-admin-oper:summary/Cisco-IOS-XR-installmgr-admin-oper:location-load-path/Cisco-IOS-XR-installmgr-admin-oper:standby-load-path'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.build_information is not None:
                                return True

                            if self.package is not None and self.package._has_data():
                                return True

                            if self.version is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                            return meta._meta_table['Install.SoftwareInventory.Inactive.Summary.LocationLoadPath.StandbyLoadPath']['meta_info']

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:software-inventory/Cisco-IOS-XR-installmgr-admin-oper:inactive/Cisco-IOS-XR-installmgr-admin-oper:summary/Cisco-IOS-XR-installmgr-admin-oper:location-load-path'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.load_path is not None:
                            for child_ref in self.load_path:
                                if child_ref._has_data():
                                    return True

                        if self.node_name is not None:
                            return True

                        if self.request_id is not None:
                            return True

                        if self.secure_domain_router_name is not None:
                            return True

                        if self.standby_load_path is not None:
                            for child_ref in self.standby_load_path:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                        return meta._meta_table['Install.SoftwareInventory.Inactive.Summary.LocationLoadPath']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:software-inventory/Cisco-IOS-XR-installmgr-admin-oper:inactive/Cisco-IOS-XR-installmgr-admin-oper:summary'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.admin_load_path is not None and self.admin_load_path._has_data():
                        return True

                    if self.default_load_path is not None and self.default_load_path._has_data():
                        return True

                    if self.location_load_path is not None:
                        for child_ref in self.location_load_path:
                            if child_ref._has_data():
                                return True

                    if self.sdr_load_path is not None:
                        for child_ref in self.sdr_load_path:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                    return meta._meta_table['Install.SoftwareInventory.Inactive.Summary']['meta_info']


            class Inventories(object):
                """
                Software inventory
                
                .. attribute:: inventory
                
                	Inventory information for specific node
                	**type**\: list of    :py:class:`Inventory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Inactive.Inventories.Inventory>`
                
                

                """

                _prefix = 'installmgr-admin-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.inventory = YList()
                    self.inventory.parent = self
                    self.inventory.name = 'inventory'


                class Inventory(object):
                    """
                    Inventory information for specific node
                    
                    .. attribute:: node_name  <key>
                    
                    	Node name
                    	**type**\:  str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    .. attribute:: boot_image_name
                    
                    	Name of the boot image
                    	**type**\:  str
                    
                    .. attribute:: load_path
                    
                    	Load path
                    	**type**\: list of    :py:class:`LoadPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Inactive.Inventories.Inventory.LoadPath>`
                    
                    .. attribute:: major
                    
                    	Major data version number
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: minor
                    
                    	Minor data version number
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: node_type
                    
                    	Node's type
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: secure_domain_router_name
                    
                    	SDR name
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'installmgr-admin-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.node_name = None
                        self.boot_image_name = None
                        self.load_path = YList()
                        self.load_path.parent = self
                        self.load_path.name = 'load_path'
                        self.major = None
                        self.minor = None
                        self.node_type = None
                        self.secure_domain_router_name = None


                    class LoadPath(object):
                        """
                        Load path
                        
                        .. attribute:: build_information
                        
                        	Build information
                        	**type**\:  str
                        
                        .. attribute:: package
                        
                        	Package
                        	**type**\:   :py:class:`Package <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Inactive.Inventories.Inventory.LoadPath.Package>`
                        
                        .. attribute:: version
                        
                        	Version
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'installmgr-admin-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.build_information = None
                            self.package = Install.SoftwareInventory.Inactive.Inventories.Inventory.LoadPath.Package()
                            self.package.parent = self
                            self.version = None


                        class Package(object):
                            """
                            Package
                            
                            .. attribute:: device_name
                            
                            	Device name
                            	**type**\:  str
                            
                            .. attribute:: name
                            
                            	Package group name
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'installmgr-admin-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.device_name = None
                                self.name = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-installmgr-admin-oper:package'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.device_name is not None:
                                    return True

                                if self.name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                                return meta._meta_table['Install.SoftwareInventory.Inactive.Inventories.Inventory.LoadPath.Package']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-installmgr-admin-oper:load-path'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.build_information is not None:
                                return True

                            if self.package is not None and self.package._has_data():
                                return True

                            if self.version is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                            return meta._meta_table['Install.SoftwareInventory.Inactive.Inventories.Inventory.LoadPath']['meta_info']

                    @property
                    def _common_path(self):
                        if self.node_name is None:
                            raise YPYModelError('Key property node_name is None')

                        return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:software-inventory/Cisco-IOS-XR-installmgr-admin-oper:inactive/Cisco-IOS-XR-installmgr-admin-oper:inventories/Cisco-IOS-XR-installmgr-admin-oper:inventory[Cisco-IOS-XR-installmgr-admin-oper:node-name = ' + str(self.node_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.node_name is not None:
                            return True

                        if self.boot_image_name is not None:
                            return True

                        if self.load_path is not None:
                            for child_ref in self.load_path:
                                if child_ref._has_data():
                                    return True

                        if self.major is not None:
                            return True

                        if self.minor is not None:
                            return True

                        if self.node_type is not None:
                            return True

                        if self.secure_domain_router_name is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                        return meta._meta_table['Install.SoftwareInventory.Inactive.Inventories.Inventory']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:software-inventory/Cisco-IOS-XR-installmgr-admin-oper:inactive/Cisco-IOS-XR-installmgr-admin-oper:inventories'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.inventory is not None:
                        for child_ref in self.inventory:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                    return meta._meta_table['Install.SoftwareInventory.Inactive.Inventories']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:software-inventory/Cisco-IOS-XR-installmgr-admin-oper:inactive'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.inventories is not None and self.inventories._has_data():
                    return True

                if self.summary is not None and self.summary._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                return meta._meta_table['Install.SoftwareInventory.Inactive']['meta_info']


        class Requests(object):
            """
            Install operation requests
            
            .. attribute:: requests
            
            	Install operation request history
            	**type**\:   :py:class:`Requests_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Requests.Requests_>`
            
            

            """

            _prefix = 'installmgr-admin-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.requests = Install.SoftwareInventory.Requests.Requests_()
                self.requests.parent = self


            class Requests_(object):
                """
                Install operation request history
                
                .. attribute:: request
                
                	Install operation request information
                	**type**\: list of    :py:class:`Request <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Requests.Requests_.Request>`
                
                

                """

                _prefix = 'installmgr-admin-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.request = YList()
                    self.request.parent = self
                    self.request.name = 'request'


                class Request(object):
                    """
                    Install operation request information
                    
                    .. attribute:: request_id  <key>
                    
                    	Install operation request ID
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: inventories
                    
                    	Inventory information of install operation request
                    	**type**\:   :py:class:`Inventories <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Requests.Requests_.Request.Inventories>`
                    
                    

                    """

                    _prefix = 'installmgr-admin-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.request_id = None
                        self.inventories = Install.SoftwareInventory.Requests.Requests_.Request.Inventories()
                        self.inventories.parent = self


                    class Inventories(object):
                        """
                        Inventory information of install operation
                        request
                        
                        .. attribute:: inventory
                        
                        	Inventory information
                        	**type**\: list of    :py:class:`Inventory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Requests.Requests_.Request.Inventories.Inventory>`
                        
                        

                        """

                        _prefix = 'installmgr-admin-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.inventory = YList()
                            self.inventory.parent = self
                            self.inventory.name = 'inventory'


                        class Inventory(object):
                            """
                            Inventory information
                            
                            .. attribute:: node_name  <key>
                            
                            	Node name
                            	**type**\:  str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            .. attribute:: boot_image_name
                            
                            	Name of the boot image
                            	**type**\:  str
                            
                            .. attribute:: load_path
                            
                            	Load path
                            	**type**\: list of    :py:class:`LoadPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Requests.Requests_.Request.Inventories.Inventory.LoadPath>`
                            
                            .. attribute:: major
                            
                            	Major data version number
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: minor
                            
                            	Minor data version number
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: node_type
                            
                            	Node's type
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: secure_domain_router_name
                            
                            	SDR name
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'installmgr-admin-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.node_name = None
                                self.boot_image_name = None
                                self.load_path = YList()
                                self.load_path.parent = self
                                self.load_path.name = 'load_path'
                                self.major = None
                                self.minor = None
                                self.node_type = None
                                self.secure_domain_router_name = None


                            class LoadPath(object):
                                """
                                Load path
                                
                                .. attribute:: build_information
                                
                                	Build information
                                	**type**\:  str
                                
                                .. attribute:: package
                                
                                	Package
                                	**type**\:   :py:class:`Package <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Requests.Requests_.Request.Inventories.Inventory.LoadPath.Package>`
                                
                                .. attribute:: version
                                
                                	Version
                                	**type**\:  str
                                
                                

                                """

                                _prefix = 'installmgr-admin-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.build_information = None
                                    self.package = Install.SoftwareInventory.Requests.Requests_.Request.Inventories.Inventory.LoadPath.Package()
                                    self.package.parent = self
                                    self.version = None


                                class Package(object):
                                    """
                                    Package
                                    
                                    .. attribute:: device_name
                                    
                                    	Device name
                                    	**type**\:  str
                                    
                                    .. attribute:: name
                                    
                                    	Package group name
                                    	**type**\:  str
                                    
                                    

                                    """

                                    _prefix = 'installmgr-admin-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.device_name = None
                                        self.name = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-installmgr-admin-oper:package'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.device_name is not None:
                                            return True

                                        if self.name is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                                        return meta._meta_table['Install.SoftwareInventory.Requests.Requests_.Request.Inventories.Inventory.LoadPath.Package']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-installmgr-admin-oper:load-path'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.build_information is not None:
                                        return True

                                    if self.package is not None and self.package._has_data():
                                        return True

                                    if self.version is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                                    return meta._meta_table['Install.SoftwareInventory.Requests.Requests_.Request.Inventories.Inventory.LoadPath']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.node_name is None:
                                    raise YPYModelError('Key property node_name is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-installmgr-admin-oper:inventory[Cisco-IOS-XR-installmgr-admin-oper:node-name = ' + str(self.node_name) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.node_name is not None:
                                    return True

                                if self.boot_image_name is not None:
                                    return True

                                if self.load_path is not None:
                                    for child_ref in self.load_path:
                                        if child_ref._has_data():
                                            return True

                                if self.major is not None:
                                    return True

                                if self.minor is not None:
                                    return True

                                if self.node_type is not None:
                                    return True

                                if self.secure_domain_router_name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                                return meta._meta_table['Install.SoftwareInventory.Requests.Requests_.Request.Inventories.Inventory']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-installmgr-admin-oper:inventories'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.inventory is not None:
                                for child_ref in self.inventory:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                            return meta._meta_table['Install.SoftwareInventory.Requests.Requests_.Request.Inventories']['meta_info']

                    @property
                    def _common_path(self):
                        if self.request_id is None:
                            raise YPYModelError('Key property request_id is None')

                        return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:software-inventory/Cisco-IOS-XR-installmgr-admin-oper:requests/Cisco-IOS-XR-installmgr-admin-oper:requests/Cisco-IOS-XR-installmgr-admin-oper:request[Cisco-IOS-XR-installmgr-admin-oper:request-id = ' + str(self.request_id) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.request_id is not None:
                            return True

                        if self.inventories is not None and self.inventories._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                        return meta._meta_table['Install.SoftwareInventory.Requests.Requests_.Request']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:software-inventory/Cisco-IOS-XR-installmgr-admin-oper:requests/Cisco-IOS-XR-installmgr-admin-oper:requests'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.request is not None:
                        for child_ref in self.request:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                    return meta._meta_table['Install.SoftwareInventory.Requests.Requests_']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:software-inventory/Cisco-IOS-XR-installmgr-admin-oper:requests'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.requests is not None and self.requests._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                return meta._meta_table['Install.SoftwareInventory.Requests']['meta_info']


        class Active(object):
            """
            Active inventory information
            
            .. attribute:: inventories
            
            	Software inventory
            	**type**\:   :py:class:`Inventories <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Active.Inventories>`
            
            .. attribute:: summary
            
            	Summarized inventory information
            	**type**\:   :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Active.Summary>`
            
            

            """

            _prefix = 'installmgr-admin-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.inventories = Install.SoftwareInventory.Active.Inventories()
                self.inventories.parent = self
                self.summary = Install.SoftwareInventory.Active.Summary()
                self.summary.parent = self


            class Summary(object):
                """
                Summarized inventory information
                
                .. attribute:: admin_load_path
                
                	Admin Resources load path
                	**type**\:   :py:class:`AdminLoadPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Active.Summary.AdminLoadPath>`
                
                .. attribute:: default_load_path
                
                	Default load path
                	**type**\:   :py:class:`DefaultLoadPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Active.Summary.DefaultLoadPath>`
                
                .. attribute:: location_load_path
                
                	Location load paths
                	**type**\: list of    :py:class:`LocationLoadPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Active.Summary.LocationLoadPath>`
                
                .. attribute:: sdr_load_path
                
                	SDR load paths
                	**type**\: list of    :py:class:`SdrLoadPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Active.Summary.SdrLoadPath>`
                
                

                """

                _prefix = 'installmgr-admin-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.admin_load_path = Install.SoftwareInventory.Active.Summary.AdminLoadPath()
                    self.admin_load_path.parent = self
                    self.default_load_path = Install.SoftwareInventory.Active.Summary.DefaultLoadPath()
                    self.default_load_path.parent = self
                    self.location_load_path = YList()
                    self.location_load_path.parent = self
                    self.location_load_path.name = 'location_load_path'
                    self.sdr_load_path = YList()
                    self.sdr_load_path.parent = self
                    self.sdr_load_path.name = 'sdr_load_path'


                class DefaultLoadPath(object):
                    """
                    Default load path
                    
                    .. attribute:: admin_match
                    
                    	Does this match the Admin Resources load path?
                    	**type**\:  bool
                    
                    .. attribute:: load_path
                    
                    	Default load path
                    	**type**\: list of    :py:class:`LoadPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Active.Summary.DefaultLoadPath.LoadPath>`
                    
                    .. attribute:: request_id
                    
                    	Install op affecting scope
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: secure_domain_router_name
                    
                    	Names of SDRs this applies to
                    	**type**\:  list of str
                    
                    .. attribute:: standby_load_path
                    
                    	Load paths for standby nodes
                    	**type**\: list of    :py:class:`StandbyLoadPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Active.Summary.DefaultLoadPath.StandbyLoadPath>`
                    
                    

                    """

                    _prefix = 'installmgr-admin-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.admin_match = None
                        self.load_path = YList()
                        self.load_path.parent = self
                        self.load_path.name = 'load_path'
                        self.request_id = None
                        self.secure_domain_router_name = YLeafList()
                        self.secure_domain_router_name.parent = self
                        self.secure_domain_router_name.name = 'secure_domain_router_name'
                        self.standby_load_path = YList()
                        self.standby_load_path.parent = self
                        self.standby_load_path.name = 'standby_load_path'


                    class LoadPath(object):
                        """
                        Default load path
                        
                        .. attribute:: build_information
                        
                        	Build information
                        	**type**\:  str
                        
                        .. attribute:: package
                        
                        	Package
                        	**type**\:   :py:class:`Package <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Active.Summary.DefaultLoadPath.LoadPath.Package>`
                        
                        .. attribute:: version
                        
                        	Version
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'installmgr-admin-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.build_information = None
                            self.package = Install.SoftwareInventory.Active.Summary.DefaultLoadPath.LoadPath.Package()
                            self.package.parent = self
                            self.version = None


                        class Package(object):
                            """
                            Package
                            
                            .. attribute:: device_name
                            
                            	Device name
                            	**type**\:  str
                            
                            .. attribute:: name
                            
                            	Package group name
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'installmgr-admin-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.device_name = None
                                self.name = None

                            @property
                            def _common_path(self):

                                return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:software-inventory/Cisco-IOS-XR-installmgr-admin-oper:active/Cisco-IOS-XR-installmgr-admin-oper:summary/Cisco-IOS-XR-installmgr-admin-oper:default-load-path/Cisco-IOS-XR-installmgr-admin-oper:load-path/Cisco-IOS-XR-installmgr-admin-oper:package'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.device_name is not None:
                                    return True

                                if self.name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                                return meta._meta_table['Install.SoftwareInventory.Active.Summary.DefaultLoadPath.LoadPath.Package']['meta_info']

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:software-inventory/Cisco-IOS-XR-installmgr-admin-oper:active/Cisco-IOS-XR-installmgr-admin-oper:summary/Cisco-IOS-XR-installmgr-admin-oper:default-load-path/Cisco-IOS-XR-installmgr-admin-oper:load-path'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.build_information is not None:
                                return True

                            if self.package is not None and self.package._has_data():
                                return True

                            if self.version is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                            return meta._meta_table['Install.SoftwareInventory.Active.Summary.DefaultLoadPath.LoadPath']['meta_info']


                    class StandbyLoadPath(object):
                        """
                        Load paths for standby nodes
                        
                        .. attribute:: build_information
                        
                        	Build information
                        	**type**\:  str
                        
                        .. attribute:: package
                        
                        	Package
                        	**type**\:   :py:class:`Package <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Active.Summary.DefaultLoadPath.StandbyLoadPath.Package>`
                        
                        .. attribute:: version
                        
                        	Version
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'installmgr-admin-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.build_information = None
                            self.package = Install.SoftwareInventory.Active.Summary.DefaultLoadPath.StandbyLoadPath.Package()
                            self.package.parent = self
                            self.version = None


                        class Package(object):
                            """
                            Package
                            
                            .. attribute:: device_name
                            
                            	Device name
                            	**type**\:  str
                            
                            .. attribute:: name
                            
                            	Package group name
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'installmgr-admin-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.device_name = None
                                self.name = None

                            @property
                            def _common_path(self):

                                return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:software-inventory/Cisco-IOS-XR-installmgr-admin-oper:active/Cisco-IOS-XR-installmgr-admin-oper:summary/Cisco-IOS-XR-installmgr-admin-oper:default-load-path/Cisco-IOS-XR-installmgr-admin-oper:standby-load-path/Cisco-IOS-XR-installmgr-admin-oper:package'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.device_name is not None:
                                    return True

                                if self.name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                                return meta._meta_table['Install.SoftwareInventory.Active.Summary.DefaultLoadPath.StandbyLoadPath.Package']['meta_info']

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:software-inventory/Cisco-IOS-XR-installmgr-admin-oper:active/Cisco-IOS-XR-installmgr-admin-oper:summary/Cisco-IOS-XR-installmgr-admin-oper:default-load-path/Cisco-IOS-XR-installmgr-admin-oper:standby-load-path'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.build_information is not None:
                                return True

                            if self.package is not None and self.package._has_data():
                                return True

                            if self.version is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                            return meta._meta_table['Install.SoftwareInventory.Active.Summary.DefaultLoadPath.StandbyLoadPath']['meta_info']

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:software-inventory/Cisco-IOS-XR-installmgr-admin-oper:active/Cisco-IOS-XR-installmgr-admin-oper:summary/Cisco-IOS-XR-installmgr-admin-oper:default-load-path'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.admin_match is not None:
                            return True

                        if self.load_path is not None:
                            for child_ref in self.load_path:
                                if child_ref._has_data():
                                    return True

                        if self.request_id is not None:
                            return True

                        if self.secure_domain_router_name is not None:
                            for child in self.secure_domain_router_name:
                                if child is not None:
                                    return True

                        if self.standby_load_path is not None:
                            for child_ref in self.standby_load_path:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                        return meta._meta_table['Install.SoftwareInventory.Active.Summary.DefaultLoadPath']['meta_info']


                class AdminLoadPath(object):
                    """
                    Admin Resources load path
                    
                    .. attribute:: load_path
                    
                    	Admin Resources load path
                    	**type**\: list of    :py:class:`LoadPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Active.Summary.AdminLoadPath.LoadPath>`
                    
                    .. attribute:: request_id
                    
                    	Install op affecting scope
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: standby_load_path
                    
                    	Load paths for standby nodes
                    	**type**\: list of    :py:class:`StandbyLoadPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Active.Summary.AdminLoadPath.StandbyLoadPath>`
                    
                    

                    """

                    _prefix = 'installmgr-admin-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.load_path = YList()
                        self.load_path.parent = self
                        self.load_path.name = 'load_path'
                        self.request_id = None
                        self.standby_load_path = YList()
                        self.standby_load_path.parent = self
                        self.standby_load_path.name = 'standby_load_path'


                    class LoadPath(object):
                        """
                        Admin Resources load path
                        
                        .. attribute:: build_information
                        
                        	Build information
                        	**type**\:  str
                        
                        .. attribute:: package
                        
                        	Package
                        	**type**\:   :py:class:`Package <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Active.Summary.AdminLoadPath.LoadPath.Package>`
                        
                        .. attribute:: version
                        
                        	Version
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'installmgr-admin-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.build_information = None
                            self.package = Install.SoftwareInventory.Active.Summary.AdminLoadPath.LoadPath.Package()
                            self.package.parent = self
                            self.version = None


                        class Package(object):
                            """
                            Package
                            
                            .. attribute:: device_name
                            
                            	Device name
                            	**type**\:  str
                            
                            .. attribute:: name
                            
                            	Package group name
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'installmgr-admin-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.device_name = None
                                self.name = None

                            @property
                            def _common_path(self):

                                return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:software-inventory/Cisco-IOS-XR-installmgr-admin-oper:active/Cisco-IOS-XR-installmgr-admin-oper:summary/Cisco-IOS-XR-installmgr-admin-oper:admin-load-path/Cisco-IOS-XR-installmgr-admin-oper:load-path/Cisco-IOS-XR-installmgr-admin-oper:package'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.device_name is not None:
                                    return True

                                if self.name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                                return meta._meta_table['Install.SoftwareInventory.Active.Summary.AdminLoadPath.LoadPath.Package']['meta_info']

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:software-inventory/Cisco-IOS-XR-installmgr-admin-oper:active/Cisco-IOS-XR-installmgr-admin-oper:summary/Cisco-IOS-XR-installmgr-admin-oper:admin-load-path/Cisco-IOS-XR-installmgr-admin-oper:load-path'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.build_information is not None:
                                return True

                            if self.package is not None and self.package._has_data():
                                return True

                            if self.version is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                            return meta._meta_table['Install.SoftwareInventory.Active.Summary.AdminLoadPath.LoadPath']['meta_info']


                    class StandbyLoadPath(object):
                        """
                        Load paths for standby nodes
                        
                        .. attribute:: build_information
                        
                        	Build information
                        	**type**\:  str
                        
                        .. attribute:: package
                        
                        	Package
                        	**type**\:   :py:class:`Package <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Active.Summary.AdminLoadPath.StandbyLoadPath.Package>`
                        
                        .. attribute:: version
                        
                        	Version
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'installmgr-admin-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.build_information = None
                            self.package = Install.SoftwareInventory.Active.Summary.AdminLoadPath.StandbyLoadPath.Package()
                            self.package.parent = self
                            self.version = None


                        class Package(object):
                            """
                            Package
                            
                            .. attribute:: device_name
                            
                            	Device name
                            	**type**\:  str
                            
                            .. attribute:: name
                            
                            	Package group name
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'installmgr-admin-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.device_name = None
                                self.name = None

                            @property
                            def _common_path(self):

                                return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:software-inventory/Cisco-IOS-XR-installmgr-admin-oper:active/Cisco-IOS-XR-installmgr-admin-oper:summary/Cisco-IOS-XR-installmgr-admin-oper:admin-load-path/Cisco-IOS-XR-installmgr-admin-oper:standby-load-path/Cisco-IOS-XR-installmgr-admin-oper:package'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.device_name is not None:
                                    return True

                                if self.name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                                return meta._meta_table['Install.SoftwareInventory.Active.Summary.AdminLoadPath.StandbyLoadPath.Package']['meta_info']

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:software-inventory/Cisco-IOS-XR-installmgr-admin-oper:active/Cisco-IOS-XR-installmgr-admin-oper:summary/Cisco-IOS-XR-installmgr-admin-oper:admin-load-path/Cisco-IOS-XR-installmgr-admin-oper:standby-load-path'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.build_information is not None:
                                return True

                            if self.package is not None and self.package._has_data():
                                return True

                            if self.version is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                            return meta._meta_table['Install.SoftwareInventory.Active.Summary.AdminLoadPath.StandbyLoadPath']['meta_info']

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:software-inventory/Cisco-IOS-XR-installmgr-admin-oper:active/Cisco-IOS-XR-installmgr-admin-oper:summary/Cisco-IOS-XR-installmgr-admin-oper:admin-load-path'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.load_path is not None:
                            for child_ref in self.load_path:
                                if child_ref._has_data():
                                    return True

                        if self.request_id is not None:
                            return True

                        if self.standby_load_path is not None:
                            for child_ref in self.standby_load_path:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                        return meta._meta_table['Install.SoftwareInventory.Active.Summary.AdminLoadPath']['meta_info']


                class SdrLoadPath(object):
                    """
                    SDR load paths
                    
                    .. attribute:: load_path
                    
                    	Load path
                    	**type**\: list of    :py:class:`LoadPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Active.Summary.SdrLoadPath.LoadPath>`
                    
                    .. attribute:: request_id
                    
                    	Install op affecting scope
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: secure_domain_router_name
                    
                    	SDR name
                    	**type**\:  str
                    
                    .. attribute:: standby_load_path
                    
                    	Load paths for standby nodes
                    	**type**\: list of    :py:class:`StandbyLoadPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Active.Summary.SdrLoadPath.StandbyLoadPath>`
                    
                    

                    """

                    _prefix = 'installmgr-admin-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.load_path = YList()
                        self.load_path.parent = self
                        self.load_path.name = 'load_path'
                        self.request_id = None
                        self.secure_domain_router_name = None
                        self.standby_load_path = YList()
                        self.standby_load_path.parent = self
                        self.standby_load_path.name = 'standby_load_path'


                    class LoadPath(object):
                        """
                        Load path
                        
                        .. attribute:: build_information
                        
                        	Build information
                        	**type**\:  str
                        
                        .. attribute:: package
                        
                        	Package
                        	**type**\:   :py:class:`Package <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Active.Summary.SdrLoadPath.LoadPath.Package>`
                        
                        .. attribute:: version
                        
                        	Version
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'installmgr-admin-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.build_information = None
                            self.package = Install.SoftwareInventory.Active.Summary.SdrLoadPath.LoadPath.Package()
                            self.package.parent = self
                            self.version = None


                        class Package(object):
                            """
                            Package
                            
                            .. attribute:: device_name
                            
                            	Device name
                            	**type**\:  str
                            
                            .. attribute:: name
                            
                            	Package group name
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'installmgr-admin-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.device_name = None
                                self.name = None

                            @property
                            def _common_path(self):

                                return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:software-inventory/Cisco-IOS-XR-installmgr-admin-oper:active/Cisco-IOS-XR-installmgr-admin-oper:summary/Cisco-IOS-XR-installmgr-admin-oper:sdr-load-path/Cisco-IOS-XR-installmgr-admin-oper:load-path/Cisco-IOS-XR-installmgr-admin-oper:package'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.device_name is not None:
                                    return True

                                if self.name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                                return meta._meta_table['Install.SoftwareInventory.Active.Summary.SdrLoadPath.LoadPath.Package']['meta_info']

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:software-inventory/Cisco-IOS-XR-installmgr-admin-oper:active/Cisco-IOS-XR-installmgr-admin-oper:summary/Cisco-IOS-XR-installmgr-admin-oper:sdr-load-path/Cisco-IOS-XR-installmgr-admin-oper:load-path'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.build_information is not None:
                                return True

                            if self.package is not None and self.package._has_data():
                                return True

                            if self.version is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                            return meta._meta_table['Install.SoftwareInventory.Active.Summary.SdrLoadPath.LoadPath']['meta_info']


                    class StandbyLoadPath(object):
                        """
                        Load paths for standby nodes
                        
                        .. attribute:: build_information
                        
                        	Build information
                        	**type**\:  str
                        
                        .. attribute:: package
                        
                        	Package
                        	**type**\:   :py:class:`Package <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Active.Summary.SdrLoadPath.StandbyLoadPath.Package>`
                        
                        .. attribute:: version
                        
                        	Version
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'installmgr-admin-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.build_information = None
                            self.package = Install.SoftwareInventory.Active.Summary.SdrLoadPath.StandbyLoadPath.Package()
                            self.package.parent = self
                            self.version = None


                        class Package(object):
                            """
                            Package
                            
                            .. attribute:: device_name
                            
                            	Device name
                            	**type**\:  str
                            
                            .. attribute:: name
                            
                            	Package group name
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'installmgr-admin-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.device_name = None
                                self.name = None

                            @property
                            def _common_path(self):

                                return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:software-inventory/Cisco-IOS-XR-installmgr-admin-oper:active/Cisco-IOS-XR-installmgr-admin-oper:summary/Cisco-IOS-XR-installmgr-admin-oper:sdr-load-path/Cisco-IOS-XR-installmgr-admin-oper:standby-load-path/Cisco-IOS-XR-installmgr-admin-oper:package'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.device_name is not None:
                                    return True

                                if self.name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                                return meta._meta_table['Install.SoftwareInventory.Active.Summary.SdrLoadPath.StandbyLoadPath.Package']['meta_info']

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:software-inventory/Cisco-IOS-XR-installmgr-admin-oper:active/Cisco-IOS-XR-installmgr-admin-oper:summary/Cisco-IOS-XR-installmgr-admin-oper:sdr-load-path/Cisco-IOS-XR-installmgr-admin-oper:standby-load-path'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.build_information is not None:
                                return True

                            if self.package is not None and self.package._has_data():
                                return True

                            if self.version is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                            return meta._meta_table['Install.SoftwareInventory.Active.Summary.SdrLoadPath.StandbyLoadPath']['meta_info']

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:software-inventory/Cisco-IOS-XR-installmgr-admin-oper:active/Cisco-IOS-XR-installmgr-admin-oper:summary/Cisco-IOS-XR-installmgr-admin-oper:sdr-load-path'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.load_path is not None:
                            for child_ref in self.load_path:
                                if child_ref._has_data():
                                    return True

                        if self.request_id is not None:
                            return True

                        if self.secure_domain_router_name is not None:
                            return True

                        if self.standby_load_path is not None:
                            for child_ref in self.standby_load_path:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                        return meta._meta_table['Install.SoftwareInventory.Active.Summary.SdrLoadPath']['meta_info']


                class LocationLoadPath(object):
                    """
                    Location load paths
                    
                    .. attribute:: load_path
                    
                    	Load path
                    	**type**\: list of    :py:class:`LoadPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Active.Summary.LocationLoadPath.LoadPath>`
                    
                    .. attribute:: node_name
                    
                    	Node identifier
                    	**type**\:  str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    .. attribute:: request_id
                    
                    	Install op affecting scope
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: secure_domain_router_name
                    
                    	SDR name
                    	**type**\:  str
                    
                    .. attribute:: standby_load_path
                    
                    	Load paths for standby nodes
                    	**type**\: list of    :py:class:`StandbyLoadPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Active.Summary.LocationLoadPath.StandbyLoadPath>`
                    
                    

                    """

                    _prefix = 'installmgr-admin-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.load_path = YList()
                        self.load_path.parent = self
                        self.load_path.name = 'load_path'
                        self.node_name = None
                        self.request_id = None
                        self.secure_domain_router_name = None
                        self.standby_load_path = YList()
                        self.standby_load_path.parent = self
                        self.standby_load_path.name = 'standby_load_path'


                    class LoadPath(object):
                        """
                        Load path
                        
                        .. attribute:: build_information
                        
                        	Build information
                        	**type**\:  str
                        
                        .. attribute:: package
                        
                        	Package
                        	**type**\:   :py:class:`Package <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Active.Summary.LocationLoadPath.LoadPath.Package>`
                        
                        .. attribute:: version
                        
                        	Version
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'installmgr-admin-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.build_information = None
                            self.package = Install.SoftwareInventory.Active.Summary.LocationLoadPath.LoadPath.Package()
                            self.package.parent = self
                            self.version = None


                        class Package(object):
                            """
                            Package
                            
                            .. attribute:: device_name
                            
                            	Device name
                            	**type**\:  str
                            
                            .. attribute:: name
                            
                            	Package group name
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'installmgr-admin-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.device_name = None
                                self.name = None

                            @property
                            def _common_path(self):

                                return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:software-inventory/Cisco-IOS-XR-installmgr-admin-oper:active/Cisco-IOS-XR-installmgr-admin-oper:summary/Cisco-IOS-XR-installmgr-admin-oper:location-load-path/Cisco-IOS-XR-installmgr-admin-oper:load-path/Cisco-IOS-XR-installmgr-admin-oper:package'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.device_name is not None:
                                    return True

                                if self.name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                                return meta._meta_table['Install.SoftwareInventory.Active.Summary.LocationLoadPath.LoadPath.Package']['meta_info']

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:software-inventory/Cisco-IOS-XR-installmgr-admin-oper:active/Cisco-IOS-XR-installmgr-admin-oper:summary/Cisco-IOS-XR-installmgr-admin-oper:location-load-path/Cisco-IOS-XR-installmgr-admin-oper:load-path'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.build_information is not None:
                                return True

                            if self.package is not None and self.package._has_data():
                                return True

                            if self.version is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                            return meta._meta_table['Install.SoftwareInventory.Active.Summary.LocationLoadPath.LoadPath']['meta_info']


                    class StandbyLoadPath(object):
                        """
                        Load paths for standby nodes
                        
                        .. attribute:: build_information
                        
                        	Build information
                        	**type**\:  str
                        
                        .. attribute:: package
                        
                        	Package
                        	**type**\:   :py:class:`Package <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Active.Summary.LocationLoadPath.StandbyLoadPath.Package>`
                        
                        .. attribute:: version
                        
                        	Version
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'installmgr-admin-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.build_information = None
                            self.package = Install.SoftwareInventory.Active.Summary.LocationLoadPath.StandbyLoadPath.Package()
                            self.package.parent = self
                            self.version = None


                        class Package(object):
                            """
                            Package
                            
                            .. attribute:: device_name
                            
                            	Device name
                            	**type**\:  str
                            
                            .. attribute:: name
                            
                            	Package group name
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'installmgr-admin-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.device_name = None
                                self.name = None

                            @property
                            def _common_path(self):

                                return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:software-inventory/Cisco-IOS-XR-installmgr-admin-oper:active/Cisco-IOS-XR-installmgr-admin-oper:summary/Cisco-IOS-XR-installmgr-admin-oper:location-load-path/Cisco-IOS-XR-installmgr-admin-oper:standby-load-path/Cisco-IOS-XR-installmgr-admin-oper:package'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.device_name is not None:
                                    return True

                                if self.name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                                return meta._meta_table['Install.SoftwareInventory.Active.Summary.LocationLoadPath.StandbyLoadPath.Package']['meta_info']

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:software-inventory/Cisco-IOS-XR-installmgr-admin-oper:active/Cisco-IOS-XR-installmgr-admin-oper:summary/Cisco-IOS-XR-installmgr-admin-oper:location-load-path/Cisco-IOS-XR-installmgr-admin-oper:standby-load-path'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.build_information is not None:
                                return True

                            if self.package is not None and self.package._has_data():
                                return True

                            if self.version is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                            return meta._meta_table['Install.SoftwareInventory.Active.Summary.LocationLoadPath.StandbyLoadPath']['meta_info']

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:software-inventory/Cisco-IOS-XR-installmgr-admin-oper:active/Cisco-IOS-XR-installmgr-admin-oper:summary/Cisco-IOS-XR-installmgr-admin-oper:location-load-path'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.load_path is not None:
                            for child_ref in self.load_path:
                                if child_ref._has_data():
                                    return True

                        if self.node_name is not None:
                            return True

                        if self.request_id is not None:
                            return True

                        if self.secure_domain_router_name is not None:
                            return True

                        if self.standby_load_path is not None:
                            for child_ref in self.standby_load_path:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                        return meta._meta_table['Install.SoftwareInventory.Active.Summary.LocationLoadPath']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:software-inventory/Cisco-IOS-XR-installmgr-admin-oper:active/Cisco-IOS-XR-installmgr-admin-oper:summary'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.admin_load_path is not None and self.admin_load_path._has_data():
                        return True

                    if self.default_load_path is not None and self.default_load_path._has_data():
                        return True

                    if self.location_load_path is not None:
                        for child_ref in self.location_load_path:
                            if child_ref._has_data():
                                return True

                    if self.sdr_load_path is not None:
                        for child_ref in self.sdr_load_path:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                    return meta._meta_table['Install.SoftwareInventory.Active.Summary']['meta_info']


            class Inventories(object):
                """
                Software inventory
                
                .. attribute:: inventory
                
                	Inventory information for specific node
                	**type**\: list of    :py:class:`Inventory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Active.Inventories.Inventory>`
                
                

                """

                _prefix = 'installmgr-admin-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.inventory = YList()
                    self.inventory.parent = self
                    self.inventory.name = 'inventory'


                class Inventory(object):
                    """
                    Inventory information for specific node
                    
                    .. attribute:: node_name  <key>
                    
                    	Node name
                    	**type**\:  str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    .. attribute:: boot_image_name
                    
                    	Name of the boot image
                    	**type**\:  str
                    
                    .. attribute:: load_path
                    
                    	Load path
                    	**type**\: list of    :py:class:`LoadPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Active.Inventories.Inventory.LoadPath>`
                    
                    .. attribute:: major
                    
                    	Major data version number
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: minor
                    
                    	Minor data version number
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: node_type
                    
                    	Node's type
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: secure_domain_router_name
                    
                    	SDR name
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'installmgr-admin-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.node_name = None
                        self.boot_image_name = None
                        self.load_path = YList()
                        self.load_path.parent = self
                        self.load_path.name = 'load_path'
                        self.major = None
                        self.minor = None
                        self.node_type = None
                        self.secure_domain_router_name = None


                    class LoadPath(object):
                        """
                        Load path
                        
                        .. attribute:: build_information
                        
                        	Build information
                        	**type**\:  str
                        
                        .. attribute:: package
                        
                        	Package
                        	**type**\:   :py:class:`Package <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.SoftwareInventory.Active.Inventories.Inventory.LoadPath.Package>`
                        
                        .. attribute:: version
                        
                        	Version
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'installmgr-admin-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.build_information = None
                            self.package = Install.SoftwareInventory.Active.Inventories.Inventory.LoadPath.Package()
                            self.package.parent = self
                            self.version = None


                        class Package(object):
                            """
                            Package
                            
                            .. attribute:: device_name
                            
                            	Device name
                            	**type**\:  str
                            
                            .. attribute:: name
                            
                            	Package group name
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'installmgr-admin-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.device_name = None
                                self.name = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-installmgr-admin-oper:package'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.device_name is not None:
                                    return True

                                if self.name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                                return meta._meta_table['Install.SoftwareInventory.Active.Inventories.Inventory.LoadPath.Package']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-installmgr-admin-oper:load-path'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.build_information is not None:
                                return True

                            if self.package is not None and self.package._has_data():
                                return True

                            if self.version is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                            return meta._meta_table['Install.SoftwareInventory.Active.Inventories.Inventory.LoadPath']['meta_info']

                    @property
                    def _common_path(self):
                        if self.node_name is None:
                            raise YPYModelError('Key property node_name is None')

                        return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:software-inventory/Cisco-IOS-XR-installmgr-admin-oper:active/Cisco-IOS-XR-installmgr-admin-oper:inventories/Cisco-IOS-XR-installmgr-admin-oper:inventory[Cisco-IOS-XR-installmgr-admin-oper:node-name = ' + str(self.node_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.node_name is not None:
                            return True

                        if self.boot_image_name is not None:
                            return True

                        if self.load_path is not None:
                            for child_ref in self.load_path:
                                if child_ref._has_data():
                                    return True

                        if self.major is not None:
                            return True

                        if self.minor is not None:
                            return True

                        if self.node_type is not None:
                            return True

                        if self.secure_domain_router_name is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                        return meta._meta_table['Install.SoftwareInventory.Active.Inventories.Inventory']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:software-inventory/Cisco-IOS-XR-installmgr-admin-oper:active/Cisco-IOS-XR-installmgr-admin-oper:inventories'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.inventory is not None:
                        for child_ref in self.inventory:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                    return meta._meta_table['Install.SoftwareInventory.Active.Inventories']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:software-inventory/Cisco-IOS-XR-installmgr-admin-oper:active'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.inventories is not None and self.inventories._has_data():
                    return True

                if self.summary is not None and self.summary._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                return meta._meta_table['Install.SoftwareInventory.Active']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:software-inventory'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.active is not None and self.active._has_data():
                return True

            if self.committed is not None and self.committed._has_data():
                return True

            if self.inactive is not None and self.inactive._has_data():
                return True

            if self.requests is not None and self.requests._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
            return meta._meta_table['Install.SoftwareInventory']['meta_info']


    class Issu(object):
        """
        Information of install ISSU operations
        
        .. attribute:: card_inventories
        
        	ISSU manager card inventory table
        	**type**\:   :py:class:`CardInventories <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Issu.CardInventories>`
        
        .. attribute:: stage
        
        	Summarized ISSU stage information
        	**type**\:   :py:class:`Stage <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Issu.Stage>`
        
        

        """

        _prefix = 'installmgr-admin-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.card_inventories = Install.Issu.CardInventories()
            self.card_inventories.parent = self
            self.stage = Install.Issu.Stage()
            self.stage.parent = self


        class CardInventories(object):
            """
            ISSU manager card inventory table
            
            .. attribute:: card_inventory
            
            	ISSU manager inventory summary of the same card type
            	**type**\: list of    :py:class:`CardInventory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Issu.CardInventories.CardInventory>`
            
            

            """

            _prefix = 'installmgr-admin-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.card_inventory = YList()
                self.card_inventory.parent = self
                self.card_inventory.name = 'card_inventory'


            class CardInventory(object):
                """
                ISSU manager inventory summary of the same
                card type
                
                .. attribute:: card_type_id  <key>
                
                	ISSU manager card type ID
                	**type**\:   :py:class:`IsmCardTypeFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.IsmCardTypeFamilyEnum>`
                
                .. attribute:: summary
                
                	node state for all nodes
                	**type**\: list of    :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Issu.CardInventories.CardInventory.Summary>`
                
                

                """

                _prefix = 'installmgr-admin-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.card_type_id = None
                    self.summary = YList()
                    self.summary.parent = self
                    self.summary.name = 'summary'


                class Summary(object):
                    """
                    node state for all nodes
                    
                    .. attribute:: attempts
                    
                    	Number of attempts made
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: is_conforming_node
                    
                    	Node none\-cnforming
                    	**type**\:   :py:class:`InstallmgrIsmNodeConformingEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.InstallmgrIsmNodeConformingEnum>`
                    
                    .. attribute:: is_node_upgraded
                    
                    	Is node upgraded?
                    	**type**\:  bool
                    
                    .. attribute:: node_current_state
                    
                    	Current node ISSU state
                    	**type**\:   :py:class:`InstmgrIsmNodeStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.InstmgrIsmNodeStateEnum>`
                    
                    .. attribute:: node_expected_state
                    
                    	Expected ISSU state
                    	**type**\:   :py:class:`InstmgrIsmNodeStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.InstmgrIsmNodeStateEnum>`
                    
                    .. attribute:: node_failure_reason
                    
                    	Node failure reason
                    	**type**\:  str
                    
                    .. attribute:: node_name
                    
                    	Node identifier
                    	**type**\:  str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    .. attribute:: node_role
                    
                    	Node roll
                    	**type**\:   :py:class:`InstmgrNodeRoleEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.InstmgrNodeRoleEnum>`
                    
                    .. attribute:: node_state
                    
                    	Node state
                    	**type**\:   :py:class:`InstmgrCardStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.InstmgrCardStateEnum>`
                    
                    .. attribute:: node_type_issu
                    
                    	ISSU node type
                    	**type**\:  str
                    
                    .. attribute:: node_type_pi
                    
                    	PI Node type
                    	**type**\:   :py:class:`InstmgrPiCardEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.InstmgrPiCardEnum>`
                    
                    .. attribute:: partner_node_name
                    
                    	Partner Node IDs
                    	**type**\:  str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    

                    """

                    _prefix = 'installmgr-admin-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.attempts = None
                        self.is_conforming_node = None
                        self.is_node_upgraded = None
                        self.node_current_state = None
                        self.node_expected_state = None
                        self.node_failure_reason = None
                        self.node_name = None
                        self.node_role = None
                        self.node_state = None
                        self.node_type_issu = None
                        self.node_type_pi = None
                        self.partner_node_name = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-installmgr-admin-oper:summary'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.attempts is not None:
                            return True

                        if self.is_conforming_node is not None:
                            return True

                        if self.is_node_upgraded is not None:
                            return True

                        if self.node_current_state is not None:
                            return True

                        if self.node_expected_state is not None:
                            return True

                        if self.node_failure_reason is not None:
                            return True

                        if self.node_name is not None:
                            return True

                        if self.node_role is not None:
                            return True

                        if self.node_state is not None:
                            return True

                        if self.node_type_issu is not None:
                            return True

                        if self.node_type_pi is not None:
                            return True

                        if self.partner_node_name is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                        return meta._meta_table['Install.Issu.CardInventories.CardInventory.Summary']['meta_info']

                @property
                def _common_path(self):
                    if self.card_type_id is None:
                        raise YPYModelError('Key property card_type_id is None')

                    return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:issu/Cisco-IOS-XR-installmgr-admin-oper:card-inventories/Cisco-IOS-XR-installmgr-admin-oper:card-inventory[Cisco-IOS-XR-installmgr-admin-oper:card-type-id = ' + str(self.card_type_id) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.card_type_id is not None:
                        return True

                    if self.summary is not None:
                        for child_ref in self.summary:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                    return meta._meta_table['Install.Issu.CardInventories.CardInventory']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:issu/Cisco-IOS-XR-installmgr-admin-oper:card-inventories'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.card_inventory is not None:
                    for child_ref in self.card_inventory:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                return meta._meta_table['Install.Issu.CardInventories']['meta_info']


        class Stage(object):
            """
            Summarized ISSU stage information
            
            .. attribute:: is_issu_aborted
            
            	ISSU aborted?
            	**type**\:  bool
            
            .. attribute:: is_issu_aborted_by_ism
            
            	ISSU aborted by ISM?
            	**type**\:  bool
            
            .. attribute:: issu_manager_fsm_state
            
            	ISM FSM state
            	**type**\:   :py:class:`InstmgrIsmFsmStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.InstmgrIsmFsmStateEnum>`
            
            .. attribute:: issu_op_id
            
            	ISSU operational ID
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: issu_state
            
            	Current ISSU state
            	**type**\:  str
            
            .. attribute:: nc_nodes
            
            	None\-conforming nodes
            	**type**\:   :py:class:`NcNodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Issu.Stage.NcNodes>`
            
            .. attribute:: node_in_progress
            
            	Nodes in progress
            	**type**\:   :py:class:`NodeInProgress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Issu.Stage.NodeInProgress>`
            
            .. attribute:: nodes_in_load
            
            	Node in LOAD phase
            	**type**\:   :py:class:`NodesInLoad <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Issu.Stage.NodesInLoad>`
            
            .. attribute:: nodes_in_run
            
            	Node in RUN phase
            	**type**\:   :py:class:`NodesInRun <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Issu.Stage.NodesInRun>`
            
            .. attribute:: num_nodes_in_progress
            
            	Number of node in progress
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: num_of_nodes_in_load
            
            	Number of nodes in LOAD phase
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: num_of_nodes_in_run
            
            	Number of nodes in RUN phase
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: numof_nc_nodes
            
            	Number of none\-conforming nodes
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: participating_node_all
            
            	Number of participating nodes
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: percentage
            
            	ISSU progress percentage
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: percentage
            
            

            """

            _prefix = 'installmgr-admin-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.is_issu_aborted = None
                self.is_issu_aborted_by_ism = None
                self.issu_manager_fsm_state = None
                self.issu_op_id = None
                self.issu_state = None
                self.nc_nodes = Install.Issu.Stage.NcNodes()
                self.nc_nodes.parent = self
                self.node_in_progress = Install.Issu.Stage.NodeInProgress()
                self.node_in_progress.parent = self
                self.nodes_in_load = Install.Issu.Stage.NodesInLoad()
                self.nodes_in_load.parent = self
                self.nodes_in_run = Install.Issu.Stage.NodesInRun()
                self.nodes_in_run.parent = self
                self.num_nodes_in_progress = None
                self.num_of_nodes_in_load = None
                self.num_of_nodes_in_run = None
                self.numof_nc_nodes = None
                self.participating_node_all = None
                self.percentage = None


            class NodeInProgress(object):
                """
                Nodes in progress
                
                .. attribute:: node
                
                	node
                	**type**\:  list of str
                
                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                
                

                """

                _prefix = 'installmgr-admin-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.node = YLeafList()
                    self.node.parent = self
                    self.node.name = 'node'

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:issu/Cisco-IOS-XR-installmgr-admin-oper:stage/Cisco-IOS-XR-installmgr-admin-oper:node-in-progress'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.node is not None:
                        for child in self.node:
                            if child is not None:
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                    return meta._meta_table['Install.Issu.Stage.NodeInProgress']['meta_info']


            class NodesInLoad(object):
                """
                Node in LOAD phase
                
                .. attribute:: node
                
                	node
                	**type**\:  list of str
                
                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                
                

                """

                _prefix = 'installmgr-admin-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.node = YLeafList()
                    self.node.parent = self
                    self.node.name = 'node'

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:issu/Cisco-IOS-XR-installmgr-admin-oper:stage/Cisco-IOS-XR-installmgr-admin-oper:nodes-in-load'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.node is not None:
                        for child in self.node:
                            if child is not None:
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                    return meta._meta_table['Install.Issu.Stage.NodesInLoad']['meta_info']


            class NodesInRun(object):
                """
                Node in RUN phase
                
                .. attribute:: node
                
                	node
                	**type**\:  list of str
                
                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                
                

                """

                _prefix = 'installmgr-admin-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.node = YLeafList()
                    self.node.parent = self
                    self.node.name = 'node'

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:issu/Cisco-IOS-XR-installmgr-admin-oper:stage/Cisco-IOS-XR-installmgr-admin-oper:nodes-in-run'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.node is not None:
                        for child in self.node:
                            if child is not None:
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                    return meta._meta_table['Install.Issu.Stage.NodesInRun']['meta_info']


            class NcNodes(object):
                """
                None\-conforming nodes
                
                .. attribute:: node
                
                	node
                	**type**\:  list of str
                
                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                
                

                """

                _prefix = 'installmgr-admin-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.node = YLeafList()
                    self.node.parent = self
                    self.node.name = 'node'

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:issu/Cisco-IOS-XR-installmgr-admin-oper:stage/Cisco-IOS-XR-installmgr-admin-oper:nc-nodes'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.node is not None:
                        for child in self.node:
                            if child is not None:
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                    return meta._meta_table['Install.Issu.Stage.NcNodes']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:issu/Cisco-IOS-XR-installmgr-admin-oper:stage'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.is_issu_aborted is not None:
                    return True

                if self.is_issu_aborted_by_ism is not None:
                    return True

                if self.issu_manager_fsm_state is not None:
                    return True

                if self.issu_op_id is not None:
                    return True

                if self.issu_state is not None:
                    return True

                if self.nc_nodes is not None and self.nc_nodes._has_data():
                    return True

                if self.node_in_progress is not None and self.node_in_progress._has_data():
                    return True

                if self.nodes_in_load is not None and self.nodes_in_load._has_data():
                    return True

                if self.nodes_in_run is not None and self.nodes_in_run._has_data():
                    return True

                if self.num_nodes_in_progress is not None:
                    return True

                if self.num_of_nodes_in_load is not None:
                    return True

                if self.num_of_nodes_in_run is not None:
                    return True

                if self.numof_nc_nodes is not None:
                    return True

                if self.participating_node_all is not None:
                    return True

                if self.percentage is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                return meta._meta_table['Install.Issu.Stage']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:issu'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.card_inventories is not None and self.card_inventories._has_data():
                return True

            if self.stage is not None and self.stage._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
            return meta._meta_table['Install.Issu']['meta_info']


    class BootImage(object):
        """
        System Boot Image
        
        .. attribute:: system_image_file
        
        	The boot image
        	**type**\:  str
        
        

        """

        _prefix = 'installmgr-admin-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.system_image_file = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:boot-image'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.system_image_file is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
            return meta._meta_table['Install.BootImage']['meta_info']


    class Logs(object):
        """
        Install operation log
        
        .. attribute:: log
        
        	Log information
        	**type**\: list of    :py:class:`Log <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Logs.Log>`
        
        

        """

        _prefix = 'installmgr-admin-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.log = YList()
            self.log.parent = self
            self.log.name = 'log'


        class Log(object):
            """
            Log information
            
            .. attribute:: request_id  <key>
            
            	Install operation request ID
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: change
            
            	Install changes
            	**type**\: list of    :py:class:`Change <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Logs.Log.Change>`
            
            .. attribute:: communication
            
            	Install communications
            	**type**\: list of    :py:class:`Communication <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Logs.Log.Communication>`
            
            .. attribute:: detail
            
            	Install details
            	**type**\: list of    :py:class:`Detail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Logs.Log.Detail>`
            
            .. attribute:: header
            
            	Header information
            	**type**\: list of    :py:class:`Header <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Logs.Log.Header>`
            
            .. attribute:: message
            
            	Status Information Logs
            	**type**\: list of    :py:class:`Message <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Logs.Log.Message>`
            
            .. attribute:: summary
            
            	Summary information
            	**type**\: list of    :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Logs.Log.Summary>`
            
            

            """

            _prefix = 'installmgr-admin-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.request_id = None
                self.change = YList()
                self.change.parent = self
                self.change.name = 'change'
                self.communication = YList()
                self.communication.parent = self
                self.communication.name = 'communication'
                self.detail = YList()
                self.detail.parent = self
                self.detail.name = 'detail'
                self.header = YList()
                self.header.parent = self
                self.header.name = 'header'
                self.message = YList()
                self.message.parent = self
                self.message.name = 'message'
                self.summary = YList()
                self.summary.parent = self
                self.summary.name = 'summary'


            class Header(object):
                """
                Header information
                
                .. attribute:: log_contents
                
                	Log contents
                	**type**\:   :py:class:`LogContents <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Logs.Log.Header.LogContents>`
                
                

                """

                _prefix = 'installmgr-admin-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.log_contents = Install.Logs.Log.Header.LogContents()
                    self.log_contents.parent = self


                class LogContents(object):
                    """
                    Log contents
                    
                    .. attribute:: v3
                    
                    	v3
                    	**type**\:   :py:class:`V3 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Logs.Log.Header.LogContents.V3>`
                    
                    .. attribute:: version
                    
                    	Version
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'installmgr-admin-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.v3 = Install.Logs.Log.Header.LogContents.V3()
                        self.v3.parent = self
                        self.version = None


                    class V3(object):
                        """
                        v3
                        
                        .. attribute:: category
                        
                        	Category of the message
                        	**type**\:   :py:class:`InstmgrBagLogEntryUserMsgCategoryEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.InstmgrBagLogEntryUserMsgCategoryEnum>`
                        
                        .. attribute:: message
                        
                        	Message
                        	**type**\:  str
                        
                        .. attribute:: scope
                        
                        	Scope of the message
                        	**type**\:   :py:class:`Scope <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Logs.Log.Header.LogContents.V3.Scope>`
                        
                        

                        """

                        _prefix = 'installmgr-admin-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.category = None
                            self.message = None
                            self.scope = Install.Logs.Log.Header.LogContents.V3.Scope()
                            self.scope.parent = self


                        class Scope(object):
                            """
                            Scope of the message
                            
                            .. attribute:: admin_read
                            
                            	Does the admin want to read this?
                            	**type**\:  bool
                            
                            .. attribute:: affected_sd_rs
                            
                            	Which SDRs are affected by the message
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'installmgr-admin-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.admin_read = None
                                self.affected_sd_rs = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-installmgr-admin-oper:scope'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.admin_read is not None:
                                    return True

                                if self.affected_sd_rs is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                                return meta._meta_table['Install.Logs.Log.Header.LogContents.V3.Scope']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-installmgr-admin-oper:v3'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.category is not None:
                                return True

                            if self.message is not None:
                                return True

                            if self.scope is not None and self.scope._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                            return meta._meta_table['Install.Logs.Log.Header.LogContents.V3']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-installmgr-admin-oper:log-contents'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.v3 is not None and self.v3._has_data():
                            return True

                        if self.version is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                        return meta._meta_table['Install.Logs.Log.Header.LogContents']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-installmgr-admin-oper:header'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.log_contents is not None and self.log_contents._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                    return meta._meta_table['Install.Logs.Log.Header']['meta_info']


            class Summary(object):
                """
                Summary information
                
                .. attribute:: log_contents
                
                	Log contents
                	**type**\:   :py:class:`LogContents <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Logs.Log.Summary.LogContents>`
                
                

                """

                _prefix = 'installmgr-admin-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.log_contents = Install.Logs.Log.Summary.LogContents()
                    self.log_contents.parent = self


                class LogContents(object):
                    """
                    Log contents
                    
                    .. attribute:: v3
                    
                    	v3
                    	**type**\:   :py:class:`V3 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Logs.Log.Summary.LogContents.V3>`
                    
                    .. attribute:: version
                    
                    	Version
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'installmgr-admin-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.v3 = Install.Logs.Log.Summary.LogContents.V3()
                        self.v3.parent = self
                        self.version = None


                    class V3(object):
                        """
                        v3
                        
                        .. attribute:: category
                        
                        	Category of the message
                        	**type**\:   :py:class:`InstmgrBagLogEntryUserMsgCategoryEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.InstmgrBagLogEntryUserMsgCategoryEnum>`
                        
                        .. attribute:: message
                        
                        	Message
                        	**type**\:  str
                        
                        .. attribute:: scope
                        
                        	Scope of the message
                        	**type**\:   :py:class:`Scope <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Logs.Log.Summary.LogContents.V3.Scope>`
                        
                        

                        """

                        _prefix = 'installmgr-admin-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.category = None
                            self.message = None
                            self.scope = Install.Logs.Log.Summary.LogContents.V3.Scope()
                            self.scope.parent = self


                        class Scope(object):
                            """
                            Scope of the message
                            
                            .. attribute:: admin_read
                            
                            	Does the admin want to read this?
                            	**type**\:  bool
                            
                            .. attribute:: affected_sd_rs
                            
                            	Which SDRs are affected by the message
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'installmgr-admin-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.admin_read = None
                                self.affected_sd_rs = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-installmgr-admin-oper:scope'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.admin_read is not None:
                                    return True

                                if self.affected_sd_rs is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                                return meta._meta_table['Install.Logs.Log.Summary.LogContents.V3.Scope']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-installmgr-admin-oper:v3'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.category is not None:
                                return True

                            if self.message is not None:
                                return True

                            if self.scope is not None and self.scope._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                            return meta._meta_table['Install.Logs.Log.Summary.LogContents.V3']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-installmgr-admin-oper:log-contents'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.v3 is not None and self.v3._has_data():
                            return True

                        if self.version is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                        return meta._meta_table['Install.Logs.Log.Summary.LogContents']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-installmgr-admin-oper:summary'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.log_contents is not None and self.log_contents._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                    return meta._meta_table['Install.Logs.Log.Summary']['meta_info']


            class Message(object):
                """
                Status Information Logs
                
                .. attribute:: log_contents
                
                	Log contents
                	**type**\:   :py:class:`LogContents <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Logs.Log.Message.LogContents>`
                
                

                """

                _prefix = 'installmgr-admin-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.log_contents = Install.Logs.Log.Message.LogContents()
                    self.log_contents.parent = self


                class LogContents(object):
                    """
                    Log contents
                    
                    .. attribute:: v3
                    
                    	v3
                    	**type**\:   :py:class:`V3 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Logs.Log.Message.LogContents.V3>`
                    
                    .. attribute:: version
                    
                    	Version
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'installmgr-admin-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.v3 = Install.Logs.Log.Message.LogContents.V3()
                        self.v3.parent = self
                        self.version = None


                    class V3(object):
                        """
                        v3
                        
                        .. attribute:: category
                        
                        	Category of the message
                        	**type**\:   :py:class:`InstmgrBagLogEntryUserMsgCategoryEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.InstmgrBagLogEntryUserMsgCategoryEnum>`
                        
                        .. attribute:: message
                        
                        	Message
                        	**type**\:  str
                        
                        .. attribute:: scope
                        
                        	Scope of the message
                        	**type**\:   :py:class:`Scope <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Logs.Log.Message.LogContents.V3.Scope>`
                        
                        

                        """

                        _prefix = 'installmgr-admin-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.category = None
                            self.message = None
                            self.scope = Install.Logs.Log.Message.LogContents.V3.Scope()
                            self.scope.parent = self


                        class Scope(object):
                            """
                            Scope of the message
                            
                            .. attribute:: admin_read
                            
                            	Does the admin want to read this?
                            	**type**\:  bool
                            
                            .. attribute:: affected_sd_rs
                            
                            	Which SDRs are affected by the message
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'installmgr-admin-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.admin_read = None
                                self.affected_sd_rs = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-installmgr-admin-oper:scope'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.admin_read is not None:
                                    return True

                                if self.affected_sd_rs is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                                return meta._meta_table['Install.Logs.Log.Message.LogContents.V3.Scope']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-installmgr-admin-oper:v3'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.category is not None:
                                return True

                            if self.message is not None:
                                return True

                            if self.scope is not None and self.scope._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                            return meta._meta_table['Install.Logs.Log.Message.LogContents.V3']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-installmgr-admin-oper:log-contents'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.v3 is not None and self.v3._has_data():
                            return True

                        if self.version is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                        return meta._meta_table['Install.Logs.Log.Message.LogContents']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-installmgr-admin-oper:message'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.log_contents is not None and self.log_contents._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                    return meta._meta_table['Install.Logs.Log.Message']['meta_info']


            class Change(object):
                """
                Install changes
                
                .. attribute:: log_contents
                
                	Log contents
                	**type**\:   :py:class:`LogContents <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Logs.Log.Change.LogContents>`
                
                

                """

                _prefix = 'installmgr-admin-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.log_contents = Install.Logs.Log.Change.LogContents()
                    self.log_contents.parent = self


                class LogContents(object):
                    """
                    Log contents
                    
                    .. attribute:: v3
                    
                    	v3
                    	**type**\:   :py:class:`V3 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Logs.Log.Change.LogContents.V3>`
                    
                    .. attribute:: version
                    
                    	Version
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'installmgr-admin-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.v3 = Install.Logs.Log.Change.LogContents.V3()
                        self.v3.parent = self
                        self.version = None


                    class V3(object):
                        """
                        v3
                        
                        .. attribute:: category
                        
                        	Category of the message
                        	**type**\:   :py:class:`InstmgrBagLogEntryUserMsgCategoryEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.InstmgrBagLogEntryUserMsgCategoryEnum>`
                        
                        .. attribute:: message
                        
                        	Message
                        	**type**\:  str
                        
                        .. attribute:: scope
                        
                        	Scope of the message
                        	**type**\:   :py:class:`Scope <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Logs.Log.Change.LogContents.V3.Scope>`
                        
                        

                        """

                        _prefix = 'installmgr-admin-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.category = None
                            self.message = None
                            self.scope = Install.Logs.Log.Change.LogContents.V3.Scope()
                            self.scope.parent = self


                        class Scope(object):
                            """
                            Scope of the message
                            
                            .. attribute:: admin_read
                            
                            	Does the admin want to read this?
                            	**type**\:  bool
                            
                            .. attribute:: affected_sd_rs
                            
                            	Which SDRs are affected by the message
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'installmgr-admin-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.admin_read = None
                                self.affected_sd_rs = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-installmgr-admin-oper:scope'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.admin_read is not None:
                                    return True

                                if self.affected_sd_rs is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                                return meta._meta_table['Install.Logs.Log.Change.LogContents.V3.Scope']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-installmgr-admin-oper:v3'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.category is not None:
                                return True

                            if self.message is not None:
                                return True

                            if self.scope is not None and self.scope._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                            return meta._meta_table['Install.Logs.Log.Change.LogContents.V3']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-installmgr-admin-oper:log-contents'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.v3 is not None and self.v3._has_data():
                            return True

                        if self.version is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                        return meta._meta_table['Install.Logs.Log.Change.LogContents']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-installmgr-admin-oper:change'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.log_contents is not None and self.log_contents._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                    return meta._meta_table['Install.Logs.Log.Change']['meta_info']


            class Detail(object):
                """
                Install details
                
                .. attribute:: log_contents
                
                	Log contents
                	**type**\:   :py:class:`LogContents <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Logs.Log.Detail.LogContents>`
                
                

                """

                _prefix = 'installmgr-admin-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.log_contents = Install.Logs.Log.Detail.LogContents()
                    self.log_contents.parent = self


                class LogContents(object):
                    """
                    Log contents
                    
                    .. attribute:: v3
                    
                    	v3
                    	**type**\:   :py:class:`V3 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Logs.Log.Detail.LogContents.V3>`
                    
                    .. attribute:: version
                    
                    	Version
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'installmgr-admin-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.v3 = Install.Logs.Log.Detail.LogContents.V3()
                        self.v3.parent = self
                        self.version = None


                    class V3(object):
                        """
                        v3
                        
                        .. attribute:: category
                        
                        	Category of the message
                        	**type**\:   :py:class:`InstmgrBagLogEntryUserMsgCategoryEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.InstmgrBagLogEntryUserMsgCategoryEnum>`
                        
                        .. attribute:: message
                        
                        	Message
                        	**type**\:  str
                        
                        .. attribute:: scope
                        
                        	Scope of the message
                        	**type**\:   :py:class:`Scope <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Logs.Log.Detail.LogContents.V3.Scope>`
                        
                        

                        """

                        _prefix = 'installmgr-admin-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.category = None
                            self.message = None
                            self.scope = Install.Logs.Log.Detail.LogContents.V3.Scope()
                            self.scope.parent = self


                        class Scope(object):
                            """
                            Scope of the message
                            
                            .. attribute:: admin_read
                            
                            	Does the admin want to read this?
                            	**type**\:  bool
                            
                            .. attribute:: affected_sd_rs
                            
                            	Which SDRs are affected by the message
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'installmgr-admin-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.admin_read = None
                                self.affected_sd_rs = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-installmgr-admin-oper:scope'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.admin_read is not None:
                                    return True

                                if self.affected_sd_rs is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                                return meta._meta_table['Install.Logs.Log.Detail.LogContents.V3.Scope']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-installmgr-admin-oper:v3'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.category is not None:
                                return True

                            if self.message is not None:
                                return True

                            if self.scope is not None and self.scope._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                            return meta._meta_table['Install.Logs.Log.Detail.LogContents.V3']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-installmgr-admin-oper:log-contents'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.v3 is not None and self.v3._has_data():
                            return True

                        if self.version is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                        return meta._meta_table['Install.Logs.Log.Detail.LogContents']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-installmgr-admin-oper:detail'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.log_contents is not None and self.log_contents._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                    return meta._meta_table['Install.Logs.Log.Detail']['meta_info']


            class Communication(object):
                """
                Install communications
                
                .. attribute:: log_contents
                
                	Log contents
                	**type**\:   :py:class:`LogContents <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Logs.Log.Communication.LogContents>`
                
                

                """

                _prefix = 'installmgr-admin-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.log_contents = Install.Logs.Log.Communication.LogContents()
                    self.log_contents.parent = self


                class LogContents(object):
                    """
                    Log contents
                    
                    .. attribute:: v3
                    
                    	v3
                    	**type**\:   :py:class:`V3 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Logs.Log.Communication.LogContents.V3>`
                    
                    .. attribute:: version
                    
                    	Version
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'installmgr-admin-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.v3 = Install.Logs.Log.Communication.LogContents.V3()
                        self.v3.parent = self
                        self.version = None


                    class V3(object):
                        """
                        v3
                        
                        .. attribute:: category
                        
                        	Category of the message
                        	**type**\:   :py:class:`InstmgrBagLogEntryUserMsgCategoryEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.InstmgrBagLogEntryUserMsgCategoryEnum>`
                        
                        .. attribute:: message
                        
                        	Message
                        	**type**\:  str
                        
                        .. attribute:: scope
                        
                        	Scope of the message
                        	**type**\:   :py:class:`Scope <ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper.Install.Logs.Log.Communication.LogContents.V3.Scope>`
                        
                        

                        """

                        _prefix = 'installmgr-admin-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.category = None
                            self.message = None
                            self.scope = Install.Logs.Log.Communication.LogContents.V3.Scope()
                            self.scope.parent = self


                        class Scope(object):
                            """
                            Scope of the message
                            
                            .. attribute:: admin_read
                            
                            	Does the admin want to read this?
                            	**type**\:  bool
                            
                            .. attribute:: affected_sd_rs
                            
                            	Which SDRs are affected by the message
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'installmgr-admin-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.admin_read = None
                                self.affected_sd_rs = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-installmgr-admin-oper:scope'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.admin_read is not None:
                                    return True

                                if self.affected_sd_rs is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                                return meta._meta_table['Install.Logs.Log.Communication.LogContents.V3.Scope']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-installmgr-admin-oper:v3'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.category is not None:
                                return True

                            if self.message is not None:
                                return True

                            if self.scope is not None and self.scope._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                            return meta._meta_table['Install.Logs.Log.Communication.LogContents.V3']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-installmgr-admin-oper:log-contents'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.v3 is not None and self.v3._has_data():
                            return True

                        if self.version is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                        return meta._meta_table['Install.Logs.Log.Communication.LogContents']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-installmgr-admin-oper:communication'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.log_contents is not None and self.log_contents._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                    return meta._meta_table['Install.Logs.Log.Communication']['meta_info']

            @property
            def _common_path(self):
                if self.request_id is None:
                    raise YPYModelError('Key property request_id is None')

                return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:logs/Cisco-IOS-XR-installmgr-admin-oper:log[Cisco-IOS-XR-installmgr-admin-oper:request-id = ' + str(self.request_id) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.request_id is not None:
                    return True

                if self.change is not None:
                    for child_ref in self.change:
                        if child_ref._has_data():
                            return True

                if self.communication is not None:
                    for child_ref in self.communication:
                        if child_ref._has_data():
                            return True

                if self.detail is not None:
                    for child_ref in self.detail:
                        if child_ref._has_data():
                            return True

                if self.header is not None:
                    for child_ref in self.header:
                        if child_ref._has_data():
                            return True

                if self.message is not None:
                    for child_ref in self.message:
                        if child_ref._has_data():
                            return True

                if self.summary is not None:
                    for child_ref in self.summary:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
                return meta._meta_table['Install.Logs.Log']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-installmgr-admin-oper:install/Cisco-IOS-XR-installmgr-admin-oper:logs'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.log is not None:
                for child_ref in self.log:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
            return meta._meta_table['Install.Logs']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-installmgr-admin-oper:install'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.boot_image is not None and self.boot_image._has_data():
            return True

        if self.boot_variables is not None and self.boot_variables._has_data():
            return True

        if self.configuration_registers is not None and self.configuration_registers._has_data():
            return True

        if self.issu is not None and self.issu._has_data():
            return True

        if self.log_size is not None:
            return True

        if self.logs is not None and self.logs._has_data():
            return True

        if self.request_statuses is not None and self.request_statuses._has_data():
            return True

        if self.software is not None and self.software._has_data():
            return True

        if self.software_inventory is not None and self.software_inventory._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_installmgr_admin_oper as meta
        return meta._meta_table['Install']['meta_info']


