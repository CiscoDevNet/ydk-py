""" Cisco_IOS_XE_cellwan_oper 

This module contains a collection of YANG definitions
for cellwan operational data.
Copyright (c) 2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CellwanChv1SimStatus(Enum):
    """
    CellwanChv1SimStatus (Enum Class)

    Cellular modem SIM card holder verification (CHV1) status

    .. data:: chv1_verify_disabled = 0

    	SIM card holder verification (CHV1) disabled

    .. data:: chv1_verify_enabled = 1

    	SIM card holder verification (CHV1) enabled

    .. data:: chv1_verify_pending = 2

    	SIM card holder verification (CHV1) pending

    """

    chv1_verify_disabled = Enum.YLeaf(0, "chv1-verify-disabled")

    chv1_verify_enabled = Enum.YLeaf(1, "chv1-verify-enabled")

    chv1_verify_pending = Enum.YLeaf(2, "chv1-verify-pending")


class CellwanSimStatus(Enum):
    """
    CellwanSimStatus (Enum Class)

    Cellular modem SIM status

    .. data:: sim_status_ok = 0

    	Cellular modem SIM status is inserted

    .. data:: sim_status_not_inserted = 1

    	Cellular modem SIM is not inserted

    .. data:: sim_status_removed = 2

    	Cellular modem SIM is in removed state

    .. data:: sim_status_init_failure = 3

    	Cellular modem SIM is in initialization failure state

    .. data:: sim_status_general_failure = 4

    	Cellular modem SIM is in general failure state

    .. data:: sim_status_locked = 5

    	Cellular modem SIM is in locked state

    .. data:: sim_status_chv1_blocked = 6

    	Cellular modem SIM is in chv1 (Card Holder Verification) blocked state

    .. data:: sim_status_chv2_blocked = 7

    	Cellular modem SIM is in chv2 (Card Holder Verification) blocked state

    .. data:: sim_status_chv1_rejected = 8

    	Cellular modem SIM is in chv1 (Card Holder Verification) rejected state

    .. data:: sim_status_chv2_rejected = 9

    	Cellular modem SIM is in chv2 (Card Holder Verification) rejected state

    .. data:: sim_status_mep_locked = 10

    	Cellular modem SIM is in MEP (Mobile Equipment Personalization) locked state

    .. data:: sim_status_network_reject = 11

    	Cellular modem SIM is in network reject state

    .. data:: sim_status_unknown = 12

    	Cellular modem SIM is in unknown state

    """

    sim_status_ok = Enum.YLeaf(0, "sim-status-ok")

    sim_status_not_inserted = Enum.YLeaf(1, "sim-status-not-inserted")

    sim_status_removed = Enum.YLeaf(2, "sim-status-removed")

    sim_status_init_failure = Enum.YLeaf(3, "sim-status-init-failure")

    sim_status_general_failure = Enum.YLeaf(4, "sim-status-general-failure")

    sim_status_locked = Enum.YLeaf(5, "sim-status-locked")

    sim_status_chv1_blocked = Enum.YLeaf(6, "sim-status-chv1-blocked")

    sim_status_chv2_blocked = Enum.YLeaf(7, "sim-status-chv2-blocked")

    sim_status_chv1_rejected = Enum.YLeaf(8, "sim-status-chv1-rejected")

    sim_status_chv2_rejected = Enum.YLeaf(9, "sim-status-chv2-rejected")

    sim_status_mep_locked = Enum.YLeaf(10, "sim-status-mep-locked")

    sim_status_network_reject = Enum.YLeaf(11, "sim-status-network-reject")

    sim_status_unknown = Enum.YLeaf(12, "sim-status-unknown")


class CellwanSimUserOp(Enum):
    """
    CellwanSimUserOp (Enum Class)

    Cellular modem SIM user operation status

    .. data:: sim_user_op_none = 0

    	Cellular modem SIM user operation is in None state

    .. data:: sim_user_op_chv1 = 1

    	Cellular modem SIM user is in CHV1 (Card Holder Verification) state

    .. data:: sim_user_op_chv2 = 2

    	Cellular modem SIM user is in CHV2 (Card Holder Verification) state

    .. data:: sim_user_op_unblock_chv1 = 3

    	Cellular modem SIM user is in Unblocked CHV1 (Card Holder Verification) state

    .. data:: sim_user_op_unblock_chv2 = 4

    	Cellular modem SIM user is in Unblocked CHV2 (Card Holder Verification) state

    .. data:: sim_user_op_mep = 5

    	Cellular modem SIM user is in MEP (Mobile Equipment Personalization) state

    .. data:: sim_user_op_unknown = 6

    	Cellular modem SIM user operation is in Unknown state

    """

    sim_user_op_none = Enum.YLeaf(0, "sim-user-op-none")

    sim_user_op_chv1 = Enum.YLeaf(1, "sim-user-op-chv1")

    sim_user_op_chv2 = Enum.YLeaf(2, "sim-user-op-chv2")

    sim_user_op_unblock_chv1 = Enum.YLeaf(3, "sim-user-op-unblock-chv1")

    sim_user_op_unblock_chv2 = Enum.YLeaf(4, "sim-user-op-unblock-chv2")

    sim_user_op_mep = Enum.YLeaf(5, "sim-user-op-mep")

    sim_user_op_unknown = Enum.YLeaf(6, "sim-user-op-unknown")


class CwRadioPowerStatus(Enum):
    """
    CwRadioPowerStatus (Enum Class)

    Radio power status indicates the current radio power mode of cellular modem

    .. data:: radio_power_mode_online = 0

    	Cellular modem is in online radio mode

    .. data:: radio_power_mode_low_power = 1

    	Cellular modem is in low power radio mode

    .. data:: radio_power_mode_factory_test = 2

    	Cellular modem is in factory test radio mode

    .. data:: radio_power_mode_offline = 3

    	Cellular modem is in offline radio mode

    .. data:: radio_power_mode_reset = 4

    	Cellular modem is in reset radio mode

    .. data:: radio_power_mode_off = 5

    	Cellular modem is in off radio mode

    .. data:: radio_power_mode_persistent_low_power = 6

    	Cellular modem is in persistent low power radio mode

    """

    radio_power_mode_online = Enum.YLeaf(0, "radio-power-mode-online")

    radio_power_mode_low_power = Enum.YLeaf(1, "radio-power-mode-low-power")

    radio_power_mode_factory_test = Enum.YLeaf(2, "radio-power-mode-factory-test")

    radio_power_mode_offline = Enum.YLeaf(3, "radio-power-mode-offline")

    radio_power_mode_reset = Enum.YLeaf(4, "radio-power-mode-reset")

    radio_power_mode_off = Enum.YLeaf(5, "radio-power-mode-off")

    radio_power_mode_persistent_low_power = Enum.YLeaf(6, "radio-power-mode-persistent-low-power")


class CwanGpsFeatureState(Enum):
    """
    CwanGpsFeatureState (Enum Class)

    Cellular modem GPS feature state status

    .. data:: gps_disabled = 0

    	Cellular modem GPS feature state is Disabled

    .. data:: gps_enabled = 1

    	Cellular modem GPS feature state is Enabled

    """

    gps_disabled = Enum.YLeaf(0, "gps-disabled")

    gps_enabled = Enum.YLeaf(1, "gps-enabled")


class CwanGpsModeSelected(Enum):
    """
    CwanGpsModeSelected (Enum Class)

    Cellular modem GPS mode selection status

    .. data:: gps_mode_disable = 0

    	Cellular modem GPS mode is disabled

    .. data:: gps_mode_standalone = 1

    	Cellular modem GPS mode is standalone

    .. data:: gps_mode_mbased = 2

    	Cellular modem GPS mode is ms-based

    .. data:: gps_mode_msassist = 3

    	Cellular modem GPS mode is ms-assist

    """

    gps_mode_disable = Enum.YLeaf(0, "gps-mode-disable")

    gps_mode_standalone = Enum.YLeaf(1, "gps-mode-standalone")

    gps_mode_mbased = Enum.YLeaf(2, "gps-mode-mbased")

    gps_mode_msassist = Enum.YLeaf(3, "gps-mode-msassist")


class CwanGpsPortSelected(Enum):
    """
    CwanGpsPortSelected (Enum Class)

    Cellular modem GPS port selection status

    .. data:: dedicated_gps_port = 0

    	Cellular modem dedicated GPS port selected

    .. data:: div_gps_port = 1

    	Cellular modem DIV port selected for GPS

    .. data:: voltage_no_bias_gps_port = 2

    	Cellular modem voltage no-bias port selected for GPS

    .. data:: gps_port_none = 3

    	Cellular modem none port selected for GPS

    """

    dedicated_gps_port = Enum.YLeaf(0, "dedicated-gps-port")

    div_gps_port = Enum.YLeaf(1, "div-gps-port")

    voltage_no_bias_gps_port = Enum.YLeaf(2, "voltage-no-bias-gps-port")

    gps_port_none = Enum.YLeaf(3, "gps-port-none")


class CwanGpsState(Enum):
    """
    CwanGpsState (Enum Class)

    Cellular modem GPS state

    .. data:: gps_state_disabled = 1

    	Cellular modem is in GPS disabled state

    .. data:: gps_state_acquiring = 2

    	Cellular modem is in GPS acquiring state

    .. data:: gps_state_enabled = 3

    	Cellular modem is in GPS enabled state

    .. data:: gps_loc_error = 4

    	Cellular modem is in GPS location error state

    """

    gps_state_disabled = Enum.YLeaf(1, "gps-state-disabled")

    gps_state_acquiring = Enum.YLeaf(2, "gps-state-acquiring")

    gps_state_enabled = Enum.YLeaf(3, "gps-state-enabled")

    gps_loc_error = Enum.YLeaf(4, "gps-loc-error")


class LteCa(Enum):
    """
    LteCa (Enum Class)

    LTE CA indicates the LTE carrier aggregation status for cellular modem

    .. data:: lte_ca_deconfigured = 0

    	LTE carrier aggregation is deconfigured

    .. data:: lte_ca_deactivated = 1

    	LTE carrier aggregation is deactivated

    .. data:: lte_ca_activated = 2

    	LTE carrier aggregation is activated

    .. data:: lte_ca_unsupported = 3

    	LTE carrier aggregation is unsupported

    """

    lte_ca_deconfigured = Enum.YLeaf(0, "lte-ca-deconfigured")

    lte_ca_deactivated = Enum.YLeaf(1, "lte-ca-deactivated")

    lte_ca_activated = Enum.YLeaf(2, "lte-ca-activated")

    lte_ca_unsupported = Enum.YLeaf(3, "lte-ca-unsupported")


class ModemService(Enum):
    """
    ModemService (Enum Class)

    Modem service indicates the current network service type for cellular modem

    .. data:: service_type_circuit_switched = 0

    	Cellular Network service type is circuit-switched

    .. data:: service_type_packet_switched = 1

    	Cellular Network service type is packet-switched

    .. data:: service_type_combined = 2

    	Cellular Network service type is combined

    .. data:: service_type_invalid = 3

    	Cellular Network service type is invalid

    .. data:: service_type_unknown = 4

    	Cellular Network service type is unknown

    """

    service_type_circuit_switched = Enum.YLeaf(0, "service-type-circuit-switched")

    service_type_packet_switched = Enum.YLeaf(1, "service-type-packet-switched")

    service_type_combined = Enum.YLeaf(2, "service-type-combined")

    service_type_invalid = Enum.YLeaf(3, "service-type-invalid")

    service_type_unknown = Enum.YLeaf(4, "service-type-unknown")


class ModemStatus(Enum):
    """
    ModemStatus (Enum Class)

    Modem status indicates the current state of cellular modem

    .. data:: modem_status_offline = 0

    	Modem is in Offline state

    .. data:: modem_status_online = 1

    	Modem is in Online state

    .. data:: modem_status_low_power = 2

    	Modem is in Low Power Mode state

    .. data:: modem_status_power_off = 3

    	Modem is in power off state

    .. data:: modem_status_boot_ready = 4

    	Modem is in boot ready state

    .. data:: modem_status_unknown = 5

    	Modem is in unknown state

    """

    modem_status_offline = Enum.YLeaf(0, "modem-status-offline")

    modem_status_online = Enum.YLeaf(1, "modem-status-online")

    modem_status_low_power = Enum.YLeaf(2, "modem-status-low-power")

    modem_status_power_off = Enum.YLeaf(3, "modem-status-power-off")

    modem_status_boot_ready = Enum.YLeaf(4, "modem-status-boot-ready")

    modem_status_unknown = Enum.YLeaf(5, "modem-status-unknown")


class ModemTechnology(Enum):
    """
    ModemTechnology (Enum Class)

    Modem technology indicates the current cellular technology selected

    .. data:: cdma_evdo_1x_rtt = 0

    	Modem technology selected is CDMA (Code Division Multiple Access) / 

    	  EVDO (Evolution-Data Optimized) / 

    	  1xRTT (Single carrier (1x) radio transmission technology)

    .. data:: gsm_umts_gprs = 1

    	Modem technology selected is GSM (Global System for Mobile Communications) 

    	  / UMTS (Universal Mobile Telecommunications Service) 

    	  / GPRS (General Packet Radio Service)

    .. data:: tech_unknown = 2

    	Modem technology selected is unknown

    """

    cdma_evdo_1x_rtt = Enum.YLeaf(0, "cdma-evdo-1x-rtt")

    gsm_umts_gprs = Enum.YLeaf(1, "gsm-umts-gprs")

    tech_unknown = Enum.YLeaf(2, "tech-unknown")


class PacketSessStatus(Enum):
    """
    PacketSessStatus (Enum Class)

    Packet Session Status indicates the Cellular packet session state

    .. data:: packet_session_status_inactive = 0

    	Cellular packet session status is inactive

    .. data:: packet_session_status_active = 1

    	Cellular packet session status is active

    """

    packet_session_status_inactive = Enum.YLeaf(0, "packet-session-status-inactive")

    packet_session_status_active = Enum.YLeaf(1, "packet-session-status-active")


class ProfileScope(Enum):
    """
    ProfileScope (Enum Class)

    Profile Scope indicates the IP address scope

    .. data:: scope_global = 0

    	IP address scope is Global

    .. data:: scope_link = 1

    	IP address scope is Link

    """

    scope_global = Enum.YLeaf(0, "scope-global")

    scope_link = Enum.YLeaf(1, "scope-link")


class RadioBandwidth(Enum):
    """
    RadioBandwidth (Enum Class)

    Radio bandwidth indicates the current cellular radio bandwidth selected in MHz

    .. data:: bandwidth_1_dot_4_mhz = 0

    	Cellular radio bandwidth is 1.4 MHz

    .. data:: bandwidth_3_mhz = 1

    	Cellular radio bandwidth is 3 MHz

    .. data:: bandwidth_5_mhz = 2

    	Cellular radio bandwidth is 5 MHz

    .. data:: bandwidth_10_mhz = 3

    	Cellular radio bandwidth is 10 MHz

    .. data:: bandwidth_15_mhz = 4

    	Cellular radio bandwidth is 15 MHz

    .. data:: bandwidth_20_mhz = 5

    	Cellular radio bandwidth is 20 MHz

    .. data:: bandwidth_invalid = 6

    	Cellular radio bandwidth is invalid

    .. data:: bandwidth_unknown = 7

    	Cellular radio bandwidth is unknown

    """

    bandwidth_1_dot_4_mhz = Enum.YLeaf(0, "bandwidth-1-dot-4-mhz")

    bandwidth_3_mhz = Enum.YLeaf(1, "bandwidth-3-mhz")

    bandwidth_5_mhz = Enum.YLeaf(2, "bandwidth-5-mhz")

    bandwidth_10_mhz = Enum.YLeaf(3, "bandwidth-10-mhz")

    bandwidth_15_mhz = Enum.YLeaf(4, "bandwidth-15-mhz")

    bandwidth_20_mhz = Enum.YLeaf(5, "bandwidth-20-mhz")

    bandwidth_invalid = Enum.YLeaf(6, "bandwidth-invalid")

    bandwidth_unknown = Enum.YLeaf(7, "bandwidth-unknown")


class RatPreference(Enum):
    """
    RatPreference (Enum Class)

    RAT preference indicates the current radio technology preference

    .. data:: lte_radio_tech_no_svc = 0

    	Radio technology preference is no svc

    .. data:: lte_radio_tech_cdma_1_xrtt = 1

    	Radio technology preference is CDMA (Code Division Multiple Access) 

    	/ 1xRTT (Single carrier (1x) radio transmission technology)

    .. data:: lte_radio_tech_cdma_evdo = 2

    	Radio technology preference is CDMA (Code Division Multiple Access) 

    	/ EVDO (Evolution-Data Optimized) 

    .. data:: lte_radio_tech_amps = 3

    	Radio technology preference is AMPS (Advanced Mobile Phone Service)

    .. data:: lte_radio_tech_gsm = 4

    	Radio technology preference is GSM (Global System for Mobile Communications)

    .. data:: lte_radio_tech_umts = 5

    	Radio technology preference is UMTS (Universal Mobile Telecommunications Service)

    .. data:: lte_radio_tech_wlan = 6

    	Radio technology preference is WLAN (wireless local area network)

    .. data:: lte_radio_tech_gprs = 7

    	Radio technology preference is GPRS (General Packet Radio Service)

    .. data:: lte_radio_tech_lte = 8

    	Radio technology preference is LTE (Long-Term Evolution)

    .. data:: lte_radio_tech_auto = 9

    	Radio technology preference is AUTO 

    .. data:: lte_radio_tech_hybrid_cdma = 10

    	Radio technology preference is Hybrid CDMA (Hybrid Code Division Multiple Access)

    .. data:: lte_radio_tech_wcdma = 11

    	Radio technology preference is WCDMA (Wideband Code Division Multiplexing Access)

    .. data:: lte_radio_tech_gwl = 12

    	Radio technology preference is GWL 

    .. data:: lte_radio_tech_edge = 13

    	Radio technology preference is EDGE (Enhanced Data rates for GSM Evolution)

    .. data:: lte_radio_tech_hsdpa_n_wcdma = 14

    	Radio technology preference is HSDPA (High Speed Downlink Packet Access)

    	& WCDMA (Wideband Code Division Multiplexing Access)

    .. data:: lte_radio_tech_wcdma_n_hsupa = 15

    	Radio technology preference is WCDMA (Wideband Code Division Multiplexing Access)

    	  & HSUPA (High Speed Uplink Packet Access)

    .. data:: lte_radio_tech_hsdpa_n_hsupa = 16

    	Radio technology preference is HSDPA (High Speed Downlink Packet Access)

    	  & HSUPA (High Speed Uplink Packet Access)

    .. data:: lte_radio_tech_hsdpa_plus_n_wcdma = 17

    	Radio technology preference is HSDPA+ (High Speed Downlink Packet Access plus) 

    	  & WCDMA (Wideband Code Division Multiplexing Access)

    .. data:: lte_radio_tech_hsdpa_plus_n_hsupa = 18

    	Radio technology preference is HSDPA+ (High Speed Downlink Packet Access plus)

    	  & HSUPA (High Speed Uplink Packet Access)

    .. data:: lte_radio_tech_dc_hsdpa_plus_n_wcdma = 19

    	Radio technology preference is 

    	  DC HSDPA+ (Dual Carrier High Speed Downlink Packet Access plus) 

    	  & WCDMA (Wideband Code Division Multiplexing Access)

    .. data:: lte_radio_tech_dc_hsdpa_plus_n_hsupa = 20

    	Radio technology preference is 

    	  DC HSDPA+ (Dual Carrier High Speed Downlink Packet Access plus) 

    	  & HSUPA (High Speed Uplink Packet Access)

    .. data:: lte_radio_tech_null_bearer = 21

    	Radio technology preference is Null Bearer 

    .. data:: lte_radio_tech_unknown = 22

    	Radio technology preference is Unknown 

    .. data:: lte_radio_tech_no_change = 23

    	Radio technology preference is unchanged 

    """

    lte_radio_tech_no_svc = Enum.YLeaf(0, "lte-radio-tech-no-svc")

    lte_radio_tech_cdma_1_xrtt = Enum.YLeaf(1, "lte-radio-tech-cdma-1-xrtt")

    lte_radio_tech_cdma_evdo = Enum.YLeaf(2, "lte-radio-tech-cdma-evdo")

    lte_radio_tech_amps = Enum.YLeaf(3, "lte-radio-tech-amps")

    lte_radio_tech_gsm = Enum.YLeaf(4, "lte-radio-tech-gsm")

    lte_radio_tech_umts = Enum.YLeaf(5, "lte-radio-tech-umts")

    lte_radio_tech_wlan = Enum.YLeaf(6, "lte-radio-tech-wlan")

    lte_radio_tech_gprs = Enum.YLeaf(7, "lte-radio-tech-gprs")

    lte_radio_tech_lte = Enum.YLeaf(8, "lte-radio-tech-lte")

    lte_radio_tech_auto = Enum.YLeaf(9, "lte-radio-tech-auto")

    lte_radio_tech_hybrid_cdma = Enum.YLeaf(10, "lte-radio-tech-hybrid-cdma")

    lte_radio_tech_wcdma = Enum.YLeaf(11, "lte-radio-tech-wcdma")

    lte_radio_tech_gwl = Enum.YLeaf(12, "lte-radio-tech-gwl")

    lte_radio_tech_edge = Enum.YLeaf(13, "lte-radio-tech-edge")

    lte_radio_tech_hsdpa_n_wcdma = Enum.YLeaf(14, "lte-radio-tech-hsdpa-n-wcdma")

    lte_radio_tech_wcdma_n_hsupa = Enum.YLeaf(15, "lte-radio-tech-wcdma-n-hsupa")

    lte_radio_tech_hsdpa_n_hsupa = Enum.YLeaf(16, "lte-radio-tech-hsdpa-n-hsupa")

    lte_radio_tech_hsdpa_plus_n_wcdma = Enum.YLeaf(17, "lte-radio-tech-hsdpa-plus-n-wcdma")

    lte_radio_tech_hsdpa_plus_n_hsupa = Enum.YLeaf(18, "lte-radio-tech-hsdpa-plus-n-hsupa")

    lte_radio_tech_dc_hsdpa_plus_n_wcdma = Enum.YLeaf(19, "lte-radio-tech-dc-hsdpa-plus-n-wcdma")

    lte_radio_tech_dc_hsdpa_plus_n_hsupa = Enum.YLeaf(20, "lte-radio-tech-dc-hsdpa-plus-n-hsupa")

    lte_radio_tech_null_bearer = Enum.YLeaf(21, "lte-radio-tech-null-bearer")

    lte_radio_tech_unknown = Enum.YLeaf(22, "lte-radio-tech-unknown")

    lte_radio_tech_no_change = Enum.YLeaf(23, "lte-radio-tech-no-change")


class RatTechnology(Enum):
    """
    RatTechnology (Enum Class)

    RAT technology indicates the current radio technology selected

    .. data:: system_mode_none = 0

    	Radio technology selected is none

    .. data:: system_mode_gprs = 1

    	Radio technology selected is GPRS (General Packet Radio Service)

    .. data:: system_mode_edge = 2

    	Radio technology selected is EDGE (Enhanced Data rates for GSM Evolution)

    .. data:: system_mode_umts = 3

    	Radio technology selected is UMTS (Universal Mobile Telecommunications System)

    .. data:: system_mode_hsdpa = 4

    	Radio technology selected is HSDPA (High Speed Downlink Packet Access)

    .. data:: system_mode_hsupa = 5

    	Radio technology selected is HSUPA (High Speed Uplink Packet Access)

    .. data:: system_mode_hspa = 6

    	Radio technology selected is HSPA (High Speed Packet Access)

    .. data:: system_mode_hspa_plus = 7

    	Radio technology selected is HSPA+ (Evolved High Speed Packet Access)

    .. data:: system_mode_lte_fdd = 8

    	Radio technology selected is LTE-FDD (Long Term Evolution-Frequency Division Duplex)

    .. data:: system_mode_lte_tdd = 9

    	Radio technology selected is LTE-TDD(Long Term Evolution-Time Division Duplex)

    .. data:: system_mode_lte_e_hrpd_1x_rtt = 10

    	Radio technology selected is LTE (Long Term Evolution) /

    	  eHRPD (Evolved High Rate Packet Data) /

    	  1xRTT (Single carrier (1x) radio transmission technology)

    .. data:: system_mode_lte_e_hrpd_evdo = 11

    	Radio technology selected is LTE (Long Term Evolution) / 

    	  eHRPD (Evolved High Rate Packet Data) / 

    	  EVDO (Evolution-Data Optimized) 

    .. data:: system_mode_evdo = 12

    	Radio technology selected is EVDO (Evolution-Data Optimized)

    .. data:: system_mode_evdo_reva = 13

    	Radio technology selected is EVDO (Evolution-Data Optimized) / 

    	  REVA (Evolution Data Optimized - Rev A)

    .. data:: system_mode_hsdpa_n_wcdma = 14

    	Radio technology selected is HSDPA (High Speed Downlink Packet Access) 

    	  & WCDMA (Wideband Code Division Multiple Access)

    .. data:: system_mode_wcdma_n_hsupa = 15

    	Radio technology selected is WCDMA (Wideband Code Division Multiple Access)

    	  & HSUPA (High Speed Uplink Packet Access) 

    .. data:: system_mode_hsdpa_n_hsupa = 16

    	Radio technology selected is HSDPA (High Speed Downlink Packet Access) 

    	  & HSUPA (High Speed Uplink Packet Access) 

    .. data:: system_mode_hsdpa_plus_n_wcdma = 17

    	Radio technology selected is HSDPA+ (High Speed Downlink Packet Access plus) 

    	  & WCDMA (Wideband Code Division Multiple Access)

    .. data:: system_mode_hsdpa_plus_n_hsupa = 18

    	Radio technology selected is HSDPA+ (High Speed Downlink Packet Access plus) 

    	  & HSUPA (High Speed Uplink Packet Access) 

    .. data:: system_mode_dc_hsdpa_plus_n_wcdma = 19

    	Radio technology selected is 

    	  DC HSDPA+ (Dual Carrier High Speed Downlink Packet Access plus) 

    	  & WCDMA (Wideband Code Division Multiple Access)

    .. data:: system_mode_dc_hsdpa_plus_n_hsupa = 20

    	Radio technology selected is 

    	  DC HSDPA+ (Dual Carrier High Speed Downlink Packet Access plus)

    	  & HSUPA (High Speed Uplink Packet Access)

    .. data:: sysyem_mode_null_bearer = 21

    	Radio technology selected is null bearer

    .. data:: system_mode_unknown = 22

    	Radio technology selected is unknown

    """

    system_mode_none = Enum.YLeaf(0, "system-mode-none")

    system_mode_gprs = Enum.YLeaf(1, "system-mode-gprs")

    system_mode_edge = Enum.YLeaf(2, "system-mode-edge")

    system_mode_umts = Enum.YLeaf(3, "system-mode-umts")

    system_mode_hsdpa = Enum.YLeaf(4, "system-mode-hsdpa")

    system_mode_hsupa = Enum.YLeaf(5, "system-mode-hsupa")

    system_mode_hspa = Enum.YLeaf(6, "system-mode-hspa")

    system_mode_hspa_plus = Enum.YLeaf(7, "system-mode-hspa-plus")

    system_mode_lte_fdd = Enum.YLeaf(8, "system-mode-lte-fdd")

    system_mode_lte_tdd = Enum.YLeaf(9, "system-mode-lte-tdd")

    system_mode_lte_e_hrpd_1x_rtt = Enum.YLeaf(10, "system-mode-lte-e-hrpd-1x-rtt")

    system_mode_lte_e_hrpd_evdo = Enum.YLeaf(11, "system-mode-lte-e-hrpd-evdo")

    system_mode_evdo = Enum.YLeaf(12, "system-mode-evdo")

    system_mode_evdo_reva = Enum.YLeaf(13, "system-mode-evdo-reva")

    system_mode_hsdpa_n_wcdma = Enum.YLeaf(14, "system-mode-hsdpa-n-wcdma")

    system_mode_wcdma_n_hsupa = Enum.YLeaf(15, "system-mode-wcdma-n-hsupa")

    system_mode_hsdpa_n_hsupa = Enum.YLeaf(16, "system-mode-hsdpa-n-hsupa")

    system_mode_hsdpa_plus_n_wcdma = Enum.YLeaf(17, "system-mode-hsdpa-plus-n-wcdma")

    system_mode_hsdpa_plus_n_hsupa = Enum.YLeaf(18, "system-mode-hsdpa-plus-n-hsupa")

    system_mode_dc_hsdpa_plus_n_wcdma = Enum.YLeaf(19, "system-mode-dc-hsdpa-plus-n-wcdma")

    system_mode_dc_hsdpa_plus_n_hsupa = Enum.YLeaf(20, "system-mode-dc-hsdpa-plus-n-hsupa")

    sysyem_mode_null_bearer = Enum.YLeaf(21, "sysyem-mode-null-bearer")

    system_mode_unknown = Enum.YLeaf(22, "system-mode-unknown")


class RegState(Enum):
    """
    RegState (Enum Class)

    Registration state indicates the current cellular network registration state

    .. data:: reg_status_not_registered = 0

    	Cellular Network is in not registered state

    .. data:: reg_status_registered = 1

    	Cellular Network is in registered state

    .. data:: reg_status_searching = 2

    	Cellular Network is in searching state

    .. data:: reg_status_registration_denied = 3

    	Cellular Network is in registration denied state

    .. data:: reg_status_unsupported = 4

    	Cellular Network is in unsupported state

    """

    reg_status_not_registered = Enum.YLeaf(0, "reg-status-not-registered")

    reg_status_registered = Enum.YLeaf(1, "reg-status-registered")

    reg_status_searching = Enum.YLeaf(2, "reg-status-searching")

    reg_status_registration_denied = Enum.YLeaf(3, "reg-status-registration-denied")

    reg_status_unsupported = Enum.YLeaf(4, "reg-status-unsupported")


class ServiceStatus(Enum):
    """
    ServiceStatus (Enum Class)

    Service status indicates the current network service for cellular modem

    .. data:: service_status_normal = 0

    	Cellular Network status is in normal state

    .. data:: service_status_emergency = 1

    	Cellular Network status is in emergency state

    .. data:: service_status_no_service = 2

    	Cellular Network status is in no service state

    .. data:: service_status_unknown = 3

    	Cellular Network status is in unknown state

    """

    service_status_normal = Enum.YLeaf(0, "service-status-normal")

    service_status_emergency = Enum.YLeaf(1, "service-status-emergency")

    service_status_no_service = Enum.YLeaf(2, "service-status-no-service")

    service_status_unknown = Enum.YLeaf(3, "service-status-unknown")



class CellwanOperData(Entity):
    """
    Cellwan operational data
    
    .. attribute:: cellwan_hardware
    
    	Cellwan modem hardware data
    	**type**\: list of  		 :py:class:`CellwanHardware <ydk.models.cisco_ios_xe.Cisco_IOS_XE_cellwan_oper.CellwanOperData.CellwanHardware>`
    
    .. attribute:: cellwan_radio
    
    	Cellwan modem radio data
    	**type**\: list of  		 :py:class:`CellwanRadio <ydk.models.cisco_ios_xe.Cisco_IOS_XE_cellwan_oper.CellwanOperData.CellwanRadio>`
    
    .. attribute:: cellwan_network
    
    	Cellwan modem network data
    	**type**\: list of  		 :py:class:`CellwanNetwork <ydk.models.cisco_ios_xe.Cisco_IOS_XE_cellwan_oper.CellwanOperData.CellwanNetwork>`
    
    .. attribute:: cellwan_connection
    
    	Cellwan modem connection data
    	**type**\: list of  		 :py:class:`CellwanConnection <ydk.models.cisco_ios_xe.Cisco_IOS_XE_cellwan_oper.CellwanOperData.CellwanConnection>`
    
    .. attribute:: cellwan_security
    
    	Cellwan modem sim security data
    	**type**\: list of  		 :py:class:`CellwanSecurity <ydk.models.cisco_ios_xe.Cisco_IOS_XE_cellwan_oper.CellwanOperData.CellwanSecurity>`
    
    .. attribute:: cellwan_sms
    
    	Cellwan modem sms data
    	**type**\: list of  		 :py:class:`CellwanSms <ydk.models.cisco_ios_xe.Cisco_IOS_XE_cellwan_oper.CellwanOperData.CellwanSms>`
    
    .. attribute:: cellwan_gps
    
    	Cellwan modem gps data
    	**type**\: list of  		 :py:class:`CellwanGps <ydk.models.cisco_ios_xe.Cisco_IOS_XE_cellwan_oper.CellwanOperData.CellwanGps>`
    
    

    """

    _prefix = 'cellwan-ios-xe-oper'
    _revision = '2018-09-04'

    def __init__(self):
        super(CellwanOperData, self).__init__()
        self._top_entity = None

        self.yang_name = "cellwan-oper-data"
        self.yang_parent_name = "Cisco-IOS-XE-cellwan-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("cellwan-hardware", ("cellwan_hardware", CellwanOperData.CellwanHardware)), ("cellwan-radio", ("cellwan_radio", CellwanOperData.CellwanRadio)), ("cellwan-network", ("cellwan_network", CellwanOperData.CellwanNetwork)), ("cellwan-connection", ("cellwan_connection", CellwanOperData.CellwanConnection)), ("cellwan-security", ("cellwan_security", CellwanOperData.CellwanSecurity)), ("cellwan-sms", ("cellwan_sms", CellwanOperData.CellwanSms)), ("cellwan-gps", ("cellwan_gps", CellwanOperData.CellwanGps))])
        self._leafs = OrderedDict()

        self.cellwan_hardware = YList(self)
        self.cellwan_radio = YList(self)
        self.cellwan_network = YList(self)
        self.cellwan_connection = YList(self)
        self.cellwan_security = YList(self)
        self.cellwan_sms = YList(self)
        self.cellwan_gps = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XE-cellwan-oper:cellwan-oper-data"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(CellwanOperData, [], name, value)


    class CellwanHardware(Entity):
        """
        Cellwan modem hardware data
        
        .. attribute:: cellular_interface  (key)
        
        	Cellular interface
        	**type**\: str
        
        .. attribute:: cellular_firmware_version
        
        	Cellular Modem firmware version
        	**type**\: str
        
        .. attribute:: cellular_firmware_build_time
        
        	Cellular Modem firmware build time
        	**type**\: str
        
        .. attribute:: cellular_hardware_version
        
        	Cellular Modem hardware version
        	**type**\: str
        
        .. attribute:: cellular_device_model
        
        	Cellular Modem device model type
        	**type**\: str
        
        .. attribute:: cellular_imsi
        
        	Cellular Modem IMSI
        	**type**\: str
        
        .. attribute:: cellular_imei
        
        	Cellular Modem IMEI
        	**type**\: str
        
        .. attribute:: cellular_iccid
        
        	Cellular Modem ICCID
        	**type**\: str
        
        .. attribute:: cellular_msisdn
        
        	Cellular Modem MSISDN
        	**type**\: str
        
        .. attribute:: cellular_fsn
        
        	Cellular Modem FSN
        	**type**\: str
        
        .. attribute:: cellular_modem_status
        
        	Cellular Modem Status
        	**type**\:  :py:class:`ModemStatus <ydk.models.cisco_ios_xe.Cisco_IOS_XE_cellwan_oper.ModemStatus>`
        
        .. attribute:: cellular_modem_temperature
        
        	Cellular Modem temperature
        	**type**\: int
        
        	**range:** \-32768..32767
        
        .. attribute:: cellular_pri_skuid
        
        	Cellular Modem PRI sku id
        	**type**\: str
        
        .. attribute:: cellular_pri_version
        
        	Cellular Modem PRI version
        	**type**\: str
        
        .. attribute:: cellular_carrier
        
        	Cellular Modem carrier
        	**type**\: str
        
        .. attribute:: cellular_oem_pri_version
        
        	Cellular Modem OEM PRI version
        	**type**\: str
        
        

        """

        _prefix = 'cellwan-ios-xe-oper'
        _revision = '2018-09-04'

        def __init__(self):
            super(CellwanOperData.CellwanHardware, self).__init__()

            self.yang_name = "cellwan-hardware"
            self.yang_parent_name = "cellwan-oper-data"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['cellular_interface']
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('cellular_interface', (YLeaf(YType.str, 'cellular-interface'), ['str'])),
                ('cellular_firmware_version', (YLeaf(YType.str, 'cellular-firmware-version'), ['str'])),
                ('cellular_firmware_build_time', (YLeaf(YType.str, 'cellular-firmware-build-time'), ['str'])),
                ('cellular_hardware_version', (YLeaf(YType.str, 'cellular-hardware-version'), ['str'])),
                ('cellular_device_model', (YLeaf(YType.str, 'cellular-device-model'), ['str'])),
                ('cellular_imsi', (YLeaf(YType.str, 'cellular-imsi'), ['str'])),
                ('cellular_imei', (YLeaf(YType.str, 'cellular-imei'), ['str'])),
                ('cellular_iccid', (YLeaf(YType.str, 'cellular-iccid'), ['str'])),
                ('cellular_msisdn', (YLeaf(YType.str, 'cellular-msisdn'), ['str'])),
                ('cellular_fsn', (YLeaf(YType.str, 'cellular-fsn'), ['str'])),
                ('cellular_modem_status', (YLeaf(YType.enumeration, 'cellular-modem-status'), [('ydk.models.cisco_ios_xe.Cisco_IOS_XE_cellwan_oper', 'ModemStatus', '')])),
                ('cellular_modem_temperature', (YLeaf(YType.int16, 'cellular-modem-temperature'), ['int'])),
                ('cellular_pri_skuid', (YLeaf(YType.str, 'cellular-pri-skuid'), ['str'])),
                ('cellular_pri_version', (YLeaf(YType.str, 'cellular-pri-version'), ['str'])),
                ('cellular_carrier', (YLeaf(YType.str, 'cellular-carrier'), ['str'])),
                ('cellular_oem_pri_version', (YLeaf(YType.str, 'cellular-oem-pri-version'), ['str'])),
            ])
            self.cellular_interface = None
            self.cellular_firmware_version = None
            self.cellular_firmware_build_time = None
            self.cellular_hardware_version = None
            self.cellular_device_model = None
            self.cellular_imsi = None
            self.cellular_imei = None
            self.cellular_iccid = None
            self.cellular_msisdn = None
            self.cellular_fsn = None
            self.cellular_modem_status = None
            self.cellular_modem_temperature = None
            self.cellular_pri_skuid = None
            self.cellular_pri_version = None
            self.cellular_carrier = None
            self.cellular_oem_pri_version = None
            self._segment_path = lambda: "cellwan-hardware" + "[cellular-interface='" + str(self.cellular_interface) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XE-cellwan-oper:cellwan-oper-data/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CellwanOperData.CellwanHardware, ['cellular_interface', 'cellular_firmware_version', 'cellular_firmware_build_time', 'cellular_hardware_version', 'cellular_device_model', 'cellular_imsi', 'cellular_imei', 'cellular_iccid', 'cellular_msisdn', 'cellular_fsn', 'cellular_modem_status', 'cellular_modem_temperature', 'cellular_pri_skuid', 'cellular_pri_version', 'cellular_carrier', 'cellular_oem_pri_version'], name, value)


    class CellwanRadio(Entity):
        """
        Cellwan modem radio data
        
        .. attribute:: cellular_interface  (key)
        
        	Cellular interface
        	**type**\: str
        
        .. attribute:: technology
        
        	Cellular modem technology
        	**type**\:  :py:class:`ModemTechnology <ydk.models.cisco_ios_xe.Cisco_IOS_XE_cellwan_oper.ModemTechnology>`
        
        .. attribute:: radio_power_mode
        
        	Cellular modem radio power mode
        	**type**\:  :py:class:`CwRadioPowerStatus <ydk.models.cisco_ios_xe.Cisco_IOS_XE_cellwan_oper.CwRadioPowerStatus>`
        
        .. attribute:: radio_rx_channel
        
        	Cellular radio receive (Rx) channel number
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: radio_tx_channel
        
        	Cellular radio transmit (Tx) channel number
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: radio_band
        
        	Cellular radio band number
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: bandwidth
        
        	Cellular radio bandwidth in MHz
        	**type**\:  :py:class:`RadioBandwidth <ydk.models.cisco_ios_xe.Cisco_IOS_XE_cellwan_oper.RadioBandwidth>`
        
        .. attribute:: radio_rssi
        
        	Cellular RSSI \- Received Signal Strength Indication in dBm
        	**type**\: int
        
        	**range:** \-32768..32767
        
        .. attribute:: radio_rsrp
        
        	Cellular RSRP \- Reference Signal Received Power in dBm
        	**type**\: int
        
        	**range:** \-32768..32767
        
        .. attribute:: radio_rsrq
        
        	Cellular RSRQ \- Reference Signal Received Quality in dB
        	**type**\: int
        
        	**range:** \-128..127
        
        .. attribute:: radio_snr
        
        	Cellular SNR \- Signal to Noise Ratio in dB
        	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
        
        	**range:** \-92233720368547758.08..92233720368547758.07
        
        .. attribute:: radio_rat_preference
        
        	Cellular Radio Access Technology preference
        	**type**\:  :py:class:`RatPreference <ydk.models.cisco_ios_xe.Cisco_IOS_XE_cellwan_oper.RatPreference>`
        
        .. attribute:: radio_rat_selected
        
        	Cellular Radio Access Technology selected
        	**type**\:  :py:class:`RatTechnology <ydk.models.cisco_ios_xe.Cisco_IOS_XE_cellwan_oper.RatTechnology>`
        
        

        """

        _prefix = 'cellwan-ios-xe-oper'
        _revision = '2018-09-04'

        def __init__(self):
            super(CellwanOperData.CellwanRadio, self).__init__()

            self.yang_name = "cellwan-radio"
            self.yang_parent_name = "cellwan-oper-data"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['cellular_interface']
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('cellular_interface', (YLeaf(YType.str, 'cellular-interface'), ['str'])),
                ('technology', (YLeaf(YType.enumeration, 'technology'), [('ydk.models.cisco_ios_xe.Cisco_IOS_XE_cellwan_oper', 'ModemTechnology', '')])),
                ('radio_power_mode', (YLeaf(YType.enumeration, 'radio-power-mode'), [('ydk.models.cisco_ios_xe.Cisco_IOS_XE_cellwan_oper', 'CwRadioPowerStatus', '')])),
                ('radio_rx_channel', (YLeaf(YType.uint32, 'radio-rx-channel'), ['int'])),
                ('radio_tx_channel', (YLeaf(YType.uint32, 'radio-tx-channel'), ['int'])),
                ('radio_band', (YLeaf(YType.uint32, 'radio-band'), ['int'])),
                ('bandwidth', (YLeaf(YType.enumeration, 'bandwidth'), [('ydk.models.cisco_ios_xe.Cisco_IOS_XE_cellwan_oper', 'RadioBandwidth', '')])),
                ('radio_rssi', (YLeaf(YType.int16, 'radio-rssi'), ['int'])),
                ('radio_rsrp', (YLeaf(YType.int16, 'radio-rsrp'), ['int'])),
                ('radio_rsrq', (YLeaf(YType.int8, 'radio-rsrq'), ['int'])),
                ('radio_snr', (YLeaf(YType.str, 'radio-snr'), ['Decimal64'])),
                ('radio_rat_preference', (YLeaf(YType.enumeration, 'radio-rat-preference'), [('ydk.models.cisco_ios_xe.Cisco_IOS_XE_cellwan_oper', 'RatPreference', '')])),
                ('radio_rat_selected', (YLeaf(YType.enumeration, 'radio-rat-selected'), [('ydk.models.cisco_ios_xe.Cisco_IOS_XE_cellwan_oper', 'RatTechnology', '')])),
            ])
            self.cellular_interface = None
            self.technology = None
            self.radio_power_mode = None
            self.radio_rx_channel = None
            self.radio_tx_channel = None
            self.radio_band = None
            self.bandwidth = None
            self.radio_rssi = None
            self.radio_rsrp = None
            self.radio_rsrq = None
            self.radio_snr = None
            self.radio_rat_preference = None
            self.radio_rat_selected = None
            self._segment_path = lambda: "cellwan-radio" + "[cellular-interface='" + str(self.cellular_interface) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XE-cellwan-oper:cellwan-oper-data/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CellwanOperData.CellwanRadio, ['cellular_interface', 'technology', 'radio_power_mode', 'radio_rx_channel', 'radio_tx_channel', 'radio_band', 'bandwidth', 'radio_rssi', 'radio_rsrp', 'radio_rsrq', 'radio_snr', 'radio_rat_preference', 'radio_rat_selected'], name, value)


    class CellwanNetwork(Entity):
        """
        Cellwan modem network data
        
        .. attribute:: cellular_interface  (key)
        
        	Cellular interface
        	**type**\: str
        
        .. attribute:: cellular_modem_time
        
        	Current Cellular modem time
        	**type**\: str
        
        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
        
        .. attribute:: radio_access_technology_selected
        
        	Cellular Radio Access Technology selected
        	**type**\:  :py:class:`RatTechnology <ydk.models.cisco_ios_xe.Cisco_IOS_XE_cellwan_oper.RatTechnology>`
        
        .. attribute:: current_service_status
        
        	Cellular network current service status
        	**type**\:  :py:class:`ServiceStatus <ydk.models.cisco_ios_xe.Cisco_IOS_XE_cellwan_oper.ServiceStatus>`
        
        .. attribute:: current_system_identifier
        
        	Cellular modem current system identifier
        	**type**\: int
        
        	**range:** 0..65535
        
        .. attribute:: current_network_identifier
        
        	Cellular modem current network identifier
        	**type**\: int
        
        	**range:** 0..65535
        
        .. attribute:: current_service_type
        
        	Cellular network current service type
        	**type**\:  :py:class:`ModemService <ydk.models.cisco_ios_xe.Cisco_IOS_XE_cellwan_oper.ModemService>`
        
        .. attribute:: current_roaming_status
        
        	Cellular network current roaming status
        	**type**\: str
        
        .. attribute:: network_selection_mode
        
        	Cellular network selection mode
        	**type**\: str
        
        .. attribute:: network_name
        
        	Cellular current network name
        	**type**\: str
        
        .. attribute:: mobile_country_code
        
        	Cellular network mobile country code
        	**type**\: int
        
        	**range:** 0..65535
        
        .. attribute:: mobile_network_code
        
        	Cellular modem mobile network code
        	**type**\: int
        
        	**range:** 0..65535
        
        .. attribute:: packet_switch_domain_state
        
        	Cellular packet switched (PS) domain state
        	**type**\: str
        
        .. attribute:: lte_carrier_aggregation
        
        	Cellular LTE carrier aggregation (CA) state
        	**type**\:  :py:class:`LteCa <ydk.models.cisco_ios_xe.Cisco_IOS_XE_cellwan_oper.LteCa>`
        
        .. attribute:: registration_state
        
        	Cellular network registration state
        	**type**\:  :py:class:`RegState <ydk.models.cisco_ios_xe.Cisco_IOS_XE_cellwan_oper.RegState>`
        
        .. attribute:: emm_state
        
        	Cellular network EMM registration state
        	**type**\: str
        
        .. attribute:: emm_substate
        
        	Cellular network EMM sub\-state
        	**type**\: str
        
        .. attribute:: location_area_code
        
        	Cellular network location area code
        	**type**\: int
        
        	**range:** 0..65535
        
        .. attribute:: tracking_area_code
        
        	Cellular network tracking area code
        	**type**\: int
        
        	**range:** 0..65535
        
        .. attribute:: cell_id
        
        	Cellular network cell ID
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: negotiated_network_mtu
        
        	Cellular modem negotiated network MTU size
        	**type**\: int
        
        	**range:** 0..65535
        
        

        """

        _prefix = 'cellwan-ios-xe-oper'
        _revision = '2018-09-04'

        def __init__(self):
            super(CellwanOperData.CellwanNetwork, self).__init__()

            self.yang_name = "cellwan-network"
            self.yang_parent_name = "cellwan-oper-data"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['cellular_interface']
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('cellular_interface', (YLeaf(YType.str, 'cellular-interface'), ['str'])),
                ('cellular_modem_time', (YLeaf(YType.str, 'cellular-modem-time'), ['str'])),
                ('radio_access_technology_selected', (YLeaf(YType.enumeration, 'radio-access-technology-selected'), [('ydk.models.cisco_ios_xe.Cisco_IOS_XE_cellwan_oper', 'RatTechnology', '')])),
                ('current_service_status', (YLeaf(YType.enumeration, 'current-service-status'), [('ydk.models.cisco_ios_xe.Cisco_IOS_XE_cellwan_oper', 'ServiceStatus', '')])),
                ('current_system_identifier', (YLeaf(YType.uint16, 'current-system-identifier'), ['int'])),
                ('current_network_identifier', (YLeaf(YType.uint16, 'current-network-identifier'), ['int'])),
                ('current_service_type', (YLeaf(YType.enumeration, 'current-service-type'), [('ydk.models.cisco_ios_xe.Cisco_IOS_XE_cellwan_oper', 'ModemService', '')])),
                ('current_roaming_status', (YLeaf(YType.str, 'current-roaming-status'), ['str'])),
                ('network_selection_mode', (YLeaf(YType.str, 'network-selection-mode'), ['str'])),
                ('network_name', (YLeaf(YType.str, 'network-name'), ['str'])),
                ('mobile_country_code', (YLeaf(YType.uint16, 'mobile-country-code'), ['int'])),
                ('mobile_network_code', (YLeaf(YType.uint16, 'mobile-network-code'), ['int'])),
                ('packet_switch_domain_state', (YLeaf(YType.str, 'packet-switch-domain-state'), ['str'])),
                ('lte_carrier_aggregation', (YLeaf(YType.enumeration, 'lte-carrier-aggregation'), [('ydk.models.cisco_ios_xe.Cisco_IOS_XE_cellwan_oper', 'LteCa', '')])),
                ('registration_state', (YLeaf(YType.enumeration, 'registration-state'), [('ydk.models.cisco_ios_xe.Cisco_IOS_XE_cellwan_oper', 'RegState', '')])),
                ('emm_state', (YLeaf(YType.str, 'emm-state'), ['str'])),
                ('emm_substate', (YLeaf(YType.str, 'emm-substate'), ['str'])),
                ('location_area_code', (YLeaf(YType.uint16, 'location-area-code'), ['int'])),
                ('tracking_area_code', (YLeaf(YType.uint16, 'tracking-area-code'), ['int'])),
                ('cell_id', (YLeaf(YType.uint64, 'cell-id'), ['int'])),
                ('negotiated_network_mtu', (YLeaf(YType.uint16, 'negotiated-network-mtu'), ['int'])),
            ])
            self.cellular_interface = None
            self.cellular_modem_time = None
            self.radio_access_technology_selected = None
            self.current_service_status = None
            self.current_system_identifier = None
            self.current_network_identifier = None
            self.current_service_type = None
            self.current_roaming_status = None
            self.network_selection_mode = None
            self.network_name = None
            self.mobile_country_code = None
            self.mobile_network_code = None
            self.packet_switch_domain_state = None
            self.lte_carrier_aggregation = None
            self.registration_state = None
            self.emm_state = None
            self.emm_substate = None
            self.location_area_code = None
            self.tracking_area_code = None
            self.cell_id = None
            self.negotiated_network_mtu = None
            self._segment_path = lambda: "cellwan-network" + "[cellular-interface='" + str(self.cellular_interface) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XE-cellwan-oper:cellwan-oper-data/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CellwanOperData.CellwanNetwork, ['cellular_interface', 'cellular_modem_time', 'radio_access_technology_selected', 'current_service_status', 'current_system_identifier', 'current_network_identifier', 'current_service_type', 'current_roaming_status', 'network_selection_mode', 'network_name', 'mobile_country_code', 'mobile_network_code', 'packet_switch_domain_state', 'lte_carrier_aggregation', 'registration_state', 'emm_state', 'emm_substate', 'location_area_code', 'tracking_area_code', 'cell_id', 'negotiated_network_mtu'], name, value)


    class CellwanConnection(Entity):
        """
        Cellwan modem connection data
        
        .. attribute:: cellular_interface  (key)
        
        	Cellular interface
        	**type**\: str
        
        .. attribute:: active_profile
        
        	Cellular modem active profile number
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: cellular_packet_status
        
        	Cellular modem packet session status
        	**type**\:  :py:class:`PacketSessStatus <ydk.models.cisco_ios_xe.Cisco_IOS_XE_cellwan_oper.PacketSessStatus>`
        
        .. attribute:: tx_packets
        
        	Cellular data packets transmitted
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: rx_packets
        
        	Cellular data packets received
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: tx_bytes
        
        	Cellular data bytes transmitted
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: rx_bytes
        
        	Cellular data bytes received
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: ipv4_addr
        
        	Cellular interface IPv4 Address
        	**type**\: union of the below types:
        
        		**type**\: str
        
        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        		**type**\: str
        
        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
        
        .. attribute:: ipv6_addr
        
        	Cellular interface IPv6 Address
        	**type**\: union of the below types:
        
        		**type**\: str
        
        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        		**type**\: str
        
        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
        
        .. attribute:: ipv4_dns_pri
        
        	Cellular interface primary IPv4 DNS Address
        	**type**\: union of the below types:
        
        		**type**\: str
        
        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        		**type**\: str
        
        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
        
        .. attribute:: ipv4_dns_sec
        
        	Cellular interface secondary IPv4 DNS Address
        	**type**\: union of the below types:
        
        		**type**\: str
        
        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        		**type**\: str
        
        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
        
        .. attribute:: ipv6_dns_pri
        
        	Cellular interface primary IPv6 DNS Address
        	**type**\: union of the below types:
        
        		**type**\: str
        
        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        		**type**\: str
        
        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
        
        .. attribute:: ipv6_dns_sec
        
        	Cellular interface secondary IPv6 DNS Address
        	**type**\: union of the below types:
        
        		**type**\: str
        
        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        		**type**\: str
        
        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
        
        .. attribute:: scope
        
        	Cellular interface profile IP address scope
        	**type**\:  :py:class:`ProfileScope <ydk.models.cisco_ios_xe.Cisco_IOS_XE_cellwan_oper.ProfileScope>`
        
        

        """

        _prefix = 'cellwan-ios-xe-oper'
        _revision = '2018-09-04'

        def __init__(self):
            super(CellwanOperData.CellwanConnection, self).__init__()

            self.yang_name = "cellwan-connection"
            self.yang_parent_name = "cellwan-oper-data"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['cellular_interface']
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('cellular_interface', (YLeaf(YType.str, 'cellular-interface'), ['str'])),
                ('active_profile', (YLeaf(YType.uint64, 'active-profile'), ['int'])),
                ('cellular_packet_status', (YLeaf(YType.enumeration, 'cellular-packet-status'), [('ydk.models.cisco_ios_xe.Cisco_IOS_XE_cellwan_oper', 'PacketSessStatus', '')])),
                ('tx_packets', (YLeaf(YType.uint64, 'tx-packets'), ['int'])),
                ('rx_packets', (YLeaf(YType.uint64, 'rx-packets'), ['int'])),
                ('tx_bytes', (YLeaf(YType.uint64, 'tx-bytes'), ['int'])),
                ('rx_bytes', (YLeaf(YType.uint64, 'rx-bytes'), ['int'])),
                ('ipv4_addr', (YLeaf(YType.str, 'ipv4-addr'), ['str','str'])),
                ('ipv6_addr', (YLeaf(YType.str, 'ipv6-addr'), ['str','str'])),
                ('ipv4_dns_pri', (YLeaf(YType.str, 'ipv4-dns-pri'), ['str','str'])),
                ('ipv4_dns_sec', (YLeaf(YType.str, 'ipv4-dns-sec'), ['str','str'])),
                ('ipv6_dns_pri', (YLeaf(YType.str, 'ipv6-dns-pri'), ['str','str'])),
                ('ipv6_dns_sec', (YLeaf(YType.str, 'ipv6-dns-sec'), ['str','str'])),
                ('scope', (YLeaf(YType.enumeration, 'scope'), [('ydk.models.cisco_ios_xe.Cisco_IOS_XE_cellwan_oper', 'ProfileScope', '')])),
            ])
            self.cellular_interface = None
            self.active_profile = None
            self.cellular_packet_status = None
            self.tx_packets = None
            self.rx_packets = None
            self.tx_bytes = None
            self.rx_bytes = None
            self.ipv4_addr = None
            self.ipv6_addr = None
            self.ipv4_dns_pri = None
            self.ipv4_dns_sec = None
            self.ipv6_dns_pri = None
            self.ipv6_dns_sec = None
            self.scope = None
            self._segment_path = lambda: "cellwan-connection" + "[cellular-interface='" + str(self.cellular_interface) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XE-cellwan-oper:cellwan-oper-data/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CellwanOperData.CellwanConnection, ['cellular_interface', 'active_profile', 'cellular_packet_status', 'tx_packets', 'rx_packets', 'tx_bytes', 'rx_bytes', 'ipv4_addr', 'ipv6_addr', 'ipv4_dns_pri', 'ipv4_dns_sec', 'ipv6_dns_pri', 'ipv6_dns_sec', 'scope'], name, value)


    class CellwanSecurity(Entity):
        """
        Cellwan modem sim security data
        
        .. attribute:: cellular_interface  (key)
        
        	Cellular interface
        	**type**\: str
        
        .. attribute:: active_sim
        
        	Cellular modem active SIM slot status
        	**type**\: int
        
        	**range:** \-128..127
        
        .. attribute:: sim_num_switchover
        
        	Cellular modem SIM switchover attempts
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: chv1_status
        
        	Cellular SIM Card Holder Verification (CHV1) status
        	**type**\:  :py:class:`CellwanChv1SimStatus <ydk.models.cisco_ios_xe.Cisco_IOS_XE_cellwan_oper.CellwanChv1SimStatus>`
        
        .. attribute:: sim_status
        
        	Cellular SIM status
        	**type**\:  :py:class:`CellwanSimStatus <ydk.models.cisco_ios_xe.Cisco_IOS_XE_cellwan_oper.CellwanSimStatus>`
        
        .. attribute:: sim_oper
        
        	Cellular SIM user operation
        	**type**\:  :py:class:`CellwanSimUserOp <ydk.models.cisco_ios_xe.Cisco_IOS_XE_cellwan_oper.CellwanSimUserOp>`
        
        .. attribute:: num_retries
        
        	Cellular SIM number of CHV1 retries remaining
        	**type**\: int
        
        	**range:** \-128..127
        
        

        """

        _prefix = 'cellwan-ios-xe-oper'
        _revision = '2018-09-04'

        def __init__(self):
            super(CellwanOperData.CellwanSecurity, self).__init__()

            self.yang_name = "cellwan-security"
            self.yang_parent_name = "cellwan-oper-data"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['cellular_interface']
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('cellular_interface', (YLeaf(YType.str, 'cellular-interface'), ['str'])),
                ('active_sim', (YLeaf(YType.int8, 'active-sim'), ['int'])),
                ('sim_num_switchover', (YLeaf(YType.uint32, 'sim-num-switchover'), ['int'])),
                ('chv1_status', (YLeaf(YType.enumeration, 'chv1-status'), [('ydk.models.cisco_ios_xe.Cisco_IOS_XE_cellwan_oper', 'CellwanChv1SimStatus', '')])),
                ('sim_status', (YLeaf(YType.enumeration, 'sim-status'), [('ydk.models.cisco_ios_xe.Cisco_IOS_XE_cellwan_oper', 'CellwanSimStatus', '')])),
                ('sim_oper', (YLeaf(YType.enumeration, 'sim-oper'), [('ydk.models.cisco_ios_xe.Cisco_IOS_XE_cellwan_oper', 'CellwanSimUserOp', '')])),
                ('num_retries', (YLeaf(YType.int8, 'num-retries'), ['int'])),
            ])
            self.cellular_interface = None
            self.active_sim = None
            self.sim_num_switchover = None
            self.chv1_status = None
            self.sim_status = None
            self.sim_oper = None
            self.num_retries = None
            self._segment_path = lambda: "cellwan-security" + "[cellular-interface='" + str(self.cellular_interface) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XE-cellwan-oper:cellwan-oper-data/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CellwanOperData.CellwanSecurity, ['cellular_interface', 'active_sim', 'sim_num_switchover', 'chv1_status', 'sim_status', 'sim_oper', 'num_retries'], name, value)


    class CellwanSms(Entity):
        """
        Cellwan modem sms data
        
        .. attribute:: cellular_interface  (key)
        
        	Cellular interface
        	**type**\: str
        
        .. attribute:: in_sms_count
        
        	Number of incoming SMS stored in Cellular modem
        	**type**\: int
        
        	**range:** 0..65535
        
        .. attribute:: in_sms_archived
        
        	Number of incoming SMS archived in Cellular modem
        	**type**\: int
        
        	**range:** 0..65535
        
        .. attribute:: in_sms_deleted
        
        	Number of incoming SMS deleted in Cellular modem
        	**type**\: int
        
        	**range:** 0..65535
        
        .. attribute:: in_sms_max
        
        	Number of SIM/modem SMS record allocated
        	**type**\: int
        
        	**range:** 0..65535
        
        .. attribute:: in_sms_used
        
        	Number of SIM/modem SMS record used
        	**type**\: int
        
        	**range:** 0..65535
        
        .. attribute:: sms_callback_count
        
        	Number of SMS triggerred data callback
        	**type**\: int
        
        	**range:** 0..65535
        
        .. attribute:: in_sms_arch_count
        
        	Number of successful archive on in SMS
        	**type**\: int
        
        	**range:** 0..65535
        
        .. attribute:: in_sms_arch_error_count
        
        	Number of failed archive on in SMS
        	**type**\: int
        
        	**range:** 0..65535
        
        .. attribute:: out_sms_count
        
        	Number of outgoing SMS successfully sent
        	**type**\: int
        
        	**range:** 0..65535
        
        .. attribute:: out_sms_error_count
        
        	Number of outgoing SMS send failure
        	**type**\: int
        
        	**range:** 0..65535
        
        .. attribute:: out_sms_pending
        
        	Number of outgoing SMS pending
        	**type**\: int
        
        	**range:** 0..65535
        
        .. attribute:: out_sms_arch_count
        
        	Number of successful archive out in SMS
        	**type**\: int
        
        	**range:** 0..65535
        
        .. attribute:: out_sms_arch_error_count
        
        	Number of failed archive on out SMS
        	**type**\: int
        
        	**range:** 0..65535
        
        

        """

        _prefix = 'cellwan-ios-xe-oper'
        _revision = '2018-09-04'

        def __init__(self):
            super(CellwanOperData.CellwanSms, self).__init__()

            self.yang_name = "cellwan-sms"
            self.yang_parent_name = "cellwan-oper-data"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['cellular_interface']
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('cellular_interface', (YLeaf(YType.str, 'cellular-interface'), ['str'])),
                ('in_sms_count', (YLeaf(YType.uint16, 'in-sms-count'), ['int'])),
                ('in_sms_archived', (YLeaf(YType.uint16, 'in-sms-archived'), ['int'])),
                ('in_sms_deleted', (YLeaf(YType.uint16, 'in-sms-deleted'), ['int'])),
                ('in_sms_max', (YLeaf(YType.uint16, 'in-sms-max'), ['int'])),
                ('in_sms_used', (YLeaf(YType.uint16, 'in-sms-used'), ['int'])),
                ('sms_callback_count', (YLeaf(YType.uint16, 'sms-callback-count'), ['int'])),
                ('in_sms_arch_count', (YLeaf(YType.uint16, 'in-sms-arch-count'), ['int'])),
                ('in_sms_arch_error_count', (YLeaf(YType.uint16, 'in-sms-arch-error-count'), ['int'])),
                ('out_sms_count', (YLeaf(YType.uint16, 'out-sms-count'), ['int'])),
                ('out_sms_error_count', (YLeaf(YType.uint16, 'out-sms-error-count'), ['int'])),
                ('out_sms_pending', (YLeaf(YType.uint16, 'out-sms-pending'), ['int'])),
                ('out_sms_arch_count', (YLeaf(YType.uint16, 'out-sms-arch-count'), ['int'])),
                ('out_sms_arch_error_count', (YLeaf(YType.uint16, 'out-sms-arch-error-count'), ['int'])),
            ])
            self.cellular_interface = None
            self.in_sms_count = None
            self.in_sms_archived = None
            self.in_sms_deleted = None
            self.in_sms_max = None
            self.in_sms_used = None
            self.sms_callback_count = None
            self.in_sms_arch_count = None
            self.in_sms_arch_error_count = None
            self.out_sms_count = None
            self.out_sms_error_count = None
            self.out_sms_pending = None
            self.out_sms_arch_count = None
            self.out_sms_arch_error_count = None
            self._segment_path = lambda: "cellwan-sms" + "[cellular-interface='" + str(self.cellular_interface) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XE-cellwan-oper:cellwan-oper-data/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CellwanOperData.CellwanSms, ['cellular_interface', 'in_sms_count', 'in_sms_archived', 'in_sms_deleted', 'in_sms_max', 'in_sms_used', 'sms_callback_count', 'in_sms_arch_count', 'in_sms_arch_error_count', 'out_sms_count', 'out_sms_error_count', 'out_sms_pending', 'out_sms_arch_count', 'out_sms_arch_error_count'], name, value)


    class CellwanGps(Entity):
        """
        Cellwan modem gps data
        
        .. attribute:: cellular_interface  (key)
        
        	Cellular interface
        	**type**\: str
        
        .. attribute:: gps_feature_state
        
        	Cellular modem GPS feature state status
        	**type**\:  :py:class:`CwanGpsFeatureState <ydk.models.cisco_ios_xe.Cisco_IOS_XE_cellwan_oper.CwanGpsFeatureState>`
        
        .. attribute:: port_selected
        
        	Cellular modem GPS port selection status
        	**type**\:  :py:class:`CwanGpsPortSelected <ydk.models.cisco_ios_xe.Cisco_IOS_XE_cellwan_oper.CwanGpsPortSelected>`
        
        .. attribute:: state
        
        	Cellular modem GPS state status
        	**type**\:  :py:class:`CwanGpsState <ydk.models.cisco_ios_xe.Cisco_IOS_XE_cellwan_oper.CwanGpsState>`
        
        .. attribute:: mode_selected
        
        	Cellular modem GPS mode selection status
        	**type**\:  :py:class:`CwanGpsModeSelected <ydk.models.cisco_ios_xe.Cisco_IOS_XE_cellwan_oper.CwanGpsModeSelected>`
        
        .. attribute:: latitude
        
        	Cellular modem GPS latitude details
        	**type**\: str
        
        .. attribute:: longitude
        
        	Cellular modem GPS longitude details
        	**type**\: str
        
        .. attribute:: timestamp
        
        	Cellular modem GPS timestamp details
        	**type**\: str
        
        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
        
        

        """

        _prefix = 'cellwan-ios-xe-oper'
        _revision = '2018-09-04'

        def __init__(self):
            super(CellwanOperData.CellwanGps, self).__init__()

            self.yang_name = "cellwan-gps"
            self.yang_parent_name = "cellwan-oper-data"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['cellular_interface']
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('cellular_interface', (YLeaf(YType.str, 'cellular-interface'), ['str'])),
                ('gps_feature_state', (YLeaf(YType.enumeration, 'gps-feature-state'), [('ydk.models.cisco_ios_xe.Cisco_IOS_XE_cellwan_oper', 'CwanGpsFeatureState', '')])),
                ('port_selected', (YLeaf(YType.enumeration, 'port-selected'), [('ydk.models.cisco_ios_xe.Cisco_IOS_XE_cellwan_oper', 'CwanGpsPortSelected', '')])),
                ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xe.Cisco_IOS_XE_cellwan_oper', 'CwanGpsState', '')])),
                ('mode_selected', (YLeaf(YType.enumeration, 'mode-selected'), [('ydk.models.cisco_ios_xe.Cisco_IOS_XE_cellwan_oper', 'CwanGpsModeSelected', '')])),
                ('latitude', (YLeaf(YType.str, 'latitude'), ['str'])),
                ('longitude', (YLeaf(YType.str, 'longitude'), ['str'])),
                ('timestamp', (YLeaf(YType.str, 'timestamp'), ['str'])),
            ])
            self.cellular_interface = None
            self.gps_feature_state = None
            self.port_selected = None
            self.state = None
            self.mode_selected = None
            self.latitude = None
            self.longitude = None
            self.timestamp = None
            self._segment_path = lambda: "cellwan-gps" + "[cellular-interface='" + str(self.cellular_interface) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XE-cellwan-oper:cellwan-oper-data/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CellwanOperData.CellwanGps, ['cellular_interface', 'gps_feature_state', 'port_selected', 'state', 'mode_selected', 'latitude', 'longitude', 'timestamp'], name, value)

    def clone_ptr(self):
        self._top_entity = CellwanOperData()
        return self._top_entity

