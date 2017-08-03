""" Cisco_IOS_XR_drivers_media_eth_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR drivers\-media\-eth package operational data.

This module contains definitions
for the following management objects\:
  ethernet\-interface\: Ethernet operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class EthCtrlrAlarmState(Enum):
    """
    EthCtrlrAlarmState

    Ethernet alarm state

    .. data:: alarm_not_supported = 0

    	Not supported on this interface

    .. data:: alarm_set = 1

    	Alarm set

    .. data:: alarm_not_set = 2

    	Alarm not set

    """

    alarm_not_supported = Enum.YLeaf(0, "alarm-not-supported")

    alarm_set = Enum.YLeaf(1, "alarm-set")

    alarm_not_set = Enum.YLeaf(2, "alarm-not-set")


class EtherAinsStatus(Enum):
    """
    EtherAinsStatus

    Ether ains status

    .. data:: ains_soak_status_none = 0

    	AINS Soak timer not running

    .. data:: ains_soak_status_pending = 1

    	AINS Soak timer pending

    .. data:: ains_soak_status_running = 2

    	AINS Soak timer running

    """

    ains_soak_status_none = Enum.YLeaf(0, "ains-soak-status-none")

    ains_soak_status_pending = Enum.YLeaf(1, "ains-soak-status-pending")

    ains_soak_status_running = Enum.YLeaf(2, "ains-soak-status-running")


class EtherDomAlarm(Enum):
    """
    EtherDomAlarm

    Ether dom alarm

    .. data:: no_information = 0

    	DOM Alarm information is not available

    .. data:: alarm_high = 1

    	Alarm high

    .. data:: warning_high = 2

    	Warning high

    .. data:: normal = 3

    	Within normal parameters

    .. data:: warning_low = 4

    	Warning low

    .. data:: alarm_low = 5

    	Alarm low

    """

    no_information = Enum.YLeaf(0, "no-information")

    alarm_high = Enum.YLeaf(1, "alarm-high")

    warning_high = Enum.YLeaf(2, "warning-high")

    normal = Enum.YLeaf(3, "normal")

    warning_low = Enum.YLeaf(4, "warning-low")

    alarm_low = Enum.YLeaf(5, "alarm-low")


class EtherFlowcontrol(Enum):
    """
    EtherFlowcontrol

    Flowcontrol type

    .. data:: no_flowcontrol = 0

    	No flow control (disabled)

    .. data:: egress = 1

    	Traffic egress (pause frames ingress)

    .. data:: ingress = 2

    	Traffic ingress (pause frames egress)

    .. data:: bidirectional = 3

    	On both ingress and egress

    """

    no_flowcontrol = Enum.YLeaf(0, "no-flowcontrol")

    egress = Enum.YLeaf(1, "egress")

    ingress = Enum.YLeaf(2, "ingress")

    bidirectional = Enum.YLeaf(3, "bidirectional")


class EtherLedState(Enum):
    """
    EtherLedState

    Ether led state

    .. data:: led_state_unknown = 0

    	LED state is unknown

    .. data:: led_off = 1

    	LED is off

    .. data:: green_on = 2

    	LED is green

    .. data:: green_flashing = 3

    	LED is flashing green

    .. data:: yellow_on = 4

    	LED is yellow

    .. data:: yellow_flashing = 5

    	LED is flashing yellow

    .. data:: red_on = 6

    	LED is red

    .. data:: red_flashing = 7

    	LED is flashing red

    """

    led_state_unknown = Enum.YLeaf(0, "led-state-unknown")

    led_off = Enum.YLeaf(1, "led-off")

    green_on = Enum.YLeaf(2, "green-on")

    green_flashing = Enum.YLeaf(3, "green-flashing")

    yellow_on = Enum.YLeaf(4, "yellow-on")

    yellow_flashing = Enum.YLeaf(5, "yellow-flashing")

    red_on = Enum.YLeaf(6, "red-on")

    red_flashing = Enum.YLeaf(7, "red-flashing")


class EtherLinkState(Enum):
    """
    EtherLinkState

    Ethernet link state\: IEEE 802.3/802.3ae clause 30

    .5.1.1.4

    .. data:: state_undefined = 0

    	State undefined

    .. data:: unknown_state = 1

    	Initializing, true state not yet known

    .. data:: available = 2

    	Link or light normal, loopback normal

    .. data:: not_available = 3

    	Link loss or low light, no loopback

    .. data:: remote_fault = 4

    	Remote fault with no detail

    .. data:: invalid_signal = 5

    	Invalid signal, applies only to 10BASE-FB

    .. data:: remote_jabber = 6

    	Remote fault, reason known to be jabber

    .. data:: link_loss = 7

    	Remote fault, reason known to be far-end link

    	loss

    .. data:: remote_test = 8

    	Remote fault, reason known to be test

    .. data:: offline = 9

    	Offline (applies to auto-negotiation)

    .. data:: auto_neg_error = 10

    	Auto-Negotiation Error

    .. data:: pmd_link_fault = 11

    	PMD/PMA receive link fault

    .. data:: frame_loss = 12

    	WIS loss of frames

    .. data:: signal_loss = 13

    	WIS loss of signal

    .. data:: link_fault = 14

    	PCS receive link fault

    .. data:: excessive_ber = 15

    	PCS Bit Error Rate monitor reporting excessive

    	error rate

    .. data:: dxs_link_fault = 16

    	DTE XGXS receive link fault

    .. data:: pxs_link_fault = 17

    	PHY XGXS transmit link fault

    .. data:: security = 18

    	Security failure (not a valid part)

    .. data:: phy_not_present = 19

    	The optics for the port are not present

    .. data:: no_optic_license = 20

    	License error (No advanced optical license)

    .. data:: unsupported_module = 21

    	Module is not supported

    .. data:: dwdm_laser_shut = 22

    	DWDM Laser shutdown

    .. data:: wanphy_laser_shut = 23

    	WANPHY Laser shutdown

    .. data:: incompatible_config = 24

    	Incompatible configuration

    .. data:: system_error = 25

    	System error

    .. data:: wan_framing_error = 26

    	WAN Framing Error

    .. data:: otn_framing_error = 27

    	OTN Framing Error

    """

    state_undefined = Enum.YLeaf(0, "state-undefined")

    unknown_state = Enum.YLeaf(1, "unknown-state")

    available = Enum.YLeaf(2, "available")

    not_available = Enum.YLeaf(3, "not-available")

    remote_fault = Enum.YLeaf(4, "remote-fault")

    invalid_signal = Enum.YLeaf(5, "invalid-signal")

    remote_jabber = Enum.YLeaf(6, "remote-jabber")

    link_loss = Enum.YLeaf(7, "link-loss")

    remote_test = Enum.YLeaf(8, "remote-test")

    offline = Enum.YLeaf(9, "offline")

    auto_neg_error = Enum.YLeaf(10, "auto-neg-error")

    pmd_link_fault = Enum.YLeaf(11, "pmd-link-fault")

    frame_loss = Enum.YLeaf(12, "frame-loss")

    signal_loss = Enum.YLeaf(13, "signal-loss")

    link_fault = Enum.YLeaf(14, "link-fault")

    excessive_ber = Enum.YLeaf(15, "excessive-ber")

    dxs_link_fault = Enum.YLeaf(16, "dxs-link-fault")

    pxs_link_fault = Enum.YLeaf(17, "pxs-link-fault")

    security = Enum.YLeaf(18, "security")

    phy_not_present = Enum.YLeaf(19, "phy-not-present")

    no_optic_license = Enum.YLeaf(20, "no-optic-license")

    unsupported_module = Enum.YLeaf(21, "unsupported-module")

    dwdm_laser_shut = Enum.YLeaf(22, "dwdm-laser-shut")

    wanphy_laser_shut = Enum.YLeaf(23, "wanphy-laser-shut")

    incompatible_config = Enum.YLeaf(24, "incompatible-config")

    system_error = Enum.YLeaf(25, "system-error")

    wan_framing_error = Enum.YLeaf(26, "wan-framing-error")

    otn_framing_error = Enum.YLeaf(27, "otn-framing-error")


class EtherPfc(Enum):
    """
    EtherPfc

    Priority flowcontrol type

    .. data:: no_pfc = 0

    	No priority flow control (disabled)

    .. data:: on = 1

    	Priority flow control enabled

    """

    no_pfc = Enum.YLeaf(0, "no-pfc")

    on = Enum.YLeaf(1, "on")


class EtherPhyPresent(Enum):
    """
    EtherPhyPresent

    Ether phy present

    .. data:: phy_not_present = 0

    	No PHY present

    .. data:: phy_present = 1

    	PHY is present

    .. data:: no_information = 2

    	State is unknown

    """

    phy_not_present = Enum.YLeaf(0, "phy-not-present")

    phy_present = Enum.YLeaf(1, "phy-present")

    no_information = Enum.YLeaf(2, "no-information")


class EthernetBertErrCnt(Enum):
    """
    EthernetBertErrCnt

    Ethernet bert err cnt

    .. data:: no_count_type = 0

    	no count type

    .. data:: bit_error_count = 1

    	bit error count

    .. data:: frame_error_count = 2

    	frame error count

    .. data:: block_error_count = 3

    	block error count

    .. data:: ethernet_bert_err_cnt_types = 4

    	ethernet bert err cnt types

    """

    no_count_type = Enum.YLeaf(0, "no-count-type")

    bit_error_count = Enum.YLeaf(1, "bit-error-count")

    frame_error_count = Enum.YLeaf(2, "frame-error-count")

    block_error_count = Enum.YLeaf(3, "block-error-count")

    ethernet_bert_err_cnt_types = Enum.YLeaf(4, "ethernet-bert-err-cnt-types")


class EthernetBertPattern(Enum):
    """
    EthernetBertPattern

    Ethernet test patterns (IEEE spec 36A/48A)

    .. data:: no_test_pattern = 0

    	no test pattern

    .. data:: high_frequency = 1

    	high frequency

    .. data:: low_frequency = 2

    	low frequency

    .. data:: mixed_frequency = 3

    	mixed frequency

    .. data:: continuous_random = 4

    	continuous random

    .. data:: continuous_jitter = 5

    	continuous jitter

    .. data:: long_continuous_random = 6

    	long continuous random

    .. data:: short_continuous_random = 7

    	short continuous random

    .. data:: pseudorandom_seed_a = 8

    	pseudorandom seed a

    .. data:: pseudorandom_seed_b = 9

    	pseudorandom seed b

    .. data:: prbs31 = 10

    	prbs31

    .. data:: square_wave = 11

    	square wave

    .. data:: pseudorandom = 12

    	pseudorandom

    .. data:: ethernet_bert_pattern_types = 13

    	ethernet bert pattern types

    """

    no_test_pattern = Enum.YLeaf(0, "no-test-pattern")

    high_frequency = Enum.YLeaf(1, "high-frequency")

    low_frequency = Enum.YLeaf(2, "low-frequency")

    mixed_frequency = Enum.YLeaf(3, "mixed-frequency")

    continuous_random = Enum.YLeaf(4, "continuous-random")

    continuous_jitter = Enum.YLeaf(5, "continuous-jitter")

    long_continuous_random = Enum.YLeaf(6, "long-continuous-random")

    short_continuous_random = Enum.YLeaf(7, "short-continuous-random")

    pseudorandom_seed_a = Enum.YLeaf(8, "pseudorandom-seed-a")

    pseudorandom_seed_b = Enum.YLeaf(9, "pseudorandom-seed-b")

    prbs31 = Enum.YLeaf(10, "prbs31")

    square_wave = Enum.YLeaf(11, "square-wave")

    pseudorandom = Enum.YLeaf(12, "pseudorandom")

    ethernet_bert_pattern_types = Enum.YLeaf(13, "ethernet-bert-pattern-types")


class EthernetDev(Enum):
    """
    EthernetDev

    Ethernet dev

    .. data:: no_device = 0

    	no device

    .. data:: pma_pmd = 1

    	pma pmd

    .. data:: wis = 2

    	wis

    .. data:: pcs = 3

    	pcs

    .. data:: phy_xs = 4

    	phy xs

    .. data:: dte_xs = 5

    	dte xs

    .. data:: ethernet_num_dev = 6

    	ethernet num dev

    """

    no_device = Enum.YLeaf(0, "no-device")

    pma_pmd = Enum.YLeaf(1, "pma-pmd")

    wis = Enum.YLeaf(2, "wis")

    pcs = Enum.YLeaf(3, "pcs")

    phy_xs = Enum.YLeaf(4, "phy-xs")

    dte_xs = Enum.YLeaf(5, "dte-xs")

    ethernet_num_dev = Enum.YLeaf(6, "ethernet-num-dev")


class EthernetDevIf(Enum):
    """
    EthernetDevIf

    Ethernet dev if

    .. data:: no_interface = 0

    	no interface

    .. data:: xgmii = 1

    	xgmii

    .. data:: xaui = 2

    	xaui

    .. data:: ethernet_num_dev_if = 3

    	ethernet num dev if

    """

    no_interface = Enum.YLeaf(0, "no-interface")

    xgmii = Enum.YLeaf(1, "xgmii")

    xaui = Enum.YLeaf(2, "xaui")

    ethernet_num_dev_if = Enum.YLeaf(3, "ethernet-num-dev-if")


class EthernetDuplex(Enum):
    """
    EthernetDuplex

    Duplexity

    .. data:: ethernet_duplex_invalid = 0

    	ethernet duplex invalid

    .. data:: half_duplex = 1

    	half duplex

    .. data:: full_duplex = 2

    	full duplex

    """

    ethernet_duplex_invalid = Enum.YLeaf(0, "ethernet-duplex-invalid")

    half_duplex = Enum.YLeaf(1, "half-duplex")

    full_duplex = Enum.YLeaf(2, "full-duplex")


class EthernetFec(Enum):
    """
    EthernetFec

    FEC type

    .. data:: not_configured = 0

    	FEC not configured

    .. data:: standard = 1

    	Reed-Solomon encoding

    .. data:: disabled = 2

    	FEC explicitly disabled

    .. data:: base_r = 3

    	BASE-R encoding

    """

    not_configured = Enum.YLeaf(0, "not-configured")

    standard = Enum.YLeaf(1, "standard")

    disabled = Enum.YLeaf(2, "disabled")

    base_r = Enum.YLeaf(3, "base-r")


class EthernetIpg(Enum):
    """
    EthernetIpg

    Inter packet gap

    .. data:: standard = 0

    	IEEE standard value of 12

    .. data:: non_standard = 1

    	Non-standard value of 16

    """

    standard = Enum.YLeaf(0, "standard")

    non_standard = Enum.YLeaf(1, "non-standard")


class EthernetLoopback(Enum):
    """
    EthernetLoopback

    Loopback type

    .. data:: no_loopback = 0

    	Disabled

    .. data:: internal = 1

    	Loopback in the framer

    .. data:: line = 2

    	Loops peer's packets back to them

    .. data:: external = 3

    	tx externally connected to rx

    """

    no_loopback = Enum.YLeaf(0, "no-loopback")

    internal = Enum.YLeaf(1, "internal")

    line = Enum.YLeaf(2, "line")

    external = Enum.YLeaf(3, "external")


class EthernetMedia(Enum):
    """
    EthernetMedia

    Ethernet media types\: IEEE 802.3/802.3ae clause

    30.5.1.1.2

    .. data:: ethernet_other = 0

    	IEEE 802.3/802.3ae clause 30.2.5

    .. data:: ethernet_unknown = 1

    	Initializing, true state or type not yet known

    .. data:: ethernet_aui = 2

    	No internal MAU, view from AUI

    .. data:: ethernet_10base5 = 3

    	Thick coax MAU

    .. data:: ethernet_foirl = 4

    	FOIRL MAU as specified in 9.9

    .. data:: ethernet_10base2 = 5

    	Thin coax MAU

    .. data:: ethernet_10broad36 = 6

    	Broadband DTE MAU

    .. data:: ethernet_10base = 7

    	UTP MAU, duplexity unknown

    .. data:: ethernet_10base_thd = 8

    	UTP MAU, half duplex

    .. data:: ethernet_10base_tfd = 9

    	UTP MAU, full duplex

    .. data:: ethernet_10base_fp = 10

    	Passive fiber MAU

    .. data:: ethernet_10base_fb = 11

    	Synchronous fiber MAU

    .. data:: ethernet_10base_fl = 12

    	Asynchronous fiber MAU, duplexity unknown

    .. data:: ethernet_10base_flhd = 13

    	Asynchronous fiber MAU, half duplex

    .. data:: ethernet_10base_flfd = 14

    	Asynchronous fiber MAU, full duplex

    .. data:: ethernet_100base_t4 = 15

    	Four-pair Category 3 UTP

    .. data:: ethernet_100base_tx = 16

    	Two-pair Category 5 UTP, duplexity unknown

    .. data:: ethernet_100base_txhd = 17

    	Two-pair Category 5 UTP, half duplex

    .. data:: ethernet_100base_txfd = 18

    	Two-pair Category 5 UTP, full duplex

    .. data:: ethernet_100base_fx = 19

    	X fiber over PMD, duplexity unknown

    .. data:: ethernet_100base_fxhd = 20

    	X fiber over PMD, half duplex

    .. data:: ethernet_100base_fxfd = 21

    	X fiber over PMD, full duplex

    .. data:: ethernet_100base_ex = 22

    	X fiber over PMD (40km), duplexity unknown

    .. data:: ethernet_100base_exhd = 23

    	X fiber over PMD (40km), half duplex

    .. data:: ethernet_100base_exfd = 24

    	X fiber over PMD (40km), full duplex

    .. data:: ethernet_100base_t2 = 25

    	Two-pair Category 3 UTP, duplexity unknown

    .. data:: ethernet_100base_t2hd = 26

    	Two-pair Category 3 UTP, half duplex

    .. data:: ethernet_100base_t2fd = 27

    	Two-pair Category 3 UTP, full duplex

    .. data:: ethernet_1000base_x = 28

    	X PCS/PMA, duplexity unknown

    .. data:: ethernet_1000base_xhd = 29

    	X 1000BASE-XHDX PCS/PMA, half duplex

    .. data:: ethernet_1000base_xfd = 30

    	X PCS/PMA, full duplex

    .. data:: ethernet_1000base_lx = 31

    	X fiber over long-wl laser PMD, duplexity

    	unknown

    .. data:: ethernet_1000base_lxhd = 32

    	X fiber over long-wl laser PMD, half duplex

    .. data:: ethernet_1000base_lxfd = 33

    	X fiber over long-wl laser PMD, full duplex

    .. data:: ethernet_1000base_sx = 34

    	X fiber over short-wl laser PMD, duplexity

    	unknown

    .. data:: ethernet_1000base_sxhd = 35

    	X fiber over short-wl laser PMD, half duplex

    .. data:: ethernet_1000base_sxfd = 36

    	X fiber over short-wl laser PMD, full duplex

    .. data:: ethernet_1000base_cx = 37

    	X copper over 150-Ohm balanced PMD, duplexity

    	unknown

    .. data:: ethernet_1000base_cxhd = 38

    	X copper over 150-Ohm balancedPMD, half duplex

    .. data:: ethernet_1000base_cxfd = 39

    	X copper over 150-Ohm balancedPMD, full duplex

    .. data:: ethernet_1000base = 40

    	Four-pair Category 5 UTP PHY, duplexity unknown

    .. data:: ethernet_1000base_thd = 41

    	Four-pair Category 5 UTP PHY, half duplex

    .. data:: ethernet_1000base_tfd = 42

    	Four-pair Category 5 UTP PHY, full duplex

    .. data:: ethernet_10gbase_x = 43

    	X PCS/PMA 

    .. data:: ethernet_10gbase_lx4 = 44

    	X fiber over 4 lane 1310nm optics

    .. data:: ethernet_10gbase_r = 45

    	R PCS/PMA

    .. data:: ethernet_10gbase_er = 46

    	R fiber over 1550nm optics

    .. data:: ethernet_10gbase_lr = 47

    	R fiber over 1310nm optics

    .. data:: ethernet_10gbase_sr = 48

    	R fiber over 850nm optics

    .. data:: ethernet_10gbase_w = 49

    	W PCS/PMA

    .. data:: ethernet_10gbase_ew = 50

    	W fiber over 1550nm optics

    .. data:: ethernet_10gbase_lw = 51

    	W fiber over 1310nm optics

    .. data:: ethernet_10gbase_sw = 52

    	W fiber over 850nm optics

    .. data:: ethernet_1000base_zx = 53

    	Single-mode fiber over 1550nm optics (Cisco)

    .. data:: ethernet_1000base_cwdm = 54

    	CWDM with unknown wavelength optics

    .. data:: ethernet_1000base_cwdm_1470 = 55

    	CWDM with 1470nm optics

    .. data:: ethernet_1000base_cwdm_1490 = 56

    	CWDM with 1490nm optics

    .. data:: ethernet_1000base_cwdm_1510 = 57

    	CWDM with 1510nm optics

    .. data:: ethernet_1000base_cwdm_1530 = 58

    	CWDM with 1530nm optics

    .. data:: ethernet_1000base_cwdm_1550 = 59

    	CWDM with 1550nm optics

    .. data:: ethernet_1000base_cwdm_1570 = 60

    	CWDM with 1570nm optics

    .. data:: ethernet_1000base_cwdm_1590 = 61

    	CWDM with 1590nm optics

    .. data:: ethernet_1000base_cwdm_1610 = 62

    	CWDM with 1610nm optics

    .. data:: ethernet_10gbase_zr = 63

    	Cisco-defined, over 1550nm optics

    .. data:: ethernet_10gbase_dwdm = 64

    	DWDM optics

    .. data:: ethernet_100gbase_lr4 = 65

    	fiber over 4 lane optics (long reach)

    .. data:: ethernet_1000base_dwdm = 66

    	DWDM optics

    .. data:: ethernet_1000base_dwdm_1533 = 67

    	DWDM with 1533nm optics

    .. data:: ethernet_1000base_dwdm_1537 = 68

    	DWDM with 1537nm optics

    .. data:: ethernet_1000base_dwdm_1541 = 69

    	DWDM with 1541nm optics

    .. data:: ethernet_1000base_dwdm_1545 = 70

    	DWDM with 1545nm optics

    .. data:: ethernet_1000base_dwdm_1549 = 71

    	DWDM with 1549nm optics

    .. data:: ethernet_1000base_dwdm_1553 = 72

    	DWDM with 1553nm optics

    .. data:: ethernet_1000base_dwdm_1557 = 73

    	DWDM with 1557nm optics

    .. data:: ethernet_1000base_dwdm_1561 = 74

    	DWDM with 1561nm optics

    .. data:: ethernet_40gbase_lr4 = 75

    	fiber over 4 lane optics (long reach)

    .. data:: ethernet_40gbase_er4 = 76

    	fiber over 4 lane optics (extended reach)

    .. data:: ethernet_100gbase_er4 = 77

    	fiber over 4 lane optics (extended reach)

    .. data:: ethernet_1000base_ex = 78

    	X fiber over 1310nm optics

    .. data:: ethernet_1000base_bx10_d = 79

    	X fibre (D, 10km)

    .. data:: ethernet_1000base_bx10_u = 80

    	X fibre (U, 10km)

    .. data:: ethernet_1000base_dwdm_1561_42 = 81

    	DWDM with 1561.42nm optics

    .. data:: ethernet_1000base_dwdm_1560_61 = 82

    	DWDM with 1560.61nm optics

    .. data:: ethernet_1000base_dwdm_1559_79 = 83

    	DWDM with 1559.79nm optics

    .. data:: ethernet_1000base_dwdm_1558_98 = 84

    	DWDM with 1558.98nm optics

    .. data:: ethernet_1000base_dwdm_1558_17 = 85

    	DWDM with 1558.17nm optics

    .. data:: ethernet_1000base_dwdm_1557_36 = 86

    	DWDM with 1557.36nm optics

    .. data:: ethernet_1000base_dwdm_1556_55 = 87

    	DWDM with 1556.55nm optics

    .. data:: ethernet_1000base_dwdm_1555_75 = 88

    	DWDM with 1555.75nm optics

    .. data:: ethernet_1000base_dwdm_1554_94 = 89

    	DWDM with 1554.94nm optics

    .. data:: ethernet_1000base_dwdm_1554_13 = 90

    	DWDM with 1554.13nm optics

    .. data:: ethernet_1000base_dwdm_1553_33 = 91

    	DWDM with 1553.33nm optics

    .. data:: ethernet_1000base_dwdm_1552_52 = 92

    	DWDM with 1552.52nm optics

    .. data:: ethernet_1000base_dwdm_1551_72 = 93

    	DWDM with 1551.72nm optics

    .. data:: ethernet_1000base_dwdm_1550_92 = 94

    	DWDM with 1550.92nm optics

    .. data:: ethernet_1000base_dwdm_1550_12 = 95

    	DWDM with 1550.12nm optics

    .. data:: ethernet_1000base_dwdm_1549_32 = 96

    	DWDM with 1549.32nm optics

    .. data:: ethernet_1000base_dwdm_1548_51 = 97

    	DWDM with 1548.51nm optics

    .. data:: ethernet_1000base_dwdm_1547_72 = 98

    	DWDM with 1547.72nm optics

    .. data:: ethernet_1000base_dwdm_1546_92 = 99

    	DWDM with 1546.92nm optics

    .. data:: ethernet_1000base_dwdm_1546_12 = 100

    	DWDM with 1546.12nm optics

    .. data:: ethernet_1000base_dwdm_1545_32 = 101

    	DWDM with 1545.32nm optics

    .. data:: ethernet_1000base_dwdm_1544_53 = 102

    	DWDM with 1544.53nm optics

    .. data:: ethernet_1000base_dwdm_1543_73 = 103

    	DWDM with 1543.73nm optics

    .. data:: ethernet_1000base_dwdm_1542_94 = 104

    	DWDM with 1542.94nm optics

    .. data:: ethernet_1000base_dwdm_1542_14 = 105

    	DWDM with 1542.14nm optics

    .. data:: ethernet_1000base_dwdm_1541_35 = 106

    	DWDM with 1541.35nm optics

    .. data:: ethernet_1000base_dwdm_1540_56 = 107

    	DWDM with 1540.56nm optics

    .. data:: ethernet_1000base_dwdm_1539_77 = 108

    	DWDM with 1539.77nm optics

    .. data:: ethernet_1000base_dwdm_1538_98 = 109

    	DWDM with 1538.98nm optics

    .. data:: ethernet_1000base_dwdm_1538_19 = 110

    	DWDM with 1538.19nm optics

    .. data:: ethernet_1000base_dwdm_1537_40 = 111

    	DWDM with 1537.40nm optics

    .. data:: ethernet_1000base_dwdm_1536_61 = 112

    	DWDM with 1536.61nm optics

    .. data:: ethernet_1000base_dwdm_1535_82 = 113

    	DWDM with 1535.82nm optics

    .. data:: ethernet_1000base_dwdm_1535_04 = 114

    	DWDM with 1535.04nm optics

    .. data:: ethernet_1000base_dwdm_1534_25 = 115

    	DWDM with 1534.25nm optics

    .. data:: ethernet_1000base_dwdm_1533_47 = 116

    	DWDM with 1533.47nm optics

    .. data:: ethernet_1000base_dwdm_1532_68 = 117

    	DWDM with 1532.68nm optics

    .. data:: ethernet_1000base_dwdm_1531_90 = 118

    	DWDM with 1531.90nm optics

    .. data:: ethernet_1000base_dwdm_1531_12 = 119

    	DWDM with 1531.12nm optics

    .. data:: ethernet_1000base_dwdm_1530_33 = 120

    	DWDM with 1530.33nm optics

    .. data:: ethernet_1000base_dwdm_tunable = 121

    	DWDM with tunable optics

    .. data:: ethernet_10gbase_dwdm_1561_42 = 122

    	DWDM with 1561.42nm optics

    .. data:: ethernet_10gbase_dwdm_1560_61 = 123

    	DWDM with 1560.61nm optics

    .. data:: ethernet_10gbase_dwdm_1559_79 = 124

    	DWDM with 1559.79nm optics

    .. data:: ethernet_10gbase_dwdm_1558_98 = 125

    	DWDM with 1558.98nm optics

    .. data:: ethernet_10gbase_dwdm_1558_17 = 126

    	DWDM with 1558.17nm optics

    .. data:: ethernet_10gbase_dwdm_1557_36 = 127

    	DWDM with 1557.36nm optics

    .. data:: ethernet_10gbase_dwdm_1556_55 = 128

    	DWDM with 1556.55nm optics

    .. data:: ethernet_10gbase_dwdm_1555_75 = 129

    	DWDM with 1555.75nm optics

    .. data:: ethernet_10gbase_dwdm_1554_94 = 130

    	DWDM with 1554.94nm optics

    .. data:: ethernet_10gbase_dwdm_1554_13 = 131

    	DWDM with 1554.13nm optics

    .. data:: ethernet_10gbase_dwdm_1553_33 = 132

    	DWDM with 1553.33nm optics

    .. data:: ethernet_10gbase_dwdm_1552_52 = 133

    	DWDM with 1552.52nm optics

    .. data:: ethernet_10gbase_dwdm_1551_72 = 134

    	DWDM with 1551.72nm optics

    .. data:: ethernet_10gbase_dwdm_1550_92 = 135

    	DWDM with 1550.92nm optics

    .. data:: ethernet_10gbase_dwdm_1550_12 = 136

    	DWDM with 1550.12nm optics

    .. data:: ethernet_10gbase_dwdm_1549_32 = 137

    	DWDM with 1549.32nm optics

    .. data:: ethernet_10gbase_dwdm_1548_51 = 138

    	DWDM with 1548.51nm optics

    .. data:: ethernet_10gbase_dwdm_1547_72 = 139

    	DWDM with 1547.72nm optics

    .. data:: ethernet_10gbase_dwdm_1546_92 = 140

    	DWDM with 1546.92nm optics

    .. data:: ethernet_10gbase_dwdm_1546_12 = 141

    	DWDM with 1546.12nm optics

    .. data:: ethernet_10gbase_dwdm_1545_32 = 142

    	DWDM with 1545.32nm optics

    .. data:: ethernet_10gbase_dwdm_1544_53 = 143

    	DWDM with 1544.53nm optics

    .. data:: ethernet_10gbase_dwdm_1543_73 = 144

    	DWDM with 1543.73nm optics

    .. data:: ethernet_10gbase_dwdm_1542_94 = 145

    	DWDM with 1542.94nm optics

    .. data:: ethernet_10gbase_dwdm_1542_14 = 146

    	DWDM with 1542.14nm optics

    .. data:: ethernet_10gbase_dwdm_1541_35 = 147

    	DWDM with 1541.35nm optics

    .. data:: ethernet_10gbase_dwdm_1540_56 = 148

    	DWDM with 1540.56nm optics

    .. data:: ethernet_10gbase_dwdm_1539_77 = 149

    	DWDM with 1539.77nm optics

    .. data:: ethernet_10gbase_dwdm_1538_98 = 150

    	DWDM with 1538.98nm optics

    .. data:: ethernet_10gbase_dwdm_1538_19 = 151

    	DWDM with 1538.19nm optics

    .. data:: ethernet_10gbase_dwdm_1537_40 = 152

    	DWDM with 1537.40nm optics

    .. data:: ethernet_10gbase_dwdm_1536_61 = 153

    	DWDM with 1536.61nm optics

    .. data:: ethernet_10gbase_dwdm_1535_82 = 154

    	DWDM with 1535.82nm optics

    .. data:: ethernet_10gbase_dwdm_1535_04 = 155

    	DWDM with 1535.04nm optics

    .. data:: ethernet_10gbase_dwdm_1534_25 = 156

    	DWDM with 1534.25nm optics

    .. data:: ethernet_10gbase_dwdm_1533_47 = 157

    	DWDM with 1533.47nm optics

    .. data:: ethernet_10gbase_dwdm_1532_68 = 158

    	DWDM with 1532.68nm optics

    .. data:: ethernet_10gbase_dwdm_1531_90 = 159

    	DWDM with 1531.90nm optics

    .. data:: ethernet_10gbase_dwdm_1531_12 = 160

    	DWDM with 1531.12nm optics

    .. data:: ethernet_10gbase_dwdm_1530_33 = 161

    	DWDM with 1530.33nm optics

    .. data:: ethernet_10gbase_dwdm_tunable = 162

    	DWDM with tunable optics

    .. data:: ethernet_40gbase_dwdm_1561_42 = 163

    	DWDM with 1561.42nm optics

    .. data:: ethernet_40gbase_dwdm_1560_61 = 164

    	DWDM with 1560.61nm optics

    .. data:: ethernet_40gbase_dwdm_1559_79 = 165

    	DWDM with 1559.79nm optics

    .. data:: ethernet_40gbase_dwdm_1558_98 = 166

    	DWDM with 1558.98nm optics

    .. data:: ethernet_40gbase_dwdm_1558_17 = 167

    	DWDM with 1558.17nm optics

    .. data:: ethernet_40gbase_dwdm_1557_36 = 168

    	DWDM with 1557.36nm optics

    .. data:: ethernet_40gbase_dwdm_1556_55 = 169

    	DWDM with 1556.55nm optics

    .. data:: ethernet_40gbase_dwdm_1555_75 = 170

    	DWDM with 1555.75nm optics

    .. data:: ethernet_40gbase_dwdm_1554_94 = 171

    	DWDM with 1554.94nm optics

    .. data:: ethernet_40gbase_dwdm_1554_13 = 172

    	DWDM with 1554.13nm optics

    .. data:: ethernet_40gbase_dwdm_1553_33 = 173

    	DWDM with 1553.33nm optics

    .. data:: ethernet_40gbase_dwdm_1552_52 = 174

    	DWDM with 1552.52nm optics

    .. data:: ethernet_40gbase_dwdm_1551_72 = 175

    	DWDM with 1551.72nm optics

    .. data:: ethernet_40gbase_dwdm_1550_92 = 176

    	DWDM with 1550.92nm optics

    .. data:: ethernet_40gbase_dwdm_1550_12 = 177

    	DWDM with 1550.12nm optics

    .. data:: ethernet_40gbase_dwdm_1549_32 = 178

    	DWDM with 1549.32nm optics

    .. data:: ethernet_40gbase_dwdm_1548_51 = 179

    	DWDM with 1548.51nm optics

    .. data:: ethernet_40gbase_dwdm_1547_72 = 180

    	DWDM with 1547.72nm optics

    .. data:: ethernet_40gbase_dwdm_1546_92 = 181

    	DWDM with 1546.92nm optics

    .. data:: ethernet_40gbase_dwdm_1546_12 = 182

    	DWDM with 1546.12nm optics

    .. data:: ethernet_40gbase_dwdm_1545_32 = 183

    	DWDM with 1545.32nm optics

    .. data:: ethernet_40gbase_dwdm_1544_53 = 184

    	DWDM with 1544.53nm optics

    .. data:: ethernet_40gbase_dwdm_1543_73 = 185

    	DWDM with 1543.73nm optics

    .. data:: ethernet_40gbase_dwdm_1542_94 = 186

    	DWDM with 1542.94nm optics

    .. data:: ethernet_40gbase_dwdm_1542_14 = 187

    	DWDM with 1542.14nm optics

    .. data:: ethernet_40gbase_dwdm_1541_35 = 188

    	DWDM with 1541.35nm optics

    .. data:: ethernet_40gbase_dwdm_1540_56 = 189

    	DWDM with 1540.56nm optics

    .. data:: ethernet_40gbase_dwdm_1539_77 = 190

    	DWDM with 1539.77nm optics

    .. data:: ethernet_40gbase_dwdm_1538_98 = 191

    	DWDM with 1538.98nm optics

    .. data:: ethernet_40gbase_dwdm_1538_19 = 192

    	DWDM with 1538.19nm optics

    .. data:: ethernet_40gbase_dwdm_1537_40 = 193

    	DWDM with 1537.40nm optics

    .. data:: ethernet_40gbase_dwdm_1536_61 = 194

    	DWDM with 1536.61nm optics

    .. data:: ethernet_40gbase_dwdm_1535_82 = 195

    	DWDM with 1535.82nm optics

    .. data:: ethernet_40gbase_dwdm_1535_04 = 196

    	DWDM with 1535.04nm optics

    .. data:: ethernet_40gbase_dwdm_1534_25 = 197

    	DWDM with 1534.25nm optics

    .. data:: ethernet_40gbase_dwdm_1533_47 = 198

    	DWDM with 1533.47nm optics

    .. data:: ethernet_40gbase_dwdm_1532_68 = 199

    	DWDM with 1532.68nm optics

    .. data:: ethernet_40gbase_dwdm_1531_90 = 200

    	DWDM with 1531.90nm optics

    .. data:: ethernet_40gbase_dwdm_1531_12 = 201

    	DWDM with 1531.12nm optics

    .. data:: ethernet_40gbase_dwdm_1530_33 = 202

    	DWDM with 1530.33nm optics

    .. data:: ethernet_40gbase_dwdm_tunable = 203

    	DWDM with tunable optics

    .. data:: ethernet_100gbase_dwdm_1561_42 = 204

    	DWDM with 1561.42nm optics

    .. data:: ethernet_100gbase_dwdm_1560_61 = 205

    	DWDM with 1560.61nm optics

    .. data:: ethernet_100gbase_dwdm_1559_79 = 206

    	DWDM with 1559.79nm optics

    .. data:: ethernet_100gbase_dwdm_1558_98 = 207

    	DWDM with 1558.98nm optics

    .. data:: ethernet_100gbase_dwdm_1558_17 = 208

    	DWDM with 1558.17nm optics

    .. data:: ethernet_100gbase_dwdm_1557_36 = 209

    	DWDM with 1557.36nm optics

    .. data:: ethernet_100gbase_dwdm_1556_55 = 210

    	DWDM with 1556.55nm optics

    .. data:: ethernet_100gbase_dwdm_1555_75 = 211

    	DWDM with 1555.75nm optics

    .. data:: ethernet_100gbase_dwdm_1554_94 = 212

    	DWDM with 1554.94nm optics

    .. data:: ethernet_100gbase_dwdm_1554_13 = 213

    	DWDM with 1554.13nm optics

    .. data:: ethernet_100gbase_dwdm_1553_33 = 214

    	DWDM with 1553.33nm optics

    .. data:: ethernet_100gbase_dwdm_1552_52 = 215

    	DWDM with 1552.52nm optics

    .. data:: ethernet_100gbase_dwdm_1551_72 = 216

    	DWDM with 1551.72nm optics

    .. data:: ethernet_100gbase_dwdm_1550_92 = 217

    	DWDM with 1550.92nm optics

    .. data:: ethernet_100gbase_dwdm_1550_12 = 218

    	DWDM with 1550.12nm optics

    .. data:: ethernet_100gbase_dwdm_1549_32 = 219

    	DWDM with 1549.32nm optics

    .. data:: ethernet_100gbase_dwdm_1548_51 = 220

    	DWDM with 1548.51nm optics

    .. data:: ethernet_100gbase_dwdm_1547_72 = 221

    	DWDM with 1547.72nm optics

    .. data:: ethernet_100gbase_dwdm_1546_92 = 222

    	DWDM with 1546.92nm optics

    .. data:: ethernet_100gbase_dwdm_1546_12 = 223

    	DWDM with 1546.12nm optics

    .. data:: ethernet_100gbase_dwdm_1545_32 = 224

    	DWDM with 1545.32nm optics

    .. data:: ethernet_100gbase_dwdm_1544_53 = 225

    	DWDM with 1544.53nm optics

    .. data:: ethernet_100gbase_dwdm_1543_73 = 226

    	DWDM with 1543.73nm optics

    .. data:: ethernet_100gbase_dwdm_1542_94 = 227

    	DWDM with 1542.94nm optics

    .. data:: ethernet_100gbase_dwdm_1542_14 = 228

    	DWDM with 1542.14nm optics

    .. data:: ethernet_100gbase_dwdm_1541_35 = 229

    	DWDM with 1541.35nm optics

    .. data:: ethernet_100gbase_dwdm_1540_56 = 230

    	DWDM with 1540.56nm optics

    .. data:: ethernet_100gbase_dwdm_1539_77 = 231

    	DWDM with 1539.77nm optics

    .. data:: ethernet_100gbase_dwdm_1538_98 = 232

    	DWDM with 1538.98nm optics

    .. data:: ethernet_100gbase_dwdm_1538_19 = 233

    	DWDM with 1538.19nm optics

    .. data:: ethernet_100gbase_dwdm_1537_40 = 234

    	DWDM with 1537.40nm optics

    .. data:: ethernet_100gbase_dwdm_1536_61 = 235

    	DWDM with 1536.61nm optics

    .. data:: ethernet_100gbase_dwdm_1535_82 = 236

    	DWDM with 1535.82nm optics

    .. data:: ethernet_100gbase_dwdm_1535_04 = 237

    	DWDM with 1535.04nm optics

    .. data:: ethernet_100gbase_dwdm_1534_25 = 238

    	DWDM with 1534.25nm optics

    .. data:: ethernet_100gbase_dwdm_1533_47 = 239

    	DWDM with 1533.47nm optics

    .. data:: ethernet_100gbase_dwdm_1532_68 = 240

    	DWDM with 1532.68nm optics

    .. data:: ethernet_100gbase_dwdm_1531_90 = 241

    	DWDM with 1531.90nm optics

    .. data:: ethernet_100gbase_dwdm_1531_12 = 242

    	DWDM with 1531.12nm optics

    .. data:: ethernet_100gbase_dwdm_1530_33 = 243

    	DWDM with 1530.33nm optics

    .. data:: ethernet_100gbase_dwdm_tunable = 244

    	DWDM with tunable optics

    .. data:: ethernet_40gbase_kr4 = 245

    	4 lane copper (backplane)

    .. data:: ethernet_40gbase_cr4 = 246

    	4 lane copper (very short reach)

    .. data:: ethernet_40gbase_sr4 = 247

    	fiber over 4 lane optics (short reach)

    .. data:: ethernet_40gbase_fr = 248

    	serial fiber (2+ km)

    .. data:: ethernet_100gbase_cr10 = 249

    	10 lane copper (very short reach)

    .. data:: ethernet_100gbase_sr10 = 250

    	MMF fiber over 10 lane optics (short reach)

    .. data:: ethernet_40gbase_csr4 = 251

    	fiber over 4 lane optics (extended short reach)

    .. data:: ethernet_10gbase_cwdm = 252

    	CWDM optics

    .. data:: ethernet_10gbase_cwdm_tunable = 253

    	CWDM with tunable optics

    .. data:: ethernet_10gbase_cwdm_1470 = 254

    	CWDM with 1470nm optics

    .. data:: ethernet_10gbase_cwdm_1490 = 255

    	CWDM with 1490nm optics

    .. data:: ethernet_10gbase_cwdm_1510 = 256

    	CWDM with 1510nm optics

    .. data:: ethernet_10gbase_cwdm_1530 = 257

    	CWDM with 1530nm optics

    .. data:: ethernet_10gbase_cwdm_1550 = 258

    	CWDM with 1550nm optics

    .. data:: ethernet_10gbase_cwdm_1570 = 259

    	CWDM with 1570nm optics

    .. data:: ethernet_10gbase_cwdm_1590 = 260

    	CWDM with 1590nm optics

    .. data:: ethernet_10gbase_cwdm_1610 = 261

    	CWDM with 1610nm optics

    .. data:: ethernet_40gbase_cwdm = 262

    	CWDM optics

    .. data:: ethernet_40gbase_cwdm_tunable = 263

    	CWDM with tunable optics

    .. data:: ethernet_40gbase_cwdm_1470 = 264

    	CWDM with 1470nm optics

    .. data:: ethernet_40gbase_cwdm_1490 = 265

    	CWDM with 1490nm optics

    .. data:: ethernet_40gbase_cwdm_1510 = 266

    	CWDM with 1510nm optics

    .. data:: ethernet_40gbase_cwdm_1530 = 267

    	CWDM with 1530nm optics

    .. data:: ethernet_40gbase_cwdm_1550 = 268

    	CWDM with 1550nm optics

    .. data:: ethernet_40gbase_cwdm_1570 = 269

    	CWDM with 1570nm optics

    .. data:: ethernet_40gbase_cwdm_1590 = 270

    	CWDM with 1590nm optics

    .. data:: ethernet_40gbase_cwdm_1610 = 271

    	CWDM with 1610nm optics

    .. data:: ethernet_100gbase_cwdm = 272

    	CWDM optics

    .. data:: ethernet_100gbase_cwdm_tunable = 273

    	CWDM with tunable optics

    .. data:: ethernet_100gbase_cwdm_1470 = 274

    	CWDM with 1470nm optics

    .. data:: ethernet_100gbase_cwdm_1490 = 275

    	CWDM with 1490nm optics

    .. data:: ethernet_100gbase_cwdm_1510 = 276

    	CWDM with 1510nm optics

    .. data:: ethernet_100gbase_cwdm_1530 = 277

    	CWDM with 1530nm optics

    .. data:: ethernet_100gbase_cwdm_1550 = 278

    	CWDM with 1550nm optics

    .. data:: ethernet_100gbase_cwdm_1570 = 279

    	CWDM with 1570nm optics

    .. data:: ethernet_100gbase_cwdm_1590 = 280

    	CWDM with 1590nm optics

    .. data:: ethernet_100gbase_cwdm_1610 = 281

    	CWDM with 1610nm optics

    .. data:: ethernet_40gbase_elpb = 282

    	Electrical loopback

    .. data:: ethernet_100gbase_elpb = 283

    	Electrical loopback

    .. data:: ethernet_100gbase_lr10 = 284

    	Fiber over 10 lane optics (long reach)

    .. data:: ethernet_40gbase = 285

    	Four-pair Category 8 STP

    .. data:: ethernet_100gbase_kp4 = 286

    	4 lane copper (backplane)

    .. data:: ethernet_100gbase_kr4 = 287

    	Improved 4 lane copper (backplane)

    .. data:: ethernet_10gbase_lrm = 288

    	Multimode fiber with 1310nm optics (long reach)

    .. data:: ethernet_10gbase_cx4 = 289

    	4 lane X copper

    .. data:: ethernet_10gbase = 290

    	Four-pair Category 6+ UTP

    .. data:: ethernet_10gbase_kx4 = 291

    	4 lane X copper (backplane)

    .. data:: ethernet_10gbase_kr = 292

    	Copper (backplane)

    .. data:: ethernet_10gbase_pr = 293

    	Passive optical network

    .. data:: ethernet_100base_lx = 294

    	X fiber over 4 lane 1310nm optics

    .. data:: ethernet_100base_zx = 295

    	Single-mode fiber over 1550nm optics (Cisco)

    .. data:: ethernet_1000base_bx_d = 296

    	X fibre (D)

    .. data:: ethernet_1000base_bx_u = 297

    	X fibre (U)

    .. data:: ethernet_1000base_bx20_d = 298

    	X fibre (D, 20km)

    .. data:: ethernet_1000base_bx20_u = 299

    	X fibre (U, 20km)

    .. data:: ethernet_1000base_bx40_d = 300

    	X fibre (D, 40km)

    .. data:: ethernet_1000base_bx40_da = 301

    	X fibre (D, 40km)

    .. data:: ethernet_1000base_bx40_u = 302

    	X fibre (U, 40km)

    .. data:: ethernet_1000base_bx80_d = 303

    	X fibre (D, 80km)

    .. data:: ethernet_1000base_bx80_u = 304

    	X fibre (U, 80km)

    .. data:: ethernet_1000base_bx120_d = 305

    	X fibre (D, 120km)

    .. data:: ethernet_1000base_bx120_u = 306

    	X fibre (U, 120km)

    .. data:: ethernet_10gbase_bx_d = 307

    	X fibre (D)

    .. data:: ethernet_10gbase_bx_u = 308

    	X fibre (U)

    .. data:: ethernet_10gbase_bx10_d = 309

    	X fibre (D, 10km)

    .. data:: ethernet_10gbase_bx10_u = 310

    	X fibre (U, 10km)

    .. data:: ethernet_10gbase_bx20_d = 311

    	X fibre (D, 20km)

    .. data:: ethernet_10gbase_bx20_u = 312

    	X fibre (U, 20km)

    .. data:: ethernet_10gbase_bx40_d = 313

    	X fibre (D, 40km)

    .. data:: ethernet_10gbase_bx40_u = 314

    	X fibre (U, 40km)

    .. data:: ethernet_10gbase_bx80_d = 315

    	X fibre (D, 80km)

    .. data:: ethernet_10gbase_bx80_u = 316

    	X fibre (U, 80km)

    .. data:: ethernet_10gbase_bx120_d = 317

    	X fibre (D, 120km)

    .. data:: ethernet_10gbase_bx120_u = 318

    	X fibre (U, 120km)

    .. data:: ethernet_1000base_dr_lx = 319

    	X fiber over long-wl laser PMD, duplexity

    	unknown, dual rate

    .. data:: ethernet_100gbase_er4l = 320

    	fiber over 4 lane optics (25km reach) (lite)

    .. data:: ethernet_100gbase_sr4 = 321

    	fiber over 4 lane optics (short reach)

    .. data:: ethernet_40gbase_sr_bd = 322

    	Bi-directional fiber over 2 lane optics (short

    	reach)

    .. data:: ethernet_25gbase_cr = 323

    	Twinaxial copper cabling

    .. data:: ethernet_25gbase_cr_s = 324

    	Twinaxial copper cabling (no RS-FEC)

    .. data:: ethernet_25gbase_kr = 325

    	One lane electrical backplane

    .. data:: ethernet_25gbase_kr_s = 326

    	One lane electrical backplane (no RS-FEC)

    .. data:: ethernet_25gbase_r = 327

    	One lane fiber

    .. data:: ethernet_25gbase_sr = 328

    	Multimode fiber

    .. data:: ethernet_25gbase_dwdm = 329

    	DWDM optics

    .. data:: ethernet_25gbase_dwdm_tunable = 330

    	DWDM with tunable optics

    .. data:: ethernet_25gbase_cwdm = 331

    	CWDM optics

    .. data:: ethernet_25gbase_cwdm_tunable = 332

    	CWDM with tunable optics

    .. data:: ethernet_100gbase_psm4 = 333

    	4 parallel single mode fibers

    .. data:: ethernet_100gbase_er10 = 334

    	Fiber over 10 lane optics (extended reach)

    .. data:: ethernet_100gbase_er10l = 335

    	Fiber over 10 lane optics (extended reach)

    	(lite)

    .. data:: ethernet_100gbase_acc = 336

    	Active copper cable

    .. data:: ethernet_100gbase_aoc = 337

    	Active optical cable

    .. data:: ethernet_100gbase_cwdm4 = 338

    	4 lane CWDM cable

    .. data:: ethernet_40gbase_psm4 = 339

    	4 parallel single mode fibers

    .. data:: ethernet_100gbase_cr4 = 340

    	4 lane copper (very short reach)

    .. data:: ethernet_100gbase_act_loop = 341

    	Active loopback

    .. data:: ethernet_100gbase_pas_loop = 342

    	Passive loopback

    .. data:: ethernet_base_max = 343

    	ethernet base max

    """

    ethernet_other = Enum.YLeaf(0, "ethernet-other")

    ethernet_unknown = Enum.YLeaf(1, "ethernet-unknown")

    ethernet_aui = Enum.YLeaf(2, "ethernet-aui")

    ethernet_10base5 = Enum.YLeaf(3, "ethernet-10base5")

    ethernet_foirl = Enum.YLeaf(4, "ethernet-foirl")

    ethernet_10base2 = Enum.YLeaf(5, "ethernet-10base2")

    ethernet_10broad36 = Enum.YLeaf(6, "ethernet-10broad36")

    ethernet_10base = Enum.YLeaf(7, "ethernet-10base")

    ethernet_10base_thd = Enum.YLeaf(8, "ethernet-10base-thd")

    ethernet_10base_tfd = Enum.YLeaf(9, "ethernet-10base-tfd")

    ethernet_10base_fp = Enum.YLeaf(10, "ethernet-10base-fp")

    ethernet_10base_fb = Enum.YLeaf(11, "ethernet-10base-fb")

    ethernet_10base_fl = Enum.YLeaf(12, "ethernet-10base-fl")

    ethernet_10base_flhd = Enum.YLeaf(13, "ethernet-10base-flhd")

    ethernet_10base_flfd = Enum.YLeaf(14, "ethernet-10base-flfd")

    ethernet_100base_t4 = Enum.YLeaf(15, "ethernet-100base-t4")

    ethernet_100base_tx = Enum.YLeaf(16, "ethernet-100base-tx")

    ethernet_100base_txhd = Enum.YLeaf(17, "ethernet-100base-txhd")

    ethernet_100base_txfd = Enum.YLeaf(18, "ethernet-100base-txfd")

    ethernet_100base_fx = Enum.YLeaf(19, "ethernet-100base-fx")

    ethernet_100base_fxhd = Enum.YLeaf(20, "ethernet-100base-fxhd")

    ethernet_100base_fxfd = Enum.YLeaf(21, "ethernet-100base-fxfd")

    ethernet_100base_ex = Enum.YLeaf(22, "ethernet-100base-ex")

    ethernet_100base_exhd = Enum.YLeaf(23, "ethernet-100base-exhd")

    ethernet_100base_exfd = Enum.YLeaf(24, "ethernet-100base-exfd")

    ethernet_100base_t2 = Enum.YLeaf(25, "ethernet-100base-t2")

    ethernet_100base_t2hd = Enum.YLeaf(26, "ethernet-100base-t2hd")

    ethernet_100base_t2fd = Enum.YLeaf(27, "ethernet-100base-t2fd")

    ethernet_1000base_x = Enum.YLeaf(28, "ethernet-1000base-x")

    ethernet_1000base_xhd = Enum.YLeaf(29, "ethernet-1000base-xhd")

    ethernet_1000base_xfd = Enum.YLeaf(30, "ethernet-1000base-xfd")

    ethernet_1000base_lx = Enum.YLeaf(31, "ethernet-1000base-lx")

    ethernet_1000base_lxhd = Enum.YLeaf(32, "ethernet-1000base-lxhd")

    ethernet_1000base_lxfd = Enum.YLeaf(33, "ethernet-1000base-lxfd")

    ethernet_1000base_sx = Enum.YLeaf(34, "ethernet-1000base-sx")

    ethernet_1000base_sxhd = Enum.YLeaf(35, "ethernet-1000base-sxhd")

    ethernet_1000base_sxfd = Enum.YLeaf(36, "ethernet-1000base-sxfd")

    ethernet_1000base_cx = Enum.YLeaf(37, "ethernet-1000base-cx")

    ethernet_1000base_cxhd = Enum.YLeaf(38, "ethernet-1000base-cxhd")

    ethernet_1000base_cxfd = Enum.YLeaf(39, "ethernet-1000base-cxfd")

    ethernet_1000base = Enum.YLeaf(40, "ethernet-1000base")

    ethernet_1000base_thd = Enum.YLeaf(41, "ethernet-1000base-thd")

    ethernet_1000base_tfd = Enum.YLeaf(42, "ethernet-1000base-tfd")

    ethernet_10gbase_x = Enum.YLeaf(43, "ethernet-10gbase-x")

    ethernet_10gbase_lx4 = Enum.YLeaf(44, "ethernet-10gbase-lx4")

    ethernet_10gbase_r = Enum.YLeaf(45, "ethernet-10gbase-r")

    ethernet_10gbase_er = Enum.YLeaf(46, "ethernet-10gbase-er")

    ethernet_10gbase_lr = Enum.YLeaf(47, "ethernet-10gbase-lr")

    ethernet_10gbase_sr = Enum.YLeaf(48, "ethernet-10gbase-sr")

    ethernet_10gbase_w = Enum.YLeaf(49, "ethernet-10gbase-w")

    ethernet_10gbase_ew = Enum.YLeaf(50, "ethernet-10gbase-ew")

    ethernet_10gbase_lw = Enum.YLeaf(51, "ethernet-10gbase-lw")

    ethernet_10gbase_sw = Enum.YLeaf(52, "ethernet-10gbase-sw")

    ethernet_1000base_zx = Enum.YLeaf(53, "ethernet-1000base-zx")

    ethernet_1000base_cwdm = Enum.YLeaf(54, "ethernet-1000base-cwdm")

    ethernet_1000base_cwdm_1470 = Enum.YLeaf(55, "ethernet-1000base-cwdm-1470")

    ethernet_1000base_cwdm_1490 = Enum.YLeaf(56, "ethernet-1000base-cwdm-1490")

    ethernet_1000base_cwdm_1510 = Enum.YLeaf(57, "ethernet-1000base-cwdm-1510")

    ethernet_1000base_cwdm_1530 = Enum.YLeaf(58, "ethernet-1000base-cwdm-1530")

    ethernet_1000base_cwdm_1550 = Enum.YLeaf(59, "ethernet-1000base-cwdm-1550")

    ethernet_1000base_cwdm_1570 = Enum.YLeaf(60, "ethernet-1000base-cwdm-1570")

    ethernet_1000base_cwdm_1590 = Enum.YLeaf(61, "ethernet-1000base-cwdm-1590")

    ethernet_1000base_cwdm_1610 = Enum.YLeaf(62, "ethernet-1000base-cwdm-1610")

    ethernet_10gbase_zr = Enum.YLeaf(63, "ethernet-10gbase-zr")

    ethernet_10gbase_dwdm = Enum.YLeaf(64, "ethernet-10gbase-dwdm")

    ethernet_100gbase_lr4 = Enum.YLeaf(65, "ethernet-100gbase-lr4")

    ethernet_1000base_dwdm = Enum.YLeaf(66, "ethernet-1000base-dwdm")

    ethernet_1000base_dwdm_1533 = Enum.YLeaf(67, "ethernet-1000base-dwdm-1533")

    ethernet_1000base_dwdm_1537 = Enum.YLeaf(68, "ethernet-1000base-dwdm-1537")

    ethernet_1000base_dwdm_1541 = Enum.YLeaf(69, "ethernet-1000base-dwdm-1541")

    ethernet_1000base_dwdm_1545 = Enum.YLeaf(70, "ethernet-1000base-dwdm-1545")

    ethernet_1000base_dwdm_1549 = Enum.YLeaf(71, "ethernet-1000base-dwdm-1549")

    ethernet_1000base_dwdm_1553 = Enum.YLeaf(72, "ethernet-1000base-dwdm-1553")

    ethernet_1000base_dwdm_1557 = Enum.YLeaf(73, "ethernet-1000base-dwdm-1557")

    ethernet_1000base_dwdm_1561 = Enum.YLeaf(74, "ethernet-1000base-dwdm-1561")

    ethernet_40gbase_lr4 = Enum.YLeaf(75, "ethernet-40gbase-lr4")

    ethernet_40gbase_er4 = Enum.YLeaf(76, "ethernet-40gbase-er4")

    ethernet_100gbase_er4 = Enum.YLeaf(77, "ethernet-100gbase-er4")

    ethernet_1000base_ex = Enum.YLeaf(78, "ethernet-1000base-ex")

    ethernet_1000base_bx10_d = Enum.YLeaf(79, "ethernet-1000base-bx10-d")

    ethernet_1000base_bx10_u = Enum.YLeaf(80, "ethernet-1000base-bx10-u")

    ethernet_1000base_dwdm_1561_42 = Enum.YLeaf(81, "ethernet-1000base-dwdm-1561-42")

    ethernet_1000base_dwdm_1560_61 = Enum.YLeaf(82, "ethernet-1000base-dwdm-1560-61")

    ethernet_1000base_dwdm_1559_79 = Enum.YLeaf(83, "ethernet-1000base-dwdm-1559-79")

    ethernet_1000base_dwdm_1558_98 = Enum.YLeaf(84, "ethernet-1000base-dwdm-1558-98")

    ethernet_1000base_dwdm_1558_17 = Enum.YLeaf(85, "ethernet-1000base-dwdm-1558-17")

    ethernet_1000base_dwdm_1557_36 = Enum.YLeaf(86, "ethernet-1000base-dwdm-1557-36")

    ethernet_1000base_dwdm_1556_55 = Enum.YLeaf(87, "ethernet-1000base-dwdm-1556-55")

    ethernet_1000base_dwdm_1555_75 = Enum.YLeaf(88, "ethernet-1000base-dwdm-1555-75")

    ethernet_1000base_dwdm_1554_94 = Enum.YLeaf(89, "ethernet-1000base-dwdm-1554-94")

    ethernet_1000base_dwdm_1554_13 = Enum.YLeaf(90, "ethernet-1000base-dwdm-1554-13")

    ethernet_1000base_dwdm_1553_33 = Enum.YLeaf(91, "ethernet-1000base-dwdm-1553-33")

    ethernet_1000base_dwdm_1552_52 = Enum.YLeaf(92, "ethernet-1000base-dwdm-1552-52")

    ethernet_1000base_dwdm_1551_72 = Enum.YLeaf(93, "ethernet-1000base-dwdm-1551-72")

    ethernet_1000base_dwdm_1550_92 = Enum.YLeaf(94, "ethernet-1000base-dwdm-1550-92")

    ethernet_1000base_dwdm_1550_12 = Enum.YLeaf(95, "ethernet-1000base-dwdm-1550-12")

    ethernet_1000base_dwdm_1549_32 = Enum.YLeaf(96, "ethernet-1000base-dwdm-1549-32")

    ethernet_1000base_dwdm_1548_51 = Enum.YLeaf(97, "ethernet-1000base-dwdm-1548-51")

    ethernet_1000base_dwdm_1547_72 = Enum.YLeaf(98, "ethernet-1000base-dwdm-1547-72")

    ethernet_1000base_dwdm_1546_92 = Enum.YLeaf(99, "ethernet-1000base-dwdm-1546-92")

    ethernet_1000base_dwdm_1546_12 = Enum.YLeaf(100, "ethernet-1000base-dwdm-1546-12")

    ethernet_1000base_dwdm_1545_32 = Enum.YLeaf(101, "ethernet-1000base-dwdm-1545-32")

    ethernet_1000base_dwdm_1544_53 = Enum.YLeaf(102, "ethernet-1000base-dwdm-1544-53")

    ethernet_1000base_dwdm_1543_73 = Enum.YLeaf(103, "ethernet-1000base-dwdm-1543-73")

    ethernet_1000base_dwdm_1542_94 = Enum.YLeaf(104, "ethernet-1000base-dwdm-1542-94")

    ethernet_1000base_dwdm_1542_14 = Enum.YLeaf(105, "ethernet-1000base-dwdm-1542-14")

    ethernet_1000base_dwdm_1541_35 = Enum.YLeaf(106, "ethernet-1000base-dwdm-1541-35")

    ethernet_1000base_dwdm_1540_56 = Enum.YLeaf(107, "ethernet-1000base-dwdm-1540-56")

    ethernet_1000base_dwdm_1539_77 = Enum.YLeaf(108, "ethernet-1000base-dwdm-1539-77")

    ethernet_1000base_dwdm_1538_98 = Enum.YLeaf(109, "ethernet-1000base-dwdm-1538-98")

    ethernet_1000base_dwdm_1538_19 = Enum.YLeaf(110, "ethernet-1000base-dwdm-1538-19")

    ethernet_1000base_dwdm_1537_40 = Enum.YLeaf(111, "ethernet-1000base-dwdm-1537-40")

    ethernet_1000base_dwdm_1536_61 = Enum.YLeaf(112, "ethernet-1000base-dwdm-1536-61")

    ethernet_1000base_dwdm_1535_82 = Enum.YLeaf(113, "ethernet-1000base-dwdm-1535-82")

    ethernet_1000base_dwdm_1535_04 = Enum.YLeaf(114, "ethernet-1000base-dwdm-1535-04")

    ethernet_1000base_dwdm_1534_25 = Enum.YLeaf(115, "ethernet-1000base-dwdm-1534-25")

    ethernet_1000base_dwdm_1533_47 = Enum.YLeaf(116, "ethernet-1000base-dwdm-1533-47")

    ethernet_1000base_dwdm_1532_68 = Enum.YLeaf(117, "ethernet-1000base-dwdm-1532-68")

    ethernet_1000base_dwdm_1531_90 = Enum.YLeaf(118, "ethernet-1000base-dwdm-1531-90")

    ethernet_1000base_dwdm_1531_12 = Enum.YLeaf(119, "ethernet-1000base-dwdm-1531-12")

    ethernet_1000base_dwdm_1530_33 = Enum.YLeaf(120, "ethernet-1000base-dwdm-1530-33")

    ethernet_1000base_dwdm_tunable = Enum.YLeaf(121, "ethernet-1000base-dwdm-tunable")

    ethernet_10gbase_dwdm_1561_42 = Enum.YLeaf(122, "ethernet-10gbase-dwdm-1561-42")

    ethernet_10gbase_dwdm_1560_61 = Enum.YLeaf(123, "ethernet-10gbase-dwdm-1560-61")

    ethernet_10gbase_dwdm_1559_79 = Enum.YLeaf(124, "ethernet-10gbase-dwdm-1559-79")

    ethernet_10gbase_dwdm_1558_98 = Enum.YLeaf(125, "ethernet-10gbase-dwdm-1558-98")

    ethernet_10gbase_dwdm_1558_17 = Enum.YLeaf(126, "ethernet-10gbase-dwdm-1558-17")

    ethernet_10gbase_dwdm_1557_36 = Enum.YLeaf(127, "ethernet-10gbase-dwdm-1557-36")

    ethernet_10gbase_dwdm_1556_55 = Enum.YLeaf(128, "ethernet-10gbase-dwdm-1556-55")

    ethernet_10gbase_dwdm_1555_75 = Enum.YLeaf(129, "ethernet-10gbase-dwdm-1555-75")

    ethernet_10gbase_dwdm_1554_94 = Enum.YLeaf(130, "ethernet-10gbase-dwdm-1554-94")

    ethernet_10gbase_dwdm_1554_13 = Enum.YLeaf(131, "ethernet-10gbase-dwdm-1554-13")

    ethernet_10gbase_dwdm_1553_33 = Enum.YLeaf(132, "ethernet-10gbase-dwdm-1553-33")

    ethernet_10gbase_dwdm_1552_52 = Enum.YLeaf(133, "ethernet-10gbase-dwdm-1552-52")

    ethernet_10gbase_dwdm_1551_72 = Enum.YLeaf(134, "ethernet-10gbase-dwdm-1551-72")

    ethernet_10gbase_dwdm_1550_92 = Enum.YLeaf(135, "ethernet-10gbase-dwdm-1550-92")

    ethernet_10gbase_dwdm_1550_12 = Enum.YLeaf(136, "ethernet-10gbase-dwdm-1550-12")

    ethernet_10gbase_dwdm_1549_32 = Enum.YLeaf(137, "ethernet-10gbase-dwdm-1549-32")

    ethernet_10gbase_dwdm_1548_51 = Enum.YLeaf(138, "ethernet-10gbase-dwdm-1548-51")

    ethernet_10gbase_dwdm_1547_72 = Enum.YLeaf(139, "ethernet-10gbase-dwdm-1547-72")

    ethernet_10gbase_dwdm_1546_92 = Enum.YLeaf(140, "ethernet-10gbase-dwdm-1546-92")

    ethernet_10gbase_dwdm_1546_12 = Enum.YLeaf(141, "ethernet-10gbase-dwdm-1546-12")

    ethernet_10gbase_dwdm_1545_32 = Enum.YLeaf(142, "ethernet-10gbase-dwdm-1545-32")

    ethernet_10gbase_dwdm_1544_53 = Enum.YLeaf(143, "ethernet-10gbase-dwdm-1544-53")

    ethernet_10gbase_dwdm_1543_73 = Enum.YLeaf(144, "ethernet-10gbase-dwdm-1543-73")

    ethernet_10gbase_dwdm_1542_94 = Enum.YLeaf(145, "ethernet-10gbase-dwdm-1542-94")

    ethernet_10gbase_dwdm_1542_14 = Enum.YLeaf(146, "ethernet-10gbase-dwdm-1542-14")

    ethernet_10gbase_dwdm_1541_35 = Enum.YLeaf(147, "ethernet-10gbase-dwdm-1541-35")

    ethernet_10gbase_dwdm_1540_56 = Enum.YLeaf(148, "ethernet-10gbase-dwdm-1540-56")

    ethernet_10gbase_dwdm_1539_77 = Enum.YLeaf(149, "ethernet-10gbase-dwdm-1539-77")

    ethernet_10gbase_dwdm_1538_98 = Enum.YLeaf(150, "ethernet-10gbase-dwdm-1538-98")

    ethernet_10gbase_dwdm_1538_19 = Enum.YLeaf(151, "ethernet-10gbase-dwdm-1538-19")

    ethernet_10gbase_dwdm_1537_40 = Enum.YLeaf(152, "ethernet-10gbase-dwdm-1537-40")

    ethernet_10gbase_dwdm_1536_61 = Enum.YLeaf(153, "ethernet-10gbase-dwdm-1536-61")

    ethernet_10gbase_dwdm_1535_82 = Enum.YLeaf(154, "ethernet-10gbase-dwdm-1535-82")

    ethernet_10gbase_dwdm_1535_04 = Enum.YLeaf(155, "ethernet-10gbase-dwdm-1535-04")

    ethernet_10gbase_dwdm_1534_25 = Enum.YLeaf(156, "ethernet-10gbase-dwdm-1534-25")

    ethernet_10gbase_dwdm_1533_47 = Enum.YLeaf(157, "ethernet-10gbase-dwdm-1533-47")

    ethernet_10gbase_dwdm_1532_68 = Enum.YLeaf(158, "ethernet-10gbase-dwdm-1532-68")

    ethernet_10gbase_dwdm_1531_90 = Enum.YLeaf(159, "ethernet-10gbase-dwdm-1531-90")

    ethernet_10gbase_dwdm_1531_12 = Enum.YLeaf(160, "ethernet-10gbase-dwdm-1531-12")

    ethernet_10gbase_dwdm_1530_33 = Enum.YLeaf(161, "ethernet-10gbase-dwdm-1530-33")

    ethernet_10gbase_dwdm_tunable = Enum.YLeaf(162, "ethernet-10gbase-dwdm-tunable")

    ethernet_40gbase_dwdm_1561_42 = Enum.YLeaf(163, "ethernet-40gbase-dwdm-1561-42")

    ethernet_40gbase_dwdm_1560_61 = Enum.YLeaf(164, "ethernet-40gbase-dwdm-1560-61")

    ethernet_40gbase_dwdm_1559_79 = Enum.YLeaf(165, "ethernet-40gbase-dwdm-1559-79")

    ethernet_40gbase_dwdm_1558_98 = Enum.YLeaf(166, "ethernet-40gbase-dwdm-1558-98")

    ethernet_40gbase_dwdm_1558_17 = Enum.YLeaf(167, "ethernet-40gbase-dwdm-1558-17")

    ethernet_40gbase_dwdm_1557_36 = Enum.YLeaf(168, "ethernet-40gbase-dwdm-1557-36")

    ethernet_40gbase_dwdm_1556_55 = Enum.YLeaf(169, "ethernet-40gbase-dwdm-1556-55")

    ethernet_40gbase_dwdm_1555_75 = Enum.YLeaf(170, "ethernet-40gbase-dwdm-1555-75")

    ethernet_40gbase_dwdm_1554_94 = Enum.YLeaf(171, "ethernet-40gbase-dwdm-1554-94")

    ethernet_40gbase_dwdm_1554_13 = Enum.YLeaf(172, "ethernet-40gbase-dwdm-1554-13")

    ethernet_40gbase_dwdm_1553_33 = Enum.YLeaf(173, "ethernet-40gbase-dwdm-1553-33")

    ethernet_40gbase_dwdm_1552_52 = Enum.YLeaf(174, "ethernet-40gbase-dwdm-1552-52")

    ethernet_40gbase_dwdm_1551_72 = Enum.YLeaf(175, "ethernet-40gbase-dwdm-1551-72")

    ethernet_40gbase_dwdm_1550_92 = Enum.YLeaf(176, "ethernet-40gbase-dwdm-1550-92")

    ethernet_40gbase_dwdm_1550_12 = Enum.YLeaf(177, "ethernet-40gbase-dwdm-1550-12")

    ethernet_40gbase_dwdm_1549_32 = Enum.YLeaf(178, "ethernet-40gbase-dwdm-1549-32")

    ethernet_40gbase_dwdm_1548_51 = Enum.YLeaf(179, "ethernet-40gbase-dwdm-1548-51")

    ethernet_40gbase_dwdm_1547_72 = Enum.YLeaf(180, "ethernet-40gbase-dwdm-1547-72")

    ethernet_40gbase_dwdm_1546_92 = Enum.YLeaf(181, "ethernet-40gbase-dwdm-1546-92")

    ethernet_40gbase_dwdm_1546_12 = Enum.YLeaf(182, "ethernet-40gbase-dwdm-1546-12")

    ethernet_40gbase_dwdm_1545_32 = Enum.YLeaf(183, "ethernet-40gbase-dwdm-1545-32")

    ethernet_40gbase_dwdm_1544_53 = Enum.YLeaf(184, "ethernet-40gbase-dwdm-1544-53")

    ethernet_40gbase_dwdm_1543_73 = Enum.YLeaf(185, "ethernet-40gbase-dwdm-1543-73")

    ethernet_40gbase_dwdm_1542_94 = Enum.YLeaf(186, "ethernet-40gbase-dwdm-1542-94")

    ethernet_40gbase_dwdm_1542_14 = Enum.YLeaf(187, "ethernet-40gbase-dwdm-1542-14")

    ethernet_40gbase_dwdm_1541_35 = Enum.YLeaf(188, "ethernet-40gbase-dwdm-1541-35")

    ethernet_40gbase_dwdm_1540_56 = Enum.YLeaf(189, "ethernet-40gbase-dwdm-1540-56")

    ethernet_40gbase_dwdm_1539_77 = Enum.YLeaf(190, "ethernet-40gbase-dwdm-1539-77")

    ethernet_40gbase_dwdm_1538_98 = Enum.YLeaf(191, "ethernet-40gbase-dwdm-1538-98")

    ethernet_40gbase_dwdm_1538_19 = Enum.YLeaf(192, "ethernet-40gbase-dwdm-1538-19")

    ethernet_40gbase_dwdm_1537_40 = Enum.YLeaf(193, "ethernet-40gbase-dwdm-1537-40")

    ethernet_40gbase_dwdm_1536_61 = Enum.YLeaf(194, "ethernet-40gbase-dwdm-1536-61")

    ethernet_40gbase_dwdm_1535_82 = Enum.YLeaf(195, "ethernet-40gbase-dwdm-1535-82")

    ethernet_40gbase_dwdm_1535_04 = Enum.YLeaf(196, "ethernet-40gbase-dwdm-1535-04")

    ethernet_40gbase_dwdm_1534_25 = Enum.YLeaf(197, "ethernet-40gbase-dwdm-1534-25")

    ethernet_40gbase_dwdm_1533_47 = Enum.YLeaf(198, "ethernet-40gbase-dwdm-1533-47")

    ethernet_40gbase_dwdm_1532_68 = Enum.YLeaf(199, "ethernet-40gbase-dwdm-1532-68")

    ethernet_40gbase_dwdm_1531_90 = Enum.YLeaf(200, "ethernet-40gbase-dwdm-1531-90")

    ethernet_40gbase_dwdm_1531_12 = Enum.YLeaf(201, "ethernet-40gbase-dwdm-1531-12")

    ethernet_40gbase_dwdm_1530_33 = Enum.YLeaf(202, "ethernet-40gbase-dwdm-1530-33")

    ethernet_40gbase_dwdm_tunable = Enum.YLeaf(203, "ethernet-40gbase-dwdm-tunable")

    ethernet_100gbase_dwdm_1561_42 = Enum.YLeaf(204, "ethernet-100gbase-dwdm-1561-42")

    ethernet_100gbase_dwdm_1560_61 = Enum.YLeaf(205, "ethernet-100gbase-dwdm-1560-61")

    ethernet_100gbase_dwdm_1559_79 = Enum.YLeaf(206, "ethernet-100gbase-dwdm-1559-79")

    ethernet_100gbase_dwdm_1558_98 = Enum.YLeaf(207, "ethernet-100gbase-dwdm-1558-98")

    ethernet_100gbase_dwdm_1558_17 = Enum.YLeaf(208, "ethernet-100gbase-dwdm-1558-17")

    ethernet_100gbase_dwdm_1557_36 = Enum.YLeaf(209, "ethernet-100gbase-dwdm-1557-36")

    ethernet_100gbase_dwdm_1556_55 = Enum.YLeaf(210, "ethernet-100gbase-dwdm-1556-55")

    ethernet_100gbase_dwdm_1555_75 = Enum.YLeaf(211, "ethernet-100gbase-dwdm-1555-75")

    ethernet_100gbase_dwdm_1554_94 = Enum.YLeaf(212, "ethernet-100gbase-dwdm-1554-94")

    ethernet_100gbase_dwdm_1554_13 = Enum.YLeaf(213, "ethernet-100gbase-dwdm-1554-13")

    ethernet_100gbase_dwdm_1553_33 = Enum.YLeaf(214, "ethernet-100gbase-dwdm-1553-33")

    ethernet_100gbase_dwdm_1552_52 = Enum.YLeaf(215, "ethernet-100gbase-dwdm-1552-52")

    ethernet_100gbase_dwdm_1551_72 = Enum.YLeaf(216, "ethernet-100gbase-dwdm-1551-72")

    ethernet_100gbase_dwdm_1550_92 = Enum.YLeaf(217, "ethernet-100gbase-dwdm-1550-92")

    ethernet_100gbase_dwdm_1550_12 = Enum.YLeaf(218, "ethernet-100gbase-dwdm-1550-12")

    ethernet_100gbase_dwdm_1549_32 = Enum.YLeaf(219, "ethernet-100gbase-dwdm-1549-32")

    ethernet_100gbase_dwdm_1548_51 = Enum.YLeaf(220, "ethernet-100gbase-dwdm-1548-51")

    ethernet_100gbase_dwdm_1547_72 = Enum.YLeaf(221, "ethernet-100gbase-dwdm-1547-72")

    ethernet_100gbase_dwdm_1546_92 = Enum.YLeaf(222, "ethernet-100gbase-dwdm-1546-92")

    ethernet_100gbase_dwdm_1546_12 = Enum.YLeaf(223, "ethernet-100gbase-dwdm-1546-12")

    ethernet_100gbase_dwdm_1545_32 = Enum.YLeaf(224, "ethernet-100gbase-dwdm-1545-32")

    ethernet_100gbase_dwdm_1544_53 = Enum.YLeaf(225, "ethernet-100gbase-dwdm-1544-53")

    ethernet_100gbase_dwdm_1543_73 = Enum.YLeaf(226, "ethernet-100gbase-dwdm-1543-73")

    ethernet_100gbase_dwdm_1542_94 = Enum.YLeaf(227, "ethernet-100gbase-dwdm-1542-94")

    ethernet_100gbase_dwdm_1542_14 = Enum.YLeaf(228, "ethernet-100gbase-dwdm-1542-14")

    ethernet_100gbase_dwdm_1541_35 = Enum.YLeaf(229, "ethernet-100gbase-dwdm-1541-35")

    ethernet_100gbase_dwdm_1540_56 = Enum.YLeaf(230, "ethernet-100gbase-dwdm-1540-56")

    ethernet_100gbase_dwdm_1539_77 = Enum.YLeaf(231, "ethernet-100gbase-dwdm-1539-77")

    ethernet_100gbase_dwdm_1538_98 = Enum.YLeaf(232, "ethernet-100gbase-dwdm-1538-98")

    ethernet_100gbase_dwdm_1538_19 = Enum.YLeaf(233, "ethernet-100gbase-dwdm-1538-19")

    ethernet_100gbase_dwdm_1537_40 = Enum.YLeaf(234, "ethernet-100gbase-dwdm-1537-40")

    ethernet_100gbase_dwdm_1536_61 = Enum.YLeaf(235, "ethernet-100gbase-dwdm-1536-61")

    ethernet_100gbase_dwdm_1535_82 = Enum.YLeaf(236, "ethernet-100gbase-dwdm-1535-82")

    ethernet_100gbase_dwdm_1535_04 = Enum.YLeaf(237, "ethernet-100gbase-dwdm-1535-04")

    ethernet_100gbase_dwdm_1534_25 = Enum.YLeaf(238, "ethernet-100gbase-dwdm-1534-25")

    ethernet_100gbase_dwdm_1533_47 = Enum.YLeaf(239, "ethernet-100gbase-dwdm-1533-47")

    ethernet_100gbase_dwdm_1532_68 = Enum.YLeaf(240, "ethernet-100gbase-dwdm-1532-68")

    ethernet_100gbase_dwdm_1531_90 = Enum.YLeaf(241, "ethernet-100gbase-dwdm-1531-90")

    ethernet_100gbase_dwdm_1531_12 = Enum.YLeaf(242, "ethernet-100gbase-dwdm-1531-12")

    ethernet_100gbase_dwdm_1530_33 = Enum.YLeaf(243, "ethernet-100gbase-dwdm-1530-33")

    ethernet_100gbase_dwdm_tunable = Enum.YLeaf(244, "ethernet-100gbase-dwdm-tunable")

    ethernet_40gbase_kr4 = Enum.YLeaf(245, "ethernet-40gbase-kr4")

    ethernet_40gbase_cr4 = Enum.YLeaf(246, "ethernet-40gbase-cr4")

    ethernet_40gbase_sr4 = Enum.YLeaf(247, "ethernet-40gbase-sr4")

    ethernet_40gbase_fr = Enum.YLeaf(248, "ethernet-40gbase-fr")

    ethernet_100gbase_cr10 = Enum.YLeaf(249, "ethernet-100gbase-cr10")

    ethernet_100gbase_sr10 = Enum.YLeaf(250, "ethernet-100gbase-sr10")

    ethernet_40gbase_csr4 = Enum.YLeaf(251, "ethernet-40gbase-csr4")

    ethernet_10gbase_cwdm = Enum.YLeaf(252, "ethernet-10gbase-cwdm")

    ethernet_10gbase_cwdm_tunable = Enum.YLeaf(253, "ethernet-10gbase-cwdm-tunable")

    ethernet_10gbase_cwdm_1470 = Enum.YLeaf(254, "ethernet-10gbase-cwdm-1470")

    ethernet_10gbase_cwdm_1490 = Enum.YLeaf(255, "ethernet-10gbase-cwdm-1490")

    ethernet_10gbase_cwdm_1510 = Enum.YLeaf(256, "ethernet-10gbase-cwdm-1510")

    ethernet_10gbase_cwdm_1530 = Enum.YLeaf(257, "ethernet-10gbase-cwdm-1530")

    ethernet_10gbase_cwdm_1550 = Enum.YLeaf(258, "ethernet-10gbase-cwdm-1550")

    ethernet_10gbase_cwdm_1570 = Enum.YLeaf(259, "ethernet-10gbase-cwdm-1570")

    ethernet_10gbase_cwdm_1590 = Enum.YLeaf(260, "ethernet-10gbase-cwdm-1590")

    ethernet_10gbase_cwdm_1610 = Enum.YLeaf(261, "ethernet-10gbase-cwdm-1610")

    ethernet_40gbase_cwdm = Enum.YLeaf(262, "ethernet-40gbase-cwdm")

    ethernet_40gbase_cwdm_tunable = Enum.YLeaf(263, "ethernet-40gbase-cwdm-tunable")

    ethernet_40gbase_cwdm_1470 = Enum.YLeaf(264, "ethernet-40gbase-cwdm-1470")

    ethernet_40gbase_cwdm_1490 = Enum.YLeaf(265, "ethernet-40gbase-cwdm-1490")

    ethernet_40gbase_cwdm_1510 = Enum.YLeaf(266, "ethernet-40gbase-cwdm-1510")

    ethernet_40gbase_cwdm_1530 = Enum.YLeaf(267, "ethernet-40gbase-cwdm-1530")

    ethernet_40gbase_cwdm_1550 = Enum.YLeaf(268, "ethernet-40gbase-cwdm-1550")

    ethernet_40gbase_cwdm_1570 = Enum.YLeaf(269, "ethernet-40gbase-cwdm-1570")

    ethernet_40gbase_cwdm_1590 = Enum.YLeaf(270, "ethernet-40gbase-cwdm-1590")

    ethernet_40gbase_cwdm_1610 = Enum.YLeaf(271, "ethernet-40gbase-cwdm-1610")

    ethernet_100gbase_cwdm = Enum.YLeaf(272, "ethernet-100gbase-cwdm")

    ethernet_100gbase_cwdm_tunable = Enum.YLeaf(273, "ethernet-100gbase-cwdm-tunable")

    ethernet_100gbase_cwdm_1470 = Enum.YLeaf(274, "ethernet-100gbase-cwdm-1470")

    ethernet_100gbase_cwdm_1490 = Enum.YLeaf(275, "ethernet-100gbase-cwdm-1490")

    ethernet_100gbase_cwdm_1510 = Enum.YLeaf(276, "ethernet-100gbase-cwdm-1510")

    ethernet_100gbase_cwdm_1530 = Enum.YLeaf(277, "ethernet-100gbase-cwdm-1530")

    ethernet_100gbase_cwdm_1550 = Enum.YLeaf(278, "ethernet-100gbase-cwdm-1550")

    ethernet_100gbase_cwdm_1570 = Enum.YLeaf(279, "ethernet-100gbase-cwdm-1570")

    ethernet_100gbase_cwdm_1590 = Enum.YLeaf(280, "ethernet-100gbase-cwdm-1590")

    ethernet_100gbase_cwdm_1610 = Enum.YLeaf(281, "ethernet-100gbase-cwdm-1610")

    ethernet_40gbase_elpb = Enum.YLeaf(282, "ethernet-40gbase-elpb")

    ethernet_100gbase_elpb = Enum.YLeaf(283, "ethernet-100gbase-elpb")

    ethernet_100gbase_lr10 = Enum.YLeaf(284, "ethernet-100gbase-lr10")

    ethernet_40gbase = Enum.YLeaf(285, "ethernet-40gbase")

    ethernet_100gbase_kp4 = Enum.YLeaf(286, "ethernet-100gbase-kp4")

    ethernet_100gbase_kr4 = Enum.YLeaf(287, "ethernet-100gbase-kr4")

    ethernet_10gbase_lrm = Enum.YLeaf(288, "ethernet-10gbase-lrm")

    ethernet_10gbase_cx4 = Enum.YLeaf(289, "ethernet-10gbase-cx4")

    ethernet_10gbase = Enum.YLeaf(290, "ethernet-10gbase")

    ethernet_10gbase_kx4 = Enum.YLeaf(291, "ethernet-10gbase-kx4")

    ethernet_10gbase_kr = Enum.YLeaf(292, "ethernet-10gbase-kr")

    ethernet_10gbase_pr = Enum.YLeaf(293, "ethernet-10gbase-pr")

    ethernet_100base_lx = Enum.YLeaf(294, "ethernet-100base-lx")

    ethernet_100base_zx = Enum.YLeaf(295, "ethernet-100base-zx")

    ethernet_1000base_bx_d = Enum.YLeaf(296, "ethernet-1000base-bx-d")

    ethernet_1000base_bx_u = Enum.YLeaf(297, "ethernet-1000base-bx-u")

    ethernet_1000base_bx20_d = Enum.YLeaf(298, "ethernet-1000base-bx20-d")

    ethernet_1000base_bx20_u = Enum.YLeaf(299, "ethernet-1000base-bx20-u")

    ethernet_1000base_bx40_d = Enum.YLeaf(300, "ethernet-1000base-bx40-d")

    ethernet_1000base_bx40_da = Enum.YLeaf(301, "ethernet-1000base-bx40-da")

    ethernet_1000base_bx40_u = Enum.YLeaf(302, "ethernet-1000base-bx40-u")

    ethernet_1000base_bx80_d = Enum.YLeaf(303, "ethernet-1000base-bx80-d")

    ethernet_1000base_bx80_u = Enum.YLeaf(304, "ethernet-1000base-bx80-u")

    ethernet_1000base_bx120_d = Enum.YLeaf(305, "ethernet-1000base-bx120-d")

    ethernet_1000base_bx120_u = Enum.YLeaf(306, "ethernet-1000base-bx120-u")

    ethernet_10gbase_bx_d = Enum.YLeaf(307, "ethernet-10gbase-bx-d")

    ethernet_10gbase_bx_u = Enum.YLeaf(308, "ethernet-10gbase-bx-u")

    ethernet_10gbase_bx10_d = Enum.YLeaf(309, "ethernet-10gbase-bx10-d")

    ethernet_10gbase_bx10_u = Enum.YLeaf(310, "ethernet-10gbase-bx10-u")

    ethernet_10gbase_bx20_d = Enum.YLeaf(311, "ethernet-10gbase-bx20-d")

    ethernet_10gbase_bx20_u = Enum.YLeaf(312, "ethernet-10gbase-bx20-u")

    ethernet_10gbase_bx40_d = Enum.YLeaf(313, "ethernet-10gbase-bx40-d")

    ethernet_10gbase_bx40_u = Enum.YLeaf(314, "ethernet-10gbase-bx40-u")

    ethernet_10gbase_bx80_d = Enum.YLeaf(315, "ethernet-10gbase-bx80-d")

    ethernet_10gbase_bx80_u = Enum.YLeaf(316, "ethernet-10gbase-bx80-u")

    ethernet_10gbase_bx120_d = Enum.YLeaf(317, "ethernet-10gbase-bx120-d")

    ethernet_10gbase_bx120_u = Enum.YLeaf(318, "ethernet-10gbase-bx120-u")

    ethernet_1000base_dr_lx = Enum.YLeaf(319, "ethernet-1000base-dr-lx")

    ethernet_100gbase_er4l = Enum.YLeaf(320, "ethernet-100gbase-er4l")

    ethernet_100gbase_sr4 = Enum.YLeaf(321, "ethernet-100gbase-sr4")

    ethernet_40gbase_sr_bd = Enum.YLeaf(322, "ethernet-40gbase-sr-bd")

    ethernet_25gbase_cr = Enum.YLeaf(323, "ethernet-25gbase-cr")

    ethernet_25gbase_cr_s = Enum.YLeaf(324, "ethernet-25gbase-cr-s")

    ethernet_25gbase_kr = Enum.YLeaf(325, "ethernet-25gbase-kr")

    ethernet_25gbase_kr_s = Enum.YLeaf(326, "ethernet-25gbase-kr-s")

    ethernet_25gbase_r = Enum.YLeaf(327, "ethernet-25gbase-r")

    ethernet_25gbase_sr = Enum.YLeaf(328, "ethernet-25gbase-sr")

    ethernet_25gbase_dwdm = Enum.YLeaf(329, "ethernet-25gbase-dwdm")

    ethernet_25gbase_dwdm_tunable = Enum.YLeaf(330, "ethernet-25gbase-dwdm-tunable")

    ethernet_25gbase_cwdm = Enum.YLeaf(331, "ethernet-25gbase-cwdm")

    ethernet_25gbase_cwdm_tunable = Enum.YLeaf(332, "ethernet-25gbase-cwdm-tunable")

    ethernet_100gbase_psm4 = Enum.YLeaf(333, "ethernet-100gbase-psm4")

    ethernet_100gbase_er10 = Enum.YLeaf(334, "ethernet-100gbase-er10")

    ethernet_100gbase_er10l = Enum.YLeaf(335, "ethernet-100gbase-er10l")

    ethernet_100gbase_acc = Enum.YLeaf(336, "ethernet-100gbase-acc")

    ethernet_100gbase_aoc = Enum.YLeaf(337, "ethernet-100gbase-aoc")

    ethernet_100gbase_cwdm4 = Enum.YLeaf(338, "ethernet-100gbase-cwdm4")

    ethernet_40gbase_psm4 = Enum.YLeaf(339, "ethernet-40gbase-psm4")

    ethernet_100gbase_cr4 = Enum.YLeaf(340, "ethernet-100gbase-cr4")

    ethernet_100gbase_act_loop = Enum.YLeaf(341, "ethernet-100gbase-act-loop")

    ethernet_100gbase_pas_loop = Enum.YLeaf(342, "ethernet-100gbase-pas-loop")

    ethernet_base_max = Enum.YLeaf(343, "ethernet-base-max")


class EthernetPortEnable(Enum):
    """
    EthernetPortEnable

    Port admin state

    .. data:: disabled = 0

    	Port disabled, both directions

    .. data:: rx_enabled = 1

    	Port enabled rx direction only

    .. data:: tx_enabled = 2

    	Port enabled tx direction only

    .. data:: enabled = 3

    	Port enabled, both directions

    """

    disabled = Enum.YLeaf(0, "disabled")

    rx_enabled = Enum.YLeaf(1, "rx-enabled")

    tx_enabled = Enum.YLeaf(2, "tx-enabled")

    enabled = Enum.YLeaf(3, "enabled")


class EthernetSpeed(Enum):
    """
    EthernetSpeed

    Speed

    .. data:: ethernet_speed_invalid = 0

    	ethernet speed invalid

    .. data:: ten_mbps = 1

    	ten mbps

    .. data:: hundred_mbps = 2

    	hundred mbps

    .. data:: one_gbps = 3

    	one gbps

    .. data:: ten_gbps = 4

    	ten gbps

    .. data:: twenty_five_gbps = 5

    	twenty five gbps

    .. data:: forty_gbps = 6

    	forty gbps

    .. data:: fifty_gbps = 7

    	fifty gbps

    .. data:: hundred_gbps = 8

    	hundred gbps

    .. data:: ethernet_speed_types_count = 9

    	ethernet speed types count

    """

    ethernet_speed_invalid = Enum.YLeaf(0, "ethernet-speed-invalid")

    ten_mbps = Enum.YLeaf(1, "ten-mbps")

    hundred_mbps = Enum.YLeaf(2, "hundred-mbps")

    one_gbps = Enum.YLeaf(3, "one-gbps")

    ten_gbps = Enum.YLeaf(4, "ten-gbps")

    twenty_five_gbps = Enum.YLeaf(5, "twenty-five-gbps")

    forty_gbps = Enum.YLeaf(6, "forty-gbps")

    fifty_gbps = Enum.YLeaf(7, "fifty-gbps")

    hundred_gbps = Enum.YLeaf(8, "hundred-gbps")

    ethernet_speed_types_count = Enum.YLeaf(9, "ethernet-speed-types-count")



class EthernetInterface(Entity):
    """
    Ethernet operational data
    
    .. attribute:: berts
    
    	Ethernet controller BERT table
    	**type**\:   :py:class:`Berts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Berts>`
    
    .. attribute:: interfaces
    
    	Ethernet controller info table
    	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Interfaces>`
    
    .. attribute:: statistics
    
    	Ethernet controller statistics table
    	**type**\:   :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Statistics>`
    
    

    """

    _prefix = 'drivers-media-eth-oper'
    _revision = '2017-04-04'

    def __init__(self):
        super(EthernetInterface, self).__init__()
        self._top_entity = None

        self.yang_name = "ethernet-interface"
        self.yang_parent_name = "Cisco-IOS-XR-drivers-media-eth-oper"

        self.berts = EthernetInterface.Berts()
        self.berts.parent = self
        self._children_name_map["berts"] = "berts"
        self._children_yang_names.add("berts")

        self.interfaces = EthernetInterface.Interfaces()
        self.interfaces.parent = self
        self._children_name_map["interfaces"] = "interfaces"
        self._children_yang_names.add("interfaces")

        self.statistics = EthernetInterface.Statistics()
        self.statistics.parent = self
        self._children_name_map["statistics"] = "statistics"
        self._children_yang_names.add("statistics")


    class Statistics(Entity):
        """
        Ethernet controller statistics table
        
        .. attribute:: statistic
        
        	Ethernet statistics information
        	**type**\: list of    :py:class:`Statistic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Statistics.Statistic>`
        
        

        """

        _prefix = 'drivers-media-eth-oper'
        _revision = '2017-04-04'

        def __init__(self):
            super(EthernetInterface.Statistics, self).__init__()

            self.yang_name = "statistics"
            self.yang_parent_name = "ethernet-interface"

            self.statistic = YList(self)

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
                        super(EthernetInterface.Statistics, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(EthernetInterface.Statistics, self).__setattr__(name, value)


        class Statistic(Entity):
            """
            Ethernet statistics information
            
            .. attribute:: interface_name  <key>
            
            	The name of the interface
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: aborted_packet_drops
            
            	Drops due to packet abort
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: buffer_underrun_packet_drops
            
            	Drops due to buffer underrun
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: dropped_ether_stats_fragments
            
            	Bad Frames < 64 Octet, dropped
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: dropped_ether_stats_undersize_pkts
            
            	Good frames < 64 Octet, dropped
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: dropped_giant_packets_greaterthan_mru
            
            	Good frames > MRU, dropped
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: dropped_jabbers_packets_greaterthan_mru
            
            	Bad Frames > MRU, dropped
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: dropped_miscellaneous_error_packets
            
            	Any other errors not counted
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: dropped_packets_with_crc_align_errors
            
            	Frames 64 \- MRU with CRC error
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ether_stats_collisions
            
            	All collision events
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: invalid_dest_mac_drop_packets
            
            	Drops due to the destination MAC not matching
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: invalid_encap_drop_packets
            
            	Drops due to the encapsulation or ether type not matching
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: miscellaneous_output_errors
            
            	Any other errors not counted
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: number_of_aborted_packets_dropped
            
            	Drops due to packet abort
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: number_of_buffer_overrun_packets_dropped
            
            	Drops due to buffer overrun
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: number_of_miscellaneous_packets_dropped
            
            	Any other drops not counted
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: numberof_invalid_vlan_id_packets_dropped
            
            	Drops due to invalid VLAN id
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: received8021q_frames
            
            	All 802.1Q frames
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: received_broadcast_frames
            
            	Received broadcast Frames
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: received_good_bytes
            
            	Total octets of all good frames
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: received_good_frames
            
            	Received Good Frames
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: received_multicast_frames
            
            	Received multicast Frames
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: received_pause_frames
            
            	All pause frames
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: received_total64_octet_frames
            
            	All 64 Octet Frame Count
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: received_total_bytes
            
            	Total octets of all frames
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: received_total_frames
            
            	All frames, good or bad
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: received_total_octet_frames_from1024_to1518
            
            	All 1024\-1518 Octet Frame Count
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: received_total_octet_frames_from128_to255
            
            	All 128\-255 Octet Frame Count
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: received_total_octet_frames_from1519_to_max
            
            	All > 1518 Octet Frame Count
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: received_total_octet_frames_from256_to511
            
            	All 256\-511 Octet Frame Count
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: received_total_octet_frames_from512_to1023
            
            	All 512\-1023 Octet Frame Count
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: received_total_octet_frames_from65_to127
            
            	All 65\-127 Octet Frame Count
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: received_unicast_frames
            
            	Received unicast Frames
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: received_unknown_opcodes
            
            	Unsupported MAC Control frames
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: rfc2819_ether_stats_crc_align_errors
            
            	RFC2819 etherStatsCRCAlignErrors
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: rfc2819_ether_stats_jabbers
            
            	RFC2819 etherStatsJabbers
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: rfc2819_ether_stats_oversized_pkts
            
            	RFC2819 etherStatsOversizedPkts
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: rfc3635dot3_stats_alignment_errors
            
            	RFC3635 dot3StatsAlignmentErrors
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: symbol_errors
            
            	Symbol errors
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: total_bytes_transmitted
            
            	Total octets of all frames
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: total_frames_transmitted
            
            	All frames, good or bad
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: total_good_bytes_transmitted
            
            	Total octets of all good frames
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: transmitted8021q_frames
            
            	All 802.1Q frames
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: transmitted_broadcast_frames
            
            	Transmitted broadcast Frames
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: transmitted_good_frames
            
            	Transmitted Good Frames
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: transmitted_multicast_frames
            
            	Transmitted multicast Frames
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: transmitted_total64_octet_frames
            
            	All 64 Octet Frame Count
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: transmitted_total_octet_frames_from1024_to1518
            
            	All 1024\-1518 Octet Frame Count
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: transmitted_total_octet_frames_from128_to255
            
            	All 128\-255 Octet Frame Count
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: transmitted_total_octet_frames_from1518_to_max
            
            	All > 1518 Octet Frame Count
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: transmitted_total_octet_frames_from256_to511
            
            	All 256\-511 Octet Frame Count
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: transmitted_total_octet_frames_from512_to1023
            
            	All 512\-1023 Octet Frame Count
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: transmitted_total_octet_frames_from65_to127
            
            	All 65\-127 Octet Frame Count
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: transmitted_total_pause_frames
            
            	All pause frames
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: transmitted_unicast_frames
            
            	Transmitted unicast Frames
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: uncounted_dropped_frames
            
            	Any other drops not counted
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            

            """

            _prefix = 'drivers-media-eth-oper'
            _revision = '2017-04-04'

            def __init__(self):
                super(EthernetInterface.Statistics.Statistic, self).__init__()

                self.yang_name = "statistic"
                self.yang_parent_name = "statistics"

                self.interface_name = YLeaf(YType.str, "interface-name")

                self.aborted_packet_drops = YLeaf(YType.uint64, "aborted-packet-drops")

                self.buffer_underrun_packet_drops = YLeaf(YType.uint64, "buffer-underrun-packet-drops")

                self.dropped_ether_stats_fragments = YLeaf(YType.uint64, "dropped-ether-stats-fragments")

                self.dropped_ether_stats_undersize_pkts = YLeaf(YType.uint64, "dropped-ether-stats-undersize-pkts")

                self.dropped_giant_packets_greaterthan_mru = YLeaf(YType.uint64, "dropped-giant-packets-greaterthan-mru")

                self.dropped_jabbers_packets_greaterthan_mru = YLeaf(YType.uint64, "dropped-jabbers-packets-greaterthan-mru")

                self.dropped_miscellaneous_error_packets = YLeaf(YType.uint64, "dropped-miscellaneous-error-packets")

                self.dropped_packets_with_crc_align_errors = YLeaf(YType.uint64, "dropped-packets-with-crc-align-errors")

                self.ether_stats_collisions = YLeaf(YType.uint64, "ether-stats-collisions")

                self.invalid_dest_mac_drop_packets = YLeaf(YType.uint64, "invalid-dest-mac-drop-packets")

                self.invalid_encap_drop_packets = YLeaf(YType.uint64, "invalid-encap-drop-packets")

                self.miscellaneous_output_errors = YLeaf(YType.uint64, "miscellaneous-output-errors")

                self.number_of_aborted_packets_dropped = YLeaf(YType.uint64, "number-of-aborted-packets-dropped")

                self.number_of_buffer_overrun_packets_dropped = YLeaf(YType.uint64, "number-of-buffer-overrun-packets-dropped")

                self.number_of_miscellaneous_packets_dropped = YLeaf(YType.uint64, "number-of-miscellaneous-packets-dropped")

                self.numberof_invalid_vlan_id_packets_dropped = YLeaf(YType.uint64, "numberof-invalid-vlan-id-packets-dropped")

                self.received8021q_frames = YLeaf(YType.uint64, "received8021q-frames")

                self.received_broadcast_frames = YLeaf(YType.uint64, "received-broadcast-frames")

                self.received_good_bytes = YLeaf(YType.uint64, "received-good-bytes")

                self.received_good_frames = YLeaf(YType.uint64, "received-good-frames")

                self.received_multicast_frames = YLeaf(YType.uint64, "received-multicast-frames")

                self.received_pause_frames = YLeaf(YType.uint64, "received-pause-frames")

                self.received_total64_octet_frames = YLeaf(YType.uint64, "received-total64-octet-frames")

                self.received_total_bytes = YLeaf(YType.uint64, "received-total-bytes")

                self.received_total_frames = YLeaf(YType.uint64, "received-total-frames")

                self.received_total_octet_frames_from1024_to1518 = YLeaf(YType.uint64, "received-total-octet-frames-from1024-to1518")

                self.received_total_octet_frames_from128_to255 = YLeaf(YType.uint64, "received-total-octet-frames-from128-to255")

                self.received_total_octet_frames_from1519_to_max = YLeaf(YType.uint64, "received-total-octet-frames-from1519-to-max")

                self.received_total_octet_frames_from256_to511 = YLeaf(YType.uint64, "received-total-octet-frames-from256-to511")

                self.received_total_octet_frames_from512_to1023 = YLeaf(YType.uint64, "received-total-octet-frames-from512-to1023")

                self.received_total_octet_frames_from65_to127 = YLeaf(YType.uint64, "received-total-octet-frames-from65-to127")

                self.received_unicast_frames = YLeaf(YType.uint64, "received-unicast-frames")

                self.received_unknown_opcodes = YLeaf(YType.uint64, "received-unknown-opcodes")

                self.rfc2819_ether_stats_crc_align_errors = YLeaf(YType.uint64, "rfc2819-ether-stats-crc-align-errors")

                self.rfc2819_ether_stats_jabbers = YLeaf(YType.uint64, "rfc2819-ether-stats-jabbers")

                self.rfc2819_ether_stats_oversized_pkts = YLeaf(YType.uint64, "rfc2819-ether-stats-oversized-pkts")

                self.rfc3635dot3_stats_alignment_errors = YLeaf(YType.uint64, "rfc3635dot3-stats-alignment-errors")

                self.symbol_errors = YLeaf(YType.uint64, "symbol-errors")

                self.total_bytes_transmitted = YLeaf(YType.uint64, "total-bytes-transmitted")

                self.total_frames_transmitted = YLeaf(YType.uint64, "total-frames-transmitted")

                self.total_good_bytes_transmitted = YLeaf(YType.uint64, "total-good-bytes-transmitted")

                self.transmitted8021q_frames = YLeaf(YType.uint64, "transmitted8021q-frames")

                self.transmitted_broadcast_frames = YLeaf(YType.uint64, "transmitted-broadcast-frames")

                self.transmitted_good_frames = YLeaf(YType.uint64, "transmitted-good-frames")

                self.transmitted_multicast_frames = YLeaf(YType.uint64, "transmitted-multicast-frames")

                self.transmitted_total64_octet_frames = YLeaf(YType.uint64, "transmitted-total64-octet-frames")

                self.transmitted_total_octet_frames_from1024_to1518 = YLeaf(YType.uint64, "transmitted-total-octet-frames-from1024-to1518")

                self.transmitted_total_octet_frames_from128_to255 = YLeaf(YType.uint64, "transmitted-total-octet-frames-from128-to255")

                self.transmitted_total_octet_frames_from1518_to_max = YLeaf(YType.uint64, "transmitted-total-octet-frames-from1518-to-max")

                self.transmitted_total_octet_frames_from256_to511 = YLeaf(YType.uint64, "transmitted-total-octet-frames-from256-to511")

                self.transmitted_total_octet_frames_from512_to1023 = YLeaf(YType.uint64, "transmitted-total-octet-frames-from512-to1023")

                self.transmitted_total_octet_frames_from65_to127 = YLeaf(YType.uint64, "transmitted-total-octet-frames-from65-to127")

                self.transmitted_total_pause_frames = YLeaf(YType.uint64, "transmitted-total-pause-frames")

                self.transmitted_unicast_frames = YLeaf(YType.uint64, "transmitted-unicast-frames")

                self.uncounted_dropped_frames = YLeaf(YType.uint64, "uncounted-dropped-frames")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("interface_name",
                                "aborted_packet_drops",
                                "buffer_underrun_packet_drops",
                                "dropped_ether_stats_fragments",
                                "dropped_ether_stats_undersize_pkts",
                                "dropped_giant_packets_greaterthan_mru",
                                "dropped_jabbers_packets_greaterthan_mru",
                                "dropped_miscellaneous_error_packets",
                                "dropped_packets_with_crc_align_errors",
                                "ether_stats_collisions",
                                "invalid_dest_mac_drop_packets",
                                "invalid_encap_drop_packets",
                                "miscellaneous_output_errors",
                                "number_of_aborted_packets_dropped",
                                "number_of_buffer_overrun_packets_dropped",
                                "number_of_miscellaneous_packets_dropped",
                                "numberof_invalid_vlan_id_packets_dropped",
                                "received8021q_frames",
                                "received_broadcast_frames",
                                "received_good_bytes",
                                "received_good_frames",
                                "received_multicast_frames",
                                "received_pause_frames",
                                "received_total64_octet_frames",
                                "received_total_bytes",
                                "received_total_frames",
                                "received_total_octet_frames_from1024_to1518",
                                "received_total_octet_frames_from128_to255",
                                "received_total_octet_frames_from1519_to_max",
                                "received_total_octet_frames_from256_to511",
                                "received_total_octet_frames_from512_to1023",
                                "received_total_octet_frames_from65_to127",
                                "received_unicast_frames",
                                "received_unknown_opcodes",
                                "rfc2819_ether_stats_crc_align_errors",
                                "rfc2819_ether_stats_jabbers",
                                "rfc2819_ether_stats_oversized_pkts",
                                "rfc3635dot3_stats_alignment_errors",
                                "symbol_errors",
                                "total_bytes_transmitted",
                                "total_frames_transmitted",
                                "total_good_bytes_transmitted",
                                "transmitted8021q_frames",
                                "transmitted_broadcast_frames",
                                "transmitted_good_frames",
                                "transmitted_multicast_frames",
                                "transmitted_total64_octet_frames",
                                "transmitted_total_octet_frames_from1024_to1518",
                                "transmitted_total_octet_frames_from128_to255",
                                "transmitted_total_octet_frames_from1518_to_max",
                                "transmitted_total_octet_frames_from256_to511",
                                "transmitted_total_octet_frames_from512_to1023",
                                "transmitted_total_octet_frames_from65_to127",
                                "transmitted_total_pause_frames",
                                "transmitted_unicast_frames",
                                "uncounted_dropped_frames") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(EthernetInterface.Statistics.Statistic, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(EthernetInterface.Statistics.Statistic, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.interface_name.is_set or
                    self.aborted_packet_drops.is_set or
                    self.buffer_underrun_packet_drops.is_set or
                    self.dropped_ether_stats_fragments.is_set or
                    self.dropped_ether_stats_undersize_pkts.is_set or
                    self.dropped_giant_packets_greaterthan_mru.is_set or
                    self.dropped_jabbers_packets_greaterthan_mru.is_set or
                    self.dropped_miscellaneous_error_packets.is_set or
                    self.dropped_packets_with_crc_align_errors.is_set or
                    self.ether_stats_collisions.is_set or
                    self.invalid_dest_mac_drop_packets.is_set or
                    self.invalid_encap_drop_packets.is_set or
                    self.miscellaneous_output_errors.is_set or
                    self.number_of_aborted_packets_dropped.is_set or
                    self.number_of_buffer_overrun_packets_dropped.is_set or
                    self.number_of_miscellaneous_packets_dropped.is_set or
                    self.numberof_invalid_vlan_id_packets_dropped.is_set or
                    self.received8021q_frames.is_set or
                    self.received_broadcast_frames.is_set or
                    self.received_good_bytes.is_set or
                    self.received_good_frames.is_set or
                    self.received_multicast_frames.is_set or
                    self.received_pause_frames.is_set or
                    self.received_total64_octet_frames.is_set or
                    self.received_total_bytes.is_set or
                    self.received_total_frames.is_set or
                    self.received_total_octet_frames_from1024_to1518.is_set or
                    self.received_total_octet_frames_from128_to255.is_set or
                    self.received_total_octet_frames_from1519_to_max.is_set or
                    self.received_total_octet_frames_from256_to511.is_set or
                    self.received_total_octet_frames_from512_to1023.is_set or
                    self.received_total_octet_frames_from65_to127.is_set or
                    self.received_unicast_frames.is_set or
                    self.received_unknown_opcodes.is_set or
                    self.rfc2819_ether_stats_crc_align_errors.is_set or
                    self.rfc2819_ether_stats_jabbers.is_set or
                    self.rfc2819_ether_stats_oversized_pkts.is_set or
                    self.rfc3635dot3_stats_alignment_errors.is_set or
                    self.symbol_errors.is_set or
                    self.total_bytes_transmitted.is_set or
                    self.total_frames_transmitted.is_set or
                    self.total_good_bytes_transmitted.is_set or
                    self.transmitted8021q_frames.is_set or
                    self.transmitted_broadcast_frames.is_set or
                    self.transmitted_good_frames.is_set or
                    self.transmitted_multicast_frames.is_set or
                    self.transmitted_total64_octet_frames.is_set or
                    self.transmitted_total_octet_frames_from1024_to1518.is_set or
                    self.transmitted_total_octet_frames_from128_to255.is_set or
                    self.transmitted_total_octet_frames_from1518_to_max.is_set or
                    self.transmitted_total_octet_frames_from256_to511.is_set or
                    self.transmitted_total_octet_frames_from512_to1023.is_set or
                    self.transmitted_total_octet_frames_from65_to127.is_set or
                    self.transmitted_total_pause_frames.is_set or
                    self.transmitted_unicast_frames.is_set or
                    self.uncounted_dropped_frames.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.interface_name.yfilter != YFilter.not_set or
                    self.aborted_packet_drops.yfilter != YFilter.not_set or
                    self.buffer_underrun_packet_drops.yfilter != YFilter.not_set or
                    self.dropped_ether_stats_fragments.yfilter != YFilter.not_set or
                    self.dropped_ether_stats_undersize_pkts.yfilter != YFilter.not_set or
                    self.dropped_giant_packets_greaterthan_mru.yfilter != YFilter.not_set or
                    self.dropped_jabbers_packets_greaterthan_mru.yfilter != YFilter.not_set or
                    self.dropped_miscellaneous_error_packets.yfilter != YFilter.not_set or
                    self.dropped_packets_with_crc_align_errors.yfilter != YFilter.not_set or
                    self.ether_stats_collisions.yfilter != YFilter.not_set or
                    self.invalid_dest_mac_drop_packets.yfilter != YFilter.not_set or
                    self.invalid_encap_drop_packets.yfilter != YFilter.not_set or
                    self.miscellaneous_output_errors.yfilter != YFilter.not_set or
                    self.number_of_aborted_packets_dropped.yfilter != YFilter.not_set or
                    self.number_of_buffer_overrun_packets_dropped.yfilter != YFilter.not_set or
                    self.number_of_miscellaneous_packets_dropped.yfilter != YFilter.not_set or
                    self.numberof_invalid_vlan_id_packets_dropped.yfilter != YFilter.not_set or
                    self.received8021q_frames.yfilter != YFilter.not_set or
                    self.received_broadcast_frames.yfilter != YFilter.not_set or
                    self.received_good_bytes.yfilter != YFilter.not_set or
                    self.received_good_frames.yfilter != YFilter.not_set or
                    self.received_multicast_frames.yfilter != YFilter.not_set or
                    self.received_pause_frames.yfilter != YFilter.not_set or
                    self.received_total64_octet_frames.yfilter != YFilter.not_set or
                    self.received_total_bytes.yfilter != YFilter.not_set or
                    self.received_total_frames.yfilter != YFilter.not_set or
                    self.received_total_octet_frames_from1024_to1518.yfilter != YFilter.not_set or
                    self.received_total_octet_frames_from128_to255.yfilter != YFilter.not_set or
                    self.received_total_octet_frames_from1519_to_max.yfilter != YFilter.not_set or
                    self.received_total_octet_frames_from256_to511.yfilter != YFilter.not_set or
                    self.received_total_octet_frames_from512_to1023.yfilter != YFilter.not_set or
                    self.received_total_octet_frames_from65_to127.yfilter != YFilter.not_set or
                    self.received_unicast_frames.yfilter != YFilter.not_set or
                    self.received_unknown_opcodes.yfilter != YFilter.not_set or
                    self.rfc2819_ether_stats_crc_align_errors.yfilter != YFilter.not_set or
                    self.rfc2819_ether_stats_jabbers.yfilter != YFilter.not_set or
                    self.rfc2819_ether_stats_oversized_pkts.yfilter != YFilter.not_set or
                    self.rfc3635dot3_stats_alignment_errors.yfilter != YFilter.not_set or
                    self.symbol_errors.yfilter != YFilter.not_set or
                    self.total_bytes_transmitted.yfilter != YFilter.not_set or
                    self.total_frames_transmitted.yfilter != YFilter.not_set or
                    self.total_good_bytes_transmitted.yfilter != YFilter.not_set or
                    self.transmitted8021q_frames.yfilter != YFilter.not_set or
                    self.transmitted_broadcast_frames.yfilter != YFilter.not_set or
                    self.transmitted_good_frames.yfilter != YFilter.not_set or
                    self.transmitted_multicast_frames.yfilter != YFilter.not_set or
                    self.transmitted_total64_octet_frames.yfilter != YFilter.not_set or
                    self.transmitted_total_octet_frames_from1024_to1518.yfilter != YFilter.not_set or
                    self.transmitted_total_octet_frames_from128_to255.yfilter != YFilter.not_set or
                    self.transmitted_total_octet_frames_from1518_to_max.yfilter != YFilter.not_set or
                    self.transmitted_total_octet_frames_from256_to511.yfilter != YFilter.not_set or
                    self.transmitted_total_octet_frames_from512_to1023.yfilter != YFilter.not_set or
                    self.transmitted_total_octet_frames_from65_to127.yfilter != YFilter.not_set or
                    self.transmitted_total_pause_frames.yfilter != YFilter.not_set or
                    self.transmitted_unicast_frames.yfilter != YFilter.not_set or
                    self.uncounted_dropped_frames.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "statistic" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-drivers-media-eth-oper:ethernet-interface/statistics/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.interface_name.get_name_leafdata())
                if (self.aborted_packet_drops.is_set or self.aborted_packet_drops.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.aborted_packet_drops.get_name_leafdata())
                if (self.buffer_underrun_packet_drops.is_set or self.buffer_underrun_packet_drops.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.buffer_underrun_packet_drops.get_name_leafdata())
                if (self.dropped_ether_stats_fragments.is_set or self.dropped_ether_stats_fragments.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dropped_ether_stats_fragments.get_name_leafdata())
                if (self.dropped_ether_stats_undersize_pkts.is_set or self.dropped_ether_stats_undersize_pkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dropped_ether_stats_undersize_pkts.get_name_leafdata())
                if (self.dropped_giant_packets_greaterthan_mru.is_set or self.dropped_giant_packets_greaterthan_mru.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dropped_giant_packets_greaterthan_mru.get_name_leafdata())
                if (self.dropped_jabbers_packets_greaterthan_mru.is_set or self.dropped_jabbers_packets_greaterthan_mru.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dropped_jabbers_packets_greaterthan_mru.get_name_leafdata())
                if (self.dropped_miscellaneous_error_packets.is_set or self.dropped_miscellaneous_error_packets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dropped_miscellaneous_error_packets.get_name_leafdata())
                if (self.dropped_packets_with_crc_align_errors.is_set or self.dropped_packets_with_crc_align_errors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dropped_packets_with_crc_align_errors.get_name_leafdata())
                if (self.ether_stats_collisions.is_set or self.ether_stats_collisions.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ether_stats_collisions.get_name_leafdata())
                if (self.invalid_dest_mac_drop_packets.is_set or self.invalid_dest_mac_drop_packets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.invalid_dest_mac_drop_packets.get_name_leafdata())
                if (self.invalid_encap_drop_packets.is_set or self.invalid_encap_drop_packets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.invalid_encap_drop_packets.get_name_leafdata())
                if (self.miscellaneous_output_errors.is_set or self.miscellaneous_output_errors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.miscellaneous_output_errors.get_name_leafdata())
                if (self.number_of_aborted_packets_dropped.is_set or self.number_of_aborted_packets_dropped.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.number_of_aborted_packets_dropped.get_name_leafdata())
                if (self.number_of_buffer_overrun_packets_dropped.is_set or self.number_of_buffer_overrun_packets_dropped.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.number_of_buffer_overrun_packets_dropped.get_name_leafdata())
                if (self.number_of_miscellaneous_packets_dropped.is_set or self.number_of_miscellaneous_packets_dropped.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.number_of_miscellaneous_packets_dropped.get_name_leafdata())
                if (self.numberof_invalid_vlan_id_packets_dropped.is_set or self.numberof_invalid_vlan_id_packets_dropped.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.numberof_invalid_vlan_id_packets_dropped.get_name_leafdata())
                if (self.received8021q_frames.is_set or self.received8021q_frames.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.received8021q_frames.get_name_leafdata())
                if (self.received_broadcast_frames.is_set or self.received_broadcast_frames.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.received_broadcast_frames.get_name_leafdata())
                if (self.received_good_bytes.is_set or self.received_good_bytes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.received_good_bytes.get_name_leafdata())
                if (self.received_good_frames.is_set or self.received_good_frames.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.received_good_frames.get_name_leafdata())
                if (self.received_multicast_frames.is_set or self.received_multicast_frames.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.received_multicast_frames.get_name_leafdata())
                if (self.received_pause_frames.is_set or self.received_pause_frames.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.received_pause_frames.get_name_leafdata())
                if (self.received_total64_octet_frames.is_set or self.received_total64_octet_frames.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.received_total64_octet_frames.get_name_leafdata())
                if (self.received_total_bytes.is_set or self.received_total_bytes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.received_total_bytes.get_name_leafdata())
                if (self.received_total_frames.is_set or self.received_total_frames.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.received_total_frames.get_name_leafdata())
                if (self.received_total_octet_frames_from1024_to1518.is_set or self.received_total_octet_frames_from1024_to1518.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.received_total_octet_frames_from1024_to1518.get_name_leafdata())
                if (self.received_total_octet_frames_from128_to255.is_set or self.received_total_octet_frames_from128_to255.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.received_total_octet_frames_from128_to255.get_name_leafdata())
                if (self.received_total_octet_frames_from1519_to_max.is_set or self.received_total_octet_frames_from1519_to_max.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.received_total_octet_frames_from1519_to_max.get_name_leafdata())
                if (self.received_total_octet_frames_from256_to511.is_set or self.received_total_octet_frames_from256_to511.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.received_total_octet_frames_from256_to511.get_name_leafdata())
                if (self.received_total_octet_frames_from512_to1023.is_set or self.received_total_octet_frames_from512_to1023.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.received_total_octet_frames_from512_to1023.get_name_leafdata())
                if (self.received_total_octet_frames_from65_to127.is_set or self.received_total_octet_frames_from65_to127.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.received_total_octet_frames_from65_to127.get_name_leafdata())
                if (self.received_unicast_frames.is_set or self.received_unicast_frames.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.received_unicast_frames.get_name_leafdata())
                if (self.received_unknown_opcodes.is_set or self.received_unknown_opcodes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.received_unknown_opcodes.get_name_leafdata())
                if (self.rfc2819_ether_stats_crc_align_errors.is_set or self.rfc2819_ether_stats_crc_align_errors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rfc2819_ether_stats_crc_align_errors.get_name_leafdata())
                if (self.rfc2819_ether_stats_jabbers.is_set or self.rfc2819_ether_stats_jabbers.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rfc2819_ether_stats_jabbers.get_name_leafdata())
                if (self.rfc2819_ether_stats_oversized_pkts.is_set or self.rfc2819_ether_stats_oversized_pkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rfc2819_ether_stats_oversized_pkts.get_name_leafdata())
                if (self.rfc3635dot3_stats_alignment_errors.is_set or self.rfc3635dot3_stats_alignment_errors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rfc3635dot3_stats_alignment_errors.get_name_leafdata())
                if (self.symbol_errors.is_set or self.symbol_errors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.symbol_errors.get_name_leafdata())
                if (self.total_bytes_transmitted.is_set or self.total_bytes_transmitted.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.total_bytes_transmitted.get_name_leafdata())
                if (self.total_frames_transmitted.is_set or self.total_frames_transmitted.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.total_frames_transmitted.get_name_leafdata())
                if (self.total_good_bytes_transmitted.is_set or self.total_good_bytes_transmitted.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.total_good_bytes_transmitted.get_name_leafdata())
                if (self.transmitted8021q_frames.is_set or self.transmitted8021q_frames.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.transmitted8021q_frames.get_name_leafdata())
                if (self.transmitted_broadcast_frames.is_set or self.transmitted_broadcast_frames.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.transmitted_broadcast_frames.get_name_leafdata())
                if (self.transmitted_good_frames.is_set or self.transmitted_good_frames.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.transmitted_good_frames.get_name_leafdata())
                if (self.transmitted_multicast_frames.is_set or self.transmitted_multicast_frames.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.transmitted_multicast_frames.get_name_leafdata())
                if (self.transmitted_total64_octet_frames.is_set or self.transmitted_total64_octet_frames.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.transmitted_total64_octet_frames.get_name_leafdata())
                if (self.transmitted_total_octet_frames_from1024_to1518.is_set or self.transmitted_total_octet_frames_from1024_to1518.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.transmitted_total_octet_frames_from1024_to1518.get_name_leafdata())
                if (self.transmitted_total_octet_frames_from128_to255.is_set or self.transmitted_total_octet_frames_from128_to255.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.transmitted_total_octet_frames_from128_to255.get_name_leafdata())
                if (self.transmitted_total_octet_frames_from1518_to_max.is_set or self.transmitted_total_octet_frames_from1518_to_max.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.transmitted_total_octet_frames_from1518_to_max.get_name_leafdata())
                if (self.transmitted_total_octet_frames_from256_to511.is_set or self.transmitted_total_octet_frames_from256_to511.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.transmitted_total_octet_frames_from256_to511.get_name_leafdata())
                if (self.transmitted_total_octet_frames_from512_to1023.is_set or self.transmitted_total_octet_frames_from512_to1023.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.transmitted_total_octet_frames_from512_to1023.get_name_leafdata())
                if (self.transmitted_total_octet_frames_from65_to127.is_set or self.transmitted_total_octet_frames_from65_to127.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.transmitted_total_octet_frames_from65_to127.get_name_leafdata())
                if (self.transmitted_total_pause_frames.is_set or self.transmitted_total_pause_frames.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.transmitted_total_pause_frames.get_name_leafdata())
                if (self.transmitted_unicast_frames.is_set or self.transmitted_unicast_frames.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.transmitted_unicast_frames.get_name_leafdata())
                if (self.uncounted_dropped_frames.is_set or self.uncounted_dropped_frames.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.uncounted_dropped_frames.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "interface-name" or name == "aborted-packet-drops" or name == "buffer-underrun-packet-drops" or name == "dropped-ether-stats-fragments" or name == "dropped-ether-stats-undersize-pkts" or name == "dropped-giant-packets-greaterthan-mru" or name == "dropped-jabbers-packets-greaterthan-mru" or name == "dropped-miscellaneous-error-packets" or name == "dropped-packets-with-crc-align-errors" or name == "ether-stats-collisions" or name == "invalid-dest-mac-drop-packets" or name == "invalid-encap-drop-packets" or name == "miscellaneous-output-errors" or name == "number-of-aborted-packets-dropped" or name == "number-of-buffer-overrun-packets-dropped" or name == "number-of-miscellaneous-packets-dropped" or name == "numberof-invalid-vlan-id-packets-dropped" or name == "received8021q-frames" or name == "received-broadcast-frames" or name == "received-good-bytes" or name == "received-good-frames" or name == "received-multicast-frames" or name == "received-pause-frames" or name == "received-total64-octet-frames" or name == "received-total-bytes" or name == "received-total-frames" or name == "received-total-octet-frames-from1024-to1518" or name == "received-total-octet-frames-from128-to255" or name == "received-total-octet-frames-from1519-to-max" or name == "received-total-octet-frames-from256-to511" or name == "received-total-octet-frames-from512-to1023" or name == "received-total-octet-frames-from65-to127" or name == "received-unicast-frames" or name == "received-unknown-opcodes" or name == "rfc2819-ether-stats-crc-align-errors" or name == "rfc2819-ether-stats-jabbers" or name == "rfc2819-ether-stats-oversized-pkts" or name == "rfc3635dot3-stats-alignment-errors" or name == "symbol-errors" or name == "total-bytes-transmitted" or name == "total-frames-transmitted" or name == "total-good-bytes-transmitted" or name == "transmitted8021q-frames" or name == "transmitted-broadcast-frames" or name == "transmitted-good-frames" or name == "transmitted-multicast-frames" or name == "transmitted-total64-octet-frames" or name == "transmitted-total-octet-frames-from1024-to1518" or name == "transmitted-total-octet-frames-from128-to255" or name == "transmitted-total-octet-frames-from1518-to-max" or name == "transmitted-total-octet-frames-from256-to511" or name == "transmitted-total-octet-frames-from512-to1023" or name == "transmitted-total-octet-frames-from65-to127" or name == "transmitted-total-pause-frames" or name == "transmitted-unicast-frames" or name == "uncounted-dropped-frames"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "interface-name"):
                    self.interface_name = value
                    self.interface_name.value_namespace = name_space
                    self.interface_name.value_namespace_prefix = name_space_prefix
                if(value_path == "aborted-packet-drops"):
                    self.aborted_packet_drops = value
                    self.aborted_packet_drops.value_namespace = name_space
                    self.aborted_packet_drops.value_namespace_prefix = name_space_prefix
                if(value_path == "buffer-underrun-packet-drops"):
                    self.buffer_underrun_packet_drops = value
                    self.buffer_underrun_packet_drops.value_namespace = name_space
                    self.buffer_underrun_packet_drops.value_namespace_prefix = name_space_prefix
                if(value_path == "dropped-ether-stats-fragments"):
                    self.dropped_ether_stats_fragments = value
                    self.dropped_ether_stats_fragments.value_namespace = name_space
                    self.dropped_ether_stats_fragments.value_namespace_prefix = name_space_prefix
                if(value_path == "dropped-ether-stats-undersize-pkts"):
                    self.dropped_ether_stats_undersize_pkts = value
                    self.dropped_ether_stats_undersize_pkts.value_namespace = name_space
                    self.dropped_ether_stats_undersize_pkts.value_namespace_prefix = name_space_prefix
                if(value_path == "dropped-giant-packets-greaterthan-mru"):
                    self.dropped_giant_packets_greaterthan_mru = value
                    self.dropped_giant_packets_greaterthan_mru.value_namespace = name_space
                    self.dropped_giant_packets_greaterthan_mru.value_namespace_prefix = name_space_prefix
                if(value_path == "dropped-jabbers-packets-greaterthan-mru"):
                    self.dropped_jabbers_packets_greaterthan_mru = value
                    self.dropped_jabbers_packets_greaterthan_mru.value_namespace = name_space
                    self.dropped_jabbers_packets_greaterthan_mru.value_namespace_prefix = name_space_prefix
                if(value_path == "dropped-miscellaneous-error-packets"):
                    self.dropped_miscellaneous_error_packets = value
                    self.dropped_miscellaneous_error_packets.value_namespace = name_space
                    self.dropped_miscellaneous_error_packets.value_namespace_prefix = name_space_prefix
                if(value_path == "dropped-packets-with-crc-align-errors"):
                    self.dropped_packets_with_crc_align_errors = value
                    self.dropped_packets_with_crc_align_errors.value_namespace = name_space
                    self.dropped_packets_with_crc_align_errors.value_namespace_prefix = name_space_prefix
                if(value_path == "ether-stats-collisions"):
                    self.ether_stats_collisions = value
                    self.ether_stats_collisions.value_namespace = name_space
                    self.ether_stats_collisions.value_namespace_prefix = name_space_prefix
                if(value_path == "invalid-dest-mac-drop-packets"):
                    self.invalid_dest_mac_drop_packets = value
                    self.invalid_dest_mac_drop_packets.value_namespace = name_space
                    self.invalid_dest_mac_drop_packets.value_namespace_prefix = name_space_prefix
                if(value_path == "invalid-encap-drop-packets"):
                    self.invalid_encap_drop_packets = value
                    self.invalid_encap_drop_packets.value_namespace = name_space
                    self.invalid_encap_drop_packets.value_namespace_prefix = name_space_prefix
                if(value_path == "miscellaneous-output-errors"):
                    self.miscellaneous_output_errors = value
                    self.miscellaneous_output_errors.value_namespace = name_space
                    self.miscellaneous_output_errors.value_namespace_prefix = name_space_prefix
                if(value_path == "number-of-aborted-packets-dropped"):
                    self.number_of_aborted_packets_dropped = value
                    self.number_of_aborted_packets_dropped.value_namespace = name_space
                    self.number_of_aborted_packets_dropped.value_namespace_prefix = name_space_prefix
                if(value_path == "number-of-buffer-overrun-packets-dropped"):
                    self.number_of_buffer_overrun_packets_dropped = value
                    self.number_of_buffer_overrun_packets_dropped.value_namespace = name_space
                    self.number_of_buffer_overrun_packets_dropped.value_namespace_prefix = name_space_prefix
                if(value_path == "number-of-miscellaneous-packets-dropped"):
                    self.number_of_miscellaneous_packets_dropped = value
                    self.number_of_miscellaneous_packets_dropped.value_namespace = name_space
                    self.number_of_miscellaneous_packets_dropped.value_namespace_prefix = name_space_prefix
                if(value_path == "numberof-invalid-vlan-id-packets-dropped"):
                    self.numberof_invalid_vlan_id_packets_dropped = value
                    self.numberof_invalid_vlan_id_packets_dropped.value_namespace = name_space
                    self.numberof_invalid_vlan_id_packets_dropped.value_namespace_prefix = name_space_prefix
                if(value_path == "received8021q-frames"):
                    self.received8021q_frames = value
                    self.received8021q_frames.value_namespace = name_space
                    self.received8021q_frames.value_namespace_prefix = name_space_prefix
                if(value_path == "received-broadcast-frames"):
                    self.received_broadcast_frames = value
                    self.received_broadcast_frames.value_namespace = name_space
                    self.received_broadcast_frames.value_namespace_prefix = name_space_prefix
                if(value_path == "received-good-bytes"):
                    self.received_good_bytes = value
                    self.received_good_bytes.value_namespace = name_space
                    self.received_good_bytes.value_namespace_prefix = name_space_prefix
                if(value_path == "received-good-frames"):
                    self.received_good_frames = value
                    self.received_good_frames.value_namespace = name_space
                    self.received_good_frames.value_namespace_prefix = name_space_prefix
                if(value_path == "received-multicast-frames"):
                    self.received_multicast_frames = value
                    self.received_multicast_frames.value_namespace = name_space
                    self.received_multicast_frames.value_namespace_prefix = name_space_prefix
                if(value_path == "received-pause-frames"):
                    self.received_pause_frames = value
                    self.received_pause_frames.value_namespace = name_space
                    self.received_pause_frames.value_namespace_prefix = name_space_prefix
                if(value_path == "received-total64-octet-frames"):
                    self.received_total64_octet_frames = value
                    self.received_total64_octet_frames.value_namespace = name_space
                    self.received_total64_octet_frames.value_namespace_prefix = name_space_prefix
                if(value_path == "received-total-bytes"):
                    self.received_total_bytes = value
                    self.received_total_bytes.value_namespace = name_space
                    self.received_total_bytes.value_namespace_prefix = name_space_prefix
                if(value_path == "received-total-frames"):
                    self.received_total_frames = value
                    self.received_total_frames.value_namespace = name_space
                    self.received_total_frames.value_namespace_prefix = name_space_prefix
                if(value_path == "received-total-octet-frames-from1024-to1518"):
                    self.received_total_octet_frames_from1024_to1518 = value
                    self.received_total_octet_frames_from1024_to1518.value_namespace = name_space
                    self.received_total_octet_frames_from1024_to1518.value_namespace_prefix = name_space_prefix
                if(value_path == "received-total-octet-frames-from128-to255"):
                    self.received_total_octet_frames_from128_to255 = value
                    self.received_total_octet_frames_from128_to255.value_namespace = name_space
                    self.received_total_octet_frames_from128_to255.value_namespace_prefix = name_space_prefix
                if(value_path == "received-total-octet-frames-from1519-to-max"):
                    self.received_total_octet_frames_from1519_to_max = value
                    self.received_total_octet_frames_from1519_to_max.value_namespace = name_space
                    self.received_total_octet_frames_from1519_to_max.value_namespace_prefix = name_space_prefix
                if(value_path == "received-total-octet-frames-from256-to511"):
                    self.received_total_octet_frames_from256_to511 = value
                    self.received_total_octet_frames_from256_to511.value_namespace = name_space
                    self.received_total_octet_frames_from256_to511.value_namespace_prefix = name_space_prefix
                if(value_path == "received-total-octet-frames-from512-to1023"):
                    self.received_total_octet_frames_from512_to1023 = value
                    self.received_total_octet_frames_from512_to1023.value_namespace = name_space
                    self.received_total_octet_frames_from512_to1023.value_namespace_prefix = name_space_prefix
                if(value_path == "received-total-octet-frames-from65-to127"):
                    self.received_total_octet_frames_from65_to127 = value
                    self.received_total_octet_frames_from65_to127.value_namespace = name_space
                    self.received_total_octet_frames_from65_to127.value_namespace_prefix = name_space_prefix
                if(value_path == "received-unicast-frames"):
                    self.received_unicast_frames = value
                    self.received_unicast_frames.value_namespace = name_space
                    self.received_unicast_frames.value_namespace_prefix = name_space_prefix
                if(value_path == "received-unknown-opcodes"):
                    self.received_unknown_opcodes = value
                    self.received_unknown_opcodes.value_namespace = name_space
                    self.received_unknown_opcodes.value_namespace_prefix = name_space_prefix
                if(value_path == "rfc2819-ether-stats-crc-align-errors"):
                    self.rfc2819_ether_stats_crc_align_errors = value
                    self.rfc2819_ether_stats_crc_align_errors.value_namespace = name_space
                    self.rfc2819_ether_stats_crc_align_errors.value_namespace_prefix = name_space_prefix
                if(value_path == "rfc2819-ether-stats-jabbers"):
                    self.rfc2819_ether_stats_jabbers = value
                    self.rfc2819_ether_stats_jabbers.value_namespace = name_space
                    self.rfc2819_ether_stats_jabbers.value_namespace_prefix = name_space_prefix
                if(value_path == "rfc2819-ether-stats-oversized-pkts"):
                    self.rfc2819_ether_stats_oversized_pkts = value
                    self.rfc2819_ether_stats_oversized_pkts.value_namespace = name_space
                    self.rfc2819_ether_stats_oversized_pkts.value_namespace_prefix = name_space_prefix
                if(value_path == "rfc3635dot3-stats-alignment-errors"):
                    self.rfc3635dot3_stats_alignment_errors = value
                    self.rfc3635dot3_stats_alignment_errors.value_namespace = name_space
                    self.rfc3635dot3_stats_alignment_errors.value_namespace_prefix = name_space_prefix
                if(value_path == "symbol-errors"):
                    self.symbol_errors = value
                    self.symbol_errors.value_namespace = name_space
                    self.symbol_errors.value_namespace_prefix = name_space_prefix
                if(value_path == "total-bytes-transmitted"):
                    self.total_bytes_transmitted = value
                    self.total_bytes_transmitted.value_namespace = name_space
                    self.total_bytes_transmitted.value_namespace_prefix = name_space_prefix
                if(value_path == "total-frames-transmitted"):
                    self.total_frames_transmitted = value
                    self.total_frames_transmitted.value_namespace = name_space
                    self.total_frames_transmitted.value_namespace_prefix = name_space_prefix
                if(value_path == "total-good-bytes-transmitted"):
                    self.total_good_bytes_transmitted = value
                    self.total_good_bytes_transmitted.value_namespace = name_space
                    self.total_good_bytes_transmitted.value_namespace_prefix = name_space_prefix
                if(value_path == "transmitted8021q-frames"):
                    self.transmitted8021q_frames = value
                    self.transmitted8021q_frames.value_namespace = name_space
                    self.transmitted8021q_frames.value_namespace_prefix = name_space_prefix
                if(value_path == "transmitted-broadcast-frames"):
                    self.transmitted_broadcast_frames = value
                    self.transmitted_broadcast_frames.value_namespace = name_space
                    self.transmitted_broadcast_frames.value_namespace_prefix = name_space_prefix
                if(value_path == "transmitted-good-frames"):
                    self.transmitted_good_frames = value
                    self.transmitted_good_frames.value_namespace = name_space
                    self.transmitted_good_frames.value_namespace_prefix = name_space_prefix
                if(value_path == "transmitted-multicast-frames"):
                    self.transmitted_multicast_frames = value
                    self.transmitted_multicast_frames.value_namespace = name_space
                    self.transmitted_multicast_frames.value_namespace_prefix = name_space_prefix
                if(value_path == "transmitted-total64-octet-frames"):
                    self.transmitted_total64_octet_frames = value
                    self.transmitted_total64_octet_frames.value_namespace = name_space
                    self.transmitted_total64_octet_frames.value_namespace_prefix = name_space_prefix
                if(value_path == "transmitted-total-octet-frames-from1024-to1518"):
                    self.transmitted_total_octet_frames_from1024_to1518 = value
                    self.transmitted_total_octet_frames_from1024_to1518.value_namespace = name_space
                    self.transmitted_total_octet_frames_from1024_to1518.value_namespace_prefix = name_space_prefix
                if(value_path == "transmitted-total-octet-frames-from128-to255"):
                    self.transmitted_total_octet_frames_from128_to255 = value
                    self.transmitted_total_octet_frames_from128_to255.value_namespace = name_space
                    self.transmitted_total_octet_frames_from128_to255.value_namespace_prefix = name_space_prefix
                if(value_path == "transmitted-total-octet-frames-from1518-to-max"):
                    self.transmitted_total_octet_frames_from1518_to_max = value
                    self.transmitted_total_octet_frames_from1518_to_max.value_namespace = name_space
                    self.transmitted_total_octet_frames_from1518_to_max.value_namespace_prefix = name_space_prefix
                if(value_path == "transmitted-total-octet-frames-from256-to511"):
                    self.transmitted_total_octet_frames_from256_to511 = value
                    self.transmitted_total_octet_frames_from256_to511.value_namespace = name_space
                    self.transmitted_total_octet_frames_from256_to511.value_namespace_prefix = name_space_prefix
                if(value_path == "transmitted-total-octet-frames-from512-to1023"):
                    self.transmitted_total_octet_frames_from512_to1023 = value
                    self.transmitted_total_octet_frames_from512_to1023.value_namespace = name_space
                    self.transmitted_total_octet_frames_from512_to1023.value_namespace_prefix = name_space_prefix
                if(value_path == "transmitted-total-octet-frames-from65-to127"):
                    self.transmitted_total_octet_frames_from65_to127 = value
                    self.transmitted_total_octet_frames_from65_to127.value_namespace = name_space
                    self.transmitted_total_octet_frames_from65_to127.value_namespace_prefix = name_space_prefix
                if(value_path == "transmitted-total-pause-frames"):
                    self.transmitted_total_pause_frames = value
                    self.transmitted_total_pause_frames.value_namespace = name_space
                    self.transmitted_total_pause_frames.value_namespace_prefix = name_space_prefix
                if(value_path == "transmitted-unicast-frames"):
                    self.transmitted_unicast_frames = value
                    self.transmitted_unicast_frames.value_namespace = name_space
                    self.transmitted_unicast_frames.value_namespace_prefix = name_space_prefix
                if(value_path == "uncounted-dropped-frames"):
                    self.uncounted_dropped_frames = value
                    self.uncounted_dropped_frames.value_namespace = name_space
                    self.uncounted_dropped_frames.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.statistic:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.statistic:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "statistics" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-drivers-media-eth-oper:ethernet-interface/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "statistic"):
                for c in self.statistic:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = EthernetInterface.Statistics.Statistic()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.statistic.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "statistic"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Interfaces(Entity):
        """
        Ethernet controller info table
        
        .. attribute:: interface
        
        	Ethernet controller information
        	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Interfaces.Interface>`
        
        

        """

        _prefix = 'drivers-media-eth-oper'
        _revision = '2017-04-04'

        def __init__(self):
            super(EthernetInterface.Interfaces, self).__init__()

            self.yang_name = "interfaces"
            self.yang_parent_name = "ethernet-interface"

            self.interface = YList(self)

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
                        super(EthernetInterface.Interfaces, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(EthernetInterface.Interfaces, self).__setattr__(name, value)


        class Interface(Entity):
            """
            Ethernet controller information
            
            .. attribute:: interface_name  <key>
            
            	The name of the interface
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: admin_state
            
            	Port Administrative State
            	**type**\:   :py:class:`EthernetPortEnable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetPortEnable>`
            
            .. attribute:: layer1_info
            
            	Layer 1 information
            	**type**\:   :py:class:`Layer1Info <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Interfaces.Interface.Layer1Info>`
            
            .. attribute:: mac_info
            
            	MAC Layer information
            	**type**\:   :py:class:`MacInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Interfaces.Interface.MacInfo>`
            
            .. attribute:: oper_state_up
            
            	Port Operational state \- TRUE if up
            	**type**\:  bool
            
            .. attribute:: phy_info
            
            	PHY information
            	**type**\:   :py:class:`PhyInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Interfaces.Interface.PhyInfo>`
            
            .. attribute:: transport_info
            
            	Transport state information
            	**type**\:   :py:class:`TransportInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Interfaces.Interface.TransportInfo>`
            
            

            """

            _prefix = 'drivers-media-eth-oper'
            _revision = '2017-04-04'

            def __init__(self):
                super(EthernetInterface.Interfaces.Interface, self).__init__()

                self.yang_name = "interface"
                self.yang_parent_name = "interfaces"

                self.interface_name = YLeaf(YType.str, "interface-name")

                self.admin_state = YLeaf(YType.enumeration, "admin-state")

                self.oper_state_up = YLeaf(YType.boolean, "oper-state-up")

                self.layer1_info = EthernetInterface.Interfaces.Interface.Layer1Info()
                self.layer1_info.parent = self
                self._children_name_map["layer1_info"] = "layer1-info"
                self._children_yang_names.add("layer1-info")

                self.mac_info = EthernetInterface.Interfaces.Interface.MacInfo()
                self.mac_info.parent = self
                self._children_name_map["mac_info"] = "mac-info"
                self._children_yang_names.add("mac-info")

                self.phy_info = EthernetInterface.Interfaces.Interface.PhyInfo()
                self.phy_info.parent = self
                self._children_name_map["phy_info"] = "phy-info"
                self._children_yang_names.add("phy-info")

                self.transport_info = EthernetInterface.Interfaces.Interface.TransportInfo()
                self.transport_info.parent = self
                self._children_name_map["transport_info"] = "transport-info"
                self._children_yang_names.add("transport-info")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("interface_name",
                                "admin_state",
                                "oper_state_up") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(EthernetInterface.Interfaces.Interface, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(EthernetInterface.Interfaces.Interface, self).__setattr__(name, value)


            class PhyInfo(Entity):
                """
                PHY information
                
                .. attribute:: fec_details
                
                	Forward Error Correction information
                	**type**\:   :py:class:`FecDetails <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Interfaces.Interface.PhyInfo.FecDetails>`
                
                .. attribute:: loopback
                
                	Port operational loopback
                	**type**\:   :py:class:`EthernetLoopback <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetLoopback>`
                
                .. attribute:: media_type
                
                	Port media type
                	**type**\:   :py:class:`EthernetMedia <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetMedia>`
                
                .. attribute:: phy_details
                
                	Details about the PHY
                	**type**\:   :py:class:`PhyDetails <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails>`
                
                .. attribute:: phy_present
                
                	Presence of PHY
                	**type**\:   :py:class:`EtherPhyPresent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EtherPhyPresent>`
                
                

                """

                _prefix = 'drivers-media-eth-oper'
                _revision = '2017-04-04'

                def __init__(self):
                    super(EthernetInterface.Interfaces.Interface.PhyInfo, self).__init__()

                    self.yang_name = "phy-info"
                    self.yang_parent_name = "interface"

                    self.loopback = YLeaf(YType.enumeration, "loopback")

                    self.media_type = YLeaf(YType.enumeration, "media-type")

                    self.phy_present = YLeaf(YType.enumeration, "phy-present")

                    self.fec_details = EthernetInterface.Interfaces.Interface.PhyInfo.FecDetails()
                    self.fec_details.parent = self
                    self._children_name_map["fec_details"] = "fec-details"
                    self._children_yang_names.add("fec-details")

                    self.phy_details = EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails()
                    self.phy_details.parent = self
                    self._children_name_map["phy_details"] = "phy-details"
                    self._children_yang_names.add("phy-details")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("loopback",
                                    "media_type",
                                    "phy_present") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(EthernetInterface.Interfaces.Interface.PhyInfo, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(EthernetInterface.Interfaces.Interface.PhyInfo, self).__setattr__(name, value)


                class PhyDetails(Entity):
                    """
                    Details about the PHY
                    
                    .. attribute:: dig_opt_mon_alarm_thresholds
                    
                    	Digital Optical Monitoring alarm thresholds
                    	**type**\:   :py:class:`DigOptMonAlarmThresholds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails.DigOptMonAlarmThresholds>`
                    
                    .. attribute:: dig_opt_mon_alarms
                    
                    	Digital Optical Monitoring alarms
                    	**type**\:   :py:class:`DigOptMonAlarms <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails.DigOptMonAlarms>`
                    
                    .. attribute:: lane
                    
                    	Digital Optical Monitoring (per lane information)
                    	**type**\: list of    :py:class:`Lane <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails.Lane>`
                    
                    .. attribute:: lane_field_validity
                    
                    	Digital Optical Monitoring (per lane information) validity
                    	**type**\:   :py:class:`LaneFieldValidity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails.LaneFieldValidity>`
                    
                    .. attribute:: optics_type
                    
                    	Optics module type
                    	**type**\:  str
                    
                    .. attribute:: optics_wavelength
                    
                    	Wavelength of the optics being used in nm \* 1000
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: revision_number
                    
                    	Module revision number
                    	**type**\:  str
                    
                    .. attribute:: transceiver_rx_power
                    
                    	The transceiver receive optical power (uW)
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: transceiver_temperature
                    
                    	The temperature of the transceiver (mDegrees C)
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: transceiver_tx_bias
                    
                    	The laser bias of the transceiver (uA)
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: transceiver_tx_power
                    
                    	The transceiver transmit laser power (uW)
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: transceiver_voltage
                    
                    	The input voltage to the transceiver (mV)
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: vendor
                    
                    	Name of the port optics manufacturer
                    	**type**\:  str
                    
                    .. attribute:: vendor_part_number
                    
                    	Part number for the port optics
                    	**type**\:  str
                    
                    .. attribute:: vendor_serial_number
                    
                    	Serial number for the port optics
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'drivers-media-eth-oper'
                    _revision = '2017-04-04'

                    def __init__(self):
                        super(EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails, self).__init__()

                        self.yang_name = "phy-details"
                        self.yang_parent_name = "phy-info"

                        self.optics_type = YLeaf(YType.str, "optics-type")

                        self.optics_wavelength = YLeaf(YType.uint32, "optics-wavelength")

                        self.revision_number = YLeaf(YType.str, "revision-number")

                        self.transceiver_rx_power = YLeaf(YType.int32, "transceiver-rx-power")

                        self.transceiver_temperature = YLeaf(YType.int32, "transceiver-temperature")

                        self.transceiver_tx_bias = YLeaf(YType.int32, "transceiver-tx-bias")

                        self.transceiver_tx_power = YLeaf(YType.int32, "transceiver-tx-power")

                        self.transceiver_voltage = YLeaf(YType.int32, "transceiver-voltage")

                        self.vendor = YLeaf(YType.str, "vendor")

                        self.vendor_part_number = YLeaf(YType.str, "vendor-part-number")

                        self.vendor_serial_number = YLeaf(YType.str, "vendor-serial-number")

                        self.dig_opt_mon_alarm_thresholds = EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails.DigOptMonAlarmThresholds()
                        self.dig_opt_mon_alarm_thresholds.parent = self
                        self._children_name_map["dig_opt_mon_alarm_thresholds"] = "dig-opt-mon-alarm-thresholds"
                        self._children_yang_names.add("dig-opt-mon-alarm-thresholds")

                        self.dig_opt_mon_alarms = EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails.DigOptMonAlarms()
                        self.dig_opt_mon_alarms.parent = self
                        self._children_name_map["dig_opt_mon_alarms"] = "dig-opt-mon-alarms"
                        self._children_yang_names.add("dig-opt-mon-alarms")

                        self.lane_field_validity = EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails.LaneFieldValidity()
                        self.lane_field_validity.parent = self
                        self._children_name_map["lane_field_validity"] = "lane-field-validity"
                        self._children_yang_names.add("lane-field-validity")

                        self.lane = YList(self)

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("optics_type",
                                        "optics_wavelength",
                                        "revision_number",
                                        "transceiver_rx_power",
                                        "transceiver_temperature",
                                        "transceiver_tx_bias",
                                        "transceiver_tx_power",
                                        "transceiver_voltage",
                                        "vendor",
                                        "vendor_part_number",
                                        "vendor_serial_number") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails, self).__setattr__(name, value)


                    class LaneFieldValidity(Entity):
                        """
                        Digital Optical Monitoring (per lane
                        information) validity
                        
                        .. attribute:: laser_bias_valid
                        
                        	The laser bias 'per lane' field is valid
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: receive_power_valid
                        
                        	The receive power 'per lane' field is valid
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: transmit_power_valid
                        
                        	The transmit power 'per lane' field is valid
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: wavelength_valid
                        
                        	The wavelength 'per lane' field is valid
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        

                        """

                        _prefix = 'drivers-media-eth-oper'
                        _revision = '2017-04-04'

                        def __init__(self):
                            super(EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails.LaneFieldValidity, self).__init__()

                            self.yang_name = "lane-field-validity"
                            self.yang_parent_name = "phy-details"

                            self.laser_bias_valid = YLeaf(YType.int32, "laser-bias-valid")

                            self.receive_power_valid = YLeaf(YType.int32, "receive-power-valid")

                            self.transmit_power_valid = YLeaf(YType.int32, "transmit-power-valid")

                            self.wavelength_valid = YLeaf(YType.int32, "wavelength-valid")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("laser_bias_valid",
                                            "receive_power_valid",
                                            "transmit_power_valid",
                                            "wavelength_valid") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails.LaneFieldValidity, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails.LaneFieldValidity, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.laser_bias_valid.is_set or
                                self.receive_power_valid.is_set or
                                self.transmit_power_valid.is_set or
                                self.wavelength_valid.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.laser_bias_valid.yfilter != YFilter.not_set or
                                self.receive_power_valid.yfilter != YFilter.not_set or
                                self.transmit_power_valid.yfilter != YFilter.not_set or
                                self.wavelength_valid.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "lane-field-validity" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.laser_bias_valid.is_set or self.laser_bias_valid.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.laser_bias_valid.get_name_leafdata())
                            if (self.receive_power_valid.is_set or self.receive_power_valid.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.receive_power_valid.get_name_leafdata())
                            if (self.transmit_power_valid.is_set or self.transmit_power_valid.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.transmit_power_valid.get_name_leafdata())
                            if (self.wavelength_valid.is_set or self.wavelength_valid.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.wavelength_valid.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "laser-bias-valid" or name == "receive-power-valid" or name == "transmit-power-valid" or name == "wavelength-valid"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "laser-bias-valid"):
                                self.laser_bias_valid = value
                                self.laser_bias_valid.value_namespace = name_space
                                self.laser_bias_valid.value_namespace_prefix = name_space_prefix
                            if(value_path == "receive-power-valid"):
                                self.receive_power_valid = value
                                self.receive_power_valid.value_namespace = name_space
                                self.receive_power_valid.value_namespace_prefix = name_space_prefix
                            if(value_path == "transmit-power-valid"):
                                self.transmit_power_valid = value
                                self.transmit_power_valid.value_namespace = name_space
                                self.transmit_power_valid.value_namespace_prefix = name_space_prefix
                            if(value_path == "wavelength-valid"):
                                self.wavelength_valid = value
                                self.wavelength_valid.value_namespace = name_space
                                self.wavelength_valid.value_namespace_prefix = name_space_prefix


                    class DigOptMonAlarmThresholds(Entity):
                        """
                        Digital Optical Monitoring alarm thresholds
                        
                        .. attribute:: field_validity
                        
                        	Field validity
                        	**type**\:   :py:class:`FieldValidity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails.DigOptMonAlarmThresholds.FieldValidity>`
                        
                        .. attribute:: laser_bias_alarm_high
                        
                        	Laser bias high alarm threshold (uA)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: laser_bias_alarm_low
                        
                        	Laser bias low alarm threshold (uA)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: laser_bias_warning_high
                        
                        	Laser bias high warning threshold (uA)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: laser_bias_warning_low
                        
                        	Laser bias low warning threshold (uA)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: optical_receive_power_alarm_high
                        
                        	High optical receive power alarm threshold (uW)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: optical_receive_power_alarm_low
                        
                        	Low optical receive power alarm threshold (uW)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: optical_receive_power_warning_high
                        
                        	High optical receive power warning threshold (uW)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: optical_receive_power_warning_low
                        
                        	Low optical receive power warning threshold (uW)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: optical_transmit_power_alarm_high
                        
                        	High optical transmit power alarm threshold (uW)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: optical_transmit_power_alarm_low
                        
                        	Low optical transmit power alarm threshold (uW)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: optical_transmit_power_warning_high
                        
                        	High optical transmit power warning threshold (uW)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: optical_transmit_power_warning_low
                        
                        	Low optical transmit power warning threshold (uW)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: transceiver_temperature_alarm_high
                        
                        	Transceiver high temperature alarm threshold (mDegrees C)
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: transceiver_temperature_alarm_low
                        
                        	Transceiver low temperature alarm threshold (mDegrees C)
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: transceiver_temperature_warning_high
                        
                        	Transceiver high temperature warning threshold (mDegrees C)
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: transceiver_temperature_warning_low
                        
                        	Transceiver low temperature warning threshold (mDegrees C)
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: transceiver_voltage_alarm_high
                        
                        	Transceiver high voltage alarm threshold (mV)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: transceiver_voltage_alarm_low
                        
                        	Transceiver low voltage alarm threshold (mV)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: transceiver_voltage_warning_high
                        
                        	Transceiver high voltage warning threshold (mV)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: transceiver_voltage_warning_low
                        
                        	Transceiver low voltage warning threshold (mV)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'drivers-media-eth-oper'
                        _revision = '2017-04-04'

                        def __init__(self):
                            super(EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails.DigOptMonAlarmThresholds, self).__init__()

                            self.yang_name = "dig-opt-mon-alarm-thresholds"
                            self.yang_parent_name = "phy-details"

                            self.laser_bias_alarm_high = YLeaf(YType.uint32, "laser-bias-alarm-high")

                            self.laser_bias_alarm_low = YLeaf(YType.uint32, "laser-bias-alarm-low")

                            self.laser_bias_warning_high = YLeaf(YType.uint32, "laser-bias-warning-high")

                            self.laser_bias_warning_low = YLeaf(YType.uint32, "laser-bias-warning-low")

                            self.optical_receive_power_alarm_high = YLeaf(YType.uint32, "optical-receive-power-alarm-high")

                            self.optical_receive_power_alarm_low = YLeaf(YType.uint32, "optical-receive-power-alarm-low")

                            self.optical_receive_power_warning_high = YLeaf(YType.uint32, "optical-receive-power-warning-high")

                            self.optical_receive_power_warning_low = YLeaf(YType.uint32, "optical-receive-power-warning-low")

                            self.optical_transmit_power_alarm_high = YLeaf(YType.uint32, "optical-transmit-power-alarm-high")

                            self.optical_transmit_power_alarm_low = YLeaf(YType.uint32, "optical-transmit-power-alarm-low")

                            self.optical_transmit_power_warning_high = YLeaf(YType.uint32, "optical-transmit-power-warning-high")

                            self.optical_transmit_power_warning_low = YLeaf(YType.uint32, "optical-transmit-power-warning-low")

                            self.transceiver_temperature_alarm_high = YLeaf(YType.int32, "transceiver-temperature-alarm-high")

                            self.transceiver_temperature_alarm_low = YLeaf(YType.int32, "transceiver-temperature-alarm-low")

                            self.transceiver_temperature_warning_high = YLeaf(YType.int32, "transceiver-temperature-warning-high")

                            self.transceiver_temperature_warning_low = YLeaf(YType.int32, "transceiver-temperature-warning-low")

                            self.transceiver_voltage_alarm_high = YLeaf(YType.uint32, "transceiver-voltage-alarm-high")

                            self.transceiver_voltage_alarm_low = YLeaf(YType.uint32, "transceiver-voltage-alarm-low")

                            self.transceiver_voltage_warning_high = YLeaf(YType.uint32, "transceiver-voltage-warning-high")

                            self.transceiver_voltage_warning_low = YLeaf(YType.uint32, "transceiver-voltage-warning-low")

                            self.field_validity = EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails.DigOptMonAlarmThresholds.FieldValidity()
                            self.field_validity.parent = self
                            self._children_name_map["field_validity"] = "field-validity"
                            self._children_yang_names.add("field-validity")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("laser_bias_alarm_high",
                                            "laser_bias_alarm_low",
                                            "laser_bias_warning_high",
                                            "laser_bias_warning_low",
                                            "optical_receive_power_alarm_high",
                                            "optical_receive_power_alarm_low",
                                            "optical_receive_power_warning_high",
                                            "optical_receive_power_warning_low",
                                            "optical_transmit_power_alarm_high",
                                            "optical_transmit_power_alarm_low",
                                            "optical_transmit_power_warning_high",
                                            "optical_transmit_power_warning_low",
                                            "transceiver_temperature_alarm_high",
                                            "transceiver_temperature_alarm_low",
                                            "transceiver_temperature_warning_high",
                                            "transceiver_temperature_warning_low",
                                            "transceiver_voltage_alarm_high",
                                            "transceiver_voltage_alarm_low",
                                            "transceiver_voltage_warning_high",
                                            "transceiver_voltage_warning_low") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails.DigOptMonAlarmThresholds, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails.DigOptMonAlarmThresholds, self).__setattr__(name, value)


                        class FieldValidity(Entity):
                            """
                            Field validity
                            
                            .. attribute:: laser_bias_valid
                            
                            	The laser bias fields are valid
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: receive_power_valid
                            
                            	The receive power fields are valid
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: temperature_valid
                            
                            	The temperature fields are valid
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: transmit_power_valid
                            
                            	The transmit power fields are valid
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: voltage_valid
                            
                            	The voltage fields are valid
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            

                            """

                            _prefix = 'drivers-media-eth-oper'
                            _revision = '2017-04-04'

                            def __init__(self):
                                super(EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails.DigOptMonAlarmThresholds.FieldValidity, self).__init__()

                                self.yang_name = "field-validity"
                                self.yang_parent_name = "dig-opt-mon-alarm-thresholds"

                                self.laser_bias_valid = YLeaf(YType.int32, "laser-bias-valid")

                                self.receive_power_valid = YLeaf(YType.int32, "receive-power-valid")

                                self.temperature_valid = YLeaf(YType.int32, "temperature-valid")

                                self.transmit_power_valid = YLeaf(YType.int32, "transmit-power-valid")

                                self.voltage_valid = YLeaf(YType.int32, "voltage-valid")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("laser_bias_valid",
                                                "receive_power_valid",
                                                "temperature_valid",
                                                "transmit_power_valid",
                                                "voltage_valid") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails.DigOptMonAlarmThresholds.FieldValidity, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails.DigOptMonAlarmThresholds.FieldValidity, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.laser_bias_valid.is_set or
                                    self.receive_power_valid.is_set or
                                    self.temperature_valid.is_set or
                                    self.transmit_power_valid.is_set or
                                    self.voltage_valid.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.laser_bias_valid.yfilter != YFilter.not_set or
                                    self.receive_power_valid.yfilter != YFilter.not_set or
                                    self.temperature_valid.yfilter != YFilter.not_set or
                                    self.transmit_power_valid.yfilter != YFilter.not_set or
                                    self.voltage_valid.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "field-validity" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.laser_bias_valid.is_set or self.laser_bias_valid.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.laser_bias_valid.get_name_leafdata())
                                if (self.receive_power_valid.is_set or self.receive_power_valid.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.receive_power_valid.get_name_leafdata())
                                if (self.temperature_valid.is_set or self.temperature_valid.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.temperature_valid.get_name_leafdata())
                                if (self.transmit_power_valid.is_set or self.transmit_power_valid.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.transmit_power_valid.get_name_leafdata())
                                if (self.voltage_valid.is_set or self.voltage_valid.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.voltage_valid.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "laser-bias-valid" or name == "receive-power-valid" or name == "temperature-valid" or name == "transmit-power-valid" or name == "voltage-valid"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "laser-bias-valid"):
                                    self.laser_bias_valid = value
                                    self.laser_bias_valid.value_namespace = name_space
                                    self.laser_bias_valid.value_namespace_prefix = name_space_prefix
                                if(value_path == "receive-power-valid"):
                                    self.receive_power_valid = value
                                    self.receive_power_valid.value_namespace = name_space
                                    self.receive_power_valid.value_namespace_prefix = name_space_prefix
                                if(value_path == "temperature-valid"):
                                    self.temperature_valid = value
                                    self.temperature_valid.value_namespace = name_space
                                    self.temperature_valid.value_namespace_prefix = name_space_prefix
                                if(value_path == "transmit-power-valid"):
                                    self.transmit_power_valid = value
                                    self.transmit_power_valid.value_namespace = name_space
                                    self.transmit_power_valid.value_namespace_prefix = name_space_prefix
                                if(value_path == "voltage-valid"):
                                    self.voltage_valid = value
                                    self.voltage_valid.value_namespace = name_space
                                    self.voltage_valid.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                self.laser_bias_alarm_high.is_set or
                                self.laser_bias_alarm_low.is_set or
                                self.laser_bias_warning_high.is_set or
                                self.laser_bias_warning_low.is_set or
                                self.optical_receive_power_alarm_high.is_set or
                                self.optical_receive_power_alarm_low.is_set or
                                self.optical_receive_power_warning_high.is_set or
                                self.optical_receive_power_warning_low.is_set or
                                self.optical_transmit_power_alarm_high.is_set or
                                self.optical_transmit_power_alarm_low.is_set or
                                self.optical_transmit_power_warning_high.is_set or
                                self.optical_transmit_power_warning_low.is_set or
                                self.transceiver_temperature_alarm_high.is_set or
                                self.transceiver_temperature_alarm_low.is_set or
                                self.transceiver_temperature_warning_high.is_set or
                                self.transceiver_temperature_warning_low.is_set or
                                self.transceiver_voltage_alarm_high.is_set or
                                self.transceiver_voltage_alarm_low.is_set or
                                self.transceiver_voltage_warning_high.is_set or
                                self.transceiver_voltage_warning_low.is_set or
                                (self.field_validity is not None and self.field_validity.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.laser_bias_alarm_high.yfilter != YFilter.not_set or
                                self.laser_bias_alarm_low.yfilter != YFilter.not_set or
                                self.laser_bias_warning_high.yfilter != YFilter.not_set or
                                self.laser_bias_warning_low.yfilter != YFilter.not_set or
                                self.optical_receive_power_alarm_high.yfilter != YFilter.not_set or
                                self.optical_receive_power_alarm_low.yfilter != YFilter.not_set or
                                self.optical_receive_power_warning_high.yfilter != YFilter.not_set or
                                self.optical_receive_power_warning_low.yfilter != YFilter.not_set or
                                self.optical_transmit_power_alarm_high.yfilter != YFilter.not_set or
                                self.optical_transmit_power_alarm_low.yfilter != YFilter.not_set or
                                self.optical_transmit_power_warning_high.yfilter != YFilter.not_set or
                                self.optical_transmit_power_warning_low.yfilter != YFilter.not_set or
                                self.transceiver_temperature_alarm_high.yfilter != YFilter.not_set or
                                self.transceiver_temperature_alarm_low.yfilter != YFilter.not_set or
                                self.transceiver_temperature_warning_high.yfilter != YFilter.not_set or
                                self.transceiver_temperature_warning_low.yfilter != YFilter.not_set or
                                self.transceiver_voltage_alarm_high.yfilter != YFilter.not_set or
                                self.transceiver_voltage_alarm_low.yfilter != YFilter.not_set or
                                self.transceiver_voltage_warning_high.yfilter != YFilter.not_set or
                                self.transceiver_voltage_warning_low.yfilter != YFilter.not_set or
                                (self.field_validity is not None and self.field_validity.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "dig-opt-mon-alarm-thresholds" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.laser_bias_alarm_high.is_set or self.laser_bias_alarm_high.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.laser_bias_alarm_high.get_name_leafdata())
                            if (self.laser_bias_alarm_low.is_set or self.laser_bias_alarm_low.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.laser_bias_alarm_low.get_name_leafdata())
                            if (self.laser_bias_warning_high.is_set or self.laser_bias_warning_high.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.laser_bias_warning_high.get_name_leafdata())
                            if (self.laser_bias_warning_low.is_set or self.laser_bias_warning_low.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.laser_bias_warning_low.get_name_leafdata())
                            if (self.optical_receive_power_alarm_high.is_set or self.optical_receive_power_alarm_high.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.optical_receive_power_alarm_high.get_name_leafdata())
                            if (self.optical_receive_power_alarm_low.is_set or self.optical_receive_power_alarm_low.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.optical_receive_power_alarm_low.get_name_leafdata())
                            if (self.optical_receive_power_warning_high.is_set or self.optical_receive_power_warning_high.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.optical_receive_power_warning_high.get_name_leafdata())
                            if (self.optical_receive_power_warning_low.is_set or self.optical_receive_power_warning_low.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.optical_receive_power_warning_low.get_name_leafdata())
                            if (self.optical_transmit_power_alarm_high.is_set or self.optical_transmit_power_alarm_high.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.optical_transmit_power_alarm_high.get_name_leafdata())
                            if (self.optical_transmit_power_alarm_low.is_set or self.optical_transmit_power_alarm_low.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.optical_transmit_power_alarm_low.get_name_leafdata())
                            if (self.optical_transmit_power_warning_high.is_set or self.optical_transmit_power_warning_high.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.optical_transmit_power_warning_high.get_name_leafdata())
                            if (self.optical_transmit_power_warning_low.is_set or self.optical_transmit_power_warning_low.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.optical_transmit_power_warning_low.get_name_leafdata())
                            if (self.transceiver_temperature_alarm_high.is_set or self.transceiver_temperature_alarm_high.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.transceiver_temperature_alarm_high.get_name_leafdata())
                            if (self.transceiver_temperature_alarm_low.is_set or self.transceiver_temperature_alarm_low.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.transceiver_temperature_alarm_low.get_name_leafdata())
                            if (self.transceiver_temperature_warning_high.is_set or self.transceiver_temperature_warning_high.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.transceiver_temperature_warning_high.get_name_leafdata())
                            if (self.transceiver_temperature_warning_low.is_set or self.transceiver_temperature_warning_low.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.transceiver_temperature_warning_low.get_name_leafdata())
                            if (self.transceiver_voltage_alarm_high.is_set or self.transceiver_voltage_alarm_high.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.transceiver_voltage_alarm_high.get_name_leafdata())
                            if (self.transceiver_voltage_alarm_low.is_set or self.transceiver_voltage_alarm_low.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.transceiver_voltage_alarm_low.get_name_leafdata())
                            if (self.transceiver_voltage_warning_high.is_set or self.transceiver_voltage_warning_high.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.transceiver_voltage_warning_high.get_name_leafdata())
                            if (self.transceiver_voltage_warning_low.is_set or self.transceiver_voltage_warning_low.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.transceiver_voltage_warning_low.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "field-validity"):
                                if (self.field_validity is None):
                                    self.field_validity = EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails.DigOptMonAlarmThresholds.FieldValidity()
                                    self.field_validity.parent = self
                                    self._children_name_map["field_validity"] = "field-validity"
                                return self.field_validity

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "field-validity" or name == "laser-bias-alarm-high" or name == "laser-bias-alarm-low" or name == "laser-bias-warning-high" or name == "laser-bias-warning-low" or name == "optical-receive-power-alarm-high" or name == "optical-receive-power-alarm-low" or name == "optical-receive-power-warning-high" or name == "optical-receive-power-warning-low" or name == "optical-transmit-power-alarm-high" or name == "optical-transmit-power-alarm-low" or name == "optical-transmit-power-warning-high" or name == "optical-transmit-power-warning-low" or name == "transceiver-temperature-alarm-high" or name == "transceiver-temperature-alarm-low" or name == "transceiver-temperature-warning-high" or name == "transceiver-temperature-warning-low" or name == "transceiver-voltage-alarm-high" or name == "transceiver-voltage-alarm-low" or name == "transceiver-voltage-warning-high" or name == "transceiver-voltage-warning-low"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "laser-bias-alarm-high"):
                                self.laser_bias_alarm_high = value
                                self.laser_bias_alarm_high.value_namespace = name_space
                                self.laser_bias_alarm_high.value_namespace_prefix = name_space_prefix
                            if(value_path == "laser-bias-alarm-low"):
                                self.laser_bias_alarm_low = value
                                self.laser_bias_alarm_low.value_namespace = name_space
                                self.laser_bias_alarm_low.value_namespace_prefix = name_space_prefix
                            if(value_path == "laser-bias-warning-high"):
                                self.laser_bias_warning_high = value
                                self.laser_bias_warning_high.value_namespace = name_space
                                self.laser_bias_warning_high.value_namespace_prefix = name_space_prefix
                            if(value_path == "laser-bias-warning-low"):
                                self.laser_bias_warning_low = value
                                self.laser_bias_warning_low.value_namespace = name_space
                                self.laser_bias_warning_low.value_namespace_prefix = name_space_prefix
                            if(value_path == "optical-receive-power-alarm-high"):
                                self.optical_receive_power_alarm_high = value
                                self.optical_receive_power_alarm_high.value_namespace = name_space
                                self.optical_receive_power_alarm_high.value_namespace_prefix = name_space_prefix
                            if(value_path == "optical-receive-power-alarm-low"):
                                self.optical_receive_power_alarm_low = value
                                self.optical_receive_power_alarm_low.value_namespace = name_space
                                self.optical_receive_power_alarm_low.value_namespace_prefix = name_space_prefix
                            if(value_path == "optical-receive-power-warning-high"):
                                self.optical_receive_power_warning_high = value
                                self.optical_receive_power_warning_high.value_namespace = name_space
                                self.optical_receive_power_warning_high.value_namespace_prefix = name_space_prefix
                            if(value_path == "optical-receive-power-warning-low"):
                                self.optical_receive_power_warning_low = value
                                self.optical_receive_power_warning_low.value_namespace = name_space
                                self.optical_receive_power_warning_low.value_namespace_prefix = name_space_prefix
                            if(value_path == "optical-transmit-power-alarm-high"):
                                self.optical_transmit_power_alarm_high = value
                                self.optical_transmit_power_alarm_high.value_namespace = name_space
                                self.optical_transmit_power_alarm_high.value_namespace_prefix = name_space_prefix
                            if(value_path == "optical-transmit-power-alarm-low"):
                                self.optical_transmit_power_alarm_low = value
                                self.optical_transmit_power_alarm_low.value_namespace = name_space
                                self.optical_transmit_power_alarm_low.value_namespace_prefix = name_space_prefix
                            if(value_path == "optical-transmit-power-warning-high"):
                                self.optical_transmit_power_warning_high = value
                                self.optical_transmit_power_warning_high.value_namespace = name_space
                                self.optical_transmit_power_warning_high.value_namespace_prefix = name_space_prefix
                            if(value_path == "optical-transmit-power-warning-low"):
                                self.optical_transmit_power_warning_low = value
                                self.optical_transmit_power_warning_low.value_namespace = name_space
                                self.optical_transmit_power_warning_low.value_namespace_prefix = name_space_prefix
                            if(value_path == "transceiver-temperature-alarm-high"):
                                self.transceiver_temperature_alarm_high = value
                                self.transceiver_temperature_alarm_high.value_namespace = name_space
                                self.transceiver_temperature_alarm_high.value_namespace_prefix = name_space_prefix
                            if(value_path == "transceiver-temperature-alarm-low"):
                                self.transceiver_temperature_alarm_low = value
                                self.transceiver_temperature_alarm_low.value_namespace = name_space
                                self.transceiver_temperature_alarm_low.value_namespace_prefix = name_space_prefix
                            if(value_path == "transceiver-temperature-warning-high"):
                                self.transceiver_temperature_warning_high = value
                                self.transceiver_temperature_warning_high.value_namespace = name_space
                                self.transceiver_temperature_warning_high.value_namespace_prefix = name_space_prefix
                            if(value_path == "transceiver-temperature-warning-low"):
                                self.transceiver_temperature_warning_low = value
                                self.transceiver_temperature_warning_low.value_namespace = name_space
                                self.transceiver_temperature_warning_low.value_namespace_prefix = name_space_prefix
                            if(value_path == "transceiver-voltage-alarm-high"):
                                self.transceiver_voltage_alarm_high = value
                                self.transceiver_voltage_alarm_high.value_namespace = name_space
                                self.transceiver_voltage_alarm_high.value_namespace_prefix = name_space_prefix
                            if(value_path == "transceiver-voltage-alarm-low"):
                                self.transceiver_voltage_alarm_low = value
                                self.transceiver_voltage_alarm_low.value_namespace = name_space
                                self.transceiver_voltage_alarm_low.value_namespace_prefix = name_space_prefix
                            if(value_path == "transceiver-voltage-warning-high"):
                                self.transceiver_voltage_warning_high = value
                                self.transceiver_voltage_warning_high.value_namespace = name_space
                                self.transceiver_voltage_warning_high.value_namespace_prefix = name_space_prefix
                            if(value_path == "transceiver-voltage-warning-low"):
                                self.transceiver_voltage_warning_low = value
                                self.transceiver_voltage_warning_low.value_namespace = name_space
                                self.transceiver_voltage_warning_low.value_namespace_prefix = name_space_prefix


                    class DigOptMonAlarms(Entity):
                        """
                        Digital Optical Monitoring alarms
                        
                        .. attribute:: laser_bias_current
                        
                        	Laser Bias Current Alarm
                        	**type**\:   :py:class:`EtherDomAlarm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EtherDomAlarm>`
                        
                        .. attribute:: received_laser_power
                        
                        	Received Optical Power Alarm
                        	**type**\:   :py:class:`EtherDomAlarm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EtherDomAlarm>`
                        
                        .. attribute:: transceiver_temperature
                        
                        	Transceiver Temperature Alarm
                        	**type**\:   :py:class:`EtherDomAlarm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EtherDomAlarm>`
                        
                        .. attribute:: transceiver_voltage
                        
                        	Transceiver Voltage Alarm
                        	**type**\:   :py:class:`EtherDomAlarm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EtherDomAlarm>`
                        
                        .. attribute:: transmit_laser_power
                        
                        	Transmit Laser Power Alarm
                        	**type**\:   :py:class:`EtherDomAlarm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EtherDomAlarm>`
                        
                        

                        """

                        _prefix = 'drivers-media-eth-oper'
                        _revision = '2017-04-04'

                        def __init__(self):
                            super(EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails.DigOptMonAlarms, self).__init__()

                            self.yang_name = "dig-opt-mon-alarms"
                            self.yang_parent_name = "phy-details"

                            self.laser_bias_current = YLeaf(YType.enumeration, "laser-bias-current")

                            self.received_laser_power = YLeaf(YType.enumeration, "received-laser-power")

                            self.transceiver_temperature = YLeaf(YType.enumeration, "transceiver-temperature")

                            self.transceiver_voltage = YLeaf(YType.enumeration, "transceiver-voltage")

                            self.transmit_laser_power = YLeaf(YType.enumeration, "transmit-laser-power")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("laser_bias_current",
                                            "received_laser_power",
                                            "transceiver_temperature",
                                            "transceiver_voltage",
                                            "transmit_laser_power") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails.DigOptMonAlarms, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails.DigOptMonAlarms, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.laser_bias_current.is_set or
                                self.received_laser_power.is_set or
                                self.transceiver_temperature.is_set or
                                self.transceiver_voltage.is_set or
                                self.transmit_laser_power.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.laser_bias_current.yfilter != YFilter.not_set or
                                self.received_laser_power.yfilter != YFilter.not_set or
                                self.transceiver_temperature.yfilter != YFilter.not_set or
                                self.transceiver_voltage.yfilter != YFilter.not_set or
                                self.transmit_laser_power.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "dig-opt-mon-alarms" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.laser_bias_current.is_set or self.laser_bias_current.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.laser_bias_current.get_name_leafdata())
                            if (self.received_laser_power.is_set or self.received_laser_power.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.received_laser_power.get_name_leafdata())
                            if (self.transceiver_temperature.is_set or self.transceiver_temperature.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.transceiver_temperature.get_name_leafdata())
                            if (self.transceiver_voltage.is_set or self.transceiver_voltage.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.transceiver_voltage.get_name_leafdata())
                            if (self.transmit_laser_power.is_set or self.transmit_laser_power.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.transmit_laser_power.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "laser-bias-current" or name == "received-laser-power" or name == "transceiver-temperature" or name == "transceiver-voltage" or name == "transmit-laser-power"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "laser-bias-current"):
                                self.laser_bias_current = value
                                self.laser_bias_current.value_namespace = name_space
                                self.laser_bias_current.value_namespace_prefix = name_space_prefix
                            if(value_path == "received-laser-power"):
                                self.received_laser_power = value
                                self.received_laser_power.value_namespace = name_space
                                self.received_laser_power.value_namespace_prefix = name_space_prefix
                            if(value_path == "transceiver-temperature"):
                                self.transceiver_temperature = value
                                self.transceiver_temperature.value_namespace = name_space
                                self.transceiver_temperature.value_namespace_prefix = name_space_prefix
                            if(value_path == "transceiver-voltage"):
                                self.transceiver_voltage = value
                                self.transceiver_voltage.value_namespace = name_space
                                self.transceiver_voltage.value_namespace_prefix = name_space_prefix
                            if(value_path == "transmit-laser-power"):
                                self.transmit_laser_power = value
                                self.transmit_laser_power.value_namespace = name_space
                                self.transmit_laser_power.value_namespace_prefix = name_space_prefix


                    class Lane(Entity):
                        """
                        Digital Optical Monitoring (per lane
                        information)
                        
                        .. attribute:: center_wavelength
                        
                        	Center Wavelength (nm\*1000)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: dig_opt_mon_alarm
                        
                        	Digital Optical Monitoring alarms
                        	**type**\:   :py:class:`DigOptMonAlarm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails.Lane.DigOptMonAlarm>`
                        
                        .. attribute:: lane_id
                        
                        	Numerical identifier for this lane
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: laser_bias_current
                        
                        	Laser Bias Current (uAmps)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: received_laser_power
                        
                        	Received Optical Power (dBm\*1000)
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: transmit_laser_power
                        
                        	Transmit Laser Power (dBm\*1000)
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        

                        """

                        _prefix = 'drivers-media-eth-oper'
                        _revision = '2017-04-04'

                        def __init__(self):
                            super(EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails.Lane, self).__init__()

                            self.yang_name = "lane"
                            self.yang_parent_name = "phy-details"

                            self.center_wavelength = YLeaf(YType.uint32, "center-wavelength")

                            self.lane_id = YLeaf(YType.uint32, "lane-id")

                            self.laser_bias_current = YLeaf(YType.uint32, "laser-bias-current")

                            self.received_laser_power = YLeaf(YType.int32, "received-laser-power")

                            self.transmit_laser_power = YLeaf(YType.int32, "transmit-laser-power")

                            self.dig_opt_mon_alarm = EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails.Lane.DigOptMonAlarm()
                            self.dig_opt_mon_alarm.parent = self
                            self._children_name_map["dig_opt_mon_alarm"] = "dig-opt-mon-alarm"
                            self._children_yang_names.add("dig-opt-mon-alarm")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("center_wavelength",
                                            "lane_id",
                                            "laser_bias_current",
                                            "received_laser_power",
                                            "transmit_laser_power") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails.Lane, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails.Lane, self).__setattr__(name, value)


                        class DigOptMonAlarm(Entity):
                            """
                            Digital Optical Monitoring alarms
                            
                            .. attribute:: laser_bias_current
                            
                            	Laser Bias Current Alarm
                            	**type**\:   :py:class:`EtherDomAlarm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EtherDomAlarm>`
                            
                            .. attribute:: received_laser_power
                            
                            	Received Optical Power Alarm
                            	**type**\:   :py:class:`EtherDomAlarm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EtherDomAlarm>`
                            
                            .. attribute:: transmit_laser_power
                            
                            	Transmit Laser Power Alarm
                            	**type**\:   :py:class:`EtherDomAlarm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EtherDomAlarm>`
                            
                            

                            """

                            _prefix = 'drivers-media-eth-oper'
                            _revision = '2017-04-04'

                            def __init__(self):
                                super(EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails.Lane.DigOptMonAlarm, self).__init__()

                                self.yang_name = "dig-opt-mon-alarm"
                                self.yang_parent_name = "lane"

                                self.laser_bias_current = YLeaf(YType.enumeration, "laser-bias-current")

                                self.received_laser_power = YLeaf(YType.enumeration, "received-laser-power")

                                self.transmit_laser_power = YLeaf(YType.enumeration, "transmit-laser-power")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("laser_bias_current",
                                                "received_laser_power",
                                                "transmit_laser_power") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails.Lane.DigOptMonAlarm, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails.Lane.DigOptMonAlarm, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.laser_bias_current.is_set or
                                    self.received_laser_power.is_set or
                                    self.transmit_laser_power.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.laser_bias_current.yfilter != YFilter.not_set or
                                    self.received_laser_power.yfilter != YFilter.not_set or
                                    self.transmit_laser_power.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "dig-opt-mon-alarm" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.laser_bias_current.is_set or self.laser_bias_current.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.laser_bias_current.get_name_leafdata())
                                if (self.received_laser_power.is_set or self.received_laser_power.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.received_laser_power.get_name_leafdata())
                                if (self.transmit_laser_power.is_set or self.transmit_laser_power.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.transmit_laser_power.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "laser-bias-current" or name == "received-laser-power" or name == "transmit-laser-power"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "laser-bias-current"):
                                    self.laser_bias_current = value
                                    self.laser_bias_current.value_namespace = name_space
                                    self.laser_bias_current.value_namespace_prefix = name_space_prefix
                                if(value_path == "received-laser-power"):
                                    self.received_laser_power = value
                                    self.received_laser_power.value_namespace = name_space
                                    self.received_laser_power.value_namespace_prefix = name_space_prefix
                                if(value_path == "transmit-laser-power"):
                                    self.transmit_laser_power = value
                                    self.transmit_laser_power.value_namespace = name_space
                                    self.transmit_laser_power.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                self.center_wavelength.is_set or
                                self.lane_id.is_set or
                                self.laser_bias_current.is_set or
                                self.received_laser_power.is_set or
                                self.transmit_laser_power.is_set or
                                (self.dig_opt_mon_alarm is not None and self.dig_opt_mon_alarm.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.center_wavelength.yfilter != YFilter.not_set or
                                self.lane_id.yfilter != YFilter.not_set or
                                self.laser_bias_current.yfilter != YFilter.not_set or
                                self.received_laser_power.yfilter != YFilter.not_set or
                                self.transmit_laser_power.yfilter != YFilter.not_set or
                                (self.dig_opt_mon_alarm is not None and self.dig_opt_mon_alarm.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "lane" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.center_wavelength.is_set or self.center_wavelength.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.center_wavelength.get_name_leafdata())
                            if (self.lane_id.is_set or self.lane_id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.lane_id.get_name_leafdata())
                            if (self.laser_bias_current.is_set or self.laser_bias_current.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.laser_bias_current.get_name_leafdata())
                            if (self.received_laser_power.is_set or self.received_laser_power.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.received_laser_power.get_name_leafdata())
                            if (self.transmit_laser_power.is_set or self.transmit_laser_power.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.transmit_laser_power.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "dig-opt-mon-alarm"):
                                if (self.dig_opt_mon_alarm is None):
                                    self.dig_opt_mon_alarm = EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails.Lane.DigOptMonAlarm()
                                    self.dig_opt_mon_alarm.parent = self
                                    self._children_name_map["dig_opt_mon_alarm"] = "dig-opt-mon-alarm"
                                return self.dig_opt_mon_alarm

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "dig-opt-mon-alarm" or name == "center-wavelength" or name == "lane-id" or name == "laser-bias-current" or name == "received-laser-power" or name == "transmit-laser-power"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "center-wavelength"):
                                self.center_wavelength = value
                                self.center_wavelength.value_namespace = name_space
                                self.center_wavelength.value_namespace_prefix = name_space_prefix
                            if(value_path == "lane-id"):
                                self.lane_id = value
                                self.lane_id.value_namespace = name_space
                                self.lane_id.value_namespace_prefix = name_space_prefix
                            if(value_path == "laser-bias-current"):
                                self.laser_bias_current = value
                                self.laser_bias_current.value_namespace = name_space
                                self.laser_bias_current.value_namespace_prefix = name_space_prefix
                            if(value_path == "received-laser-power"):
                                self.received_laser_power = value
                                self.received_laser_power.value_namespace = name_space
                                self.received_laser_power.value_namespace_prefix = name_space_prefix
                            if(value_path == "transmit-laser-power"):
                                self.transmit_laser_power = value
                                self.transmit_laser_power.value_namespace = name_space
                                self.transmit_laser_power.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.lane:
                            if (c.has_data()):
                                return True
                        return (
                            self.optics_type.is_set or
                            self.optics_wavelength.is_set or
                            self.revision_number.is_set or
                            self.transceiver_rx_power.is_set or
                            self.transceiver_temperature.is_set or
                            self.transceiver_tx_bias.is_set or
                            self.transceiver_tx_power.is_set or
                            self.transceiver_voltage.is_set or
                            self.vendor.is_set or
                            self.vendor_part_number.is_set or
                            self.vendor_serial_number.is_set or
                            (self.dig_opt_mon_alarm_thresholds is not None and self.dig_opt_mon_alarm_thresholds.has_data()) or
                            (self.dig_opt_mon_alarms is not None and self.dig_opt_mon_alarms.has_data()) or
                            (self.lane_field_validity is not None and self.lane_field_validity.has_data()))

                    def has_operation(self):
                        for c in self.lane:
                            if (c.has_operation()):
                                return True
                        return (
                            self.yfilter != YFilter.not_set or
                            self.optics_type.yfilter != YFilter.not_set or
                            self.optics_wavelength.yfilter != YFilter.not_set or
                            self.revision_number.yfilter != YFilter.not_set or
                            self.transceiver_rx_power.yfilter != YFilter.not_set or
                            self.transceiver_temperature.yfilter != YFilter.not_set or
                            self.transceiver_tx_bias.yfilter != YFilter.not_set or
                            self.transceiver_tx_power.yfilter != YFilter.not_set or
                            self.transceiver_voltage.yfilter != YFilter.not_set or
                            self.vendor.yfilter != YFilter.not_set or
                            self.vendor_part_number.yfilter != YFilter.not_set or
                            self.vendor_serial_number.yfilter != YFilter.not_set or
                            (self.dig_opt_mon_alarm_thresholds is not None and self.dig_opt_mon_alarm_thresholds.has_operation()) or
                            (self.dig_opt_mon_alarms is not None and self.dig_opt_mon_alarms.has_operation()) or
                            (self.lane_field_validity is not None and self.lane_field_validity.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "phy-details" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.optics_type.is_set or self.optics_type.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.optics_type.get_name_leafdata())
                        if (self.optics_wavelength.is_set or self.optics_wavelength.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.optics_wavelength.get_name_leafdata())
                        if (self.revision_number.is_set or self.revision_number.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.revision_number.get_name_leafdata())
                        if (self.transceiver_rx_power.is_set or self.transceiver_rx_power.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.transceiver_rx_power.get_name_leafdata())
                        if (self.transceiver_temperature.is_set or self.transceiver_temperature.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.transceiver_temperature.get_name_leafdata())
                        if (self.transceiver_tx_bias.is_set or self.transceiver_tx_bias.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.transceiver_tx_bias.get_name_leafdata())
                        if (self.transceiver_tx_power.is_set or self.transceiver_tx_power.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.transceiver_tx_power.get_name_leafdata())
                        if (self.transceiver_voltage.is_set or self.transceiver_voltage.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.transceiver_voltage.get_name_leafdata())
                        if (self.vendor.is_set or self.vendor.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.vendor.get_name_leafdata())
                        if (self.vendor_part_number.is_set or self.vendor_part_number.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.vendor_part_number.get_name_leafdata())
                        if (self.vendor_serial_number.is_set or self.vendor_serial_number.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.vendor_serial_number.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "dig-opt-mon-alarm-thresholds"):
                            if (self.dig_opt_mon_alarm_thresholds is None):
                                self.dig_opt_mon_alarm_thresholds = EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails.DigOptMonAlarmThresholds()
                                self.dig_opt_mon_alarm_thresholds.parent = self
                                self._children_name_map["dig_opt_mon_alarm_thresholds"] = "dig-opt-mon-alarm-thresholds"
                            return self.dig_opt_mon_alarm_thresholds

                        if (child_yang_name == "dig-opt-mon-alarms"):
                            if (self.dig_opt_mon_alarms is None):
                                self.dig_opt_mon_alarms = EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails.DigOptMonAlarms()
                                self.dig_opt_mon_alarms.parent = self
                                self._children_name_map["dig_opt_mon_alarms"] = "dig-opt-mon-alarms"
                            return self.dig_opt_mon_alarms

                        if (child_yang_name == "lane"):
                            for c in self.lane:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails.Lane()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.lane.append(c)
                            return c

                        if (child_yang_name == "lane-field-validity"):
                            if (self.lane_field_validity is None):
                                self.lane_field_validity = EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails.LaneFieldValidity()
                                self.lane_field_validity.parent = self
                                self._children_name_map["lane_field_validity"] = "lane-field-validity"
                            return self.lane_field_validity

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "dig-opt-mon-alarm-thresholds" or name == "dig-opt-mon-alarms" or name == "lane" or name == "lane-field-validity" or name == "optics-type" or name == "optics-wavelength" or name == "revision-number" or name == "transceiver-rx-power" or name == "transceiver-temperature" or name == "transceiver-tx-bias" or name == "transceiver-tx-power" or name == "transceiver-voltage" or name == "vendor" or name == "vendor-part-number" or name == "vendor-serial-number"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "optics-type"):
                            self.optics_type = value
                            self.optics_type.value_namespace = name_space
                            self.optics_type.value_namespace_prefix = name_space_prefix
                        if(value_path == "optics-wavelength"):
                            self.optics_wavelength = value
                            self.optics_wavelength.value_namespace = name_space
                            self.optics_wavelength.value_namespace_prefix = name_space_prefix
                        if(value_path == "revision-number"):
                            self.revision_number = value
                            self.revision_number.value_namespace = name_space
                            self.revision_number.value_namespace_prefix = name_space_prefix
                        if(value_path == "transceiver-rx-power"):
                            self.transceiver_rx_power = value
                            self.transceiver_rx_power.value_namespace = name_space
                            self.transceiver_rx_power.value_namespace_prefix = name_space_prefix
                        if(value_path == "transceiver-temperature"):
                            self.transceiver_temperature = value
                            self.transceiver_temperature.value_namespace = name_space
                            self.transceiver_temperature.value_namespace_prefix = name_space_prefix
                        if(value_path == "transceiver-tx-bias"):
                            self.transceiver_tx_bias = value
                            self.transceiver_tx_bias.value_namespace = name_space
                            self.transceiver_tx_bias.value_namespace_prefix = name_space_prefix
                        if(value_path == "transceiver-tx-power"):
                            self.transceiver_tx_power = value
                            self.transceiver_tx_power.value_namespace = name_space
                            self.transceiver_tx_power.value_namespace_prefix = name_space_prefix
                        if(value_path == "transceiver-voltage"):
                            self.transceiver_voltage = value
                            self.transceiver_voltage.value_namespace = name_space
                            self.transceiver_voltage.value_namespace_prefix = name_space_prefix
                        if(value_path == "vendor"):
                            self.vendor = value
                            self.vendor.value_namespace = name_space
                            self.vendor.value_namespace_prefix = name_space_prefix
                        if(value_path == "vendor-part-number"):
                            self.vendor_part_number = value
                            self.vendor_part_number.value_namespace = name_space
                            self.vendor_part_number.value_namespace_prefix = name_space_prefix
                        if(value_path == "vendor-serial-number"):
                            self.vendor_serial_number = value
                            self.vendor_serial_number.value_namespace = name_space
                            self.vendor_serial_number.value_namespace_prefix = name_space_prefix


                class FecDetails(Entity):
                    """
                    Forward Error Correction information
                    
                    .. attribute:: corrected_codeword_count
                    
                    	Corrected codeword error count
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: fec
                    
                    	Port operational FEC type
                    	**type**\:   :py:class:`EthernetFec <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetFec>`
                    
                    .. attribute:: uncorrected_codeword_count
                    
                    	Uncorrected codeword error count
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    

                    """

                    _prefix = 'drivers-media-eth-oper'
                    _revision = '2017-04-04'

                    def __init__(self):
                        super(EthernetInterface.Interfaces.Interface.PhyInfo.FecDetails, self).__init__()

                        self.yang_name = "fec-details"
                        self.yang_parent_name = "phy-info"

                        self.corrected_codeword_count = YLeaf(YType.uint64, "corrected-codeword-count")

                        self.fec = YLeaf(YType.enumeration, "fec")

                        self.uncorrected_codeword_count = YLeaf(YType.uint64, "uncorrected-codeword-count")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("corrected_codeword_count",
                                        "fec",
                                        "uncorrected_codeword_count") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(EthernetInterface.Interfaces.Interface.PhyInfo.FecDetails, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(EthernetInterface.Interfaces.Interface.PhyInfo.FecDetails, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.corrected_codeword_count.is_set or
                            self.fec.is_set or
                            self.uncorrected_codeword_count.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.corrected_codeword_count.yfilter != YFilter.not_set or
                            self.fec.yfilter != YFilter.not_set or
                            self.uncorrected_codeword_count.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "fec-details" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.corrected_codeword_count.is_set or self.corrected_codeword_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.corrected_codeword_count.get_name_leafdata())
                        if (self.fec.is_set or self.fec.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.fec.get_name_leafdata())
                        if (self.uncorrected_codeword_count.is_set or self.uncorrected_codeword_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.uncorrected_codeword_count.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "corrected-codeword-count" or name == "fec" or name == "uncorrected-codeword-count"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "corrected-codeword-count"):
                            self.corrected_codeword_count = value
                            self.corrected_codeword_count.value_namespace = name_space
                            self.corrected_codeword_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "fec"):
                            self.fec = value
                            self.fec.value_namespace = name_space
                            self.fec.value_namespace_prefix = name_space_prefix
                        if(value_path == "uncorrected-codeword-count"):
                            self.uncorrected_codeword_count = value
                            self.uncorrected_codeword_count.value_namespace = name_space
                            self.uncorrected_codeword_count.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.loopback.is_set or
                        self.media_type.is_set or
                        self.phy_present.is_set or
                        (self.fec_details is not None and self.fec_details.has_data()) or
                        (self.phy_details is not None and self.phy_details.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.loopback.yfilter != YFilter.not_set or
                        self.media_type.yfilter != YFilter.not_set or
                        self.phy_present.yfilter != YFilter.not_set or
                        (self.fec_details is not None and self.fec_details.has_operation()) or
                        (self.phy_details is not None and self.phy_details.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "phy-info" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.loopback.is_set or self.loopback.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.loopback.get_name_leafdata())
                    if (self.media_type.is_set or self.media_type.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.media_type.get_name_leafdata())
                    if (self.phy_present.is_set or self.phy_present.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.phy_present.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "fec-details"):
                        if (self.fec_details is None):
                            self.fec_details = EthernetInterface.Interfaces.Interface.PhyInfo.FecDetails()
                            self.fec_details.parent = self
                            self._children_name_map["fec_details"] = "fec-details"
                        return self.fec_details

                    if (child_yang_name == "phy-details"):
                        if (self.phy_details is None):
                            self.phy_details = EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails()
                            self.phy_details.parent = self
                            self._children_name_map["phy_details"] = "phy-details"
                        return self.phy_details

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "fec-details" or name == "phy-details" or name == "loopback" or name == "media-type" or name == "phy-present"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "loopback"):
                        self.loopback = value
                        self.loopback.value_namespace = name_space
                        self.loopback.value_namespace_prefix = name_space_prefix
                    if(value_path == "media-type"):
                        self.media_type = value
                        self.media_type.value_namespace = name_space
                        self.media_type.value_namespace_prefix = name_space_prefix
                    if(value_path == "phy-present"):
                        self.phy_present = value
                        self.phy_present.value_namespace = name_space
                        self.phy_present.value_namespace_prefix = name_space_prefix


            class Layer1Info(Entity):
                """
                Layer 1 information
                
                .. attribute:: autoneg
                
                	Port autonegotiation configuration settings
                	**type**\:   :py:class:`Autoneg <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Interfaces.Interface.Layer1Info.Autoneg>`
                
                .. attribute:: bandwidth
                
                	Port operational bandwidth
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: bandwidth_utilization
                
                	Bandwidth utilization (hundredths of a percent)
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: percentage
                
                .. attribute:: ber_monitoring
                
                	BER monitoring details
                	**type**\:   :py:class:`BerMonitoring <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Interfaces.Interface.Layer1Info.BerMonitoring>`
                
                .. attribute:: current_alarms
                
                	Current alarms
                	**type**\:   :py:class:`CurrentAlarms <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Interfaces.Interface.Layer1Info.CurrentAlarms>`
                
                .. attribute:: duplex
                
                	Port operational duplexity
                	**type**\:   :py:class:`EthernetDuplex <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetDuplex>`
                
                .. attribute:: error_counts
                
                	Statistics for detected errors
                	**type**\:   :py:class:`ErrorCounts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Interfaces.Interface.Layer1Info.ErrorCounts>`
                
                .. attribute:: flowcontrol
                
                	Port operational flow control
                	**type**\:   :py:class:`EtherFlowcontrol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EtherFlowcontrol>`
                
                .. attribute:: ipg
                
                	Port operational inter\-packet\-gap
                	**type**\:   :py:class:`EthernetIpg <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetIpg>`
                
                .. attribute:: laser_squelch_enabled
                
                	Laser Squelch \- TRUE if enabled
                	**type**\:  bool
                
                .. attribute:: led_state
                
                	State of the LED
                	**type**\:   :py:class:`EtherLedState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EtherLedState>`
                
                .. attribute:: link_state
                
                	Link state
                	**type**\:   :py:class:`EtherLinkState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EtherLinkState>`
                
                .. attribute:: opd_monitoring
                
                	OPD monitoring details
                	**type**\:   :py:class:`OpdMonitoring <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Interfaces.Interface.Layer1Info.OpdMonitoring>`
                
                .. attribute:: pfc_info
                
                	Priority flow control information
                	**type**\:   :py:class:`PfcInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Interfaces.Interface.Layer1Info.PfcInfo>`
                
                .. attribute:: previous_alarms
                
                	Previous alarms
                	**type**\:   :py:class:`PreviousAlarms <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Interfaces.Interface.Layer1Info.PreviousAlarms>`
                
                .. attribute:: speed
                
                	Port operational speed
                	**type**\:   :py:class:`EthernetSpeed <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetSpeed>`
                
                

                """

                _prefix = 'drivers-media-eth-oper'
                _revision = '2017-04-04'

                def __init__(self):
                    super(EthernetInterface.Interfaces.Interface.Layer1Info, self).__init__()

                    self.yang_name = "layer1-info"
                    self.yang_parent_name = "interface"

                    self.bandwidth = YLeaf(YType.uint64, "bandwidth")

                    self.bandwidth_utilization = YLeaf(YType.uint32, "bandwidth-utilization")

                    self.duplex = YLeaf(YType.enumeration, "duplex")

                    self.flowcontrol = YLeaf(YType.enumeration, "flowcontrol")

                    self.ipg = YLeaf(YType.enumeration, "ipg")

                    self.laser_squelch_enabled = YLeaf(YType.boolean, "laser-squelch-enabled")

                    self.led_state = YLeaf(YType.enumeration, "led-state")

                    self.link_state = YLeaf(YType.enumeration, "link-state")

                    self.speed = YLeaf(YType.enumeration, "speed")

                    self.autoneg = EthernetInterface.Interfaces.Interface.Layer1Info.Autoneg()
                    self.autoneg.parent = self
                    self._children_name_map["autoneg"] = "autoneg"
                    self._children_yang_names.add("autoneg")

                    self.ber_monitoring = EthernetInterface.Interfaces.Interface.Layer1Info.BerMonitoring()
                    self.ber_monitoring.parent = self
                    self._children_name_map["ber_monitoring"] = "ber-monitoring"
                    self._children_yang_names.add("ber-monitoring")

                    self.current_alarms = EthernetInterface.Interfaces.Interface.Layer1Info.CurrentAlarms()
                    self.current_alarms.parent = self
                    self._children_name_map["current_alarms"] = "current-alarms"
                    self._children_yang_names.add("current-alarms")

                    self.error_counts = EthernetInterface.Interfaces.Interface.Layer1Info.ErrorCounts()
                    self.error_counts.parent = self
                    self._children_name_map["error_counts"] = "error-counts"
                    self._children_yang_names.add("error-counts")

                    self.opd_monitoring = EthernetInterface.Interfaces.Interface.Layer1Info.OpdMonitoring()
                    self.opd_monitoring.parent = self
                    self._children_name_map["opd_monitoring"] = "opd-monitoring"
                    self._children_yang_names.add("opd-monitoring")

                    self.pfc_info = EthernetInterface.Interfaces.Interface.Layer1Info.PfcInfo()
                    self.pfc_info.parent = self
                    self._children_name_map["pfc_info"] = "pfc-info"
                    self._children_yang_names.add("pfc-info")

                    self.previous_alarms = EthernetInterface.Interfaces.Interface.Layer1Info.PreviousAlarms()
                    self.previous_alarms.parent = self
                    self._children_name_map["previous_alarms"] = "previous-alarms"
                    self._children_yang_names.add("previous-alarms")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("bandwidth",
                                    "bandwidth_utilization",
                                    "duplex",
                                    "flowcontrol",
                                    "ipg",
                                    "laser_squelch_enabled",
                                    "led_state",
                                    "link_state",
                                    "speed") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(EthernetInterface.Interfaces.Interface.Layer1Info, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(EthernetInterface.Interfaces.Interface.Layer1Info, self).__setattr__(name, value)


                class Autoneg(Entity):
                    """
                    Port autonegotiation configuration settings
                    
                    .. attribute:: autoneg_enabled
                    
                    	TRUE if autonegotiation is enabled
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: config_override
                    
                    	If true, configuration overrides negotiated settings.  If false, negotiated settings in effect
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: duplex
                    
                    	Restricted duplex (if relevant bit is set in mask)
                    	**type**\:   :py:class:`EthernetDuplex <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetDuplex>`
                    
                    .. attribute:: fec
                    
                    	Restricted FEC (if revelevant bit is set in mask)
                    	**type**\:   :py:class:`EthernetFec <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetFec>`
                    
                    .. attribute:: flowcontrol
                    
                    	Restricted flowcontrol (if relevant bit is set in mask)
                    	**type**\:   :py:class:`EtherFlowcontrol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EtherFlowcontrol>`
                    
                    .. attribute:: mask
                    
                    	Validity mask\: 0x1 speed, 0x2 duplex, 0x4 flowcontrol, 0x8 fec
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: speed
                    
                    	Restricted speed (if relevant bit is set in mask)
                    	**type**\:   :py:class:`EthernetSpeed <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetSpeed>`
                    
                    

                    """

                    _prefix = 'drivers-media-eth-oper'
                    _revision = '2017-04-04'

                    def __init__(self):
                        super(EthernetInterface.Interfaces.Interface.Layer1Info.Autoneg, self).__init__()

                        self.yang_name = "autoneg"
                        self.yang_parent_name = "layer1-info"

                        self.autoneg_enabled = YLeaf(YType.int32, "autoneg-enabled")

                        self.config_override = YLeaf(YType.int32, "config-override")

                        self.duplex = YLeaf(YType.enumeration, "duplex")

                        self.fec = YLeaf(YType.enumeration, "fec")

                        self.flowcontrol = YLeaf(YType.enumeration, "flowcontrol")

                        self.mask = YLeaf(YType.uint32, "mask")

                        self.speed = YLeaf(YType.enumeration, "speed")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("autoneg_enabled",
                                        "config_override",
                                        "duplex",
                                        "fec",
                                        "flowcontrol",
                                        "mask",
                                        "speed") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(EthernetInterface.Interfaces.Interface.Layer1Info.Autoneg, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(EthernetInterface.Interfaces.Interface.Layer1Info.Autoneg, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.autoneg_enabled.is_set or
                            self.config_override.is_set or
                            self.duplex.is_set or
                            self.fec.is_set or
                            self.flowcontrol.is_set or
                            self.mask.is_set or
                            self.speed.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.autoneg_enabled.yfilter != YFilter.not_set or
                            self.config_override.yfilter != YFilter.not_set or
                            self.duplex.yfilter != YFilter.not_set or
                            self.fec.yfilter != YFilter.not_set or
                            self.flowcontrol.yfilter != YFilter.not_set or
                            self.mask.yfilter != YFilter.not_set or
                            self.speed.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "autoneg" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.autoneg_enabled.is_set or self.autoneg_enabled.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.autoneg_enabled.get_name_leafdata())
                        if (self.config_override.is_set or self.config_override.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.config_override.get_name_leafdata())
                        if (self.duplex.is_set or self.duplex.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.duplex.get_name_leafdata())
                        if (self.fec.is_set or self.fec.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.fec.get_name_leafdata())
                        if (self.flowcontrol.is_set or self.flowcontrol.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.flowcontrol.get_name_leafdata())
                        if (self.mask.is_set or self.mask.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.mask.get_name_leafdata())
                        if (self.speed.is_set or self.speed.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.speed.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "autoneg-enabled" or name == "config-override" or name == "duplex" or name == "fec" or name == "flowcontrol" or name == "mask" or name == "speed"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "autoneg-enabled"):
                            self.autoneg_enabled = value
                            self.autoneg_enabled.value_namespace = name_space
                            self.autoneg_enabled.value_namespace_prefix = name_space_prefix
                        if(value_path == "config-override"):
                            self.config_override = value
                            self.config_override.value_namespace = name_space
                            self.config_override.value_namespace_prefix = name_space_prefix
                        if(value_path == "duplex"):
                            self.duplex = value
                            self.duplex.value_namespace = name_space
                            self.duplex.value_namespace_prefix = name_space_prefix
                        if(value_path == "fec"):
                            self.fec = value
                            self.fec.value_namespace = name_space
                            self.fec.value_namespace_prefix = name_space_prefix
                        if(value_path == "flowcontrol"):
                            self.flowcontrol = value
                            self.flowcontrol.value_namespace = name_space
                            self.flowcontrol.value_namespace_prefix = name_space_prefix
                        if(value_path == "mask"):
                            self.mask = value
                            self.mask.value_namespace = name_space
                            self.mask.value_namespace_prefix = name_space_prefix
                        if(value_path == "speed"):
                            self.speed = value
                            self.speed.value_namespace = name_space
                            self.speed.value_namespace_prefix = name_space_prefix


                class CurrentAlarms(Entity):
                    """
                    Current alarms
                    
                    .. attribute:: hi_ber_alarm
                    
                    	Hi BER
                    	**type**\:   :py:class:`EthCtrlrAlarmState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthCtrlrAlarmState>`
                    
                    .. attribute:: local_fault_alarm
                    
                    	Local Fault
                    	**type**\:   :py:class:`EthCtrlrAlarmState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthCtrlrAlarmState>`
                    
                    .. attribute:: loss_of_synchronization_data_alarm
                    
                    	Loss of Synchronization Data
                    	**type**\:   :py:class:`EthCtrlrAlarmState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthCtrlrAlarmState>`
                    
                    .. attribute:: pcs_loss_of_block_lock_alarm
                    
                    	PCS Loss of Block Lock
                    	**type**\:   :py:class:`EthCtrlrAlarmState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthCtrlrAlarmState>`
                    
                    .. attribute:: received_loss_of_signal_alarm
                    
                    	Received Loss of Signal
                    	**type**\:   :py:class:`EthCtrlrAlarmState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthCtrlrAlarmState>`
                    
                    .. attribute:: remote_fault_alarm
                    
                    	Remote Fault
                    	**type**\:   :py:class:`EthCtrlrAlarmState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthCtrlrAlarmState>`
                    
                    .. attribute:: rx_opd_alarm
                    
                    	Rx OPD Alarm
                    	**type**\:   :py:class:`EthCtrlrAlarmState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthCtrlrAlarmState>`
                    
                    .. attribute:: sd_ber_alarm
                    
                    	SD BER
                    	**type**\:   :py:class:`EthCtrlrAlarmState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthCtrlrAlarmState>`
                    
                    .. attribute:: sf_ber_alarm
                    
                    	SF BER
                    	**type**\:   :py:class:`EthCtrlrAlarmState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthCtrlrAlarmState>`
                    
                    .. attribute:: squelch_alarm
                    
                    	Squelch
                    	**type**\:   :py:class:`EthCtrlrAlarmState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthCtrlrAlarmState>`
                    
                    

                    """

                    _prefix = 'drivers-media-eth-oper'
                    _revision = '2017-04-04'

                    def __init__(self):
                        super(EthernetInterface.Interfaces.Interface.Layer1Info.CurrentAlarms, self).__init__()

                        self.yang_name = "current-alarms"
                        self.yang_parent_name = "layer1-info"

                        self.hi_ber_alarm = YLeaf(YType.enumeration, "hi-ber-alarm")

                        self.local_fault_alarm = YLeaf(YType.enumeration, "local-fault-alarm")

                        self.loss_of_synchronization_data_alarm = YLeaf(YType.enumeration, "loss-of-synchronization-data-alarm")

                        self.pcs_loss_of_block_lock_alarm = YLeaf(YType.enumeration, "pcs-loss-of-block-lock-alarm")

                        self.received_loss_of_signal_alarm = YLeaf(YType.enumeration, "received-loss-of-signal-alarm")

                        self.remote_fault_alarm = YLeaf(YType.enumeration, "remote-fault-alarm")

                        self.rx_opd_alarm = YLeaf(YType.enumeration, "rx-opd-alarm")

                        self.sd_ber_alarm = YLeaf(YType.enumeration, "sd-ber-alarm")

                        self.sf_ber_alarm = YLeaf(YType.enumeration, "sf-ber-alarm")

                        self.squelch_alarm = YLeaf(YType.enumeration, "squelch-alarm")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("hi_ber_alarm",
                                        "local_fault_alarm",
                                        "loss_of_synchronization_data_alarm",
                                        "pcs_loss_of_block_lock_alarm",
                                        "received_loss_of_signal_alarm",
                                        "remote_fault_alarm",
                                        "rx_opd_alarm",
                                        "sd_ber_alarm",
                                        "sf_ber_alarm",
                                        "squelch_alarm") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(EthernetInterface.Interfaces.Interface.Layer1Info.CurrentAlarms, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(EthernetInterface.Interfaces.Interface.Layer1Info.CurrentAlarms, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.hi_ber_alarm.is_set or
                            self.local_fault_alarm.is_set or
                            self.loss_of_synchronization_data_alarm.is_set or
                            self.pcs_loss_of_block_lock_alarm.is_set or
                            self.received_loss_of_signal_alarm.is_set or
                            self.remote_fault_alarm.is_set or
                            self.rx_opd_alarm.is_set or
                            self.sd_ber_alarm.is_set or
                            self.sf_ber_alarm.is_set or
                            self.squelch_alarm.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.hi_ber_alarm.yfilter != YFilter.not_set or
                            self.local_fault_alarm.yfilter != YFilter.not_set or
                            self.loss_of_synchronization_data_alarm.yfilter != YFilter.not_set or
                            self.pcs_loss_of_block_lock_alarm.yfilter != YFilter.not_set or
                            self.received_loss_of_signal_alarm.yfilter != YFilter.not_set or
                            self.remote_fault_alarm.yfilter != YFilter.not_set or
                            self.rx_opd_alarm.yfilter != YFilter.not_set or
                            self.sd_ber_alarm.yfilter != YFilter.not_set or
                            self.sf_ber_alarm.yfilter != YFilter.not_set or
                            self.squelch_alarm.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "current-alarms" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.hi_ber_alarm.is_set or self.hi_ber_alarm.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.hi_ber_alarm.get_name_leafdata())
                        if (self.local_fault_alarm.is_set or self.local_fault_alarm.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.local_fault_alarm.get_name_leafdata())
                        if (self.loss_of_synchronization_data_alarm.is_set or self.loss_of_synchronization_data_alarm.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.loss_of_synchronization_data_alarm.get_name_leafdata())
                        if (self.pcs_loss_of_block_lock_alarm.is_set or self.pcs_loss_of_block_lock_alarm.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.pcs_loss_of_block_lock_alarm.get_name_leafdata())
                        if (self.received_loss_of_signal_alarm.is_set or self.received_loss_of_signal_alarm.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.received_loss_of_signal_alarm.get_name_leafdata())
                        if (self.remote_fault_alarm.is_set or self.remote_fault_alarm.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.remote_fault_alarm.get_name_leafdata())
                        if (self.rx_opd_alarm.is_set or self.rx_opd_alarm.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.rx_opd_alarm.get_name_leafdata())
                        if (self.sd_ber_alarm.is_set or self.sd_ber_alarm.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.sd_ber_alarm.get_name_leafdata())
                        if (self.sf_ber_alarm.is_set or self.sf_ber_alarm.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.sf_ber_alarm.get_name_leafdata())
                        if (self.squelch_alarm.is_set or self.squelch_alarm.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.squelch_alarm.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "hi-ber-alarm" or name == "local-fault-alarm" or name == "loss-of-synchronization-data-alarm" or name == "pcs-loss-of-block-lock-alarm" or name == "received-loss-of-signal-alarm" or name == "remote-fault-alarm" or name == "rx-opd-alarm" or name == "sd-ber-alarm" or name == "sf-ber-alarm" or name == "squelch-alarm"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "hi-ber-alarm"):
                            self.hi_ber_alarm = value
                            self.hi_ber_alarm.value_namespace = name_space
                            self.hi_ber_alarm.value_namespace_prefix = name_space_prefix
                        if(value_path == "local-fault-alarm"):
                            self.local_fault_alarm = value
                            self.local_fault_alarm.value_namespace = name_space
                            self.local_fault_alarm.value_namespace_prefix = name_space_prefix
                        if(value_path == "loss-of-synchronization-data-alarm"):
                            self.loss_of_synchronization_data_alarm = value
                            self.loss_of_synchronization_data_alarm.value_namespace = name_space
                            self.loss_of_synchronization_data_alarm.value_namespace_prefix = name_space_prefix
                        if(value_path == "pcs-loss-of-block-lock-alarm"):
                            self.pcs_loss_of_block_lock_alarm = value
                            self.pcs_loss_of_block_lock_alarm.value_namespace = name_space
                            self.pcs_loss_of_block_lock_alarm.value_namespace_prefix = name_space_prefix
                        if(value_path == "received-loss-of-signal-alarm"):
                            self.received_loss_of_signal_alarm = value
                            self.received_loss_of_signal_alarm.value_namespace = name_space
                            self.received_loss_of_signal_alarm.value_namespace_prefix = name_space_prefix
                        if(value_path == "remote-fault-alarm"):
                            self.remote_fault_alarm = value
                            self.remote_fault_alarm.value_namespace = name_space
                            self.remote_fault_alarm.value_namespace_prefix = name_space_prefix
                        if(value_path == "rx-opd-alarm"):
                            self.rx_opd_alarm = value
                            self.rx_opd_alarm.value_namespace = name_space
                            self.rx_opd_alarm.value_namespace_prefix = name_space_prefix
                        if(value_path == "sd-ber-alarm"):
                            self.sd_ber_alarm = value
                            self.sd_ber_alarm.value_namespace = name_space
                            self.sd_ber_alarm.value_namespace_prefix = name_space_prefix
                        if(value_path == "sf-ber-alarm"):
                            self.sf_ber_alarm = value
                            self.sf_ber_alarm.value_namespace = name_space
                            self.sf_ber_alarm.value_namespace_prefix = name_space_prefix
                        if(value_path == "squelch-alarm"):
                            self.squelch_alarm = value
                            self.squelch_alarm.value_namespace = name_space
                            self.squelch_alarm.value_namespace_prefix = name_space_prefix


                class PreviousAlarms(Entity):
                    """
                    Previous alarms
                    
                    .. attribute:: hi_ber_alarm
                    
                    	Hi BER
                    	**type**\:   :py:class:`EthCtrlrAlarmState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthCtrlrAlarmState>`
                    
                    .. attribute:: local_fault_alarm
                    
                    	Local Fault
                    	**type**\:   :py:class:`EthCtrlrAlarmState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthCtrlrAlarmState>`
                    
                    .. attribute:: loss_of_synchronization_data_alarm
                    
                    	Loss of Synchronization Data
                    	**type**\:   :py:class:`EthCtrlrAlarmState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthCtrlrAlarmState>`
                    
                    .. attribute:: pcs_loss_of_block_lock_alarm
                    
                    	PCS Loss of Block Lock
                    	**type**\:   :py:class:`EthCtrlrAlarmState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthCtrlrAlarmState>`
                    
                    .. attribute:: received_loss_of_signal_alarm
                    
                    	Received Loss of Signal
                    	**type**\:   :py:class:`EthCtrlrAlarmState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthCtrlrAlarmState>`
                    
                    .. attribute:: remote_fault_alarm
                    
                    	Remote Fault
                    	**type**\:   :py:class:`EthCtrlrAlarmState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthCtrlrAlarmState>`
                    
                    .. attribute:: rx_opd_alarm
                    
                    	Rx OPD Alarm
                    	**type**\:   :py:class:`EthCtrlrAlarmState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthCtrlrAlarmState>`
                    
                    .. attribute:: sd_ber_alarm
                    
                    	SD BER
                    	**type**\:   :py:class:`EthCtrlrAlarmState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthCtrlrAlarmState>`
                    
                    .. attribute:: sf_ber_alarm
                    
                    	SF BER
                    	**type**\:   :py:class:`EthCtrlrAlarmState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthCtrlrAlarmState>`
                    
                    .. attribute:: squelch_alarm
                    
                    	Squelch
                    	**type**\:   :py:class:`EthCtrlrAlarmState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthCtrlrAlarmState>`
                    
                    

                    """

                    _prefix = 'drivers-media-eth-oper'
                    _revision = '2017-04-04'

                    def __init__(self):
                        super(EthernetInterface.Interfaces.Interface.Layer1Info.PreviousAlarms, self).__init__()

                        self.yang_name = "previous-alarms"
                        self.yang_parent_name = "layer1-info"

                        self.hi_ber_alarm = YLeaf(YType.enumeration, "hi-ber-alarm")

                        self.local_fault_alarm = YLeaf(YType.enumeration, "local-fault-alarm")

                        self.loss_of_synchronization_data_alarm = YLeaf(YType.enumeration, "loss-of-synchronization-data-alarm")

                        self.pcs_loss_of_block_lock_alarm = YLeaf(YType.enumeration, "pcs-loss-of-block-lock-alarm")

                        self.received_loss_of_signal_alarm = YLeaf(YType.enumeration, "received-loss-of-signal-alarm")

                        self.remote_fault_alarm = YLeaf(YType.enumeration, "remote-fault-alarm")

                        self.rx_opd_alarm = YLeaf(YType.enumeration, "rx-opd-alarm")

                        self.sd_ber_alarm = YLeaf(YType.enumeration, "sd-ber-alarm")

                        self.sf_ber_alarm = YLeaf(YType.enumeration, "sf-ber-alarm")

                        self.squelch_alarm = YLeaf(YType.enumeration, "squelch-alarm")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("hi_ber_alarm",
                                        "local_fault_alarm",
                                        "loss_of_synchronization_data_alarm",
                                        "pcs_loss_of_block_lock_alarm",
                                        "received_loss_of_signal_alarm",
                                        "remote_fault_alarm",
                                        "rx_opd_alarm",
                                        "sd_ber_alarm",
                                        "sf_ber_alarm",
                                        "squelch_alarm") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(EthernetInterface.Interfaces.Interface.Layer1Info.PreviousAlarms, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(EthernetInterface.Interfaces.Interface.Layer1Info.PreviousAlarms, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.hi_ber_alarm.is_set or
                            self.local_fault_alarm.is_set or
                            self.loss_of_synchronization_data_alarm.is_set or
                            self.pcs_loss_of_block_lock_alarm.is_set or
                            self.received_loss_of_signal_alarm.is_set or
                            self.remote_fault_alarm.is_set or
                            self.rx_opd_alarm.is_set or
                            self.sd_ber_alarm.is_set or
                            self.sf_ber_alarm.is_set or
                            self.squelch_alarm.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.hi_ber_alarm.yfilter != YFilter.not_set or
                            self.local_fault_alarm.yfilter != YFilter.not_set or
                            self.loss_of_synchronization_data_alarm.yfilter != YFilter.not_set or
                            self.pcs_loss_of_block_lock_alarm.yfilter != YFilter.not_set or
                            self.received_loss_of_signal_alarm.yfilter != YFilter.not_set or
                            self.remote_fault_alarm.yfilter != YFilter.not_set or
                            self.rx_opd_alarm.yfilter != YFilter.not_set or
                            self.sd_ber_alarm.yfilter != YFilter.not_set or
                            self.sf_ber_alarm.yfilter != YFilter.not_set or
                            self.squelch_alarm.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "previous-alarms" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.hi_ber_alarm.is_set or self.hi_ber_alarm.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.hi_ber_alarm.get_name_leafdata())
                        if (self.local_fault_alarm.is_set or self.local_fault_alarm.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.local_fault_alarm.get_name_leafdata())
                        if (self.loss_of_synchronization_data_alarm.is_set or self.loss_of_synchronization_data_alarm.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.loss_of_synchronization_data_alarm.get_name_leafdata())
                        if (self.pcs_loss_of_block_lock_alarm.is_set or self.pcs_loss_of_block_lock_alarm.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.pcs_loss_of_block_lock_alarm.get_name_leafdata())
                        if (self.received_loss_of_signal_alarm.is_set or self.received_loss_of_signal_alarm.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.received_loss_of_signal_alarm.get_name_leafdata())
                        if (self.remote_fault_alarm.is_set or self.remote_fault_alarm.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.remote_fault_alarm.get_name_leafdata())
                        if (self.rx_opd_alarm.is_set or self.rx_opd_alarm.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.rx_opd_alarm.get_name_leafdata())
                        if (self.sd_ber_alarm.is_set or self.sd_ber_alarm.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.sd_ber_alarm.get_name_leafdata())
                        if (self.sf_ber_alarm.is_set or self.sf_ber_alarm.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.sf_ber_alarm.get_name_leafdata())
                        if (self.squelch_alarm.is_set or self.squelch_alarm.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.squelch_alarm.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "hi-ber-alarm" or name == "local-fault-alarm" or name == "loss-of-synchronization-data-alarm" or name == "pcs-loss-of-block-lock-alarm" or name == "received-loss-of-signal-alarm" or name == "remote-fault-alarm" or name == "rx-opd-alarm" or name == "sd-ber-alarm" or name == "sf-ber-alarm" or name == "squelch-alarm"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "hi-ber-alarm"):
                            self.hi_ber_alarm = value
                            self.hi_ber_alarm.value_namespace = name_space
                            self.hi_ber_alarm.value_namespace_prefix = name_space_prefix
                        if(value_path == "local-fault-alarm"):
                            self.local_fault_alarm = value
                            self.local_fault_alarm.value_namespace = name_space
                            self.local_fault_alarm.value_namespace_prefix = name_space_prefix
                        if(value_path == "loss-of-synchronization-data-alarm"):
                            self.loss_of_synchronization_data_alarm = value
                            self.loss_of_synchronization_data_alarm.value_namespace = name_space
                            self.loss_of_synchronization_data_alarm.value_namespace_prefix = name_space_prefix
                        if(value_path == "pcs-loss-of-block-lock-alarm"):
                            self.pcs_loss_of_block_lock_alarm = value
                            self.pcs_loss_of_block_lock_alarm.value_namespace = name_space
                            self.pcs_loss_of_block_lock_alarm.value_namespace_prefix = name_space_prefix
                        if(value_path == "received-loss-of-signal-alarm"):
                            self.received_loss_of_signal_alarm = value
                            self.received_loss_of_signal_alarm.value_namespace = name_space
                            self.received_loss_of_signal_alarm.value_namespace_prefix = name_space_prefix
                        if(value_path == "remote-fault-alarm"):
                            self.remote_fault_alarm = value
                            self.remote_fault_alarm.value_namespace = name_space
                            self.remote_fault_alarm.value_namespace_prefix = name_space_prefix
                        if(value_path == "rx-opd-alarm"):
                            self.rx_opd_alarm = value
                            self.rx_opd_alarm.value_namespace = name_space
                            self.rx_opd_alarm.value_namespace_prefix = name_space_prefix
                        if(value_path == "sd-ber-alarm"):
                            self.sd_ber_alarm = value
                            self.sd_ber_alarm.value_namespace = name_space
                            self.sd_ber_alarm.value_namespace_prefix = name_space_prefix
                        if(value_path == "sf-ber-alarm"):
                            self.sf_ber_alarm = value
                            self.sf_ber_alarm.value_namespace = name_space
                            self.sf_ber_alarm.value_namespace_prefix = name_space_prefix
                        if(value_path == "squelch-alarm"):
                            self.squelch_alarm = value
                            self.squelch_alarm.value_namespace = name_space
                            self.squelch_alarm.value_namespace_prefix = name_space_prefix


                class ErrorCounts(Entity):
                    """
                    Statistics for detected errors
                    
                    .. attribute:: pcsbip_errors
                    
                    	PCS BIP error count
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: sync_header_errors
                    
                    	Sync\-header error count
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    

                    """

                    _prefix = 'drivers-media-eth-oper'
                    _revision = '2017-04-04'

                    def __init__(self):
                        super(EthernetInterface.Interfaces.Interface.Layer1Info.ErrorCounts, self).__init__()

                        self.yang_name = "error-counts"
                        self.yang_parent_name = "layer1-info"

                        self.pcsbip_errors = YLeaf(YType.uint64, "pcsbip-errors")

                        self.sync_header_errors = YLeaf(YType.uint64, "sync-header-errors")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("pcsbip_errors",
                                        "sync_header_errors") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(EthernetInterface.Interfaces.Interface.Layer1Info.ErrorCounts, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(EthernetInterface.Interfaces.Interface.Layer1Info.ErrorCounts, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.pcsbip_errors.is_set or
                            self.sync_header_errors.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.pcsbip_errors.yfilter != YFilter.not_set or
                            self.sync_header_errors.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "error-counts" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.pcsbip_errors.is_set or self.pcsbip_errors.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.pcsbip_errors.get_name_leafdata())
                        if (self.sync_header_errors.is_set or self.sync_header_errors.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.sync_header_errors.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "pcsbip-errors" or name == "sync-header-errors"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "pcsbip-errors"):
                            self.pcsbip_errors = value
                            self.pcsbip_errors.value_namespace = name_space
                            self.pcsbip_errors.value_namespace_prefix = name_space_prefix
                        if(value_path == "sync-header-errors"):
                            self.sync_header_errors = value
                            self.sync_header_errors.value_namespace = name_space
                            self.sync_header_errors.value_namespace_prefix = name_space_prefix


                class BerMonitoring(Entity):
                    """
                    BER monitoring details
                    
                    .. attribute:: settings
                    
                    	The BER monitoring settings to be applied
                    	**type**\:   :py:class:`Settings <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Interfaces.Interface.Layer1Info.BerMonitoring.Settings>`
                    
                    .. attribute:: supported
                    
                    	Whether or not BER monitoring is supported
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    

                    """

                    _prefix = 'drivers-media-eth-oper'
                    _revision = '2017-04-04'

                    def __init__(self):
                        super(EthernetInterface.Interfaces.Interface.Layer1Info.BerMonitoring, self).__init__()

                        self.yang_name = "ber-monitoring"
                        self.yang_parent_name = "layer1-info"

                        self.supported = YLeaf(YType.int32, "supported")

                        self.settings = EthernetInterface.Interfaces.Interface.Layer1Info.BerMonitoring.Settings()
                        self.settings.parent = self
                        self._children_name_map["settings"] = "settings"
                        self._children_yang_names.add("settings")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("supported") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(EthernetInterface.Interfaces.Interface.Layer1Info.BerMonitoring, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(EthernetInterface.Interfaces.Interface.Layer1Info.BerMonitoring, self).__setattr__(name, value)


                    class Settings(Entity):
                        """
                        The BER monitoring settings to be applied
                        
                        .. attribute:: signal_degrade_alarm
                        
                        	Report alarm to indicate signal degrade
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: signal_degrade_threshold
                        
                        	BER threshold for signal to degrade
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: signal_fail_alarm
                        
                        	Report alarm to indicate signal failure
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: signal_fail_threshold
                        
                        	BER threshold for signal to fail
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: signal_remote_fault
                        
                        	Whether drivers should signal remote faults
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        

                        """

                        _prefix = 'drivers-media-eth-oper'
                        _revision = '2017-04-04'

                        def __init__(self):
                            super(EthernetInterface.Interfaces.Interface.Layer1Info.BerMonitoring.Settings, self).__init__()

                            self.yang_name = "settings"
                            self.yang_parent_name = "ber-monitoring"

                            self.signal_degrade_alarm = YLeaf(YType.int32, "signal-degrade-alarm")

                            self.signal_degrade_threshold = YLeaf(YType.uint32, "signal-degrade-threshold")

                            self.signal_fail_alarm = YLeaf(YType.int32, "signal-fail-alarm")

                            self.signal_fail_threshold = YLeaf(YType.uint32, "signal-fail-threshold")

                            self.signal_remote_fault = YLeaf(YType.int32, "signal-remote-fault")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("signal_degrade_alarm",
                                            "signal_degrade_threshold",
                                            "signal_fail_alarm",
                                            "signal_fail_threshold",
                                            "signal_remote_fault") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(EthernetInterface.Interfaces.Interface.Layer1Info.BerMonitoring.Settings, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(EthernetInterface.Interfaces.Interface.Layer1Info.BerMonitoring.Settings, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.signal_degrade_alarm.is_set or
                                self.signal_degrade_threshold.is_set or
                                self.signal_fail_alarm.is_set or
                                self.signal_fail_threshold.is_set or
                                self.signal_remote_fault.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.signal_degrade_alarm.yfilter != YFilter.not_set or
                                self.signal_degrade_threshold.yfilter != YFilter.not_set or
                                self.signal_fail_alarm.yfilter != YFilter.not_set or
                                self.signal_fail_threshold.yfilter != YFilter.not_set or
                                self.signal_remote_fault.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "settings" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.signal_degrade_alarm.is_set or self.signal_degrade_alarm.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.signal_degrade_alarm.get_name_leafdata())
                            if (self.signal_degrade_threshold.is_set or self.signal_degrade_threshold.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.signal_degrade_threshold.get_name_leafdata())
                            if (self.signal_fail_alarm.is_set or self.signal_fail_alarm.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.signal_fail_alarm.get_name_leafdata())
                            if (self.signal_fail_threshold.is_set or self.signal_fail_threshold.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.signal_fail_threshold.get_name_leafdata())
                            if (self.signal_remote_fault.is_set or self.signal_remote_fault.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.signal_remote_fault.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "signal-degrade-alarm" or name == "signal-degrade-threshold" or name == "signal-fail-alarm" or name == "signal-fail-threshold" or name == "signal-remote-fault"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "signal-degrade-alarm"):
                                self.signal_degrade_alarm = value
                                self.signal_degrade_alarm.value_namespace = name_space
                                self.signal_degrade_alarm.value_namespace_prefix = name_space_prefix
                            if(value_path == "signal-degrade-threshold"):
                                self.signal_degrade_threshold = value
                                self.signal_degrade_threshold.value_namespace = name_space
                                self.signal_degrade_threshold.value_namespace_prefix = name_space_prefix
                            if(value_path == "signal-fail-alarm"):
                                self.signal_fail_alarm = value
                                self.signal_fail_alarm.value_namespace = name_space
                                self.signal_fail_alarm.value_namespace_prefix = name_space_prefix
                            if(value_path == "signal-fail-threshold"):
                                self.signal_fail_threshold = value
                                self.signal_fail_threshold.value_namespace = name_space
                                self.signal_fail_threshold.value_namespace_prefix = name_space_prefix
                            if(value_path == "signal-remote-fault"):
                                self.signal_remote_fault = value
                                self.signal_remote_fault.value_namespace = name_space
                                self.signal_remote_fault.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.supported.is_set or
                            (self.settings is not None and self.settings.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.supported.yfilter != YFilter.not_set or
                            (self.settings is not None and self.settings.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "ber-monitoring" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.supported.is_set or self.supported.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.supported.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "settings"):
                            if (self.settings is None):
                                self.settings = EthernetInterface.Interfaces.Interface.Layer1Info.BerMonitoring.Settings()
                                self.settings.parent = self
                                self._children_name_map["settings"] = "settings"
                            return self.settings

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "settings" or name == "supported"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "supported"):
                            self.supported = value
                            self.supported.value_namespace = name_space
                            self.supported.value_namespace_prefix = name_space_prefix


                class OpdMonitoring(Entity):
                    """
                    OPD monitoring details
                    
                    .. attribute:: settings
                    
                    	The OPD monitoring settings to be applied
                    	**type**\:   :py:class:`Settings <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Interfaces.Interface.Layer1Info.OpdMonitoring.Settings>`
                    
                    .. attribute:: supported
                    
                    	Whether or not OPD monitoring is supported
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    

                    """

                    _prefix = 'drivers-media-eth-oper'
                    _revision = '2017-04-04'

                    def __init__(self):
                        super(EthernetInterface.Interfaces.Interface.Layer1Info.OpdMonitoring, self).__init__()

                        self.yang_name = "opd-monitoring"
                        self.yang_parent_name = "layer1-info"

                        self.supported = YLeaf(YType.int32, "supported")

                        self.settings = EthernetInterface.Interfaces.Interface.Layer1Info.OpdMonitoring.Settings()
                        self.settings.parent = self
                        self._children_name_map["settings"] = "settings"
                        self._children_yang_names.add("settings")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("supported") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(EthernetInterface.Interfaces.Interface.Layer1Info.OpdMonitoring, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(EthernetInterface.Interfaces.Interface.Layer1Info.OpdMonitoring, self).__setattr__(name, value)


                    class Settings(Entity):
                        """
                        The OPD monitoring settings to be applied
                        
                        .. attribute:: received_optical_power_degrade_threshold
                        
                        	Rx\-OPD alarm threshold value
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: received_optical_power_degrade_threshold_set
                        
                        	Rx\-OPD alarm threshold set?
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        

                        """

                        _prefix = 'drivers-media-eth-oper'
                        _revision = '2017-04-04'

                        def __init__(self):
                            super(EthernetInterface.Interfaces.Interface.Layer1Info.OpdMonitoring.Settings, self).__init__()

                            self.yang_name = "settings"
                            self.yang_parent_name = "opd-monitoring"

                            self.received_optical_power_degrade_threshold = YLeaf(YType.int32, "received-optical-power-degrade-threshold")

                            self.received_optical_power_degrade_threshold_set = YLeaf(YType.int32, "received-optical-power-degrade-threshold-set")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("received_optical_power_degrade_threshold",
                                            "received_optical_power_degrade_threshold_set") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(EthernetInterface.Interfaces.Interface.Layer1Info.OpdMonitoring.Settings, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(EthernetInterface.Interfaces.Interface.Layer1Info.OpdMonitoring.Settings, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.received_optical_power_degrade_threshold.is_set or
                                self.received_optical_power_degrade_threshold_set.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.received_optical_power_degrade_threshold.yfilter != YFilter.not_set or
                                self.received_optical_power_degrade_threshold_set.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "settings" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.received_optical_power_degrade_threshold.is_set or self.received_optical_power_degrade_threshold.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.received_optical_power_degrade_threshold.get_name_leafdata())
                            if (self.received_optical_power_degrade_threshold_set.is_set or self.received_optical_power_degrade_threshold_set.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.received_optical_power_degrade_threshold_set.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "received-optical-power-degrade-threshold" or name == "received-optical-power-degrade-threshold-set"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "received-optical-power-degrade-threshold"):
                                self.received_optical_power_degrade_threshold = value
                                self.received_optical_power_degrade_threshold.value_namespace = name_space
                                self.received_optical_power_degrade_threshold.value_namespace_prefix = name_space_prefix
                            if(value_path == "received-optical-power-degrade-threshold-set"):
                                self.received_optical_power_degrade_threshold_set = value
                                self.received_optical_power_degrade_threshold_set.value_namespace = name_space
                                self.received_optical_power_degrade_threshold_set.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.supported.is_set or
                            (self.settings is not None and self.settings.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.supported.yfilter != YFilter.not_set or
                            (self.settings is not None and self.settings.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "opd-monitoring" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.supported.is_set or self.supported.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.supported.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "settings"):
                            if (self.settings is None):
                                self.settings = EthernetInterface.Interfaces.Interface.Layer1Info.OpdMonitoring.Settings()
                                self.settings.parent = self
                                self._children_name_map["settings"] = "settings"
                            return self.settings

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "settings" or name == "supported"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "supported"):
                            self.supported = value
                            self.supported.value_namespace = name_space
                            self.supported.value_namespace_prefix = name_space_prefix


                class PfcInfo(Entity):
                    """
                    Priority flow control information
                    
                    .. attribute:: priority_enabled_bitmap
                    
                    	Priority bitmap
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: priority_flowcontrol
                    
                    	Port operational priority flow control
                    	**type**\:   :py:class:`EtherPfc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EtherPfc>`
                    
                    .. attribute:: rx_frame
                    
                    	RX Frame counts
                    	**type**\:  list of int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: tx_frame
                    
                    	TX Frame counts
                    	**type**\:  list of int
                    
                    	**range:** 0..18446744073709551615
                    
                    

                    """

                    _prefix = 'drivers-media-eth-oper'
                    _revision = '2017-04-04'

                    def __init__(self):
                        super(EthernetInterface.Interfaces.Interface.Layer1Info.PfcInfo, self).__init__()

                        self.yang_name = "pfc-info"
                        self.yang_parent_name = "layer1-info"

                        self.priority_enabled_bitmap = YLeaf(YType.uint8, "priority-enabled-bitmap")

                        self.priority_flowcontrol = YLeaf(YType.enumeration, "priority-flowcontrol")

                        self.rx_frame = YLeafList(YType.uint64, "rx-frame")

                        self.tx_frame = YLeafList(YType.uint64, "tx-frame")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("priority_enabled_bitmap",
                                        "priority_flowcontrol",
                                        "rx_frame",
                                        "tx_frame") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(EthernetInterface.Interfaces.Interface.Layer1Info.PfcInfo, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(EthernetInterface.Interfaces.Interface.Layer1Info.PfcInfo, self).__setattr__(name, value)

                    def has_data(self):
                        for leaf in self.rx_frame.getYLeafs():
                            if (leaf.yfilter != YFilter.not_set):
                                return True
                        for leaf in self.tx_frame.getYLeafs():
                            if (leaf.yfilter != YFilter.not_set):
                                return True
                        return (
                            self.priority_enabled_bitmap.is_set or
                            self.priority_flowcontrol.is_set)

                    def has_operation(self):
                        for leaf in self.rx_frame.getYLeafs():
                            if (leaf.is_set):
                                return True
                        for leaf in self.tx_frame.getYLeafs():
                            if (leaf.is_set):
                                return True
                        return (
                            self.yfilter != YFilter.not_set or
                            self.priority_enabled_bitmap.yfilter != YFilter.not_set or
                            self.priority_flowcontrol.yfilter != YFilter.not_set or
                            self.rx_frame.yfilter != YFilter.not_set or
                            self.tx_frame.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "pfc-info" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.priority_enabled_bitmap.is_set or self.priority_enabled_bitmap.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.priority_enabled_bitmap.get_name_leafdata())
                        if (self.priority_flowcontrol.is_set or self.priority_flowcontrol.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.priority_flowcontrol.get_name_leafdata())

                        leaf_name_data.extend(self.rx_frame.get_name_leafdata())

                        leaf_name_data.extend(self.tx_frame.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "priority-enabled-bitmap" or name == "priority-flowcontrol" or name == "rx-frame" or name == "tx-frame"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "priority-enabled-bitmap"):
                            self.priority_enabled_bitmap = value
                            self.priority_enabled_bitmap.value_namespace = name_space
                            self.priority_enabled_bitmap.value_namespace_prefix = name_space_prefix
                        if(value_path == "priority-flowcontrol"):
                            self.priority_flowcontrol = value
                            self.priority_flowcontrol.value_namespace = name_space
                            self.priority_flowcontrol.value_namespace_prefix = name_space_prefix
                        if(value_path == "rx-frame"):
                            self.rx_frame.append(value)
                        if(value_path == "tx-frame"):
                            self.tx_frame.append(value)

                def has_data(self):
                    return (
                        self.bandwidth.is_set or
                        self.bandwidth_utilization.is_set or
                        self.duplex.is_set or
                        self.flowcontrol.is_set or
                        self.ipg.is_set or
                        self.laser_squelch_enabled.is_set or
                        self.led_state.is_set or
                        self.link_state.is_set or
                        self.speed.is_set or
                        (self.autoneg is not None and self.autoneg.has_data()) or
                        (self.ber_monitoring is not None and self.ber_monitoring.has_data()) or
                        (self.current_alarms is not None and self.current_alarms.has_data()) or
                        (self.error_counts is not None and self.error_counts.has_data()) or
                        (self.opd_monitoring is not None and self.opd_monitoring.has_data()) or
                        (self.pfc_info is not None and self.pfc_info.has_data()) or
                        (self.previous_alarms is not None and self.previous_alarms.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.bandwidth.yfilter != YFilter.not_set or
                        self.bandwidth_utilization.yfilter != YFilter.not_set or
                        self.duplex.yfilter != YFilter.not_set or
                        self.flowcontrol.yfilter != YFilter.not_set or
                        self.ipg.yfilter != YFilter.not_set or
                        self.laser_squelch_enabled.yfilter != YFilter.not_set or
                        self.led_state.yfilter != YFilter.not_set or
                        self.link_state.yfilter != YFilter.not_set or
                        self.speed.yfilter != YFilter.not_set or
                        (self.autoneg is not None and self.autoneg.has_operation()) or
                        (self.ber_monitoring is not None and self.ber_monitoring.has_operation()) or
                        (self.current_alarms is not None and self.current_alarms.has_operation()) or
                        (self.error_counts is not None and self.error_counts.has_operation()) or
                        (self.opd_monitoring is not None and self.opd_monitoring.has_operation()) or
                        (self.pfc_info is not None and self.pfc_info.has_operation()) or
                        (self.previous_alarms is not None and self.previous_alarms.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "layer1-info" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.bandwidth.is_set or self.bandwidth.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.bandwidth.get_name_leafdata())
                    if (self.bandwidth_utilization.is_set or self.bandwidth_utilization.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.bandwidth_utilization.get_name_leafdata())
                    if (self.duplex.is_set or self.duplex.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.duplex.get_name_leafdata())
                    if (self.flowcontrol.is_set or self.flowcontrol.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.flowcontrol.get_name_leafdata())
                    if (self.ipg.is_set or self.ipg.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ipg.get_name_leafdata())
                    if (self.laser_squelch_enabled.is_set or self.laser_squelch_enabled.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.laser_squelch_enabled.get_name_leafdata())
                    if (self.led_state.is_set or self.led_state.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.led_state.get_name_leafdata())
                    if (self.link_state.is_set or self.link_state.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.link_state.get_name_leafdata())
                    if (self.speed.is_set or self.speed.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.speed.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "autoneg"):
                        if (self.autoneg is None):
                            self.autoneg = EthernetInterface.Interfaces.Interface.Layer1Info.Autoneg()
                            self.autoneg.parent = self
                            self._children_name_map["autoneg"] = "autoneg"
                        return self.autoneg

                    if (child_yang_name == "ber-monitoring"):
                        if (self.ber_monitoring is None):
                            self.ber_monitoring = EthernetInterface.Interfaces.Interface.Layer1Info.BerMonitoring()
                            self.ber_monitoring.parent = self
                            self._children_name_map["ber_monitoring"] = "ber-monitoring"
                        return self.ber_monitoring

                    if (child_yang_name == "current-alarms"):
                        if (self.current_alarms is None):
                            self.current_alarms = EthernetInterface.Interfaces.Interface.Layer1Info.CurrentAlarms()
                            self.current_alarms.parent = self
                            self._children_name_map["current_alarms"] = "current-alarms"
                        return self.current_alarms

                    if (child_yang_name == "error-counts"):
                        if (self.error_counts is None):
                            self.error_counts = EthernetInterface.Interfaces.Interface.Layer1Info.ErrorCounts()
                            self.error_counts.parent = self
                            self._children_name_map["error_counts"] = "error-counts"
                        return self.error_counts

                    if (child_yang_name == "opd-monitoring"):
                        if (self.opd_monitoring is None):
                            self.opd_monitoring = EthernetInterface.Interfaces.Interface.Layer1Info.OpdMonitoring()
                            self.opd_monitoring.parent = self
                            self._children_name_map["opd_monitoring"] = "opd-monitoring"
                        return self.opd_monitoring

                    if (child_yang_name == "pfc-info"):
                        if (self.pfc_info is None):
                            self.pfc_info = EthernetInterface.Interfaces.Interface.Layer1Info.PfcInfo()
                            self.pfc_info.parent = self
                            self._children_name_map["pfc_info"] = "pfc-info"
                        return self.pfc_info

                    if (child_yang_name == "previous-alarms"):
                        if (self.previous_alarms is None):
                            self.previous_alarms = EthernetInterface.Interfaces.Interface.Layer1Info.PreviousAlarms()
                            self.previous_alarms.parent = self
                            self._children_name_map["previous_alarms"] = "previous-alarms"
                        return self.previous_alarms

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "autoneg" or name == "ber-monitoring" or name == "current-alarms" or name == "error-counts" or name == "opd-monitoring" or name == "pfc-info" or name == "previous-alarms" or name == "bandwidth" or name == "bandwidth-utilization" or name == "duplex" or name == "flowcontrol" or name == "ipg" or name == "laser-squelch-enabled" or name == "led-state" or name == "link-state" or name == "speed"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "bandwidth"):
                        self.bandwidth = value
                        self.bandwidth.value_namespace = name_space
                        self.bandwidth.value_namespace_prefix = name_space_prefix
                    if(value_path == "bandwidth-utilization"):
                        self.bandwidth_utilization = value
                        self.bandwidth_utilization.value_namespace = name_space
                        self.bandwidth_utilization.value_namespace_prefix = name_space_prefix
                    if(value_path == "duplex"):
                        self.duplex = value
                        self.duplex.value_namespace = name_space
                        self.duplex.value_namespace_prefix = name_space_prefix
                    if(value_path == "flowcontrol"):
                        self.flowcontrol = value
                        self.flowcontrol.value_namespace = name_space
                        self.flowcontrol.value_namespace_prefix = name_space_prefix
                    if(value_path == "ipg"):
                        self.ipg = value
                        self.ipg.value_namespace = name_space
                        self.ipg.value_namespace_prefix = name_space_prefix
                    if(value_path == "laser-squelch-enabled"):
                        self.laser_squelch_enabled = value
                        self.laser_squelch_enabled.value_namespace = name_space
                        self.laser_squelch_enabled.value_namespace_prefix = name_space_prefix
                    if(value_path == "led-state"):
                        self.led_state = value
                        self.led_state.value_namespace = name_space
                        self.led_state.value_namespace_prefix = name_space_prefix
                    if(value_path == "link-state"):
                        self.link_state = value
                        self.link_state.value_namespace = name_space
                        self.link_state.value_namespace_prefix = name_space_prefix
                    if(value_path == "speed"):
                        self.speed = value
                        self.speed.value_namespace = name_space
                        self.speed.value_namespace_prefix = name_space_prefix


            class MacInfo(Entity):
                """
                MAC Layer information
                
                .. attribute:: burned_in_mac_address
                
                	Port Burned\-In MAC address
                	**type**\:  str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                .. attribute:: mru
                
                	Port operational MRU
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: mtu
                
                	Port operational MTU
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: multicast_mac_filters
                
                	Port multicast MAC filter information
                	**type**\:   :py:class:`MulticastMacFilters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Interfaces.Interface.MacInfo.MulticastMacFilters>`
                
                .. attribute:: operational_mac_address
                
                	Port operational MAC address
                	**type**\:  str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                .. attribute:: unicast_mac_filters
                
                	Port unicast MAC filter information
                	**type**\:   :py:class:`UnicastMacFilters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Interfaces.Interface.MacInfo.UnicastMacFilters>`
                
                

                """

                _prefix = 'drivers-media-eth-oper'
                _revision = '2017-04-04'

                def __init__(self):
                    super(EthernetInterface.Interfaces.Interface.MacInfo, self).__init__()

                    self.yang_name = "mac-info"
                    self.yang_parent_name = "interface"

                    self.burned_in_mac_address = YLeaf(YType.str, "burned-in-mac-address")

                    self.mru = YLeaf(YType.uint32, "mru")

                    self.mtu = YLeaf(YType.uint32, "mtu")

                    self.operational_mac_address = YLeaf(YType.str, "operational-mac-address")

                    self.multicast_mac_filters = EthernetInterface.Interfaces.Interface.MacInfo.MulticastMacFilters()
                    self.multicast_mac_filters.parent = self
                    self._children_name_map["multicast_mac_filters"] = "multicast-mac-filters"
                    self._children_yang_names.add("multicast-mac-filters")

                    self.unicast_mac_filters = EthernetInterface.Interfaces.Interface.MacInfo.UnicastMacFilters()
                    self.unicast_mac_filters.parent = self
                    self._children_name_map["unicast_mac_filters"] = "unicast-mac-filters"
                    self._children_yang_names.add("unicast-mac-filters")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("burned_in_mac_address",
                                    "mru",
                                    "mtu",
                                    "operational_mac_address") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(EthernetInterface.Interfaces.Interface.MacInfo, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(EthernetInterface.Interfaces.Interface.MacInfo, self).__setattr__(name, value)


                class UnicastMacFilters(Entity):
                    """
                    Port unicast MAC filter information
                    
                    .. attribute:: unicast_mac_address
                    
                    	MAC addresses in the unicast ingress destination MAC filter
                    	**type**\:  list of str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    

                    """

                    _prefix = 'drivers-media-eth-oper'
                    _revision = '2017-04-04'

                    def __init__(self):
                        super(EthernetInterface.Interfaces.Interface.MacInfo.UnicastMacFilters, self).__init__()

                        self.yang_name = "unicast-mac-filters"
                        self.yang_parent_name = "mac-info"

                        self.unicast_mac_address = YLeafList(YType.str, "unicast-mac-address")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("unicast_mac_address") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(EthernetInterface.Interfaces.Interface.MacInfo.UnicastMacFilters, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(EthernetInterface.Interfaces.Interface.MacInfo.UnicastMacFilters, self).__setattr__(name, value)

                    def has_data(self):
                        for leaf in self.unicast_mac_address.getYLeafs():
                            if (leaf.yfilter != YFilter.not_set):
                                return True
                        return False

                    def has_operation(self):
                        for leaf in self.unicast_mac_address.getYLeafs():
                            if (leaf.is_set):
                                return True
                        return (
                            self.yfilter != YFilter.not_set or
                            self.unicast_mac_address.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "unicast-mac-filters" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()

                        leaf_name_data.extend(self.unicast_mac_address.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "unicast-mac-address"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "unicast-mac-address"):
                            self.unicast_mac_address.append(value)


                class MulticastMacFilters(Entity):
                    """
                    Port multicast MAC filter information
                    
                    .. attribute:: multicast_mac_address
                    
                    	MAC addresses in the multicast ingress destination MAC filter
                    	**type**\: list of    :py:class:`MulticastMacAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Interfaces.Interface.MacInfo.MulticastMacFilters.MulticastMacAddress>`
                    
                    .. attribute:: multicast_promiscuous
                    
                    	Whether the port is in multicast promiscuous mode
                    	**type**\:  bool
                    
                    

                    """

                    _prefix = 'drivers-media-eth-oper'
                    _revision = '2017-04-04'

                    def __init__(self):
                        super(EthernetInterface.Interfaces.Interface.MacInfo.MulticastMacFilters, self).__init__()

                        self.yang_name = "multicast-mac-filters"
                        self.yang_parent_name = "mac-info"

                        self.multicast_promiscuous = YLeaf(YType.boolean, "multicast-promiscuous")

                        self.multicast_mac_address = YList(self)

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("multicast_promiscuous") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(EthernetInterface.Interfaces.Interface.MacInfo.MulticastMacFilters, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(EthernetInterface.Interfaces.Interface.MacInfo.MulticastMacFilters, self).__setattr__(name, value)


                    class MulticastMacAddress(Entity):
                        """
                        MAC addresses in the multicast ingress
                        destination MAC filter
                        
                        .. attribute:: mac_address
                        
                        	MAC address
                        	**type**\:  str
                        
                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                        
                        .. attribute:: mask
                        
                        	Mask for this MAC address
                        	**type**\:  str
                        
                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                        
                        

                        """

                        _prefix = 'drivers-media-eth-oper'
                        _revision = '2017-04-04'

                        def __init__(self):
                            super(EthernetInterface.Interfaces.Interface.MacInfo.MulticastMacFilters.MulticastMacAddress, self).__init__()

                            self.yang_name = "multicast-mac-address"
                            self.yang_parent_name = "multicast-mac-filters"

                            self.mac_address = YLeaf(YType.str, "mac-address")

                            self.mask = YLeaf(YType.str, "mask")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("mac_address",
                                            "mask") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(EthernetInterface.Interfaces.Interface.MacInfo.MulticastMacFilters.MulticastMacAddress, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(EthernetInterface.Interfaces.Interface.MacInfo.MulticastMacFilters.MulticastMacAddress, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.mac_address.is_set or
                                self.mask.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.mac_address.yfilter != YFilter.not_set or
                                self.mask.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "multicast-mac-address" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.mac_address.is_set or self.mac_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.mac_address.get_name_leafdata())
                            if (self.mask.is_set or self.mask.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.mask.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "mac-address" or name == "mask"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "mac-address"):
                                self.mac_address = value
                                self.mac_address.value_namespace = name_space
                                self.mac_address.value_namespace_prefix = name_space_prefix
                            if(value_path == "mask"):
                                self.mask = value
                                self.mask.value_namespace = name_space
                                self.mask.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.multicast_mac_address:
                            if (c.has_data()):
                                return True
                        return self.multicast_promiscuous.is_set

                    def has_operation(self):
                        for c in self.multicast_mac_address:
                            if (c.has_operation()):
                                return True
                        return (
                            self.yfilter != YFilter.not_set or
                            self.multicast_promiscuous.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "multicast-mac-filters" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.multicast_promiscuous.is_set or self.multicast_promiscuous.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.multicast_promiscuous.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "multicast-mac-address"):
                            for c in self.multicast_mac_address:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = EthernetInterface.Interfaces.Interface.MacInfo.MulticastMacFilters.MulticastMacAddress()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.multicast_mac_address.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "multicast-mac-address" or name == "multicast-promiscuous"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "multicast-promiscuous"):
                            self.multicast_promiscuous = value
                            self.multicast_promiscuous.value_namespace = name_space
                            self.multicast_promiscuous.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.burned_in_mac_address.is_set or
                        self.mru.is_set or
                        self.mtu.is_set or
                        self.operational_mac_address.is_set or
                        (self.multicast_mac_filters is not None and self.multicast_mac_filters.has_data()) or
                        (self.unicast_mac_filters is not None and self.unicast_mac_filters.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.burned_in_mac_address.yfilter != YFilter.not_set or
                        self.mru.yfilter != YFilter.not_set or
                        self.mtu.yfilter != YFilter.not_set or
                        self.operational_mac_address.yfilter != YFilter.not_set or
                        (self.multicast_mac_filters is not None and self.multicast_mac_filters.has_operation()) or
                        (self.unicast_mac_filters is not None and self.unicast_mac_filters.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "mac-info" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.burned_in_mac_address.is_set or self.burned_in_mac_address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.burned_in_mac_address.get_name_leafdata())
                    if (self.mru.is_set or self.mru.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.mru.get_name_leafdata())
                    if (self.mtu.is_set or self.mtu.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.mtu.get_name_leafdata())
                    if (self.operational_mac_address.is_set or self.operational_mac_address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.operational_mac_address.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "multicast-mac-filters"):
                        if (self.multicast_mac_filters is None):
                            self.multicast_mac_filters = EthernetInterface.Interfaces.Interface.MacInfo.MulticastMacFilters()
                            self.multicast_mac_filters.parent = self
                            self._children_name_map["multicast_mac_filters"] = "multicast-mac-filters"
                        return self.multicast_mac_filters

                    if (child_yang_name == "unicast-mac-filters"):
                        if (self.unicast_mac_filters is None):
                            self.unicast_mac_filters = EthernetInterface.Interfaces.Interface.MacInfo.UnicastMacFilters()
                            self.unicast_mac_filters.parent = self
                            self._children_name_map["unicast_mac_filters"] = "unicast-mac-filters"
                        return self.unicast_mac_filters

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "multicast-mac-filters" or name == "unicast-mac-filters" or name == "burned-in-mac-address" or name == "mru" or name == "mtu" or name == "operational-mac-address"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "burned-in-mac-address"):
                        self.burned_in_mac_address = value
                        self.burned_in_mac_address.value_namespace = name_space
                        self.burned_in_mac_address.value_namespace_prefix = name_space_prefix
                    if(value_path == "mru"):
                        self.mru = value
                        self.mru.value_namespace = name_space
                        self.mru.value_namespace_prefix = name_space_prefix
                    if(value_path == "mtu"):
                        self.mtu = value
                        self.mtu.value_namespace = name_space
                        self.mtu.value_namespace_prefix = name_space_prefix
                    if(value_path == "operational-mac-address"):
                        self.operational_mac_address = value
                        self.operational_mac_address.value_namespace = name_space
                        self.operational_mac_address.value_namespace_prefix = name_space_prefix


            class TransportInfo(Entity):
                """
                Transport state information
                
                .. attribute:: ains_status
                
                	AINS Soak status
                	**type**\:   :py:class:`EtherAinsStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EtherAinsStatus>`
                
                .. attribute:: maintenance_mode_enabled
                
                	Maintenance Mode \- TRUE if enabled
                	**type**\:  bool
                
                .. attribute:: remaining_duration
                
                	Remaining duration (seconds) of AINS soak timer
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: total_duration
                
                	Total duration (seconds) of AINS soak timer
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                

                """

                _prefix = 'drivers-media-eth-oper'
                _revision = '2017-04-04'

                def __init__(self):
                    super(EthernetInterface.Interfaces.Interface.TransportInfo, self).__init__()

                    self.yang_name = "transport-info"
                    self.yang_parent_name = "interface"

                    self.ains_status = YLeaf(YType.enumeration, "ains-status")

                    self.maintenance_mode_enabled = YLeaf(YType.boolean, "maintenance-mode-enabled")

                    self.remaining_duration = YLeaf(YType.uint32, "remaining-duration")

                    self.total_duration = YLeaf(YType.uint32, "total-duration")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("ains_status",
                                    "maintenance_mode_enabled",
                                    "remaining_duration",
                                    "total_duration") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(EthernetInterface.Interfaces.Interface.TransportInfo, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(EthernetInterface.Interfaces.Interface.TransportInfo, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.ains_status.is_set or
                        self.maintenance_mode_enabled.is_set or
                        self.remaining_duration.is_set or
                        self.total_duration.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.ains_status.yfilter != YFilter.not_set or
                        self.maintenance_mode_enabled.yfilter != YFilter.not_set or
                        self.remaining_duration.yfilter != YFilter.not_set or
                        self.total_duration.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "transport-info" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.ains_status.is_set or self.ains_status.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ains_status.get_name_leafdata())
                    if (self.maintenance_mode_enabled.is_set or self.maintenance_mode_enabled.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.maintenance_mode_enabled.get_name_leafdata())
                    if (self.remaining_duration.is_set or self.remaining_duration.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.remaining_duration.get_name_leafdata())
                    if (self.total_duration.is_set or self.total_duration.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.total_duration.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "ains-status" or name == "maintenance-mode-enabled" or name == "remaining-duration" or name == "total-duration"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "ains-status"):
                        self.ains_status = value
                        self.ains_status.value_namespace = name_space
                        self.ains_status.value_namespace_prefix = name_space_prefix
                    if(value_path == "maintenance-mode-enabled"):
                        self.maintenance_mode_enabled = value
                        self.maintenance_mode_enabled.value_namespace = name_space
                        self.maintenance_mode_enabled.value_namespace_prefix = name_space_prefix
                    if(value_path == "remaining-duration"):
                        self.remaining_duration = value
                        self.remaining_duration.value_namespace = name_space
                        self.remaining_duration.value_namespace_prefix = name_space_prefix
                    if(value_path == "total-duration"):
                        self.total_duration = value
                        self.total_duration.value_namespace = name_space
                        self.total_duration.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.interface_name.is_set or
                    self.admin_state.is_set or
                    self.oper_state_up.is_set or
                    (self.layer1_info is not None and self.layer1_info.has_data()) or
                    (self.mac_info is not None and self.mac_info.has_data()) or
                    (self.phy_info is not None and self.phy_info.has_data()) or
                    (self.transport_info is not None and self.transport_info.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.interface_name.yfilter != YFilter.not_set or
                    self.admin_state.yfilter != YFilter.not_set or
                    self.oper_state_up.yfilter != YFilter.not_set or
                    (self.layer1_info is not None and self.layer1_info.has_operation()) or
                    (self.mac_info is not None and self.mac_info.has_operation()) or
                    (self.phy_info is not None and self.phy_info.has_operation()) or
                    (self.transport_info is not None and self.transport_info.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "interface" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-drivers-media-eth-oper:ethernet-interface/interfaces/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.interface_name.get_name_leafdata())
                if (self.admin_state.is_set or self.admin_state.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.admin_state.get_name_leafdata())
                if (self.oper_state_up.is_set or self.oper_state_up.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.oper_state_up.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "layer1-info"):
                    if (self.layer1_info is None):
                        self.layer1_info = EthernetInterface.Interfaces.Interface.Layer1Info()
                        self.layer1_info.parent = self
                        self._children_name_map["layer1_info"] = "layer1-info"
                    return self.layer1_info

                if (child_yang_name == "mac-info"):
                    if (self.mac_info is None):
                        self.mac_info = EthernetInterface.Interfaces.Interface.MacInfo()
                        self.mac_info.parent = self
                        self._children_name_map["mac_info"] = "mac-info"
                    return self.mac_info

                if (child_yang_name == "phy-info"):
                    if (self.phy_info is None):
                        self.phy_info = EthernetInterface.Interfaces.Interface.PhyInfo()
                        self.phy_info.parent = self
                        self._children_name_map["phy_info"] = "phy-info"
                    return self.phy_info

                if (child_yang_name == "transport-info"):
                    if (self.transport_info is None):
                        self.transport_info = EthernetInterface.Interfaces.Interface.TransportInfo()
                        self.transport_info.parent = self
                        self._children_name_map["transport_info"] = "transport-info"
                    return self.transport_info

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "layer1-info" or name == "mac-info" or name == "phy-info" or name == "transport-info" or name == "interface-name" or name == "admin-state" or name == "oper-state-up"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "interface-name"):
                    self.interface_name = value
                    self.interface_name.value_namespace = name_space
                    self.interface_name.value_namespace_prefix = name_space_prefix
                if(value_path == "admin-state"):
                    self.admin_state = value
                    self.admin_state.value_namespace = name_space
                    self.admin_state.value_namespace_prefix = name_space_prefix
                if(value_path == "oper-state-up"):
                    self.oper_state_up = value
                    self.oper_state_up.value_namespace = name_space
                    self.oper_state_up.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.interface:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.interface:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "interfaces" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-drivers-media-eth-oper:ethernet-interface/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "interface"):
                for c in self.interface:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = EthernetInterface.Interfaces.Interface()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.interface.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "interface"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Berts(Entity):
        """
        Ethernet controller BERT table
        
        .. attribute:: bert
        
        	Ethernet BERT information
        	**type**\: list of    :py:class:`Bert <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Berts.Bert>`
        
        

        """

        _prefix = 'drivers-media-eth-oper'
        _revision = '2017-04-04'

        def __init__(self):
            super(EthernetInterface.Berts, self).__init__()

            self.yang_name = "berts"
            self.yang_parent_name = "ethernet-interface"

            self.bert = YList(self)

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
                        super(EthernetInterface.Berts, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(EthernetInterface.Berts, self).__setattr__(name, value)


        class Bert(Entity):
            """
            Ethernet BERT information
            
            .. attribute:: interface_name  <key>
            
            	The name of the interface
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: bert_status
            
            	Current test status
            	**type**\:   :py:class:`BertStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Berts.Bert.BertStatus>`
            
            .. attribute:: port_bert_interval
            
            	Port BERT interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: time_left
            
            	Remaining time for this test in seconds
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: second
            
            

            """

            _prefix = 'drivers-media-eth-oper'
            _revision = '2017-04-04'

            def __init__(self):
                super(EthernetInterface.Berts.Bert, self).__init__()

                self.yang_name = "bert"
                self.yang_parent_name = "berts"

                self.interface_name = YLeaf(YType.str, "interface-name")

                self.port_bert_interval = YLeaf(YType.uint32, "port-bert-interval")

                self.time_left = YLeaf(YType.uint32, "time-left")

                self.bert_status = EthernetInterface.Berts.Bert.BertStatus()
                self.bert_status.parent = self
                self._children_name_map["bert_status"] = "bert-status"
                self._children_yang_names.add("bert-status")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("interface_name",
                                "port_bert_interval",
                                "time_left") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(EthernetInterface.Berts.Bert, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(EthernetInterface.Berts.Bert, self).__setattr__(name, value)


            class BertStatus(Entity):
                """
                Current test status
                
                .. attribute:: bert_state_enabled
                
                	State
                	**type**\:  bool
                
                .. attribute:: data_availability
                
                	Flag indicating available data
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: device_under_test
                
                	Device being tested
                	**type**\:   :py:class:`EthernetDev <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetDev>`
                
                .. attribute:: error_type
                
                	Bit, block or frame error
                	**type**\:   :py:class:`EthernetBertErrCnt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetBertErrCnt>`
                
                .. attribute:: interface_device
                
                	Interface being tested
                	**type**\:   :py:class:`EthernetDevIf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetDevIf>`
                
                .. attribute:: receive_count
                
                	Receive count (if 0x1 set in flag)
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: receive_errors
                
                	Received errors (if 0x4 set in flag)
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: test_pattern
                
                	Test pattern
                	**type**\:   :py:class:`EthernetBertPattern <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetBertPattern>`
                
                .. attribute:: transmit_count
                
                	Transmit count (if 0x2 set in flag)
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'drivers-media-eth-oper'
                _revision = '2017-04-04'

                def __init__(self):
                    super(EthernetInterface.Berts.Bert.BertStatus, self).__init__()

                    self.yang_name = "bert-status"
                    self.yang_parent_name = "bert"

                    self.bert_state_enabled = YLeaf(YType.boolean, "bert-state-enabled")

                    self.data_availability = YLeaf(YType.uint32, "data-availability")

                    self.device_under_test = YLeaf(YType.enumeration, "device-under-test")

                    self.error_type = YLeaf(YType.enumeration, "error-type")

                    self.interface_device = YLeaf(YType.enumeration, "interface-device")

                    self.receive_count = YLeaf(YType.uint64, "receive-count")

                    self.receive_errors = YLeaf(YType.uint64, "receive-errors")

                    self.test_pattern = YLeaf(YType.enumeration, "test-pattern")

                    self.transmit_count = YLeaf(YType.uint64, "transmit-count")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("bert_state_enabled",
                                    "data_availability",
                                    "device_under_test",
                                    "error_type",
                                    "interface_device",
                                    "receive_count",
                                    "receive_errors",
                                    "test_pattern",
                                    "transmit_count") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(EthernetInterface.Berts.Bert.BertStatus, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(EthernetInterface.Berts.Bert.BertStatus, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.bert_state_enabled.is_set or
                        self.data_availability.is_set or
                        self.device_under_test.is_set or
                        self.error_type.is_set or
                        self.interface_device.is_set or
                        self.receive_count.is_set or
                        self.receive_errors.is_set or
                        self.test_pattern.is_set or
                        self.transmit_count.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.bert_state_enabled.yfilter != YFilter.not_set or
                        self.data_availability.yfilter != YFilter.not_set or
                        self.device_under_test.yfilter != YFilter.not_set or
                        self.error_type.yfilter != YFilter.not_set or
                        self.interface_device.yfilter != YFilter.not_set or
                        self.receive_count.yfilter != YFilter.not_set or
                        self.receive_errors.yfilter != YFilter.not_set or
                        self.test_pattern.yfilter != YFilter.not_set or
                        self.transmit_count.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "bert-status" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.bert_state_enabled.is_set or self.bert_state_enabled.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.bert_state_enabled.get_name_leafdata())
                    if (self.data_availability.is_set or self.data_availability.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.data_availability.get_name_leafdata())
                    if (self.device_under_test.is_set or self.device_under_test.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.device_under_test.get_name_leafdata())
                    if (self.error_type.is_set or self.error_type.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.error_type.get_name_leafdata())
                    if (self.interface_device.is_set or self.interface_device.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.interface_device.get_name_leafdata())
                    if (self.receive_count.is_set or self.receive_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.receive_count.get_name_leafdata())
                    if (self.receive_errors.is_set or self.receive_errors.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.receive_errors.get_name_leafdata())
                    if (self.test_pattern.is_set or self.test_pattern.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.test_pattern.get_name_leafdata())
                    if (self.transmit_count.is_set or self.transmit_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.transmit_count.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "bert-state-enabled" or name == "data-availability" or name == "device-under-test" or name == "error-type" or name == "interface-device" or name == "receive-count" or name == "receive-errors" or name == "test-pattern" or name == "transmit-count"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "bert-state-enabled"):
                        self.bert_state_enabled = value
                        self.bert_state_enabled.value_namespace = name_space
                        self.bert_state_enabled.value_namespace_prefix = name_space_prefix
                    if(value_path == "data-availability"):
                        self.data_availability = value
                        self.data_availability.value_namespace = name_space
                        self.data_availability.value_namespace_prefix = name_space_prefix
                    if(value_path == "device-under-test"):
                        self.device_under_test = value
                        self.device_under_test.value_namespace = name_space
                        self.device_under_test.value_namespace_prefix = name_space_prefix
                    if(value_path == "error-type"):
                        self.error_type = value
                        self.error_type.value_namespace = name_space
                        self.error_type.value_namespace_prefix = name_space_prefix
                    if(value_path == "interface-device"):
                        self.interface_device = value
                        self.interface_device.value_namespace = name_space
                        self.interface_device.value_namespace_prefix = name_space_prefix
                    if(value_path == "receive-count"):
                        self.receive_count = value
                        self.receive_count.value_namespace = name_space
                        self.receive_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "receive-errors"):
                        self.receive_errors = value
                        self.receive_errors.value_namespace = name_space
                        self.receive_errors.value_namespace_prefix = name_space_prefix
                    if(value_path == "test-pattern"):
                        self.test_pattern = value
                        self.test_pattern.value_namespace = name_space
                        self.test_pattern.value_namespace_prefix = name_space_prefix
                    if(value_path == "transmit-count"):
                        self.transmit_count = value
                        self.transmit_count.value_namespace = name_space
                        self.transmit_count.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.interface_name.is_set or
                    self.port_bert_interval.is_set or
                    self.time_left.is_set or
                    (self.bert_status is not None and self.bert_status.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.interface_name.yfilter != YFilter.not_set or
                    self.port_bert_interval.yfilter != YFilter.not_set or
                    self.time_left.yfilter != YFilter.not_set or
                    (self.bert_status is not None and self.bert_status.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "bert" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-drivers-media-eth-oper:ethernet-interface/berts/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.interface_name.get_name_leafdata())
                if (self.port_bert_interval.is_set or self.port_bert_interval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.port_bert_interval.get_name_leafdata())
                if (self.time_left.is_set or self.time_left.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.time_left.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "bert-status"):
                    if (self.bert_status is None):
                        self.bert_status = EthernetInterface.Berts.Bert.BertStatus()
                        self.bert_status.parent = self
                        self._children_name_map["bert_status"] = "bert-status"
                    return self.bert_status

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "bert-status" or name == "interface-name" or name == "port-bert-interval" or name == "time-left"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "interface-name"):
                    self.interface_name = value
                    self.interface_name.value_namespace = name_space
                    self.interface_name.value_namespace_prefix = name_space_prefix
                if(value_path == "port-bert-interval"):
                    self.port_bert_interval = value
                    self.port_bert_interval.value_namespace = name_space
                    self.port_bert_interval.value_namespace_prefix = name_space_prefix
                if(value_path == "time-left"):
                    self.time_left = value
                    self.time_left.value_namespace = name_space
                    self.time_left.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.bert:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.bert:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "berts" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-drivers-media-eth-oper:ethernet-interface/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "bert"):
                for c in self.bert:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = EthernetInterface.Berts.Bert()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.bert.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "bert"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.berts is not None and self.berts.has_data()) or
            (self.interfaces is not None and self.interfaces.has_data()) or
            (self.statistics is not None and self.statistics.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.berts is not None and self.berts.has_operation()) or
            (self.interfaces is not None and self.interfaces.has_operation()) or
            (self.statistics is not None and self.statistics.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-drivers-media-eth-oper:ethernet-interface" + path_buffer

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

        if (child_yang_name == "berts"):
            if (self.berts is None):
                self.berts = EthernetInterface.Berts()
                self.berts.parent = self
                self._children_name_map["berts"] = "berts"
            return self.berts

        if (child_yang_name == "interfaces"):
            if (self.interfaces is None):
                self.interfaces = EthernetInterface.Interfaces()
                self.interfaces.parent = self
                self._children_name_map["interfaces"] = "interfaces"
            return self.interfaces

        if (child_yang_name == "statistics"):
            if (self.statistics is None):
                self.statistics = EthernetInterface.Statistics()
                self.statistics.parent = self
                self._children_name_map["statistics"] = "statistics"
            return self.statistics

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "berts" or name == "interfaces" or name == "statistics"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = EthernetInterface()
        return self._top_entity

