""" Cisco_IOS_XR_drivers_media_eth_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR drivers\-media\-eth package operational data.

This module contains definitions
for the following management objects\:
  ethernet\-interface\: Ethernet operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class EthCtrlrAlarmStateEnum(Enum):
    """
    EthCtrlrAlarmStateEnum

    Ethernet alarm state

    .. data:: alarm_not_supported = 0

    	Not supported on this interface

    .. data:: alarm_set = 1

    	Alarm set

    .. data:: alarm_not_set = 2

    	Alarm not set

    """

    alarm_not_supported = 0

    alarm_set = 1

    alarm_not_set = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
        return meta._meta_table['EthCtrlrAlarmStateEnum']


class EtherAinsStatusEnum(Enum):
    """
    EtherAinsStatusEnum

    Ether ains status

    .. data:: ains_soak_status_none = 0

    	AINS Soak timer not running

    .. data:: ains_soak_status_pending = 1

    	AINS Soak timer pending

    .. data:: ains_soak_status_running = 2

    	AINS Soak timer running

    """

    ains_soak_status_none = 0

    ains_soak_status_pending = 1

    ains_soak_status_running = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
        return meta._meta_table['EtherAinsStatusEnum']


class EtherDomAlarmEnum(Enum):
    """
    EtherDomAlarmEnum

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

    no_information = 0

    alarm_high = 1

    warning_high = 2

    normal = 3

    warning_low = 4

    alarm_low = 5


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
        return meta._meta_table['EtherDomAlarmEnum']


class EtherFlowcontrolEnum(Enum):
    """
    EtherFlowcontrolEnum

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

    no_flowcontrol = 0

    egress = 1

    ingress = 2

    bidirectional = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
        return meta._meta_table['EtherFlowcontrolEnum']


class EtherLedStateEnum(Enum):
    """
    EtherLedStateEnum

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

    led_state_unknown = 0

    led_off = 1

    green_on = 2

    green_flashing = 3

    yellow_on = 4

    yellow_flashing = 5

    red_on = 6

    red_flashing = 7


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
        return meta._meta_table['EtherLedStateEnum']


class EtherLinkStateEnum(Enum):
    """
    EtherLinkStateEnum

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

    state_undefined = 0

    unknown_state = 1

    available = 2

    not_available = 3

    remote_fault = 4

    invalid_signal = 5

    remote_jabber = 6

    link_loss = 7

    remote_test = 8

    offline = 9

    auto_neg_error = 10

    pmd_link_fault = 11

    frame_loss = 12

    signal_loss = 13

    link_fault = 14

    excessive_ber = 15

    dxs_link_fault = 16

    pxs_link_fault = 17

    security = 18

    phy_not_present = 19

    no_optic_license = 20

    unsupported_module = 21

    dwdm_laser_shut = 22

    wanphy_laser_shut = 23

    incompatible_config = 24

    system_error = 25

    wan_framing_error = 26

    otn_framing_error = 27


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
        return meta._meta_table['EtherLinkStateEnum']


class EtherPfcEnum(Enum):
    """
    EtherPfcEnum

    Priority flowcontrol type

    .. data:: no_pfc = 0

    	No priority flow control (disabled)

    .. data:: on = 1

    	Priority flow control enabled

    """

    no_pfc = 0

    on = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
        return meta._meta_table['EtherPfcEnum']


class EtherPhyPresentEnum(Enum):
    """
    EtherPhyPresentEnum

    Ether phy present

    .. data:: phy_not_present = 0

    	No PHY present

    .. data:: phy_present = 1

    	PHY is present

    .. data:: no_information = 2

    	State is unknown

    """

    phy_not_present = 0

    phy_present = 1

    no_information = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
        return meta._meta_table['EtherPhyPresentEnum']


class EthernetBertErrCntEnum(Enum):
    """
    EthernetBertErrCntEnum

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

    no_count_type = 0

    bit_error_count = 1

    frame_error_count = 2

    block_error_count = 3

    ethernet_bert_err_cnt_types = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
        return meta._meta_table['EthernetBertErrCntEnum']


class EthernetBertPatternEnum(Enum):
    """
    EthernetBertPatternEnum

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

    no_test_pattern = 0

    high_frequency = 1

    low_frequency = 2

    mixed_frequency = 3

    continuous_random = 4

    continuous_jitter = 5

    long_continuous_random = 6

    short_continuous_random = 7

    pseudorandom_seed_a = 8

    pseudorandom_seed_b = 9

    prbs31 = 10

    square_wave = 11

    pseudorandom = 12

    ethernet_bert_pattern_types = 13


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
        return meta._meta_table['EthernetBertPatternEnum']


class EthernetDevEnum(Enum):
    """
    EthernetDevEnum

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

    no_device = 0

    pma_pmd = 1

    wis = 2

    pcs = 3

    phy_xs = 4

    dte_xs = 5

    ethernet_num_dev = 6


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
        return meta._meta_table['EthernetDevEnum']


class EthernetDevIfEnum(Enum):
    """
    EthernetDevIfEnum

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

    no_interface = 0

    xgmii = 1

    xaui = 2

    ethernet_num_dev_if = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
        return meta._meta_table['EthernetDevIfEnum']


class EthernetDuplexEnum(Enum):
    """
    EthernetDuplexEnum

    Duplexity

    .. data:: ethernet_duplex_invalid = 0

    	ethernet duplex invalid

    .. data:: half_duplex = 1

    	half duplex

    .. data:: full_duplex = 2

    	full duplex

    """

    ethernet_duplex_invalid = 0

    half_duplex = 1

    full_duplex = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
        return meta._meta_table['EthernetDuplexEnum']


class EthernetFecEnum(Enum):
    """
    EthernetFecEnum

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

    not_configured = 0

    standard = 1

    disabled = 2

    base_r = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
        return meta._meta_table['EthernetFecEnum']


class EthernetIpgEnum(Enum):
    """
    EthernetIpgEnum

    Inter packet gap

    .. data:: standard = 0

    	IEEE standard value of 12

    .. data:: non_standard = 1

    	Non-standard value of 16

    """

    standard = 0

    non_standard = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
        return meta._meta_table['EthernetIpgEnum']


