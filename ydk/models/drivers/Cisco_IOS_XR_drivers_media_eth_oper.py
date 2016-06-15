""" Cisco_IOS_XR_drivers_media_eth_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR drivers\-media\-eth package operational data.

This module contains definitions
for the following management objects\:
  ethernet\-interface\: Ethernet operational data

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
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

    .. data:: ALARM_NOT_SUPPORTED = 0

    	Not supported on this interface

    .. data:: ALARM_SET = 1

    	Alarm set

    .. data:: ALARM_NOT_SET = 2

    	Alarm not set

    """

    ALARM_NOT_SUPPORTED = 0

    ALARM_SET = 1

    ALARM_NOT_SET = 2


    @staticmethod
    def _meta_info():
        from ydk.models.drivers._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
        return meta._meta_table['EthCtrlrAlarmStateEnum']


class EtherAinsStatusEnum(Enum):
    """
    EtherAinsStatusEnum

    Ether ains status

    .. data:: AINS_SOAK_STATUS_NONE = 0

    	AINS Soak timer not running

    .. data:: AINS_SOAK_STATUS_PENDING = 1

    	AINS Soak timer pending

    .. data:: AINS_SOAK_STATUS_RUNNING = 2

    	AINS Soak timer running

    """

    AINS_SOAK_STATUS_NONE = 0

    AINS_SOAK_STATUS_PENDING = 1

    AINS_SOAK_STATUS_RUNNING = 2


    @staticmethod
    def _meta_info():
        from ydk.models.drivers._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
        return meta._meta_table['EtherAinsStatusEnum']


class EtherDomAlarmEnum(Enum):
    """
    EtherDomAlarmEnum

    Ether dom alarm

    .. data:: NO_INFORMATION = 0

    	DOM Alarm information is not available

    .. data:: ALARM_HIGH = 1

    	Alarm high

    .. data:: WARNING_HIGH = 2

    	Warning high

    .. data:: NORMAL = 3

    	Within normal parameters

    .. data:: WARNING_LOW = 4

    	Warning low

    .. data:: ALARM_LOW = 5

    	Alarm low

    """

    NO_INFORMATION = 0

    ALARM_HIGH = 1

    WARNING_HIGH = 2

    NORMAL = 3

    WARNING_LOW = 4

    ALARM_LOW = 5


    @staticmethod
    def _meta_info():
        from ydk.models.drivers._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
        return meta._meta_table['EtherDomAlarmEnum']


class EtherFlowcontrolEnum(Enum):
    """
    EtherFlowcontrolEnum

    Flowcontrol type

    .. data:: NO_FLOWCONTROL = 0

    	No flow control (disabled)

    .. data:: EGRESS = 1

    	Traffic egress (pause frames ingress)

    .. data:: INGRESS = 2

    	Traffic ingress (pause frames egress)

    .. data:: BIDIRECTIONAL = 3

    	On both ingress and egress

    """

    NO_FLOWCONTROL = 0

    EGRESS = 1

    INGRESS = 2

    BIDIRECTIONAL = 3


    @staticmethod
    def _meta_info():
        from ydk.models.drivers._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
        return meta._meta_table['EtherFlowcontrolEnum']


class EtherLedStateEnum(Enum):
    """
    EtherLedStateEnum

    Ether led state

    .. data:: LED_STATE_UNKNOWN = 0

    	LED state is unknown

    .. data:: LED_OFF = 1

    	LED is off

    .. data:: GREEN_ON = 2

    	LED is green

    .. data:: GREEN_FLASHING = 3

    	LED is flashing green

    .. data:: YELLOW_ON = 4

    	LED is yellow

    .. data:: YELLOW_FLASHING = 5

    	LED is flashing yellow

    .. data:: RED_ON = 6

    	LED is red

    .. data:: RED_FLASHING = 7

    	LED is flashing red

    """

    LED_STATE_UNKNOWN = 0

    LED_OFF = 1

    GREEN_ON = 2

    GREEN_FLASHING = 3

    YELLOW_ON = 4

    YELLOW_FLASHING = 5

    RED_ON = 6

    RED_FLASHING = 7


    @staticmethod
    def _meta_info():
        from ydk.models.drivers._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
        return meta._meta_table['EtherLedStateEnum']


class EtherLinkStateEnum(Enum):
    """
    EtherLinkStateEnum

    Ethernet link state\: IEEE 802.3/802.3ae clause 30

    .5.1.1.4

    .. data:: STATE_UNDEFINED = 0

    	State undefined

    .. data:: UNKNOWN_STATE = 1

    	Initializing, true state not yet known

    .. data:: AVAILABLE = 2

    	Link or light normal, loopback normal

    .. data:: NOT_AVAILABLE = 3

    	Link loss or low light, no loopback

    .. data:: REMOTE_FAULT = 4

    	Remote fault with no detail

    .. data:: INVALID_SIGNAL = 5

    	Invalid signal, applies only to 10BASE-FB

    .. data:: REMOTE_JABBER = 6

    	Remote fault, reason known to be jabber

    .. data:: LINK_LOSS = 7

    	Remote fault, reason known to be far-end link

    	loss

    .. data:: REMOTE_TEST = 8

    	Remote fault, reason known to be test

    .. data:: OFFLINE = 9

    	Offline (applies to auto-negotiation)

    .. data:: AUTO_NEG_ERROR = 10

    	Auto-Negotiation Error

    .. data:: PMD_LINK_FAULT = 11

    	PMD/PMA receive link fault

    .. data:: FRAME_LOSS = 12

    	WIS loss of frames

    .. data:: SIGNAL_LOSS = 13

    	WIS loss of signal

    .. data:: LINK_FAULT = 14

    	PCS receive link fault

    .. data:: EXCESSIVE_BER = 15

    	PCS Bit Error Rate monitor reporting excessive

    	error rate

    .. data:: DXS_LINK_FAULT = 16

    	DTE XGXS receive link fault

    .. data:: PXS_LINK_FAULT = 17

    	PHY XGXS transmit link fault

    .. data:: SECURITY = 18

    	Security failure (not a valid part)

    .. data:: PHY_NOT_PRESENT = 19

    	The optics for the port are not present

    .. data:: NO_OPTIC_LICENSE = 20

    	License error (No advanced optical license)

    .. data:: UNSUPPORTED_MODULE = 21

    	Module is not supported

    .. data:: DWDM_LASER_SHUT = 22

    	DWDM Laser shutdown

    .. data:: WANPHY_LASER_SHUT = 23

    	WANPHY Laser shutdown

    .. data:: INCOMPATIBLE_CONFIG = 24

    	Incompatible configuration

    .. data:: SYSTEM_ERROR = 25

    	System error

    .. data:: WAN_FRAMING_ERROR = 26

    	WAN Framing Error

    .. data:: OTN_FRAMING_ERROR = 27

    	OTN Framing Error

    """

    STATE_UNDEFINED = 0

    UNKNOWN_STATE = 1

    AVAILABLE = 2

    NOT_AVAILABLE = 3

    REMOTE_FAULT = 4

    INVALID_SIGNAL = 5

    REMOTE_JABBER = 6

    LINK_LOSS = 7

    REMOTE_TEST = 8

    OFFLINE = 9

    AUTO_NEG_ERROR = 10

    PMD_LINK_FAULT = 11

    FRAME_LOSS = 12

    SIGNAL_LOSS = 13

    LINK_FAULT = 14

    EXCESSIVE_BER = 15

    DXS_LINK_FAULT = 16

    PXS_LINK_FAULT = 17

    SECURITY = 18

    PHY_NOT_PRESENT = 19

    NO_OPTIC_LICENSE = 20

    UNSUPPORTED_MODULE = 21

    DWDM_LASER_SHUT = 22

    WANPHY_LASER_SHUT = 23

    INCOMPATIBLE_CONFIG = 24

    SYSTEM_ERROR = 25

    WAN_FRAMING_ERROR = 26

    OTN_FRAMING_ERROR = 27


    @staticmethod
    def _meta_info():
        from ydk.models.drivers._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
        return meta._meta_table['EtherLinkStateEnum']


class EtherPhyPresentEnum(Enum):
    """
    EtherPhyPresentEnum

    Ether phy present

    .. data:: PHY_NOT_PRESENT = 0

    	No PHY present

    .. data:: PHY_PRESENT = 1

    	PHY is present

    .. data:: NO_INFORMATION = 2

    	State is unknown

    """

    PHY_NOT_PRESENT = 0

    PHY_PRESENT = 1

    NO_INFORMATION = 2


    @staticmethod
    def _meta_info():
        from ydk.models.drivers._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
        return meta._meta_table['EtherPhyPresentEnum']


class EthernetBertErrCntEnum(Enum):
    """
    EthernetBertErrCntEnum

    Ethernet bert err cnt

    .. data:: NO_COUNT_TYPE = 0

    	no count type

    .. data:: BIT_ERROR_COUNT = 1

    	bit error count

    .. data:: FRAME_ERROR_COUNT = 2

    	frame error count

    .. data:: BLOCK_ERROR_COUNT = 3

    	block error count

    .. data:: ETHERNET_BERT_ERR_CNT_TYPES = 4

    	ethernet bert err cnt types

    """

    NO_COUNT_TYPE = 0

    BIT_ERROR_COUNT = 1

    FRAME_ERROR_COUNT = 2

    BLOCK_ERROR_COUNT = 3

    ETHERNET_BERT_ERR_CNT_TYPES = 4


    @staticmethod
    def _meta_info():
        from ydk.models.drivers._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
        return meta._meta_table['EthernetBertErrCntEnum']


class EthernetBertPatternEnum(Enum):
    """
    EthernetBertPatternEnum

    Ethernet test patterns (IEEE spec 36A/48A)

    .. data:: NO_TEST_PATTERN = 0

    	no test pattern

    .. data:: HIGH_FREQUENCY = 1

    	high frequency

    .. data:: LOW_FREQUENCY = 2

    	low frequency

    .. data:: MIXED_FREQUENCY = 3

    	mixed frequency

    .. data:: CONTINUOUS_RANDOM = 4

    	continuous random

    .. data:: CONTINUOUS_JITTER = 5

    	continuous jitter

    .. data:: LONG_CONTINUOUS_RANDOM = 6

    	long continuous random

    .. data:: SHORT_CONTINUOUS_RANDOM = 7

    	short continuous random

    .. data:: PSEUDORANDOM_SEED_A = 8

    	pseudorandom seed a

    .. data:: PSEUDORANDOM_SEED_B = 9

    	pseudorandom seed b

    .. data:: PRBS31 = 10

    	prbs31

    .. data:: SQUARE_WAVE = 11

    	square wave

    .. data:: PSEUDORANDOM = 12

    	pseudorandom

    .. data:: ETHERNET_BERT_PATTERN_TYPES = 13

    	ethernet bert pattern types

    """

    NO_TEST_PATTERN = 0

    HIGH_FREQUENCY = 1

    LOW_FREQUENCY = 2

    MIXED_FREQUENCY = 3

    CONTINUOUS_RANDOM = 4

    CONTINUOUS_JITTER = 5

    LONG_CONTINUOUS_RANDOM = 6

    SHORT_CONTINUOUS_RANDOM = 7

    PSEUDORANDOM_SEED_A = 8

    PSEUDORANDOM_SEED_B = 9

    PRBS31 = 10

    SQUARE_WAVE = 11

    PSEUDORANDOM = 12

    ETHERNET_BERT_PATTERN_TYPES = 13


    @staticmethod
    def _meta_info():
        from ydk.models.drivers._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
        return meta._meta_table['EthernetBertPatternEnum']


class EthernetDevEnum(Enum):
    """
    EthernetDevEnum

    Ethernet dev

    .. data:: NO_DEVICE = 0

    	no device

    .. data:: PMA_PMD = 1

    	pma pmd

    .. data:: WIS = 2

    	wis

    .. data:: PCS = 3

    	pcs

    .. data:: PHY_XS = 4

    	phy xs

    .. data:: DTE_XS = 5

    	dte xs

    .. data:: ETHERNET_NUM_DEV = 6

    	ethernet num dev

    """

    NO_DEVICE = 0

    PMA_PMD = 1

    WIS = 2

    PCS = 3

    PHY_XS = 4

    DTE_XS = 5

    ETHERNET_NUM_DEV = 6


    @staticmethod
    def _meta_info():
        from ydk.models.drivers._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
        return meta._meta_table['EthernetDevEnum']


class EthernetDevIfEnum(Enum):
    """
    EthernetDevIfEnum

    Ethernet dev if

    .. data:: NO_INTERFACE = 0

    	no interface

    .. data:: XGMII = 1

    	xgmii

    .. data:: XAUI = 2

    	xaui

    .. data:: ETHERNET_NUM_DEV_IF = 3

    	ethernet num dev if

    """

    NO_INTERFACE = 0

    XGMII = 1

    XAUI = 2

    ETHERNET_NUM_DEV_IF = 3


    @staticmethod
    def _meta_info():
        from ydk.models.drivers._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
        return meta._meta_table['EthernetDevIfEnum']


class EthernetDuplexEnum(Enum):
    """
    EthernetDuplexEnum

    Duplexity

    .. data:: ETHERNET_DUPLEX_INVALID = 0

    	ethernet duplex invalid

    .. data:: HALF_DUPLEX = 1

    	half duplex

    .. data:: FULL_DUPLEX = 2

    	full duplex

    """

    ETHERNET_DUPLEX_INVALID = 0

    HALF_DUPLEX = 1

    FULL_DUPLEX = 2


    @staticmethod
    def _meta_info():
        from ydk.models.drivers._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
        return meta._meta_table['EthernetDuplexEnum']


class EthernetFecEnum(Enum):
    """
    EthernetFecEnum

    FEC type

    .. data:: NOT_CONFIGURED = 0

    	FEC not configured

    .. data:: STANDARD = 1

    	Reed-Solomon encoding

    .. data:: DISABLED = 2

    	FEC explicitly disabled

    """

    NOT_CONFIGURED = 0

    STANDARD = 1

    DISABLED = 2


    @staticmethod
    def _meta_info():
        from ydk.models.drivers._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
        return meta._meta_table['EthernetFecEnum']


