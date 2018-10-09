""" Cisco_IOS_XR_controller_odu_datatypes 

This module contains a collection of generally useful
derived YANG data types.

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Mode(Enum):
    """
    Mode (Enum Class)

    Mode

    .. data:: mode_invalid = 0

    	prbs Mode Invalid

    .. data:: mode_source = 1

    	Prbs Mode Source

    .. data:: mode_sink = 2

    	Prbs Mode Sink

    .. data:: mode_source_sink = 3

    	Prbs Mode Source_Sink

    """

    mode_invalid = Enum.YLeaf(0, "mode-invalid")

    mode_source = Enum.YLeaf(1, "mode-source")

    mode_sink = Enum.YLeaf(2, "mode-sink")

    mode_source_sink = Enum.YLeaf(3, "mode-source-sink")


class OduDelay(Enum):
    """
    OduDelay (Enum Class)

    Odu delay

    .. data:: disable = 0

    	Delay Disable

    .. data:: enable = 1

    	Delay Enable

    """

    disable = Enum.YLeaf(0, "disable")

    enable = Enum.YLeaf(1, "enable")


class OduTimeSlotGranularity(Enum):
    """
    OduTimeSlotGranularity (Enum Class)

    Odu time slot granularity

    .. data:: Y_1__DOT__25g = 0

    	1.25G time slot granularity

    .. data:: Y_2__DOT__5g = 1

    	2.5G time slot granularity

    """

    Y_1__DOT__25g = Enum.YLeaf(0, "1.25g")

    Y_2__DOT__5g = Enum.YLeaf(1, "2.5g")


class OtnChildControllerName(Enum):
    """
    OtnChildControllerName (Enum Class)

    Otn child controller name

    .. data:: odu1 = 1

    	Create lower order odu1 controller

    .. data:: odu2 = 2

    	Create lower order odu2 controller

    .. data:: odu3 = 3

    	Create lower order odu3 controller

    .. data:: odu0 = 10

    	Create lower order odu0 controller

    .. data:: odu2e = 11

    	Create lower order odu2e controller

    .. data:: odu1e = 23

    	Create lower order odu1e controller

    .. data:: odu2f = 25

    	Create lower order odu2f controller

    .. data:: odu3e1 = 26

    	Create lower order odu3e1 controller

    .. data:: odu3e2 = 27

    	Create lower order odu3e2 controller

    """

    odu1 = Enum.YLeaf(1, "odu1")

    odu2 = Enum.YLeaf(2, "odu2")

    odu3 = Enum.YLeaf(3, "odu3")

    odu0 = Enum.YLeaf(10, "odu0")

    odu2e = Enum.YLeaf(11, "odu2e")

    odu1e = Enum.YLeaf(23, "odu1e")

    odu2f = Enum.YLeaf(25, "odu2f")

    odu3e1 = Enum.YLeaf(26, "odu3e1")

    odu3e2 = Enum.YLeaf(27, "odu3e2")


class OtnChildFlexControllerName(Enum):
    """
    OtnChildFlexControllerName (Enum Class)

    Otn child flex controller name

    .. data:: odu_flex = 22

    	Create lower order odu-flex controller

    """

    odu_flex = Enum.YLeaf(22, "odu-flex")


class OtnExpTtiTypeDapi(Enum):
    """
    OtnExpTtiTypeDapi (Enum Class)

    Otn exp tti type dapi

    .. data:: exp_tti_dapi_ascii__FWD_SLASH__dapi_ascii = 9

    	Expected TTI DAPI ASCII string

    """

    exp_tti_dapi_ascii__FWD_SLASH__dapi_ascii = Enum.YLeaf(9, "exp-tti-dapi-ascii/dapi-ascii")


class OtnExpTtiTypeFull(Enum):
    """
    OtnExpTtiTypeFull (Enum Class)

    Otn exp tti type full

    .. data:: exp_tti_full_ascii__FWD_SLASH__full_ascii = 5

    	Expected TTI Full ASCII string

    .. data:: exp_tti_hex__FWD_SLASH__hex = 7

    	Expected TTI hex string

    """

    exp_tti_full_ascii__FWD_SLASH__full_ascii = Enum.YLeaf(5, "exp-tti-full-ascii/full-ascii")

    exp_tti_hex__FWD_SLASH__hex = Enum.YLeaf(7, "exp-tti-hex/hex")


class OtnExpTtiTypeOs(Enum):
    """
    OtnExpTtiTypeOs (Enum Class)

    Otn exp tti type os

    .. data:: exp_tti_os_ascii__FWD_SLASH__os_ascii = 11

    	Expected TTI OS ASCII string

    .. data:: exp_tti_os_hex__FWD_SLASH__os_hex = 13

    	Expected TTI OS HEX string

    """

    exp_tti_os_ascii__FWD_SLASH__os_ascii = Enum.YLeaf(11, "exp-tti-os-ascii/os-ascii")

    exp_tti_os_hex__FWD_SLASH__os_hex = Enum.YLeaf(13, "exp-tti-os-hex/os-hex")


class OtnExpTtiTypeSapi(Enum):
    """
    OtnExpTtiTypeSapi (Enum Class)

    Otn exp tti type sapi

    .. data:: exp_tti_sapi_ascii__FWD_SLASH__sapi_ascii = 15

    	Expected TTI SAPI ASCII string

    """

    exp_tti_sapi_ascii__FWD_SLASH__sapi_ascii = Enum.YLeaf(15, "exp-tti-sapi-ascii/sapi-ascii")


class OtnFlexMapping(Enum):
    """
    OtnFlexMapping (Enum Class)

    Otn flex mapping

    .. data:: gfp_f_fixed = 1

    	GFP-FIX Mapping

    .. data:: gfp_resizable = 2

    	GFP-Resizable Mapping

    .. data:: cbr = 3

    	CBR Mapping

    """

    gfp_f_fixed = Enum.YLeaf(1, "gfp-f-fixed")

    gfp_resizable = Enum.YLeaf(2, "gfp-resizable")

    cbr = Enum.YLeaf(3, "cbr")


class OtnLoopback(Enum):
    """
    OtnLoopback (Enum Class)

    Otn loopback

    .. data:: line = 2

    	Line loopback

    .. data:: internal = 4

    	Internal loopback

    """

    line = Enum.YLeaf(2, "line")

    internal = Enum.YLeaf(4, "internal")


class OtnMapping(Enum):
    """
    OtnMapping (Enum Class)

    Otn mapping

    .. data:: gfp_f = 1

    	gfp_f for mapping

    .. data:: bmp = 3

    	bmp for mapping

    .. data:: gmp = 4

    	gmp for mapping

    .. data:: gfp_f_ext = 6

    	gfp_f_ext for mapping

    """

    gfp_f = Enum.YLeaf(1, "gfp-f")

    bmp = Enum.YLeaf(3, "bmp")

    gmp = Enum.YLeaf(4, "gmp")

    gfp_f_ext = Enum.YLeaf(6, "gfp-f-ext")


class OtnPerMon(Enum):
    """
    OtnPerMon (Enum Class)

    Otn per mon

    .. data:: disable = 0

    	Performance Monitoring Disabled

    .. data:: enable = 1

    	Performance Monitoring Enabled

    """

    disable = Enum.YLeaf(0, "disable")

    enable = Enum.YLeaf(1, "enable")


class OtnSecAdminState(Enum):
    """
    OtnSecAdminState (Enum Class)

    Otn sec admin state

    .. data:: normal = 0

    	In normal state

    .. data:: maintenance = 1

    	Under maintenance

    """

    normal = Enum.YLeaf(0, "normal")

    maintenance = Enum.YLeaf(1, "maintenance")


class OtnSendTtiTypeDapi(Enum):
    """
    OtnSendTtiTypeDapi (Enum Class)

    Otn send tti type dapi

    .. data:: send_tti_dapi_ascii__FWD_SLASH__dapi_ascii = 8

    	Send TTI DAPI ASCII string

    """

    send_tti_dapi_ascii__FWD_SLASH__dapi_ascii = Enum.YLeaf(8, "send-tti-dapi-ascii/dapi-ascii")


class OtnSendTtiTypeFull(Enum):
    """
    OtnSendTtiTypeFull (Enum Class)

    Otn send tti type full

    .. data:: send_tti_full_ascii__FWD_SLASH__full_ascii = 4

    	Send TTI Full ASCII string

    .. data:: send_tti_hex__FWD_SLASH__hex = 6

    	Send TTI hex string

    """

    send_tti_full_ascii__FWD_SLASH__full_ascii = Enum.YLeaf(4, "send-tti-full-ascii/full-ascii")

    send_tti_hex__FWD_SLASH__hex = Enum.YLeaf(6, "send-tti-hex/hex")


class OtnSendTtiTypeOs(Enum):
    """
    OtnSendTtiTypeOs (Enum Class)

    Otn send tti type os

    .. data:: send_tti_os_ascii__FWD_SLASH__os_ascii = 10

    	Send TTI OS ASCII string

    .. data:: send_tti_os_hex__FWD_SLASH__os_hex = 12

    	Send TTI OS HEX string

    """

    send_tti_os_ascii__FWD_SLASH__os_ascii = Enum.YLeaf(10, "send-tti-os-ascii/os-ascii")

    send_tti_os_hex__FWD_SLASH__os_hex = Enum.YLeaf(12, "send-tti-os-hex/os-hex")


class OtnSendTtiTypeSapi(Enum):
    """
    OtnSendTtiTypeSapi (Enum Class)

    Otn send tti type sapi

    .. data:: send_tti_sapi_ascii__FWD_SLASH__sapi_ascii = 14

    	Send TTI SAPI ASCII string

    """

    send_tti_sapi_ascii__FWD_SLASH__sapi_ascii = Enum.YLeaf(14, "send-tti-sapi-ascii/sapi-ascii")


class OtnTermination(Enum):
    """
    OtnTermination (Enum Class)

    Otn termination

    .. data:: ether = 1

    	Termination to ether

    """

    ether = Enum.YLeaf(1, "ether")


class Otnpmtimca(Enum):
    """
    Otnpmtimca (Enum Class)

    Otnpmtimca

    .. data:: disable = 0

    	Path layer PM TIM Consequent action Disabled

    .. data:: enable = 1

    	Path layer PM TIM Consequent action  Enabled

    """

    disable = Enum.YLeaf(0, "disable")

    enable = Enum.YLeaf(1, "enable")


class OtntcmMode(Enum):
    """
    OtntcmMode (Enum Class)

    Otntcm mode

    .. data:: transparent = 0

    	Set TCM Mode as transparent

    .. data:: nim = 1

    	Set TCM Mode as NIM

    .. data:: operational = 2

    	Set TCM Mode as operational

    """

    transparent = Enum.YLeaf(0, "transparent")

    nim = Enum.YLeaf(1, "nim")

    operational = Enum.YLeaf(2, "operational")


class Otntcmca(Enum):
    """
    Otntcmca (Enum Class)

    Otntcmca

    .. data:: disable = 0

    	Consequent(ial) action for Disabled

    .. data:: enable = 1

    	consequent(ial) action for Enabled

    """

    disable = Enum.YLeaf(0, "disable")

    enable = Enum.YLeaf(1, "enable")


class Pattern(Enum):
    """
    Pattern (Enum Class)

    Pattern

    .. data:: pattern_none = 0

    	prbs pattern None

    .. data:: pattern_pn31 = 1

    	Prbs pattern pn31

    .. data:: pattern_pn23 = 2

    	Prbs pattern pn23

    .. data:: pattern_pn11 = 4

    	Prbs pattern pn11

    .. data:: pattern_inverted_pn31 = 8

    	Prbs pattern inverted pn31

    .. data:: pattern_inverted_pn11 = 16

    	Prbs pattern inverted pn11

    """

    pattern_none = Enum.YLeaf(0, "pattern-none")

    pattern_pn31 = Enum.YLeaf(1, "pattern-pn31")

    pattern_pn23 = Enum.YLeaf(2, "pattern-pn23")

    pattern_pn11 = Enum.YLeaf(4, "pattern-pn11")

    pattern_inverted_pn31 = Enum.YLeaf(8, "pattern-inverted-pn31")

    pattern_inverted_pn11 = Enum.YLeaf(16, "pattern-inverted-pn11")



