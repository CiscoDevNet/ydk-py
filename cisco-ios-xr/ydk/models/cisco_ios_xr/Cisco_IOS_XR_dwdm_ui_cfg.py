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

    .. data:: out_of_service = 0

    	Out of service

    .. data:: in_service = 1

    	In service

    .. data:: maintenance = 2

    	Out of service maintenance

    .. data:: in_service_config_allowed = 3

    	In service Config allowed

    """

    out_of_service = 0

    in_service = 1

    maintenance = 2

    in_service_config_allowed = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_cfg as meta
        return meta._meta_table['DwdmAdminStateEnum']


class DwdmLoopbackEnum(Enum):
    """
    DwdmLoopbackEnum

    Dwdm loopback

    .. data:: none = 0

    	No Loopback

    .. data:: line = 1

    	Line Loopback

    .. data:: internal = 2

    	Internal Loopback

    """

    none = 0

    line = 1

    internal = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_cfg as meta
        return meta._meta_table['DwdmLoopbackEnum']


class EfecEnum(Enum):
    """
    EfecEnum

    Efec

    .. data:: none = 0

    	default submode to handle backward

    	compatibility

    .. data:: i__DOT__4 = 1

    	efec i.4

    .. data:: i__DOT__7 = 2

    	efec i.7

    """

    none = 0

    i__DOT__4 = 1

    i__DOT__7 = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_cfg as meta
        return meta._meta_table['EfecEnum']


class ExpectedTtiEnum(Enum):
    """
    ExpectedTtiEnum

    Expected tti

    .. data:: expected_tti_ascii = 3

    	Expected TTI ascii string

    .. data:: expected_tti_hex = 4

    	Expected TTI hex string

    """

    expected_tti_ascii = 3

    expected_tti_hex = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_cfg as meta
        return meta._meta_table['ExpectedTtiEnum']


class FecEnum(Enum):
    """
    FecEnum

    Fec

    .. data:: none = 0

    	No FEC

    .. data:: standard = 1

    	Standard FEC

    .. data:: enhanced = 2

    	Enhanced FEC

    .. data:: high_gain_hd = 3

    	High-Gain Hard Decision

    .. data:: long_haul_hd = 4

    	Long-Haul Hard Decision

    .. data:: high_gain_sd = 5

    	High-Gain Soft Decision

    .. data:: long_haul_sd = 6

    	Long-Haul Soft Decision

    .. data:: ci_bch = 7

    	Ci BCH

    .. data:: high_gain_multivendor_hd = 8

    	High-Gain Multivendor Interoperable Hard

    	Decision

    """

    none = 0

    standard = 1

    enhanced = 2

    high_gain_hd = 3

    long_haul_hd = 4

    high_gain_sd = 5

    long_haul_sd = 6

    ci_bch = 7

    high_gain_multivendor_hd = 8


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_cfg as meta
        return meta._meta_table['FecEnum']


class FramingEnum(Enum):
    """
    FramingEnum

    Framing

    .. data:: opu1e = 1

    	opu1e Framing

    .. data:: opu2e = 2

    	opu2e Framing

    """

    opu1e = 1

    opu2e = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_cfg as meta
        return meta._meta_table['FramingEnum']


class OduAlarmEnum(Enum):
    """
    OduAlarmEnum

    Odu alarm

    .. data:: oci = 14

    	ODU OCI

    .. data:: odu_ais = 15

    	ODU AIS

    .. data:: lck = 16

    	ODU LCK

    .. data:: odu_bdi = 17

    	ODU BDI

    .. data:: odu_sf = 20

    	ODU SF BER

    .. data:: odu_sd = 21

    	ODU SD BER

    .. data:: plm = 22

    	ODU PTIM

    .. data:: odu_tim = 23

    	ODU TIM

    """

    oci = 14

    odu_ais = 15

    lck = 16

    odu_bdi = 17

    odu_sf = 20

    odu_sd = 21

    plm = 22

    odu_tim = 23


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_cfg as meta
        return meta._meta_table['OduAlarmEnum']


class OduThresholdEnum(Enum):
    """
    OduThresholdEnum

    Odu threshold

    .. data:: odu_sd = 8

    	ODU SD BER threshold

    .. data:: odu_sf = 9

    	ODU SF BER threshold

    """

    odu_sd = 8

    odu_sf = 9


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_cfg as meta
        return meta._meta_table['OduThresholdEnum']


class OtuAlarmEnum(Enum):
    """
    OtuAlarmEnum

    Otu alarm

    .. data:: los = 0

    	LOS

    .. data:: lof = 1

    	LOF

    .. data:: lom = 2

    	LOM

    .. data:: iae = 6

    	OTU IAE

    .. data:: otu_bdi = 7

    	OTU BDI

    .. data:: otu_tim = 8

    	OTU TIM

    .. data:: otu_sf = 10

    	OTU SF BER

    .. data:: otu_sd = 11

    	OTU SD BER

    .. data:: fec_mismatch = 24

    	FEC mismatch

    .. data:: prefec_sd_ber = 31

    	PREFEC SD BER

    .. data:: prefec_sf_ber = 32

    	PREFEC SF BER

    """

    los = 0

    lof = 1

    lom = 2

    iae = 6

    otu_bdi = 7

    otu_tim = 8

    otu_sf = 10

    otu_sd = 11

    fec_mismatch = 24

    prefec_sd_ber = 31

    prefec_sf_ber = 32


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_cfg as meta
        return meta._meta_table['OtuAlarmEnum']


class OtuThresholdEnum(Enum):
    """
    OtuThresholdEnum

    Otu threshold

    .. data:: prefec_sd = 0

    	PREFEC SD BER THRESHOLD

    .. data:: prefec_sf = 1

    	PREFEC SF BER THRESHOLD

    .. data:: otu_sd = 4

    	OTU SD BER threshold

    .. data:: otu_sf = 5

    	OTU SF BER threshold

    """

    prefec_sd = 0

    prefec_sf = 1

    otu_sd = 4

    otu_sf = 5


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_cfg as meta
        return meta._meta_table['OtuThresholdEnum']


class PrbsModeEnum(Enum):
    """
    PrbsModeEnum

    Prbs mode

    .. data:: source = 0

    	Source Mode

    .. data:: sink = 1

    	Sink Mode

    .. data:: source_sink = 2

    	Source-Sink Mode

    .. data:: invalid = 3

    	Invalid Mode

    """

    source = 0

    sink = 1

    source_sink = 2

    invalid = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_cfg as meta
        return meta._meta_table['PrbsModeEnum']


class PrbsPatternEnum(Enum):
    """
    PrbsPatternEnum

    Prbs pattern

    .. data:: none = 0

    	None Pattern

    .. data:: null = 1

    	Null Pattern

    .. data:: pn11 = 2

    	PN11 Pattern

    .. data:: pn23 = 3

    	PN23 Pattern

    .. data:: pn31 = 4

    	PN31 Pattern

    """

    none = 0

    null = 1

    pn11 = 2

    pn23 = 3

    pn31 = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_cfg as meta
        return meta._meta_table['PrbsPatternEnum']


class ProactiveEnum(Enum):
    """
    ProactiveEnum

    Proactive

    .. data:: default = 1

    	Proactive Protection Default Mode

    .. data:: graceful = 2

    	Proactive Protection Graceful Mode

    """

    default = 1

    graceful = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_cfg as meta
        return meta._meta_table['ProactiveEnum']


class TxTtiEnum(Enum):
    """
    TxTtiEnum

    Tx tti

    .. data:: tx_tti_ascii = 0

    	TX TTI ascii string

    .. data:: tx_tti_hex = 1

    	TX TTI hex string

    """

    tx_tti_ascii = 0

    tx_tti_hex = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_cfg as meta
        return meta._meta_table['TxTtiEnum']


class WaveChannelNumEnum(Enum):
    """
    WaveChannelNumEnum

    Wave channel num

    .. data:: default = 0

    	Default Wave Channel Number

    .. data:: channel_wavelength = 1

    	Wavelength Wave Channel Number

    .. data:: channel_frequency = 2

    	Frequency Wave Channel Number

    .. data:: Y_100mhz_frequency = 4

    	Frequency in Steps of 100MHz

    """

    default = 0

    channel_wavelength = 1

    channel_frequency = 2

    Y_100mhz_frequency = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_cfg as meta
        return meta._meta_table['WaveChannelNumEnum']



