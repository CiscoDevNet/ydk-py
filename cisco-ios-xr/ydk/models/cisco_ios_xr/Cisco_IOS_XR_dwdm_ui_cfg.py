""" Cisco_IOS_XR_dwdm_ui_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR dwdm\-ui package configuration.

This YANG module augments the
  Cisco\-IOS\-XR\-ifmgr\-cfg
module with configuration data.

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class DwdmAdminState(Enum):
    """
    DwdmAdminState (Enum Class)

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

    out_of_service = Enum.YLeaf(0, "out-of-service")

    in_service = Enum.YLeaf(1, "in-service")

    maintenance = Enum.YLeaf(2, "maintenance")

    in_service_config_allowed = Enum.YLeaf(3, "in-service-config-allowed")


class DwdmLoopback(Enum):
    """
    DwdmLoopback (Enum Class)

    Dwdm loopback

    .. data:: none = 0

    	No Loopback

    .. data:: line = 1

    	Line Loopback

    .. data:: internal = 2

    	Internal Loopback

    """

    none = Enum.YLeaf(0, "none")

    line = Enum.YLeaf(1, "line")

    internal = Enum.YLeaf(2, "internal")


class Efec(Enum):
    """
    Efec (Enum Class)

    Efec

    .. data:: none = 0

    	default submode to handle backward

    	compatibility

    .. data:: i__DOT__4 = 1

    	efec i.4

    .. data:: i__DOT__7 = 2

    	efec i.7

    """

    none = Enum.YLeaf(0, "none")

    i__DOT__4 = Enum.YLeaf(1, "i.4")

    i__DOT__7 = Enum.YLeaf(2, "i.7")


class ExpectedTti(Enum):
    """
    ExpectedTti (Enum Class)

    Expected tti

    .. data:: expected_tti_ascii = 3

    	Expected TTI ascii string

    .. data:: expected_tti_hex = 4

    	Expected TTI hex string

    """

    expected_tti_ascii = Enum.YLeaf(3, "expected-tti-ascii")

    expected_tti_hex = Enum.YLeaf(4, "expected-tti-hex")


class Fec(Enum):
    """
    Fec (Enum Class)

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

    .. data:: sd_everest = 9

    	SD Everest

    .. data:: sd_denali = 10

    	SD Denali

    """

    none = Enum.YLeaf(0, "none")

    standard = Enum.YLeaf(1, "standard")

    enhanced = Enum.YLeaf(2, "enhanced")

    high_gain_hd = Enum.YLeaf(3, "high-gain-hd")

    long_haul_hd = Enum.YLeaf(4, "long-haul-hd")

    high_gain_sd = Enum.YLeaf(5, "high-gain-sd")

    long_haul_sd = Enum.YLeaf(6, "long-haul-sd")

    ci_bch = Enum.YLeaf(7, "ci-bch")

    high_gain_multivendor_hd = Enum.YLeaf(8, "high-gain-multivendor-hd")

    sd_everest = Enum.YLeaf(9, "sd-everest")

    sd_denali = Enum.YLeaf(10, "sd-denali")


class Framing(Enum):
    """
    Framing (Enum Class)

    Framing

    .. data:: opu1e = 1

    	opu1e Framing

    .. data:: opu2e = 2

    	opu2e Framing

    """

    opu1e = Enum.YLeaf(1, "opu1e")

    opu2e = Enum.YLeaf(2, "opu2e")


class OduAlarm(Enum):
    """
    OduAlarm (Enum Class)

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

    oci = Enum.YLeaf(14, "oci")

    odu_ais = Enum.YLeaf(15, "odu-ais")

    lck = Enum.YLeaf(16, "lck")

    odu_bdi = Enum.YLeaf(17, "odu-bdi")

    odu_sf = Enum.YLeaf(20, "odu-sf")

    odu_sd = Enum.YLeaf(21, "odu-sd")

    plm = Enum.YLeaf(22, "plm")

    odu_tim = Enum.YLeaf(23, "odu-tim")


class OduThreshold(Enum):
    """
    OduThreshold (Enum Class)

    Odu threshold

    .. data:: odu_sd = 8

    	ODU SD BER threshold

    .. data:: odu_sf = 9

    	ODU SF BER threshold

    """

    odu_sd = Enum.YLeaf(8, "odu-sd")

    odu_sf = Enum.YLeaf(9, "odu-sf")


class OtuAlarm(Enum):
    """
    OtuAlarm (Enum Class)

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

    los = Enum.YLeaf(0, "los")

    lof = Enum.YLeaf(1, "lof")

    lom = Enum.YLeaf(2, "lom")

    iae = Enum.YLeaf(6, "iae")

    otu_bdi = Enum.YLeaf(7, "otu-bdi")

    otu_tim = Enum.YLeaf(8, "otu-tim")

    otu_sf = Enum.YLeaf(10, "otu-sf")

    otu_sd = Enum.YLeaf(11, "otu-sd")

    fec_mismatch = Enum.YLeaf(24, "fec-mismatch")

    prefec_sd_ber = Enum.YLeaf(31, "prefec-sd-ber")

    prefec_sf_ber = Enum.YLeaf(32, "prefec-sf-ber")


class OtuThreshold(Enum):
    """
    OtuThreshold (Enum Class)

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

    prefec_sd = Enum.YLeaf(0, "prefec-sd")

    prefec_sf = Enum.YLeaf(1, "prefec-sf")

    otu_sd = Enum.YLeaf(4, "otu-sd")

    otu_sf = Enum.YLeaf(5, "otu-sf")


class PrbsMode(Enum):
    """
    PrbsMode (Enum Class)

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

    source = Enum.YLeaf(0, "source")

    sink = Enum.YLeaf(1, "sink")

    source_sink = Enum.YLeaf(2, "source-sink")

    invalid = Enum.YLeaf(3, "invalid")


class PrbsPattern(Enum):
    """
    PrbsPattern (Enum Class)

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

    none = Enum.YLeaf(0, "none")

    null = Enum.YLeaf(1, "null")

    pn11 = Enum.YLeaf(2, "pn11")

    pn23 = Enum.YLeaf(3, "pn23")

    pn31 = Enum.YLeaf(4, "pn31")


class Proactive(Enum):
    """
    Proactive (Enum Class)

    Proactive

    .. data:: default = 1

    	Proactive Protection Default Mode

    .. data:: graceful = 2

    	Proactive Protection Graceful Mode

    """

    default = Enum.YLeaf(1, "default")

    graceful = Enum.YLeaf(2, "graceful")


class TxTti(Enum):
    """
    TxTti (Enum Class)

    Tx tti

    .. data:: tx_tti_ascii = 0

    	TX TTI ascii string

    .. data:: tx_tti_hex = 1

    	TX TTI hex string

    """

    tx_tti_ascii = Enum.YLeaf(0, "tx-tti-ascii")

    tx_tti_hex = Enum.YLeaf(1, "tx-tti-hex")


class WaveChannelNum(Enum):
    """
    WaveChannelNum (Enum Class)

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

    default = Enum.YLeaf(0, "default")

    channel_wavelength = Enum.YLeaf(1, "channel-wavelength")

    channel_frequency = Enum.YLeaf(2, "channel-frequency")

    Y_100mhz_frequency = Enum.YLeaf(4, "100mhz-frequency")



