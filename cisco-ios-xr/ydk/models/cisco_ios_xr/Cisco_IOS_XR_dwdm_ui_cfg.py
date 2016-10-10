""" Cisco_IOS_XR_dwdm_ui_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR dwdm\-ui package configuration.

This YANG module augments the
  Cisco\-IOS\-XR\-ifmgr\-cfg
module with configuration data.

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class DwdmAdminStateEnum(Enum):
    """
    DwdmAdminStateEnum

    Dwdm admin state

    .. data:: OUT_OF_SERVICE = 0

    	Out of service

    .. data:: IN_SERVICE = 1

    	In service

    .. data:: MAINTENANCE = 2

    	Out of service maintenance

    .. data:: IN_SERVICE_CONFIG_ALLOWED = 3

    	In service Config allowed

    """

    OUT_OF_SERVICE = 0

    IN_SERVICE = 1

    MAINTENANCE = 2

    IN_SERVICE_CONFIG_ALLOWED = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_cfg as meta
        return meta._meta_table['DwdmAdminStateEnum']


class DwdmLoopbackEnum(Enum):
    """
    DwdmLoopbackEnum

    Dwdm loopback

    .. data:: NONE = 0

    	No Loopback

    .. data:: LINE = 1

    	Line Loopback

    .. data:: INTERNAL = 2

    	Internal Loopback

    """

    NONE = 0

    LINE = 1

    INTERNAL = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_cfg as meta
        return meta._meta_table['DwdmLoopbackEnum']


class EfecEnum(Enum):
    """
    EfecEnum

    Efec

    .. data:: NONE = 0

    	default submode to handle backward

    	compatibility

    .. data:: I__DOT__4 = 1

    	efec i.4

    .. data:: I__DOT__7 = 2

    	efec i.7

    """

    NONE = 0

    I__DOT__4 = 1

    I__DOT__7 = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_cfg as meta
        return meta._meta_table['EfecEnum']


class ExpectedTtiEnum(Enum):
    """
    ExpectedTtiEnum

    Expected tti

    .. data:: EXPECTED_TTI_ASCII = 3

    	Expected TTI ascii string

    .. data:: EXPECTED_TTI_HEX = 4

    	Expected TTI hex string

    """

    EXPECTED_TTI_ASCII = 3

    EXPECTED_TTI_HEX = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_cfg as meta
        return meta._meta_table['ExpectedTtiEnum']


class FecEnum(Enum):
    """
    FecEnum

    Fec

    .. data:: NONE = 0

    	No FEC

    .. data:: STANDARD = 1

    	Standard FEC

    .. data:: ENHANCED = 2

    	Enhanced FEC

    .. data:: HIGH_GAIN_HD = 3

    	High-Gain Hard Decision

    .. data:: LONG_HAUL_HD = 4

    	Long-Haul Hard Decision

    .. data:: HIGH_GAIN_SD = 5

    	High-Gain Soft Decision

    .. data:: LONG_HAUL_SD = 6

    	Long-Haul Soft Decision

    .. data:: CI_BCH = 7

    	Ci BCH

    .. data:: HIGH_GAIN_MULTIVENDOR_HD = 8

    	High-Gain Multivendor Interoperable Hard

    	Decision

    """

    NONE = 0

    STANDARD = 1

    ENHANCED = 2

    HIGH_GAIN_HD = 3

    LONG_HAUL_HD = 4

    HIGH_GAIN_SD = 5

    LONG_HAUL_SD = 6

    CI_BCH = 7

    HIGH_GAIN_MULTIVENDOR_HD = 8


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_cfg as meta
        return meta._meta_table['FecEnum']


class FramingEnum(Enum):
    """
    FramingEnum

    Framing

    .. data:: OPU1E = 1

    	opu1e Framing

    .. data:: OPU2E = 2

    	opu2e Framing

    """

    OPU1E = 1

    OPU2E = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_cfg as meta
        return meta._meta_table['FramingEnum']


class OduAlarmEnum(Enum):
    """
    OduAlarmEnum

    Odu alarm

    .. data:: OCI = 14

    	ODU OCI

    .. data:: ODU_AIS = 15

    	ODU AIS

    .. data:: LCK = 16

    	ODU LCK

    .. data:: ODU_BDI = 17

    	ODU BDI

    .. data:: ODU_SF = 20

    	ODU SF BER

    .. data:: ODU_SD = 21

    	ODU SD BER

    .. data:: PLM = 22

    	ODU PTIM

    .. data:: ODU_TIM = 23

    	ODU TIM

    """

    OCI = 14

    ODU_AIS = 15

    LCK = 16

    ODU_BDI = 17

    ODU_SF = 20

    ODU_SD = 21

    PLM = 22

    ODU_TIM = 23


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_cfg as meta
        return meta._meta_table['OduAlarmEnum']


class OduThresholdEnum(Enum):
    """
    OduThresholdEnum

    Odu threshold

    .. data:: ODU_SD = 8

    	ODU SD BER threshold

    .. data:: ODU_SF = 9

    	ODU SF BER threshold

    """

    ODU_SD = 8

    ODU_SF = 9


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_cfg as meta
        return meta._meta_table['OduThresholdEnum']


class OtuAlarmEnum(Enum):
    """
    OtuAlarmEnum

    Otu alarm

    .. data:: LOS = 0

    	LOS

    .. data:: LOF = 1

    	LOF

    .. data:: LOM = 2

    	LOM

    .. data:: IAE = 6

    	OTU IAE

    .. data:: OTU_BDI = 7

    	OTU BDI

    .. data:: OTU_TIM = 8

    	OTU TIM

    .. data:: OTU_SF = 10

    	OTU SF BER

    .. data:: OTU_SD = 11

    	OTU SD BER

    .. data:: FEC_MISMATCH = 24

    	FEC mismatch

    .. data:: PREFEC_SD_BER = 31

    	PREFEC SD BER

    .. data:: PREFEC_SF_BER = 32

    	PREFEC SF BER

    """

    LOS = 0

    LOF = 1

    LOM = 2

    IAE = 6

    OTU_BDI = 7

    OTU_TIM = 8

    OTU_SF = 10

    OTU_SD = 11

    FEC_MISMATCH = 24

    PREFEC_SD_BER = 31

    PREFEC_SF_BER = 32


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_cfg as meta
        return meta._meta_table['OtuAlarmEnum']


class OtuThresholdEnum(Enum):
    """
    OtuThresholdEnum

    Otu threshold

    .. data:: PREFEC_SD = 0

    	PREFEC SD BER THRESHOLD

    .. data:: PREFEC_SF = 1

    	PREFEC SF BER THRESHOLD

    .. data:: OTU_SD = 4

    	OTU SD BER threshold

    .. data:: OTU_SF = 5

    	OTU SF BER threshold

    """

    PREFEC_SD = 0

    PREFEC_SF = 1

    OTU_SD = 4

    OTU_SF = 5


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_cfg as meta
        return meta._meta_table['OtuThresholdEnum']


class PrbsModeEnum(Enum):
    """
    PrbsModeEnum

    Prbs mode

    .. data:: SOURCE = 0

    	Source Mode

    .. data:: SINK = 1

    	Sink Mode

    .. data:: SOURCE_SINK = 2

    	Source-Sink Mode

    .. data:: INVALID = 3

    	Invalid Mode

    """

    SOURCE = 0

    SINK = 1

    SOURCE_SINK = 2

    INVALID = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_cfg as meta
        return meta._meta_table['PrbsModeEnum']


class PrbsPatternEnum(Enum):
    """
    PrbsPatternEnum

    Prbs pattern

    .. data:: NONE = 0

    	None Pattern

    .. data:: NULL = 1

    	Null Pattern

    .. data:: PN11 = 2

    	PN11 Pattern

    .. data:: PN23 = 3

    	PN23 Pattern

    .. data:: PN31 = 4

    	PN31 Pattern

    """

    NONE = 0

    NULL = 1

    PN11 = 2

    PN23 = 3

    PN31 = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_cfg as meta
        return meta._meta_table['PrbsPatternEnum']


class ProactiveEnum(Enum):
    """
    ProactiveEnum

    Proactive

    .. data:: DEFAULT = 1

    	Proactive Protection Default Mode

    .. data:: GRACEFUL = 2

    	Proactive Protection Graceful Mode

    """

    DEFAULT = 1

    GRACEFUL = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_cfg as meta
        return meta._meta_table['ProactiveEnum']


class TxTtiEnum(Enum):
    """
    TxTtiEnum

    Tx tti

    .. data:: TX_TTI_ASCII = 0

    	TX TTI ascii string

    .. data:: TX_TTI_HEX = 1

    	TX TTI hex string

    """

    TX_TTI_ASCII = 0

    TX_TTI_HEX = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_cfg as meta
        return meta._meta_table['TxTtiEnum']


class WaveChannelNumEnum(Enum):
    """
    WaveChannelNumEnum

    Wave channel num

    .. data:: DEFAULT = 0

    	Default Wave Channel Number

    .. data:: CHANNEL_WAVELENGTH = 1

    	Wavelength Wave Channel Number

    .. data:: CHANNEL_FREQUENCY = 2

    	Frequency Wave Channel Number

    .. data:: Y_100MHZ_FREQUENCY = 4

    	Frequency in Steps of 100MHz

    """

    DEFAULT = 0

    CHANNEL_WAVELENGTH = 1

    CHANNEL_FREQUENCY = 2

    Y_100MHZ_FREQUENCY = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_cfg as meta
        return meta._meta_table['WaveChannelNumEnum']