class EthernetIpgEnum(Enum):
    """
    EthernetIpgEnum

    Inter packet gap

    .. data:: STANDARD = 0

    	IEEE standard value of 12

    .. data:: NON_STANDARD = 1

    	Non-standard value of 16

    """

    STANDARD = 0

    NON_STANDARD = 1


    @staticmethod
    def _meta_info():
        from ydk.models.drivers._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
        return meta._meta_table['EthernetIpgEnum']


class EthernetLoopbackEnum(Enum):
    """
    EthernetLoopbackEnum

    Loopback type

    .. data:: NO_LOOPBACK = 0

    	Disabled

    .. data:: INTERNAL = 1

    	Loopback in the framer

    .. data:: LINE = 2

    	Loops peer's packets back to them

    .. data:: EXTERNAL = 3

    	tx externally connected to rx

    """

    NO_LOOPBACK = 0

    INTERNAL = 1

    LINE = 2

    EXTERNAL = 3


    @staticmethod
    def _meta_info():
        from ydk.models.drivers._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
        return meta._meta_table['EthernetLoopbackEnum']


class EthernetMediaEnum(Enum):
    """
    EthernetMediaEnum

    Ethernet media types\: IEEE 802.3/802.3ae clause

    30.5.1.1.2

    .. data:: ETHERNET_OTHER = 0

    	IEEE 802.3/802.3ae clause 30.2.5

    .. data:: ETHERNET_UNKNOWN = 1

    	Initializing, true state or type not yet known

    .. data:: ETHERNET_AUI = 2

    	No internal MAU, view from AUI

    .. data:: ETHERNET_10BASE5 = 3

    	Thick coax MAU

    .. data:: ETHERNET_FOIRL = 4

    	FOIRL MAU as specified in 9.9

    .. data:: ETHERNET_10BASE2 = 5

    	Thin coax MAU

    .. data:: ETHERNET_10BROAD36 = 6

    	Broadband DTE MAU

    .. data:: ETHERNET_10BASE = 7

    	UTP MAU, duplexity unknown

    .. data:: ETHERNET_10BASE_THD = 8

    	UTP MAU, half duplex

    .. data:: ETHERNET_10BASE_TFD = 9

    	UTP MAU, full duplex

    .. data:: ETHERNET_10BASE_FP = 10

    	Passive fiber MAU

    .. data:: ETHERNET_10BASE_FB = 11

    	Synchronous fiber MAU

    .. data:: ETHERNET_10BASE_FL = 12

    	Asynchronous fiber MAU, duplexity unknown

    .. data:: ETHERNET_10BASE_FLHD = 13

    	Asynchronous fiber MAU, half duplex

    .. data:: ETHERNET_10BASE_FLFD = 14

    	Asynchronous fiber MAU, full duplex

    .. data:: ETHERNET_100BASE_T4 = 15

    	Four-pair Category 3 UTP

    .. data:: ETHERNET_100BASE_TX = 16

    	Two-pair Category 5 UTP, duplexity unknown

    .. data:: ETHERNET_100BASE_TXHD = 17

    	Two-pair Category 5 UTP, half duplex

    .. data:: ETHERNET_100BASE_TXFD = 18

    	Two-pair Category 5 UTP, full duplex

    .. data:: ETHERNET_100BASE_FX = 19

    	X fiber over PMD, duplexity unknown

    .. data:: ETHERNET_100BASE_FXHD = 20

    	X fiber over PMD, half duplex

    .. data:: ETHERNET_100BASE_FXFD = 21

    	X fiber over PMD, full duplex

    .. data:: ETHERNET_100BASE_EX = 22

    	X fiber over PMD (40km), duplexity unknown

    .. data:: ETHERNET_100BASE_EXHD = 23

    	X fiber over PMD (40km), half duplex

    .. data:: ETHERNET_100BASE_EXFD = 24

    	X fiber over PMD (40km), full duplex

    .. data:: ETHERNET_100BASE_T2 = 25

    	Two-pair Category 3 UTP, duplexity unknown

    .. data:: ETHERNET_100BASE_T2HD = 26

    	Two-pair Category 3 UTP, half duplex

    .. data:: ETHERNET_100BASE_T2FD = 27

    	Two-pair Category 3 UTP, full duplex

    .. data:: ETHERNET_1000BASE_X = 28

    	X PCS/PMA, duplexity unknown

    .. data:: ETHERNET_1000BASE_XHD = 29

    	X 1000BASE-XHDX PCS/PMA, half duplex

    .. data:: ETHERNET_1000BASE_XFD = 30

    	X PCS/PMA, full duplex

    .. data:: ETHERNET_1000BASE_LX = 31

    	X fiber over long-wl laser PMD, duplexity

    	unknown

    .. data:: ETHERNET_1000BASE_LXHD = 32

    	X fiber over long-wl laser PMD, half duplex

    .. data:: ETHERNET_1000BASE_LXFD = 33

    	X fiber over long-wl laser PMD, full duplex

    .. data:: ETHERNET_1000BASE_SX = 34

    	X fiber over short-wl laser PMD, duplexity

    	unknown

    .. data:: ETHERNET_1000BASE_SXHD = 35

    	X fiber over short-wl laser PMD, half duplex

    .. data:: ETHERNET_1000BASE_SXFD = 36

    	X fiber over short-wl laser PMD, full duplex

    .. data:: ETHERNET_1000BASE_CX = 37

    	X copper over 150-Ohm balanced PMD, duplexity

    	unknown

    .. data:: ETHERNET_1000BASE_CXHD = 38

    	X copper over 150-Ohm balancedPMD, half duplex

    .. data:: ETHERNET_1000BASE_CXFD = 39

    	X copper over 150-Ohm balancedPMD, full duplex

    .. data:: ETHERNET_1000BASE = 40

    	Four-pair Category 5 UTP PHY, duplexity unknown

    .. data:: ETHERNET_1000BASE_THD = 41

    	Four-pair Category 5 UTP PHY, half duplex

    .. data:: ETHERNET_1000BASE_TFD = 42

    	Four-pair Category 5 UTP PHY, full duplex

    .. data:: ETHERNET_10GBASE_X = 43

    	X PCS/PMA 

    .. data:: ETHERNET_10GBASE_LX4 = 44

    	X fiber over 4 lane 1310nm optics

    .. data:: ETHERNET_10GBASE_R = 45

    	R PCS/PMA

    .. data:: ETHERNET_10GBASE_ER = 46

    	R fiber over 1550nm optics

    .. data:: ETHERNET_10GBASE_LR = 47

    	R fiber over 1310nm optics

    .. data:: ETHERNET_10GBASE_SR = 48

    	R fiber over 850nm optics

    .. data:: ETHERNET_10GBASE_W = 49

    	W PCS/PMA

    .. data:: ETHERNET_10GBASE_EW = 50

    	W fiber over 1550nm optics

    .. data:: ETHERNET_10GBASE_LW = 51

    	W fiber over 1310nm optics

    .. data:: ETHERNET_10GBASE_SW = 52

    	W fiber over 850nm optics

    .. data:: ETHERNET_1000BASE_ZX = 53

    	Single-mode fiber over 1550nm optics (Cisco)

    .. data:: ETHERNET_1000BASE_CWDM = 54

    	CWDM with unknown wavelength optics

    .. data:: ETHERNET_1000BASE_CWDM_1470 = 55

    	CWDM with 1470nm optics

    .. data:: ETHERNET_1000BASE_CWDM_1490 = 56

    	CWDM with 1490nm optics

    .. data:: ETHERNET_1000BASE_CWDM_1510 = 57

    	CWDM with 1510nm optics

    .. data:: ETHERNET_1000BASE_CWDM_1530 = 58

    	CWDM with 1530nm optics

    .. data:: ETHERNET_1000BASE_CWDM_1550 = 59

    	CWDM with 1550nm optics

    .. data:: ETHERNET_1000BASE_CWDM_1570 = 60

    	CWDM with 1570nm optics

    .. data:: ETHERNET_1000BASE_CWDM_1590 = 61

    	CWDM with 1590nm optics

    .. data:: ETHERNET_1000BASE_CWDM_1610 = 62

    	CWDM with 1610nm optics

    .. data:: ETHERNET_10GBASE_ZR = 63

    	Cisco-defined, over 1550nm optics

    .. data:: ETHERNET_10GBASE_DWDM = 64

    	DWDM optics

    .. data:: ETHERNET_100GBASE_LR4 = 65

    	fiber over 4 lane optics (long reach)

    .. data:: ETHERNET_1000BASE_DWDM = 66

    	DWDM optics

    .. data:: ETHERNET_1000BASE_DWDM_1533 = 67

    	DWDM with 1533nm optics

    .. data:: ETHERNET_1000BASE_DWDM_1537 = 68

    	DWDM with 1537nm optics

    .. data:: ETHERNET_1000BASE_DWDM_1541 = 69

    	DWDM with 1541nm optics

    .. data:: ETHERNET_1000BASE_DWDM_1545 = 70

    	DWDM with 1545nm optics

    .. data:: ETHERNET_1000BASE_DWDM_1549 = 71

    	DWDM with 1549nm optics

    .. data:: ETHERNET_1000BASE_DWDM_1553 = 72

    	DWDM with 1553nm optics

    .. data:: ETHERNET_1000BASE_DWDM_1557 = 73

    	DWDM with 1557nm optics

    .. data:: ETHERNET_1000BASE_DWDM_1561 = 74

    	DWDM with 1561nm optics

    .. data:: ETHERNET_40GBASE_LR4 = 75

    	fiber over 4 lane optics (long reach)

    .. data:: ETHERNET_40GBASE_ER4 = 76

    	fiber over 4 lane optics (extended reach)

    .. data:: ETHERNET_100GBASE_ER4 = 77

    	fiber over 4 lane optics (extended reach)

    .. data:: ETHERNET_1000BASE_EX = 78

    	X fiber over 1310nm optics

    .. data:: ETHERNET_1000BASE_BX10_D = 79

    	X fibre (D, 10km)

    .. data:: ETHERNET_1000BASE_BX10_U = 80

    	X fibre (U, 10km)

    .. data:: ETHERNET_1000BASE_DWDM_1561_42 = 81

    	DWDM with 1561.42nm optics

    .. data:: ETHERNET_1000BASE_DWDM_1560_61 = 82

    	DWDM with 1560.61nm optics

    .. data:: ETHERNET_1000BASE_DWDM_1559_79 = 83

    	DWDM with 1559.79nm optics

    .. data:: ETHERNET_1000BASE_DWDM_1558_98 = 84

    	DWDM with 1558.98nm optics

    .. data:: ETHERNET_1000BASE_DWDM_1558_17 = 85

    	DWDM with 1558.17nm optics

    .. data:: ETHERNET_1000BASE_DWDM_1557_36 = 86

    	DWDM with 1557.36nm optics

    .. data:: ETHERNET_1000BASE_DWDM_1556_55 = 87

    	DWDM with 1556.55nm optics

    .. data:: ETHERNET_1000BASE_DWDM_1555_75 = 88

    	DWDM with 1555.75nm optics

    .. data:: ETHERNET_1000BASE_DWDM_1554_94 = 89

    	DWDM with 1554.94nm optics

    .. data:: ETHERNET_1000BASE_DWDM_1554_13 = 90

    	DWDM with 1554.13nm optics

    .. data:: ETHERNET_1000BASE_DWDM_1553_33 = 91

    	DWDM with 1553.33nm optics

    .. data:: ETHERNET_1000BASE_DWDM_1552_52 = 92

    	DWDM with 1552.52nm optics

    .. data:: ETHERNET_1000BASE_DWDM_1551_72 = 93

    	DWDM with 1551.72nm optics

    .. data:: ETHERNET_1000BASE_DWDM_1550_92 = 94

    	DWDM with 1550.92nm optics

    .. data:: ETHERNET_1000BASE_DWDM_1550_12 = 95

    	DWDM with 1550.12nm optics

    .. data:: ETHERNET_1000BASE_DWDM_1549_32 = 96

    	DWDM with 1549.32nm optics

    .. data:: ETHERNET_1000BASE_DWDM_1548_51 = 97

    	DWDM with 1548.51nm optics

    .. data:: ETHERNET_1000BASE_DWDM_1547_72 = 98

    	DWDM with 1547.72nm optics

    .. data:: ETHERNET_1000BASE_DWDM_1546_92 = 99

    	DWDM with 1546.92nm optics

    .. data:: ETHERNET_1000BASE_DWDM_1546_12 = 100

    	DWDM with 1546.12nm optics

    .. data:: ETHERNET_1000BASE_DWDM_1545_32 = 101

    	DWDM with 1545.32nm optics

    .. data:: ETHERNET_1000BASE_DWDM_1544_53 = 102

    	DWDM with 1544.53nm optics

    .. data:: ETHERNET_1000BASE_DWDM_1543_73 = 103

    	DWDM with 1543.73nm optics

    .. data:: ETHERNET_1000BASE_DWDM_1542_94 = 104

    	DWDM with 1542.94nm optics

    .. data:: ETHERNET_1000BASE_DWDM_1542_14 = 105

    	DWDM with 1542.14nm optics

    .. data:: ETHERNET_1000BASE_DWDM_1541_35 = 106

    	DWDM with 1541.35nm optics

    .. data:: ETHERNET_1000BASE_DWDM_1540_56 = 107

    	DWDM with 1540.56nm optics

    .. data:: ETHERNET_1000BASE_DWDM_1539_77 = 108

    	DWDM with 1539.77nm optics

    .. data:: ETHERNET_1000BASE_DWDM_1538_98 = 109

    	DWDM with 1538.98nm optics

    .. data:: ETHERNET_1000BASE_DWDM_1538_19 = 110

    	DWDM with 1538.19nm optics

    .. data:: ETHERNET_1000BASE_DWDM_1537_40 = 111

    	DWDM with 1537.40nm optics

    .. data:: ETHERNET_1000BASE_DWDM_1536_61 = 112

    	DWDM with 1536.61nm optics

    .. data:: ETHERNET_1000BASE_DWDM_1535_82 = 113

    	DWDM with 1535.82nm optics

    .. data:: ETHERNET_1000BASE_DWDM_1535_04 = 114

    	DWDM with 1535.04nm optics

    .. data:: ETHERNET_1000BASE_DWDM_1534_25 = 115

    	DWDM with 1534.25nm optics

    .. data:: ETHERNET_1000BASE_DWDM_1533_47 = 116

    	DWDM with 1533.47nm optics

    .. data:: ETHERNET_1000BASE_DWDM_1532_68 = 117

    	DWDM with 1532.68nm optics

    .. data:: ETHERNET_1000BASE_DWDM_1531_90 = 118

    	DWDM with 1531.90nm optics

    .. data:: ETHERNET_1000BASE_DWDM_1531_12 = 119

    	DWDM with 1531.12nm optics

    .. data:: ETHERNET_1000BASE_DWDM_1530_33 = 120

    	DWDM with 1530.33nm optics

    .. data:: ETHERNET_1000BASE_DWDM_TUNABLE = 121

    	DWDM with tunable optics

    .. data:: ETHERNET_10GBASE_DWDM_1561_42 = 122

    	DWDM with 1561.42nm optics

    .. data:: ETHERNET_10GBASE_DWDM_1560_61 = 123

    	DWDM with 1560.61nm optics

    .. data:: ETHERNET_10GBASE_DWDM_1559_79 = 124

    	DWDM with 1559.79nm optics

    .. data:: ETHERNET_10GBASE_DWDM_1558_98 = 125

    	DWDM with 1558.98nm optics

    .. data:: ETHERNET_10GBASE_DWDM_1558_17 = 126

    	DWDM with 1558.17nm optics

    .. data:: ETHERNET_10GBASE_DWDM_1557_36 = 127

    	DWDM with 1557.36nm optics

    .. data:: ETHERNET_10GBASE_DWDM_1556_55 = 128

    	DWDM with 1556.55nm optics

    .. data:: ETHERNET_10GBASE_DWDM_1555_75 = 129

    	DWDM with 1555.75nm optics

    .. data:: ETHERNET_10GBASE_DWDM_1554_94 = 130

    	DWDM with 1554.94nm optics

    .. data:: ETHERNET_10GBASE_DWDM_1554_13 = 131

    	DWDM with 1554.13nm optics

    .. data:: ETHERNET_10GBASE_DWDM_1553_33 = 132

    	DWDM with 1553.33nm optics

    .. data:: ETHERNET_10GBASE_DWDM_1552_52 = 133

    	DWDM with 1552.52nm optics

    .. data:: ETHERNET_10GBASE_DWDM_1551_72 = 134

    	DWDM with 1551.72nm optics

    .. data:: ETHERNET_10GBASE_DWDM_1550_92 = 135

    	DWDM with 1550.92nm optics

    .. data:: ETHERNET_10GBASE_DWDM_1550_12 = 136

    	DWDM with 1550.12nm optics

    .. data:: ETHERNET_10GBASE_DWDM_1549_32 = 137

    	DWDM with 1549.32nm optics

    .. data:: ETHERNET_10GBASE_DWDM_1548_51 = 138

    	DWDM with 1548.51nm optics

    .. data:: ETHERNET_10GBASE_DWDM_1547_72 = 139

    	DWDM with 1547.72nm optics

    .. data:: ETHERNET_10GBASE_DWDM_1546_92 = 140

    	DWDM with 1546.92nm optics

    .. data:: ETHERNET_10GBASE_DWDM_1546_12 = 141

    	DWDM with 1546.12nm optics

    .. data:: ETHERNET_10GBASE_DWDM_1545_32 = 142

    	DWDM with 1545.32nm optics

    .. data:: ETHERNET_10GBASE_DWDM_1544_53 = 143

    	DWDM with 1544.53nm optics

    .. data:: ETHERNET_10GBASE_DWDM_1543_73 = 144

    	DWDM with 1543.73nm optics

    .. data:: ETHERNET_10GBASE_DWDM_1542_94 = 145

    	DWDM with 1542.94nm optics

    .. data:: ETHERNET_10GBASE_DWDM_1542_14 = 146

    	DWDM with 1542.14nm optics

    .. data:: ETHERNET_10GBASE_DWDM_1541_35 = 147

    	DWDM with 1541.35nm optics

    .. data:: ETHERNET_10GBASE_DWDM_1540_56 = 148

    	DWDM with 1540.56nm optics

    .. data:: ETHERNET_10GBASE_DWDM_1539_77 = 149

    	DWDM with 1539.77nm optics

    .. data:: ETHERNET_10GBASE_DWDM_1538_98 = 150

    	DWDM with 1538.98nm optics

    .. data:: ETHERNET_10GBASE_DWDM_1538_19 = 151

    	DWDM with 1538.19nm optics

    .. data:: ETHERNET_10GBASE_DWDM_1537_40 = 152

    	DWDM with 1537.40nm optics

    .. data:: ETHERNET_10GBASE_DWDM_1536_61 = 153

    	DWDM with 1536.61nm optics

    .. data:: ETHERNET_10GBASE_DWDM_1535_82 = 154

    	DWDM with 1535.82nm optics

    .. data:: ETHERNET_10GBASE_DWDM_1535_04 = 155

    	DWDM with 1535.04nm optics

    .. data:: ETHERNET_10GBASE_DWDM_1534_25 = 156

    	DWDM with 1534.25nm optics

    .. data:: ETHERNET_10GBASE_DWDM_1533_47 = 157

    	DWDM with 1533.47nm optics

    .. data:: ETHERNET_10GBASE_DWDM_1532_68 = 158

    	DWDM with 1532.68nm optics

    .. data:: ETHERNET_10GBASE_DWDM_1531_90 = 159

    	DWDM with 1531.90nm optics

    .. data:: ETHERNET_10GBASE_DWDM_1531_12 = 160

    	DWDM with 1531.12nm optics

    .. data:: ETHERNET_10GBASE_DWDM_1530_33 = 161

    	DWDM with 1530.33nm optics

    .. data:: ETHERNET_10GBASE_DWDM_TUNABLE = 162

    	DWDM with tunable optics

    .. data:: ETHERNET_40GBASE_DWDM_1561_42 = 163

    	DWDM with 1561.42nm optics

    .. data:: ETHERNET_40GBASE_DWDM_1560_61 = 164

    	DWDM with 1560.61nm optics

    .. data:: ETHERNET_40GBASE_DWDM_1559_79 = 165

    	DWDM with 1559.79nm optics

    .. data:: ETHERNET_40GBASE_DWDM_1558_98 = 166

    	DWDM with 1558.98nm optics

    .. data:: ETHERNET_40GBASE_DWDM_1558_17 = 167

    	DWDM with 1558.17nm optics

    .. data:: ETHERNET_40GBASE_DWDM_1557_36 = 168

    	DWDM with 1557.36nm optics

    .. data:: ETHERNET_40GBASE_DWDM_1556_55 = 169

    	DWDM with 1556.55nm optics

    .. data:: ETHERNET_40GBASE_DWDM_1555_75 = 170

    	DWDM with 1555.75nm optics

    .. data:: ETHERNET_40GBASE_DWDM_1554_94 = 171

    	DWDM with 1554.94nm optics

    .. data:: ETHERNET_40GBASE_DWDM_1554_13 = 172

    	DWDM with 1554.13nm optics

    .. data:: ETHERNET_40GBASE_DWDM_1553_33 = 173

    	DWDM with 1553.33nm optics

    .. data:: ETHERNET_40GBASE_DWDM_1552_52 = 174

    	DWDM with 1552.52nm optics

    .. data:: ETHERNET_40GBASE_DWDM_1551_72 = 175

    	DWDM with 1551.72nm optics

    .. data:: ETHERNET_40GBASE_DWDM_1550_92 = 176

    	DWDM with 1550.92nm optics

    .. data:: ETHERNET_40GBASE_DWDM_1550_12 = 177

    	DWDM with 1550.12nm optics

    .. data:: ETHERNET_40GBASE_DWDM_1549_32 = 178

    	DWDM with 1549.32nm optics

    .. data:: ETHERNET_40GBASE_DWDM_1548_51 = 179

    	DWDM with 1548.51nm optics

    .. data:: ETHERNET_40GBASE_DWDM_1547_72 = 180

    	DWDM with 1547.72nm optics

    .. data:: ETHERNET_40GBASE_DWDM_1546_92 = 181

    	DWDM with 1546.92nm optics

    .. data:: ETHERNET_40GBASE_DWDM_1546_12 = 182

    	DWDM with 1546.12nm optics

    .. data:: ETHERNET_40GBASE_DWDM_1545_32 = 183

    	DWDM with 1545.32nm optics

    .. data:: ETHERNET_40GBASE_DWDM_1544_53 = 184

    	DWDM with 1544.53nm optics

    .. data:: ETHERNET_40GBASE_DWDM_1543_73 = 185

    	DWDM with 1543.73nm optics

    .. data:: ETHERNET_40GBASE_DWDM_1542_94 = 186

    	DWDM with 1542.94nm optics

    .. data:: ETHERNET_40GBASE_DWDM_1542_14 = 187

    	DWDM with 1542.14nm optics

    .. data:: ETHERNET_40GBASE_DWDM_1541_35 = 188

    	DWDM with 1541.35nm optics

    .. data:: ETHERNET_40GBASE_DWDM_1540_56 = 189

    	DWDM with 1540.56nm optics

    .. data:: ETHERNET_40GBASE_DWDM_1539_77 = 190

    	DWDM with 1539.77nm optics

    .. data:: ETHERNET_40GBASE_DWDM_1538_98 = 191

    	DWDM with 1538.98nm optics

    .. data:: ETHERNET_40GBASE_DWDM_1538_19 = 192

    	DWDM with 1538.19nm optics

    .. data:: ETHERNET_40GBASE_DWDM_1537_40 = 193

    	DWDM with 1537.40nm optics

    .. data:: ETHERNET_40GBASE_DWDM_1536_61 = 194

    	DWDM with 1536.61nm optics

    .. data:: ETHERNET_40GBASE_DWDM_1535_82 = 195

    	DWDM with 1535.82nm optics

    .. data:: ETHERNET_40GBASE_DWDM_1535_04 = 196

    	DWDM with 1535.04nm optics

    .. data:: ETHERNET_40GBASE_DWDM_1534_25 = 197

    	DWDM with 1534.25nm optics

    .. data:: ETHERNET_40GBASE_DWDM_1533_47 = 198

    	DWDM with 1533.47nm optics

    .. data:: ETHERNET_40GBASE_DWDM_1532_68 = 199

    	DWDM with 1532.68nm optics

    .. data:: ETHERNET_40GBASE_DWDM_1531_90 = 200

    	DWDM with 1531.90nm optics

    .. data:: ETHERNET_40GBASE_DWDM_1531_12 = 201

    	DWDM with 1531.12nm optics

    .. data:: ETHERNET_40GBASE_DWDM_1530_33 = 202

    	DWDM with 1530.33nm optics

    .. data:: ETHERNET_40GBASE_DWDM_TUNABLE = 203

    	DWDM with tunable optics

    .. data:: ETHERNET_100GBASE_DWDM_1561_42 = 204

    	DWDM with 1561.42nm optics

    .. data:: ETHERNET_100GBASE_DWDM_1560_61 = 205

    	DWDM with 1560.61nm optics

    .. data:: ETHERNET_100GBASE_DWDM_1559_79 = 206

    	DWDM with 1559.79nm optics

    .. data:: ETHERNET_100GBASE_DWDM_1558_98 = 207

    	DWDM with 1558.98nm optics

    .. data:: ETHERNET_100GBASE_DWDM_1558_17 = 208

    	DWDM with 1558.17nm optics

    .. data:: ETHERNET_100GBASE_DWDM_1557_36 = 209

    	DWDM with 1557.36nm optics

    .. data:: ETHERNET_100GBASE_DWDM_1556_55 = 210

    	DWDM with 1556.55nm optics

    .. data:: ETHERNET_100GBASE_DWDM_1555_75 = 211

    	DWDM with 1555.75nm optics

    .. data:: ETHERNET_100GBASE_DWDM_1554_94 = 212

    	DWDM with 1554.94nm optics

    .. data:: ETHERNET_100GBASE_DWDM_1554_13 = 213

    	DWDM with 1554.13nm optics

    .. data:: ETHERNET_100GBASE_DWDM_1553_33 = 214

    	DWDM with 1553.33nm optics

    .. data:: ETHERNET_100GBASE_DWDM_1552_52 = 215

    	DWDM with 1552.52nm optics

    .. data:: ETHERNET_100GBASE_DWDM_1551_72 = 216

    	DWDM with 1551.72nm optics

    .. data:: ETHERNET_100GBASE_DWDM_1550_92 = 217

    	DWDM with 1550.92nm optics

    .. data:: ETHERNET_100GBASE_DWDM_1550_12 = 218

    	DWDM with 1550.12nm optics

    .. data:: ETHERNET_100GBASE_DWDM_1549_32 = 219

    	DWDM with 1549.32nm optics

    .. data:: ETHERNET_100GBASE_DWDM_1548_51 = 220

    	DWDM with 1548.51nm optics

    .. data:: ETHERNET_100GBASE_DWDM_1547_72 = 221

    	DWDM with 1547.72nm optics

    .. data:: ETHERNET_100GBASE_DWDM_1546_92 = 222

    	DWDM with 1546.92nm optics

    .. data:: ETHERNET_100GBASE_DWDM_1546_12 = 223

    	DWDM with 1546.12nm optics

    .. data:: ETHERNET_100GBASE_DWDM_1545_32 = 224

    	DWDM with 1545.32nm optics

    .. data:: ETHERNET_100GBASE_DWDM_1544_53 = 225

    	DWDM with 1544.53nm optics

    .. data:: ETHERNET_100GBASE_DWDM_1543_73 = 226

    	DWDM with 1543.73nm optics

    .. data:: ETHERNET_100GBASE_DWDM_1542_94 = 227

    	DWDM with 1542.94nm optics

    .. data:: ETHERNET_100GBASE_DWDM_1542_14 = 228

    	DWDM with 1542.14nm optics

    .. data:: ETHERNET_100GBASE_DWDM_1541_35 = 229

    	DWDM with 1541.35nm optics

    .. data:: ETHERNET_100GBASE_DWDM_1540_56 = 230

    	DWDM with 1540.56nm optics

    .. data:: ETHERNET_100GBASE_DWDM_1539_77 = 231

    	DWDM with 1539.77nm optics

    .. data:: ETHERNET_100GBASE_DWDM_1538_98 = 232

    	DWDM with 1538.98nm optics

    .. data:: ETHERNET_100GBASE_DWDM_1538_19 = 233

    	DWDM with 1538.19nm optics

    .. data:: ETHERNET_100GBASE_DWDM_1537_40 = 234

    	DWDM with 1537.40nm optics

    .. data:: ETHERNET_100GBASE_DWDM_1536_61 = 235

    	DWDM with 1536.61nm optics

    .. data:: ETHERNET_100GBASE_DWDM_1535_82 = 236

    	DWDM with 1535.82nm optics

    .. data:: ETHERNET_100GBASE_DWDM_1535_04 = 237

    	DWDM with 1535.04nm optics

    .. data:: ETHERNET_100GBASE_DWDM_1534_25 = 238

    	DWDM with 1534.25nm optics

    .. data:: ETHERNET_100GBASE_DWDM_1533_47 = 239

    	DWDM with 1533.47nm optics

    .. data:: ETHERNET_100GBASE_DWDM_1532_68 = 240

    	DWDM with 1532.68nm optics

    .. data:: ETHERNET_100GBASE_DWDM_1531_90 = 241

    	DWDM with 1531.90nm optics

    .. data:: ETHERNET_100GBASE_DWDM_1531_12 = 242

    	DWDM with 1531.12nm optics

    .. data:: ETHERNET_100GBASE_DWDM_1530_33 = 243

    	DWDM with 1530.33nm optics

    .. data:: ETHERNET_100GBASE_DWDM_TUNABLE = 244

    	DWDM with tunable optics

    .. data:: ETHERNET_40GBASE_KR4 = 245

    	4 lane copper (backplane)

    .. data:: ETHERNET_40GBASE_CR4 = 246

    	4 lane copper (very short reach)

    .. data:: ETHERNET_40GBASE_SR4 = 247

    	fiber over 4 lane optics (short reach)

    .. data:: ETHERNET_40GBASE_FR = 248

    	serial fiber (2+ km)

    .. data:: ETHERNET_100GBASE_CR10 = 249

    	10 lane copper (very short reach)

    .. data:: ETHERNET_100GBASE_SR10 = 250

    	MMF fiber over 10 lane optics (short reach)

    .. data:: ETHERNET_40GBASE_CSR4 = 251

    	fiber over 4 lane optics (extended short reach)

    .. data:: ETHERNET_10GBASE_CWDM = 252

    	CWDM optics

    .. data:: ETHERNET_10GBASE_CWDM_TUNABLE = 253

    	CWDM with tunable optics

    .. data:: ETHERNET_10GBASE_CWDM_1470 = 254

    	CWDM with 1470nm optics

    .. data:: ETHERNET_10GBASE_CWDM_1490 = 255

    	CWDM with 1490nm optics

    .. data:: ETHERNET_10GBASE_CWDM_1510 = 256

    	CWDM with 1510nm optics

    .. data:: ETHERNET_10GBASE_CWDM_1530 = 257

    	CWDM with 1530nm optics

    .. data:: ETHERNET_10GBASE_CWDM_1550 = 258

    	CWDM with 1550nm optics

    .. data:: ETHERNET_10GBASE_CWDM_1570 = 259

    	CWDM with 1570nm optics

    .. data:: ETHERNET_10GBASE_CWDM_1590 = 260

    	CWDM with 1590nm optics

    .. data:: ETHERNET_10GBASE_CWDM_1610 = 261

    	CWDM with 1610nm optics

    .. data:: ETHERNET_40GBASE_CWDM = 262

    	CWDM optics

    .. data:: ETHERNET_40GBASE_CWDM_TUNABLE = 263

    	CWDM with tunable optics

    .. data:: ETHERNET_40GBASE_CWDM_1470 = 264

    	CWDM with 1470nm optics

    .. data:: ETHERNET_40GBASE_CWDM_1490 = 265

    	CWDM with 1490nm optics

    .. data:: ETHERNET_40GBASE_CWDM_1510 = 266

    	CWDM with 1510nm optics

    .. data:: ETHERNET_40GBASE_CWDM_1530 = 267

    	CWDM with 1530nm optics

    .. data:: ETHERNET_40GBASE_CWDM_1550 = 268

    	CWDM with 1550nm optics

    .. data:: ETHERNET_40GBASE_CWDM_1570 = 269

    	CWDM with 1570nm optics

    .. data:: ETHERNET_40GBASE_CWDM_1590 = 270

    	CWDM with 1590nm optics

    .. data:: ETHERNET_40GBASE_CWDM_1610 = 271

    	CWDM with 1610nm optics

    .. data:: ETHERNET_100GBASE_CWDM = 272

    	CWDM optics

    .. data:: ETHERNET_100GBASE_CWDM_TUNABLE = 273

    	CWDM with tunable optics

    .. data:: ETHERNET_100GBASE_CWDM_1470 = 274

    	CWDM with 1470nm optics

    .. data:: ETHERNET_100GBASE_CWDM_1490 = 275

    	CWDM with 1490nm optics

    .. data:: ETHERNET_100GBASE_CWDM_1510 = 276

    	CWDM with 1510nm optics

    .. data:: ETHERNET_100GBASE_CWDM_1530 = 277

    	CWDM with 1530nm optics

    .. data:: ETHERNET_100GBASE_CWDM_1550 = 278

    	CWDM with 1550nm optics

    .. data:: ETHERNET_100GBASE_CWDM_1570 = 279

    	CWDM with 1570nm optics

    .. data:: ETHERNET_100GBASE_CWDM_1590 = 280

    	CWDM with 1590nm optics

    .. data:: ETHERNET_100GBASE_CWDM_1610 = 281

    	CWDM with 1610nm optics

    .. data:: ETHERNET_40GBASE_ELPB = 282

    	Electrical loopback

    .. data:: ETHERNET_100GBASE_ELPB = 283

    	Electrical loopback

    .. data:: ETHERNET_100GBASE_LR10 = 284

    	Fiber over 10 lane optics (long reach)

    .. data:: ETHERNET_40GBASE = 285

    	Four-pair Category 8 STP

    .. data:: ETHERNET_100GBASE_KP4 = 286

    	4 lane copper (backplane)

    .. data:: ETHERNET_100GBASE_KR4 = 287

    	Improved 4 lane copper (backplane)

    .. data:: ETHERNET_10GBASE_LRM = 288

    	Multimode fiber with 1310nm optics (long reach)

    .. data:: ETHERNET_10GBASE_CX4 = 289

    	4 lane X copper

    .. data:: ETHERNET_10GBASE = 290

    	Four-pair Category 6+ UTP

    .. data:: ETHERNET_10GBASE_KX4 = 291

    	4 lane X copper (backplane)

    .. data:: ETHERNET_10GBASE_KR = 292

    	Copper (backplane)

    .. data:: ETHERNET_10GBASE_PR = 293

    	Passive optical network

    .. data:: ETHERNET_100BASE_LX = 294

    	X fiber over 4 lane 1310nm optics

    .. data:: ETHERNET_100BASE_ZX = 295

    	Single-mode fiber over 1550nm optics (Cisco)

    .. data:: ETHERNET_1000BASE_BX_D = 296

    	X fibre (D)

    .. data:: ETHERNET_1000BASE_BX_U = 297

    	X fibre (U)

    .. data:: ETHERNET_1000BASE_BX20_D = 298

    	X fibre (D, 20km)

    .. data:: ETHERNET_1000BASE_BX20_U = 299

    	X fibre (U, 20km)

    .. data:: ETHERNET_1000BASE_BX40_D = 300

    	X fibre (D, 40km)

    .. data:: ETHERNET_1000BASE_BX40_DA = 301

    	X fibre (D, 40km)

    .. data:: ETHERNET_1000BASE_BX40_U = 302

    	X fibre (U, 40km)

    .. data:: ETHERNET_1000BASE_BX80_D = 303

    	X fibre (D, 80km)

    .. data:: ETHERNET_1000BASE_BX80_U = 304

    	X fibre (U, 80km)

    .. data:: ETHERNET_1000BASE_BX120_D = 305

    	X fibre (D, 120km)

    .. data:: ETHERNET_1000BASE_BX120_U = 306

    	X fibre (U, 120km)

    .. data:: ETHERNET_10GBASE_BX_D = 307

    	X fibre (D)

    .. data:: ETHERNET_10GBASE_BX_U = 308

    	X fibre (U)

    .. data:: ETHERNET_10GBASE_BX10_D = 309

    	X fibre (D, 10km)

    .. data:: ETHERNET_10GBASE_BX10_U = 310

    	X fibre (U, 10km)

    .. data:: ETHERNET_10GBASE_BX20_D = 311

    	X fibre (D, 20km)

    .. data:: ETHERNET_10GBASE_BX20_U = 312

    	X fibre (U, 20km)

    .. data:: ETHERNET_10GBASE_BX40_D = 313

    	X fibre (D, 40km)

    .. data:: ETHERNET_10GBASE_BX40_U = 314

    	X fibre (U, 40km)

    .. data:: ETHERNET_10GBASE_BX80_D = 315

    	X fibre (D, 80km)

    .. data:: ETHERNET_10GBASE_BX80_U = 316

    	X fibre (U, 80km)

    .. data:: ETHERNET_10GBASE_BX120_D = 317

    	X fibre (D, 120km)

    .. data:: ETHERNET_10GBASE_BX120_U = 318

    	X fibre (U, 120km)

    .. data:: ETHERNET_1000BASE_DR_LX = 319

    	X fiber over long-wl laser PMD, duplexity

    	unknown, dual rate

    .. data:: ETHERNET_100GBASE_ER4L = 320

    	fiber over 4 lane optics (25km reach)

    .. data:: ETHERNET_100GBASE_SR4 = 321

    	fiber over 4 lane optics (short reach)

    .. data:: ETHERNET_40GBASE_SR_BD = 322

    	Bi-directional fiber over 2 lane optics (short

    	reach)

    .. data:: ETHERNET_BASE_MAX = 323

    	ethernet base max

    """

    ETHERNET_OTHER = 0

    ETHERNET_UNKNOWN = 1

    ETHERNET_AUI = 2

    ETHERNET_10BASE5 = 3

    ETHERNET_FOIRL = 4

    ETHERNET_10BASE2 = 5

    ETHERNET_10BROAD36 = 6

    ETHERNET_10BASE = 7

    ETHERNET_10BASE_THD = 8

    ETHERNET_10BASE_TFD = 9

    ETHERNET_10BASE_FP = 10

    ETHERNET_10BASE_FB = 11

    ETHERNET_10BASE_FL = 12

    ETHERNET_10BASE_FLHD = 13

    ETHERNET_10BASE_FLFD = 14

    ETHERNET_100BASE_T4 = 15

    ETHERNET_100BASE_TX = 16

    ETHERNET_100BASE_TXHD = 17

    ETHERNET_100BASE_TXFD = 18

    ETHERNET_100BASE_FX = 19

    ETHERNET_100BASE_FXHD = 20

    ETHERNET_100BASE_FXFD = 21

    ETHERNET_100BASE_EX = 22

    ETHERNET_100BASE_EXHD = 23

    ETHERNET_100BASE_EXFD = 24

    ETHERNET_100BASE_T2 = 25

    ETHERNET_100BASE_T2HD = 26

    ETHERNET_100BASE_T2FD = 27

    ETHERNET_1000BASE_X = 28

    ETHERNET_1000BASE_XHD = 29

    ETHERNET_1000BASE_XFD = 30

    ETHERNET_1000BASE_LX = 31

    ETHERNET_1000BASE_LXHD = 32

    ETHERNET_1000BASE_LXFD = 33

    ETHERNET_1000BASE_SX = 34

    ETHERNET_1000BASE_SXHD = 35

    ETHERNET_1000BASE_SXFD = 36

    ETHERNET_1000BASE_CX = 37

    ETHERNET_1000BASE_CXHD = 38

    ETHERNET_1000BASE_CXFD = 39

    ETHERNET_1000BASE = 40

    ETHERNET_1000BASE_THD = 41

    ETHERNET_1000BASE_TFD = 42

    ETHERNET_10GBASE_X = 43

    ETHERNET_10GBASE_LX4 = 44

    ETHERNET_10GBASE_R = 45

    ETHERNET_10GBASE_ER = 46

    ETHERNET_10GBASE_LR = 47

    ETHERNET_10GBASE_SR = 48

    ETHERNET_10GBASE_W = 49

    ETHERNET_10GBASE_EW = 50

    ETHERNET_10GBASE_LW = 51

    ETHERNET_10GBASE_SW = 52

    ETHERNET_1000BASE_ZX = 53

    ETHERNET_1000BASE_CWDM = 54

    ETHERNET_1000BASE_CWDM_1470 = 55

    ETHERNET_1000BASE_CWDM_1490 = 56

    ETHERNET_1000BASE_CWDM_1510 = 57

    ETHERNET_1000BASE_CWDM_1530 = 58

    ETHERNET_1000BASE_CWDM_1550 = 59

    ETHERNET_1000BASE_CWDM_1570 = 60

    ETHERNET_1000BASE_CWDM_1590 = 61

    ETHERNET_1000BASE_CWDM_1610 = 62

    ETHERNET_10GBASE_ZR = 63

    ETHERNET_10GBASE_DWDM = 64

    ETHERNET_100GBASE_LR4 = 65

    ETHERNET_1000BASE_DWDM = 66

    ETHERNET_1000BASE_DWDM_1533 = 67

    ETHERNET_1000BASE_DWDM_1537 = 68

    ETHERNET_1000BASE_DWDM_1541 = 69

    ETHERNET_1000BASE_DWDM_1545 = 70

    ETHERNET_1000BASE_DWDM_1549 = 71

    ETHERNET_1000BASE_DWDM_1553 = 72

    ETHERNET_1000BASE_DWDM_1557 = 73

    ETHERNET_1000BASE_DWDM_1561 = 74

    ETHERNET_40GBASE_LR4 = 75

    ETHERNET_40GBASE_ER4 = 76

    ETHERNET_100GBASE_ER4 = 77

    ETHERNET_1000BASE_EX = 78

    ETHERNET_1000BASE_BX10_D = 79

    ETHERNET_1000BASE_BX10_U = 80

    ETHERNET_1000BASE_DWDM_1561_42 = 81

    ETHERNET_1000BASE_DWDM_1560_61 = 82

    ETHERNET_1000BASE_DWDM_1559_79 = 83

    ETHERNET_1000BASE_DWDM_1558_98 = 84

    ETHERNET_1000BASE_DWDM_1558_17 = 85

    ETHERNET_1000BASE_DWDM_1557_36 = 86

    ETHERNET_1000BASE_DWDM_1556_55 = 87

    ETHERNET_1000BASE_DWDM_1555_75 = 88

    ETHERNET_1000BASE_DWDM_1554_94 = 89

    ETHERNET_1000BASE_DWDM_1554_13 = 90

    ETHERNET_1000BASE_DWDM_1553_33 = 91

    ETHERNET_1000BASE_DWDM_1552_52 = 92

    ETHERNET_1000BASE_DWDM_1551_72 = 93

    ETHERNET_1000BASE_DWDM_1550_92 = 94

    ETHERNET_1000BASE_DWDM_1550_12 = 95

    ETHERNET_1000BASE_DWDM_1549_32 = 96

    ETHERNET_1000BASE_DWDM_1548_51 = 97

    ETHERNET_1000BASE_DWDM_1547_72 = 98

    ETHERNET_1000BASE_DWDM_1546_92 = 99

    ETHERNET_1000BASE_DWDM_1546_12 = 100

    ETHERNET_1000BASE_DWDM_1545_32 = 101

    ETHERNET_1000BASE_DWDM_1544_53 = 102

    ETHERNET_1000BASE_DWDM_1543_73 = 103

    ETHERNET_1000BASE_DWDM_1542_94 = 104

    ETHERNET_1000BASE_DWDM_1542_14 = 105

    ETHERNET_1000BASE_DWDM_1541_35 = 106

    ETHERNET_1000BASE_DWDM_1540_56 = 107

    ETHERNET_1000BASE_DWDM_1539_77 = 108

    ETHERNET_1000BASE_DWDM_1538_98 = 109

    ETHERNET_1000BASE_DWDM_1538_19 = 110

    ETHERNET_1000BASE_DWDM_1537_40 = 111

    ETHERNET_1000BASE_DWDM_1536_61 = 112

    ETHERNET_1000BASE_DWDM_1535_82 = 113

    ETHERNET_1000BASE_DWDM_1535_04 = 114

    ETHERNET_1000BASE_DWDM_1534_25 = 115

    ETHERNET_1000BASE_DWDM_1533_47 = 116

    ETHERNET_1000BASE_DWDM_1532_68 = 117

    ETHERNET_1000BASE_DWDM_1531_90 = 118

    ETHERNET_1000BASE_DWDM_1531_12 = 119

    ETHERNET_1000BASE_DWDM_1530_33 = 120

    ETHERNET_1000BASE_DWDM_TUNABLE = 121

    ETHERNET_10GBASE_DWDM_1561_42 = 122

    ETHERNET_10GBASE_DWDM_1560_61 = 123

    ETHERNET_10GBASE_DWDM_1559_79 = 124

    ETHERNET_10GBASE_DWDM_1558_98 = 125

    ETHERNET_10GBASE_DWDM_1558_17 = 126

    ETHERNET_10GBASE_DWDM_1557_36 = 127

    ETHERNET_10GBASE_DWDM_1556_55 = 128

    ETHERNET_10GBASE_DWDM_1555_75 = 129

    ETHERNET_10GBASE_DWDM_1554_94 = 130

    ETHERNET_10GBASE_DWDM_1554_13 = 131

    ETHERNET_10GBASE_DWDM_1553_33 = 132

    ETHERNET_10GBASE_DWDM_1552_52 = 133

    ETHERNET_10GBASE_DWDM_1551_72 = 134

    ETHERNET_10GBASE_DWDM_1550_92 = 135

    ETHERNET_10GBASE_DWDM_1550_12 = 136

    ETHERNET_10GBASE_DWDM_1549_32 = 137

    ETHERNET_10GBASE_DWDM_1548_51 = 138

    ETHERNET_10GBASE_DWDM_1547_72 = 139

    ETHERNET_10GBASE_DWDM_1546_92 = 140

    ETHERNET_10GBASE_DWDM_1546_12 = 141

    ETHERNET_10GBASE_DWDM_1545_32 = 142

    ETHERNET_10GBASE_DWDM_1544_53 = 143

    ETHERNET_10GBASE_DWDM_1543_73 = 144

    ETHERNET_10GBASE_DWDM_1542_94 = 145

    ETHERNET_10GBASE_DWDM_1542_14 = 146

    ETHERNET_10GBASE_DWDM_1541_35 = 147

    ETHERNET_10GBASE_DWDM_1540_56 = 148

    ETHERNET_10GBASE_DWDM_1539_77 = 149

    ETHERNET_10GBASE_DWDM_1538_98 = 150

    ETHERNET_10GBASE_DWDM_1538_19 = 151

    ETHERNET_10GBASE_DWDM_1537_40 = 152

    ETHERNET_10GBASE_DWDM_1536_61 = 153

    ETHERNET_10GBASE_DWDM_1535_82 = 154

    ETHERNET_10GBASE_DWDM_1535_04 = 155

    ETHERNET_10GBASE_DWDM_1534_25 = 156

    ETHERNET_10GBASE_DWDM_1533_47 = 157

    ETHERNET_10GBASE_DWDM_1532_68 = 158

    ETHERNET_10GBASE_DWDM_1531_90 = 159

    ETHERNET_10GBASE_DWDM_1531_12 = 160

    ETHERNET_10GBASE_DWDM_1530_33 = 161

    ETHERNET_10GBASE_DWDM_TUNABLE = 162

    ETHERNET_40GBASE_DWDM_1561_42 = 163

    ETHERNET_40GBASE_DWDM_1560_61 = 164

    ETHERNET_40GBASE_DWDM_1559_79 = 165

    ETHERNET_40GBASE_DWDM_1558_98 = 166

    ETHERNET_40GBASE_DWDM_1558_17 = 167

    ETHERNET_40GBASE_DWDM_1557_36 = 168

    ETHERNET_40GBASE_DWDM_1556_55 = 169

    ETHERNET_40GBASE_DWDM_1555_75 = 170

    ETHERNET_40GBASE_DWDM_1554_94 = 171

    ETHERNET_40GBASE_DWDM_1554_13 = 172

    ETHERNET_40GBASE_DWDM_1553_33 = 173

    ETHERNET_40GBASE_DWDM_1552_52 = 174

    ETHERNET_40GBASE_DWDM_1551_72 = 175

    ETHERNET_40GBASE_DWDM_1550_92 = 176

    ETHERNET_40GBASE_DWDM_1550_12 = 177

    ETHERNET_40GBASE_DWDM_1549_32 = 178

    ETHERNET_40GBASE_DWDM_1548_51 = 179

    ETHERNET_40GBASE_DWDM_1547_72 = 180

    ETHERNET_40GBASE_DWDM_1546_92 = 181

    ETHERNET_40GBASE_DWDM_1546_12 = 182

    ETHERNET_40GBASE_DWDM_1545_32 = 183

    ETHERNET_40GBASE_DWDM_1544_53 = 184

    ETHERNET_40GBASE_DWDM_1543_73 = 185

    ETHERNET_40GBASE_DWDM_1542_94 = 186

    ETHERNET_40GBASE_DWDM_1542_14 = 187

    ETHERNET_40GBASE_DWDM_1541_35 = 188

    ETHERNET_40GBASE_DWDM_1540_56 = 189

    ETHERNET_40GBASE_DWDM_1539_77 = 190

    ETHERNET_40GBASE_DWDM_1538_98 = 191

    ETHERNET_40GBASE_DWDM_1538_19 = 192

    ETHERNET_40GBASE_DWDM_1537_40 = 193

    ETHERNET_40GBASE_DWDM_1536_61 = 194

    ETHERNET_40GBASE_DWDM_1535_82 = 195

    ETHERNET_40GBASE_DWDM_1535_04 = 196

    ETHERNET_40GBASE_DWDM_1534_25 = 197

    ETHERNET_40GBASE_DWDM_1533_47 = 198

    ETHERNET_40GBASE_DWDM_1532_68 = 199

    ETHERNET_40GBASE_DWDM_1531_90 = 200

    ETHERNET_40GBASE_DWDM_1531_12 = 201

    ETHERNET_40GBASE_DWDM_1530_33 = 202

    ETHERNET_40GBASE_DWDM_TUNABLE = 203

    ETHERNET_100GBASE_DWDM_1561_42 = 204

    ETHERNET_100GBASE_DWDM_1560_61 = 205

    ETHERNET_100GBASE_DWDM_1559_79 = 206

    ETHERNET_100GBASE_DWDM_1558_98 = 207

    ETHERNET_100GBASE_DWDM_1558_17 = 208

    ETHERNET_100GBASE_DWDM_1557_36 = 209

    ETHERNET_100GBASE_DWDM_1556_55 = 210

    ETHERNET_100GBASE_DWDM_1555_75 = 211

    ETHERNET_100GBASE_DWDM_1554_94 = 212

    ETHERNET_100GBASE_DWDM_1554_13 = 213

    ETHERNET_100GBASE_DWDM_1553_33 = 214

    ETHERNET_100GBASE_DWDM_1552_52 = 215

    ETHERNET_100GBASE_DWDM_1551_72 = 216

    ETHERNET_100GBASE_DWDM_1550_92 = 217

    ETHERNET_100GBASE_DWDM_1550_12 = 218

    ETHERNET_100GBASE_DWDM_1549_32 = 219

    ETHERNET_100GBASE_DWDM_1548_51 = 220

    ETHERNET_100GBASE_DWDM_1547_72 = 221

    ETHERNET_100GBASE_DWDM_1546_92 = 222

    ETHERNET_100GBASE_DWDM_1546_12 = 223

    ETHERNET_100GBASE_DWDM_1545_32 = 224

    ETHERNET_100GBASE_DWDM_1544_53 = 225

    ETHERNET_100GBASE_DWDM_1543_73 = 226

    ETHERNET_100GBASE_DWDM_1542_94 = 227

    ETHERNET_100GBASE_DWDM_1542_14 = 228

    ETHERNET_100GBASE_DWDM_1541_35 = 229

    ETHERNET_100GBASE_DWDM_1540_56 = 230

    ETHERNET_100GBASE_DWDM_1539_77 = 231

    ETHERNET_100GBASE_DWDM_1538_98 = 232

    ETHERNET_100GBASE_DWDM_1538_19 = 233

    ETHERNET_100GBASE_DWDM_1537_40 = 234

    ETHERNET_100GBASE_DWDM_1536_61 = 235

    ETHERNET_100GBASE_DWDM_1535_82 = 236

    ETHERNET_100GBASE_DWDM_1535_04 = 237

    ETHERNET_100GBASE_DWDM_1534_25 = 238

    ETHERNET_100GBASE_DWDM_1533_47 = 239

    ETHERNET_100GBASE_DWDM_1532_68 = 240

    ETHERNET_100GBASE_DWDM_1531_90 = 241

    ETHERNET_100GBASE_DWDM_1531_12 = 242

    ETHERNET_100GBASE_DWDM_1530_33 = 243

    ETHERNET_100GBASE_DWDM_TUNABLE = 244

    ETHERNET_40GBASE_KR4 = 245

    ETHERNET_40GBASE_CR4 = 246

    ETHERNET_40GBASE_SR4 = 247

    ETHERNET_40GBASE_FR = 248

    ETHERNET_100GBASE_CR10 = 249

    ETHERNET_100GBASE_SR10 = 250

    ETHERNET_40GBASE_CSR4 = 251

    ETHERNET_10GBASE_CWDM = 252

    ETHERNET_10GBASE_CWDM_TUNABLE = 253

    ETHERNET_10GBASE_CWDM_1470 = 254

    ETHERNET_10GBASE_CWDM_1490 = 255

    ETHERNET_10GBASE_CWDM_1510 = 256

    ETHERNET_10GBASE_CWDM_1530 = 257

    ETHERNET_10GBASE_CWDM_1550 = 258

    ETHERNET_10GBASE_CWDM_1570 = 259

    ETHERNET_10GBASE_CWDM_1590 = 260

    ETHERNET_10GBASE_CWDM_1610 = 261

    ETHERNET_40GBASE_CWDM = 262

    ETHERNET_40GBASE_CWDM_TUNABLE = 263

    ETHERNET_40GBASE_CWDM_1470 = 264

    ETHERNET_40GBASE_CWDM_1490 = 265

    ETHERNET_40GBASE_CWDM_1510 = 266

    ETHERNET_40GBASE_CWDM_1530 = 267

    ETHERNET_40GBASE_CWDM_1550 = 268

    ETHERNET_40GBASE_CWDM_1570 = 269

    ETHERNET_40GBASE_CWDM_1590 = 270

    ETHERNET_40GBASE_CWDM_1610 = 271

    ETHERNET_100GBASE_CWDM = 272

    ETHERNET_100GBASE_CWDM_TUNABLE = 273

    ETHERNET_100GBASE_CWDM_1470 = 274

    ETHERNET_100GBASE_CWDM_1490 = 275

    ETHERNET_100GBASE_CWDM_1510 = 276

    ETHERNET_100GBASE_CWDM_1530 = 277

    ETHERNET_100GBASE_CWDM_1550 = 278

    ETHERNET_100GBASE_CWDM_1570 = 279

    ETHERNET_100GBASE_CWDM_1590 = 280

    ETHERNET_100GBASE_CWDM_1610 = 281

    ETHERNET_40GBASE_ELPB = 282

    ETHERNET_100GBASE_ELPB = 283

    ETHERNET_100GBASE_LR10 = 284

    ETHERNET_40GBASE = 285

    ETHERNET_100GBASE_KP4 = 286

    ETHERNET_100GBASE_KR4 = 287

    ETHERNET_10GBASE_LRM = 288

    ETHERNET_10GBASE_CX4 = 289

    ETHERNET_10GBASE = 290

    ETHERNET_10GBASE_KX4 = 291

    ETHERNET_10GBASE_KR = 292

    ETHERNET_10GBASE_PR = 293

    ETHERNET_100BASE_LX = 294

    ETHERNET_100BASE_ZX = 295

    ETHERNET_1000BASE_BX_D = 296

    ETHERNET_1000BASE_BX_U = 297

    ETHERNET_1000BASE_BX20_D = 298

    ETHERNET_1000BASE_BX20_U = 299

    ETHERNET_1000BASE_BX40_D = 300

    ETHERNET_1000BASE_BX40_DA = 301

    ETHERNET_1000BASE_BX40_U = 302

    ETHERNET_1000BASE_BX80_D = 303

    ETHERNET_1000BASE_BX80_U = 304

    ETHERNET_1000BASE_BX120_D = 305

    ETHERNET_1000BASE_BX120_U = 306

    ETHERNET_10GBASE_BX_D = 307

    ETHERNET_10GBASE_BX_U = 308

    ETHERNET_10GBASE_BX10_D = 309

    ETHERNET_10GBASE_BX10_U = 310

    ETHERNET_10GBASE_BX20_D = 311

    ETHERNET_10GBASE_BX20_U = 312

    ETHERNET_10GBASE_BX40_D = 313

    ETHERNET_10GBASE_BX40_U = 314

    ETHERNET_10GBASE_BX80_D = 315

    ETHERNET_10GBASE_BX80_U = 316

    ETHERNET_10GBASE_BX120_D = 317

    ETHERNET_10GBASE_BX120_U = 318

    ETHERNET_1000BASE_DR_LX = 319

    ETHERNET_100GBASE_ER4L = 320

    ETHERNET_100GBASE_SR4 = 321

    ETHERNET_40GBASE_SR_BD = 322

    ETHERNET_BASE_MAX = 323


    @staticmethod
    def _meta_info():
        from ydk.models.drivers._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
        return meta._meta_table['EthernetMediaEnum']