class EthernetLoopbackEnum(Enum):
    """
    EthernetLoopbackEnum

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

    no_loopback = 0

    internal = 1

    line = 2

    external = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
        return meta._meta_table['EthernetLoopbackEnum']


class EthernetMediaEnum(Enum):
    """
    EthernetMediaEnum

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

    ethernet_other = 0

    ethernet_unknown = 1

    ethernet_aui = 2

    ethernet_10base5 = 3

    ethernet_foirl = 4

    ethernet_10base2 = 5

    ethernet_10broad36 = 6

    ethernet_10base = 7

    ethernet_10base_thd = 8

    ethernet_10base_tfd = 9

    ethernet_10base_fp = 10

    ethernet_10base_fb = 11

    ethernet_10base_fl = 12

    ethernet_10base_flhd = 13

    ethernet_10base_flfd = 14

    ethernet_100base_t4 = 15

    ethernet_100base_tx = 16

    ethernet_100base_txhd = 17

    ethernet_100base_txfd = 18

    ethernet_100base_fx = 19

    ethernet_100base_fxhd = 20

    ethernet_100base_fxfd = 21

    ethernet_100base_ex = 22

    ethernet_100base_exhd = 23

    ethernet_100base_exfd = 24

    ethernet_100base_t2 = 25

    ethernet_100base_t2hd = 26

    ethernet_100base_t2fd = 27

    ethernet_1000base_x = 28

    ethernet_1000base_xhd = 29

    ethernet_1000base_xfd = 30

    ethernet_1000base_lx = 31

    ethernet_1000base_lxhd = 32

    ethernet_1000base_lxfd = 33

    ethernet_1000base_sx = 34

    ethernet_1000base_sxhd = 35

    ethernet_1000base_sxfd = 36

    ethernet_1000base_cx = 37

    ethernet_1000base_cxhd = 38

    ethernet_1000base_cxfd = 39

    ethernet_1000base = 40

    ethernet_1000base_thd = 41

    ethernet_1000base_tfd = 42

    ethernet_10gbase_x = 43

    ethernet_10gbase_lx4 = 44

    ethernet_10gbase_r = 45

    ethernet_10gbase_er = 46

    ethernet_10gbase_lr = 47

    ethernet_10gbase_sr = 48

    ethernet_10gbase_w = 49

    ethernet_10gbase_ew = 50

    ethernet_10gbase_lw = 51

    ethernet_10gbase_sw = 52

    ethernet_1000base_zx = 53

    ethernet_1000base_cwdm = 54

    ethernet_1000base_cwdm_1470 = 55

    ethernet_1000base_cwdm_1490 = 56

    ethernet_1000base_cwdm_1510 = 57

    ethernet_1000base_cwdm_1530 = 58

    ethernet_1000base_cwdm_1550 = 59

    ethernet_1000base_cwdm_1570 = 60

    ethernet_1000base_cwdm_1590 = 61

    ethernet_1000base_cwdm_1610 = 62

    ethernet_10gbase_zr = 63

    ethernet_10gbase_dwdm = 64

    ethernet_100gbase_lr4 = 65

    ethernet_1000base_dwdm = 66

    ethernet_1000base_dwdm_1533 = 67

    ethernet_1000base_dwdm_1537 = 68

    ethernet_1000base_dwdm_1541 = 69

    ethernet_1000base_dwdm_1545 = 70

    ethernet_1000base_dwdm_1549 = 71

    ethernet_1000base_dwdm_1553 = 72

    ethernet_1000base_dwdm_1557 = 73

    ethernet_1000base_dwdm_1561 = 74

    ethernet_40gbase_lr4 = 75

    ethernet_40gbase_er4 = 76

    ethernet_100gbase_er4 = 77

    ethernet_1000base_ex = 78

    ethernet_1000base_bx10_d = 79

    ethernet_1000base_bx10_u = 80

    ethernet_1000base_dwdm_1561_42 = 81

    ethernet_1000base_dwdm_1560_61 = 82

    ethernet_1000base_dwdm_1559_79 = 83

    ethernet_1000base_dwdm_1558_98 = 84

    ethernet_1000base_dwdm_1558_17 = 85

    ethernet_1000base_dwdm_1557_36 = 86

    ethernet_1000base_dwdm_1556_55 = 87

    ethernet_1000base_dwdm_1555_75 = 88

    ethernet_1000base_dwdm_1554_94 = 89

    ethernet_1000base_dwdm_1554_13 = 90

    ethernet_1000base_dwdm_1553_33 = 91

    ethernet_1000base_dwdm_1552_52 = 92

    ethernet_1000base_dwdm_1551_72 = 93

    ethernet_1000base_dwdm_1550_92 = 94

    ethernet_1000base_dwdm_1550_12 = 95

    ethernet_1000base_dwdm_1549_32 = 96

    ethernet_1000base_dwdm_1548_51 = 97

    ethernet_1000base_dwdm_1547_72 = 98

    ethernet_1000base_dwdm_1546_92 = 99

    ethernet_1000base_dwdm_1546_12 = 100

    ethernet_1000base_dwdm_1545_32 = 101

    ethernet_1000base_dwdm_1544_53 = 102

    ethernet_1000base_dwdm_1543_73 = 103

    ethernet_1000base_dwdm_1542_94 = 104

    ethernet_1000base_dwdm_1542_14 = 105

    ethernet_1000base_dwdm_1541_35 = 106

    ethernet_1000base_dwdm_1540_56 = 107

    ethernet_1000base_dwdm_1539_77 = 108

    ethernet_1000base_dwdm_1538_98 = 109

    ethernet_1000base_dwdm_1538_19 = 110

    ethernet_1000base_dwdm_1537_40 = 111

    ethernet_1000base_dwdm_1536_61 = 112

    ethernet_1000base_dwdm_1535_82 = 113

    ethernet_1000base_dwdm_1535_04 = 114

    ethernet_1000base_dwdm_1534_25 = 115

    ethernet_1000base_dwdm_1533_47 = 116

    ethernet_1000base_dwdm_1532_68 = 117

    ethernet_1000base_dwdm_1531_90 = 118

    ethernet_1000base_dwdm_1531_12 = 119

    ethernet_1000base_dwdm_1530_33 = 120

    ethernet_1000base_dwdm_tunable = 121

    ethernet_10gbase_dwdm_1561_42 = 122

    ethernet_10gbase_dwdm_1560_61 = 123

    ethernet_10gbase_dwdm_1559_79 = 124

    ethernet_10gbase_dwdm_1558_98 = 125

    ethernet_10gbase_dwdm_1558_17 = 126

    ethernet_10gbase_dwdm_1557_36 = 127

    ethernet_10gbase_dwdm_1556_55 = 128

    ethernet_10gbase_dwdm_1555_75 = 129

    ethernet_10gbase_dwdm_1554_94 = 130

    ethernet_10gbase_dwdm_1554_13 = 131

    ethernet_10gbase_dwdm_1553_33 = 132

    ethernet_10gbase_dwdm_1552_52 = 133

    ethernet_10gbase_dwdm_1551_72 = 134

    ethernet_10gbase_dwdm_1550_92 = 135

    ethernet_10gbase_dwdm_1550_12 = 136

    ethernet_10gbase_dwdm_1549_32 = 137

    ethernet_10gbase_dwdm_1548_51 = 138

    ethernet_10gbase_dwdm_1547_72 = 139

    ethernet_10gbase_dwdm_1546_92 = 140

    ethernet_10gbase_dwdm_1546_12 = 141

    ethernet_10gbase_dwdm_1545_32 = 142

    ethernet_10gbase_dwdm_1544_53 = 143

    ethernet_10gbase_dwdm_1543_73 = 144

    ethernet_10gbase_dwdm_1542_94 = 145

    ethernet_10gbase_dwdm_1542_14 = 146

    ethernet_10gbase_dwdm_1541_35 = 147

    ethernet_10gbase_dwdm_1540_56 = 148

    ethernet_10gbase_dwdm_1539_77 = 149

    ethernet_10gbase_dwdm_1538_98 = 150

    ethernet_10gbase_dwdm_1538_19 = 151

    ethernet_10gbase_dwdm_1537_40 = 152

    ethernet_10gbase_dwdm_1536_61 = 153

    ethernet_10gbase_dwdm_1535_82 = 154

    ethernet_10gbase_dwdm_1535_04 = 155

    ethernet_10gbase_dwdm_1534_25 = 156

    ethernet_10gbase_dwdm_1533_47 = 157

    ethernet_10gbase_dwdm_1532_68 = 158

    ethernet_10gbase_dwdm_1531_90 = 159

    ethernet_10gbase_dwdm_1531_12 = 160

    ethernet_10gbase_dwdm_1530_33 = 161

    ethernet_10gbase_dwdm_tunable = 162

    ethernet_40gbase_dwdm_1561_42 = 163

    ethernet_40gbase_dwdm_1560_61 = 164

    ethernet_40gbase_dwdm_1559_79 = 165

    ethernet_40gbase_dwdm_1558_98 = 166

    ethernet_40gbase_dwdm_1558_17 = 167

    ethernet_40gbase_dwdm_1557_36 = 168

    ethernet_40gbase_dwdm_1556_55 = 169

    ethernet_40gbase_dwdm_1555_75 = 170

    ethernet_40gbase_dwdm_1554_94 = 171

    ethernet_40gbase_dwdm_1554_13 = 172

    ethernet_40gbase_dwdm_1553_33 = 173

    ethernet_40gbase_dwdm_1552_52 = 174

    ethernet_40gbase_dwdm_1551_72 = 175

    ethernet_40gbase_dwdm_1550_92 = 176

    ethernet_40gbase_dwdm_1550_12 = 177

    ethernet_40gbase_dwdm_1549_32 = 178

    ethernet_40gbase_dwdm_1548_51 = 179

    ethernet_40gbase_dwdm_1547_72 = 180

    ethernet_40gbase_dwdm_1546_92 = 181

    ethernet_40gbase_dwdm_1546_12 = 182

    ethernet_40gbase_dwdm_1545_32 = 183

    ethernet_40gbase_dwdm_1544_53 = 184

    ethernet_40gbase_dwdm_1543_73 = 185

    ethernet_40gbase_dwdm_1542_94 = 186

    ethernet_40gbase_dwdm_1542_14 = 187

    ethernet_40gbase_dwdm_1541_35 = 188

    ethernet_40gbase_dwdm_1540_56 = 189

    ethernet_40gbase_dwdm_1539_77 = 190

    ethernet_40gbase_dwdm_1538_98 = 191

    ethernet_40gbase_dwdm_1538_19 = 192

    ethernet_40gbase_dwdm_1537_40 = 193

    ethernet_40gbase_dwdm_1536_61 = 194

    ethernet_40gbase_dwdm_1535_82 = 195

    ethernet_40gbase_dwdm_1535_04 = 196

    ethernet_40gbase_dwdm_1534_25 = 197

    ethernet_40gbase_dwdm_1533_47 = 198

    ethernet_40gbase_dwdm_1532_68 = 199

    ethernet_40gbase_dwdm_1531_90 = 200

    ethernet_40gbase_dwdm_1531_12 = 201

    ethernet_40gbase_dwdm_1530_33 = 202

    ethernet_40gbase_dwdm_tunable = 203

    ethernet_100gbase_dwdm_1561_42 = 204

    ethernet_100gbase_dwdm_1560_61 = 205

    ethernet_100gbase_dwdm_1559_79 = 206

    ethernet_100gbase_dwdm_1558_98 = 207

    ethernet_100gbase_dwdm_1558_17 = 208

    ethernet_100gbase_dwdm_1557_36 = 209

    ethernet_100gbase_dwdm_1556_55 = 210

    ethernet_100gbase_dwdm_1555_75 = 211

    ethernet_100gbase_dwdm_1554_94 = 212

    ethernet_100gbase_dwdm_1554_13 = 213

    ethernet_100gbase_dwdm_1553_33 = 214

    ethernet_100gbase_dwdm_1552_52 = 215

    ethernet_100gbase_dwdm_1551_72 = 216

    ethernet_100gbase_dwdm_1550_92 = 217

    ethernet_100gbase_dwdm_1550_12 = 218

    ethernet_100gbase_dwdm_1549_32 = 219

    ethernet_100gbase_dwdm_1548_51 = 220

    ethernet_100gbase_dwdm_1547_72 = 221

    ethernet_100gbase_dwdm_1546_92 = 222

    ethernet_100gbase_dwdm_1546_12 = 223

    ethernet_100gbase_dwdm_1545_32 = 224

    ethernet_100gbase_dwdm_1544_53 = 225

    ethernet_100gbase_dwdm_1543_73 = 226

    ethernet_100gbase_dwdm_1542_94 = 227

    ethernet_100gbase_dwdm_1542_14 = 228

    ethernet_100gbase_dwdm_1541_35 = 229

    ethernet_100gbase_dwdm_1540_56 = 230

    ethernet_100gbase_dwdm_1539_77 = 231

    ethernet_100gbase_dwdm_1538_98 = 232

    ethernet_100gbase_dwdm_1538_19 = 233

    ethernet_100gbase_dwdm_1537_40 = 234

    ethernet_100gbase_dwdm_1536_61 = 235

    ethernet_100gbase_dwdm_1535_82 = 236

    ethernet_100gbase_dwdm_1535_04 = 237

    ethernet_100gbase_dwdm_1534_25 = 238

    ethernet_100gbase_dwdm_1533_47 = 239

    ethernet_100gbase_dwdm_1532_68 = 240

    ethernet_100gbase_dwdm_1531_90 = 241

    ethernet_100gbase_dwdm_1531_12 = 242

    ethernet_100gbase_dwdm_1530_33 = 243

    ethernet_100gbase_dwdm_tunable = 244

    ethernet_40gbase_kr4 = 245

    ethernet_40gbase_cr4 = 246

    ethernet_40gbase_sr4 = 247

    ethernet_40gbase_fr = 248

    ethernet_100gbase_cr10 = 249

    ethernet_100gbase_sr10 = 250

    ethernet_40gbase_csr4 = 251

    ethernet_10gbase_cwdm = 252

    ethernet_10gbase_cwdm_tunable = 253

    ethernet_10gbase_cwdm_1470 = 254

    ethernet_10gbase_cwdm_1490 = 255

    ethernet_10gbase_cwdm_1510 = 256

    ethernet_10gbase_cwdm_1530 = 257

    ethernet_10gbase_cwdm_1550 = 258

    ethernet_10gbase_cwdm_1570 = 259

    ethernet_10gbase_cwdm_1590 = 260

    ethernet_10gbase_cwdm_1610 = 261

    ethernet_40gbase_cwdm = 262

    ethernet_40gbase_cwdm_tunable = 263

    ethernet_40gbase_cwdm_1470 = 264

    ethernet_40gbase_cwdm_1490 = 265

    ethernet_40gbase_cwdm_1510 = 266

    ethernet_40gbase_cwdm_1530 = 267

    ethernet_40gbase_cwdm_1550 = 268

    ethernet_40gbase_cwdm_1570 = 269

    ethernet_40gbase_cwdm_1590 = 270

    ethernet_40gbase_cwdm_1610 = 271

    ethernet_100gbase_cwdm = 272

    ethernet_100gbase_cwdm_tunable = 273

    ethernet_100gbase_cwdm_1470 = 274

    ethernet_100gbase_cwdm_1490 = 275

    ethernet_100gbase_cwdm_1510 = 276

    ethernet_100gbase_cwdm_1530 = 277

    ethernet_100gbase_cwdm_1550 = 278

    ethernet_100gbase_cwdm_1570 = 279

    ethernet_100gbase_cwdm_1590 = 280

    ethernet_100gbase_cwdm_1610 = 281

    ethernet_40gbase_elpb = 282

    ethernet_100gbase_elpb = 283

    ethernet_100gbase_lr10 = 284

    ethernet_40gbase = 285

    ethernet_100gbase_kp4 = 286

    ethernet_100gbase_kr4 = 287

    ethernet_10gbase_lrm = 288

    ethernet_10gbase_cx4 = 289

    ethernet_10gbase = 290

    ethernet_10gbase_kx4 = 291

    ethernet_10gbase_kr = 292

    ethernet_10gbase_pr = 293

    ethernet_100base_lx = 294

    ethernet_100base_zx = 295

    ethernet_1000base_bx_d = 296

    ethernet_1000base_bx_u = 297

    ethernet_1000base_bx20_d = 298

    ethernet_1000base_bx20_u = 299

    ethernet_1000base_bx40_d = 300

    ethernet_1000base_bx40_da = 301

    ethernet_1000base_bx40_u = 302

    ethernet_1000base_bx80_d = 303

    ethernet_1000base_bx80_u = 304

    ethernet_1000base_bx120_d = 305

    ethernet_1000base_bx120_u = 306

    ethernet_10gbase_bx_d = 307

    ethernet_10gbase_bx_u = 308

    ethernet_10gbase_bx10_d = 309

    ethernet_10gbase_bx10_u = 310

    ethernet_10gbase_bx20_d = 311

    ethernet_10gbase_bx20_u = 312

    ethernet_10gbase_bx40_d = 313

    ethernet_10gbase_bx40_u = 314

    ethernet_10gbase_bx80_d = 315

    ethernet_10gbase_bx80_u = 316

    ethernet_10gbase_bx120_d = 317

    ethernet_10gbase_bx120_u = 318

    ethernet_1000base_dr_lx = 319

    ethernet_100gbase_er4l = 320

    ethernet_100gbase_sr4 = 321

    ethernet_40gbase_sr_bd = 322

    ethernet_25gbase_cr = 323

    ethernet_25gbase_cr_s = 324

    ethernet_25gbase_kr = 325

    ethernet_25gbase_kr_s = 326

    ethernet_25gbase_r = 327

    ethernet_25gbase_sr = 328

    ethernet_25gbase_dwdm = 329

    ethernet_25gbase_dwdm_tunable = 330

    ethernet_25gbase_cwdm = 331

    ethernet_25gbase_cwdm_tunable = 332

    ethernet_100gbase_psm4 = 333

    ethernet_100gbase_er10 = 334

    ethernet_100gbase_er10l = 335

    ethernet_100gbase_acc = 336

    ethernet_100gbase_aoc = 337

    ethernet_100gbase_cwdm4 = 338

    ethernet_40gbase_psm4 = 339

    ethernet_100gbase_cr4 = 340

    ethernet_100gbase_act_loop = 341

    ethernet_100gbase_pas_loop = 342

    ethernet_base_max = 343


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
        return meta._meta_table['EthernetMediaEnum']


