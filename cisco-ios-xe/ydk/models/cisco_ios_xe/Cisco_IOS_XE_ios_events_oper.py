""" Cisco_IOS_XE_ios_events_oper 

This module contains a collection of YANG definitions
for asynchronous events from network element.
Copyright (c) 2016\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class BgpPstate(Enum):
    """
    BgpPstate (Enum Class)

    GGP state

    .. data:: bgp_state_idle = 0

    .. data:: bgp_state_connect = 1

    .. data:: bgp_state_active = 2

    .. data:: bgp_state_opensent = 3

    .. data:: bgp_state_openconfirm = 4

    .. data:: bgp_state_established = 5

    .. data:: bgp_state_clearing = 6

    .. data:: bgp_state_deleted = 7

    """

    bgp_state_idle = Enum.YLeaf(0, "bgp-state-idle")

    bgp_state_connect = Enum.YLeaf(1, "bgp-state-connect")

    bgp_state_active = Enum.YLeaf(2, "bgp-state-active")

    bgp_state_opensent = Enum.YLeaf(3, "bgp-state-opensent")

    bgp_state_openconfirm = Enum.YLeaf(4, "bgp-state-openconfirm")

    bgp_state_established = Enum.YLeaf(5, "bgp-state-established")

    bgp_state_clearing = Enum.YLeaf(6, "bgp-state-clearing")

    bgp_state_deleted = Enum.YLeaf(7, "bgp-state-deleted")


class DhcpServerStateVal(Enum):
    """
    DhcpServerStateVal (Enum Class)

    DHCP Server state

    .. data:: dhcp_server_state_up = 0

    .. data:: dhcp_server_state_down = 1

    """

    dhcp_server_state_up = Enum.YLeaf(0, "dhcp-server-state-up")

    dhcp_server_state_down = Enum.YLeaf(1, "dhcp-server-state-down")


class FibUpdatesAfType(Enum):
    """
    FibUpdatesAfType (Enum Class)

    FIB updates AF type

    .. data:: fib_updates_af_unknown = 0

    .. data:: fib_updates_af_ipv4 = 1

    .. data:: fib_updates_af_ipv6 = 2

    """

    fib_updates_af_unknown = Enum.YLeaf(0, "fib-updates-af-unknown")

    fib_updates_af_ipv4 = Enum.YLeaf(1, "fib-updates-af-ipv4")

    fib_updates_af_ipv6 = Enum.YLeaf(2, "fib-updates-af-ipv6")


class HardwareSensorType(Enum):
    """
    HardwareSensorType (Enum Class)

    Hardware Sensor Type

    .. data:: hw_sensor_board = 0

    	Hardware sensor board

    .. data:: hw_sensor_cpu_junction = 1

    	Hardware sensor CPU junction

    .. data:: hw_sensor_dram = 2

    	Hardware sensor DRAM

    .. data:: hw_sensor_pim = 3

    	Hardware sensor PIM

    """

    hw_sensor_board = Enum.YLeaf(0, "hw-sensor-board")

    hw_sensor_cpu_junction = Enum.YLeaf(1, "hw-sensor-cpu-junction")

    hw_sensor_dram = Enum.YLeaf(2, "hw-sensor-dram")

    hw_sensor_pim = Enum.YLeaf(3, "hw-sensor-pim")


class InterfaceNotifState(Enum):
    """
    InterfaceNotifState (Enum Class)

    Interface Notification state

    .. data:: interface_notif_state_up = 0

    .. data:: interface_notif_state_down = 1

    """

    interface_notif_state_up = Enum.YLeaf(0, "interface-notif-state-up")

    interface_notif_state_down = Enum.YLeaf(1, "interface-notif-state-down")


class IntfAdminState(Enum):
    """
    IntfAdminState (Enum Class)

    Interface admin state

    .. data:: up = 0

    .. data:: down = 1

    """

    up = Enum.YLeaf(0, "up")

    down = Enum.YLeaf(1, "down")


class NotificationFailureState(Enum):
    """
    NotificationFailureState (Enum Class)

    Notification failure state

    .. data:: notf_failure_state_ok = 0

    	Notification failure state ok

    .. data:: notf_failure_state_failed = 1

    	Notification failure state failed

    """

    notf_failure_state_ok = Enum.YLeaf(0, "notf-failure-state-ok")

    notf_failure_state_failed = Enum.YLeaf(1, "notf-failure-state-failed")


class NotificationModuleState(Enum):
    """
    NotificationModuleState (Enum Class)

    Notification module state

    .. data:: notf_module_state_inserted = 0

    	Notification module inserted state

    .. data:: notf_module_state_removed = 1

    	Notification module removed state

    """

    notf_module_state_inserted = Enum.YLeaf(0, "notf-module-state-inserted")

    notf_module_state_removed = Enum.YLeaf(1, "notf-module-state-removed")


class NotificationSensorState(Enum):
    """
    NotificationSensorState (Enum Class)

    Notification sensor state

    .. data:: sensor_state_green = 0

    	Sensor state green

    .. data:: sensor_state_yellow = 1

    	Sensor state yellow

    .. data:: sensor_state_red = 2

    	Sensor state red

    """

    sensor_state_green = Enum.YLeaf(0, "sensor-state-green")

    sensor_state_yellow = Enum.YLeaf(1, "sensor-state-yellow")

    sensor_state_red = Enum.YLeaf(2, "sensor-state-red")


class NotificationSeverity(Enum):
    """
    NotificationSeverity (Enum Class)

    Notification severity

    .. data:: critical = 0

    .. data:: major = 1

    .. data:: minor = 2

    """

    critical = Enum.YLeaf(0, "critical")

    major = Enum.YLeaf(1, "major")

    minor = Enum.YLeaf(2, "minor")


class OspfIntfState(Enum):
    """
    OspfIntfState (Enum Class)

    OSPF interface states

    .. data:: ospf_ifs_down = 0

    .. data:: ospf_ifs_loopback = 1

    .. data:: ospf_ifs_waiting = 2

    .. data:: ospf_ifs_point_to_m_point = 3

    .. data:: ospf_ifs_point_to_point = 4

    .. data:: ospf_ifs_dr = 5

    .. data:: ospf_ifs_backup = 6

    .. data:: ospf_ifs_dr_other = 7

    .. data:: ospf_ifs_depend_upon = 8

    """

    ospf_ifs_down = Enum.YLeaf(0, "ospf-ifs-down")

    ospf_ifs_loopback = Enum.YLeaf(1, "ospf-ifs-loopback")

    ospf_ifs_waiting = Enum.YLeaf(2, "ospf-ifs-waiting")

    ospf_ifs_point_to_m_point = Enum.YLeaf(3, "ospf-ifs-point-to-m-point")

    ospf_ifs_point_to_point = Enum.YLeaf(4, "ospf-ifs-point-to-point")

    ospf_ifs_dr = Enum.YLeaf(5, "ospf-ifs-dr")

    ospf_ifs_backup = Enum.YLeaf(6, "ospf-ifs-backup")

    ospf_ifs_dr_other = Enum.YLeaf(7, "ospf-ifs-dr-other")

    ospf_ifs_depend_upon = Enum.YLeaf(8, "ospf-ifs-depend-upon")


class OspfNbrState(Enum):
    """
    OspfNbrState (Enum Class)

    OSPF neighbor states

    .. data:: ospf_nbr_down = 0

    .. data:: ospf_nbr_attempt = 1

    .. data:: ospf_nbr_init = 2

    .. data:: ospf_nbr_two_way = 3

    .. data:: ospf_nbr_exstart = 4

    .. data:: ospf_nbr_exchange = 5

    .. data:: ospf_nbr_loading = 6

    .. data:: ospf_nbr_full = 7

    .. data:: ospf_nbr_deleted = 8

    .. data:: ospf_nbr_depend_upon = 9

    """

    ospf_nbr_down = Enum.YLeaf(0, "ospf-nbr-down")

    ospf_nbr_attempt = Enum.YLeaf(1, "ospf-nbr-attempt")

    ospf_nbr_init = Enum.YLeaf(2, "ospf-nbr-init")

    ospf_nbr_two_way = Enum.YLeaf(3, "ospf-nbr-two-way")

    ospf_nbr_exstart = Enum.YLeaf(4, "ospf-nbr-exstart")

    ospf_nbr_exchange = Enum.YLeaf(5, "ospf-nbr-exchange")

    ospf_nbr_loading = Enum.YLeaf(6, "ospf-nbr-loading")

    ospf_nbr_full = Enum.YLeaf(7, "ospf-nbr-full")

    ospf_nbr_deleted = Enum.YLeaf(8, "ospf-nbr-deleted")

    ospf_nbr_depend_upon = Enum.YLeaf(9, "ospf-nbr-depend-upon")


class UtdIpsAlertActionVal(Enum):
    """
    UtdIpsAlertActionVal (Enum Class)

    Unified Threat Defense (UTD) Intrusion Prevention System (IPS) alert action

    .. data:: utd_ips_alert_action_unknown = 0

    	Unified Threat Defense (UTD) Intrusion Prevention System (IPS) alert action is unknown

    .. data:: utd_ips_alert_action_alert = 1

    	Unified Threat Defense (UTD) Intrusion Prevention System (IPS) alert action generated an alert

    .. data:: utd_ips_alert_action_drop = 2

    	Unified Threat Defense (UTD) Intrusion Prevention System (IPS) alert action resulted in a drop

    .. data:: utd_ips_alert_action_wdrop = 3

    	Unified Threat Defense (UTD) Intrusion Prevention System (IPS) alert action would have resulted in a drop if running in IPS mode

    """

    utd_ips_alert_action_unknown = Enum.YLeaf(0, "utd-ips-alert-action-unknown")

    utd_ips_alert_action_alert = Enum.YLeaf(1, "utd-ips-alert-action-alert")

    utd_ips_alert_action_drop = Enum.YLeaf(2, "utd-ips-alert-action-drop")

    utd_ips_alert_action_wdrop = Enum.YLeaf(3, "utd-ips-alert-action-wdrop")


class UtdIpsAlertClassificationVal(Enum):
    """
    UtdIpsAlertClassificationVal (Enum Class)

    Unified Threat Defense (UTD) Intrusion Prevention System (IPS) alert classification

    .. data:: utd_ips_alert_classification_none = 0

    	Unified Threat Defense (UTD) Intrusion Prevention System (IPS) alert classification is not set

    .. data:: utd_ips_alert_classification_not_suspicious = 1

    	Unified Threat Defense (UTD) Intrusion Prevention System (IPS) alert classification is not suspicious traffic

    .. data:: utd_ips_alert_classification_unknown = 2

    	Unified Threat Defense (UTD) Intrusion Prevention System (IPS) alert classification is unknown traffic

    .. data:: utd_ips_alert_classification_bad_unknown = 3

    	Unified Threat Defense (UTD) Intrusion Prevention System (IPS) alert classification is potentially bad traffic

    .. data:: utd_ips_alert_classification_attempted_recon = 4

    	Unified Threat Defense (UTD) Intrusion Prevention System (IPS) alert classification is attempted information leak

    .. data:: utd_ips_alert_classification_successful_recon_limited = 5

    	Unified Threat Defense (UTD) Intrusion Prevention System (IPS) alert classification is information leak

    .. data:: utd_ips_alert_classification_successful_recon_largescale = 6

    	Unified Threat Defense (UTD) Intrusion Prevention System (IPS) alert classification is large scale information leak

    .. data:: utd_ips_alert_classification_attempted_dos = 7

    	Unified Threat Defense (UTD) Intrusion Prevention System (IPS) alert classification is attempted denial of service

    .. data:: utd_ips_alert_classification_successful_dos = 8

    	Unified Threat Defense (UTD) Intrusion Prevention System (IPS) alert classification is denial of service

    .. data:: utd_ips_alert_classification_attempted_user = 9

    	Unified Threat Defense (UTD) Intrusion Prevention System (IPS) alert classification is attempted user privilege gain

    .. data:: utd_ips_alert_classification_unsuccessful_user = 10

    	Unified Threat Defense (UTD) Intrusion Prevention System (IPS) alert classification is unsuccessful user privilege gain

    .. data:: utd_ips_alert_classification_successful_user = 11

    	Unified Threat Defense (UTD) Intrusion Prevention System (IPS) alert classification is successful user privilege gain

    .. data:: utd_ips_alert_classification_attempted_admin = 12

    	Unified Threat Defense (UTD) Intrusion Prevention System (IPS) alert classification is attempted administrator privilege gain

    .. data:: utd_ips_alert_classification_successful_admin = 13

    	Unified Threat Defense (UTD) Intrusion Prevention System (IPS) alert classification is successful administrator privilege gain

    .. data:: utd_ips_alert_classification_rpc_portmap_decode = 14

    	Unified Threat Defense (UTD) Intrusion Prevention System (IPS) alert classification is decode of an rpc query

    .. data:: utd_ips_alert_classification_shellcode_detect = 15

    	Unified Threat Defense (UTD) Intrusion Prevention System (IPS) alert classification is executable code was detected

    .. data:: utd_ips_alert_classification_string_detect = 16

    	Unified Threat Defense (UTD) Intrusion Prevention System (IPS) alert classification is a suspicious string was detected

    .. data:: utd_ips_alert_classification_suspicious_filename_detect = 17

    	Unified Threat Defense (UTD) Intrusion Prevention System (IPS) alert classification is a suspicious filename was detected

    .. data:: utd_ips_alert_classification_suspicious_login = 18

    	Unified Threat Defense (UTD) Intrusion Prevention System (IPS) alert classification is an attempted login using a suspicious username was detected

    .. data:: utd_ips_alert_classification_system_call_detect = 19

    	Unified Threat Defense (UTD) Intrusion Prevention System (IPS) alert classification is a system call was detected

    .. data:: utd_ips_alert_classification_tcp_connection = 20

    	Unified Threat Defense (UTD) Intrusion Prevention System (IPS) alert classification is a tcp connection was detected

    .. data:: utd_ips_alert_classification_trojan_activity = 21

    	Unified Threat Defense (UTD) Intrusion Prevention System (IPS) alert classification is a network trojan was detected

    .. data:: utd_ips_alert_classification_unusual_client_port_connection = 22

    	Unified Threat Defense (UTD) Intrusion Prevention System (IPS) alert classification is a client was using an unusual port

    .. data:: utd_ips_alert_classification_network_scan = 23

    	Unified Threat Defense (UTD) Intrusion Prevention System (IPS) alert classification is detection of a network scan

    .. data:: utd_ips_alert_classification_denial_of_service = 24

    	Unified Threat Defense (UTD) Intrusion Prevention System (IPS) alert classification is detection of a denial of service attack

    .. data:: utd_ips_alert_classification_non_standard_protocol = 25

    	Unified Threat Defense (UTD) Intrusion Prevention System (IPS) alert classification is detection of a non-standard protocol or event

    .. data:: utd_ips_alert_classification_protocol_command_decode = 26

    	Unified Threat Defense (UTD) Intrusion Prevention System (IPS) alert classification is generic protocol command decode

    .. data:: utd_ips_alert_classification_web_application_activity = 27

    	Unified Threat Defense (UTD) Intrusion Prevention System (IPS) alert classification is access to a potentially vulnerable web application

    .. data:: utd_ips_alert_classification_web_application_attack = 28

    	Unified Threat Defense (UTD) Intrusion Prevention System (IPS) alert classification is web application attack

    .. data:: utd_ips_alert_classification_misc_activity = 29

    	Unified Threat Defense (UTD) Intrusion Prevention System (IPS) alert classification is misc activity

    .. data:: utd_ips_alert_classification_misc_attack = 30

    	Unified Threat Defense (UTD) Intrusion Prevention System (IPS) alert classification is misc attack

    .. data:: utd_ips_alert_classification_icmp_event = 31

    	Unified Threat Defense (UTD) Intrusion Prevention System (IPS) alert classification is generic icmp event

    .. data:: utd_ips_alert_classification_inappropriate_content = 32

    	Unified Threat Defense (UTD) Intrusion Prevention System (IPS) alert classification is inappropriate content was detected

    .. data:: utd_ips_alert_classification_policy_violation = 33

    	Unified Threat Defense (UTD) Intrusion Prevention System (IPS) alert classification is potential corporate privacy violation

    .. data:: utd_ips_alert_classification_default_login_attempt = 34

    	Unified Threat Defense (UTD) Intrusion Prevention System (IPS) alert classification is attempt to login by a default username and password

    .. data:: utd_ips_alert_classification_sdf = 35

    	Unified Threat Defense (UTD) Intrusion Prevention System (IPS) alert classification is senstive data

    .. data:: utd_ips_alert_classification_file_format = 36

    	Unified Threat Defense (UTD) Intrusion Prevention System (IPS) alert classification is known malicious file or file based exploit

    .. data:: utd_ips_alert_classification_malware_cnc = 37

    	Unified Threat Defense (UTD) Intrusion Prevention System (IPS) alert classification is known malware command and control traffic

    .. data:: utd_ips_alert_classification_client_side_exploit = 38

    	Unified Threat Defense (UTD) Intrusion Prevention System (IPS) alert classification is known client side exploit attempt

    """

    utd_ips_alert_classification_none = Enum.YLeaf(0, "utd-ips-alert-classification-none")

    utd_ips_alert_classification_not_suspicious = Enum.YLeaf(1, "utd-ips-alert-classification-not-suspicious")

    utd_ips_alert_classification_unknown = Enum.YLeaf(2, "utd-ips-alert-classification-unknown")

    utd_ips_alert_classification_bad_unknown = Enum.YLeaf(3, "utd-ips-alert-classification-bad-unknown")

    utd_ips_alert_classification_attempted_recon = Enum.YLeaf(4, "utd-ips-alert-classification-attempted-recon")

    utd_ips_alert_classification_successful_recon_limited = Enum.YLeaf(5, "utd-ips-alert-classification-successful-recon-limited")

    utd_ips_alert_classification_successful_recon_largescale = Enum.YLeaf(6, "utd-ips-alert-classification-successful-recon-largescale")

    utd_ips_alert_classification_attempted_dos = Enum.YLeaf(7, "utd-ips-alert-classification-attempted-dos")

    utd_ips_alert_classification_successful_dos = Enum.YLeaf(8, "utd-ips-alert-classification-successful-dos")

    utd_ips_alert_classification_attempted_user = Enum.YLeaf(9, "utd-ips-alert-classification-attempted-user")

    utd_ips_alert_classification_unsuccessful_user = Enum.YLeaf(10, "utd-ips-alert-classification-unsuccessful-user")

    utd_ips_alert_classification_successful_user = Enum.YLeaf(11, "utd-ips-alert-classification-successful-user")

    utd_ips_alert_classification_attempted_admin = Enum.YLeaf(12, "utd-ips-alert-classification-attempted-admin")

    utd_ips_alert_classification_successful_admin = Enum.YLeaf(13, "utd-ips-alert-classification-successful-admin")

    utd_ips_alert_classification_rpc_portmap_decode = Enum.YLeaf(14, "utd-ips-alert-classification-rpc-portmap-decode")

    utd_ips_alert_classification_shellcode_detect = Enum.YLeaf(15, "utd-ips-alert-classification-shellcode-detect")

    utd_ips_alert_classification_string_detect = Enum.YLeaf(16, "utd-ips-alert-classification-string-detect")

    utd_ips_alert_classification_suspicious_filename_detect = Enum.YLeaf(17, "utd-ips-alert-classification-suspicious-filename-detect")

    utd_ips_alert_classification_suspicious_login = Enum.YLeaf(18, "utd-ips-alert-classification-suspicious-login")

    utd_ips_alert_classification_system_call_detect = Enum.YLeaf(19, "utd-ips-alert-classification-system-call-detect")

    utd_ips_alert_classification_tcp_connection = Enum.YLeaf(20, "utd-ips-alert-classification-tcp-connection")

    utd_ips_alert_classification_trojan_activity = Enum.YLeaf(21, "utd-ips-alert-classification-trojan-activity")

    utd_ips_alert_classification_unusual_client_port_connection = Enum.YLeaf(22, "utd-ips-alert-classification-unusual-client-port-connection")

    utd_ips_alert_classification_network_scan = Enum.YLeaf(23, "utd-ips-alert-classification-network-scan")

    utd_ips_alert_classification_denial_of_service = Enum.YLeaf(24, "utd-ips-alert-classification-denial-of-service")

    utd_ips_alert_classification_non_standard_protocol = Enum.YLeaf(25, "utd-ips-alert-classification-non-standard-protocol")

    utd_ips_alert_classification_protocol_command_decode = Enum.YLeaf(26, "utd-ips-alert-classification-protocol-command-decode")

    utd_ips_alert_classification_web_application_activity = Enum.YLeaf(27, "utd-ips-alert-classification-web-application-activity")

    utd_ips_alert_classification_web_application_attack = Enum.YLeaf(28, "utd-ips-alert-classification-web-application-attack")

    utd_ips_alert_classification_misc_activity = Enum.YLeaf(29, "utd-ips-alert-classification-misc-activity")

    utd_ips_alert_classification_misc_attack = Enum.YLeaf(30, "utd-ips-alert-classification-misc-attack")

    utd_ips_alert_classification_icmp_event = Enum.YLeaf(31, "utd-ips-alert-classification-icmp-event")

    utd_ips_alert_classification_inappropriate_content = Enum.YLeaf(32, "utd-ips-alert-classification-inappropriate-content")

    utd_ips_alert_classification_policy_violation = Enum.YLeaf(33, "utd-ips-alert-classification-policy-violation")

    utd_ips_alert_classification_default_login_attempt = Enum.YLeaf(34, "utd-ips-alert-classification-default-login-attempt")

    utd_ips_alert_classification_sdf = Enum.YLeaf(35, "utd-ips-alert-classification-sdf")

    utd_ips_alert_classification_file_format = Enum.YLeaf(36, "utd-ips-alert-classification-file-format")

    utd_ips_alert_classification_malware_cnc = Enum.YLeaf(37, "utd-ips-alert-classification-malware-cnc")

    utd_ips_alert_classification_client_side_exploit = Enum.YLeaf(38, "utd-ips-alert-classification-client-side-exploit")


class UtdIpsAlertPriorityVal(Enum):
    """
    UtdIpsAlertPriorityVal (Enum Class)

    Unified Threat Defense (UTD) Intrusion Prevention System (IPS) alert priority

    .. data:: utd_ips_alert_priority_unknown = 0

    	Unified Threat Defense (UTD) Intrusion Prevention System (IPS) alert priority is unknown

    .. data:: utd_ips_alert_priority_emerg = 1

    	Unified Threat Defense (UTD) Intrusion Prevention System (IPS) alert priority is emergency

    .. data:: utd_ips_alert_priority_alert = 2

    	Unified Threat Defense (UTD) Intrusion Prevention System (IPS) alert priority is alert

    .. data:: utd_ips_alert_priority_crit = 3

    	Unified Threat Defense (UTD) Intrusion Prevention System (IPS) alert priority is critical

    .. data:: utd_ips_alert_priority_error = 4

    	Unified Threat Defense (UTD) Intrusion Prevention System (IPS) alert priority is error

    .. data:: utd_ips_alert_priority_warn = 5

    	Unified Threat Defense (UTD) Intrusion Prevention System (IPS) alert priority is warning

    .. data:: utd_ips_alert_priority_notice = 6

    	Unified Threat Defense (UTD) Intrusion Prevention System (IPS) alert priority is notice

    .. data:: utd_ips_alert_priority_info = 7

    	Unified Threat Defense (UTD) Intrusion Prevention System (IPS) alert priority is info

    .. data:: utd_ips_alert_priority_debug = 8

    	Unified Threat Defense (UTD) Intrusion Prevention System (IPS) alert priority is debug

    """

    utd_ips_alert_priority_unknown = Enum.YLeaf(0, "utd-ips-alert-priority-unknown")

    utd_ips_alert_priority_emerg = Enum.YLeaf(1, "utd-ips-alert-priority-emerg")

    utd_ips_alert_priority_alert = Enum.YLeaf(2, "utd-ips-alert-priority-alert")

    utd_ips_alert_priority_crit = Enum.YLeaf(3, "utd-ips-alert-priority-crit")

    utd_ips_alert_priority_error = Enum.YLeaf(4, "utd-ips-alert-priority-error")

    utd_ips_alert_priority_warn = Enum.YLeaf(5, "utd-ips-alert-priority-warn")

    utd_ips_alert_priority_notice = Enum.YLeaf(6, "utd-ips-alert-priority-notice")

    utd_ips_alert_priority_info = Enum.YLeaf(7, "utd-ips-alert-priority-info")

    utd_ips_alert_priority_debug = Enum.YLeaf(8, "utd-ips-alert-priority-debug")


class UtdUpdateTypeVal(Enum):
    """
    UtdUpdateTypeVal (Enum Class)

    Unified Threat Defense (UTD) update type

    .. data:: utd_update_type_unknown = 0

    	Unified Threat Defense (UTD) update type is unknown

    .. data:: utd_update_type_ips = 1

    	Unified Threat Defense (UTD) update is an IPS signature package update

    .. data:: utd_update_type_urlf = 2

    	Unified Threat Defense (UTD) update is a URL-Filtering DB update

    """

    utd_update_type_unknown = Enum.YLeaf(0, "utd-update-type-unknown")

    utd_update_type_ips = Enum.YLeaf(1, "utd-update-type-ips")

    utd_update_type_urlf = Enum.YLeaf(2, "utd-update-type-urlf")


class VrrpIpAddrType(Enum):
    """
    VrrpIpAddrType (Enum Class)

    IP Address type

    .. data:: vrrp_undefined = 0

    .. data:: vrrp_ipv4_address = 1

    .. data:: vrrp_ipv6_address = 2

    """

    vrrp_undefined = Enum.YLeaf(0, "vrrp-undefined")

    vrrp_ipv4_address = Enum.YLeaf(1, "vrrp-ipv4-address")

    vrrp_ipv6_address = Enum.YLeaf(2, "vrrp-ipv6-address")


class VrrpNotifProtoState(Enum):
    """
    VrrpNotifProtoState (Enum Class)

    VRRP protocol state

    .. data:: vrrp_notif_init = 1

    .. data:: vrrp_notif_backup = 2

    .. data:: vrrp_notif_master = 3

    .. data:: vrrp_notif_recover = 4

    """

    vrrp_notif_init = Enum.YLeaf(1, "vrrp-notif-init")

    vrrp_notif_backup = Enum.YLeaf(2, "vrrp-notif-backup")

    vrrp_notif_master = Enum.YLeaf(3, "vrrp-notif-master")

    vrrp_notif_recover = Enum.YLeaf(4, "vrrp-notif-recover")



class IosEvents(Entity):
    """
    Events generated from IOS features
    
    

    """

    _prefix = 'ios-events-ios-xe-oper'
    _revision = '2017-10-10'

    def __init__(self):
        super(IosEvents, self).__init__()
        self._top_entity = None

        self.yang_name = "ios-events"
        self.yang_parent_name = "Cisco-IOS-XE-ios-events-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()
        self._segment_path = lambda: "Cisco-IOS-XE-ios-events-oper:ios-events"
        self._is_frozen = True

    def clone_ptr(self):
        self._top_entity = IosEvents()
        return self._top_entity