class EthernetPortEnableEnum(Enum):
    """
    EthernetPortEnableEnum

    Port admin state

    .. data:: DISABLED = 0

    	Port disabled, both directions

    .. data:: RX_ENABLED = 1

    	Port enabled rx direction only

    .. data:: TX_ENABLED = 2

    	Port enabled tx direction only

    .. data:: ENABLED = 3

    	Port enabled, both directions

    """

    DISABLED = 0

    RX_ENABLED = 1

    TX_ENABLED = 2

    ENABLED = 3


    @staticmethod
    def _meta_info():
        from ydk.models.drivers._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
        return meta._meta_table['EthernetPortEnableEnum']


class EthernetSpeedEnum(Enum):
    """
    EthernetSpeedEnum

    Speed

    .. data:: ETHERNET_SPEED_INVALID = 0

    	ethernet speed invalid

    .. data:: TEN_MBPS = 1

    	ten mbps

    .. data:: HUNDRED_MBPS = 2

    	hundred mbps

    .. data:: ONE_GBPS = 3

    	one gbps

    .. data:: TEN_GBPS = 4

    	ten gbps

    .. data:: FORTY_GBPS = 5

    	forty gbps

    .. data:: HUNDRED_GBPS = 6

    	hundred gbps

    .. data:: ETHERNET_SPEED_TYPES_COUNT = 7

    	ethernet speed types count

    """

    ETHERNET_SPEED_INVALID = 0

    TEN_MBPS = 1

    HUNDRED_MBPS = 2

    ONE_GBPS = 3

    TEN_GBPS = 4

    FORTY_GBPS = 5

    HUNDRED_GBPS = 6

    ETHERNET_SPEED_TYPES_COUNT = 7


    @staticmethod
    def _meta_info():
        from ydk.models.drivers._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
        return meta._meta_table['EthernetSpeedEnum']