class EthernetPortEnableEnum(Enum):
    """
    EthernetPortEnableEnum

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

    disabled = 0

    rx_enabled = 1

    tx_enabled = 2

    enabled = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
        return meta._meta_table['EthernetPortEnableEnum']


class EthernetSpeedEnum(Enum):
    """
    EthernetSpeedEnum

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

    ethernet_speed_invalid = 0

    ten_mbps = 1

    hundred_mbps = 2

    one_gbps = 3

    ten_gbps = 4

    twenty_five_gbps = 5

    forty_gbps = 6

    fifty_gbps = 7

    hundred_gbps = 8

    ethernet_speed_types_count = 9


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
        return meta._meta_table['EthernetSpeedEnum']



class EthernetInterface(object):
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
    _revision = '2015-10-14'

    def __init__(self):
        self.berts = EthernetInterface.Berts()
        self.berts.parent = self
        self.interfaces = EthernetInterface.Interfaces()
        self.interfaces.parent = self
        self.statistics = EthernetInterface.Statistics()
        self.statistics.parent = self


    class Statistics(object):
        """
        Ethernet controller statistics table
        
        .. attribute:: statistic
        
        	Ethernet statistics information
        	**type**\: list of    :py:class:`Statistic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Statistics.Statistic>`
        
        

        """

        _prefix = 'drivers-media-eth-oper'
        _revision = '2015-10-14'

        def __init__(self):
            self.parent = None
            self.statistic = YList()
            self.statistic.parent = self
            self.statistic.name = 'statistic'


        class Statistic(object):
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
            _revision = '2015-10-14'

            def __init__(self):
                self.parent = None
                self.interface_name = None
                self.aborted_packet_drops = None
                self.buffer_underrun_packet_drops = None
                self.dropped_ether_stats_fragments = None
                self.dropped_ether_stats_undersize_pkts = None
                self.dropped_giant_packets_greaterthan_mru = None
                self.dropped_jabbers_packets_greaterthan_mru = None
                self.dropped_miscellaneous_error_packets = None
                self.dropped_packets_with_crc_align_errors = None
                self.ether_stats_collisions = None
                self.invalid_dest_mac_drop_packets = None
                self.invalid_encap_drop_packets = None
                self.miscellaneous_output_errors = None
                self.number_of_aborted_packets_dropped = None
                self.number_of_buffer_overrun_packets_dropped = None
                self.number_of_miscellaneous_packets_dropped = None
                self.numberof_invalid_vlan_id_packets_dropped = None
                self.received8021q_frames = None
                self.received_broadcast_frames = None
                self.received_good_bytes = None
                self.received_good_frames = None
                self.received_multicast_frames = None
                self.received_pause_frames = None
                self.received_total64_octet_frames = None
                self.received_total_bytes = None
                self.received_total_frames = None
                self.received_total_octet_frames_from1024_to1518 = None
                self.received_total_octet_frames_from128_to255 = None
                self.received_total_octet_frames_from1519_to_max = None
                self.received_total_octet_frames_from256_to511 = None
                self.received_total_octet_frames_from512_to1023 = None
                self.received_total_octet_frames_from65_to127 = None
                self.received_unicast_frames = None
                self.received_unknown_opcodes = None
                self.rfc2819_ether_stats_crc_align_errors = None
                self.rfc2819_ether_stats_jabbers = None
                self.rfc2819_ether_stats_oversized_pkts = None
                self.rfc3635dot3_stats_alignment_errors = None
                self.symbol_errors = None
                self.total_bytes_transmitted = None
                self.total_frames_transmitted = None
                self.total_good_bytes_transmitted = None
                self.transmitted8021q_frames = None
                self.transmitted_broadcast_frames = None
                self.transmitted_good_frames = None
                self.transmitted_multicast_frames = None
                self.transmitted_total64_octet_frames = None
                self.transmitted_total_octet_frames_from1024_to1518 = None
                self.transmitted_total_octet_frames_from128_to255 = None
                self.transmitted_total_octet_frames_from1518_to_max = None
                self.transmitted_total_octet_frames_from256_to511 = None
                self.transmitted_total_octet_frames_from512_to1023 = None
                self.transmitted_total_octet_frames_from65_to127 = None
                self.transmitted_total_pause_frames = None
                self.transmitted_unicast_frames = None
                self.uncounted_dropped_frames = None

            @property
            def _common_path(self):
                if self.interface_name is None:
                    raise YPYModelError('Key property interface_name is None')

                return '/Cisco-IOS-XR-drivers-media-eth-oper:ethernet-interface/Cisco-IOS-XR-drivers-media-eth-oper:statistics/Cisco-IOS-XR-drivers-media-eth-oper:statistic[Cisco-IOS-XR-drivers-media-eth-oper:interface-name = ' + str(self.interface_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.interface_name is not None:
                    return True

                if self.aborted_packet_drops is not None:
                    return True

                if self.buffer_underrun_packet_drops is not None:
                    return True

                if self.dropped_ether_stats_fragments is not None:
                    return True

                if self.dropped_ether_stats_undersize_pkts is not None:
                    return True

                if self.dropped_giant_packets_greaterthan_mru is not None:
                    return True

                if self.dropped_jabbers_packets_greaterthan_mru is not None:
                    return True

                if self.dropped_miscellaneous_error_packets is not None:
                    return True

                if self.dropped_packets_with_crc_align_errors is not None:
                    return True

                if self.ether_stats_collisions is not None:
                    return True

                if self.invalid_dest_mac_drop_packets is not None:
                    return True

                if self.invalid_encap_drop_packets is not None:
                    return True

                if self.miscellaneous_output_errors is not None:
                    return True

                if self.number_of_aborted_packets_dropped is not None:
                    return True

                if self.number_of_buffer_overrun_packets_dropped is not None:
                    return True

                if self.number_of_miscellaneous_packets_dropped is not None:
                    return True

                if self.numberof_invalid_vlan_id_packets_dropped is not None:
                    return True

                if self.received8021q_frames is not None:
                    return True

                if self.received_broadcast_frames is not None:
                    return True

                if self.received_good_bytes is not None:
                    return True

                if self.received_good_frames is not None:
                    return True

                if self.received_multicast_frames is not None:
                    return True

                if self.received_pause_frames is not None:
                    return True

                if self.received_total64_octet_frames is not None:
                    return True

                if self.received_total_bytes is not None:
                    return True

                if self.received_total_frames is not None:
                    return True

                if self.received_total_octet_frames_from1024_to1518 is not None:
                    return True

                if self.received_total_octet_frames_from128_to255 is not None:
                    return True

                if self.received_total_octet_frames_from1519_to_max is not None:
                    return True

                if self.received_total_octet_frames_from256_to511 is not None:
                    return True

                if self.received_total_octet_frames_from512_to1023 is not None:
                    return True

                if self.received_total_octet_frames_from65_to127 is not None:
                    return True

                if self.received_unicast_frames is not None:
                    return True

                if self.received_unknown_opcodes is not None:
                    return True

                if self.rfc2819_ether_stats_crc_align_errors is not None:
                    return True

                if self.rfc2819_ether_stats_jabbers is not None:
                    return True

                if self.rfc2819_ether_stats_oversized_pkts is not None:
                    return True

                if self.rfc3635dot3_stats_alignment_errors is not None:
                    return True

                if self.symbol_errors is not None:
                    return True

                if self.total_bytes_transmitted is not None:
                    return True

                if self.total_frames_transmitted is not None:
                    return True

                if self.total_good_bytes_transmitted is not None:
                    return True

                if self.transmitted8021q_frames is not None:
                    return True

                if self.transmitted_broadcast_frames is not None:
                    return True

                if self.transmitted_good_frames is not None:
                    return True

                if self.transmitted_multicast_frames is not None:
                    return True

                if self.transmitted_total64_octet_frames is not None:
                    return True

                if self.transmitted_total_octet_frames_from1024_to1518 is not None:
                    return True

                if self.transmitted_total_octet_frames_from128_to255 is not None:
                    return True

                if self.transmitted_total_octet_frames_from1518_to_max is not None:
                    return True

                if self.transmitted_total_octet_frames_from256_to511 is not None:
                    return True

                if self.transmitted_total_octet_frames_from512_to1023 is not None:
                    return True

                if self.transmitted_total_octet_frames_from65_to127 is not None:
                    return True

                if self.transmitted_total_pause_frames is not None:
                    return True

                if self.transmitted_unicast_frames is not None:
                    return True

                if self.uncounted_dropped_frames is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
                return meta._meta_table['EthernetInterface.Statistics.Statistic']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-drivers-media-eth-oper:ethernet-interface/Cisco-IOS-XR-drivers-media-eth-oper:statistics'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.statistic is not None:
                for child_ref in self.statistic:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
            return meta._meta_table['EthernetInterface.Statistics']['meta_info']


    class Interfaces(object):
        """
        Ethernet controller info table
        
        .. attribute:: interface
        
        	Ethernet controller information
        	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Interfaces.Interface>`
        
        

        """

        _prefix = 'drivers-media-eth-oper'
        _revision = '2015-10-14'

        def __init__(self):
            self.parent = None
            self.interface = YList()
            self.interface.parent = self
            self.interface.name = 'interface'


        class Interface(object):
            """
            Ethernet controller information
            
            .. attribute:: interface_name  <key>
            
            	The name of the interface
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: admin_state
            
            	Port Administrative State
            	**type**\:   :py:class:`EthernetPortEnableEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetPortEnableEnum>`
            
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
            _revision = '2015-10-14'

            def __init__(self):
                self.parent = None
                self.interface_name = None
                self.admin_state = None
                self.layer1_info = EthernetInterface.Interfaces.Interface.Layer1Info()
                self.layer1_info.parent = self
                self.mac_info = EthernetInterface.Interfaces.Interface.MacInfo()
                self.mac_info.parent = self
                self.oper_state_up = None
                self.phy_info = EthernetInterface.Interfaces.Interface.PhyInfo()
                self.phy_info.parent = self
                self.transport_info = EthernetInterface.Interfaces.Interface.TransportInfo()
                self.transport_info.parent = self


            class PhyInfo(object):
                """
                PHY information
                
                .. attribute:: fec_details
                
                	Forward Error Correction information
                	**type**\:   :py:class:`FecDetails <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Interfaces.Interface.PhyInfo.FecDetails>`
                
                .. attribute:: loopback
                
                	Port operational loopback
                	**type**\:   :py:class:`EthernetLoopbackEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetLoopbackEnum>`
                
                .. attribute:: media_type
                
                	Port media type
                	**type**\:   :py:class:`EthernetMediaEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetMediaEnum>`
                
                .. attribute:: phy_details
                
                	Details about the PHY
                	**type**\:   :py:class:`PhyDetails <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails>`
                
                .. attribute:: phy_present
                
                	Presence of PHY
                	**type**\:   :py:class:`EtherPhyPresentEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EtherPhyPresentEnum>`
                
                

                """

                _prefix = 'drivers-media-eth-oper'
                _revision = '2015-10-14'

                def __init__(self):
                    self.parent = None
                    self.fec_details = EthernetInterface.Interfaces.Interface.PhyInfo.FecDetails()
                    self.fec_details.parent = self
                    self.loopback = None
                    self.media_type = None
                    self.phy_details = EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails()
                    self.phy_details.parent = self
                    self.phy_present = None


                class PhyDetails(object):
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
                    
                    .. attribute:: optics_wavelength
                    
                    	Wavelength of the optics being used in nm \* 1000
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
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
                    _revision = '2015-10-14'

                    def __init__(self):
                        self.parent = None
                        self.dig_opt_mon_alarm_thresholds = EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails.DigOptMonAlarmThresholds()
                        self.dig_opt_mon_alarm_thresholds.parent = self
                        self.dig_opt_mon_alarms = EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails.DigOptMonAlarms()
                        self.dig_opt_mon_alarms.parent = self
                        self.lane = YList()
                        self.lane.parent = self
                        self.lane.name = 'lane'
                        self.lane_field_validity = EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails.LaneFieldValidity()
                        self.lane_field_validity.parent = self
                        self.optics_wavelength = None
                        self.transceiver_rx_power = None
                        self.transceiver_temperature = None
                        self.transceiver_tx_bias = None
                        self.transceiver_tx_power = None
                        self.transceiver_voltage = None
                        self.vendor = None
                        self.vendor_part_number = None
                        self.vendor_serial_number = None


                    class LaneFieldValidity(object):
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
                        _revision = '2015-10-14'

                        def __init__(self):
                            self.parent = None
                            self.laser_bias_valid = None
                            self.receive_power_valid = None
                            self.transmit_power_valid = None
                            self.wavelength_valid = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-drivers-media-eth-oper:lane-field-validity'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.laser_bias_valid is not None:
                                return True

                            if self.receive_power_valid is not None:
                                return True

                            if self.transmit_power_valid is not None:
                                return True

                            if self.wavelength_valid is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
                            return meta._meta_table['EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails.LaneFieldValidity']['meta_info']


                    class DigOptMonAlarmThresholds(object):
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
                        _revision = '2015-10-14'

                        def __init__(self):
                            self.parent = None
                            self.field_validity = EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails.DigOptMonAlarmThresholds.FieldValidity()
                            self.field_validity.parent = self
                            self.laser_bias_alarm_high = None
                            self.laser_bias_alarm_low = None
                            self.laser_bias_warning_high = None
                            self.laser_bias_warning_low = None
                            self.optical_receive_power_alarm_high = None
                            self.optical_receive_power_alarm_low = None
                            self.optical_receive_power_warning_high = None
                            self.optical_receive_power_warning_low = None
                            self.optical_transmit_power_alarm_high = None
                            self.optical_transmit_power_alarm_low = None
                            self.optical_transmit_power_warning_high = None
                            self.optical_transmit_power_warning_low = None
                            self.transceiver_temperature_alarm_high = None
                            self.transceiver_temperature_alarm_low = None
                            self.transceiver_temperature_warning_high = None
                            self.transceiver_temperature_warning_low = None
                            self.transceiver_voltage_alarm_high = None
                            self.transceiver_voltage_alarm_low = None
                            self.transceiver_voltage_warning_high = None
                            self.transceiver_voltage_warning_low = None


                        class FieldValidity(object):
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
                            _revision = '2015-10-14'

                            def __init__(self):
                                self.parent = None
                                self.laser_bias_valid = None
                                self.receive_power_valid = None
                                self.temperature_valid = None
                                self.transmit_power_valid = None
                                self.voltage_valid = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-drivers-media-eth-oper:field-validity'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.laser_bias_valid is not None:
                                    return True

                                if self.receive_power_valid is not None:
                                    return True

                                if self.temperature_valid is not None:
                                    return True

                                if self.transmit_power_valid is not None:
                                    return True

                                if self.voltage_valid is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
                                return meta._meta_table['EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails.DigOptMonAlarmThresholds.FieldValidity']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-drivers-media-eth-oper:dig-opt-mon-alarm-thresholds'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.field_validity is not None and self.field_validity._has_data():
                                return True

                            if self.laser_bias_alarm_high is not None:
                                return True

                            if self.laser_bias_alarm_low is not None:
                                return True

                            if self.laser_bias_warning_high is not None:
                                return True

                            if self.laser_bias_warning_low is not None:
                                return True

                            if self.optical_receive_power_alarm_high is not None:
                                return True

                            if self.optical_receive_power_alarm_low is not None:
                                return True

                            if self.optical_receive_power_warning_high is not None:
                                return True

                            if self.optical_receive_power_warning_low is not None:
                                return True

                            if self.optical_transmit_power_alarm_high is not None:
                                return True

                            if self.optical_transmit_power_alarm_low is not None:
                                return True

                            if self.optical_transmit_power_warning_high is not None:
                                return True

                            if self.optical_transmit_power_warning_low is not None:
                                return True

                            if self.transceiver_temperature_alarm_high is not None:
                                return True

                            if self.transceiver_temperature_alarm_low is not None:
                                return True

                            if self.transceiver_temperature_warning_high is not None:
                                return True

                            if self.transceiver_temperature_warning_low is not None:
                                return True

                            if self.transceiver_voltage_alarm_high is not None:
                                return True

                            if self.transceiver_voltage_alarm_low is not None:
                                return True

                            if self.transceiver_voltage_warning_high is not None:
                                return True

                            if self.transceiver_voltage_warning_low is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
                            return meta._meta_table['EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails.DigOptMonAlarmThresholds']['meta_info']


                    class DigOptMonAlarms(object):
                        """
                        Digital Optical Monitoring alarms
                        
                        .. attribute:: laser_bias_current
                        
                        	Laser Bias Current Alarm
                        	**type**\:   :py:class:`EtherDomAlarmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EtherDomAlarmEnum>`
                        
                        .. attribute:: received_laser_power
                        
                        	Received Optical Power Alarm
                        	**type**\:   :py:class:`EtherDomAlarmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EtherDomAlarmEnum>`
                        
                        .. attribute:: transceiver_temperature
                        
                        	Transceiver Temperature Alarm
                        	**type**\:   :py:class:`EtherDomAlarmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EtherDomAlarmEnum>`
                        
                        .. attribute:: transceiver_voltage
                        
                        	Transceiver Voltage Alarm
                        	**type**\:   :py:class:`EtherDomAlarmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EtherDomAlarmEnum>`
                        
                        .. attribute:: transmit_laser_power
                        
                        	Transmit Laser Power Alarm
                        	**type**\:   :py:class:`EtherDomAlarmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EtherDomAlarmEnum>`
                        
                        

                        """

                        _prefix = 'drivers-media-eth-oper'
                        _revision = '2015-10-14'

                        def __init__(self):
                            self.parent = None
                            self.laser_bias_current = None
                            self.received_laser_power = None
                            self.transceiver_temperature = None
                            self.transceiver_voltage = None
                            self.transmit_laser_power = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-drivers-media-eth-oper:dig-opt-mon-alarms'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.laser_bias_current is not None:
                                return True

                            if self.received_laser_power is not None:
                                return True

                            if self.transceiver_temperature is not None:
                                return True

                            if self.transceiver_voltage is not None:
                                return True

                            if self.transmit_laser_power is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
                            return meta._meta_table['EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails.DigOptMonAlarms']['meta_info']


                    class Lane(object):
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
                        _revision = '2015-10-14'

                        def __init__(self):
                            self.parent = None
                            self.center_wavelength = None
                            self.dig_opt_mon_alarm = EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails.Lane.DigOptMonAlarm()
                            self.dig_opt_mon_alarm.parent = self
                            self.lane_id = None
                            self.laser_bias_current = None
                            self.received_laser_power = None
                            self.transmit_laser_power = None


                        class DigOptMonAlarm(object):
                            """
                            Digital Optical Monitoring alarms
                            
                            .. attribute:: laser_bias_current
                            
                            	Laser Bias Current Alarm
                            	**type**\:   :py:class:`EtherDomAlarmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EtherDomAlarmEnum>`
                            
                            .. attribute:: received_laser_power
                            
                            	Received Optical Power Alarm
                            	**type**\:   :py:class:`EtherDomAlarmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EtherDomAlarmEnum>`
                            
                            .. attribute:: transmit_laser_power
                            
                            	Transmit Laser Power Alarm
                            	**type**\:   :py:class:`EtherDomAlarmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EtherDomAlarmEnum>`
                            
                            

                            """

                            _prefix = 'drivers-media-eth-oper'
                            _revision = '2015-10-14'

                            def __init__(self):
                                self.parent = None
                                self.laser_bias_current = None
                                self.received_laser_power = None
                                self.transmit_laser_power = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-drivers-media-eth-oper:dig-opt-mon-alarm'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.laser_bias_current is not None:
                                    return True

                                if self.received_laser_power is not None:
                                    return True

                                if self.transmit_laser_power is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
                                return meta._meta_table['EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails.Lane.DigOptMonAlarm']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-drivers-media-eth-oper:lane'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.center_wavelength is not None:
                                return True

                            if self.dig_opt_mon_alarm is not None and self.dig_opt_mon_alarm._has_data():
                                return True

                            if self.lane_id is not None:
                                return True

                            if self.laser_bias_current is not None:
                                return True

                            if self.received_laser_power is not None:
                                return True

                            if self.transmit_laser_power is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
                            return meta._meta_table['EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails.Lane']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-drivers-media-eth-oper:phy-details'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.dig_opt_mon_alarm_thresholds is not None and self.dig_opt_mon_alarm_thresholds._has_data():
                            return True

                        if self.dig_opt_mon_alarms is not None and self.dig_opt_mon_alarms._has_data():
                            return True

                        if self.lane is not None:
                            for child_ref in self.lane:
                                if child_ref._has_data():
                                    return True

                        if self.lane_field_validity is not None and self.lane_field_validity._has_data():
                            return True

                        if self.optics_wavelength is not None:
                            return True

                        if self.transceiver_rx_power is not None:
                            return True

                        if self.transceiver_temperature is not None:
                            return True

                        if self.transceiver_tx_bias is not None:
                            return True

                        if self.transceiver_tx_power is not None:
                            return True

                        if self.transceiver_voltage is not None:
                            return True

                        if self.vendor is not None:
                            return True

                        if self.vendor_part_number is not None:
                            return True

                        if self.vendor_serial_number is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
                        return meta._meta_table['EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails']['meta_info']


                class FecDetails(object):
                    """
                    Forward Error Correction information
                    
                    .. attribute:: corrected_codeword_count
                    
                    	Corrected codeword error count
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: fec
                    
                    	Port operational FEC type
                    	**type**\:   :py:class:`EthernetFecEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetFecEnum>`
                    
                    .. attribute:: uncorrected_codeword_count
                    
                    	Uncorrected codeword error count
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    

                    """

                    _prefix = 'drivers-media-eth-oper'
                    _revision = '2015-10-14'

                    def __init__(self):
                        self.parent = None
                        self.corrected_codeword_count = None
                        self.fec = None
                        self.uncorrected_codeword_count = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-drivers-media-eth-oper:fec-details'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.corrected_codeword_count is not None:
                            return True

                        if self.fec is not None:
                            return True

                        if self.uncorrected_codeword_count is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
                        return meta._meta_table['EthernetInterface.Interfaces.Interface.PhyInfo.FecDetails']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-drivers-media-eth-oper:phy-info'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.fec_details is not None and self.fec_details._has_data():
                        return True

                    if self.loopback is not None:
                        return True

                    if self.media_type is not None:
                        return True

                    if self.phy_details is not None and self.phy_details._has_data():
                        return True

                    if self.phy_present is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
                    return meta._meta_table['EthernetInterface.Interfaces.Interface.PhyInfo']['meta_info']


            class Layer1Info(object):
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
                	**type**\:   :py:class:`EthernetDuplexEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetDuplexEnum>`
                
                .. attribute:: error_counts
                
                	Statistics for detected errors
                	**type**\:   :py:class:`ErrorCounts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Interfaces.Interface.Layer1Info.ErrorCounts>`
                
                .. attribute:: flowcontrol
                
                	Port operational flow control
                	**type**\:   :py:class:`EtherFlowcontrolEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EtherFlowcontrolEnum>`
                
                .. attribute:: ipg
                
                	Port operational inter\-packet\-gap
                	**type**\:   :py:class:`EthernetIpgEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetIpgEnum>`
                
                .. attribute:: laser_squelch_enabled
                
                	Laser Squelch \- TRUE if enabled
                	**type**\:  bool
                
                .. attribute:: led_state
                
                	State of the LED
                	**type**\:   :py:class:`EtherLedStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EtherLedStateEnum>`
                
                .. attribute:: link_state
                
                	Link state
                	**type**\:   :py:class:`EtherLinkStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EtherLinkStateEnum>`
                
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
                	**type**\:   :py:class:`EthernetSpeedEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetSpeedEnum>`
                
                

                """

                _prefix = 'drivers-media-eth-oper'
                _revision = '2015-10-14'

                def __init__(self):
                    self.parent = None
                    self.autoneg = EthernetInterface.Interfaces.Interface.Layer1Info.Autoneg()
                    self.autoneg.parent = self
                    self.bandwidth = None
                    self.bandwidth_utilization = None
                    self.ber_monitoring = EthernetInterface.Interfaces.Interface.Layer1Info.BerMonitoring()
                    self.ber_monitoring.parent = self
                    self.current_alarms = EthernetInterface.Interfaces.Interface.Layer1Info.CurrentAlarms()
                    self.current_alarms.parent = self
                    self.duplex = None
                    self.error_counts = EthernetInterface.Interfaces.Interface.Layer1Info.ErrorCounts()
                    self.error_counts.parent = self
                    self.flowcontrol = None
                    self.ipg = None
                    self.laser_squelch_enabled = None
                    self.led_state = None
                    self.link_state = None
                    self.opd_monitoring = EthernetInterface.Interfaces.Interface.Layer1Info.OpdMonitoring()
                    self.opd_monitoring.parent = self
                    self.pfc_info = EthernetInterface.Interfaces.Interface.Layer1Info.PfcInfo()
                    self.pfc_info.parent = self
                    self.previous_alarms = EthernetInterface.Interfaces.Interface.Layer1Info.PreviousAlarms()
                    self.previous_alarms.parent = self
                    self.speed = None


                class Autoneg(object):
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
                    	**type**\:   :py:class:`EthernetDuplexEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetDuplexEnum>`
                    
                    .. attribute:: fec
                    
                    	Restricted FEC (if revelevant bit is set in mask)
                    	**type**\:   :py:class:`EthernetFecEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetFecEnum>`
                    
                    .. attribute:: flowcontrol
                    
                    	Restricted flowcontrol (if relevant bit is set in mask)
                    	**type**\:   :py:class:`EtherFlowcontrolEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EtherFlowcontrolEnum>`
                    
                    .. attribute:: mask
                    
                    	Validity mask\: 0x1 speed, 0x2 duplex, 0x4 flowcontrol, 0x8 fec
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: speed
                    
                    	Restricted speed (if relevant bit is set in mask)
                    	**type**\:   :py:class:`EthernetSpeedEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetSpeedEnum>`
                    
                    

                    """

                    _prefix = 'drivers-media-eth-oper'
                    _revision = '2015-10-14'

                    def __init__(self):
                        self.parent = None
                        self.autoneg_enabled = None
                        self.config_override = None
                        self.duplex = None
                        self.fec = None
                        self.flowcontrol = None
                        self.mask = None
                        self.speed = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-drivers-media-eth-oper:autoneg'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.autoneg_enabled is not None:
                            return True

                        if self.config_override is not None:
                            return True

                        if self.duplex is not None:
                            return True

                        if self.fec is not None:
                            return True

                        if self.flowcontrol is not None:
                            return True

                        if self.mask is not None:
                            return True

                        if self.speed is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
                        return meta._meta_table['EthernetInterface.Interfaces.Interface.Layer1Info.Autoneg']['meta_info']


                class CurrentAlarms(object):
                    """
                    Current alarms
                    
                    .. attribute:: hi_ber_alarm
                    
                    	Hi BER
                    	**type**\:   :py:class:`EthCtrlrAlarmStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthCtrlrAlarmStateEnum>`
                    
                    .. attribute:: local_fault_alarm
                    
                    	Local Fault
                    	**type**\:   :py:class:`EthCtrlrAlarmStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthCtrlrAlarmStateEnum>`
                    
                    .. attribute:: loss_of_synchronization_data_alarm
                    
                    	Loss of Synchronization Data
                    	**type**\:   :py:class:`EthCtrlrAlarmStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthCtrlrAlarmStateEnum>`
                    
                    .. attribute:: pcs_loss_of_block_lock_alarm
                    
                    	PCS Loss of Block Lock
                    	**type**\:   :py:class:`EthCtrlrAlarmStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthCtrlrAlarmStateEnum>`
                    
                    .. attribute:: received_loss_of_signal_alarm
                    
                    	Received Loss of Signal
                    	**type**\:   :py:class:`EthCtrlrAlarmStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthCtrlrAlarmStateEnum>`
                    
                    .. attribute:: remote_fault_alarm
                    
                    	Remote Fault
                    	**type**\:   :py:class:`EthCtrlrAlarmStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthCtrlrAlarmStateEnum>`
                    
                    .. attribute:: rx_opd_alarm
                    
                    	Rx OPD Alarm
                    	**type**\:   :py:class:`EthCtrlrAlarmStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthCtrlrAlarmStateEnum>`
                    
                    .. attribute:: sd_ber_alarm
                    
                    	SD BER
                    	**type**\:   :py:class:`EthCtrlrAlarmStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthCtrlrAlarmStateEnum>`
                    
                    .. attribute:: sf_ber_alarm
                    
                    	SF BER
                    	**type**\:   :py:class:`EthCtrlrAlarmStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthCtrlrAlarmStateEnum>`
                    
                    .. attribute:: squelch_alarm
                    
                    	Squelch
                    	**type**\:   :py:class:`EthCtrlrAlarmStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthCtrlrAlarmStateEnum>`
                    
                    

                    """

                    _prefix = 'drivers-media-eth-oper'
                    _revision = '2015-10-14'

                    def __init__(self):
                        self.parent = None
                        self.hi_ber_alarm = None
                        self.local_fault_alarm = None
                        self.loss_of_synchronization_data_alarm = None
                        self.pcs_loss_of_block_lock_alarm = None
                        self.received_loss_of_signal_alarm = None
                        self.remote_fault_alarm = None
                        self.rx_opd_alarm = None
                        self.sd_ber_alarm = None
                        self.sf_ber_alarm = None
                        self.squelch_alarm = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-drivers-media-eth-oper:current-alarms'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.hi_ber_alarm is not None:
                            return True

                        if self.local_fault_alarm is not None:
                            return True

                        if self.loss_of_synchronization_data_alarm is not None:
                            return True

                        if self.pcs_loss_of_block_lock_alarm is not None:
                            return True

                        if self.received_loss_of_signal_alarm is not None:
                            return True

                        if self.remote_fault_alarm is not None:
                            return True

                        if self.rx_opd_alarm is not None:
                            return True

                        if self.sd_ber_alarm is not None:
                            return True

                        if self.sf_ber_alarm is not None:
                            return True

                        if self.squelch_alarm is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
                        return meta._meta_table['EthernetInterface.Interfaces.Interface.Layer1Info.CurrentAlarms']['meta_info']


                class PreviousAlarms(object):
                    """
                    Previous alarms
                    
                    .. attribute:: hi_ber_alarm
                    
                    	Hi BER
                    	**type**\:   :py:class:`EthCtrlrAlarmStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthCtrlrAlarmStateEnum>`
                    
                    .. attribute:: local_fault_alarm
                    
                    	Local Fault
                    	**type**\:   :py:class:`EthCtrlrAlarmStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthCtrlrAlarmStateEnum>`
                    
                    .. attribute:: loss_of_synchronization_data_alarm
                    
                    	Loss of Synchronization Data
                    	**type**\:   :py:class:`EthCtrlrAlarmStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthCtrlrAlarmStateEnum>`
                    
                    .. attribute:: pcs_loss_of_block_lock_alarm
                    
                    	PCS Loss of Block Lock
                    	**type**\:   :py:class:`EthCtrlrAlarmStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthCtrlrAlarmStateEnum>`
                    
                    .. attribute:: received_loss_of_signal_alarm
                    
                    	Received Loss of Signal
                    	**type**\:   :py:class:`EthCtrlrAlarmStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthCtrlrAlarmStateEnum>`
                    
                    .. attribute:: remote_fault_alarm
                    
                    	Remote Fault
                    	**type**\:   :py:class:`EthCtrlrAlarmStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthCtrlrAlarmStateEnum>`
                    
                    .. attribute:: rx_opd_alarm
                    
                    	Rx OPD Alarm
                    	**type**\:   :py:class:`EthCtrlrAlarmStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthCtrlrAlarmStateEnum>`
                    
                    .. attribute:: sd_ber_alarm
                    
                    	SD BER
                    	**type**\:   :py:class:`EthCtrlrAlarmStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthCtrlrAlarmStateEnum>`
                    
                    .. attribute:: sf_ber_alarm
                    
                    	SF BER
                    	**type**\:   :py:class:`EthCtrlrAlarmStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthCtrlrAlarmStateEnum>`
                    
                    .. attribute:: squelch_alarm
                    
                    	Squelch
                    	**type**\:   :py:class:`EthCtrlrAlarmStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthCtrlrAlarmStateEnum>`
                    
                    

                    """

                    _prefix = 'drivers-media-eth-oper'
                    _revision = '2015-10-14'

                    def __init__(self):
                        self.parent = None
                        self.hi_ber_alarm = None
                        self.local_fault_alarm = None
                        self.loss_of_synchronization_data_alarm = None
                        self.pcs_loss_of_block_lock_alarm = None
                        self.received_loss_of_signal_alarm = None
                        self.remote_fault_alarm = None
                        self.rx_opd_alarm = None
                        self.sd_ber_alarm = None
                        self.sf_ber_alarm = None
                        self.squelch_alarm = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-drivers-media-eth-oper:previous-alarms'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.hi_ber_alarm is not None:
                            return True

                        if self.local_fault_alarm is not None:
                            return True

                        if self.loss_of_synchronization_data_alarm is not None:
                            return True

                        if self.pcs_loss_of_block_lock_alarm is not None:
                            return True

                        if self.received_loss_of_signal_alarm is not None:
                            return True

                        if self.remote_fault_alarm is not None:
                            return True

                        if self.rx_opd_alarm is not None:
                            return True

                        if self.sd_ber_alarm is not None:
                            return True

                        if self.sf_ber_alarm is not None:
                            return True

                        if self.squelch_alarm is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
                        return meta._meta_table['EthernetInterface.Interfaces.Interface.Layer1Info.PreviousAlarms']['meta_info']


                class ErrorCounts(object):
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
                    _revision = '2015-10-14'

                    def __init__(self):
                        self.parent = None
                        self.pcsbip_errors = None
                        self.sync_header_errors = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-drivers-media-eth-oper:error-counts'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.pcsbip_errors is not None:
                            return True

                        if self.sync_header_errors is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
                        return meta._meta_table['EthernetInterface.Interfaces.Interface.Layer1Info.ErrorCounts']['meta_info']


                class BerMonitoring(object):
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
                    _revision = '2015-10-14'

                    def __init__(self):
                        self.parent = None
                        self.settings = EthernetInterface.Interfaces.Interface.Layer1Info.BerMonitoring.Settings()
                        self.settings.parent = self
                        self.supported = None


                    class Settings(object):
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
                        _revision = '2015-10-14'

                        def __init__(self):
                            self.parent = None
                            self.signal_degrade_alarm = None
                            self.signal_degrade_threshold = None
                            self.signal_fail_alarm = None
                            self.signal_fail_threshold = None
                            self.signal_remote_fault = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-drivers-media-eth-oper:settings'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.signal_degrade_alarm is not None:
                                return True

                            if self.signal_degrade_threshold is not None:
                                return True

                            if self.signal_fail_alarm is not None:
                                return True

                            if self.signal_fail_threshold is not None:
                                return True

                            if self.signal_remote_fault is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
                            return meta._meta_table['EthernetInterface.Interfaces.Interface.Layer1Info.BerMonitoring.Settings']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-drivers-media-eth-oper:ber-monitoring'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.settings is not None and self.settings._has_data():
                            return True

                        if self.supported is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
                        return meta._meta_table['EthernetInterface.Interfaces.Interface.Layer1Info.BerMonitoring']['meta_info']


                class OpdMonitoring(object):
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
                    _revision = '2015-10-14'

                    def __init__(self):
                        self.parent = None
                        self.settings = EthernetInterface.Interfaces.Interface.Layer1Info.OpdMonitoring.Settings()
                        self.settings.parent = self
                        self.supported = None


                    class Settings(object):
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
                        _revision = '2015-10-14'

                        def __init__(self):
                            self.parent = None
                            self.received_optical_power_degrade_threshold = None
                            self.received_optical_power_degrade_threshold_set = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-drivers-media-eth-oper:settings'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.received_optical_power_degrade_threshold is not None:
                                return True

                            if self.received_optical_power_degrade_threshold_set is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
                            return meta._meta_table['EthernetInterface.Interfaces.Interface.Layer1Info.OpdMonitoring.Settings']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-drivers-media-eth-oper:opd-monitoring'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.settings is not None and self.settings._has_data():
                            return True

                        if self.supported is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
                        return meta._meta_table['EthernetInterface.Interfaces.Interface.Layer1Info.OpdMonitoring']['meta_info']


                class PfcInfo(object):
                    """
                    Priority flow control information
                    
                    .. attribute:: priority_enabled_bitmap
                    
                    	Priority bitmap
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: priority_flowcontrol
                    
                    	Port operational priority flow control
                    	**type**\:   :py:class:`EtherPfcEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EtherPfcEnum>`
                    
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
                    _revision = '2015-10-14'

                    def __init__(self):
                        self.parent = None
                        self.priority_enabled_bitmap = None
                        self.priority_flowcontrol = None
                        self.rx_frame = YLeafList()
                        self.rx_frame.parent = self
                        self.rx_frame.name = 'rx_frame'
                        self.tx_frame = YLeafList()
                        self.tx_frame.parent = self
                        self.tx_frame.name = 'tx_frame'

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-drivers-media-eth-oper:pfc-info'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.priority_enabled_bitmap is not None:
                            return True

                        if self.priority_flowcontrol is not None:
                            return True

                        if self.rx_frame is not None:
                            for child in self.rx_frame:
                                if child is not None:
                                    return True

                        if self.tx_frame is not None:
                            for child in self.tx_frame:
                                if child is not None:
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
                        return meta._meta_table['EthernetInterface.Interfaces.Interface.Layer1Info.PfcInfo']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-drivers-media-eth-oper:layer1-info'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.autoneg is not None and self.autoneg._has_data():
                        return True

                    if self.bandwidth is not None:
                        return True

                    if self.bandwidth_utilization is not None:
                        return True

                    if self.ber_monitoring is not None and self.ber_monitoring._has_data():
                        return True

                    if self.current_alarms is not None and self.current_alarms._has_data():
                        return True

                    if self.duplex is not None:
                        return True

                    if self.error_counts is not None and self.error_counts._has_data():
                        return True

                    if self.flowcontrol is not None:
                        return True

                    if self.ipg is not None:
                        return True

                    if self.laser_squelch_enabled is not None:
                        return True

                    if self.led_state is not None:
                        return True

                    if self.link_state is not None:
                        return True

                    if self.opd_monitoring is not None and self.opd_monitoring._has_data():
                        return True

                    if self.pfc_info is not None and self.pfc_info._has_data():
                        return True

                    if self.previous_alarms is not None and self.previous_alarms._has_data():
                        return True

                    if self.speed is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
                    return meta._meta_table['EthernetInterface.Interfaces.Interface.Layer1Info']['meta_info']


            class MacInfo(object):
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
                _revision = '2015-10-14'

                def __init__(self):
                    self.parent = None
                    self.burned_in_mac_address = None
                    self.mru = None
                    self.mtu = None
                    self.multicast_mac_filters = EthernetInterface.Interfaces.Interface.MacInfo.MulticastMacFilters()
                    self.multicast_mac_filters.parent = self
                    self.operational_mac_address = None
                    self.unicast_mac_filters = EthernetInterface.Interfaces.Interface.MacInfo.UnicastMacFilters()
                    self.unicast_mac_filters.parent = self


                class UnicastMacFilters(object):
                    """
                    Port unicast MAC filter information
                    
                    .. attribute:: unicast_mac_address
                    
                    	MAC addresses in the unicast ingress destination MAC filter
                    	**type**\:  list of str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    

                    """

                    _prefix = 'drivers-media-eth-oper'
                    _revision = '2015-10-14'

                    def __init__(self):
                        self.parent = None
                        self.unicast_mac_address = YLeafList()
                        self.unicast_mac_address.parent = self
                        self.unicast_mac_address.name = 'unicast_mac_address'

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-drivers-media-eth-oper:unicast-mac-filters'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.unicast_mac_address is not None:
                            for child in self.unicast_mac_address:
                                if child is not None:
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
                        return meta._meta_table['EthernetInterface.Interfaces.Interface.MacInfo.UnicastMacFilters']['meta_info']


                class MulticastMacFilters(object):
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
                    _revision = '2015-10-14'

                    def __init__(self):
                        self.parent = None
                        self.multicast_mac_address = YList()
                        self.multicast_mac_address.parent = self
                        self.multicast_mac_address.name = 'multicast_mac_address'
                        self.multicast_promiscuous = None


                    class MulticastMacAddress(object):
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
                        _revision = '2015-10-14'

                        def __init__(self):
                            self.parent = None
                            self.mac_address = None
                            self.mask = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-drivers-media-eth-oper:multicast-mac-address'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.mac_address is not None:
                                return True

                            if self.mask is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
                            return meta._meta_table['EthernetInterface.Interfaces.Interface.MacInfo.MulticastMacFilters.MulticastMacAddress']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-drivers-media-eth-oper:multicast-mac-filters'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.multicast_mac_address is not None:
                            for child_ref in self.multicast_mac_address:
                                if child_ref._has_data():
                                    return True

                        if self.multicast_promiscuous is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
                        return meta._meta_table['EthernetInterface.Interfaces.Interface.MacInfo.MulticastMacFilters']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-drivers-media-eth-oper:mac-info'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.burned_in_mac_address is not None:
                        return True

                    if self.mru is not None:
                        return True

                    if self.mtu is not None:
                        return True

                    if self.multicast_mac_filters is not None and self.multicast_mac_filters._has_data():
                        return True

                    if self.operational_mac_address is not None:
                        return True

                    if self.unicast_mac_filters is not None and self.unicast_mac_filters._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
                    return meta._meta_table['EthernetInterface.Interfaces.Interface.MacInfo']['meta_info']


            class TransportInfo(object):
                """
                Transport state information
                
                .. attribute:: ains_status
                
                	AINS Soak status
                	**type**\:   :py:class:`EtherAinsStatusEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EtherAinsStatusEnum>`
                
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
                _revision = '2015-10-14'

                def __init__(self):
                    self.parent = None
                    self.ains_status = None
                    self.maintenance_mode_enabled = None
                    self.remaining_duration = None
                    self.total_duration = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-drivers-media-eth-oper:transport-info'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.ains_status is not None:
                        return True

                    if self.maintenance_mode_enabled is not None:
                        return True

                    if self.remaining_duration is not None:
                        return True

                    if self.total_duration is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
                    return meta._meta_table['EthernetInterface.Interfaces.Interface.TransportInfo']['meta_info']

            @property
            def _common_path(self):
                if self.interface_name is None:
                    raise YPYModelError('Key property interface_name is None')

                return '/Cisco-IOS-XR-drivers-media-eth-oper:ethernet-interface/Cisco-IOS-XR-drivers-media-eth-oper:interfaces/Cisco-IOS-XR-drivers-media-eth-oper:interface[Cisco-IOS-XR-drivers-media-eth-oper:interface-name = ' + str(self.interface_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.interface_name is not None:
                    return True

                if self.admin_state is not None:
                    return True

                if self.layer1_info is not None and self.layer1_info._has_data():
                    return True

                if self.mac_info is not None and self.mac_info._has_data():
                    return True

                if self.oper_state_up is not None:
                    return True

                if self.phy_info is not None and self.phy_info._has_data():
                    return True

                if self.transport_info is not None and self.transport_info._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
                return meta._meta_table['EthernetInterface.Interfaces.Interface']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-drivers-media-eth-oper:ethernet-interface/Cisco-IOS-XR-drivers-media-eth-oper:interfaces'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.interface is not None:
                for child_ref in self.interface:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
            return meta._meta_table['EthernetInterface.Interfaces']['meta_info']


    class Berts(object):
        """
        Ethernet controller BERT table
        
        .. attribute:: bert
        
        	Ethernet BERT information
        	**type**\: list of    :py:class:`Bert <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Berts.Bert>`
        
        

        """

        _prefix = 'drivers-media-eth-oper'
        _revision = '2015-10-14'

        def __init__(self):
            self.parent = None
            self.bert = YList()
            self.bert.parent = self
            self.bert.name = 'bert'


        class Bert(object):
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
            _revision = '2015-10-14'

            def __init__(self):
                self.parent = None
                self.interface_name = None
                self.bert_status = EthernetInterface.Berts.Bert.BertStatus()
                self.bert_status.parent = self
                self.port_bert_interval = None
                self.time_left = None


            class BertStatus(object):
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
                	**type**\:   :py:class:`EthernetDevEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetDevEnum>`
                
                .. attribute:: error_type
                
                	Bit, block or frame error
                	**type**\:   :py:class:`EthernetBertErrCntEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetBertErrCntEnum>`
                
                .. attribute:: interface_device
                
                	Interface being tested
                	**type**\:   :py:class:`EthernetDevIfEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetDevIfEnum>`
                
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
                	**type**\:   :py:class:`EthernetBertPatternEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_oper.EthernetBertPatternEnum>`
                
                .. attribute:: transmit_count
                
                	Transmit count (if 0x2 set in flag)
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'drivers-media-eth-oper'
                _revision = '2015-10-14'

                def __init__(self):
                    self.parent = None
                    self.bert_state_enabled = None
                    self.data_availability = None
                    self.device_under_test = None
                    self.error_type = None
                    self.interface_device = None
                    self.receive_count = None
                    self.receive_errors = None
                    self.test_pattern = None
                    self.transmit_count = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-drivers-media-eth-oper:bert-status'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.bert_state_enabled is not None:
                        return True

                    if self.data_availability is not None:
                        return True

                    if self.device_under_test is not None:
                        return True

                    if self.error_type is not None:
                        return True

                    if self.interface_device is not None:
                        return True

                    if self.receive_count is not None:
                        return True

                    if self.receive_errors is not None:
                        return True

                    if self.test_pattern is not None:
                        return True

                    if self.transmit_count is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
                    return meta._meta_table['EthernetInterface.Berts.Bert.BertStatus']['meta_info']

            @property
            def _common_path(self):
                if self.interface_name is None:
                    raise YPYModelError('Key property interface_name is None')

                return '/Cisco-IOS-XR-drivers-media-eth-oper:ethernet-interface/Cisco-IOS-XR-drivers-media-eth-oper:berts/Cisco-IOS-XR-drivers-media-eth-oper:bert[Cisco-IOS-XR-drivers-media-eth-oper:interface-name = ' + str(self.interface_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.interface_name is not None:
                    return True

                if self.bert_status is not None and self.bert_status._has_data():
                    return True

                if self.port_bert_interval is not None:
                    return True

                if self.time_left is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
                return meta._meta_table['EthernetInterface.Berts.Bert']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-drivers-media-eth-oper:ethernet-interface/Cisco-IOS-XR-drivers-media-eth-oper:berts'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.bert is not None:
                for child_ref in self.bert:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
            return meta._meta_table['EthernetInterface.Berts']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-drivers-media-eth-oper:ethernet-interface'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.berts is not None and self.berts._has_data():
            return True

        if self.interfaces is not None and self.interfaces._has_data():
            return True

        if self.statistics is not None and self.statistics._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
        return meta._meta_table['EthernetInterface']['meta_info']


