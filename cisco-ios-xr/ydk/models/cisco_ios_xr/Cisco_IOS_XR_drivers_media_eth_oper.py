""" Cisco_IOS_XR_drivers_media_eth_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR drivers\-media\-eth package operational data.

This module contains definitions
for the following management objects\:
  ethernet\-interface\: Ethernet operational data

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class EthCtrlrAlarmState(Enum):
    """
    EthCtrlrAlarmState (Enum Class)

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
    EtherAinsStatus (Enum Class)

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
    EtherDomAlarm (Enum Class)

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
    EtherFlowcontrol (Enum Class)

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
    EtherLedState (Enum Class)

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
    EtherLinkState (Enum Class)

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

    .. data:: shutdown = 28

    	Link is shutdown

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

    shutdown = Enum.YLeaf(28, "shutdown")


class EtherPfc(Enum):
    """
    EtherPfc (Enum Class)

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
    EtherPhyPresent (Enum Class)

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
    EthernetBertErrCnt (Enum Class)

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
    EthernetBertPattern (Enum Class)

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
    EthernetDev (Enum Class)

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
    EthernetDevIf (Enum Class)

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
    EthernetDuplex (Enum Class)

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
    EthernetFec (Enum Class)

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
    EthernetIpg (Enum Class)

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
    EthernetLoopback (Enum Class)

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
    EthernetMedia (Enum Class)

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

    .. data:: ethernet_50gbase_cr2 = 343

    	2 lane copper (very short reach)

    .. data:: ethernet_50gbase_sr2 = 344

    	fiber over 2 lane optics (short reach)

    .. data:: ethernet_50gbase_psm2 = 345

    	2 parallel single mode fibers

    .. data:: ethernet_200gbase_cr4 = 346

    	4 lanes Passive Copper

    .. data:: ethernet_400gbase_fr4 = 347

    	Duplex SMF LC Connector 2km

    .. data:: ethernet_400gbase_dr4 = 348

    	SMF with MPO-12 connector

    .. data:: ethernet_400gbase_cr4 = 349

    	4 lanes Passive Copper

    .. data:: ethernet_10gbase_cu1m = 350

    	Passive Twinax cable assembly 1m

    .. data:: ethernet_10gbase_cu1_5m = 351

    	Passive Twinax cable assembly 1.5m

    .. data:: ethernet_10gbase_cu2m = 352

    	Passive Twinax cable assembly 2m

    .. data:: ethernet_10gbase_cu2_5m = 353

    	Passive Twinax cable assembly 2.5m

    .. data:: ethernet_10gbase_cu3m = 354

    	Passive Twinax cable assembly 3m

    .. data:: ethernet_10gbase_cu5m = 355

    	Passive Twinax cable assembly 5m

    .. data:: ethernet_10gbase_acu7m = 356

    	Active Twinax cable assembly 7m

    .. data:: ethernet_10gbase_acu10m = 357

    	Active Twinax cable assembly 10m

    .. data:: ethernet_10gbase_aoc1m = 358

    	Active optical cable 1m

    .. data:: ethernet_10gbase_aoc2m = 359

    	Active optical cable 2m

    .. data:: ethernet_10gbase_aoc3m = 360

    	Active optical cable 3m

    .. data:: ethernet_10gbase_aoc5m = 361

    	Active optical cable 5m

    .. data:: ethernet_10gbase_aoc7m = 362

    	Active optical cable 7m

    .. data:: ethernet_10gbase_aoc10m = 363

    	Active optical cable 10m

    .. data:: ethernet_40gbase_aoc = 364

    	Active optical cable

    .. data:: ethernet_4x10g_base_lr = 365

    	fiber over 4 lane optics (long reach)

    .. data:: ethernet_40gbase_acu1m = 366

    	Active Twinax cable assembly 1m

    .. data:: ethernet_40gbase_acu3m = 367

    	Active Twinax cable assembly 3m

    .. data:: ethernet_40gbase_acu5m = 368

    	Active Twinax cable assembly 5m

    .. data:: ethernet_40gbase_acu7m = 369

    	Active Twinax cable assembly 7m

    .. data:: ethernet_40gbase_acu10m = 370

    	Active Twinax cable assembly 10m

    .. data:: ethernet_25gbase_cu1m = 371

    	Twinaxial copper cabling (1m)

    .. data:: ethernet_25gbase_cu2m = 372

    	Twinaxial copper cabling (2m)

    .. data:: ethernet_25gbase_cu3m = 373

    	Twinaxial copper cabling (3m)

    .. data:: ethernet_25gbase_cu5m = 374

    	Twinaxial copper cabling (5m)

    .. data:: ethernet_100gbase_sm_sr = 375

    	4 lane CWDM Lite cable

    .. data:: ethernet_base_max = 376

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

    ethernet_50gbase_cr2 = Enum.YLeaf(343, "ethernet-50gbase-cr2")

    ethernet_50gbase_sr2 = Enum.YLeaf(344, "ethernet-50gbase-sr2")

    ethernet_50gbase_psm2 = Enum.YLeaf(345, "ethernet-50gbase-psm2")

    ethernet_200gbase_cr4 = Enum.YLeaf(346, "ethernet-200gbase-cr4")

    ethernet_400gbase_fr4 = Enum.YLeaf(347, "ethernet-400gbase-fr4")

    ethernet_400gbase_dr4 = Enum.YLeaf(348, "ethernet-400gbase-dr4")

    ethernet_400gbase_cr4 = Enum.YLeaf(349, "ethernet-400gbase-cr4")

    ethernet_10gbase_cu1m = Enum.YLeaf(350, "ethernet-10gbase-cu1m")

    ethernet_10gbase_cu1_5m = Enum.YLeaf(351, "ethernet-10gbase-cu1-5m")

    ethernet_10gbase_cu2m = Enum.YLeaf(352, "ethernet-10gbase-cu2m")

    ethernet_10gbase_cu2_5m = Enum.YLeaf(353, "ethernet-10gbase-cu2-5m")

    ethernet_10gbase_cu3m = Enum.YLeaf(354, "ethernet-10gbase-cu3m")

    ethernet_10gbase_cu5m = Enum.YLeaf(355, "ethernet-10gbase-cu5m")

    ethernet_10gbase_acu7m = Enum.YLeaf(356, "ethernet-10gbase-acu7m")

    ethernet_10gbase_acu10m = Enum.YLeaf(357, "ethernet-10gbase-acu10m")

    ethernet_10gbase_aoc1m = Enum.YLeaf(358, "ethernet-10gbase-aoc1m")

    ethernet_10gbase_aoc2m = Enum.YLeaf(359, "ethernet-10gbase-aoc2m")

    ethernet_10gbase_aoc3m = Enum.YLeaf(360, "ethernet-10gbase-aoc3m")

    ethernet_10gbase_aoc5m = Enum.YLeaf(361, "ethernet-10gbase-aoc5m")

    ethernet_10gbase_aoc7m = Enum.YLeaf(362, "ethernet-10gbase-aoc7m")

    ethernet_10gbase_aoc10m = Enum.YLeaf(363, "ethernet-10gbase-aoc10m")

    ethernet_40gbase_aoc = Enum.YLeaf(364, "ethernet-40gbase-aoc")

    ethernet_4x10g_base_lr = Enum.YLeaf(365, "ethernet-4x10g-base-lr")

    ethernet_40gbase_acu1m = Enum.YLeaf(366, "ethernet-40gbase-acu1m")

    ethernet_40gbase_acu3m = Enum.YLeaf(367, "ethernet-40gbase-acu3m")

    ethernet_40gbase_acu5m = Enum.YLeaf(368, "ethernet-40gbase-acu5m")

    ethernet_40gbase_acu7m = Enum.YLeaf(369, "ethernet-40gbase-acu7m")

    ethernet_40gbase_acu10m = Enum.YLeaf(370, "ethernet-40gbase-acu10m")

    ethernet_25gbase_cu1m = Enum.YLeaf(371, "ethernet-25gbase-cu1m")

    ethernet_25gbase_cu2m = Enum.YLeaf(372, "ethernet-25gbase-cu2m")

    ethernet_25gbase_cu3m = Enum.YLeaf(373, "ethernet-25gbase-cu3m")

    ethernet_25gbase_cu5m = Enum.YLeaf(374, "ethernet-25gbase-cu5m")

    ethernet_100gbase_sm_sr = Enum.YLeaf(375, "ethernet-100gbase-sm-sr")

    ethernet_base_max = Enum.YLeaf(376, "ethernet-base-max")


class EthernetPortEnable(Enum):
    """
    EthernetPortEnable (Enum Class)

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
    EthernetSpeed (Enum Class)

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

    .. data:: two_hundred_gbps = 9

    	two hundred gbps

    .. data:: four_hundred_gbps = 10

    	four hundred gbps

    .. data:: ethernet_speed_types_count = 11

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

    two_hundred_gbps = Enum.YLeaf(9, "two-hundred-gbps")

    four_hundred_gbps = Enum.YLeaf(10, "four-hundred-gbps")

    ethernet_speed_types_count = Enum.YLeaf(11, "ethernet-speed-types-count")