class EthernetInterface(object):
    """
    Ethernet operational data
    
    .. attribute:: berts
    
    	Ethernet controller BERT table
    	**type**\: :py:class:`Berts <ydk.models.drivers.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Berts>`
    
    .. attribute:: interfaces
    
    	Ethernet controller info table
    	**type**\: :py:class:`Interfaces <ydk.models.drivers.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Interfaces>`
    
    .. attribute:: statistics
    
    	Ethernet controller statistics table
    	**type**\: :py:class:`Statistics <ydk.models.drivers.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Statistics>`
    
    

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
        	**type**\: list of :py:class:`Statistic <ydk.models.drivers.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Statistics.Statistic>`
        
        

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
            	**type**\: str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: aborted_packet_drops
            
            	Drops due to packet abort
            	**type**\: long
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: buffer_underrun_packet_drops
            
            	Drops due to buffer underrun
            	**type**\: long
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: dropped_ether_stats_fragments
            
            	Bad Frames < 64 Octet, dropped
            	**type**\: long
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: dropped_ether_stats_undersize_pkts
            
            	Good frames < 64 Octet, dropped
            	**type**\: long
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: dropped_giant_packets_greaterthan_mru
            
            	Good frames > MRU, dropped
            	**type**\: long
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: dropped_jabbers_packets_greaterthan_mru
            
            	Bad Frames > MRU, dropped
            	**type**\: long
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: dropped_miscellaneous_error_packets
            
            	Any other errors not counted
            	**type**\: long
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: dropped_packets_with_crc_align_errors
            
            	Frames 64 \- MRU with CRC error
            	**type**\: long
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ether_stats_collisions
            
            	All collision events
            	**type**\: long
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: invalid_dest_mac_drop_packets
            
            	Drops due to the destination MAC not matching
            	**type**\: long
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: invalid_encap_drop_packets
            
            	Drops due to the encapsulation or ether type not matching
            	**type**\: long
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: miscellaneous_output_errors
            
            	Any other errors not counted
            	**type**\: long
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: number_of_aborted_packets_dropped
            
            	Drops due to packet abort
            	**type**\: long
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: number_of_buffer_overrun_packets_dropped
            
            	Drops due to buffer overrun
            	**type**\: long
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: number_of_miscellaneous_packets_dropped
            
            	Any other drops not counted
            	**type**\: long
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: numberof_invalid_vlan_id_packets_dropped
            
            	Drops due to invalid VLAN id
            	**type**\: long
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: received8021q_frames
            
            	All 802.1Q frames
            	**type**\: long
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: received_broadcast_frames
            
            	Received broadcast Frames
            	**type**\: long
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: received_good_bytes
            
            	Total octets of all good frames
            	**type**\: long
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: received_good_frames
            
            	Received Good Frames
            	**type**\: long
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: received_multicast_frames
            
            	Received multicast Frames
            	**type**\: long
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: received_pause_frames
            
            	All pause frames
            	**type**\: long
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: received_total64_octet_frames
            
            	All 64 Octet Frame Count
            	**type**\: long
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: received_total_bytes
            
            	Total octets of all frames
            	**type**\: long
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: received_total_frames
            
            	All frames, good or bad
            	**type**\: long
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: received_total_octet_frames_from1024_to1518
            
            	All 1024\-1518 Octet Frame Count
            	**type**\: long
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: received_total_octet_frames_from128_to255
            
            	All 128\-255 Octet Frame Count
            	**type**\: long
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: received_total_octet_frames_from1519_to_max
            
            	All > 1518 Octet Frame Count
            	**type**\: long
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: received_total_octet_frames_from256_to511
            
            	All 256\-511 Octet Frame Count
            	**type**\: long
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: received_total_octet_frames_from512_to1023
            
            	All 512\-1023 Octet Frame Count
            	**type**\: long
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: received_total_octet_frames_from65_to127
            
            	All 65\-127 Octet Frame Count
            	**type**\: long
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: received_unicast_frames
            
            	Received unicast Frames
            	**type**\: long
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: received_unknown_opcodes
            
            	Unsupported MAC Control frames
            	**type**\: long
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: rfc2819_ether_stats_crc_align_errors
            
            	RFC2819 etherStatsCRCAlignErrors
            	**type**\: long
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: rfc2819_ether_stats_jabbers
            
            	RFC2819 etherStatsJabbers
            	**type**\: long
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: rfc2819_ether_stats_oversized_pkts
            
            	RFC2819 etherStatsOversizedPkts
            	**type**\: long
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: rfc3635dot3_stats_alignment_errors
            
            	RFC3635 dot3StatsAlignmentErrors
            	**type**\: long
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: symbol_errors
            
            	Symbol errors
            	**type**\: long
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: total_bytes_transmitted
            
            	Total octets of all frames
            	**type**\: long
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: total_frames_transmitted
            
            	All frames, good or bad
            	**type**\: long
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: total_good_bytes_transmitted
            
            	Total octets of all good frames
            	**type**\: long
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: transmitted8021q_frames
            
            	All 802.1Q frames
            	**type**\: long
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: transmitted_broadcast_frames
            
            	Transmitted broadcast Frames
            	**type**\: long
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: transmitted_good_frames
            
            	Transmitted Good Frames
            	**type**\: long
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: transmitted_multicast_frames
            
            	Transmitted multicast Frames
            	**type**\: long
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: transmitted_total64_octet_frames
            
            	All 64 Octet Frame Count
            	**type**\: long
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: transmitted_total_octet_frames_from1024_to1518
            
            	All 1024\-1518 Octet Frame Count
            	**type**\: long
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: transmitted_total_octet_frames_from128_to255
            
            	All 128\-255 Octet Frame Count
            	**type**\: long
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: transmitted_total_octet_frames_from1518_to_max
            
            	All > 1518 Octet Frame Count
            	**type**\: long
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: transmitted_total_octet_frames_from256_to511
            
            	All 256\-511 Octet Frame Count
            	**type**\: long
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: transmitted_total_octet_frames_from512_to1023
            
            	All 512\-1023 Octet Frame Count
            	**type**\: long
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: transmitted_total_octet_frames_from65_to127
            
            	All 65\-127 Octet Frame Count
            	**type**\: long
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: transmitted_total_pause_frames
            
            	All pause frames
            	**type**\: long
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: transmitted_unicast_frames
            
            	Transmitted unicast Frames
            	**type**\: long
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: uncounted_dropped_frames
            
            	Any other drops not counted
            	**type**\: long
            
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
                if not self.is_config():
                    return False
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
                from ydk.models.drivers._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
                return meta._meta_table['EthernetInterface.Statistics.Statistic']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-drivers-media-eth-oper:ethernet-interface/Cisco-IOS-XR-drivers-media-eth-oper:statistics'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.statistic is not None:
                for child_ref in self.statistic:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.drivers._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
            return meta._meta_table['EthernetInterface.Statistics']['meta_info']


    class Interfaces(object):
        """
        Ethernet controller info table
        
        .. attribute:: interface
        
        	Ethernet controller information
        	**type**\: list of :py:class:`Interface <ydk.models.drivers.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Interfaces.Interface>`
        
        

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
            	**type**\: str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: admin_state
            
            	Port Administrative State
            	**type**\: :py:class:`EthernetPortEnableEnum <ydk.models.drivers.Cisco_IOS_XR_drivers_media_eth_oper.EthernetPortEnableEnum>`
            
            .. attribute:: layer1_info
            
            	Layer 1 information
            	**type**\: :py:class:`Layer1Info <ydk.models.drivers.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Interfaces.Interface.Layer1Info>`
            
            .. attribute:: mac_info
            
            	MAC Layer information
            	**type**\: :py:class:`MacInfo <ydk.models.drivers.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Interfaces.Interface.MacInfo>`
            
            .. attribute:: oper_state_up
            
            	Port Operational state \- TRUE if up
            	**type**\: bool
            
            .. attribute:: phy_info
            
            	PHY information
            	**type**\: :py:class:`PhyInfo <ydk.models.drivers.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Interfaces.Interface.PhyInfo>`
            
            .. attribute:: transport_info
            
            	Transport state information
            	**type**\: :py:class:`TransportInfo <ydk.models.drivers.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Interfaces.Interface.TransportInfo>`
            
            

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
                	**type**\: :py:class:`FecDetails <ydk.models.drivers.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Interfaces.Interface.PhyInfo.FecDetails>`
                
                .. attribute:: loopback
                
                	Port operational loopback
                	**type**\: :py:class:`EthernetLoopbackEnum <ydk.models.drivers.Cisco_IOS_XR_drivers_media_eth_oper.EthernetLoopbackEnum>`
                
                .. attribute:: media_type
                
                	Port media type
                	**type**\: :py:class:`EthernetMediaEnum <ydk.models.drivers.Cisco_IOS_XR_drivers_media_eth_oper.EthernetMediaEnum>`
                
                .. attribute:: phy_details
                
                	Details about the PHY
                	**type**\: :py:class:`PhyDetails <ydk.models.drivers.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails>`
                
                .. attribute:: phy_present
                
                	Presence of PHY
                	**type**\: :py:class:`EtherPhyPresentEnum <ydk.models.drivers.Cisco_IOS_XR_drivers_media_eth_oper.EtherPhyPresentEnum>`
                
                

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
                    	**type**\: :py:class:`DigOptMonAlarmThresholds <ydk.models.drivers.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails.DigOptMonAlarmThresholds>`
                    
                    .. attribute:: dig_opt_mon_alarms
                    
                    	Digital Optical Monitoring alarms
                    	**type**\: :py:class:`DigOptMonAlarms <ydk.models.drivers.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails.DigOptMonAlarms>`
                    
                    .. attribute:: lane
                    
                    	Digital Optical Monitoring (per lane information)
                    	**type**\: list of :py:class:`Lane <ydk.models.drivers.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails.Lane>`
                    
                    .. attribute:: lane_field_validity
                    
                    	Digital Optical Monitoring (per lane information) validity
                    	**type**\: :py:class:`LaneFieldValidity <ydk.models.drivers.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails.LaneFieldValidity>`
                    
                    .. attribute:: optics_wavelength
                    
                    	Wavelength of the optics being used in nm \* 1000
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: transceiver_temperature
                    
                    	The temperature of the transceiver (mDegrees C)
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: transceiver_voltage
                    
                    	The input voltage to the transceiver (mV)
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: vendor
                    
                    	Name of the port optics manufacturer
                    	**type**\: str
                    
                    .. attribute:: vendor_part_number
                    
                    	Part number for the port optics
                    	**type**\: str
                    
                    .. attribute:: vendor_serial_number
                    
                    	Serial number for the port optics
                    	**type**\: str
                    
                    

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
                        self.transceiver_temperature = None
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
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: receive_power_valid
                        
                        	The receive power 'per lane' field is valid
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: transmit_power_valid
                        
                        	The transmit power 'per lane' field is valid
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: wavelength_valid
                        
                        	The wavelength 'per lane' field is valid
                        	**type**\: int
                        
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
                            if not self.is_config():
                                return False
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
                            from ydk.models.drivers._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
                            return meta._meta_table['EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails.LaneFieldValidity']['meta_info']


                    class DigOptMonAlarmThresholds(object):
                        """
                        Digital Optical Monitoring alarm thresholds
                        
                        .. attribute:: field_validity
                        
                        	Field validity
                        	**type**\: :py:class:`FieldValidity <ydk.models.drivers.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails.DigOptMonAlarmThresholds.FieldValidity>`
                        
                        .. attribute:: laser_bias_alarm_high
                        
                        	Laser bias high alarm threshold (mA)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: laser_bias_alarm_low
                        
                        	Laser bias low alarm threshold (mA)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: laser_bias_warning_high
                        
                        	Laser bias high warning threshold (mA)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: laser_bias_warning_low
                        
                        	Laser bias low warning threshold (mA)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: optical_receive_power_alarm_high
                        
                        	High optical receive power alarm threshold (mW)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: optical_receive_power_alarm_low
                        
                        	Low optical receive power alarm threshold (mW)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: optical_receive_power_warning_high
                        
                        	High optical receive power warning threshold (mW)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: optical_receive_power_warning_low
                        
                        	Low optical receive power warning threshold (mW)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: optical_transmit_power_alarm_high
                        
                        	High optical transmit power alarm threshold (mW)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: optical_transmit_power_alarm_low
                        
                        	Low optical transmit power alarm threshold (mW)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: optical_transmit_power_warning_high
                        
                        	High optical transmit power warning threshold (mW)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: optical_transmit_power_warning_low
                        
                        	Low optical transmit power warning threshold (mW)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: transceiver_temperature_alarm_high
                        
                        	Transceiver high temperature alarm threshold (mDegrees C)
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: transceiver_temperature_alarm_low
                        
                        	Transceiver low temperature alarm threshold (mDegrees C)
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
                        
                        .. attribute:: transceiver_voltage_alarm_high
                        
                        	Transceiver high voltage alarm threshold (mV)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: transceiver_voltage_alarm_low
                        
                        	Transceiver low voltage alarm threshold (mV)
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
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: receive_power_valid
                            
                            	The receive power fields are valid
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: temperature_valid
                            
                            	The temperature fields are valid
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: transmit_power_valid
                            
                            	The transmit power fields are valid
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: voltage_valid
                            
                            	The voltage fields are valid
                            	**type**\: int
                            
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
                                if not self.is_config():
                                    return False
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
                                from ydk.models.drivers._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
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
                            if not self.is_config():
                                return False
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
                            from ydk.models.drivers._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
                            return meta._meta_table['EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails.DigOptMonAlarmThresholds']['meta_info']


                    class DigOptMonAlarms(object):
                        """
                        Digital Optical Monitoring alarms
                        
                        .. attribute:: laser_bias_current
                        
                        	Laser Bias Current Alarm
                        	**type**\: :py:class:`EtherDomAlarmEnum <ydk.models.drivers.Cisco_IOS_XR_drivers_media_eth_oper.EtherDomAlarmEnum>`
                        
                        .. attribute:: received_laser_power
                        
                        	Received Optical Power Alarm
                        	**type**\: :py:class:`EtherDomAlarmEnum <ydk.models.drivers.Cisco_IOS_XR_drivers_media_eth_oper.EtherDomAlarmEnum>`
                        
                        .. attribute:: transceiver_temperature
                        
                        	Transceiver Temperature Alarm
                        	**type**\: :py:class:`EtherDomAlarmEnum <ydk.models.drivers.Cisco_IOS_XR_drivers_media_eth_oper.EtherDomAlarmEnum>`
                        
                        .. attribute:: transceiver_voltage
                        
                        	Transceiver Voltage Alarm
                        	**type**\: :py:class:`EtherDomAlarmEnum <ydk.models.drivers.Cisco_IOS_XR_drivers_media_eth_oper.EtherDomAlarmEnum>`
                        
                        .. attribute:: transmit_laser_power
                        
                        	Transmit Laser Power Alarm
                        	**type**\: :py:class:`EtherDomAlarmEnum <ydk.models.drivers.Cisco_IOS_XR_drivers_media_eth_oper.EtherDomAlarmEnum>`
                        
                        

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
                            if not self.is_config():
                                return False
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
                            from ydk.models.drivers._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
                            return meta._meta_table['EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails.DigOptMonAlarms']['meta_info']


                    class Lane(object):
                        """
                        Digital Optical Monitoring (per lane
                        information)
                        
                        .. attribute:: center_wavelength
                        
                        	Center Wavelength (nm\*1000)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: dig_opt_mon_alarm
                        
                        	Digital Optical Monitoring alarms
                        	**type**\: :py:class:`DigOptMonAlarm <ydk.models.drivers.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails.Lane.DigOptMonAlarm>`
                        
                        .. attribute:: laser_bias_current
                        
                        	Laser Bias Current (uAmps)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: received_laser_power
                        
                        	Received Optical Power (dBm\*1000)
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: transmit_laser_power
                        
                        	Transmit Laser Power (dBm\*1000)
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        

                        """

                        _prefix = 'drivers-media-eth-oper'
                        _revision = '2015-10-14'

                        def __init__(self):
                            self.parent = None
                            self.center_wavelength = None
                            self.dig_opt_mon_alarm = EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails.Lane.DigOptMonAlarm()
                            self.dig_opt_mon_alarm.parent = self
                            self.laser_bias_current = None
                            self.received_laser_power = None
                            self.transmit_laser_power = None


                        class DigOptMonAlarm(object):
                            """
                            Digital Optical Monitoring alarms
                            
                            .. attribute:: laser_bias_current
                            
                            	Laser Bias Current Alarm
                            	**type**\: :py:class:`EtherDomAlarmEnum <ydk.models.drivers.Cisco_IOS_XR_drivers_media_eth_oper.EtherDomAlarmEnum>`
                            
                            .. attribute:: received_laser_power
                            
                            	Received Optical Power Alarm
                            	**type**\: :py:class:`EtherDomAlarmEnum <ydk.models.drivers.Cisco_IOS_XR_drivers_media_eth_oper.EtherDomAlarmEnum>`
                            
                            .. attribute:: transmit_laser_power
                            
                            	Transmit Laser Power Alarm
                            	**type**\: :py:class:`EtherDomAlarmEnum <ydk.models.drivers.Cisco_IOS_XR_drivers_media_eth_oper.EtherDomAlarmEnum>`
                            
                            

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
                                if not self.is_config():
                                    return False
                                if self.laser_bias_current is not None:
                                    return True

                                if self.received_laser_power is not None:
                                    return True

                                if self.transmit_laser_power is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.drivers._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
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
                            if not self.is_config():
                                return False
                            if self.center_wavelength is not None:
                                return True

                            if self.dig_opt_mon_alarm is not None and self.dig_opt_mon_alarm._has_data():
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
                            from ydk.models.drivers._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
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
                        if not self.is_config():
                            return False
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

                        if self.transceiver_temperature is not None:
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
                        from ydk.models.drivers._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
                        return meta._meta_table['EthernetInterface.Interfaces.Interface.PhyInfo.PhyDetails']['meta_info']


                class FecDetails(object):
                    """
                    Forward Error Correction information
                    
                    .. attribute:: corrected_codeword_count
                    
                    	Corrected codeword error count
                    	**type**\: long
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: fec
                    
                    	Port operational FEC type
                    	**type**\: :py:class:`EthernetFecEnum <ydk.models.drivers.Cisco_IOS_XR_drivers_media_eth_oper.EthernetFecEnum>`
                    
                    .. attribute:: uncorrected_codeword_count
                    
                    	Uncorrected codeword error count
                    	**type**\: long
                    
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
                        if not self.is_config():
                            return False
                        if self.corrected_codeword_count is not None:
                            return True

                        if self.fec is not None:
                            return True

                        if self.uncorrected_codeword_count is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.drivers._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
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
                    if not self.is_config():
                        return False
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
                    from ydk.models.drivers._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
                    return meta._meta_table['EthernetInterface.Interfaces.Interface.PhyInfo']['meta_info']


            class Layer1Info(object):
                """
                Layer 1 information
                
                .. attribute:: autoneg
                
                	Port autonegotiation configuration settings
                	**type**\: :py:class:`Autoneg <ydk.models.drivers.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Interfaces.Interface.Layer1Info.Autoneg>`
                
                .. attribute:: bandwidth_utilization
                
                	Bandwidth utilization (hundredths of a percent)
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: ber_monitoring
                
                	BER monitoring details
                	**type**\: :py:class:`BerMonitoring <ydk.models.drivers.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Interfaces.Interface.Layer1Info.BerMonitoring>`
                
                .. attribute:: current_alarms
                
                	Current alarms
                	**type**\: :py:class:`CurrentAlarms <ydk.models.drivers.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Interfaces.Interface.Layer1Info.CurrentAlarms>`
                
                .. attribute:: duplex
                
                	Port operational duplexity
                	**type**\: :py:class:`EthernetDuplexEnum <ydk.models.drivers.Cisco_IOS_XR_drivers_media_eth_oper.EthernetDuplexEnum>`
                
                .. attribute:: error_counts
                
                	Statistics for detected errors
                	**type**\: :py:class:`ErrorCounts <ydk.models.drivers.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Interfaces.Interface.Layer1Info.ErrorCounts>`
                
                .. attribute:: flowcontrol
                
                	Port operational flow control
                	**type**\: :py:class:`EtherFlowcontrolEnum <ydk.models.drivers.Cisco_IOS_XR_drivers_media_eth_oper.EtherFlowcontrolEnum>`
                
                .. attribute:: ipg
                
                	Port operational inter\-packet\-gap
                	**type**\: :py:class:`EthernetIpgEnum <ydk.models.drivers.Cisco_IOS_XR_drivers_media_eth_oper.EthernetIpgEnum>`
                
                .. attribute:: laser_squelch_enabled
                
                	Laser Squelch \- TRUE if enabled
                	**type**\: bool
                
                .. attribute:: led_state
                
                	State of the LED
                	**type**\: :py:class:`EtherLedStateEnum <ydk.models.drivers.Cisco_IOS_XR_drivers_media_eth_oper.EtherLedStateEnum>`
                
                .. attribute:: link_state
                
                	Link state
                	**type**\: :py:class:`EtherLinkStateEnum <ydk.models.drivers.Cisco_IOS_XR_drivers_media_eth_oper.EtherLinkStateEnum>`
                
                .. attribute:: previous_alarms
                
                	Previous alarms
                	**type**\: :py:class:`PreviousAlarms <ydk.models.drivers.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Interfaces.Interface.Layer1Info.PreviousAlarms>`
                
                .. attribute:: speed
                
                	Port operational speed
                	**type**\: :py:class:`EthernetSpeedEnum <ydk.models.drivers.Cisco_IOS_XR_drivers_media_eth_oper.EthernetSpeedEnum>`
                
                

                """

                _prefix = 'drivers-media-eth-oper'
                _revision = '2015-10-14'

                def __init__(self):
                    self.parent = None
                    self.autoneg = EthernetInterface.Interfaces.Interface.Layer1Info.Autoneg()
                    self.autoneg.parent = self
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
                    self.previous_alarms = EthernetInterface.Interfaces.Interface.Layer1Info.PreviousAlarms()
                    self.previous_alarms.parent = self
                    self.speed = None


                class Autoneg(object):
                    """
                    Port autonegotiation configuration settings
                    
                    .. attribute:: autoneg_enabled
                    
                    	TRUE if autonegotiation is enabled
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: config_override
                    
                    	If true, configuration overrides negotiated settings.  If false, negotiated settings in effect
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: duplex
                    
                    	Restricted duplex (if relevant bit is set in mask)
                    	**type**\: :py:class:`EthernetDuplexEnum <ydk.models.drivers.Cisco_IOS_XR_drivers_media_eth_oper.EthernetDuplexEnum>`
                    
                    .. attribute:: flowcontrol
                    
                    	Restricted flowcontrol (if relevant bit is set in mask)
                    	**type**\: :py:class:`EtherFlowcontrolEnum <ydk.models.drivers.Cisco_IOS_XR_drivers_media_eth_oper.EtherFlowcontrolEnum>`
                    
                    .. attribute:: mask
                    
                    	Validity mask\: 0x1 speed, 0x2 duplex, 0x4 flowcontrol
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: speed
                    
                    	Restricted speed (if relevant bit is set in mask)
                    	**type**\: :py:class:`EthernetSpeedEnum <ydk.models.drivers.Cisco_IOS_XR_drivers_media_eth_oper.EthernetSpeedEnum>`
                    
                    

                    """

                    _prefix = 'drivers-media-eth-oper'
                    _revision = '2015-10-14'

                    def __init__(self):
                        self.parent = None
                        self.autoneg_enabled = None
                        self.config_override = None
                        self.duplex = None
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
                        if not self.is_config():
                            return False
                        if self.autoneg_enabled is not None:
                            return True

                        if self.config_override is not None:
                            return True

                        if self.duplex is not None:
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
                        from ydk.models.drivers._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
                        return meta._meta_table['EthernetInterface.Interfaces.Interface.Layer1Info.Autoneg']['meta_info']


                class CurrentAlarms(object):
                    """
                    Current alarms
                    
                    .. attribute:: hi_ber_alarm
                    
                    	Hi BER
                    	**type**\: :py:class:`EthCtrlrAlarmStateEnum <ydk.models.drivers.Cisco_IOS_XR_drivers_media_eth_oper.EthCtrlrAlarmStateEnum>`
                    
                    .. attribute:: local_fault_alarm
                    
                    	Local Fault
                    	**type**\: :py:class:`EthCtrlrAlarmStateEnum <ydk.models.drivers.Cisco_IOS_XR_drivers_media_eth_oper.EthCtrlrAlarmStateEnum>`
                    
                    .. attribute:: loss_of_synchronization_data_alarm
                    
                    	Loss of Synchronization Data
                    	**type**\: :py:class:`EthCtrlrAlarmStateEnum <ydk.models.drivers.Cisco_IOS_XR_drivers_media_eth_oper.EthCtrlrAlarmStateEnum>`
                    
                    .. attribute:: pcs_loss_of_block_lock_alarm
                    
                    	PCS Loss of Block Lock
                    	**type**\: :py:class:`EthCtrlrAlarmStateEnum <ydk.models.drivers.Cisco_IOS_XR_drivers_media_eth_oper.EthCtrlrAlarmStateEnum>`
                    
                    .. attribute:: received_loss_of_signal_alarm
                    
                    	Received Loss of Signal
                    	**type**\: :py:class:`EthCtrlrAlarmStateEnum <ydk.models.drivers.Cisco_IOS_XR_drivers_media_eth_oper.EthCtrlrAlarmStateEnum>`
                    
                    .. attribute:: remote_fault_alarm
                    
                    	Remote Fault
                    	**type**\: :py:class:`EthCtrlrAlarmStateEnum <ydk.models.drivers.Cisco_IOS_XR_drivers_media_eth_oper.EthCtrlrAlarmStateEnum>`
                    
                    .. attribute:: sd_ber_alarm
                    
                    	SD BER
                    	**type**\: :py:class:`EthCtrlrAlarmStateEnum <ydk.models.drivers.Cisco_IOS_XR_drivers_media_eth_oper.EthCtrlrAlarmStateEnum>`
                    
                    .. attribute:: sf_ber_alarm
                    
                    	SF BER
                    	**type**\: :py:class:`EthCtrlrAlarmStateEnum <ydk.models.drivers.Cisco_IOS_XR_drivers_media_eth_oper.EthCtrlrAlarmStateEnum>`
                    
                    .. attribute:: squelch_alarm
                    
                    	Squelch
                    	**type**\: :py:class:`EthCtrlrAlarmStateEnum <ydk.models.drivers.Cisco_IOS_XR_drivers_media_eth_oper.EthCtrlrAlarmStateEnum>`
                    
                    

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
                        if not self.is_config():
                            return False
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

                        if self.sd_ber_alarm is not None:
                            return True

                        if self.sf_ber_alarm is not None:
                            return True

                        if self.squelch_alarm is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.drivers._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
                        return meta._meta_table['EthernetInterface.Interfaces.Interface.Layer1Info.CurrentAlarms']['meta_info']


                class PreviousAlarms(object):
                    """
                    Previous alarms
                    
                    .. attribute:: hi_ber_alarm
                    
                    	Hi BER
                    	**type**\: :py:class:`EthCtrlrAlarmStateEnum <ydk.models.drivers.Cisco_IOS_XR_drivers_media_eth_oper.EthCtrlrAlarmStateEnum>`
                    
                    .. attribute:: local_fault_alarm
                    
                    	Local Fault
                    	**type**\: :py:class:`EthCtrlrAlarmStateEnum <ydk.models.drivers.Cisco_IOS_XR_drivers_media_eth_oper.EthCtrlrAlarmStateEnum>`
                    
                    .. attribute:: loss_of_synchronization_data_alarm
                    
                    	Loss of Synchronization Data
                    	**type**\: :py:class:`EthCtrlrAlarmStateEnum <ydk.models.drivers.Cisco_IOS_XR_drivers_media_eth_oper.EthCtrlrAlarmStateEnum>`
                    
                    .. attribute:: pcs_loss_of_block_lock_alarm
                    
                    	PCS Loss of Block Lock
                    	**type**\: :py:class:`EthCtrlrAlarmStateEnum <ydk.models.drivers.Cisco_IOS_XR_drivers_media_eth_oper.EthCtrlrAlarmStateEnum>`
                    
                    .. attribute:: received_loss_of_signal_alarm
                    
                    	Received Loss of Signal
                    	**type**\: :py:class:`EthCtrlrAlarmStateEnum <ydk.models.drivers.Cisco_IOS_XR_drivers_media_eth_oper.EthCtrlrAlarmStateEnum>`
                    
                    .. attribute:: remote_fault_alarm
                    
                    	Remote Fault
                    	**type**\: :py:class:`EthCtrlrAlarmStateEnum <ydk.models.drivers.Cisco_IOS_XR_drivers_media_eth_oper.EthCtrlrAlarmStateEnum>`
                    
                    .. attribute:: sd_ber_alarm
                    
                    	SD BER
                    	**type**\: :py:class:`EthCtrlrAlarmStateEnum <ydk.models.drivers.Cisco_IOS_XR_drivers_media_eth_oper.EthCtrlrAlarmStateEnum>`
                    
                    .. attribute:: sf_ber_alarm
                    
                    	SF BER
                    	**type**\: :py:class:`EthCtrlrAlarmStateEnum <ydk.models.drivers.Cisco_IOS_XR_drivers_media_eth_oper.EthCtrlrAlarmStateEnum>`
                    
                    .. attribute:: squelch_alarm
                    
                    	Squelch
                    	**type**\: :py:class:`EthCtrlrAlarmStateEnum <ydk.models.drivers.Cisco_IOS_XR_drivers_media_eth_oper.EthCtrlrAlarmStateEnum>`
                    
                    

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
                        if not self.is_config():
                            return False
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

                        if self.sd_ber_alarm is not None:
                            return True

                        if self.sf_ber_alarm is not None:
                            return True

                        if self.squelch_alarm is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.drivers._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
                        return meta._meta_table['EthernetInterface.Interfaces.Interface.Layer1Info.PreviousAlarms']['meta_info']


                class ErrorCounts(object):
                    """
                    Statistics for detected errors
                    
                    .. attribute:: pcsbip_errors
                    
                    	PCS BIP error count
                    	**type**\: long
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: sync_header_errors
                    
                    	Sync\-header error count
                    	**type**\: long
                    
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
                        if not self.is_config():
                            return False
                        if self.pcsbip_errors is not None:
                            return True

                        if self.sync_header_errors is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.drivers._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
                        return meta._meta_table['EthernetInterface.Interfaces.Interface.Layer1Info.ErrorCounts']['meta_info']


                class BerMonitoring(object):
                    """
                    BER monitoring details
                    
                    .. attribute:: settings
                    
                    	The BER monitoring settings to be applied
                    	**type**\: :py:class:`Settings <ydk.models.drivers.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Interfaces.Interface.Layer1Info.BerMonitoring.Settings>`
                    
                    .. attribute:: supported
                    
                    	Whether or not BER monitoring is supported
                    	**type**\: int
                    
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
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: signal_degrade_threshold
                        
                        	BER threshold for signal to degrade
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: signal_fail_alarm
                        
                        	Report alarm to indicate signal failure
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: signal_fail_threshold
                        
                        	BER threshold for signal to fail
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: signal_remote_fault
                        
                        	Whether drivers should signal remote faults
                        	**type**\: int
                        
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
                            if not self.is_config():
                                return False
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
                            from ydk.models.drivers._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
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
                        if not self.is_config():
                            return False
                        if self.settings is not None and self.settings._has_data():
                            return True

                        if self.supported is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.drivers._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
                        return meta._meta_table['EthernetInterface.Interfaces.Interface.Layer1Info.BerMonitoring']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-drivers-media-eth-oper:layer1-info'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.autoneg is not None and self.autoneg._has_data():
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

                    if self.previous_alarms is not None and self.previous_alarms._has_data():
                        return True

                    if self.speed is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.drivers._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
                    return meta._meta_table['EthernetInterface.Interfaces.Interface.Layer1Info']['meta_info']


            class MacInfo(object):
                """
                MAC Layer information
                
                .. attribute:: burned_in_mac_address
                
                	Port Burned\-In MAC address
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                .. attribute:: mru
                
                	Port operational MRU
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: mtu
                
                	Port operational MTU
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: multicast_mac_filters
                
                	Port multicast MAC filter information
                	**type**\: :py:class:`MulticastMacFilters <ydk.models.drivers.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Interfaces.Interface.MacInfo.MulticastMacFilters>`
                
                .. attribute:: operational_mac_address
                
                	Port operational MAC address
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                .. attribute:: unicast_mac_filters
                
                	Port unicast MAC filter information
                	**type**\: :py:class:`UnicastMacFilters <ydk.models.drivers.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Interfaces.Interface.MacInfo.UnicastMacFilters>`
                
                

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
                    	**type**\: list of str
                    
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
                        if not self.is_config():
                            return False
                        if self.unicast_mac_address is not None:
                            for child in self.unicast_mac_address:
                                if child is not None:
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.drivers._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
                        return meta._meta_table['EthernetInterface.Interfaces.Interface.MacInfo.UnicastMacFilters']['meta_info']


                class MulticastMacFilters(object):
                    """
                    Port multicast MAC filter information
                    
                    .. attribute:: multicast_mac_address
                    
                    	MAC addresses in the multicast ingress destination MAC filter
                    	**type**\: list of :py:class:`MulticastMacAddress <ydk.models.drivers.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Interfaces.Interface.MacInfo.MulticastMacFilters.MulticastMacAddress>`
                    
                    .. attribute:: multicast_promiscuous
                    
                    	Whether the port is in multicast promiscuous mode
                    	**type**\: bool
                    
                    

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
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                        
                        .. attribute:: mask
                        
                        	Mask for this MAC address
                        	**type**\: str
                        
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
                            if not self.is_config():
                                return False
                            if self.mac_address is not None:
                                return True

                            if self.mask is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.drivers._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
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
                        if not self.is_config():
                            return False
                        if self.multicast_mac_address is not None:
                            for child_ref in self.multicast_mac_address:
                                if child_ref._has_data():
                                    return True

                        if self.multicast_promiscuous is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.drivers._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
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
                    if not self.is_config():
                        return False
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
                    from ydk.models.drivers._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
                    return meta._meta_table['EthernetInterface.Interfaces.Interface.MacInfo']['meta_info']


            class TransportInfo(object):
                """
                Transport state information
                
                .. attribute:: ains_status
                
                	AINS Soak status
                	**type**\: :py:class:`EtherAinsStatusEnum <ydk.models.drivers.Cisco_IOS_XR_drivers_media_eth_oper.EtherAinsStatusEnum>`
                
                .. attribute:: maintenance_mode_enabled
                
                	Maintenance Mode \- TRUE if enabled
                	**type**\: bool
                
                .. attribute:: remaining_duration
                
                	Remaining duration (seconds) of AINS soak timer
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: total_duration
                
                	Total duration (seconds) of AINS soak timer
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

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
                    if not self.is_config():
                        return False
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
                    from ydk.models.drivers._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
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
                if not self.is_config():
                    return False
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
                from ydk.models.drivers._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
                return meta._meta_table['EthernetInterface.Interfaces.Interface']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-drivers-media-eth-oper:ethernet-interface/Cisco-IOS-XR-drivers-media-eth-oper:interfaces'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.interface is not None:
                for child_ref in self.interface:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.drivers._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
            return meta._meta_table['EthernetInterface.Interfaces']['meta_info']


    class Berts(object):
        """
        Ethernet controller BERT table
        
        .. attribute:: bert
        
        	Ethernet BERT information
        	**type**\: list of :py:class:`Bert <ydk.models.drivers.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Berts.Bert>`
        
        

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
            	**type**\: str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: bert_status
            
            	Current test status
            	**type**\: :py:class:`BertStatus <ydk.models.drivers.Cisco_IOS_XR_drivers_media_eth_oper.EthernetInterface.Berts.Bert.BertStatus>`
            
            .. attribute:: port_bert_interval
            
            	Port BERT interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: time_left
            
            	Remaining time for this test in seconds
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

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
                	**type**\: bool
                
                .. attribute:: data_availability
                
                	Flag indicating available data
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: device_under_test
                
                	Device being tested
                	**type**\: :py:class:`EthernetDevEnum <ydk.models.drivers.Cisco_IOS_XR_drivers_media_eth_oper.EthernetDevEnum>`
                
                .. attribute:: error_type
                
                	Bit, block or frame error
                	**type**\: :py:class:`EthernetBertErrCntEnum <ydk.models.drivers.Cisco_IOS_XR_drivers_media_eth_oper.EthernetBertErrCntEnum>`
                
                .. attribute:: interface_device
                
                	Interface being tested
                	**type**\: :py:class:`EthernetDevIfEnum <ydk.models.drivers.Cisco_IOS_XR_drivers_media_eth_oper.EthernetDevIfEnum>`
                
                .. attribute:: receive_count
                
                	Receive count (if 0x1 set in flag)
                	**type**\: long
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: receive_errors
                
                	Received errors (if 0x4 set in flag)
                	**type**\: long
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: test_pattern
                
                	Test pattern
                	**type**\: :py:class:`EthernetBertPatternEnum <ydk.models.drivers.Cisco_IOS_XR_drivers_media_eth_oper.EthernetBertPatternEnum>`
                
                .. attribute:: transmit_count
                
                	Transmit count (if 0x2 set in flag)
                	**type**\: long
                
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
                    if not self.is_config():
                        return False
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
                    from ydk.models.drivers._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
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
                if not self.is_config():
                    return False
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
                from ydk.models.drivers._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
                return meta._meta_table['EthernetInterface.Berts.Bert']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-drivers-media-eth-oper:ethernet-interface/Cisco-IOS-XR-drivers-media-eth-oper:berts'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.bert is not None:
                for child_ref in self.bert:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.drivers._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
            return meta._meta_table['EthernetInterface.Berts']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-drivers-media-eth-oper:ethernet-interface'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.berts is not None and self.berts._has_data():
            return True

        if self.interfaces is not None and self.interfaces._has_data():
            return True

        if self.statistics is not None and self.statistics._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.drivers._meta import _Cisco_IOS_XR_drivers_media_eth_oper as meta
        return meta._meta_table['EthernetInterface']['meta_info']