class EthernetInterface(Entity):
    """
    Ethernet operational data
    
    .. attribute:: statistics
    
    	Ethernet controller statistics table
    	**type**\:  :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Statistics>`
    
    .. attribute:: interfaces
    
    	Ethernet controller info table
    	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Interfaces>`
    
    .. attribute:: berts
    
    	Ethernet controller BERT table
    	**type**\:  :py:class:`Berts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Berts>`
    
    

    """

    _prefix = 'drivers-media-eth-oper'
    _revision = '2017-05-01'

    def __init__(self):
        super(EthernetInterface, self).__init__()
        self._top_entity = None

        self.yang_name = "ethernet-interface"
        self.yang_parent_name = "Cisco-IOS-XR-drivers-media-eth-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("statistics", ("statistics", EthernetInterface.Statistics)), ("interfaces", ("interfaces", EthernetInterface.Interfaces)), ("berts", ("berts", EthernetInterface.Berts))])
        self._leafs = OrderedDict()

        self.statistics = EthernetInterface.Statistics()
        self.statistics.parent = self
        self._children_name_map["statistics"] = "statistics"

        self.interfaces = EthernetInterface.Interfaces()
        self.interfaces.parent = self
        self._children_name_map["interfaces"] = "interfaces"

        self.berts = EthernetInterface.Berts()
        self.berts.parent = self
        self._children_name_map["berts"] = "berts"
        self._segment_path = lambda: "Cisco-IOS-XR-drivers-media-eth-oper:ethernet-interface"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(EthernetInterface, [], name, value)


    class Statistics(Entity):
        """
        Ethernet controller statistics table
        
        .. attribute:: statistic
        
        	Ethernet statistics information
        	**type**\: list of  		 :py:class:`Statistic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Statistics.Statistic>`
        
        

        """

        _prefix = 'drivers-media-eth-oper'
        _revision = '2017-05-01'

        def __init__(self):
            super(EthernetInterface.Statistics, self).__init__()

            self.yang_name = "statistics"
            self.yang_parent_name = "ethernet-interface"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("statistic", ("statistic", EthernetInterface.Statistics.Statistic))])
            self._leafs = OrderedDict()

            self.statistic = YList(self)
            self._segment_path = lambda: "statistics"
            self._absolute_path = lambda: "Cisco-IOS-XR-drivers-media-eth-oper:ethernet-interface/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(EthernetInterface.Statistics, [], name, value)


        class Statistic(Entity):
            """
            Ethernet statistics information
            
            .. attribute:: interface_name  (key)
            
            	The name of the interface
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
            
            .. attribute:: received_total_bytes
            
            	Total octets of all frames
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: received_good_bytes
            
            	Total octets of all good frames
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: received_total_frames
            
            	All frames, good or bad
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: received8021q_frames
            
            	All 802.1Q frames
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: received_pause_frames
            
            	All pause frames
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: received_unknown_opcodes
            
            	Unsupported MAC Control frames
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: received_total64_octet_frames
            
            	All 64 Octet Frame Count
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: received_total_octet_frames_from65_to127
            
            	All 65\-127 Octet Frame Count
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: received_total_octet_frames_from128_to255
            
            	All 128\-255 Octet Frame Count
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: received_total_octet_frames_from256_to511
            
            	All 256\-511 Octet Frame Count
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: received_total_octet_frames_from512_to1023
            
            	All 512\-1023 Octet Frame Count
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: received_total_octet_frames_from1024_to1518
            
            	All 1024\-1518 Octet Frame Count
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: received_total_octet_frames_from1519_to_max
            
            	All > 1518 Octet Frame Count
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: received_good_frames
            
            	Received Good Frames
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: received_unicast_frames
            
            	Received unicast Frames
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: received_multicast_frames
            
            	Received multicast Frames
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: received_broadcast_frames
            
            	Received broadcast Frames
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: number_of_buffer_overrun_packets_dropped
            
            	Drops due to buffer overrun
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: number_of_aborted_packets_dropped
            
            	Drops due to packet abort
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: numberof_invalid_vlan_id_packets_dropped
            
            	Drops due to invalid VLAN id
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: invalid_dest_mac_drop_packets
            
            	Drops due to the destination MAC not matching
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: invalid_encap_drop_packets
            
            	Drops due to the encapsulation or ether type not matching
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: number_of_miscellaneous_packets_dropped
            
            	Any other drops not counted
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: dropped_giant_packets_greaterthan_mru
            
            	Good frames > MRU, dropped
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: dropped_ether_stats_undersize_pkts
            
            	Good frames < 64 Octet, dropped
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: dropped_jabbers_packets_greaterthan_mru
            
            	Bad Frames > MRU, dropped
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: dropped_ether_stats_fragments
            
            	Bad Frames < 64 Octet, dropped
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: dropped_packets_with_crc_align_errors
            
            	Frames 64 \- MRU with CRC error
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ether_stats_collisions
            
            	All collision events
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: symbol_errors
            
            	Symbol errors
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: dropped_miscellaneous_error_packets
            
            	Any other errors not counted
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: rfc2819_ether_stats_oversized_pkts
            
            	RFC2819 etherStatsOversizedPkts
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: rfc2819_ether_stats_jabbers
            
            	RFC2819 etherStatsJabbers
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: rfc2819_ether_stats_crc_align_errors
            
            	RFC2819 etherStatsCRCAlignErrors
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: rfc3635dot3_stats_alignment_errors
            
            	RFC3635 dot3StatsAlignmentErrors
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: total_bytes_transmitted
            
            	Total octets of all frames
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: total_good_bytes_transmitted
            
            	Total octets of all good frames
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: total_frames_transmitted
            
            	All frames, good or bad
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: transmitted8021q_frames
            
            	All 802.1Q frames
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: transmitted_total_pause_frames
            
            	All pause frames
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: transmitted_total64_octet_frames
            
            	All 64 Octet Frame Count
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: transmitted_total_octet_frames_from65_to127
            
            	All 65\-127 Octet Frame Count
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: transmitted_total_octet_frames_from128_to255
            
            	All 128\-255 Octet Frame Count
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: transmitted_total_octet_frames_from256_to511
            
            	All 256\-511 Octet Frame Count
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: transmitted_total_octet_frames_from512_to1023
            
            	All 512\-1023 Octet Frame Count
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: transmitted_total_octet_frames_from1024_to1518
            
            	All 1024\-1518 Octet Frame Count
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: transmitted_total_octet_frames_from1518_to_max
            
            	All > 1518 Octet Frame Count
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: transmitted_good_frames
            
            	Transmitted Good Frames
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: transmitted_unicast_frames
            
            	Transmitted unicast Frames
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: transmitted_multicast_frames
            
            	Transmitted multicast Frames
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: transmitted_broadcast_frames
            
            	Transmitted broadcast Frames
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: buffer_underrun_packet_drops
            
            	Drops due to buffer underrun
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: aborted_packet_drops
            
            	Drops due to packet abort
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: uncounted_dropped_frames
            
            	Any other drops not counted
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: miscellaneous_output_errors
            
            	Any other errors not counted
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            

            """

            _prefix = 'drivers-media-eth-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(EthernetInterface.Statistics.Statistic, self).__init__()

                self.yang_name = "statistic"
                self.yang_parent_name = "statistics"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['interface_name']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                    ('received_total_bytes', (YLeaf(YType.uint64, 'received-total-bytes'), ['int'])),
                    ('received_good_bytes', (YLeaf(YType.uint64, 'received-good-bytes'), ['int'])),
                    ('received_total_frames', (YLeaf(YType.uint64, 'received-total-frames'), ['int'])),
                    ('received8021q_frames', (YLeaf(YType.uint64, 'received8021q-frames'), ['int'])),
                    ('received_pause_frames', (YLeaf(YType.uint64, 'received-pause-frames'), ['int'])),
                    ('received_unknown_opcodes', (YLeaf(YType.uint64, 'received-unknown-opcodes'), ['int'])),
                    ('received_total64_octet_frames', (YLeaf(YType.uint64, 'received-total64-octet-frames'), ['int'])),
                    ('received_total_octet_frames_from65_to127', (YLeaf(YType.uint64, 'received-total-octet-frames-from65-to127'), ['int'])),
                    ('received_total_octet_frames_from128_to255', (YLeaf(YType.uint64, 'received-total-octet-frames-from128-to255'), ['int'])),
                    ('received_total_octet_frames_from256_to511', (YLeaf(YType.uint64, 'received-total-octet-frames-from256-to511'), ['int'])),
                    ('received_total_octet_frames_from512_to1023', (YLeaf(YType.uint64, 'received-total-octet-frames-from512-to1023'), ['int'])),
                    ('received_total_octet_frames_from1024_to1518', (YLeaf(YType.uint64, 'received-total-octet-frames-from1024-to1518'), ['int'])),
                    ('received_total_octet_frames_from1519_to_max', (YLeaf(YType.uint64, 'received-total-octet-frames-from1519-to-max'), ['int'])),
                    ('received_good_frames', (YLeaf(YType.uint64, 'received-good-frames'), ['int'])),
                    ('received_unicast_frames', (YLeaf(YType.uint64, 'received-unicast-frames'), ['int'])),
                    ('received_multicast_frames', (YLeaf(YType.uint64, 'received-multicast-frames'), ['int'])),
                    ('received_broadcast_frames', (YLeaf(YType.uint64, 'received-broadcast-frames'), ['int'])),
                    ('number_of_buffer_overrun_packets_dropped', (YLeaf(YType.uint64, 'number-of-buffer-overrun-packets-dropped'), ['int'])),
                    ('number_of_aborted_packets_dropped', (YLeaf(YType.uint64, 'number-of-aborted-packets-dropped'), ['int'])),
                    ('numberof_invalid_vlan_id_packets_dropped', (YLeaf(YType.uint64, 'numberof-invalid-vlan-id-packets-dropped'), ['int'])),
                    ('invalid_dest_mac_drop_packets', (YLeaf(YType.uint64, 'invalid-dest-mac-drop-packets'), ['int'])),
                    ('invalid_encap_drop_packets', (YLeaf(YType.uint64, 'invalid-encap-drop-packets'), ['int'])),
                    ('number_of_miscellaneous_packets_dropped', (YLeaf(YType.uint64, 'number-of-miscellaneous-packets-dropped'), ['int'])),
                    ('dropped_giant_packets_greaterthan_mru', (YLeaf(YType.uint64, 'dropped-giant-packets-greaterthan-mru'), ['int'])),
                    ('dropped_ether_stats_undersize_pkts', (YLeaf(YType.uint64, 'dropped-ether-stats-undersize-pkts'), ['int'])),
                    ('dropped_jabbers_packets_greaterthan_mru', (YLeaf(YType.uint64, 'dropped-jabbers-packets-greaterthan-mru'), ['int'])),
                    ('dropped_ether_stats_fragments', (YLeaf(YType.uint64, 'dropped-ether-stats-fragments'), ['int'])),
                    ('dropped_packets_with_crc_align_errors', (YLeaf(YType.uint64, 'dropped-packets-with-crc-align-errors'), ['int'])),
                    ('ether_stats_collisions', (YLeaf(YType.uint64, 'ether-stats-collisions'), ['int'])),
                    ('symbol_errors', (YLeaf(YType.uint64, 'symbol-errors'), ['int'])),
                    ('dropped_miscellaneous_error_packets', (YLeaf(YType.uint64, 'dropped-miscellaneous-error-packets'), ['int'])),
                    ('rfc2819_ether_stats_oversized_pkts', (YLeaf(YType.uint64, 'rfc2819-ether-stats-oversized-pkts'), ['int'])),
                    ('rfc2819_ether_stats_jabbers', (YLeaf(YType.uint64, 'rfc2819-ether-stats-jabbers'), ['int'])),
                    ('rfc2819_ether_stats_crc_align_errors', (YLeaf(YType.uint64, 'rfc2819-ether-stats-crc-align-errors'), ['int'])),
                    ('rfc3635dot3_stats_alignment_errors', (YLeaf(YType.uint64, 'rfc3635dot3-stats-alignment-errors'), ['int'])),
                    ('total_bytes_transmitted', (YLeaf(YType.uint64, 'total-bytes-transmitted'), ['int'])),
                    ('total_good_bytes_transmitted', (YLeaf(YType.uint64, 'total-good-bytes-transmitted'), ['int'])),
                    ('total_frames_transmitted', (YLeaf(YType.uint64, 'total-frames-transmitted'), ['int'])),
                    ('transmitted8021q_frames', (YLeaf(YType.uint64, 'transmitted8021q-frames'), ['int'])),
                    ('transmitted_total_pause_frames', (YLeaf(YType.uint64, 'transmitted-total-pause-frames'), ['int'])),
                    ('transmitted_total64_octet_frames', (YLeaf(YType.uint64, 'transmitted-total64-octet-frames'), ['int'])),
                    ('transmitted_total_octet_frames_from65_to127', (YLeaf(YType.uint64, 'transmitted-total-octet-frames-from65-to127'), ['int'])),
                    ('transmitted_total_octet_frames_from128_to255', (YLeaf(YType.uint64, 'transmitted-total-octet-frames-from128-to255'), ['int'])),
                    ('transmitted_total_octet_frames_from256_to511', (YLeaf(YType.uint64, 'transmitted-total-octet-frames-from256-to511'), ['int'])),
                    ('transmitted_total_octet_frames_from512_to1023', (YLeaf(YType.uint64, 'transmitted-total-octet-frames-from512-to1023'), ['int'])),
                    ('transmitted_total_octet_frames_from1024_to1518', (YLeaf(YType.uint64, 'transmitted-total-octet-frames-from1024-to1518'), ['int'])),
                    ('transmitted_total_octet_frames_from1518_to_max', (YLeaf(YType.uint64, 'transmitted-total-octet-frames-from1518-to-max'), ['int'])),
                    ('transmitted_good_frames', (YLeaf(YType.uint64, 'transmitted-good-frames'), ['int'])),
                    ('transmitted_unicast_frames', (YLeaf(YType.uint64, 'transmitted-unicast-frames'), ['int'])),
                    ('transmitted_multicast_frames', (YLeaf(YType.uint64, 'transmitted-multicast-frames'), ['int'])),
                    ('transmitted_broadcast_frames', (YLeaf(YType.uint64, 'transmitted-broadcast-frames'), ['int'])),
                    ('buffer_underrun_packet_drops', (YLeaf(YType.uint64, 'buffer-underrun-packet-drops'), ['int'])),
                    ('aborted_packet_drops', (YLeaf(YType.uint64, 'aborted-packet-drops'), ['int'])),
                    ('uncounted_dropped_frames', (YLeaf(YType.uint64, 'uncounted-dropped-frames'), ['int'])),
                    ('miscellaneous_output_errors', (YLeaf(YType.uint64, 'miscellaneous-output-errors'), ['int'])),
                ])
                self.interface_name = None
                self.received_total_bytes = None
                self.received_good_bytes = None
                self.received_total_frames = None
                self.received8021q_frames = None
                self.received_pause_frames = None
                self.received_unknown_opcodes = None
                self.received_total64_octet_frames = None
                self.received_total_octet_frames_from65_to127 = None
                self.received_total_octet_frames_from128_to255 = None
                self.received_total_octet_frames_from256_to511 = None
                self.received_total_octet_frames_from512_to1023 = None
                self.received_total_octet_frames_from1024_to1518 = None
                self.received_total_octet_frames_from1519_to_max = None
                self.received_good_frames = None
                self.received_unicast_frames = None
                self.received_multicast_frames = None
                self.received_broadcast_frames = None
                self.number_of_buffer_overrun_packets_dropped = None
                self.number_of_aborted_packets_dropped = None
                self.numberof_invalid_vlan_id_packets_dropped = None
                self.invalid_dest_mac_drop_packets = None
                self.invalid_encap_drop_packets = None
                self.number_of_miscellaneous_packets_dropped = None
                self.dropped_giant_packets_greaterthan_mru = None
                self.dropped_ether_stats_undersize_pkts = None
                self.dropped_jabbers_packets_greaterthan_mru = None
                self.dropped_ether_stats_fragments = None
                self.dropped_packets_with_crc_align_errors = None
                self.ether_stats_collisions = None
                self.symbol_errors = None
                self.dropped_miscellaneous_error_packets = None
                self.rfc2819_ether_stats_oversized_pkts = None
                self.rfc2819_ether_stats_jabbers = None
                self.rfc2819_ether_stats_crc_align_errors = None
                self.rfc3635dot3_stats_alignment_errors = None
                self.total_bytes_transmitted = None
                self.total_good_bytes_transmitted = None
                self.total_frames_transmitted = None
                self.transmitted8021q_frames = None
                self.transmitted_total_pause_frames = None
                self.transmitted_total64_octet_frames = None
                self.transmitted_total_octet_frames_from65_to127 = None
                self.transmitted_total_octet_frames_from128_to255 = None
                self.transmitted_total_octet_frames_from256_to511 = None
                self.transmitted_total_octet_frames_from512_to1023 = None
                self.transmitted_total_octet_frames_from1024_to1518 = None
                self.transmitted_total_octet_frames_from1518_to_max = None
                self.transmitted_good_frames = None
                self.transmitted_unicast_frames = None
                self.transmitted_multicast_frames = None
                self.transmitted_broadcast_frames = None
                self.buffer_underrun_packet_drops = None
                self.aborted_packet_drops = None
                self.uncounted_dropped_frames = None
                self.miscellaneous_output_errors = None
                self._segment_path = lambda: "statistic" + "[interface-name='" + str(self.interface_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-drivers-media-eth-oper:ethernet-interface/statistics/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(EthernetInterface.Statistics.Statistic, ['interface_name', 'received_total_bytes', 'received_good_bytes', 'received_total_frames', 'received8021q_frames', 'received_pause_frames', 'received_unknown_opcodes', 'received_total64_octet_frames', 'received_total_octet_frames_from65_to127', 'received_total_octet_frames_from128_to255', 'received_total_octet_frames_from256_to511', 'received_total_octet_frames_from512_to1023', 'received_total_octet_frames_from1024_to1518', 'received_total_octet_frames_from1519_to_max', 'received_good_frames', 'received_unicast_frames', 'received_multicast_frames', 'received_broadcast_frames', 'number_of_buffer_overrun_packets_dropped', 'number_of_aborted_packets_dropped', 'numberof_invalid_vlan_id_packets_dropped', 'invalid_dest_mac_drop_packets', 'invalid_encap_drop_packets', 'number_of_miscellaneous_packets_dropped', 'dropped_giant_packets_greaterthan_mru', 'dropped_ether_stats_undersize_pkts', 'dropped_jabbers_packets_greaterthan_mru', 'dropped_ether_stats_fragments', 'dropped_packets_with_crc_align_errors', 'ether_stats_collisions', 'symbol_errors', 'dropped_miscellaneous_error_packets', 'rfc2819_ether_stats_oversized_pkts', 'rfc2819_ether_stats_jabbers', 'rfc2819_ether_stats_crc_align_errors', 'rfc3635dot3_stats_alignment_errors', 'total_bytes_transmitted', 'total_good_bytes_transmitted', 'total_frames_transmitted', 'transmitted8021q_frames', 'transmitted_total_pause_frames', 'transmitted_total64_octet_frames', 'transmitted_total_octet_frames_from65_to127', 'transmitted_total_octet_frames_from128_to255', 'transmitted_total_octet_frames_from256_to511', 'transmitted_total_octet_frames_from512_to1023', 'transmitted_total_octet_frames_from1024_to1518', 'transmitted_total_octet_frames_from1518_to_max', 'transmitted_good_frames', 'transmitted_unicast_frames', 'transmitted_multicast_frames', 'transmitted_broadcast_frames', 'buffer_underrun_packet_drops', 'aborted_packet_drops', 'uncounted_dropped_frames', 'miscellaneous_output_errors'], name, value)


    class Interfaces(Entity):
        """
        Ethernet controller info table
        
        .. attribute:: interface
        
        	Ethernet controller information
        	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Interfaces.Interface>`
        
        

        """

        _prefix = 'drivers-media-eth-oper'
        _revision = '2017-05-01'

        def __init__(self):
            super(EthernetInterface.Interfaces, self).__init__()

            self.yang_name = "interfaces"
            self.yang_parent_name = "ethernet-interface"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("interface", ("interface", EthernetInterface.Interfaces.Interface))])
            self._leafs = OrderedDict()

            self.interface = YList(self)
            self._segment_path = lambda: "interfaces"
            self._absolute_path = lambda: "Cisco-IOS-XR-drivers-media-eth-oper:ethernet-interface/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(EthernetInterface.Interfaces, [], name, value)


        class Interface(Entity):
            """
            Ethernet controller information
            
            .. attribute:: interface_name  (key)
            
            	The name of the interface
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
            
            .. attribute:: phy_info
            
            	PHY information
            	**type**\:  :py:class:`PhyInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Interfaces.Interface.PhyInfo>`
            
            .. attribute:: layer1_info
            
            	Layer 1 information
            	**type**\:  :py:class:`Layer1Info <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Interfaces.Interface.Layer1Info>`
            
            .. attribute:: mac_info
            
            	MAC Layer information
            	**type**\:  :py:class:`MacInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Interfaces.Interface.MacInfo>`
            
            .. attribute:: transport_info
            
            	Transport state information
            	**type**\:  :py:class:`TransportInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Interfaces.Interface.TransportInfo>`
            
            .. attribute:: admin_state
            
            	Port Administrative State
            	**type**\:  :py:class:`EthernetPortEnable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetPortEnable>`
            
            .. attribute:: oper_state_up
            
            	Port Operational state \- TRUE if up
            	**type**\: bool
            
            

            """

            _prefix = 'drivers-media-eth-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(EthernetInterface.Interfaces.Interface, self).__init__()

                self.yang_name = "interface"
                self.yang_parent_name = "interfaces"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['interface_name']
                self._child_classes = OrderedDict([("phy-info", ("phy_info", EthernetInterface.Interfaces.Interface.PhyInfo)), ("layer1-info", ("layer1_info", EthernetInterface.Interfaces.Interface.Layer1Info)), ("mac-info", ("mac_info", EthernetInterface.Interfaces.Interface.MacInfo)), ("transport-info", ("transport_info", EthernetInterface.Interfaces.Interface.TransportInfo))])
                self._leafs = OrderedDict([
                    ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                    ('admin_state', (YLeaf(YType.enumeration, 'admin-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper', 'EthernetPortEnable', '')])),
                    ('oper_state_up', (YLeaf(YType.boolean, 'oper-state-up'), ['bool'])),
                ])
                self.interface_name = None
                self.admin_state = None
                self.oper_state_up = None

                self.phy_info = EthernetInterface.Interfaces.Interface.PhyInfo()
                self.phy_info.parent = self
                self._children_name_map["phy_info"] = "phy-info"

                self.layer1_info = EthernetInterface.Interfaces.Interface.Layer1Info()
                self.layer1_info.parent = self
                self._children_name_map["layer1_info"] = "layer1-info"

                self.mac_info = EthernetInterface.Interfaces.Interface.MacInfo()
                self.mac_info.parent = self
                self._children_name_map["mac_info"] = "mac-info"

                self.transport_info = EthernetInterface.Interfaces.Interface.TransportInfo()
                self.transport_info.parent = self
                self._children_name_map["transport_info"] = "transport-info"
                self._segment_path = lambda: "interface" + "[interface-name='" + str(self.interface_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-drivers-media-eth-oper:ethernet-interface/interfaces/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(EthernetInterface.Interfaces.Interface, ['interface_name', 'admin_state', 'oper_state_up'], name, value)


            class PhyInfo(Entity):
                """
                PHY information
                
                .. attribute:: phy_details
                
                	Details about the PHY
                	**type**\:  :py:class:`PhyDetails <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails>`
                
                .. attribute:: fec_details
                
                	Forward Error Correction information
                	**type**\:  :py:class:`FecDetails <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Interfaces.Interface.PhyInfo.FecDetails>`
                
                .. attribute:: media_type
                
                	Port media type
                	**type**\:  :py:class:`EthernetMedia <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetMedia>`
                
                .. attribute:: phy_present
                
                	Presence of PHY
                	**type**\:  :py:class:`EtherPhyPresent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EtherPhyPresent>`
                
                .. attribute:: loopback
                
                	Port operational loopback
                	**type**\:  :py:class:`EthernetLoopback <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetLoopback>`
                
                .. attribute:: holdoff_time
                
                	Holdoff Time
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: extended_loopback
                
                	Port operational extended loopback
                	**type**\: list of  		 :py:class:`ExtendedLoopback <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Interfaces.Interface.PhyInfo.ExtendedLoopback>`
                
                

                """

                _prefix = 'drivers-media-eth-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(EthernetInterface.Interfaces.Interface.PhyInfo, self).__init__()

                    self.yang_name = "phy-info"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("phy-details", ("phy_details", EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails)), ("fec-details", ("fec_details", EthernetInterface.Interfaces.Interface.PhyInfo.FecDetails)), ("extended-loopback", ("extended_loopback", EthernetInterface.Interfaces.Interface.PhyInfo.ExtendedLoopback))])
                    self._leafs = OrderedDict([
                        ('media_type', (YLeaf(YType.enumeration, 'media-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper', 'EthernetMedia', '')])),
                        ('phy_present', (YLeaf(YType.enumeration, 'phy-present'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper', 'EtherPhyPresent', '')])),
                        ('loopback', (YLeaf(YType.enumeration, 'loopback'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper', 'EthernetLoopback', '')])),
                        ('holdoff_time', (YLeaf(YType.uint32, 'holdoff-time'), ['int'])),
                    ])
                    self.media_type = None
                    self.phy_present = None
                    self.loopback = None
                    self.holdoff_time = None

                    self.phy_details = EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails()
                    self.phy_details.parent = self
                    self._children_name_map["phy_details"] = "phy-details"

                    self.fec_details = EthernetInterface.Interfaces.Interface.PhyInfo.FecDetails()
                    self.fec_details.parent = self
                    self._children_name_map["fec_details"] = "fec-details"

                    self.extended_loopback = YList(self)
                    self._segment_path = lambda: "phy-info"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(EthernetInterface.Interfaces.Interface.PhyInfo, ['media_type', 'phy_present', 'loopback', 'holdoff_time'], name, value)


                class PhyDetails(Entity):
                    """
                    Details about the PHY
                    
                    .. attribute:: lane_field_validity
                    
                    	Digital Optical Monitoring (per lane information) validity
                    	**type**\:  :py:class:`LaneFieldValidity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails.LaneFieldValidity>`
                    
                    .. attribute:: dig_opt_mon_alarm_thresholds
                    
                    	Digital Optical Monitoring alarm thresholds
                    	**type**\:  :py:class:`DigOptMonAlarmThresholds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails.DigOptMonAlarmThresholds>`
                    
                    .. attribute:: dig_opt_mon_alarms
                    
                    	Digital Optical Monitoring alarms
                    	**type**\:  :py:class:`DigOptMonAlarms <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails.DigOptMonAlarms>`
                    
                    .. attribute:: vendor
                    
                    	Name of the port optics manufacturer
                    	**type**\: str
                    
                    .. attribute:: vendor_part_number
                    
                    	Part number for the port optics
                    	**type**\: str
                    
                    .. attribute:: vendor_serial_number
                    
                    	Serial number for the port optics
                    	**type**\: str
                    
                    .. attribute:: transceiver_temperature
                    
                    	The temperature of the transceiver (mDegrees C)
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: transceiver_voltage
                    
                    	The input voltage to the transceiver (mV)
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: transceiver_tx_power
                    
                    	The transceiver transmit laser power (uW)
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: transceiver_rx_power
                    
                    	The transceiver receive optical power (uW)
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: transceiver_tx_bias
                    
                    	The laser bias of the transceiver (uA)
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: optics_wavelength
                    
                    	Wavelength of the optics being used in nm \* 1000
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: optics_type
                    
                    	Optics module type
                    	**type**\: str
                    
                    .. attribute:: revision_number
                    
                    	Module revision number
                    	**type**\: str
                    
                    .. attribute:: lane
                    
                    	Digital Optical Monitoring (per lane information)
                    	**type**\: list of  		 :py:class:`Lane <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails.Lane>`
                    
                    

                    """

                    _prefix = 'drivers-media-eth-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails, self).__init__()

                        self.yang_name = "phy-details"
                        self.yang_parent_name = "phy-info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("lane-field-validity", ("lane_field_validity", EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails.LaneFieldValidity)), ("dig-opt-mon-alarm-thresholds", ("dig_opt_mon_alarm_thresholds", EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails.DigOptMonAlarmThresholds)), ("dig-opt-mon-alarms", ("dig_opt_mon_alarms", EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails.DigOptMonAlarms)), ("lane", ("lane", EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails.Lane))])
                        self._leafs = OrderedDict([
                            ('vendor', (YLeaf(YType.str, 'vendor'), ['str'])),
                            ('vendor_part_number', (YLeaf(YType.str, 'vendor-part-number'), ['str'])),
                            ('vendor_serial_number', (YLeaf(YType.str, 'vendor-serial-number'), ['str'])),
                            ('transceiver_temperature', (YLeaf(YType.int32, 'transceiver-temperature'), ['int'])),
                            ('transceiver_voltage', (YLeaf(YType.int32, 'transceiver-voltage'), ['int'])),
                            ('transceiver_tx_power', (YLeaf(YType.int32, 'transceiver-tx-power'), ['int'])),
                            ('transceiver_rx_power', (YLeaf(YType.int32, 'transceiver-rx-power'), ['int'])),
                            ('transceiver_tx_bias', (YLeaf(YType.int32, 'transceiver-tx-bias'), ['int'])),
                            ('optics_wavelength', (YLeaf(YType.uint32, 'optics-wavelength'), ['int'])),
                            ('optics_type', (YLeaf(YType.str, 'optics-type'), ['str'])),
                            ('revision_number', (YLeaf(YType.str, 'revision-number'), ['str'])),
                        ])
                        self.vendor = None
                        self.vendor_part_number = None
                        self.vendor_serial_number = None
                        self.transceiver_temperature = None
                        self.transceiver_voltage = None
                        self.transceiver_tx_power = None
                        self.transceiver_rx_power = None
                        self.transceiver_tx_bias = None
                        self.optics_wavelength = None
                        self.optics_type = None
                        self.revision_number = None

                        self.lane_field_validity = EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails.LaneFieldValidity()
                        self.lane_field_validity.parent = self
                        self._children_name_map["lane_field_validity"] = "lane-field-validity"

                        self.dig_opt_mon_alarm_thresholds = EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails.DigOptMonAlarmThresholds()
                        self.dig_opt_mon_alarm_thresholds.parent = self
                        self._children_name_map["dig_opt_mon_alarm_thresholds"] = "dig-opt-mon-alarm-thresholds"

                        self.dig_opt_mon_alarms = EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails.DigOptMonAlarms()
                        self.dig_opt_mon_alarms.parent = self
                        self._children_name_map["dig_opt_mon_alarms"] = "dig-opt-mon-alarms"

                        self.lane = YList(self)
                        self._segment_path = lambda: "phy-details"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails, ['vendor', 'vendor_part_number', 'vendor_serial_number', 'transceiver_temperature', 'transceiver_voltage', 'transceiver_tx_power', 'transceiver_rx_power', 'transceiver_tx_bias', 'optics_wavelength', 'optics_type', 'revision_number'], name, value)


                    class LaneFieldValidity(Entity):
                        """
                        Digital Optical Monitoring (per lane
                        information) validity
                        
                        .. attribute:: wavelength_valid
                        
                        	The wavelength 'per lane' field is valid
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: transmit_power_valid
                        
                        	The transmit power 'per lane' field is valid
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: receive_power_valid
                        
                        	The receive power 'per lane' field is valid
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: laser_bias_valid
                        
                        	The laser bias 'per lane' field is valid
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        

                        """

                        _prefix = 'drivers-media-eth-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails.LaneFieldValidity, self).__init__()

                            self.yang_name = "lane-field-validity"
                            self.yang_parent_name = "phy-details"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('wavelength_valid', (YLeaf(YType.int32, 'wavelength-valid'), ['int'])),
                                ('transmit_power_valid', (YLeaf(YType.int32, 'transmit-power-valid'), ['int'])),
                                ('receive_power_valid', (YLeaf(YType.int32, 'receive-power-valid'), ['int'])),
                                ('laser_bias_valid', (YLeaf(YType.int32, 'laser-bias-valid'), ['int'])),
                            ])
                            self.wavelength_valid = None
                            self.transmit_power_valid = None
                            self.receive_power_valid = None
                            self.laser_bias_valid = None
                            self._segment_path = lambda: "lane-field-validity"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails.LaneFieldValidity, ['wavelength_valid', 'transmit_power_valid', 'receive_power_valid', 'laser_bias_valid'], name, value)


                    class DigOptMonAlarmThresholds(Entity):
                        """
                        Digital Optical Monitoring alarm thresholds
                        
                        .. attribute:: field_validity
                        
                        	Field validity
                        	**type**\:  :py:class:`FieldValidity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails.DigOptMonAlarmThresholds.FieldValidity>`
                        
                        .. attribute:: transceiver_temperature_alarm_high
                        
                        	Transceiver high temperature alarm threshold (mDegrees C)
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: transceiver_temperature_warning_high
                        
                        	Transceiver high temperature warning threshold (mDegrees C)
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: transceiver_temperature_warning_low
                        
                        	Transceiver low temperature warning threshold (mDegrees C)
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: transceiver_temperature_alarm_low
                        
                        	Transceiver low temperature alarm threshold (mDegrees C)
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: transceiver_voltage_alarm_high
                        
                        	Transceiver high voltage alarm threshold (mV)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: transceiver_voltage_warning_high
                        
                        	Transceiver high voltage warning threshold (mV)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: transceiver_voltage_warning_low
                        
                        	Transceiver low voltage warning threshold (mV)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: transceiver_voltage_alarm_low
                        
                        	Transceiver low voltage alarm threshold (mV)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: laser_bias_alarm_high
                        
                        	Laser bias high alarm threshold (uA)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: laser_bias_warning_high
                        
                        	Laser bias high warning threshold (uA)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: laser_bias_warning_low
                        
                        	Laser bias low warning threshold (uA)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: laser_bias_alarm_low
                        
                        	Laser bias low alarm threshold (uA)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: optical_transmit_power_alarm_high
                        
                        	High optical transmit power alarm threshold (uW)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: optical_transmit_power_warning_high
                        
                        	High optical transmit power warning threshold (uW)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: optical_transmit_power_warning_low
                        
                        	Low optical transmit power warning threshold (uW)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: optical_transmit_power_alarm_low
                        
                        	Low optical transmit power alarm threshold (uW)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: optical_receive_power_alarm_high
                        
                        	High optical receive power alarm threshold (uW)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: optical_receive_power_warning_high
                        
                        	High optical receive power warning threshold (uW)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: optical_receive_power_warning_low
                        
                        	Low optical receive power warning threshold (uW)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: optical_receive_power_alarm_low
                        
                        	Low optical receive power alarm threshold (uW)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'drivers-media-eth-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails.DigOptMonAlarmThresholds, self).__init__()

                            self.yang_name = "dig-opt-mon-alarm-thresholds"
                            self.yang_parent_name = "phy-details"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("field-validity", ("field_validity", EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails.DigOptMonAlarmThresholds.FieldValidity))])
                            self._leafs = OrderedDict([
                                ('transceiver_temperature_alarm_high', (YLeaf(YType.int32, 'transceiver-temperature-alarm-high'), ['int'])),
                                ('transceiver_temperature_warning_high', (YLeaf(YType.int32, 'transceiver-temperature-warning-high'), ['int'])),
                                ('transceiver_temperature_warning_low', (YLeaf(YType.int32, 'transceiver-temperature-warning-low'), ['int'])),
                                ('transceiver_temperature_alarm_low', (YLeaf(YType.int32, 'transceiver-temperature-alarm-low'), ['int'])),
                                ('transceiver_voltage_alarm_high', (YLeaf(YType.uint32, 'transceiver-voltage-alarm-high'), ['int'])),
                                ('transceiver_voltage_warning_high', (YLeaf(YType.uint32, 'transceiver-voltage-warning-high'), ['int'])),
                                ('transceiver_voltage_warning_low', (YLeaf(YType.uint32, 'transceiver-voltage-warning-low'), ['int'])),
                                ('transceiver_voltage_alarm_low', (YLeaf(YType.uint32, 'transceiver-voltage-alarm-low'), ['int'])),
                                ('laser_bias_alarm_high', (YLeaf(YType.uint32, 'laser-bias-alarm-high'), ['int'])),
                                ('laser_bias_warning_high', (YLeaf(YType.uint32, 'laser-bias-warning-high'), ['int'])),
                                ('laser_bias_warning_low', (YLeaf(YType.uint32, 'laser-bias-warning-low'), ['int'])),
                                ('laser_bias_alarm_low', (YLeaf(YType.uint32, 'laser-bias-alarm-low'), ['int'])),
                                ('optical_transmit_power_alarm_high', (YLeaf(YType.uint32, 'optical-transmit-power-alarm-high'), ['int'])),
                                ('optical_transmit_power_warning_high', (YLeaf(YType.uint32, 'optical-transmit-power-warning-high'), ['int'])),
                                ('optical_transmit_power_warning_low', (YLeaf(YType.uint32, 'optical-transmit-power-warning-low'), ['int'])),
                                ('optical_transmit_power_alarm_low', (YLeaf(YType.uint32, 'optical-transmit-power-alarm-low'), ['int'])),
                                ('optical_receive_power_alarm_high', (YLeaf(YType.uint32, 'optical-receive-power-alarm-high'), ['int'])),
                                ('optical_receive_power_warning_high', (YLeaf(YType.uint32, 'optical-receive-power-warning-high'), ['int'])),
                                ('optical_receive_power_warning_low', (YLeaf(YType.uint32, 'optical-receive-power-warning-low'), ['int'])),
                                ('optical_receive_power_alarm_low', (YLeaf(YType.uint32, 'optical-receive-power-alarm-low'), ['int'])),
                            ])
                            self.transceiver_temperature_alarm_high = None
                            self.transceiver_temperature_warning_high = None
                            self.transceiver_temperature_warning_low = None
                            self.transceiver_temperature_alarm_low = None
                            self.transceiver_voltage_alarm_high = None
                            self.transceiver_voltage_warning_high = None
                            self.transceiver_voltage_warning_low = None
                            self.transceiver_voltage_alarm_low = None
                            self.laser_bias_alarm_high = None
                            self.laser_bias_warning_high = None
                            self.laser_bias_warning_low = None
                            self.laser_bias_alarm_low = None
                            self.optical_transmit_power_alarm_high = None
                            self.optical_transmit_power_warning_high = None
                            self.optical_transmit_power_warning_low = None
                            self.optical_transmit_power_alarm_low = None
                            self.optical_receive_power_alarm_high = None
                            self.optical_receive_power_warning_high = None
                            self.optical_receive_power_warning_low = None
                            self.optical_receive_power_alarm_low = None

                            self.field_validity = EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails.DigOptMonAlarmThresholds.FieldValidity()
                            self.field_validity.parent = self
                            self._children_name_map["field_validity"] = "field-validity"
                            self._segment_path = lambda: "dig-opt-mon-alarm-thresholds"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails.DigOptMonAlarmThresholds, ['transceiver_temperature_alarm_high', 'transceiver_temperature_warning_high', 'transceiver_temperature_warning_low', 'transceiver_temperature_alarm_low', 'transceiver_voltage_alarm_high', 'transceiver_voltage_warning_high', 'transceiver_voltage_warning_low', 'transceiver_voltage_alarm_low', 'laser_bias_alarm_high', 'laser_bias_warning_high', 'laser_bias_warning_low', 'laser_bias_alarm_low', 'optical_transmit_power_alarm_high', 'optical_transmit_power_warning_high', 'optical_transmit_power_warning_low', 'optical_transmit_power_alarm_low', 'optical_receive_power_alarm_high', 'optical_receive_power_warning_high', 'optical_receive_power_warning_low', 'optical_receive_power_alarm_low'], name, value)


                        class FieldValidity(Entity):
                            """
                            Field validity
                            
                            .. attribute:: temperature_valid
                            
                            	The temperature fields are valid
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: voltage_valid
                            
                            	The voltage fields are valid
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: laser_bias_valid
                            
                            	The laser bias fields are valid
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: transmit_power_valid
                            
                            	The transmit power fields are valid
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: receive_power_valid
                            
                            	The receive power fields are valid
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            

                            """

                            _prefix = 'drivers-media-eth-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails.DigOptMonAlarmThresholds.FieldValidity, self).__init__()

                                self.yang_name = "field-validity"
                                self.yang_parent_name = "dig-opt-mon-alarm-thresholds"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('temperature_valid', (YLeaf(YType.int32, 'temperature-valid'), ['int'])),
                                    ('voltage_valid', (YLeaf(YType.int32, 'voltage-valid'), ['int'])),
                                    ('laser_bias_valid', (YLeaf(YType.int32, 'laser-bias-valid'), ['int'])),
                                    ('transmit_power_valid', (YLeaf(YType.int32, 'transmit-power-valid'), ['int'])),
                                    ('receive_power_valid', (YLeaf(YType.int32, 'receive-power-valid'), ['int'])),
                                ])
                                self.temperature_valid = None
                                self.voltage_valid = None
                                self.laser_bias_valid = None
                                self.transmit_power_valid = None
                                self.receive_power_valid = None
                                self._segment_path = lambda: "field-validity"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails.DigOptMonAlarmThresholds.FieldValidity, ['temperature_valid', 'voltage_valid', 'laser_bias_valid', 'transmit_power_valid', 'receive_power_valid'], name, value)


                    class DigOptMonAlarms(Entity):
                        """
                        Digital Optical Monitoring alarms
                        
                        .. attribute:: transceiver_temperature
                        
                        	Transceiver Temperature Alarm
                        	**type**\:  :py:class:`EtherDomAlarm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EtherDomAlarm>`
                        
                        .. attribute:: transceiver_voltage
                        
                        	Transceiver Voltage Alarm
                        	**type**\:  :py:class:`EtherDomAlarm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EtherDomAlarm>`
                        
                        .. attribute:: transmit_laser_power
                        
                        	Transmit Laser Power Alarm
                        	**type**\:  :py:class:`EtherDomAlarm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EtherDomAlarm>`
                        
                        .. attribute:: received_laser_power
                        
                        	Received Optical Power Alarm
                        	**type**\:  :py:class:`EtherDomAlarm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EtherDomAlarm>`
                        
                        .. attribute:: laser_bias_current
                        
                        	Laser Bias Current Alarm
                        	**type**\:  :py:class:`EtherDomAlarm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EtherDomAlarm>`
                        
                        

                        """

                        _prefix = 'drivers-media-eth-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails.DigOptMonAlarms, self).__init__()

                            self.yang_name = "dig-opt-mon-alarms"
                            self.yang_parent_name = "phy-details"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('transceiver_temperature', (YLeaf(YType.enumeration, 'transceiver-temperature'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper', 'EtherDomAlarm', '')])),
                                ('transceiver_voltage', (YLeaf(YType.enumeration, 'transceiver-voltage'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper', 'EtherDomAlarm', '')])),
                                ('transmit_laser_power', (YLeaf(YType.enumeration, 'transmit-laser-power'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper', 'EtherDomAlarm', '')])),
                                ('received_laser_power', (YLeaf(YType.enumeration, 'received-laser-power'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper', 'EtherDomAlarm', '')])),
                                ('laser_bias_current', (YLeaf(YType.enumeration, 'laser-bias-current'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper', 'EtherDomAlarm', '')])),
                            ])
                            self.transceiver_temperature = None
                            self.transceiver_voltage = None
                            self.transmit_laser_power = None
                            self.received_laser_power = None
                            self.laser_bias_current = None
                            self._segment_path = lambda: "dig-opt-mon-alarms"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails.DigOptMonAlarms, ['transceiver_temperature', 'transceiver_voltage', 'transmit_laser_power', 'received_laser_power', 'laser_bias_current'], name, value)


                    class Lane(Entity):
                        """
                        Digital Optical Monitoring (per lane
                        information)
                        
                        .. attribute:: dig_opt_mon_alarm
                        
                        	Digital Optical Monitoring alarms
                        	**type**\:  :py:class:`DigOptMonAlarm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails.Lane.DigOptMonAlarm>`
                        
                        .. attribute:: center_wavelength
                        
                        	Center Wavelength (nm\*1000)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: transmit_laser_power
                        
                        	Transmit Laser Power (dBm\*1000)
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: received_laser_power
                        
                        	Received Optical Power (dBm\*1000)
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: laser_bias_current
                        
                        	Laser Bias Current (uAmps)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: lane_id
                        
                        	Numerical identifier for this lane
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'drivers-media-eth-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails.Lane, self).__init__()

                            self.yang_name = "lane"
                            self.yang_parent_name = "phy-details"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("dig-opt-mon-alarm", ("dig_opt_mon_alarm", EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails.Lane.DigOptMonAlarm))])
                            self._leafs = OrderedDict([
                                ('center_wavelength', (YLeaf(YType.uint32, 'center-wavelength'), ['int'])),
                                ('transmit_laser_power', (YLeaf(YType.int32, 'transmit-laser-power'), ['int'])),
                                ('received_laser_power', (YLeaf(YType.int32, 'received-laser-power'), ['int'])),
                                ('laser_bias_current', (YLeaf(YType.uint32, 'laser-bias-current'), ['int'])),
                                ('lane_id', (YLeaf(YType.uint32, 'lane-id'), ['int'])),
                            ])
                            self.center_wavelength = None
                            self.transmit_laser_power = None
                            self.received_laser_power = None
                            self.laser_bias_current = None
                            self.lane_id = None

                            self.dig_opt_mon_alarm = EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails.Lane.DigOptMonAlarm()
                            self.dig_opt_mon_alarm.parent = self
                            self._children_name_map["dig_opt_mon_alarm"] = "dig-opt-mon-alarm"
                            self._segment_path = lambda: "lane"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails.Lane, ['center_wavelength', 'transmit_laser_power', 'received_laser_power', 'laser_bias_current', 'lane_id'], name, value)


                        class DigOptMonAlarm(Entity):
                            """
                            Digital Optical Monitoring alarms
                            
                            .. attribute:: transmit_laser_power
                            
                            	Transmit Laser Power Alarm
                            	**type**\:  :py:class:`EtherDomAlarm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EtherDomAlarm>`
                            
                            .. attribute:: received_laser_power
                            
                            	Received Optical Power Alarm
                            	**type**\:  :py:class:`EtherDomAlarm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EtherDomAlarm>`
                            
                            .. attribute:: laser_bias_current
                            
                            	Laser Bias Current Alarm
                            	**type**\:  :py:class:`EtherDomAlarm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EtherDomAlarm>`
                            
                            

                            """

                            _prefix = 'drivers-media-eth-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails.Lane.DigOptMonAlarm, self).__init__()

                                self.yang_name = "dig-opt-mon-alarm"
                                self.yang_parent_name = "lane"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('transmit_laser_power', (YLeaf(YType.enumeration, 'transmit-laser-power'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper', 'EtherDomAlarm', '')])),
                                    ('received_laser_power', (YLeaf(YType.enumeration, 'received-laser-power'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper', 'EtherDomAlarm', '')])),
                                    ('laser_bias_current', (YLeaf(YType.enumeration, 'laser-bias-current'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper', 'EtherDomAlarm', '')])),
                                ])
                                self.transmit_laser_power = None
                                self.received_laser_power = None
                                self.laser_bias_current = None
                                self._segment_path = lambda: "dig-opt-mon-alarm"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails.Lane.DigOptMonAlarm, ['transmit_laser_power', 'received_laser_power', 'laser_bias_current'], name, value)


                class FecDetails(Entity):
                    """
                    Forward Error Correction information
                    
                    .. attribute:: fec
                    
                    	Port operational FEC type
                    	**type**\:  :py:class:`EthernetFec <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetFec>`
                    
                    .. attribute:: corrected_codeword_count
                    
                    	Corrected codeword error count
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: uncorrected_codeword_count
                    
                    	Uncorrected codeword error count
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    

                    """

                    _prefix = 'drivers-media-eth-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(EthernetInterface.Interfaces.Interface.PhyInfo.FecDetails, self).__init__()

                        self.yang_name = "fec-details"
                        self.yang_parent_name = "phy-info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('fec', (YLeaf(YType.enumeration, 'fec'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper', 'EthernetFec', '')])),
                            ('corrected_codeword_count', (YLeaf(YType.uint64, 'corrected-codeword-count'), ['int'])),
                            ('uncorrected_codeword_count', (YLeaf(YType.uint64, 'uncorrected-codeword-count'), ['int'])),
                        ])
                        self.fec = None
                        self.corrected_codeword_count = None
                        self.uncorrected_codeword_count = None
                        self._segment_path = lambda: "fec-details"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(EthernetInterface.Interfaces.Interface.PhyInfo.FecDetails, ['fec', 'corrected_codeword_count', 'uncorrected_codeword_count'], name, value)


                class ExtendedLoopback(Entity):
                    """
                    Port operational extended loopback
                    
                    .. attribute:: level
                    
                    	Level
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: loopback
                    
                    	Port operational loopback
                    	**type**\:  :py:class:`EthernetLoopback <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetLoopback>`
                    
                    

                    """

                    _prefix = 'drivers-media-eth-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(EthernetInterface.Interfaces.Interface.PhyInfo.ExtendedLoopback, self).__init__()

                        self.yang_name = "extended-loopback"
                        self.yang_parent_name = "phy-info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('level', (YLeaf(YType.uint32, 'level'), ['int'])),
                            ('loopback', (YLeaf(YType.enumeration, 'loopback'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper', 'EthernetLoopback', '')])),
                        ])
                        self.level = None
                        self.loopback = None
                        self._segment_path = lambda: "extended-loopback"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(EthernetInterface.Interfaces.Interface.PhyInfo.ExtendedLoopback, ['level', 'loopback'], name, value)


            class Layer1Info(Entity):
                """
                Layer 1 information
                
                .. attribute:: autoneg
                
                	Port autonegotiation configuration settings
                	**type**\:  :py:class:`Autoneg <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Interfaces.Interface.Layer1Info.Autoneg>`
                
                .. attribute:: current_alarms
                
                	Current alarms
                	**type**\:  :py:class:`CurrentAlarms <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Interfaces.Interface.Layer1Info.CurrentAlarms>`
                
                .. attribute:: previous_alarms
                
                	Previous alarms
                	**type**\:  :py:class:`PreviousAlarms <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Interfaces.Interface.Layer1Info.PreviousAlarms>`
                
                .. attribute:: error_counts
                
                	Statistics for detected errors
                	**type**\:  :py:class:`ErrorCounts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Interfaces.Interface.Layer1Info.ErrorCounts>`
                
                .. attribute:: ber_monitoring
                
                	BER monitoring details
                	**type**\:  :py:class:`BerMonitoring <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Interfaces.Interface.Layer1Info.BerMonitoring>`
                
                .. attribute:: opd_monitoring
                
                	OPD monitoring details
                	**type**\:  :py:class:`OpdMonitoring <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Interfaces.Interface.Layer1Info.OpdMonitoring>`
                
                .. attribute:: pfc_info
                
                	Priority flow control information
                	**type**\:  :py:class:`PfcInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Interfaces.Interface.Layer1Info.PfcInfo>`
                
                .. attribute:: link_state
                
                	Link state
                	**type**\:  :py:class:`EtherLinkState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EtherLinkState>`
                
                .. attribute:: led_state
                
                	State of the LED
                	**type**\:  :py:class:`EtherLedState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EtherLedState>`
                
                .. attribute:: speed
                
                	Port operational speed
                	**type**\:  :py:class:`EthernetSpeed <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetSpeed>`
                
                .. attribute:: duplex
                
                	Port operational duplexity
                	**type**\:  :py:class:`EthernetDuplex <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetDuplex>`
                
                .. attribute:: flowcontrol
                
                	Port operational flow control
                	**type**\:  :py:class:`EtherFlowcontrol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EtherFlowcontrol>`
                
                .. attribute:: ipg
                
                	Port operational inter\-packet\-gap
                	**type**\:  :py:class:`EthernetIpg <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetIpg>`
                
                .. attribute:: laser_squelch_enabled
                
                	Laser Squelch \- TRUE if enabled
                	**type**\: bool
                
                .. attribute:: bandwidth_utilization
                
                	Bandwidth utilization (hundredths of a percent)
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: percentage
                
                .. attribute:: bandwidth
                
                	Port operational bandwidth
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'drivers-media-eth-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(EthernetInterface.Interfaces.Interface.Layer1Info, self).__init__()

                    self.yang_name = "layer1-info"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("autoneg", ("autoneg", EthernetInterface.Interfaces.Interface.Layer1Info.Autoneg)), ("current-alarms", ("current_alarms", EthernetInterface.Interfaces.Interface.Layer1Info.CurrentAlarms)), ("previous-alarms", ("previous_alarms", EthernetInterface.Interfaces.Interface.Layer1Info.PreviousAlarms)), ("error-counts", ("error_counts", EthernetInterface.Interfaces.Interface.Layer1Info.ErrorCounts)), ("ber-monitoring", ("ber_monitoring", EthernetInterface.Interfaces.Interface.Layer1Info.BerMonitoring)), ("opd-monitoring", ("opd_monitoring", EthernetInterface.Interfaces.Interface.Layer1Info.OpdMonitoring)), ("pfc-info", ("pfc_info", EthernetInterface.Interfaces.Interface.Layer1Info.PfcInfo))])
                    self._leafs = OrderedDict([
                        ('link_state', (YLeaf(YType.enumeration, 'link-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper', 'EtherLinkState', '')])),
                        ('led_state', (YLeaf(YType.enumeration, 'led-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper', 'EtherLedState', '')])),
                        ('speed', (YLeaf(YType.enumeration, 'speed'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper', 'EthernetSpeed', '')])),
                        ('duplex', (YLeaf(YType.enumeration, 'duplex'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper', 'EthernetDuplex', '')])),
                        ('flowcontrol', (YLeaf(YType.enumeration, 'flowcontrol'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper', 'EtherFlowcontrol', '')])),
                        ('ipg', (YLeaf(YType.enumeration, 'ipg'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper', 'EthernetIpg', '')])),
                        ('laser_squelch_enabled', (YLeaf(YType.boolean, 'laser-squelch-enabled'), ['bool'])),
                        ('bandwidth_utilization', (YLeaf(YType.uint32, 'bandwidth-utilization'), ['int'])),
                        ('bandwidth', (YLeaf(YType.uint64, 'bandwidth'), ['int'])),
                    ])
                    self.link_state = None
                    self.led_state = None
                    self.speed = None
                    self.duplex = None
                    self.flowcontrol = None
                    self.ipg = None
                    self.laser_squelch_enabled = None
                    self.bandwidth_utilization = None
                    self.bandwidth = None

                    self.autoneg = EthernetInterface.Interfaces.Interface.Layer1Info.Autoneg()
                    self.autoneg.parent = self
                    self._children_name_map["autoneg"] = "autoneg"

                    self.current_alarms = EthernetInterface.Interfaces.Interface.Layer1Info.CurrentAlarms()
                    self.current_alarms.parent = self
                    self._children_name_map["current_alarms"] = "current-alarms"

                    self.previous_alarms = EthernetInterface.Interfaces.Interface.Layer1Info.PreviousAlarms()
                    self.previous_alarms.parent = self
                    self._children_name_map["previous_alarms"] = "previous-alarms"

                    self.error_counts = EthernetInterface.Interfaces.Interface.Layer1Info.ErrorCounts()
                    self.error_counts.parent = self
                    self._children_name_map["error_counts"] = "error-counts"

                    self.ber_monitoring = EthernetInterface.Interfaces.Interface.Layer1Info.BerMonitoring()
                    self.ber_monitoring.parent = self
                    self._children_name_map["ber_monitoring"] = "ber-monitoring"

                    self.opd_monitoring = EthernetInterface.Interfaces.Interface.Layer1Info.OpdMonitoring()
                    self.opd_monitoring.parent = self
                    self._children_name_map["opd_monitoring"] = "opd-monitoring"

                    self.pfc_info = EthernetInterface.Interfaces.Interface.Layer1Info.PfcInfo()
                    self.pfc_info.parent = self
                    self._children_name_map["pfc_info"] = "pfc-info"
                    self._segment_path = lambda: "layer1-info"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(EthernetInterface.Interfaces.Interface.Layer1Info, ['link_state', 'led_state', 'speed', 'duplex', 'flowcontrol', 'ipg', 'laser_squelch_enabled', 'bandwidth_utilization', 'bandwidth'], name, value)


                class Autoneg(Entity):
                    """
                    Port autonegotiation configuration settings
                    
                    .. attribute:: autoneg_enabled
                    
                    	TRUE if autonegotiation is enabled
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: mask
                    
                    	Validity mask\: 0x1 speed, 0x2 duplex, 0x4 flowcontrol, 0x8 fec
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: speed
                    
                    	Restricted speed (if relevant bit is set in mask)
                    	**type**\:  :py:class:`EthernetSpeed <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetSpeed>`
                    
                    .. attribute:: duplex
                    
                    	Restricted duplex (if relevant bit is set in mask)
                    	**type**\:  :py:class:`EthernetDuplex <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetDuplex>`
                    
                    .. attribute:: flowcontrol
                    
                    	Restricted flowcontrol (if relevant bit is set in mask)
                    	**type**\:  :py:class:`EtherFlowcontrol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EtherFlowcontrol>`
                    
                    .. attribute:: config_override
                    
                    	If true, configuration overrides negotiated settings.  If false, negotiated settings in effect
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: fec
                    
                    	Restricted FEC (if revelevant bit is set in mask)
                    	**type**\:  :py:class:`EthernetFec <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetFec>`
                    
                    

                    """

                    _prefix = 'drivers-media-eth-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(EthernetInterface.Interfaces.Interface.Layer1Info.Autoneg, self).__init__()

                        self.yang_name = "autoneg"
                        self.yang_parent_name = "layer1-info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('autoneg_enabled', (YLeaf(YType.int32, 'autoneg-enabled'), ['int'])),
                            ('mask', (YLeaf(YType.uint32, 'mask'), ['int'])),
                            ('speed', (YLeaf(YType.enumeration, 'speed'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper', 'EthernetSpeed', '')])),
                            ('duplex', (YLeaf(YType.enumeration, 'duplex'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper', 'EthernetDuplex', '')])),
                            ('flowcontrol', (YLeaf(YType.enumeration, 'flowcontrol'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper', 'EtherFlowcontrol', '')])),
                            ('config_override', (YLeaf(YType.int32, 'config-override'), ['int'])),
                            ('fec', (YLeaf(YType.enumeration, 'fec'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper', 'EthernetFec', '')])),
                        ])
                        self.autoneg_enabled = None
                        self.mask = None
                        self.speed = None
                        self.duplex = None
                        self.flowcontrol = None
                        self.config_override = None
                        self.fec = None
                        self._segment_path = lambda: "autoneg"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(EthernetInterface.Interfaces.Interface.Layer1Info.Autoneg, ['autoneg_enabled', 'mask', 'speed', 'duplex', 'flowcontrol', 'config_override', 'fec'], name, value)


                class CurrentAlarms(Entity):
                    """
                    Current alarms
                    
                    .. attribute:: received_loss_of_signal_alarm
                    
                    	Received Loss of Signal
                    	**type**\:  :py:class:`EthCtrlrAlarmState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthCtrlrAlarmState>`
                    
                    .. attribute:: pcs_loss_of_block_lock_alarm
                    
                    	PCS Loss of Block Lock
                    	**type**\:  :py:class:`EthCtrlrAlarmState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthCtrlrAlarmState>`
                    
                    .. attribute:: local_fault_alarm
                    
                    	Local Fault
                    	**type**\:  :py:class:`EthCtrlrAlarmState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthCtrlrAlarmState>`
                    
                    .. attribute:: remote_fault_alarm
                    
                    	Remote Fault
                    	**type**\:  :py:class:`EthCtrlrAlarmState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthCtrlrAlarmState>`
                    
                    .. attribute:: sd_ber_alarm
                    
                    	SD BER
                    	**type**\:  :py:class:`EthCtrlrAlarmState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthCtrlrAlarmState>`
                    
                    .. attribute:: sf_ber_alarm
                    
                    	SF BER
                    	**type**\:  :py:class:`EthCtrlrAlarmState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthCtrlrAlarmState>`
                    
                    .. attribute:: loss_of_synchronization_data_alarm
                    
                    	Loss of Synchronization Data
                    	**type**\:  :py:class:`EthCtrlrAlarmState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthCtrlrAlarmState>`
                    
                    .. attribute:: hi_ber_alarm
                    
                    	Hi BER
                    	**type**\:  :py:class:`EthCtrlrAlarmState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthCtrlrAlarmState>`
                    
                    .. attribute:: squelch_alarm
                    
                    	Squelch
                    	**type**\:  :py:class:`EthCtrlrAlarmState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthCtrlrAlarmState>`
                    
                    .. attribute:: rx_opd_alarm
                    
                    	Rx OPD Alarm
                    	**type**\:  :py:class:`EthCtrlrAlarmState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthCtrlrAlarmState>`
                    
                    

                    """

                    _prefix = 'drivers-media-eth-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(EthernetInterface.Interfaces.Interface.Layer1Info.CurrentAlarms, self).__init__()

                        self.yang_name = "current-alarms"
                        self.yang_parent_name = "layer1-info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('received_loss_of_signal_alarm', (YLeaf(YType.enumeration, 'received-loss-of-signal-alarm'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper', 'EthCtrlrAlarmState', '')])),
                            ('pcs_loss_of_block_lock_alarm', (YLeaf(YType.enumeration, 'pcs-loss-of-block-lock-alarm'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper', 'EthCtrlrAlarmState', '')])),
                            ('local_fault_alarm', (YLeaf(YType.enumeration, 'local-fault-alarm'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper', 'EthCtrlrAlarmState', '')])),
                            ('remote_fault_alarm', (YLeaf(YType.enumeration, 'remote-fault-alarm'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper', 'EthCtrlrAlarmState', '')])),
                            ('sd_ber_alarm', (YLeaf(YType.enumeration, 'sd-ber-alarm'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper', 'EthCtrlrAlarmState', '')])),
                            ('sf_ber_alarm', (YLeaf(YType.enumeration, 'sf-ber-alarm'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper', 'EthCtrlrAlarmState', '')])),
                            ('loss_of_synchronization_data_alarm', (YLeaf(YType.enumeration, 'loss-of-synchronization-data-alarm'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper', 'EthCtrlrAlarmState', '')])),
                            ('hi_ber_alarm', (YLeaf(YType.enumeration, 'hi-ber-alarm'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper', 'EthCtrlrAlarmState', '')])),
                            ('squelch_alarm', (YLeaf(YType.enumeration, 'squelch-alarm'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper', 'EthCtrlrAlarmState', '')])),
                            ('rx_opd_alarm', (YLeaf(YType.enumeration, 'rx-opd-alarm'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper', 'EthCtrlrAlarmState', '')])),
                        ])
                        self.received_loss_of_signal_alarm = None
                        self.pcs_loss_of_block_lock_alarm = None
                        self.local_fault_alarm = None
                        self.remote_fault_alarm = None
                        self.sd_ber_alarm = None
                        self.sf_ber_alarm = None
                        self.loss_of_synchronization_data_alarm = None
                        self.hi_ber_alarm = None
                        self.squelch_alarm = None
                        self.rx_opd_alarm = None
                        self._segment_path = lambda: "current-alarms"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(EthernetInterface.Interfaces.Interface.Layer1Info.CurrentAlarms, ['received_loss_of_signal_alarm', 'pcs_loss_of_block_lock_alarm', 'local_fault_alarm', 'remote_fault_alarm', 'sd_ber_alarm', 'sf_ber_alarm', 'loss_of_synchronization_data_alarm', 'hi_ber_alarm', 'squelch_alarm', 'rx_opd_alarm'], name, value)


                class PreviousAlarms(Entity):
                    """
                    Previous alarms
                    
                    .. attribute:: received_loss_of_signal_alarm
                    
                    	Received Loss of Signal
                    	**type**\:  :py:class:`EthCtrlrAlarmState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthCtrlrAlarmState>`
                    
                    .. attribute:: pcs_loss_of_block_lock_alarm
                    
                    	PCS Loss of Block Lock
                    	**type**\:  :py:class:`EthCtrlrAlarmState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthCtrlrAlarmState>`
                    
                    .. attribute:: local_fault_alarm
                    
                    	Local Fault
                    	**type**\:  :py:class:`EthCtrlrAlarmState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthCtrlrAlarmState>`
                    
                    .. attribute:: remote_fault_alarm
                    
                    	Remote Fault
                    	**type**\:  :py:class:`EthCtrlrAlarmState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthCtrlrAlarmState>`
                    
                    .. attribute:: sd_ber_alarm
                    
                    	SD BER
                    	**type**\:  :py:class:`EthCtrlrAlarmState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthCtrlrAlarmState>`
                    
                    .. attribute:: sf_ber_alarm
                    
                    	SF BER
                    	**type**\:  :py:class:`EthCtrlrAlarmState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthCtrlrAlarmState>`
                    
                    .. attribute:: loss_of_synchronization_data_alarm
                    
                    	Loss of Synchronization Data
                    	**type**\:  :py:class:`EthCtrlrAlarmState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthCtrlrAlarmState>`
                    
                    .. attribute:: hi_ber_alarm
                    
                    	Hi BER
                    	**type**\:  :py:class:`EthCtrlrAlarmState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthCtrlrAlarmState>`
                    
                    .. attribute:: squelch_alarm
                    
                    	Squelch
                    	**type**\:  :py:class:`EthCtrlrAlarmState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthCtrlrAlarmState>`
                    
                    .. attribute:: rx_opd_alarm
                    
                    	Rx OPD Alarm
                    	**type**\:  :py:class:`EthCtrlrAlarmState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthCtrlrAlarmState>`
                    
                    

                    """

                    _prefix = 'drivers-media-eth-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(EthernetInterface.Interfaces.Interface.Layer1Info.PreviousAlarms, self).__init__()

                        self.yang_name = "previous-alarms"
                        self.yang_parent_name = "layer1-info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('received_loss_of_signal_alarm', (YLeaf(YType.enumeration, 'received-loss-of-signal-alarm'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper', 'EthCtrlrAlarmState', '')])),
                            ('pcs_loss_of_block_lock_alarm', (YLeaf(YType.enumeration, 'pcs-loss-of-block-lock-alarm'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper', 'EthCtrlrAlarmState', '')])),
                            ('local_fault_alarm', (YLeaf(YType.enumeration, 'local-fault-alarm'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper', 'EthCtrlrAlarmState', '')])),
                            ('remote_fault_alarm', (YLeaf(YType.enumeration, 'remote-fault-alarm'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper', 'EthCtrlrAlarmState', '')])),
                            ('sd_ber_alarm', (YLeaf(YType.enumeration, 'sd-ber-alarm'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper', 'EthCtrlrAlarmState', '')])),
                            ('sf_ber_alarm', (YLeaf(YType.enumeration, 'sf-ber-alarm'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper', 'EthCtrlrAlarmState', '')])),
                            ('loss_of_synchronization_data_alarm', (YLeaf(YType.enumeration, 'loss-of-synchronization-data-alarm'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper', 'EthCtrlrAlarmState', '')])),
                            ('hi_ber_alarm', (YLeaf(YType.enumeration, 'hi-ber-alarm'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper', 'EthCtrlrAlarmState', '')])),
                            ('squelch_alarm', (YLeaf(YType.enumeration, 'squelch-alarm'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper', 'EthCtrlrAlarmState', '')])),
                            ('rx_opd_alarm', (YLeaf(YType.enumeration, 'rx-opd-alarm'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper', 'EthCtrlrAlarmState', '')])),
                        ])
                        self.received_loss_of_signal_alarm = None
                        self.pcs_loss_of_block_lock_alarm = None
                        self.local_fault_alarm = None
                        self.remote_fault_alarm = None
                        self.sd_ber_alarm = None
                        self.sf_ber_alarm = None
                        self.loss_of_synchronization_data_alarm = None
                        self.hi_ber_alarm = None
                        self.squelch_alarm = None
                        self.rx_opd_alarm = None
                        self._segment_path = lambda: "previous-alarms"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(EthernetInterface.Interfaces.Interface.Layer1Info.PreviousAlarms, ['received_loss_of_signal_alarm', 'pcs_loss_of_block_lock_alarm', 'local_fault_alarm', 'remote_fault_alarm', 'sd_ber_alarm', 'sf_ber_alarm', 'loss_of_synchronization_data_alarm', 'hi_ber_alarm', 'squelch_alarm', 'rx_opd_alarm'], name, value)


                class ErrorCounts(Entity):
                    """
                    Statistics for detected errors
                    
                    .. attribute:: sync_header_errors
                    
                    	Sync\-header error count
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: pcsbip_errors
                    
                    	PCS BIP error count
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    

                    """

                    _prefix = 'drivers-media-eth-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(EthernetInterface.Interfaces.Interface.Layer1Info.ErrorCounts, self).__init__()

                        self.yang_name = "error-counts"
                        self.yang_parent_name = "layer1-info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('sync_header_errors', (YLeaf(YType.uint64, 'sync-header-errors'), ['int'])),
                            ('pcsbip_errors', (YLeaf(YType.uint64, 'pcsbip-errors'), ['int'])),
                        ])
                        self.sync_header_errors = None
                        self.pcsbip_errors = None
                        self._segment_path = lambda: "error-counts"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(EthernetInterface.Interfaces.Interface.Layer1Info.ErrorCounts, ['sync_header_errors', 'pcsbip_errors'], name, value)


                class BerMonitoring(Entity):
                    """
                    BER monitoring details
                    
                    .. attribute:: settings
                    
                    	The BER monitoring settings to be applied
                    	**type**\:  :py:class:`Settings <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Interfaces.Interface.Layer1Info.BerMonitoring.Settings>`
                    
                    .. attribute:: state
                    
                    	The BER state
                    	**type**\:  :py:class:`State <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Interfaces.Interface.Layer1Info.BerMonitoring.State>`
                    
                    .. attribute:: supported
                    
                    	Whether or not BER monitoring is supported
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    

                    """

                    _prefix = 'drivers-media-eth-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(EthernetInterface.Interfaces.Interface.Layer1Info.BerMonitoring, self).__init__()

                        self.yang_name = "ber-monitoring"
                        self.yang_parent_name = "layer1-info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("settings", ("settings", EthernetInterface.Interfaces.Interface.Layer1Info.BerMonitoring.Settings)), ("state", ("state", EthernetInterface.Interfaces.Interface.Layer1Info.BerMonitoring.State))])
                        self._leafs = OrderedDict([
                            ('supported', (YLeaf(YType.int32, 'supported'), ['int'])),
                        ])
                        self.supported = None

                        self.settings = EthernetInterface.Interfaces.Interface.Layer1Info.BerMonitoring.Settings()
                        self.settings.parent = self
                        self._children_name_map["settings"] = "settings"

                        self.state = EthernetInterface.Interfaces.Interface.Layer1Info.BerMonitoring.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"
                        self._segment_path = lambda: "ber-monitoring"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(EthernetInterface.Interfaces.Interface.Layer1Info.BerMonitoring, ['supported'], name, value)


                    class Settings(Entity):
                        """
                        The BER monitoring settings to be applied
                        
                        .. attribute:: signal_degrade_threshold
                        
                        	BER threshold for signal to degrade
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: signal_degrade_alarm
                        
                        	Report alarm to indicate signal degrade
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: signal_fail_threshold
                        
                        	BER threshold for signal to fail
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: signal_fail_alarm
                        
                        	Report alarm to indicate signal failure
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: signal_remote_fault
                        
                        	Whether drivers should signal remote faults
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        

                        """

                        _prefix = 'drivers-media-eth-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(EthernetInterface.Interfaces.Interface.Layer1Info.BerMonitoring.Settings, self).__init__()

                            self.yang_name = "settings"
                            self.yang_parent_name = "ber-monitoring"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('signal_degrade_threshold', (YLeaf(YType.uint32, 'signal-degrade-threshold'), ['int'])),
                                ('signal_degrade_alarm', (YLeaf(YType.int32, 'signal-degrade-alarm'), ['int'])),
                                ('signal_fail_threshold', (YLeaf(YType.uint32, 'signal-fail-threshold'), ['int'])),
                                ('signal_fail_alarm', (YLeaf(YType.int32, 'signal-fail-alarm'), ['int'])),
                                ('signal_remote_fault', (YLeaf(YType.int32, 'signal-remote-fault'), ['int'])),
                            ])
                            self.signal_degrade_threshold = None
                            self.signal_degrade_alarm = None
                            self.signal_fail_threshold = None
                            self.signal_fail_alarm = None
                            self.signal_remote_fault = None
                            self._segment_path = lambda: "settings"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(EthernetInterface.Interfaces.Interface.Layer1Info.BerMonitoring.Settings, ['signal_degrade_threshold', 'signal_degrade_alarm', 'signal_fail_threshold', 'signal_fail_alarm', 'signal_remote_fault'], name, value)


                    class State(Entity):
                        """
                        The BER state
                        
                        .. attribute:: sd_current_ber
                        
                        	Current SD\-BER
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sf_current_ber
                        
                        	Current SF\-BER
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'drivers-media-eth-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(EthernetInterface.Interfaces.Interface.Layer1Info.BerMonitoring.State, self).__init__()

                            self.yang_name = "state"
                            self.yang_parent_name = "ber-monitoring"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('sd_current_ber', (YLeaf(YType.uint32, 'sd-current-ber'), ['int'])),
                                ('sf_current_ber', (YLeaf(YType.uint32, 'sf-current-ber'), ['int'])),
                            ])
                            self.sd_current_ber = None
                            self.sf_current_ber = None
                            self._segment_path = lambda: "state"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(EthernetInterface.Interfaces.Interface.Layer1Info.BerMonitoring.State, ['sd_current_ber', 'sf_current_ber'], name, value)


                class OpdMonitoring(Entity):
                    """
                    OPD monitoring details
                    
                    .. attribute:: settings
                    
                    	The OPD monitoring settings to be applied
                    	**type**\:  :py:class:`Settings <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Interfaces.Interface.Layer1Info.OpdMonitoring.Settings>`
                    
                    .. attribute:: supported
                    
                    	Whether or not OPD monitoring is supported
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    

                    """

                    _prefix = 'drivers-media-eth-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(EthernetInterface.Interfaces.Interface.Layer1Info.OpdMonitoring, self).__init__()

                        self.yang_name = "opd-monitoring"
                        self.yang_parent_name = "layer1-info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("settings", ("settings", EthernetInterface.Interfaces.Interface.Layer1Info.OpdMonitoring.Settings))])
                        self._leafs = OrderedDict([
                            ('supported', (YLeaf(YType.int32, 'supported'), ['int'])),
                        ])
                        self.supported = None

                        self.settings = EthernetInterface.Interfaces.Interface.Layer1Info.OpdMonitoring.Settings()
                        self.settings.parent = self
                        self._children_name_map["settings"] = "settings"
                        self._segment_path = lambda: "opd-monitoring"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(EthernetInterface.Interfaces.Interface.Layer1Info.OpdMonitoring, ['supported'], name, value)


                    class Settings(Entity):
                        """
                        The OPD monitoring settings to be applied
                        
                        .. attribute:: received_optical_power_degrade_threshold_set
                        
                        	Rx\-OPD alarm threshold set?
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: received_optical_power_degrade_threshold
                        
                        	Rx\-OPD alarm threshold value
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        

                        """

                        _prefix = 'drivers-media-eth-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(EthernetInterface.Interfaces.Interface.Layer1Info.OpdMonitoring.Settings, self).__init__()

                            self.yang_name = "settings"
                            self.yang_parent_name = "opd-monitoring"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('received_optical_power_degrade_threshold_set', (YLeaf(YType.int32, 'received-optical-power-degrade-threshold-set'), ['int'])),
                                ('received_optical_power_degrade_threshold', (YLeaf(YType.int32, 'received-optical-power-degrade-threshold'), ['int'])),
                            ])
                            self.received_optical_power_degrade_threshold_set = None
                            self.received_optical_power_degrade_threshold = None
                            self._segment_path = lambda: "settings"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(EthernetInterface.Interfaces.Interface.Layer1Info.OpdMonitoring.Settings, ['received_optical_power_degrade_threshold_set', 'received_optical_power_degrade_threshold'], name, value)


                class PfcInfo(Entity):
                    """
                    Priority flow control information
                    
                    .. attribute:: priority_flowcontrol
                    
                    	Port operational priority flow control
                    	**type**\:  :py:class:`EtherPfc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EtherPfc>`
                    
                    .. attribute:: priority_enabled_bitmap
                    
                    	Priority bitmap
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: rx_frame
                    
                    	RX Frame counts
                    	**type**\: list of int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: tx_frame
                    
                    	TX Frame counts
                    	**type**\: list of int
                    
                    	**range:** 0..18446744073709551615
                    
                    

                    """

                    _prefix = 'drivers-media-eth-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(EthernetInterface.Interfaces.Interface.Layer1Info.PfcInfo, self).__init__()

                        self.yang_name = "pfc-info"
                        self.yang_parent_name = "layer1-info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('priority_flowcontrol', (YLeaf(YType.enumeration, 'priority-flowcontrol'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper', 'EtherPfc', '')])),
                            ('priority_enabled_bitmap', (YLeaf(YType.uint8, 'priority-enabled-bitmap'), ['int'])),
                            ('rx_frame', (YLeafList(YType.uint64, 'rx-frame'), ['int'])),
                            ('tx_frame', (YLeafList(YType.uint64, 'tx-frame'), ['int'])),
                        ])
                        self.priority_flowcontrol = None
                        self.priority_enabled_bitmap = None
                        self.rx_frame = []
                        self.tx_frame = []
                        self._segment_path = lambda: "pfc-info"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(EthernetInterface.Interfaces.Interface.Layer1Info.PfcInfo, ['priority_flowcontrol', 'priority_enabled_bitmap', 'rx_frame', 'tx_frame'], name, value)


            class MacInfo(Entity):
                """
                MAC Layer information
                
                .. attribute:: unicast_mac_filters
                
                	Port unicast MAC filter information
                	**type**\:  :py:class:`UnicastMacFilters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Interfaces.Interface.MacInfo.UnicastMacFilters>`
                
                .. attribute:: multicast_mac_filters
                
                	Port multicast MAC filter information
                	**type**\:  :py:class:`MulticastMacFilters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Interfaces.Interface.MacInfo.MulticastMacFilters>`
                
                .. attribute:: mtu
                
                	Port operational MTU
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: mru
                
                	Port operational MRU
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: burned_in_mac_address
                
                	Port Burned\-In MAC address
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                .. attribute:: operational_mac_address
                
                	Port operational MAC address
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                

                """

                _prefix = 'drivers-media-eth-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(EthernetInterface.Interfaces.Interface.MacInfo, self).__init__()

                    self.yang_name = "mac-info"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("unicast-mac-filters", ("unicast_mac_filters", EthernetInterface.Interfaces.Interface.MacInfo.UnicastMacFilters)), ("multicast-mac-filters", ("multicast_mac_filters", EthernetInterface.Interfaces.Interface.MacInfo.MulticastMacFilters))])
                    self._leafs = OrderedDict([
                        ('mtu', (YLeaf(YType.uint32, 'mtu'), ['int'])),
                        ('mru', (YLeaf(YType.uint32, 'mru'), ['int'])),
                        ('burned_in_mac_address', (YLeaf(YType.str, 'burned-in-mac-address'), ['str'])),
                        ('operational_mac_address', (YLeaf(YType.str, 'operational-mac-address'), ['str'])),
                    ])
                    self.mtu = None
                    self.mru = None
                    self.burned_in_mac_address = None
                    self.operational_mac_address = None

                    self.unicast_mac_filters = EthernetInterface.Interfaces.Interface.MacInfo.UnicastMacFilters()
                    self.unicast_mac_filters.parent = self
                    self._children_name_map["unicast_mac_filters"] = "unicast-mac-filters"

                    self.multicast_mac_filters = EthernetInterface.Interfaces.Interface.MacInfo.MulticastMacFilters()
                    self.multicast_mac_filters.parent = self
                    self._children_name_map["multicast_mac_filters"] = "multicast-mac-filters"
                    self._segment_path = lambda: "mac-info"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(EthernetInterface.Interfaces.Interface.MacInfo, ['mtu', 'mru', 'burned_in_mac_address', 'operational_mac_address'], name, value)


                class UnicastMacFilters(Entity):
                    """
                    Port unicast MAC filter information
                    
                    .. attribute:: unicast_mac_address
                    
                    	MAC addresses in the unicast ingress destination MAC filter
                    	**type**\: list of str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    

                    """

                    _prefix = 'drivers-media-eth-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(EthernetInterface.Interfaces.Interface.MacInfo.UnicastMacFilters, self).__init__()

                        self.yang_name = "unicast-mac-filters"
                        self.yang_parent_name = "mac-info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('unicast_mac_address', (YLeafList(YType.str, 'unicast-mac-address'), ['str'])),
                        ])
                        self.unicast_mac_address = []
                        self._segment_path = lambda: "unicast-mac-filters"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(EthernetInterface.Interfaces.Interface.MacInfo.UnicastMacFilters, ['unicast_mac_address'], name, value)


                class MulticastMacFilters(Entity):
                    """
                    Port multicast MAC filter information
                    
                    .. attribute:: multicast_promiscuous
                    
                    	Whether the port is in multicast promiscuous mode
                    	**type**\: bool
                    
                    .. attribute:: multicast_mac_address
                    
                    	MAC addresses in the multicast ingress destination MAC filter
                    	**type**\: list of  		 :py:class:`MulticastMacAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Interfaces.Interface.MacInfo.MulticastMacFilters.MulticastMacAddress>`
                    
                    

                    """

                    _prefix = 'drivers-media-eth-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(EthernetInterface.Interfaces.Interface.MacInfo.MulticastMacFilters, self).__init__()

                        self.yang_name = "multicast-mac-filters"
                        self.yang_parent_name = "mac-info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("multicast-mac-address", ("multicast_mac_address", EthernetInterface.Interfaces.Interface.MacInfo.MulticastMacFilters.MulticastMacAddress))])
                        self._leafs = OrderedDict([
                            ('multicast_promiscuous', (YLeaf(YType.boolean, 'multicast-promiscuous'), ['bool'])),
                        ])
                        self.multicast_promiscuous = None

                        self.multicast_mac_address = YList(self)
                        self._segment_path = lambda: "multicast-mac-filters"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(EthernetInterface.Interfaces.Interface.MacInfo.MulticastMacFilters, ['multicast_promiscuous'], name, value)


                    class MulticastMacAddress(Entity):
                        """
                        MAC addresses in the multicast ingress
                        destination MAC filter
                        
                        .. attribute:: mac_address
                        
                        	MAC address
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                        
                        .. attribute:: mask
                        
                        	Mask for this MAC address
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                        
                        

                        """

                        _prefix = 'drivers-media-eth-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(EthernetInterface.Interfaces.Interface.MacInfo.MulticastMacFilters.MulticastMacAddress, self).__init__()

                            self.yang_name = "multicast-mac-address"
                            self.yang_parent_name = "multicast-mac-filters"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('mac_address', (YLeaf(YType.str, 'mac-address'), ['str'])),
                                ('mask', (YLeaf(YType.str, 'mask'), ['str'])),
                            ])
                            self.mac_address = None
                            self.mask = None
                            self._segment_path = lambda: "multicast-mac-address"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(EthernetInterface.Interfaces.Interface.MacInfo.MulticastMacFilters.MulticastMacAddress, ['mac_address', 'mask'], name, value)


            class TransportInfo(Entity):
                """
                Transport state information
                
                .. attribute:: maintenance_mode_enabled
                
                	Maintenance Mode \- TRUE if enabled
                	**type**\: bool
                
                .. attribute:: ains_status
                
                	AINS Soak status
                	**type**\:  :py:class:`EtherAinsStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EtherAinsStatus>`
                
                .. attribute:: total_duration
                
                	Total duration (minutes) of AINS soak timer
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: minute
                
                .. attribute:: remaining_duration
                
                	Remaining duration (seconds) of AINS soak timer
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                

                """

                _prefix = 'drivers-media-eth-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(EthernetInterface.Interfaces.Interface.TransportInfo, self).__init__()

                    self.yang_name = "transport-info"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('maintenance_mode_enabled', (YLeaf(YType.boolean, 'maintenance-mode-enabled'), ['bool'])),
                        ('ains_status', (YLeaf(YType.enumeration, 'ains-status'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper', 'EtherAinsStatus', '')])),
                        ('total_duration', (YLeaf(YType.uint32, 'total-duration'), ['int'])),
                        ('remaining_duration', (YLeaf(YType.uint32, 'remaining-duration'), ['int'])),
                    ])
                    self.maintenance_mode_enabled = None
                    self.ains_status = None
                    self.total_duration = None
                    self.remaining_duration = None
                    self._segment_path = lambda: "transport-info"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(EthernetInterface.Interfaces.Interface.TransportInfo, ['maintenance_mode_enabled', 'ains_status', 'total_duration', 'remaining_duration'], name, value)


    class Berts(Entity):
        """
        Ethernet controller BERT table
        
        .. attribute:: bert
        
        	Ethernet BERT information
        	**type**\: list of  		 :py:class:`Bert <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Berts.Bert>`
        
        

        """

        _prefix = 'drivers-media-eth-oper'
        _revision = '2017-05-01'

        def __init__(self):
            super(EthernetInterface.Berts, self).__init__()

            self.yang_name = "berts"
            self.yang_parent_name = "ethernet-interface"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("bert", ("bert", EthernetInterface.Berts.Bert))])
            self._leafs = OrderedDict()

            self.bert = YList(self)
            self._segment_path = lambda: "berts"
            self._absolute_path = lambda: "Cisco-IOS-XR-drivers-media-eth-oper:ethernet-interface/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(EthernetInterface.Berts, [], name, value)


        class Bert(Entity):
            """
            Ethernet BERT information
            
            .. attribute:: interface_name  (key)
            
            	The name of the interface
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
            
            .. attribute:: bert_status
            
            	Current test status
            	**type**\:  :py:class:`BertStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Berts.Bert.BertStatus>`
            
            .. attribute:: time_left
            
            	Remaining time for this test in seconds
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: second
            
            .. attribute:: port_bert_interval
            
            	Port BERT interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'drivers-media-eth-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(EthernetInterface.Berts.Bert, self).__init__()

                self.yang_name = "bert"
                self.yang_parent_name = "berts"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['interface_name']
                self._child_classes = OrderedDict([("bert-status", ("bert_status", EthernetInterface.Berts.Bert.BertStatus))])
                self._leafs = OrderedDict([
                    ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                    ('time_left', (YLeaf(YType.uint32, 'time-left'), ['int'])),
                    ('port_bert_interval', (YLeaf(YType.uint32, 'port-bert-interval'), ['int'])),
                ])
                self.interface_name = None
                self.time_left = None
                self.port_bert_interval = None

                self.bert_status = EthernetInterface.Berts.Bert.BertStatus()
                self.bert_status.parent = self
                self._children_name_map["bert_status"] = "bert-status"
                self._segment_path = lambda: "bert" + "[interface-name='" + str(self.interface_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-drivers-media-eth-oper:ethernet-interface/berts/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(EthernetInterface.Berts.Bert, ['interface_name', 'time_left', 'port_bert_interval'], name, value)


            class BertStatus(Entity):
                """
                Current test status
                
                .. attribute:: bert_state_enabled
                
                	State
                	**type**\: bool
                
                .. attribute:: data_availability
                
                	Flag indicating available data
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: receive_count
                
                	Receive count (if 0x1 set in flag)
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: transmit_count
                
                	Transmit count (if 0x2 set in flag)
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: receive_errors
                
                	Received errors (if 0x4 set in flag)
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: error_type
                
                	Bit, block or frame error
                	**type**\:  :py:class:`EthernetBertErrCnt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetBertErrCnt>`
                
                .. attribute:: test_pattern
                
                	Test pattern
                	**type**\:  :py:class:`EthernetBertPattern <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetBertPattern>`
                
                .. attribute:: device_under_test
                
                	Device being tested
                	**type**\:  :py:class:`EthernetDev <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetDev>`
                
                .. attribute:: interface_device
                
                	Interface being tested
                	**type**\:  :py:class:`EthernetDevIf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetDevIf>`
                
                

                """

                _prefix = 'drivers-media-eth-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(EthernetInterface.Berts.Bert.BertStatus, self).__init__()

                    self.yang_name = "bert-status"
                    self.yang_parent_name = "bert"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('bert_state_enabled', (YLeaf(YType.boolean, 'bert-state-enabled'), ['bool'])),
                        ('data_availability', (YLeaf(YType.uint32, 'data-availability'), ['int'])),
                        ('receive_count', (YLeaf(YType.uint64, 'receive-count'), ['int'])),
                        ('transmit_count', (YLeaf(YType.uint64, 'transmit-count'), ['int'])),
                        ('receive_errors', (YLeaf(YType.uint64, 'receive-errors'), ['int'])),
                        ('error_type', (YLeaf(YType.enumeration, 'error-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper', 'EthernetBertErrCnt', '')])),
                        ('test_pattern', (YLeaf(YType.enumeration, 'test-pattern'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper', 'EthernetBertPattern', '')])),
                        ('device_under_test', (YLeaf(YType.enumeration, 'device-under-test'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper', 'EthernetDev', '')])),
                        ('interface_device', (YLeaf(YType.enumeration, 'interface-device'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper', 'EthernetDevIf', '')])),
                    ])
                    self.bert_state_enabled = None
                    self.data_availability = None
                    self.receive_count = None
                    self.transmit_count = None
                    self.receive_errors = None
                    self.error_type = None
                    self.test_pattern = None
                    self.device_under_test = None
                    self.interface_device = None
                    self._segment_path = lambda: "bert-status"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(EthernetInterface.Berts.Bert.BertStatus, ['bert_state_enabled', 'data_availability', 'receive_count', 'transmit_count', 'receive_errors', 'error_type', 'test_pattern', 'device_under_test', 'interface_device'], name, value)

    def clone_ptr(self):
        self._top_entity = EthernetInterface()
        return self._top_entity

