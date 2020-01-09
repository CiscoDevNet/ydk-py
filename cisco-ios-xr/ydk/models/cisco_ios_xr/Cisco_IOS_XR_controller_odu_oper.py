""" Cisco_IOS_XR_controller_odu_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR controller\-odu package operational data.

This module contains definitions
for the following management objects\:
  odu\: ODU operational data

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
import sys
from collections import OrderedDict

from ydk.types import Entity as _Entity_
from ydk.types import EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class DpProgrammed(Enum):
    """
    DpProgrammed (Enum Class)

    Dp programmed

    .. data:: dp_not_programmed = 0

    	DP not programmed

    .. data:: dp_programmed_success = 1

    	DP programmed

    .. data:: end_pt_first_channel_ized = 2

    	ENDPT FIRST CHANNELIZED

    .. data:: end_pt_se_cond_channel_ized = 3

    	ENDPT SECOND CHANNELIZED

    .. data:: end_pt_first_cross_connected = 4

    	ENDPT FIRST CROSS CONNECTED

    .. data:: end_pt_se_cond_cross_connected = 5

    	ENDPT SECOND CROSS CONNECTED

    .. data:: end_pt_first_open_connected = 6

    	ENDPT FIRST OPEN CONNECTED

    .. data:: end_pt_se_cond_open_connected = 7

    	ENDPT SECOND OPEN CONNECTED

    .. data:: end_pt_first_loop_back_ed = 8

    	ENDPT FIRST LOOPBACKED

    .. data:: end_pt_se_cond_loop_back_ed = 9

    	ENDPT SECOND LOOPBACKED

    .. data:: end_pt_odu_type_mismatch = 10

    	ENDPT ODU TYPE MISMATCH

    .. data:: xc_not_set = 11

    	XCONNECT NOT SET

    """

    dp_not_programmed = Enum.YLeaf(0, "dp-not-programmed")

    dp_programmed_success = Enum.YLeaf(1, "dp-programmed-success")

    end_pt_first_channel_ized = Enum.YLeaf(2, "end-pt-first-channel-ized")

    end_pt_se_cond_channel_ized = Enum.YLeaf(3, "end-pt-se-cond-channel-ized")

    end_pt_first_cross_connected = Enum.YLeaf(4, "end-pt-first-cross-connected")

    end_pt_se_cond_cross_connected = Enum.YLeaf(5, "end-pt-se-cond-cross-connected")

    end_pt_first_open_connected = Enum.YLeaf(6, "end-pt-first-open-connected")

    end_pt_se_cond_open_connected = Enum.YLeaf(7, "end-pt-se-cond-open-connected")

    end_pt_first_loop_back_ed = Enum.YLeaf(8, "end-pt-first-loop-back-ed")

    end_pt_se_cond_loop_back_ed = Enum.YLeaf(9, "end-pt-se-cond-loop-back-ed")

    end_pt_odu_type_mismatch = Enum.YLeaf(10, "end-pt-odu-type-mismatch")

    xc_not_set = Enum.YLeaf(11, "xc-not-set")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
        return meta._meta_table['DpProgrammed']


class GmplsTtiMode(Enum):
    """
    GmplsTtiMode (Enum Class)

    Gmpls tti mode

    .. data:: gmpls_odu_tti_mode_none = 0

    	Not Set

    .. data:: gmpls_odu_tti_mode_sm = 1

    	Section Monitoring

    .. data:: gmpls_odu_tti_mode_pm = 2

    	Path Monitoring

    .. data:: gmpls_odu_tti_mode_tcm = 3

    	Tandem Connection Monitoring

    """

    gmpls_odu_tti_mode_none = Enum.YLeaf(0, "gmpls-odu-tti-mode-none")

    gmpls_odu_tti_mode_sm = Enum.YLeaf(1, "gmpls-odu-tti-mode-sm")

    gmpls_odu_tti_mode_pm = Enum.YLeaf(2, "gmpls-odu-tti-mode-pm")

    gmpls_odu_tti_mode_tcm = Enum.YLeaf(3, "gmpls-odu-tti-mode-tcm")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
        return meta._meta_table['GmplsTtiMode']


class OduAinsStateEt(Enum):
    """
    OduAinsStateEt (Enum Class)

    Odu ains state et

    .. data:: none = 0

    	None

    .. data:: active_running = 1

    	Running

    .. data:: active_pending = 2

    	Pending

    """

    none = Enum.YLeaf(0, "none")

    active_running = Enum.YLeaf(1, "active-running")

    active_pending = Enum.YLeaf(2, "active-pending")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
        return meta._meta_table['OduAinsStateEt']


class OduDerState(Enum):
    """
    OduDerState (Enum Class)

    Odu der state

    .. data:: out_of_service = 0

    	Out Of Service

    .. data:: in_service = 1

    	In Service

    .. data:: maintenance = 2

    	Maintenance

    .. data:: ains = 3

    	Automatic In Service

    """

    out_of_service = Enum.YLeaf(0, "out-of-service")

    in_service = Enum.YLeaf(1, "in-service")

    maintenance = Enum.YLeaf(2, "maintenance")

    ains = Enum.YLeaf(3, "ains")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
        return meta._meta_table['OduDerState']


class OduEtherMapPingEt(Enum):
    """
    OduEtherMapPingEt (Enum Class)

    Odu ether map ping et

    .. data:: none = 0

    	None

    .. data:: gfp = 1

    	GfpF

    .. data:: amp = 2

    	Amp

    .. data:: bmp = 3

    	Bmp

    .. data:: gmp = 4

    	Gmp

    .. data:: wis = 5

    	Wis

    .. data:: gfp_ext = 6

    	GfpF Ext

    """

    none = Enum.YLeaf(0, "none")

    gfp = Enum.YLeaf(1, "gfp")

    amp = Enum.YLeaf(2, "amp")

    bmp = Enum.YLeaf(3, "bmp")

    gmp = Enum.YLeaf(4, "gmp")

    wis = Enum.YLeaf(5, "wis")

    gfp_ext = Enum.YLeaf(6, "gfp-ext")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
        return meta._meta_table['OduEtherMapPingEt']


class OduFlexTypeEt(Enum):
    """
    OduFlexTypeEt (Enum Class)

    Odu flex type et

    .. data:: na = 0

    	NA

    .. data:: cbr = 1

    	ODU Flex Type CBR

    .. data:: gfp_resizable = 2

    	ODU Flex Type GFP resizable

    .. data:: gfp_fix = 3

    	ODU Flex Type GFP fix

    """

    na = Enum.YLeaf(0, "na")

    cbr = Enum.YLeaf(1, "cbr")

    gfp_resizable = Enum.YLeaf(2, "gfp-resizable")

    gfp_fix = Enum.YLeaf(3, "gfp-fix")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
        return meta._meta_table['OduFlexTypeEt']


class OduLoopBackMode(Enum):
    """
    OduLoopBackMode (Enum Class)

    Odu loop back mode

    .. data:: none = 1

    	None

    .. data:: line = 2

    	Line

    .. data:: internal = 4

    	Internal

    """

    none = Enum.YLeaf(1, "none")

    line = Enum.YLeaf(2, "line")

    internal = Enum.YLeaf(4, "internal")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
        return meta._meta_table['OduLoopBackMode']


class OduPerMon(Enum):
    """
    OduPerMon (Enum Class)

    Odu per mon

    .. data:: disable = 0

    	Disable

    .. data:: enable = 1

    	Enable

    """

    disable = Enum.YLeaf(0, "disable")

    enable = Enum.YLeaf(1, "enable")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
        return meta._meta_table['OduPerMon']


class OduPmCaEt(Enum):
    """
    OduPmCaEt (Enum Class)

    Odu pm ca et

    .. data:: disable = 0

    	Disable

    .. data:: enable = 1

    	Enable

    """

    disable = Enum.YLeaf(0, "disable")

    enable = Enum.YLeaf(1, "enable")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
        return meta._meta_table['OduPmCaEt']


class OduPmMode(Enum):
    """
    OduPmMode (Enum Class)

    Odu pm mode

    .. data:: nim = 0

    	Non-Intrusive Monitor

    .. data:: oper = 1

    	Operational

    """

    nim = Enum.YLeaf(0, "nim")

    oper = Enum.YLeaf(1, "oper")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
        return meta._meta_table['OduPmMode']


class OduPrbsMode(Enum):
    """
    OduPrbsMode (Enum Class)

    Odu prbs mode

    .. data:: invalid = 0

    	invalid

    .. data:: source = 1

    	Source

    .. data:: sink = 2

    	Sink

    .. data:: source_sink = 3

    	Source Sink

    """

    invalid = Enum.YLeaf(0, "invalid")

    source = Enum.YLeaf(1, "source")

    sink = Enum.YLeaf(2, "sink")

    source_sink = Enum.YLeaf(3, "source-sink")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
        return meta._meta_table['OduPrbsMode']


class OduPrbsPattern(Enum):
    """
    OduPrbsPattern (Enum Class)

    Odu prbs pattern

    .. data:: pn_none = 0

    	PNNONE

    .. data:: pn31 = 1

    	PN31

    .. data:: pn23 = 2

    	PN23

    .. data:: pn11 = 4

    	PN11

    .. data:: inverted_pn31 = 8

    	INVERTED PN31

    .. data:: inverted_pn11 = 16

    	INVERTED PN11

    """

    pn_none = Enum.YLeaf(0, "pn-none")

    pn31 = Enum.YLeaf(1, "pn31")

    pn23 = Enum.YLeaf(2, "pn23")

    pn11 = Enum.YLeaf(4, "pn11")

    inverted_pn31 = Enum.YLeaf(8, "inverted-pn31")

    inverted_pn11 = Enum.YLeaf(16, "inverted-pn11")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
        return meta._meta_table['OduPrbsPattern']


class OduPrbsStatus(Enum):
    """
    OduPrbsStatus (Enum Class)

    Odu prbs status

    .. data:: locked = 0

    	Locked

    .. data:: unlocked = 1

    	Unlocked

    .. data:: not_applicable = 2

    	Not Applicable

    """

    locked = Enum.YLeaf(0, "locked")

    unlocked = Enum.YLeaf(1, "unlocked")

    not_applicable = Enum.YLeaf(2, "not-applicable")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
        return meta._meta_table['OduPrbsStatus']


class OduPrbsTest(Enum):
    """
    OduPrbsTest (Enum Class)

    Odu prbs test

    .. data:: disable = 0

    	Disable

    .. data:: enable = 1

    	Enable

    """

    disable = Enum.YLeaf(0, "disable")

    enable = Enum.YLeaf(1, "enable")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
        return meta._meta_table['OduPrbsTest']


class OduPtTypeEt(Enum):
    """
    OduPtTypeEt (Enum Class)

    Odu pt type et

    .. data:: na = 0

    	NA

    .. data:: two_asynchronous_cbr_mapping = 2

    	02 (Asynchronous CBR mapping)

    .. data:: three_bit_synchronous_cbr_mapping = 3

    	03 (Bit synchronous CBR mapping)

    .. data:: five_gfp_mapping = 5

    	05 (GFP mapping)

    .. data:: six_virtual_concatenated_signal = 6

    	06 (Virtual Concatenated Signal)

    .. data:: seven_pcs_codeword_transparent_ethernet_mapping = 7

    	07 (PCS codeword transparent Ethernet mapping)

    .. data:: nine_gfp_mapping_into_opu2 = 9

    	09 (GFP mapping into OPU2)

    .. data:: zero_astm1_mapping_into_opu0 = 10

    	0A (STM1 mapping into OPU0)

    .. data:: zero_bstm4_mapping_into_opu0 = 11

    	0B (STM4 mapping into OPU0)

    .. data:: twenty_odu_multiplex_structure_supporting_odt_ujk = 32

    	20 (ODU multiplex structure supporting ODTUjk)

    .. data:: twenty_one_odu_multiplex_structure_supporting_odt_ujk_and_odt_ukts = 33

    	21 (ODU multiplex structure supporting ODTUjk

    	and ODTUk.ts)

    """

    na = Enum.YLeaf(0, "na")

    two_asynchronous_cbr_mapping = Enum.YLeaf(2, "two-asynchronous-cbr-mapping")

    three_bit_synchronous_cbr_mapping = Enum.YLeaf(3, "three-bit-synchronous-cbr-mapping")

    five_gfp_mapping = Enum.YLeaf(5, "five-gfp-mapping")

    six_virtual_concatenated_signal = Enum.YLeaf(6, "six-virtual-concatenated-signal")

    seven_pcs_codeword_transparent_ethernet_mapping = Enum.YLeaf(7, "seven-pcs-codeword-transparent-ethernet-mapping")

    nine_gfp_mapping_into_opu2 = Enum.YLeaf(9, "nine-gfp-mapping-into-opu2")

    zero_astm1_mapping_into_opu0 = Enum.YLeaf(10, "zero-astm1-mapping-into-opu0")

    zero_bstm4_mapping_into_opu0 = Enum.YLeaf(11, "zero-bstm4-mapping-into-opu0")

    twenty_odu_multiplex_structure_supporting_odt_ujk = Enum.YLeaf(32, "twenty-odu-multiplex-structure-supporting-odt-ujk")

    twenty_one_odu_multiplex_structure_supporting_odt_ujk_and_odt_ukts = Enum.YLeaf(33, "twenty-one-odu-multiplex-structure-supporting-odt-ujk-and-odt-ukts")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
        return meta._meta_table['OduPtTypeEt']


class OduResourceEt(Enum):
    """
    OduResourceEt (Enum Class)

    Odu resource et

    .. data:: resource_free = 0

    	ODU Resource Free

    .. data:: open_connection = 1

    	ODU Open Connection

    .. data:: cross_connection = 2

    	ODU Cross Connection

    .. data:: channelized = 3

    	ODU Channelized

    .. data:: loopbacked = 4

    	ODU Loopbacked

    .. data:: cross_connected_and_loopbacked = 5

    	ODU Cross Connection and Loopbacked

    .. data:: terminated = 6

    	ODU Terminated

    .. data:: invalid = 7

    	ODU Invalid

    """

    resource_free = Enum.YLeaf(0, "resource-free")

    open_connection = Enum.YLeaf(1, "open-connection")

    cross_connection = Enum.YLeaf(2, "cross-connection")

    channelized = Enum.YLeaf(3, "channelized")

    loopbacked = Enum.YLeaf(4, "loopbacked")

    cross_connected_and_loopbacked = Enum.YLeaf(5, "cross-connected-and-loopbacked")

    terminated = Enum.YLeaf(6, "terminated")

    invalid = Enum.YLeaf(7, "invalid")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
        return meta._meta_table['OduResourceEt']


class OduSecState(Enum):
    """
    OduSecState (Enum Class)

    Odu sec state

    .. data:: normal = 0

    	Normal

    .. data:: maintenance = 1

    	Maintenance

    .. data:: ains = 2

    	Automatic In Service

    """

    normal = Enum.YLeaf(0, "normal")

    maintenance = Enum.YLeaf(1, "maintenance")

    ains = Enum.YLeaf(2, "ains")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
        return meta._meta_table['OduSecState']


class OduStateEt(Enum):
    """
    OduStateEt (Enum Class)

    Odu state et

    .. data:: not_ready = 0

    	Not Ready

    .. data:: admin_down = 1

    	Admin Down

    .. data:: down = 2

    	Down

    .. data:: up = 3

    	Up

    .. data:: shutdown = 4

    	Shutdown

    .. data:: error_disable = 5

    	Error Disable

    .. data:: down_immediate = 6

    	Down Immediate

    .. data:: down_immediate_admin = 7

    	Down Immediate Admin

    .. data:: down_graceful = 8

    	Down Graceful

    .. data:: begin_shutdown = 9

    	Begin Shutdown

    .. data:: end_shutdown = 10

    	End Shutdown

    .. data:: begin_error_disable = 11

    	Begin Error Disable

    .. data:: end_error_disable = 12

    	End Error Disable

    .. data:: begin_down_graceful = 13

    	Begin Down Graceful

    .. data:: reset = 14

    	Reset

    .. data:: operational = 15

    	Operational

    .. data:: not_operational = 16

    	Not Operational

    .. data:: unknown = 17

    	Unknown

    .. data:: last = 18

    	Last

    """

    not_ready = Enum.YLeaf(0, "not-ready")

    admin_down = Enum.YLeaf(1, "admin-down")

    down = Enum.YLeaf(2, "down")

    up = Enum.YLeaf(3, "up")

    shutdown = Enum.YLeaf(4, "shutdown")

    error_disable = Enum.YLeaf(5, "error-disable")

    down_immediate = Enum.YLeaf(6, "down-immediate")

    down_immediate_admin = Enum.YLeaf(7, "down-immediate-admin")

    down_graceful = Enum.YLeaf(8, "down-graceful")

    begin_shutdown = Enum.YLeaf(9, "begin-shutdown")

    end_shutdown = Enum.YLeaf(10, "end-shutdown")

    begin_error_disable = Enum.YLeaf(11, "begin-error-disable")

    end_error_disable = Enum.YLeaf(12, "end-error-disable")

    begin_down_graceful = Enum.YLeaf(13, "begin-down-graceful")

    reset = Enum.YLeaf(14, "reset")

    operational = Enum.YLeaf(15, "operational")

    not_operational = Enum.YLeaf(16, "not-operational")

    unknown = Enum.YLeaf(17, "unknown")

    last = Enum.YLeaf(18, "last")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
        return meta._meta_table['OduStateEt']


class OduTcmMode(Enum):
    """
    OduTcmMode (Enum Class)

    Odu tcm mode

    .. data:: odu_tcm_mode_trans_parent = 0

    	Transparent

    .. data:: nim = 1

    	Non-Intrusive Monitor

    .. data:: oper = 2

    	Operational

    """

    odu_tcm_mode_trans_parent = Enum.YLeaf(0, "odu-tcm-mode-trans-parent")

    nim = Enum.YLeaf(1, "nim")

    oper = Enum.YLeaf(2, "oper")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
        return meta._meta_table['OduTcmMode']


class OduTcmPerMon(Enum):
    """
    OduTcmPerMon (Enum Class)

    Odu tcm per mon

    .. data:: disable = 0

    	Disable

    .. data:: enable = 1

    	Enable

    """

    disable = Enum.YLeaf(0, "disable")

    enable = Enum.YLeaf(1, "enable")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
        return meta._meta_table['OduTcmPerMon']


class OduTcmStateEt(Enum):
    """
    OduTcmStateEt (Enum Class)

    Odu tcm state et

    .. data:: disable = 0

    	Disable

    .. data:: enable = 1

    	Enable

    """

    disable = Enum.YLeaf(0, "disable")

    enable = Enum.YLeaf(1, "enable")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
        return meta._meta_table['OduTcmStateEt']


class OduTsGEt(Enum):
    """
    OduTsGEt (Enum Class)

    Odu ts g et

    .. data:: one_dot_two_five_g = 0

    	1.25G

    .. data:: two_dot_five_g = 1

    	2.5G

    .. data:: tsg_not_applicable = 2

    	NA

    """

    one_dot_two_five_g = Enum.YLeaf(0, "one-dot-two-five-g")

    two_dot_five_g = Enum.YLeaf(1, "two-dot-five-g")

    tsg_not_applicable = Enum.YLeaf(2, "tsg-not-applicable")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
        return meta._meta_table['OduTsGEt']


class OduTtiEt(Enum):
    """
    OduTtiEt (Enum Class)

    Odu tti et

    .. data:: ascii = 0

    	ASCII

    .. data:: hex = 1

    	HEX

    .. data:: full_ascii = 2

    	FULL ASCII

    .. data:: full_hex = 3

    	FULL HEX

    """

    ascii = Enum.YLeaf(0, "ascii")

    hex = Enum.YLeaf(1, "hex")

    full_ascii = Enum.YLeaf(2, "full-ascii")

    full_hex = Enum.YLeaf(3, "full-hex")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
        return meta._meta_table['OduTtiEt']


class OduUserEt(Enum):
    """
    OduUserEt (Enum Class)

    Odu user et

    .. data:: mp = 0

    	MP

    .. data:: gmpls = 1

    	GMPLS

    .. data:: all = 2

    	All

    """

    mp = Enum.YLeaf(0, "mp")

    gmpls = Enum.YLeaf(1, "gmpls")

    all = Enum.YLeaf(2, "all")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
        return meta._meta_table['OduUserEt']


class OtmMplsLibC(Enum):
    """
    OtmMplsLibC (Enum Class)

    Otm mpls lib c

    .. data:: otm_mpls_lib_c_type_null = 0

    	NULL

    .. data:: otm_mpls_lib_c_type_ipv4 = 1

    	IPV4

    .. data:: otm_mpls_lib_c_type_ipv4_p2p_tunnel = 7

    	IPV4 P2P TUNNEL

    .. data:: otm_mpls_lib_c_type_ipv6_p2p_tunnel = 8

    	IPV6 P2P TUNNEL

    .. data:: otm_mpls_lib_c_type_ipv4_uni = 9

    	IPV4 UNI

    .. data:: otm_mpls_lib_c_type_ipv4_p2mp_tunnel = 13

    	IPV4 P2MP TUNNEL

    .. data:: otm_mpls_lib_c_type_ipv6_p2mp_tunnel = 14

    	IPV6 P2MP TUNNEL

    .. data:: otm_mpls_lib_c_type_ipv4_tp_tunnel = 15

    	IPV4 TP TUNNEL

    .. data:: otm_mpls_lib_c_type_ipv6_tp_tunnel = 16

    	IPV6 TP TUNNEL

    """

    otm_mpls_lib_c_type_null = Enum.YLeaf(0, "otm-mpls-lib-c-type-null")

    otm_mpls_lib_c_type_ipv4 = Enum.YLeaf(1, "otm-mpls-lib-c-type-ipv4")

    otm_mpls_lib_c_type_ipv4_p2p_tunnel = Enum.YLeaf(7, "otm-mpls-lib-c-type-ipv4-p2p-tunnel")

    otm_mpls_lib_c_type_ipv6_p2p_tunnel = Enum.YLeaf(8, "otm-mpls-lib-c-type-ipv6-p2p-tunnel")

    otm_mpls_lib_c_type_ipv4_uni = Enum.YLeaf(9, "otm-mpls-lib-c-type-ipv4-uni")

    otm_mpls_lib_c_type_ipv4_p2mp_tunnel = Enum.YLeaf(13, "otm-mpls-lib-c-type-ipv4-p2mp-tunnel")

    otm_mpls_lib_c_type_ipv6_p2mp_tunnel = Enum.YLeaf(14, "otm-mpls-lib-c-type-ipv6-p2mp-tunnel")

    otm_mpls_lib_c_type_ipv4_tp_tunnel = Enum.YLeaf(15, "otm-mpls-lib-c-type-ipv4-tp-tunnel")

    otm_mpls_lib_c_type_ipv6_tp_tunnel = Enum.YLeaf(16, "otm-mpls-lib-c-type-ipv6-tp-tunnel")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
        return meta._meta_table['OtmMplsLibC']


class OtmOpticalRmCtxt(Enum):
    """
    OtmOpticalRmCtxt (Enum Class)

    Otm optical rm ctxt

    .. data:: otm_opt_rm_ctxt_type_none = 0

    	NONE

    .. data:: otm_opt_rm_ctxt_type_down_stream_rw_add = 1

    	DOWNSTREAM RW ADD

    .. data:: otm_opt_rm_ctxt_type_up_stream_rw_add = 2

    	UPSTREAM RW ADD

    .. data:: otm_opt_rm_ctxt_type_down_stream_rw_del = 3

    	DOWNSTREAM RW DEL

    .. data:: otm_opt_rm_ctxt_type_up_stream_rw_del = 4

    	UPSTREAM RW DEL

    .. data:: otm_opt_rm_ctxt_type_down_stream_lbl_get = 5

    	DOWNSTREAM LBL GET

    .. data:: otm_opt_rm_ctxt_type_up_stream_lbl_get = 6

    	UPSTREAM LBL GET

    .. data:: otm_opt_rm_ctxt_type_down_stream_lbl_rel = 7

    	DOWNSTREAM LBL REL

    .. data:: otm_opt_rm_ctxt_type_up_stream_lbl_rel = 8

    	UPSTREAM LBL REL

    .. data:: otm_opt_rm_ctxt_type_end_point_rw_add = 9

    	ENDPOINT RW ADD

    .. data:: otm_opt_rm_ctxt_type_end_point_rw_del = 10

    	ENDPOINT RW DEL

    .. data:: otm_opt_rm_ctxt_type_odu_group_add = 11

    	ODU GROUP ADD

    .. data:: otm_opt_rm_ctxt_type_odu_group_del = 12

    	ODU GROUP DEL

    .. data:: otm_optical_rm_ctxt_type_last = 13

    	LAST

    """

    otm_opt_rm_ctxt_type_none = Enum.YLeaf(0, "otm-opt-rm-ctxt-type-none")

    otm_opt_rm_ctxt_type_down_stream_rw_add = Enum.YLeaf(1, "otm-opt-rm-ctxt-type-down-stream-rw-add")

    otm_opt_rm_ctxt_type_up_stream_rw_add = Enum.YLeaf(2, "otm-opt-rm-ctxt-type-up-stream-rw-add")

    otm_opt_rm_ctxt_type_down_stream_rw_del = Enum.YLeaf(3, "otm-opt-rm-ctxt-type-down-stream-rw-del")

    otm_opt_rm_ctxt_type_up_stream_rw_del = Enum.YLeaf(4, "otm-opt-rm-ctxt-type-up-stream-rw-del")

    otm_opt_rm_ctxt_type_down_stream_lbl_get = Enum.YLeaf(5, "otm-opt-rm-ctxt-type-down-stream-lbl-get")

    otm_opt_rm_ctxt_type_up_stream_lbl_get = Enum.YLeaf(6, "otm-opt-rm-ctxt-type-up-stream-lbl-get")

    otm_opt_rm_ctxt_type_down_stream_lbl_rel = Enum.YLeaf(7, "otm-opt-rm-ctxt-type-down-stream-lbl-rel")

    otm_opt_rm_ctxt_type_up_stream_lbl_rel = Enum.YLeaf(8, "otm-opt-rm-ctxt-type-up-stream-lbl-rel")

    otm_opt_rm_ctxt_type_end_point_rw_add = Enum.YLeaf(9, "otm-opt-rm-ctxt-type-end-point-rw-add")

    otm_opt_rm_ctxt_type_end_point_rw_del = Enum.YLeaf(10, "otm-opt-rm-ctxt-type-end-point-rw-del")

    otm_opt_rm_ctxt_type_odu_group_add = Enum.YLeaf(11, "otm-opt-rm-ctxt-type-odu-group-add")

    otm_opt_rm_ctxt_type_odu_group_del = Enum.YLeaf(12, "otm-opt-rm-ctxt-type-odu-group-del")

    otm_optical_rm_ctxt_type_last = Enum.YLeaf(13, "otm-optical-rm-ctxt-type-last")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
        return meta._meta_table['OtmOpticalRmCtxt']


class OtmOpticalRmCtxtRm(Enum):
    """
    OtmOpticalRmCtxtRm (Enum Class)

    Otm optical rm ctxt rm

    .. data:: otm_opt_rm_ctxt_rm_none = 0

    	NONE

    .. data:: otm_opt_rm_ctxt_rm_wdm = 1

    	WDM

    .. data:: otm_opt_rm_ctxt_rm_fsc = 2

    	FSC

    .. data:: otm_opt_rm_ctxt_rm_tdm = 3

    	TDM

    .. data:: otm_opt_rm_ctxt_rm_g709_otn = 4

    	G709 OTN

    .. data:: otm_optical_rm_ctxt_rm_last = 5

    	LAST

    """

    otm_opt_rm_ctxt_rm_none = Enum.YLeaf(0, "otm-opt-rm-ctxt-rm-none")

    otm_opt_rm_ctxt_rm_wdm = Enum.YLeaf(1, "otm-opt-rm-ctxt-rm-wdm")

    otm_opt_rm_ctxt_rm_fsc = Enum.YLeaf(2, "otm-opt-rm-ctxt-rm-fsc")

    otm_opt_rm_ctxt_rm_tdm = Enum.YLeaf(3, "otm-opt-rm-ctxt-rm-tdm")

    otm_opt_rm_ctxt_rm_g709_otn = Enum.YLeaf(4, "otm-opt-rm-ctxt-rm-g709-otn")

    otm_optical_rm_ctxt_rm_last = Enum.YLeaf(5, "otm-optical-rm-ctxt-rm-last")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
        return meta._meta_table['OtmOpticalRmCtxtRm']


class OtmTeTunnelInfo(Enum):
    """
    OtmTeTunnelInfo (Enum Class)

    Otm te tunnel info

    .. data:: otm_te_info_none = 0

    	NONE

    .. data:: otm_te_info_s2l = 1

    	S2L

    .. data:: otm_te_info_tunnel_id = 2

    	ID

    .. data:: otm_te_info_passive_match = 3

    	MAT

    """

    otm_te_info_none = Enum.YLeaf(0, "otm-te-info-none")

    otm_te_info_s2l = Enum.YLeaf(1, "otm-te-info-s2l")

    otm_te_info_tunnel_id = Enum.YLeaf(2, "otm-te-info-tunnel-id")

    otm_te_info_passive_match = Enum.YLeaf(3, "otm-te-info-passive-match")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
        return meta._meta_table['OtmTeTunnelInfo']



class Odu(_Entity_):
    """
    ODU operational data
    
    .. attribute:: controllers
    
    	All ODU Port operational data
    	**type**\:  :py:class:`Controllers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers>`
    
    	**config**\: False
    
    

    """

    _prefix = 'controller-odu-oper'
    _revision = '2015-11-09'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(Odu, self).__init__()
        self._top_entity = None

        self.yang_name = "odu"
        self.yang_parent_name = "Cisco-IOS-XR-controller-odu-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("controllers", ("controllers", Odu.Controllers))])
        self._leafs = OrderedDict()

        self.controllers = Odu.Controllers()
        self.controllers.parent = self
        self._children_name_map["controllers"] = "controllers"
        self._segment_path = lambda: "Cisco-IOS-XR-controller-odu-oper:odu"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Odu, [], name, value)


    class Controllers(_Entity_):
        """
        All ODU Port operational data
        
        .. attribute:: controller
        
        	ODU Port operational data
        	**type**\: list of  		 :py:class:`Controller <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller>`
        
        	**config**\: False
        
        

        """

        _prefix = 'controller-odu-oper'
        _revision = '2015-11-09'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Odu.Controllers, self).__init__()

            self.yang_name = "controllers"
            self.yang_parent_name = "odu"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("controller", ("controller", Odu.Controllers.Controller))])
            self._leafs = OrderedDict()

            self.controller = YList(self)
            self._segment_path = lambda: "controllers"
            self._absolute_path = lambda: "Cisco-IOS-XR-controller-odu-oper:odu/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Odu.Controllers, [], name, value)


        class Controller(_Entity_):
            """
            ODU Port operational data
            
            .. attribute:: controller_name  (key)
            
            	Port name
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
            
            	**config**\: False
            
            .. attribute:: prbs
            
            	ODU port operational data
            	**type**\:  :py:class:`Prbs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Prbs>`
            
            	**config**\: False
            
            .. attribute:: info
            
            	ODU port operational data
            	**type**\:  :py:class:`Info <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info>`
            
            	**config**\: False
            
            

            """

            _prefix = 'controller-odu-oper'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Odu.Controllers.Controller, self).__init__()

                self.yang_name = "controller"
                self.yang_parent_name = "controllers"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['controller_name']
                self._child_classes = OrderedDict([("prbs", ("prbs", Odu.Controllers.Controller.Prbs)), ("info", ("info", Odu.Controllers.Controller.Info))])
                self._leafs = OrderedDict([
                    ('controller_name', (YLeaf(YType.str, 'controller-name'), ['str'])),
                ])
                self.controller_name = None

                self.prbs = Odu.Controllers.Controller.Prbs()
                self.prbs.parent = self
                self._children_name_map["prbs"] = "prbs"

                self.info = Odu.Controllers.Controller.Info()
                self.info.parent = self
                self._children_name_map["info"] = "info"
                self._segment_path = lambda: "controller" + "[controller-name='" + str(self.controller_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-controller-odu-oper:odu/controllers/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Odu.Controllers.Controller, ['controller_name'], name, value)


            class Prbs(_Entity_):
                """
                ODU port operational data
                
                .. attribute:: odu_prbs_test
                
                	odu prbs test
                	**type**\:  :py:class:`OduPrbsTest <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.OduPrbsTest>`
                
                	**config**\: False
                
                .. attribute:: odu_prbs_mode
                
                	odu prbs mode
                	**type**\:  :py:class:`OduPrbsMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.OduPrbsMode>`
                
                	**config**\: False
                
                .. attribute:: odu_prbs_pattern
                
                	odu prbs pattern
                	**type**\:  :py:class:`OduPrbsPattern <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.OduPrbsPattern>`
                
                	**config**\: False
                
                .. attribute:: odu_prbs_status
                
                	odu prbs status
                	**type**\:  :py:class:`OduPrbsStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.OduPrbsStatus>`
                
                	**config**\: False
                
                

                """

                _prefix = 'controller-odu-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Odu.Controllers.Controller.Prbs, self).__init__()

                    self.yang_name = "prbs"
                    self.yang_parent_name = "controller"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('odu_prbs_test', (YLeaf(YType.enumeration, 'odu-prbs-test'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper', 'OduPrbsTest', '')])),
                        ('odu_prbs_mode', (YLeaf(YType.enumeration, 'odu-prbs-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper', 'OduPrbsMode', '')])),
                        ('odu_prbs_pattern', (YLeaf(YType.enumeration, 'odu-prbs-pattern'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper', 'OduPrbsPattern', '')])),
                        ('odu_prbs_status', (YLeaf(YType.enumeration, 'odu-prbs-status'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper', 'OduPrbsStatus', '')])),
                    ])
                    self.odu_prbs_test = None
                    self.odu_prbs_mode = None
                    self.odu_prbs_pattern = None
                    self.odu_prbs_status = None
                    self._segment_path = lambda: "prbs"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Odu.Controllers.Controller.Prbs, ['odu_prbs_test', 'odu_prbs_mode', 'odu_prbs_pattern', 'odu_prbs_status'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                    return meta._meta_table['Odu.Controllers.Controller.Prbs']['meta_info']


            class Info(_Entity_):
                """
                ODU port operational data
                
                .. attribute:: local
                
                	TTI
                	**type**\:  :py:class:`Local <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.Local>`
                
                	**config**\: False
                
                .. attribute:: remote
                
                	Remote
                	**type**\:  :py:class:`Remote <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.Remote>`
                
                	**config**\: False
                
                .. attribute:: tti_mode
                
                	TTI
                	**type**\:  :py:class:`TtiMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.TtiMode>`
                
                	**config**\: False
                
                .. attribute:: odu_fwd_ref
                
                	ODU fwd\_ref 
                	**type**\:  :py:class:`OduFwdRef <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.OduFwdRef>`
                
                	**config**\: False
                
                .. attribute:: alarm
                
                	Alarm
                	**type**\:  :py:class:`Alarm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.Alarm>`
                
                	**config**\: False
                
                .. attribute:: te_ctx_data
                
                	Label Get Data
                	**type**\:  :py:class:`TeCtxData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.TeCtxData>`
                
                	**config**\: False
                
                .. attribute:: xc_add_ctx_data
                
                	Xconnect Add Data
                	**type**\:  :py:class:`XcAddCtxData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.XcAddCtxData>`
                
                	**config**\: False
                
                .. attribute:: xc_rem_ctx_data
                
                	Xconnect Remove Data
                	**type**\:  :py:class:`XcRemCtxData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.XcRemCtxData>`
                
                	**config**\: False
                
                .. attribute:: odu_delay
                
                	ODU Delay
                	**type**\:  :py:class:`OduDelay <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.OduDelay>`
                
                	**config**\: False
                
                .. attribute:: odu_terminate_ether
                
                	odu terminate ether
                	**type**\:  :py:class:`OduTerminateEther <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.OduTerminateEther>`
                
                	**config**\: False
                
                .. attribute:: ains_info
                
                	AINS information
                	**type**\:  :py:class:`AinsInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.AinsInfo>`
                
                	**config**\: False
                
                .. attribute:: state
                
                	Admin State
                	**type**\:  :py:class:`OduStateEt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.OduStateEt>`
                
                	**config**\: False
                
                .. attribute:: sf
                
                	SF in the form of 1.0E \- <SF>
                	**type**\: int
                
                	**range:** 0..255
                
                	**config**\: False
                
                .. attribute:: sd
                
                	SD in the form of 1.0E \- <SD>
                	**type**\: int
                
                	**range:** 0..255
                
                	**config**\: False
                
                .. attribute:: loopback_mode
                
                	Loopback
                	**type**\:  :py:class:`OduLoopBackMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.OduLoopBackMode>`
                
                	**config**\: False
                
                .. attribute:: derived_mode
                
                	Derived State
                	**type**\:  :py:class:`OduDerState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.OduDerState>`
                
                	**config**\: False
                
                .. attribute:: inherit_sec_state
                
                	Sec State 
                	**type**\:  :py:class:`OduSecState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.OduSecState>`
                
                	**config**\: False
                
                .. attribute:: config_sec_state
                
                	Sec State 
                	**type**\:  :py:class:`OduSecState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.OduSecState>`
                
                	**config**\: False
                
                .. attribute:: gcc_mode
                
                	ODU GCC
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: child_name
                
                	Child Name
                	**type**\: str
                
                	**length:** 0..64
                
                	**config**\: False
                
                .. attribute:: max_odu_child
                
                	ODU maximum no of children
                	**type**\: int
                
                	**range:** 0..255
                
                	**config**\: False
                
                .. attribute:: od_uuser
                
                	 ODU User
                	**type**\:  :py:class:`OduUserEt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.OduUserEt>`
                
                	**config**\: False
                
                .. attribute:: resource_state
                
                	Resource State
                	**type**\:  :py:class:`OduResourceEt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.OduResourceEt>`
                
                	**config**\: False
                
                .. attribute:: pt_type
                
                	PT type
                	**type**\:  :py:class:`OduPtTypeEt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.OduPtTypeEt>`
                
                	**config**\: False
                
                .. attribute:: flex_type
                
                	FLEX type
                	**type**\:  :py:class:`OduFlexTypeEt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.OduFlexTypeEt>`
                
                	**config**\: False
                
                .. attribute:: flex_bw
                
                	FLEX bw
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: flex_tolerence
                
                	FLEX tolerence
                	**type**\: int
                
                	**range:** 0..65535
                
                	**config**\: False
                
                .. attribute:: option
                
                	Option
                	**type**\: int
                
                	**range:** 0..255
                
                	**config**\: False
                
                .. attribute:: tpn_value
                
                	TPN
                	**type**\: int
                
                	**range:** 0..255
                
                	**config**\: False
                
                .. attribute:: num_ts
                
                	Number of TS
                	**type**\: int
                
                	**range:** 0..255
                
                	**config**\: False
                
                .. attribute:: ts_g
                
                	TS Granuality
                	**type**\:  :py:class:`OduTsGEt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.OduTsGEt>`
                
                	**config**\: False
                
                .. attribute:: ts_b
                
                	child ts bitmap
                	**type**\: str
                
                	**length:** 0..256
                
                	**config**\: False
                
                .. attribute:: tpn_b
                
                	tpn bitmap
                	**type**\: str
                
                	**length:** 0..256
                
                	**config**\: False
                
                .. attribute:: pts_b
                
                	ts bitmap
                	**type**\: str
                
                	**length:** 0..256
                
                	**config**\: False
                
                .. attribute:: fwd_ref
                
                	fwd ref
                	**type**\: str
                
                	**length:** 0..64
                
                	**config**\: False
                
                .. attribute:: xc_id
                
                	Xconnect ID
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: xconnect_name
                
                	Xconnect Name
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: fwd_ref_ifhandle
                
                	fwd\_ref ifhandle
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: no_parent_slot
                
                	Number of parent slot
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: xc_resp_code
                
                	Odu Xconnect Response code
                	**type**\:  :py:class:`DpProgrammed <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.DpProgrammed>`
                
                	**config**\: False
                
                .. attribute:: performance_monitoring
                
                	Performance Monitoring
                	**type**\:  :py:class:`OduPerMon <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.OduPerMon>`
                
                	**config**\: False
                
                .. attribute:: pmtimca
                
                	PM TIM\-CA state
                	**type**\:  :py:class:`OduPmCaEt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.OduPmCaEt>`
                
                	**config**\: False
                
                .. attribute:: pm_mode
                
                	ODU PM Mode
                	**type**\:  :py:class:`OduPmMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.OduPmMode>`
                
                	**config**\: False
                
                .. attribute:: nv_optical_support
                
                	NV Optical support
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: gmpls_tti_mode
                
                	tti mode
                	**type**\:  :py:class:`GmplsTtiMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.GmplsTtiMode>`
                
                	**config**\: False
                
                .. attribute:: gmpls_tcm_id
                
                	tcm id
                	**type**\: int
                
                	**range:** 0..255
                
                	**config**\: False
                
                .. attribute:: odu
                
                	Child Ts
                	**type**\: list of  		 :py:class:`Odu_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.Odu_>`
                
                	**config**\: False
                
                .. attribute:: odutcm
                
                	ODU TCM
                	**type**\: list of  		 :py:class:`Odutcm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.Odutcm>`
                
                	**config**\: False
                
                

                """

                _prefix = 'controller-odu-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Odu.Controllers.Controller.Info, self).__init__()

                    self.yang_name = "info"
                    self.yang_parent_name = "controller"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("local", ("local", Odu.Controllers.Controller.Info.Local)), ("remote", ("remote", Odu.Controllers.Controller.Info.Remote)), ("tti-mode", ("tti_mode", Odu.Controllers.Controller.Info.TtiMode)), ("odu-fwd-ref", ("odu_fwd_ref", Odu.Controllers.Controller.Info.OduFwdRef)), ("alarm", ("alarm", Odu.Controllers.Controller.Info.Alarm)), ("te-ctx-data", ("te_ctx_data", Odu.Controllers.Controller.Info.TeCtxData)), ("xc-add-ctx-data", ("xc_add_ctx_data", Odu.Controllers.Controller.Info.XcAddCtxData)), ("xc-rem-ctx-data", ("xc_rem_ctx_data", Odu.Controllers.Controller.Info.XcRemCtxData)), ("odu-delay", ("odu_delay", Odu.Controllers.Controller.Info.OduDelay)), ("odu-terminate-ether", ("odu_terminate_ether", Odu.Controllers.Controller.Info.OduTerminateEther)), ("ains-info", ("ains_info", Odu.Controllers.Controller.Info.AinsInfo)), ("odu", ("odu", Odu.Controllers.Controller.Info.Odu_)), ("odutcm", ("odutcm", Odu.Controllers.Controller.Info.Odutcm))])
                    self._leafs = OrderedDict([
                        ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper', 'OduStateEt', '')])),
                        ('sf', (YLeaf(YType.uint8, 'sf'), ['int'])),
                        ('sd', (YLeaf(YType.uint8, 'sd'), ['int'])),
                        ('loopback_mode', (YLeaf(YType.enumeration, 'loopback-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper', 'OduLoopBackMode', '')])),
                        ('derived_mode', (YLeaf(YType.enumeration, 'derived-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper', 'OduDerState', '')])),
                        ('inherit_sec_state', (YLeaf(YType.enumeration, 'inherit-sec-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper', 'OduSecState', '')])),
                        ('config_sec_state', (YLeaf(YType.enumeration, 'config-sec-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper', 'OduSecState', '')])),
                        ('gcc_mode', (YLeaf(YType.boolean, 'gcc-mode'), ['bool'])),
                        ('child_name', (YLeaf(YType.str, 'child-name'), ['str'])),
                        ('max_odu_child', (YLeaf(YType.uint8, 'max-odu-child'), ['int'])),
                        ('od_uuser', (YLeaf(YType.enumeration, 'od-uuser'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper', 'OduUserEt', '')])),
                        ('resource_state', (YLeaf(YType.enumeration, 'resource-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper', 'OduResourceEt', '')])),
                        ('pt_type', (YLeaf(YType.enumeration, 'pt-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper', 'OduPtTypeEt', '')])),
                        ('flex_type', (YLeaf(YType.enumeration, 'flex-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper', 'OduFlexTypeEt', '')])),
                        ('flex_bw', (YLeaf(YType.uint32, 'flex-bw'), ['int'])),
                        ('flex_tolerence', (YLeaf(YType.uint16, 'flex-tolerence'), ['int'])),
                        ('option', (YLeaf(YType.uint8, 'option'), ['int'])),
                        ('tpn_value', (YLeaf(YType.uint8, 'tpn-value'), ['int'])),
                        ('num_ts', (YLeaf(YType.uint8, 'num-ts'), ['int'])),
                        ('ts_g', (YLeaf(YType.enumeration, 'ts-g'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper', 'OduTsGEt', '')])),
                        ('ts_b', (YLeaf(YType.str, 'ts-b'), ['str'])),
                        ('tpn_b', (YLeaf(YType.str, 'tpn-b'), ['str'])),
                        ('pts_b', (YLeaf(YType.str, 'pts-b'), ['str'])),
                        ('fwd_ref', (YLeaf(YType.str, 'fwd-ref'), ['str'])),
                        ('xc_id', (YLeaf(YType.uint32, 'xc-id'), ['int'])),
                        ('xconnect_name', (YLeaf(YType.str, 'xconnect-name'), ['str'])),
                        ('fwd_ref_ifhandle', (YLeaf(YType.uint32, 'fwd-ref-ifhandle'), ['int'])),
                        ('no_parent_slot', (YLeaf(YType.uint32, 'no-parent-slot'), ['int'])),
                        ('xc_resp_code', (YLeaf(YType.enumeration, 'xc-resp-code'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper', 'DpProgrammed', '')])),
                        ('performance_monitoring', (YLeaf(YType.enumeration, 'performance-monitoring'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper', 'OduPerMon', '')])),
                        ('pmtimca', (YLeaf(YType.enumeration, 'pmtimca'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper', 'OduPmCaEt', '')])),
                        ('pm_mode', (YLeaf(YType.enumeration, 'pm-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper', 'OduPmMode', '')])),
                        ('nv_optical_support', (YLeaf(YType.boolean, 'nv-optical-support'), ['bool'])),
                        ('gmpls_tti_mode', (YLeaf(YType.enumeration, 'gmpls-tti-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper', 'GmplsTtiMode', '')])),
                        ('gmpls_tcm_id', (YLeaf(YType.uint8, 'gmpls-tcm-id'), ['int'])),
                    ])
                    self.state = None
                    self.sf = None
                    self.sd = None
                    self.loopback_mode = None
                    self.derived_mode = None
                    self.inherit_sec_state = None
                    self.config_sec_state = None
                    self.gcc_mode = None
                    self.child_name = None
                    self.max_odu_child = None
                    self.od_uuser = None
                    self.resource_state = None
                    self.pt_type = None
                    self.flex_type = None
                    self.flex_bw = None
                    self.flex_tolerence = None
                    self.option = None
                    self.tpn_value = None
                    self.num_ts = None
                    self.ts_g = None
                    self.ts_b = None
                    self.tpn_b = None
                    self.pts_b = None
                    self.fwd_ref = None
                    self.xc_id = None
                    self.xconnect_name = None
                    self.fwd_ref_ifhandle = None
                    self.no_parent_slot = None
                    self.xc_resp_code = None
                    self.performance_monitoring = None
                    self.pmtimca = None
                    self.pm_mode = None
                    self.nv_optical_support = None
                    self.gmpls_tti_mode = None
                    self.gmpls_tcm_id = None

                    self.local = Odu.Controllers.Controller.Info.Local()
                    self.local.parent = self
                    self._children_name_map["local"] = "local"

                    self.remote = Odu.Controllers.Controller.Info.Remote()
                    self.remote.parent = self
                    self._children_name_map["remote"] = "remote"

                    self.tti_mode = Odu.Controllers.Controller.Info.TtiMode()
                    self.tti_mode.parent = self
                    self._children_name_map["tti_mode"] = "tti-mode"

                    self.odu_fwd_ref = Odu.Controllers.Controller.Info.OduFwdRef()
                    self.odu_fwd_ref.parent = self
                    self._children_name_map["odu_fwd_ref"] = "odu-fwd-ref"

                    self.alarm = Odu.Controllers.Controller.Info.Alarm()
                    self.alarm.parent = self
                    self._children_name_map["alarm"] = "alarm"

                    self.te_ctx_data = Odu.Controllers.Controller.Info.TeCtxData()
                    self.te_ctx_data.parent = self
                    self._children_name_map["te_ctx_data"] = "te-ctx-data"

                    self.xc_add_ctx_data = Odu.Controllers.Controller.Info.XcAddCtxData()
                    self.xc_add_ctx_data.parent = self
                    self._children_name_map["xc_add_ctx_data"] = "xc-add-ctx-data"

                    self.xc_rem_ctx_data = Odu.Controllers.Controller.Info.XcRemCtxData()
                    self.xc_rem_ctx_data.parent = self
                    self._children_name_map["xc_rem_ctx_data"] = "xc-rem-ctx-data"

                    self.odu_delay = Odu.Controllers.Controller.Info.OduDelay()
                    self.odu_delay.parent = self
                    self._children_name_map["odu_delay"] = "odu-delay"

                    self.odu_terminate_ether = Odu.Controllers.Controller.Info.OduTerminateEther()
                    self.odu_terminate_ether.parent = self
                    self._children_name_map["odu_terminate_ether"] = "odu-terminate-ether"

                    self.ains_info = Odu.Controllers.Controller.Info.AinsInfo()
                    self.ains_info.parent = self
                    self._children_name_map["ains_info"] = "ains-info"

                    self.odu = YList(self)
                    self.odutcm = YList(self)
                    self._segment_path = lambda: "info"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Odu.Controllers.Controller.Info, ['state', 'sf', 'sd', 'loopback_mode', 'derived_mode', 'inherit_sec_state', 'config_sec_state', 'gcc_mode', 'child_name', 'max_odu_child', 'od_uuser', 'resource_state', 'pt_type', 'flex_type', 'flex_bw', 'flex_tolerence', 'option', 'tpn_value', 'num_ts', 'ts_g', 'ts_b', 'tpn_b', 'pts_b', 'fwd_ref', 'xc_id', 'xconnect_name', 'fwd_ref_ifhandle', 'no_parent_slot', 'xc_resp_code', 'performance_monitoring', 'pmtimca', 'pm_mode', 'nv_optical_support', 'gmpls_tti_mode', 'gmpls_tcm_id'], name, value)


                class Local(_Entity_):
                    """
                    TTI
                    
                    .. attribute:: router_id
                    
                    	Router ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: if_index
                    
                    	IfIndex
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'controller-odu-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Odu.Controllers.Controller.Info.Local, self).__init__()

                        self.yang_name = "local"
                        self.yang_parent_name = "info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('router_id', (YLeaf(YType.uint32, 'router-id'), ['int'])),
                            ('if_index', (YLeaf(YType.uint32, 'if-index'), ['int'])),
                        ])
                        self.router_id = None
                        self.if_index = None
                        self._segment_path = lambda: "local"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Odu.Controllers.Controller.Info.Local, ['router_id', 'if_index'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                        return meta._meta_table['Odu.Controllers.Controller.Info.Local']['meta_info']


                class Remote(_Entity_):
                    """
                    Remote
                    
                    .. attribute:: router_id
                    
                    	Router ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: if_index
                    
                    	IfIndex
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'controller-odu-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Odu.Controllers.Controller.Info.Remote, self).__init__()

                        self.yang_name = "remote"
                        self.yang_parent_name = "info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('router_id', (YLeaf(YType.uint32, 'router-id'), ['int'])),
                            ('if_index', (YLeaf(YType.uint32, 'if-index'), ['int'])),
                        ])
                        self.router_id = None
                        self.if_index = None
                        self._segment_path = lambda: "remote"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Odu.Controllers.Controller.Info.Remote, ['router_id', 'if_index'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                        return meta._meta_table['Odu.Controllers.Controller.Info.Remote']['meta_info']


                class TtiMode(_Entity_):
                    """
                    TTI
                    
                    .. attribute:: tx
                    
                    	String Sent
                    	**type**\:  :py:class:`Tx <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.TtiMode.Tx>`
                    
                    	**config**\: False
                    
                    .. attribute:: exp
                    
                    	String Expected
                    	**type**\:  :py:class:`Exp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.TtiMode.Exp>`
                    
                    	**config**\: False
                    
                    .. attribute:: rec
                    
                    	String Received
                    	**type**\:  :py:class:`Rec <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.TtiMode.Rec>`
                    
                    	**config**\: False
                    
                    .. attribute:: g709tti_sent_mode
                    
                    	G709TTI Sent
                    	**type**\:  :py:class:`OduTtiEt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.OduTtiEt>`
                    
                    	**config**\: False
                    
                    .. attribute:: g709tti_exp_mode
                    
                    	G709TTI Expected
                    	**type**\:  :py:class:`OduTtiEt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.OduTtiEt>`
                    
                    	**config**\: False
                    
                    .. attribute:: g709tti_rec_mode
                    
                    	G709TTI Recieved
                    	**type**\:  :py:class:`OduTtiEt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.OduTtiEt>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'controller-odu-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Odu.Controllers.Controller.Info.TtiMode, self).__init__()

                        self.yang_name = "tti-mode"
                        self.yang_parent_name = "info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("tx", ("tx", Odu.Controllers.Controller.Info.TtiMode.Tx)), ("exp", ("exp", Odu.Controllers.Controller.Info.TtiMode.Exp)), ("rec", ("rec", Odu.Controllers.Controller.Info.TtiMode.Rec))])
                        self._leafs = OrderedDict([
                            ('g709tti_sent_mode', (YLeaf(YType.enumeration, 'g709tti-sent-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper', 'OduTtiEt', '')])),
                            ('g709tti_exp_mode', (YLeaf(YType.enumeration, 'g709tti-exp-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper', 'OduTtiEt', '')])),
                            ('g709tti_rec_mode', (YLeaf(YType.enumeration, 'g709tti-rec-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper', 'OduTtiEt', '')])),
                        ])
                        self.g709tti_sent_mode = None
                        self.g709tti_exp_mode = None
                        self.g709tti_rec_mode = None

                        self.tx = Odu.Controllers.Controller.Info.TtiMode.Tx()
                        self.tx.parent = self
                        self._children_name_map["tx"] = "tx"

                        self.exp = Odu.Controllers.Controller.Info.TtiMode.Exp()
                        self.exp.parent = self
                        self._children_name_map["exp"] = "exp"

                        self.rec = Odu.Controllers.Controller.Info.TtiMode.Rec()
                        self.rec.parent = self
                        self._children_name_map["rec"] = "rec"
                        self._segment_path = lambda: "tti-mode"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Odu.Controllers.Controller.Info.TtiMode, ['g709tti_sent_mode', 'g709tti_exp_mode', 'g709tti_rec_mode'], name, value)


                    class Tx(_Entity_):
                        """
                        String Sent
                        
                        .. attribute:: sapi
                        
                        	tx String
                        	**type**\: list of int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: dapi
                        
                        	exp String
                        	**type**\: list of int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: operator_specific
                        
                        	rec String
                        	**type**\: list of int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-odu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Odu.Controllers.Controller.Info.TtiMode.Tx, self).__init__()

                            self.yang_name = "tx"
                            self.yang_parent_name = "tti-mode"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('sapi', (YLeafList(YType.uint8, 'sapi'), ['int'])),
                                ('dapi', (YLeafList(YType.uint8, 'dapi'), ['int'])),
                                ('operator_specific', (YLeafList(YType.uint8, 'operator-specific'), ['int'])),
                            ])
                            self.sapi = []
                            self.dapi = []
                            self.operator_specific = []
                            self._segment_path = lambda: "tx"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Odu.Controllers.Controller.Info.TtiMode.Tx, ['sapi', 'dapi', 'operator_specific'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                            return meta._meta_table['Odu.Controllers.Controller.Info.TtiMode.Tx']['meta_info']


                    class Exp(_Entity_):
                        """
                        String Expected
                        
                        .. attribute:: sapi
                        
                        	tx String
                        	**type**\: list of int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: dapi
                        
                        	exp String
                        	**type**\: list of int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: operator_specific
                        
                        	rec String
                        	**type**\: list of int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-odu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Odu.Controllers.Controller.Info.TtiMode.Exp, self).__init__()

                            self.yang_name = "exp"
                            self.yang_parent_name = "tti-mode"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('sapi', (YLeafList(YType.uint8, 'sapi'), ['int'])),
                                ('dapi', (YLeafList(YType.uint8, 'dapi'), ['int'])),
                                ('operator_specific', (YLeafList(YType.uint8, 'operator-specific'), ['int'])),
                            ])
                            self.sapi = []
                            self.dapi = []
                            self.operator_specific = []
                            self._segment_path = lambda: "exp"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Odu.Controllers.Controller.Info.TtiMode.Exp, ['sapi', 'dapi', 'operator_specific'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                            return meta._meta_table['Odu.Controllers.Controller.Info.TtiMode.Exp']['meta_info']


                    class Rec(_Entity_):
                        """
                        String Received
                        
                        .. attribute:: sapi
                        
                        	tx String
                        	**type**\: list of int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: dapi
                        
                        	exp String
                        	**type**\: list of int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: operator_specific
                        
                        	rec String
                        	**type**\: list of int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-odu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Odu.Controllers.Controller.Info.TtiMode.Rec, self).__init__()

                            self.yang_name = "rec"
                            self.yang_parent_name = "tti-mode"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('sapi', (YLeafList(YType.uint8, 'sapi'), ['int'])),
                                ('dapi', (YLeafList(YType.uint8, 'dapi'), ['int'])),
                                ('operator_specific', (YLeafList(YType.uint8, 'operator-specific'), ['int'])),
                            ])
                            self.sapi = []
                            self.dapi = []
                            self.operator_specific = []
                            self._segment_path = lambda: "rec"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Odu.Controllers.Controller.Info.TtiMode.Rec, ['sapi', 'dapi', 'operator_specific'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                            return meta._meta_table['Odu.Controllers.Controller.Info.TtiMode.Rec']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                        return meta._meta_table['Odu.Controllers.Controller.Info.TtiMode']['meta_info']


                class OduFwdRef(_Entity_):
                    """
                    ODU fwd\_ref 
                    
                    .. attribute:: od_uuser
                    
                    	 ODU User
                    	**type**\:  :py:class:`OduUserEt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.OduUserEt>`
                    
                    	**config**\: False
                    
                    .. attribute:: resource_state
                    
                    	Resource State
                    	**type**\:  :py:class:`OduResourceEt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.OduResourceEt>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'controller-odu-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Odu.Controllers.Controller.Info.OduFwdRef, self).__init__()

                        self.yang_name = "odu-fwd-ref"
                        self.yang_parent_name = "info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('od_uuser', (YLeaf(YType.enumeration, 'od-uuser'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper', 'OduUserEt', '')])),
                            ('resource_state', (YLeaf(YType.enumeration, 'resource-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper', 'OduResourceEt', '')])),
                        ])
                        self.od_uuser = None
                        self.resource_state = None
                        self._segment_path = lambda: "odu-fwd-ref"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Odu.Controllers.Controller.Info.OduFwdRef, ['od_uuser', 'resource_state'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                        return meta._meta_table['Odu.Controllers.Controller.Info.OduFwdRef']['meta_info']


                class Alarm(_Entity_):
                    """
                    Alarm
                    
                    .. attribute:: oci
                    
                    	Open Connection Indiction
                    	**type**\:  :py:class:`Oci <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.Alarm.Oci>`
                    
                    	**config**\: False
                    
                    .. attribute:: ais
                    
                    	Alarm Indication Signal
                    	**type**\:  :py:class:`Ais <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.Alarm.Ais>`
                    
                    	**config**\: False
                    
                    .. attribute:: lck
                    
                    	Upstream Connection Locked
                    	**type**\:  :py:class:`Lck <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.Alarm.Lck>`
                    
                    	**config**\: False
                    
                    .. attribute:: bdi
                    
                    	Backward Defect Indication
                    	**type**\:  :py:class:`Bdi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.Alarm.Bdi>`
                    
                    	**config**\: False
                    
                    .. attribute:: eoc
                    
                    	GCC End of Channel
                    	**type**\:  :py:class:`Eoc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.Alarm.Eoc>`
                    
                    	**config**\: False
                    
                    .. attribute:: ptim
                    
                    	Payload Type Identifier Mismatch
                    	**type**\:  :py:class:`Ptim <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.Alarm.Ptim>`
                    
                    	**config**\: False
                    
                    .. attribute:: tim
                    
                    	Trace Identifier Mismatch information
                    	**type**\:  :py:class:`Tim <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.Alarm.Tim>`
                    
                    	**config**\: False
                    
                    .. attribute:: iae
                    
                    	Incoming Alignment Error
                    	**type**\:  :py:class:`Iae <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.Alarm.Iae>`
                    
                    	**config**\: False
                    
                    .. attribute:: biae
                    
                    	Backward Incoming Alignment Error
                    	**type**\:  :py:class:`Biae <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.Alarm.Biae>`
                    
                    	**config**\: False
                    
                    .. attribute:: sf_ber
                    
                    	SF BER alarm
                    	**type**\:  :py:class:`SfBer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.Alarm.SfBer>`
                    
                    	**config**\: False
                    
                    .. attribute:: sd_ber
                    
                    	SD BER alarm
                    	**type**\:  :py:class:`SdBer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.Alarm.SdBer>`
                    
                    	**config**\: False
                    
                    .. attribute:: csf
                    
                    	Client Signal Failure
                    	**type**\:  :py:class:`Csf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.Alarm.Csf>`
                    
                    	**config**\: False
                    
                    .. attribute:: tcm1_ais
                    
                    	TCM1 Alarm Indication Signal
                    	**type**\:  :py:class:`Tcm1Ais <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.Alarm.Tcm1Ais>`
                    
                    	**config**\: False
                    
                    .. attribute:: tcm1_ltc
                    
                    	TCM1 Loss of Tandem connection Monitoring
                    	**type**\:  :py:class:`Tcm1Ltc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.Alarm.Tcm1Ltc>`
                    
                    	**config**\: False
                    
                    .. attribute:: tcm1_oci
                    
                    	TCM1 Open Connection Indiction
                    	**type**\:  :py:class:`Tcm1Oci <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.Alarm.Tcm1Oci>`
                    
                    	**config**\: False
                    
                    .. attribute:: tcm1_lck
                    
                    	TCM1  Upstream Connection Locked
                    	**type**\:  :py:class:`Tcm1Lck <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.Alarm.Tcm1Lck>`
                    
                    	**config**\: False
                    
                    .. attribute:: tcm1_iae
                    
                    	TCM1 Incoming Alignment Error
                    	**type**\:  :py:class:`Tcm1Iae <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.Alarm.Tcm1Iae>`
                    
                    	**config**\: False
                    
                    .. attribute:: tcm1_biae
                    
                    	TCM1 Backward Incoming Alignment Error
                    	**type**\:  :py:class:`Tcm1Biae <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.Alarm.Tcm1Biae>`
                    
                    	**config**\: False
                    
                    .. attribute:: tcm1_bdi
                    
                    	TCM1 Backward Defect Monitoring
                    	**type**\:  :py:class:`Tcm1Bdi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.Alarm.Tcm1Bdi>`
                    
                    	**config**\: False
                    
                    .. attribute:: tcm1_tim
                    
                    	TCM1 Trail Trace Identifier Mismatch 
                    	**type**\:  :py:class:`Tcm1Tim <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.Alarm.Tcm1Tim>`
                    
                    	**config**\: False
                    
                    .. attribute:: tcm1_sf_ber
                    
                    	TCM1 SF BER alarm
                    	**type**\:  :py:class:`Tcm1SfBer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.Alarm.Tcm1SfBer>`
                    
                    	**config**\: False
                    
                    .. attribute:: tcm1_sd_ber
                    
                    	TCM1 SD BER alarm
                    	**type**\:  :py:class:`Tcm1SdBer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.Alarm.Tcm1SdBer>`
                    
                    	**config**\: False
                    
                    .. attribute:: tcm2_ais
                    
                    	TCM2 Alarm Indication Signal
                    	**type**\:  :py:class:`Tcm2Ais <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.Alarm.Tcm2Ais>`
                    
                    	**config**\: False
                    
                    .. attribute:: tcm2_ltc
                    
                    	TCM2 Loss of Tandem connection Monitoring
                    	**type**\:  :py:class:`Tcm2Ltc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.Alarm.Tcm2Ltc>`
                    
                    	**config**\: False
                    
                    .. attribute:: tcm2_oci
                    
                    	TCM2 Open Connection Indiction
                    	**type**\:  :py:class:`Tcm2Oci <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.Alarm.Tcm2Oci>`
                    
                    	**config**\: False
                    
                    .. attribute:: tcm2_lck
                    
                    	TCM2  Upstream Connection Locked
                    	**type**\:  :py:class:`Tcm2Lck <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.Alarm.Tcm2Lck>`
                    
                    	**config**\: False
                    
                    .. attribute:: tcm2_iae
                    
                    	TCM2 Incoming Alignment Error
                    	**type**\:  :py:class:`Tcm2Iae <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.Alarm.Tcm2Iae>`
                    
                    	**config**\: False
                    
                    .. attribute:: tcm2_biae
                    
                    	TCM2 Backward Incoming Alignment Error
                    	**type**\:  :py:class:`Tcm2Biae <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.Alarm.Tcm2Biae>`
                    
                    	**config**\: False
                    
                    .. attribute:: tcm2_bdi
                    
                    	TCM2 Backward Defect Monitoring
                    	**type**\:  :py:class:`Tcm2Bdi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.Alarm.Tcm2Bdi>`
                    
                    	**config**\: False
                    
                    .. attribute:: tcm2_tim
                    
                    	TCM2 Trail Trace Identifier Mismatch 
                    	**type**\:  :py:class:`Tcm2Tim <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.Alarm.Tcm2Tim>`
                    
                    	**config**\: False
                    
                    .. attribute:: tcm2_sf_ber
                    
                    	TCM2 SF BER alarm
                    	**type**\:  :py:class:`Tcm2SfBer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.Alarm.Tcm2SfBer>`
                    
                    	**config**\: False
                    
                    .. attribute:: tcm2_sd_ber
                    
                    	TCM2 SD BER alarm
                    	**type**\:  :py:class:`Tcm2SdBer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.Alarm.Tcm2SdBer>`
                    
                    	**config**\: False
                    
                    .. attribute:: tcm3_ais
                    
                    	TCM3 Alarm Indication Signal
                    	**type**\:  :py:class:`Tcm3Ais <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.Alarm.Tcm3Ais>`
                    
                    	**config**\: False
                    
                    .. attribute:: tcm3_ltc
                    
                    	TCM3 Loss of Tandem connection Monitoring
                    	**type**\:  :py:class:`Tcm3Ltc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.Alarm.Tcm3Ltc>`
                    
                    	**config**\: False
                    
                    .. attribute:: tcm3_oci
                    
                    	TCM3 Open Connection Indiction
                    	**type**\:  :py:class:`Tcm3Oci <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.Alarm.Tcm3Oci>`
                    
                    	**config**\: False
                    
                    .. attribute:: tcm3_lck
                    
                    	TCM3  Upstream Connection Locked
                    	**type**\:  :py:class:`Tcm3Lck <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.Alarm.Tcm3Lck>`
                    
                    	**config**\: False
                    
                    .. attribute:: tcm3_iae
                    
                    	TCM3 Incoming Alignment Error
                    	**type**\:  :py:class:`Tcm3Iae <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.Alarm.Tcm3Iae>`
                    
                    	**config**\: False
                    
                    .. attribute:: tcm3_biae
                    
                    	TCM3 Backward Incoming Alignment Error
                    	**type**\:  :py:class:`Tcm3Biae <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.Alarm.Tcm3Biae>`
                    
                    	**config**\: False
                    
                    .. attribute:: tcm3_bdi
                    
                    	TCM3 Backward Defect Monitoring
                    	**type**\:  :py:class:`Tcm3Bdi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.Alarm.Tcm3Bdi>`
                    
                    	**config**\: False
                    
                    .. attribute:: tcm3_tim
                    
                    	TCM3 Trail Trace Identifier Mismatch 
                    	**type**\:  :py:class:`Tcm3Tim <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.Alarm.Tcm3Tim>`
                    
                    	**config**\: False
                    
                    .. attribute:: tcm3_sf_ber
                    
                    	TCM3 SF BER alarm
                    	**type**\:  :py:class:`Tcm3SfBer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.Alarm.Tcm3SfBer>`
                    
                    	**config**\: False
                    
                    .. attribute:: tcm3_sd_ber
                    
                    	TCM3 SD BER alarm
                    	**type**\:  :py:class:`Tcm3SdBer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.Alarm.Tcm3SdBer>`
                    
                    	**config**\: False
                    
                    .. attribute:: tcm4_ais
                    
                    	TCM4 Alarm Indication Signal
                    	**type**\:  :py:class:`Tcm4Ais <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.Alarm.Tcm4Ais>`
                    
                    	**config**\: False
                    
                    .. attribute:: tcm4_ltc
                    
                    	TCM4 Loss of Tandem connection Monitoring
                    	**type**\:  :py:class:`Tcm4Ltc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.Alarm.Tcm4Ltc>`
                    
                    	**config**\: False
                    
                    .. attribute:: tcm4_oci
                    
                    	TCM4 Open Connection Indiction
                    	**type**\:  :py:class:`Tcm4Oci <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.Alarm.Tcm4Oci>`
                    
                    	**config**\: False
                    
                    .. attribute:: tcm4_lck
                    
                    	TCM4  Upstream Connection Locked
                    	**type**\:  :py:class:`Tcm4Lck <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.Alarm.Tcm4Lck>`
                    
                    	**config**\: False
                    
                    .. attribute:: tcm4_iae
                    
                    	TCM4 Incoming Alignment Error
                    	**type**\:  :py:class:`Tcm4Iae <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.Alarm.Tcm4Iae>`
                    
                    	**config**\: False
                    
                    .. attribute:: tcm4_biae
                    
                    	TCM4 Backward Incoming Alignment Error
                    	**type**\:  :py:class:`Tcm4Biae <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.Alarm.Tcm4Biae>`
                    
                    	**config**\: False
                    
                    .. attribute:: tcm4_bdi
                    
                    	TCM4 Backward Defect Monitoring
                    	**type**\:  :py:class:`Tcm4Bdi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.Alarm.Tcm4Bdi>`
                    
                    	**config**\: False
                    
                    .. attribute:: tcm4_tim
                    
                    	TCM4 Trail Trace Identifier Mismatch 
                    	**type**\:  :py:class:`Tcm4Tim <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.Alarm.Tcm4Tim>`
                    
                    	**config**\: False
                    
                    .. attribute:: tcm4_sf_ber
                    
                    	TCM4 SF BER alarm
                    	**type**\:  :py:class:`Tcm4SfBer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.Alarm.Tcm4SfBer>`
                    
                    	**config**\: False
                    
                    .. attribute:: tcm4_sd_ber
                    
                    	TCM4 SD BER alarm
                    	**type**\:  :py:class:`Tcm4SdBer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.Alarm.Tcm4SdBer>`
                    
                    	**config**\: False
                    
                    .. attribute:: tcm5_ais
                    
                    	TCM5 Alarm Indication Signal
                    	**type**\:  :py:class:`Tcm5Ais <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.Alarm.Tcm5Ais>`
                    
                    	**config**\: False
                    
                    .. attribute:: tcm5_ltc
                    
                    	TCM5 Loss of Tandem connection Monitoring
                    	**type**\:  :py:class:`Tcm5Ltc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.Alarm.Tcm5Ltc>`
                    
                    	**config**\: False
                    
                    .. attribute:: tcm5_oci
                    
                    	TCM5 Open Connection Indiction
                    	**type**\:  :py:class:`Tcm5Oci <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.Alarm.Tcm5Oci>`
                    
                    	**config**\: False
                    
                    .. attribute:: tcm5_lck
                    
                    	TCM5  Upstream Connection Locked
                    	**type**\:  :py:class:`Tcm5Lck <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.Alarm.Tcm5Lck>`
                    
                    	**config**\: False
                    
                    .. attribute:: tcm5_iae
                    
                    	TCM5 Incoming Alignment Error
                    	**type**\:  :py:class:`Tcm5Iae <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.Alarm.Tcm5Iae>`
                    
                    	**config**\: False
                    
                    .. attribute:: tcm5_biae
                    
                    	TCM5 Backward Incoming Alignment Error
                    	**type**\:  :py:class:`Tcm5Biae <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.Alarm.Tcm5Biae>`
                    
                    	**config**\: False
                    
                    .. attribute:: tcm5_bdi
                    
                    	TCM5 Backward Defect Monitoring
                    	**type**\:  :py:class:`Tcm5Bdi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.Alarm.Tcm5Bdi>`
                    
                    	**config**\: False
                    
                    .. attribute:: tcm5_tim
                    
                    	TCM5 Trail Trace Identifier Mismatch 
                    	**type**\:  :py:class:`Tcm5Tim <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.Alarm.Tcm5Tim>`
                    
                    	**config**\: False
                    
                    .. attribute:: tcm5_sf_ber
                    
                    	TCM5 SF BER alarm
                    	**type**\:  :py:class:`Tcm5SfBer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.Alarm.Tcm5SfBer>`
                    
                    	**config**\: False
                    
                    .. attribute:: tcm5_sd_ber
                    
                    	TCM5 SD BER alarm
                    	**type**\:  :py:class:`Tcm5SdBer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.Alarm.Tcm5SdBer>`
                    
                    	**config**\: False
                    
                    .. attribute:: tcm6_ais
                    
                    	TCM6 Alarm Indication Signal
                    	**type**\:  :py:class:`Tcm6Ais <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.Alarm.Tcm6Ais>`
                    
                    	**config**\: False
                    
                    .. attribute:: tcm6_ltc
                    
                    	TCM6 Loss of Tandem connection Monitoring
                    	**type**\:  :py:class:`Tcm6Ltc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.Alarm.Tcm6Ltc>`
                    
                    	**config**\: False
                    
                    .. attribute:: tcm6_oci
                    
                    	TCM6 Open Connection Indiction
                    	**type**\:  :py:class:`Tcm6Oci <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.Alarm.Tcm6Oci>`
                    
                    	**config**\: False
                    
                    .. attribute:: tcm6_lck
                    
                    	TCM6  Upstream Connection Locked
                    	**type**\:  :py:class:`Tcm6Lck <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.Alarm.Tcm6Lck>`
                    
                    	**config**\: False
                    
                    .. attribute:: tcm6_iae
                    
                    	TCM6 Incoming Alignment Error
                    	**type**\:  :py:class:`Tcm6Iae <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.Alarm.Tcm6Iae>`
                    
                    	**config**\: False
                    
                    .. attribute:: tcm6_biae
                    
                    	TCM6 Backward Incoming Alignment Error
                    	**type**\:  :py:class:`Tcm6Biae <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.Alarm.Tcm6Biae>`
                    
                    	**config**\: False
                    
                    .. attribute:: tcm6_bdi
                    
                    	TCM6 Backward Defect Monitoring
                    	**type**\:  :py:class:`Tcm6Bdi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.Alarm.Tcm6Bdi>`
                    
                    	**config**\: False
                    
                    .. attribute:: tcm6_tim
                    
                    	TCM6 Trail Trace Identifier Mismatch 
                    	**type**\:  :py:class:`Tcm6Tim <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.Alarm.Tcm6Tim>`
                    
                    	**config**\: False
                    
                    .. attribute:: tcm6_sf_ber
                    
                    	TCM6 SF BER alarm
                    	**type**\:  :py:class:`Tcm6SfBer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.Alarm.Tcm6SfBer>`
                    
                    	**config**\: False
                    
                    .. attribute:: tcm6_sd_ber
                    
                    	TCM6 SD BER alarm
                    	**type**\:  :py:class:`Tcm6SdBer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.Alarm.Tcm6SdBer>`
                    
                    	**config**\: False
                    
                    .. attribute:: gfp_lfd
                    
                    	Loss Of Frame Delineation
                    	**type**\:  :py:class:`GfpLfd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.Alarm.GfpLfd>`
                    
                    	**config**\: False
                    
                    .. attribute:: gfp_locs
                    
                    	Loss Of Client Signal
                    	**type**\:  :py:class:`GfpLocs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.Alarm.GfpLocs>`
                    
                    	**config**\: False
                    
                    .. attribute:: gfp_loccs
                    
                    	Loss Of Character Synchronization
                    	**type**\:  :py:class:`GfpLoccs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.Alarm.GfpLoccs>`
                    
                    	**config**\: False
                    
                    .. attribute:: gfp_upm
                    
                    	User Payload Mismatch
                    	**type**\:  :py:class:`GfpUpm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.Alarm.GfpUpm>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'controller-odu-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Odu.Controllers.Controller.Info.Alarm, self).__init__()

                        self.yang_name = "alarm"
                        self.yang_parent_name = "info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("oci", ("oci", Odu.Controllers.Controller.Info.Alarm.Oci)), ("ais", ("ais", Odu.Controllers.Controller.Info.Alarm.Ais)), ("lck", ("lck", Odu.Controllers.Controller.Info.Alarm.Lck)), ("bdi", ("bdi", Odu.Controllers.Controller.Info.Alarm.Bdi)), ("eoc", ("eoc", Odu.Controllers.Controller.Info.Alarm.Eoc)), ("ptim", ("ptim", Odu.Controllers.Controller.Info.Alarm.Ptim)), ("tim", ("tim", Odu.Controllers.Controller.Info.Alarm.Tim)), ("iae", ("iae", Odu.Controllers.Controller.Info.Alarm.Iae)), ("biae", ("biae", Odu.Controllers.Controller.Info.Alarm.Biae)), ("sf-ber", ("sf_ber", Odu.Controllers.Controller.Info.Alarm.SfBer)), ("sd-ber", ("sd_ber", Odu.Controllers.Controller.Info.Alarm.SdBer)), ("csf", ("csf", Odu.Controllers.Controller.Info.Alarm.Csf)), ("tcm1-ais", ("tcm1_ais", Odu.Controllers.Controller.Info.Alarm.Tcm1Ais)), ("tcm1-ltc", ("tcm1_ltc", Odu.Controllers.Controller.Info.Alarm.Tcm1Ltc)), ("tcm1-oci", ("tcm1_oci", Odu.Controllers.Controller.Info.Alarm.Tcm1Oci)), ("tcm1-lck", ("tcm1_lck", Odu.Controllers.Controller.Info.Alarm.Tcm1Lck)), ("tcm1-iae", ("tcm1_iae", Odu.Controllers.Controller.Info.Alarm.Tcm1Iae)), ("tcm1-biae", ("tcm1_biae", Odu.Controllers.Controller.Info.Alarm.Tcm1Biae)), ("tcm1-bdi", ("tcm1_bdi", Odu.Controllers.Controller.Info.Alarm.Tcm1Bdi)), ("tcm1-tim", ("tcm1_tim", Odu.Controllers.Controller.Info.Alarm.Tcm1Tim)), ("tcm1-sf-ber", ("tcm1_sf_ber", Odu.Controllers.Controller.Info.Alarm.Tcm1SfBer)), ("tcm1-sd-ber", ("tcm1_sd_ber", Odu.Controllers.Controller.Info.Alarm.Tcm1SdBer)), ("tcm2-ais", ("tcm2_ais", Odu.Controllers.Controller.Info.Alarm.Tcm2Ais)), ("tcm2-ltc", ("tcm2_ltc", Odu.Controllers.Controller.Info.Alarm.Tcm2Ltc)), ("tcm2-oci", ("tcm2_oci", Odu.Controllers.Controller.Info.Alarm.Tcm2Oci)), ("tcm2-lck", ("tcm2_lck", Odu.Controllers.Controller.Info.Alarm.Tcm2Lck)), ("tcm2-iae", ("tcm2_iae", Odu.Controllers.Controller.Info.Alarm.Tcm2Iae)), ("tcm2-biae", ("tcm2_biae", Odu.Controllers.Controller.Info.Alarm.Tcm2Biae)), ("tcm2-bdi", ("tcm2_bdi", Odu.Controllers.Controller.Info.Alarm.Tcm2Bdi)), ("tcm2-tim", ("tcm2_tim", Odu.Controllers.Controller.Info.Alarm.Tcm2Tim)), ("tcm2-sf-ber", ("tcm2_sf_ber", Odu.Controllers.Controller.Info.Alarm.Tcm2SfBer)), ("tcm2-sd-ber", ("tcm2_sd_ber", Odu.Controllers.Controller.Info.Alarm.Tcm2SdBer)), ("tcm3-ais", ("tcm3_ais", Odu.Controllers.Controller.Info.Alarm.Tcm3Ais)), ("tcm3-ltc", ("tcm3_ltc", Odu.Controllers.Controller.Info.Alarm.Tcm3Ltc)), ("tcm3-oci", ("tcm3_oci", Odu.Controllers.Controller.Info.Alarm.Tcm3Oci)), ("tcm3-lck", ("tcm3_lck", Odu.Controllers.Controller.Info.Alarm.Tcm3Lck)), ("tcm3-iae", ("tcm3_iae", Odu.Controllers.Controller.Info.Alarm.Tcm3Iae)), ("tcm3-biae", ("tcm3_biae", Odu.Controllers.Controller.Info.Alarm.Tcm3Biae)), ("tcm3-bdi", ("tcm3_bdi", Odu.Controllers.Controller.Info.Alarm.Tcm3Bdi)), ("tcm3-tim", ("tcm3_tim", Odu.Controllers.Controller.Info.Alarm.Tcm3Tim)), ("tcm3-sf-ber", ("tcm3_sf_ber", Odu.Controllers.Controller.Info.Alarm.Tcm3SfBer)), ("tcm3-sd-ber", ("tcm3_sd_ber", Odu.Controllers.Controller.Info.Alarm.Tcm3SdBer)), ("tcm4-ais", ("tcm4_ais", Odu.Controllers.Controller.Info.Alarm.Tcm4Ais)), ("tcm4-ltc", ("tcm4_ltc", Odu.Controllers.Controller.Info.Alarm.Tcm4Ltc)), ("tcm4-oci", ("tcm4_oci", Odu.Controllers.Controller.Info.Alarm.Tcm4Oci)), ("tcm4-lck", ("tcm4_lck", Odu.Controllers.Controller.Info.Alarm.Tcm4Lck)), ("tcm4-iae", ("tcm4_iae", Odu.Controllers.Controller.Info.Alarm.Tcm4Iae)), ("tcm4-biae", ("tcm4_biae", Odu.Controllers.Controller.Info.Alarm.Tcm4Biae)), ("tcm4-bdi", ("tcm4_bdi", Odu.Controllers.Controller.Info.Alarm.Tcm4Bdi)), ("tcm4-tim", ("tcm4_tim", Odu.Controllers.Controller.Info.Alarm.Tcm4Tim)), ("tcm4-sf-ber", ("tcm4_sf_ber", Odu.Controllers.Controller.Info.Alarm.Tcm4SfBer)), ("tcm4-sd-ber", ("tcm4_sd_ber", Odu.Controllers.Controller.Info.Alarm.Tcm4SdBer)), ("tcm5-ais", ("tcm5_ais", Odu.Controllers.Controller.Info.Alarm.Tcm5Ais)), ("tcm5-ltc", ("tcm5_ltc", Odu.Controllers.Controller.Info.Alarm.Tcm5Ltc)), ("tcm5-oci", ("tcm5_oci", Odu.Controllers.Controller.Info.Alarm.Tcm5Oci)), ("tcm5-lck", ("tcm5_lck", Odu.Controllers.Controller.Info.Alarm.Tcm5Lck)), ("tcm5-iae", ("tcm5_iae", Odu.Controllers.Controller.Info.Alarm.Tcm5Iae)), ("tcm5-biae", ("tcm5_biae", Odu.Controllers.Controller.Info.Alarm.Tcm5Biae)), ("tcm5-bdi", ("tcm5_bdi", Odu.Controllers.Controller.Info.Alarm.Tcm5Bdi)), ("tcm5-tim", ("tcm5_tim", Odu.Controllers.Controller.Info.Alarm.Tcm5Tim)), ("tcm5-sf-ber", ("tcm5_sf_ber", Odu.Controllers.Controller.Info.Alarm.Tcm5SfBer)), ("tcm5-sd-ber", ("tcm5_sd_ber", Odu.Controllers.Controller.Info.Alarm.Tcm5SdBer)), ("tcm6-ais", ("tcm6_ais", Odu.Controllers.Controller.Info.Alarm.Tcm6Ais)), ("tcm6-ltc", ("tcm6_ltc", Odu.Controllers.Controller.Info.Alarm.Tcm6Ltc)), ("tcm6-oci", ("tcm6_oci", Odu.Controllers.Controller.Info.Alarm.Tcm6Oci)), ("tcm6-lck", ("tcm6_lck", Odu.Controllers.Controller.Info.Alarm.Tcm6Lck)), ("tcm6-iae", ("tcm6_iae", Odu.Controllers.Controller.Info.Alarm.Tcm6Iae)), ("tcm6-biae", ("tcm6_biae", Odu.Controllers.Controller.Info.Alarm.Tcm6Biae)), ("tcm6-bdi", ("tcm6_bdi", Odu.Controllers.Controller.Info.Alarm.Tcm6Bdi)), ("tcm6-tim", ("tcm6_tim", Odu.Controllers.Controller.Info.Alarm.Tcm6Tim)), ("tcm6-sf-ber", ("tcm6_sf_ber", Odu.Controllers.Controller.Info.Alarm.Tcm6SfBer)), ("tcm6-sd-ber", ("tcm6_sd_ber", Odu.Controllers.Controller.Info.Alarm.Tcm6SdBer)), ("gfp-lfd", ("gfp_lfd", Odu.Controllers.Controller.Info.Alarm.GfpLfd)), ("gfp-locs", ("gfp_locs", Odu.Controllers.Controller.Info.Alarm.GfpLocs)), ("gfp-loccs", ("gfp_loccs", Odu.Controllers.Controller.Info.Alarm.GfpLoccs)), ("gfp-upm", ("gfp_upm", Odu.Controllers.Controller.Info.Alarm.GfpUpm))])
                        self._leafs = OrderedDict()

                        self.oci = Odu.Controllers.Controller.Info.Alarm.Oci()
                        self.oci.parent = self
                        self._children_name_map["oci"] = "oci"

                        self.ais = Odu.Controllers.Controller.Info.Alarm.Ais()
                        self.ais.parent = self
                        self._children_name_map["ais"] = "ais"

                        self.lck = Odu.Controllers.Controller.Info.Alarm.Lck()
                        self.lck.parent = self
                        self._children_name_map["lck"] = "lck"

                        self.bdi = Odu.Controllers.Controller.Info.Alarm.Bdi()
                        self.bdi.parent = self
                        self._children_name_map["bdi"] = "bdi"

                        self.eoc = Odu.Controllers.Controller.Info.Alarm.Eoc()
                        self.eoc.parent = self
                        self._children_name_map["eoc"] = "eoc"

                        self.ptim = Odu.Controllers.Controller.Info.Alarm.Ptim()
                        self.ptim.parent = self
                        self._children_name_map["ptim"] = "ptim"

                        self.tim = Odu.Controllers.Controller.Info.Alarm.Tim()
                        self.tim.parent = self
                        self._children_name_map["tim"] = "tim"

                        self.iae = Odu.Controllers.Controller.Info.Alarm.Iae()
                        self.iae.parent = self
                        self._children_name_map["iae"] = "iae"

                        self.biae = Odu.Controllers.Controller.Info.Alarm.Biae()
                        self.biae.parent = self
                        self._children_name_map["biae"] = "biae"

                        self.sf_ber = Odu.Controllers.Controller.Info.Alarm.SfBer()
                        self.sf_ber.parent = self
                        self._children_name_map["sf_ber"] = "sf-ber"

                        self.sd_ber = Odu.Controllers.Controller.Info.Alarm.SdBer()
                        self.sd_ber.parent = self
                        self._children_name_map["sd_ber"] = "sd-ber"

                        self.csf = Odu.Controllers.Controller.Info.Alarm.Csf()
                        self.csf.parent = self
                        self._children_name_map["csf"] = "csf"

                        self.tcm1_ais = Odu.Controllers.Controller.Info.Alarm.Tcm1Ais()
                        self.tcm1_ais.parent = self
                        self._children_name_map["tcm1_ais"] = "tcm1-ais"

                        self.tcm1_ltc = Odu.Controllers.Controller.Info.Alarm.Tcm1Ltc()
                        self.tcm1_ltc.parent = self
                        self._children_name_map["tcm1_ltc"] = "tcm1-ltc"

                        self.tcm1_oci = Odu.Controllers.Controller.Info.Alarm.Tcm1Oci()
                        self.tcm1_oci.parent = self
                        self._children_name_map["tcm1_oci"] = "tcm1-oci"

                        self.tcm1_lck = Odu.Controllers.Controller.Info.Alarm.Tcm1Lck()
                        self.tcm1_lck.parent = self
                        self._children_name_map["tcm1_lck"] = "tcm1-lck"

                        self.tcm1_iae = Odu.Controllers.Controller.Info.Alarm.Tcm1Iae()
                        self.tcm1_iae.parent = self
                        self._children_name_map["tcm1_iae"] = "tcm1-iae"

                        self.tcm1_biae = Odu.Controllers.Controller.Info.Alarm.Tcm1Biae()
                        self.tcm1_biae.parent = self
                        self._children_name_map["tcm1_biae"] = "tcm1-biae"

                        self.tcm1_bdi = Odu.Controllers.Controller.Info.Alarm.Tcm1Bdi()
                        self.tcm1_bdi.parent = self
                        self._children_name_map["tcm1_bdi"] = "tcm1-bdi"

                        self.tcm1_tim = Odu.Controllers.Controller.Info.Alarm.Tcm1Tim()
                        self.tcm1_tim.parent = self
                        self._children_name_map["tcm1_tim"] = "tcm1-tim"

                        self.tcm1_sf_ber = Odu.Controllers.Controller.Info.Alarm.Tcm1SfBer()
                        self.tcm1_sf_ber.parent = self
                        self._children_name_map["tcm1_sf_ber"] = "tcm1-sf-ber"

                        self.tcm1_sd_ber = Odu.Controllers.Controller.Info.Alarm.Tcm1SdBer()
                        self.tcm1_sd_ber.parent = self
                        self._children_name_map["tcm1_sd_ber"] = "tcm1-sd-ber"

                        self.tcm2_ais = Odu.Controllers.Controller.Info.Alarm.Tcm2Ais()
                        self.tcm2_ais.parent = self
                        self._children_name_map["tcm2_ais"] = "tcm2-ais"

                        self.tcm2_ltc = Odu.Controllers.Controller.Info.Alarm.Tcm2Ltc()
                        self.tcm2_ltc.parent = self
                        self._children_name_map["tcm2_ltc"] = "tcm2-ltc"

                        self.tcm2_oci = Odu.Controllers.Controller.Info.Alarm.Tcm2Oci()
                        self.tcm2_oci.parent = self
                        self._children_name_map["tcm2_oci"] = "tcm2-oci"

                        self.tcm2_lck = Odu.Controllers.Controller.Info.Alarm.Tcm2Lck()
                        self.tcm2_lck.parent = self
                        self._children_name_map["tcm2_lck"] = "tcm2-lck"

                        self.tcm2_iae = Odu.Controllers.Controller.Info.Alarm.Tcm2Iae()
                        self.tcm2_iae.parent = self
                        self._children_name_map["tcm2_iae"] = "tcm2-iae"

                        self.tcm2_biae = Odu.Controllers.Controller.Info.Alarm.Tcm2Biae()
                        self.tcm2_biae.parent = self
                        self._children_name_map["tcm2_biae"] = "tcm2-biae"

                        self.tcm2_bdi = Odu.Controllers.Controller.Info.Alarm.Tcm2Bdi()
                        self.tcm2_bdi.parent = self
                        self._children_name_map["tcm2_bdi"] = "tcm2-bdi"

                        self.tcm2_tim = Odu.Controllers.Controller.Info.Alarm.Tcm2Tim()
                        self.tcm2_tim.parent = self
                        self._children_name_map["tcm2_tim"] = "tcm2-tim"

                        self.tcm2_sf_ber = Odu.Controllers.Controller.Info.Alarm.Tcm2SfBer()
                        self.tcm2_sf_ber.parent = self
                        self._children_name_map["tcm2_sf_ber"] = "tcm2-sf-ber"

                        self.tcm2_sd_ber = Odu.Controllers.Controller.Info.Alarm.Tcm2SdBer()
                        self.tcm2_sd_ber.parent = self
                        self._children_name_map["tcm2_sd_ber"] = "tcm2-sd-ber"

                        self.tcm3_ais = Odu.Controllers.Controller.Info.Alarm.Tcm3Ais()
                        self.tcm3_ais.parent = self
                        self._children_name_map["tcm3_ais"] = "tcm3-ais"

                        self.tcm3_ltc = Odu.Controllers.Controller.Info.Alarm.Tcm3Ltc()
                        self.tcm3_ltc.parent = self
                        self._children_name_map["tcm3_ltc"] = "tcm3-ltc"

                        self.tcm3_oci = Odu.Controllers.Controller.Info.Alarm.Tcm3Oci()
                        self.tcm3_oci.parent = self
                        self._children_name_map["tcm3_oci"] = "tcm3-oci"

                        self.tcm3_lck = Odu.Controllers.Controller.Info.Alarm.Tcm3Lck()
                        self.tcm3_lck.parent = self
                        self._children_name_map["tcm3_lck"] = "tcm3-lck"

                        self.tcm3_iae = Odu.Controllers.Controller.Info.Alarm.Tcm3Iae()
                        self.tcm3_iae.parent = self
                        self._children_name_map["tcm3_iae"] = "tcm3-iae"

                        self.tcm3_biae = Odu.Controllers.Controller.Info.Alarm.Tcm3Biae()
                        self.tcm3_biae.parent = self
                        self._children_name_map["tcm3_biae"] = "tcm3-biae"

                        self.tcm3_bdi = Odu.Controllers.Controller.Info.Alarm.Tcm3Bdi()
                        self.tcm3_bdi.parent = self
                        self._children_name_map["tcm3_bdi"] = "tcm3-bdi"

                        self.tcm3_tim = Odu.Controllers.Controller.Info.Alarm.Tcm3Tim()
                        self.tcm3_tim.parent = self
                        self._children_name_map["tcm3_tim"] = "tcm3-tim"

                        self.tcm3_sf_ber = Odu.Controllers.Controller.Info.Alarm.Tcm3SfBer()
                        self.tcm3_sf_ber.parent = self
                        self._children_name_map["tcm3_sf_ber"] = "tcm3-sf-ber"

                        self.tcm3_sd_ber = Odu.Controllers.Controller.Info.Alarm.Tcm3SdBer()
                        self.tcm3_sd_ber.parent = self
                        self._children_name_map["tcm3_sd_ber"] = "tcm3-sd-ber"

                        self.tcm4_ais = Odu.Controllers.Controller.Info.Alarm.Tcm4Ais()
                        self.tcm4_ais.parent = self
                        self._children_name_map["tcm4_ais"] = "tcm4-ais"

                        self.tcm4_ltc = Odu.Controllers.Controller.Info.Alarm.Tcm4Ltc()
                        self.tcm4_ltc.parent = self
                        self._children_name_map["tcm4_ltc"] = "tcm4-ltc"

                        self.tcm4_oci = Odu.Controllers.Controller.Info.Alarm.Tcm4Oci()
                        self.tcm4_oci.parent = self
                        self._children_name_map["tcm4_oci"] = "tcm4-oci"

                        self.tcm4_lck = Odu.Controllers.Controller.Info.Alarm.Tcm4Lck()
                        self.tcm4_lck.parent = self
                        self._children_name_map["tcm4_lck"] = "tcm4-lck"

                        self.tcm4_iae = Odu.Controllers.Controller.Info.Alarm.Tcm4Iae()
                        self.tcm4_iae.parent = self
                        self._children_name_map["tcm4_iae"] = "tcm4-iae"

                        self.tcm4_biae = Odu.Controllers.Controller.Info.Alarm.Tcm4Biae()
                        self.tcm4_biae.parent = self
                        self._children_name_map["tcm4_biae"] = "tcm4-biae"

                        self.tcm4_bdi = Odu.Controllers.Controller.Info.Alarm.Tcm4Bdi()
                        self.tcm4_bdi.parent = self
                        self._children_name_map["tcm4_bdi"] = "tcm4-bdi"

                        self.tcm4_tim = Odu.Controllers.Controller.Info.Alarm.Tcm4Tim()
                        self.tcm4_tim.parent = self
                        self._children_name_map["tcm4_tim"] = "tcm4-tim"

                        self.tcm4_sf_ber = Odu.Controllers.Controller.Info.Alarm.Tcm4SfBer()
                        self.tcm4_sf_ber.parent = self
                        self._children_name_map["tcm4_sf_ber"] = "tcm4-sf-ber"

                        self.tcm4_sd_ber = Odu.Controllers.Controller.Info.Alarm.Tcm4SdBer()
                        self.tcm4_sd_ber.parent = self
                        self._children_name_map["tcm4_sd_ber"] = "tcm4-sd-ber"

                        self.tcm5_ais = Odu.Controllers.Controller.Info.Alarm.Tcm5Ais()
                        self.tcm5_ais.parent = self
                        self._children_name_map["tcm5_ais"] = "tcm5-ais"

                        self.tcm5_ltc = Odu.Controllers.Controller.Info.Alarm.Tcm5Ltc()
                        self.tcm5_ltc.parent = self
                        self._children_name_map["tcm5_ltc"] = "tcm5-ltc"

                        self.tcm5_oci = Odu.Controllers.Controller.Info.Alarm.Tcm5Oci()
                        self.tcm5_oci.parent = self
                        self._children_name_map["tcm5_oci"] = "tcm5-oci"

                        self.tcm5_lck = Odu.Controllers.Controller.Info.Alarm.Tcm5Lck()
                        self.tcm5_lck.parent = self
                        self._children_name_map["tcm5_lck"] = "tcm5-lck"

                        self.tcm5_iae = Odu.Controllers.Controller.Info.Alarm.Tcm5Iae()
                        self.tcm5_iae.parent = self
                        self._children_name_map["tcm5_iae"] = "tcm5-iae"

                        self.tcm5_biae = Odu.Controllers.Controller.Info.Alarm.Tcm5Biae()
                        self.tcm5_biae.parent = self
                        self._children_name_map["tcm5_biae"] = "tcm5-biae"

                        self.tcm5_bdi = Odu.Controllers.Controller.Info.Alarm.Tcm5Bdi()
                        self.tcm5_bdi.parent = self
                        self._children_name_map["tcm5_bdi"] = "tcm5-bdi"

                        self.tcm5_tim = Odu.Controllers.Controller.Info.Alarm.Tcm5Tim()
                        self.tcm5_tim.parent = self
                        self._children_name_map["tcm5_tim"] = "tcm5-tim"

                        self.tcm5_sf_ber = Odu.Controllers.Controller.Info.Alarm.Tcm5SfBer()
                        self.tcm5_sf_ber.parent = self
                        self._children_name_map["tcm5_sf_ber"] = "tcm5-sf-ber"

                        self.tcm5_sd_ber = Odu.Controllers.Controller.Info.Alarm.Tcm5SdBer()
                        self.tcm5_sd_ber.parent = self
                        self._children_name_map["tcm5_sd_ber"] = "tcm5-sd-ber"

                        self.tcm6_ais = Odu.Controllers.Controller.Info.Alarm.Tcm6Ais()
                        self.tcm6_ais.parent = self
                        self._children_name_map["tcm6_ais"] = "tcm6-ais"

                        self.tcm6_ltc = Odu.Controllers.Controller.Info.Alarm.Tcm6Ltc()
                        self.tcm6_ltc.parent = self
                        self._children_name_map["tcm6_ltc"] = "tcm6-ltc"

                        self.tcm6_oci = Odu.Controllers.Controller.Info.Alarm.Tcm6Oci()
                        self.tcm6_oci.parent = self
                        self._children_name_map["tcm6_oci"] = "tcm6-oci"

                        self.tcm6_lck = Odu.Controllers.Controller.Info.Alarm.Tcm6Lck()
                        self.tcm6_lck.parent = self
                        self._children_name_map["tcm6_lck"] = "tcm6-lck"

                        self.tcm6_iae = Odu.Controllers.Controller.Info.Alarm.Tcm6Iae()
                        self.tcm6_iae.parent = self
                        self._children_name_map["tcm6_iae"] = "tcm6-iae"

                        self.tcm6_biae = Odu.Controllers.Controller.Info.Alarm.Tcm6Biae()
                        self.tcm6_biae.parent = self
                        self._children_name_map["tcm6_biae"] = "tcm6-biae"

                        self.tcm6_bdi = Odu.Controllers.Controller.Info.Alarm.Tcm6Bdi()
                        self.tcm6_bdi.parent = self
                        self._children_name_map["tcm6_bdi"] = "tcm6-bdi"

                        self.tcm6_tim = Odu.Controllers.Controller.Info.Alarm.Tcm6Tim()
                        self.tcm6_tim.parent = self
                        self._children_name_map["tcm6_tim"] = "tcm6-tim"

                        self.tcm6_sf_ber = Odu.Controllers.Controller.Info.Alarm.Tcm6SfBer()
                        self.tcm6_sf_ber.parent = self
                        self._children_name_map["tcm6_sf_ber"] = "tcm6-sf-ber"

                        self.tcm6_sd_ber = Odu.Controllers.Controller.Info.Alarm.Tcm6SdBer()
                        self.tcm6_sd_ber.parent = self
                        self._children_name_map["tcm6_sd_ber"] = "tcm6-sd-ber"

                        self.gfp_lfd = Odu.Controllers.Controller.Info.Alarm.GfpLfd()
                        self.gfp_lfd.parent = self
                        self._children_name_map["gfp_lfd"] = "gfp-lfd"

                        self.gfp_locs = Odu.Controllers.Controller.Info.Alarm.GfpLocs()
                        self.gfp_locs.parent = self
                        self._children_name_map["gfp_locs"] = "gfp-locs"

                        self.gfp_loccs = Odu.Controllers.Controller.Info.Alarm.GfpLoccs()
                        self.gfp_loccs.parent = self
                        self._children_name_map["gfp_loccs"] = "gfp-loccs"

                        self.gfp_upm = Odu.Controllers.Controller.Info.Alarm.GfpUpm()
                        self.gfp_upm.parent = self
                        self._children_name_map["gfp_upm"] = "gfp-upm"
                        self._segment_path = lambda: "alarm"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Odu.Controllers.Controller.Info.Alarm, [], name, value)


                    class Oci(_Entity_):
                        """
                        Open Connection Indiction
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-odu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Odu.Controllers.Controller.Info.Alarm.Oci, self).__init__()

                            self.yang_name = "oci"
                            self.yang_parent_name = "alarm"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "oci"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Odu.Controllers.Controller.Info.Alarm.Oci, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                            return meta._meta_table['Odu.Controllers.Controller.Info.Alarm.Oci']['meta_info']


                    class Ais(_Entity_):
                        """
                        Alarm Indication Signal
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-odu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Odu.Controllers.Controller.Info.Alarm.Ais, self).__init__()

                            self.yang_name = "ais"
                            self.yang_parent_name = "alarm"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "ais"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Odu.Controllers.Controller.Info.Alarm.Ais, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                            return meta._meta_table['Odu.Controllers.Controller.Info.Alarm.Ais']['meta_info']


                    class Lck(_Entity_):
                        """
                        Upstream Connection Locked
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-odu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Odu.Controllers.Controller.Info.Alarm.Lck, self).__init__()

                            self.yang_name = "lck"
                            self.yang_parent_name = "alarm"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "lck"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Odu.Controllers.Controller.Info.Alarm.Lck, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                            return meta._meta_table['Odu.Controllers.Controller.Info.Alarm.Lck']['meta_info']


                    class Bdi(_Entity_):
                        """
                        Backward Defect Indication
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-odu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Odu.Controllers.Controller.Info.Alarm.Bdi, self).__init__()

                            self.yang_name = "bdi"
                            self.yang_parent_name = "alarm"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "bdi"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Odu.Controllers.Controller.Info.Alarm.Bdi, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                            return meta._meta_table['Odu.Controllers.Controller.Info.Alarm.Bdi']['meta_info']


                    class Eoc(_Entity_):
                        """
                        GCC End of Channel
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-odu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Odu.Controllers.Controller.Info.Alarm.Eoc, self).__init__()

                            self.yang_name = "eoc"
                            self.yang_parent_name = "alarm"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "eoc"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Odu.Controllers.Controller.Info.Alarm.Eoc, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                            return meta._meta_table['Odu.Controllers.Controller.Info.Alarm.Eoc']['meta_info']


                    class Ptim(_Entity_):
                        """
                        Payload Type Identifier Mismatch
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-odu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Odu.Controllers.Controller.Info.Alarm.Ptim, self).__init__()

                            self.yang_name = "ptim"
                            self.yang_parent_name = "alarm"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "ptim"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Odu.Controllers.Controller.Info.Alarm.Ptim, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                            return meta._meta_table['Odu.Controllers.Controller.Info.Alarm.Ptim']['meta_info']


                    class Tim(_Entity_):
                        """
                        Trace Identifier Mismatch information
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-odu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Odu.Controllers.Controller.Info.Alarm.Tim, self).__init__()

                            self.yang_name = "tim"
                            self.yang_parent_name = "alarm"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "tim"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Odu.Controllers.Controller.Info.Alarm.Tim, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                            return meta._meta_table['Odu.Controllers.Controller.Info.Alarm.Tim']['meta_info']


                    class Iae(_Entity_):
                        """
                        Incoming Alignment Error
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-odu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Odu.Controllers.Controller.Info.Alarm.Iae, self).__init__()

                            self.yang_name = "iae"
                            self.yang_parent_name = "alarm"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "iae"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Odu.Controllers.Controller.Info.Alarm.Iae, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                            return meta._meta_table['Odu.Controllers.Controller.Info.Alarm.Iae']['meta_info']


                    class Biae(_Entity_):
                        """
                        Backward Incoming Alignment Error
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-odu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Odu.Controllers.Controller.Info.Alarm.Biae, self).__init__()

                            self.yang_name = "biae"
                            self.yang_parent_name = "alarm"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "biae"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Odu.Controllers.Controller.Info.Alarm.Biae, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                            return meta._meta_table['Odu.Controllers.Controller.Info.Alarm.Biae']['meta_info']


                    class SfBer(_Entity_):
                        """
                        SF BER alarm
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-odu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Odu.Controllers.Controller.Info.Alarm.SfBer, self).__init__()

                            self.yang_name = "sf-ber"
                            self.yang_parent_name = "alarm"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "sf-ber"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Odu.Controllers.Controller.Info.Alarm.SfBer, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                            return meta._meta_table['Odu.Controllers.Controller.Info.Alarm.SfBer']['meta_info']


                    class SdBer(_Entity_):
                        """
                        SD BER alarm
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-odu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Odu.Controllers.Controller.Info.Alarm.SdBer, self).__init__()

                            self.yang_name = "sd-ber"
                            self.yang_parent_name = "alarm"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "sd-ber"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Odu.Controllers.Controller.Info.Alarm.SdBer, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                            return meta._meta_table['Odu.Controllers.Controller.Info.Alarm.SdBer']['meta_info']


                    class Csf(_Entity_):
                        """
                        Client Signal Failure
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-odu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Odu.Controllers.Controller.Info.Alarm.Csf, self).__init__()

                            self.yang_name = "csf"
                            self.yang_parent_name = "alarm"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "csf"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Odu.Controllers.Controller.Info.Alarm.Csf, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                            return meta._meta_table['Odu.Controllers.Controller.Info.Alarm.Csf']['meta_info']


                    class Tcm1Ais(_Entity_):
                        """
                        TCM1 Alarm Indication Signal
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-odu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Odu.Controllers.Controller.Info.Alarm.Tcm1Ais, self).__init__()

                            self.yang_name = "tcm1-ais"
                            self.yang_parent_name = "alarm"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "tcm1-ais"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Odu.Controllers.Controller.Info.Alarm.Tcm1Ais, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                            return meta._meta_table['Odu.Controllers.Controller.Info.Alarm.Tcm1Ais']['meta_info']


                    class Tcm1Ltc(_Entity_):
                        """
                        TCM1 Loss of Tandem connection Monitoring
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-odu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Odu.Controllers.Controller.Info.Alarm.Tcm1Ltc, self).__init__()

                            self.yang_name = "tcm1-ltc"
                            self.yang_parent_name = "alarm"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "tcm1-ltc"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Odu.Controllers.Controller.Info.Alarm.Tcm1Ltc, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                            return meta._meta_table['Odu.Controllers.Controller.Info.Alarm.Tcm1Ltc']['meta_info']


                    class Tcm1Oci(_Entity_):
                        """
                        TCM1 Open Connection Indiction
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-odu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Odu.Controllers.Controller.Info.Alarm.Tcm1Oci, self).__init__()

                            self.yang_name = "tcm1-oci"
                            self.yang_parent_name = "alarm"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "tcm1-oci"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Odu.Controllers.Controller.Info.Alarm.Tcm1Oci, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                            return meta._meta_table['Odu.Controllers.Controller.Info.Alarm.Tcm1Oci']['meta_info']


                    class Tcm1Lck(_Entity_):
                        """
                        TCM1  Upstream Connection Locked
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-odu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Odu.Controllers.Controller.Info.Alarm.Tcm1Lck, self).__init__()

                            self.yang_name = "tcm1-lck"
                            self.yang_parent_name = "alarm"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "tcm1-lck"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Odu.Controllers.Controller.Info.Alarm.Tcm1Lck, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                            return meta._meta_table['Odu.Controllers.Controller.Info.Alarm.Tcm1Lck']['meta_info']


                    class Tcm1Iae(_Entity_):
                        """
                        TCM1 Incoming Alignment Error
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-odu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Odu.Controllers.Controller.Info.Alarm.Tcm1Iae, self).__init__()

                            self.yang_name = "tcm1-iae"
                            self.yang_parent_name = "alarm"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "tcm1-iae"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Odu.Controllers.Controller.Info.Alarm.Tcm1Iae, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                            return meta._meta_table['Odu.Controllers.Controller.Info.Alarm.Tcm1Iae']['meta_info']


                    class Tcm1Biae(_Entity_):
                        """
                        TCM1 Backward Incoming Alignment Error
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-odu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Odu.Controllers.Controller.Info.Alarm.Tcm1Biae, self).__init__()

                            self.yang_name = "tcm1-biae"
                            self.yang_parent_name = "alarm"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "tcm1-biae"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Odu.Controllers.Controller.Info.Alarm.Tcm1Biae, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                            return meta._meta_table['Odu.Controllers.Controller.Info.Alarm.Tcm1Biae']['meta_info']


                    class Tcm1Bdi(_Entity_):
                        """
                        TCM1 Backward Defect Monitoring
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-odu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Odu.Controllers.Controller.Info.Alarm.Tcm1Bdi, self).__init__()

                            self.yang_name = "tcm1-bdi"
                            self.yang_parent_name = "alarm"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "tcm1-bdi"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Odu.Controllers.Controller.Info.Alarm.Tcm1Bdi, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                            return meta._meta_table['Odu.Controllers.Controller.Info.Alarm.Tcm1Bdi']['meta_info']


                    class Tcm1Tim(_Entity_):
                        """
                        TCM1 Trail Trace Identifier Mismatch 
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-odu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Odu.Controllers.Controller.Info.Alarm.Tcm1Tim, self).__init__()

                            self.yang_name = "tcm1-tim"
                            self.yang_parent_name = "alarm"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "tcm1-tim"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Odu.Controllers.Controller.Info.Alarm.Tcm1Tim, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                            return meta._meta_table['Odu.Controllers.Controller.Info.Alarm.Tcm1Tim']['meta_info']


                    class Tcm1SfBer(_Entity_):
                        """
                        TCM1 SF BER alarm
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-odu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Odu.Controllers.Controller.Info.Alarm.Tcm1SfBer, self).__init__()

                            self.yang_name = "tcm1-sf-ber"
                            self.yang_parent_name = "alarm"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "tcm1-sf-ber"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Odu.Controllers.Controller.Info.Alarm.Tcm1SfBer, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                            return meta._meta_table['Odu.Controllers.Controller.Info.Alarm.Tcm1SfBer']['meta_info']


                    class Tcm1SdBer(_Entity_):
                        """
                        TCM1 SD BER alarm
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-odu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Odu.Controllers.Controller.Info.Alarm.Tcm1SdBer, self).__init__()

                            self.yang_name = "tcm1-sd-ber"
                            self.yang_parent_name = "alarm"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "tcm1-sd-ber"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Odu.Controllers.Controller.Info.Alarm.Tcm1SdBer, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                            return meta._meta_table['Odu.Controllers.Controller.Info.Alarm.Tcm1SdBer']['meta_info']


                    class Tcm2Ais(_Entity_):
                        """
                        TCM2 Alarm Indication Signal
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-odu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Odu.Controllers.Controller.Info.Alarm.Tcm2Ais, self).__init__()

                            self.yang_name = "tcm2-ais"
                            self.yang_parent_name = "alarm"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "tcm2-ais"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Odu.Controllers.Controller.Info.Alarm.Tcm2Ais, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                            return meta._meta_table['Odu.Controllers.Controller.Info.Alarm.Tcm2Ais']['meta_info']


                    class Tcm2Ltc(_Entity_):
                        """
                        TCM2 Loss of Tandem connection Monitoring
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-odu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Odu.Controllers.Controller.Info.Alarm.Tcm2Ltc, self).__init__()

                            self.yang_name = "tcm2-ltc"
                            self.yang_parent_name = "alarm"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "tcm2-ltc"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Odu.Controllers.Controller.Info.Alarm.Tcm2Ltc, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                            return meta._meta_table['Odu.Controllers.Controller.Info.Alarm.Tcm2Ltc']['meta_info']


                    class Tcm2Oci(_Entity_):
                        """
                        TCM2 Open Connection Indiction
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-odu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Odu.Controllers.Controller.Info.Alarm.Tcm2Oci, self).__init__()

                            self.yang_name = "tcm2-oci"
                            self.yang_parent_name = "alarm"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "tcm2-oci"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Odu.Controllers.Controller.Info.Alarm.Tcm2Oci, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                            return meta._meta_table['Odu.Controllers.Controller.Info.Alarm.Tcm2Oci']['meta_info']


                    class Tcm2Lck(_Entity_):
                        """
                        TCM2  Upstream Connection Locked
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-odu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Odu.Controllers.Controller.Info.Alarm.Tcm2Lck, self).__init__()

                            self.yang_name = "tcm2-lck"
                            self.yang_parent_name = "alarm"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "tcm2-lck"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Odu.Controllers.Controller.Info.Alarm.Tcm2Lck, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                            return meta._meta_table['Odu.Controllers.Controller.Info.Alarm.Tcm2Lck']['meta_info']


                    class Tcm2Iae(_Entity_):
                        """
                        TCM2 Incoming Alignment Error
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-odu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Odu.Controllers.Controller.Info.Alarm.Tcm2Iae, self).__init__()

                            self.yang_name = "tcm2-iae"
                            self.yang_parent_name = "alarm"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "tcm2-iae"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Odu.Controllers.Controller.Info.Alarm.Tcm2Iae, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                            return meta._meta_table['Odu.Controllers.Controller.Info.Alarm.Tcm2Iae']['meta_info']


                    class Tcm2Biae(_Entity_):
                        """
                        TCM2 Backward Incoming Alignment Error
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-odu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Odu.Controllers.Controller.Info.Alarm.Tcm2Biae, self).__init__()

                            self.yang_name = "tcm2-biae"
                            self.yang_parent_name = "alarm"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "tcm2-biae"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Odu.Controllers.Controller.Info.Alarm.Tcm2Biae, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                            return meta._meta_table['Odu.Controllers.Controller.Info.Alarm.Tcm2Biae']['meta_info']


                    class Tcm2Bdi(_Entity_):
                        """
                        TCM2 Backward Defect Monitoring
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-odu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Odu.Controllers.Controller.Info.Alarm.Tcm2Bdi, self).__init__()

                            self.yang_name = "tcm2-bdi"
                            self.yang_parent_name = "alarm"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "tcm2-bdi"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Odu.Controllers.Controller.Info.Alarm.Tcm2Bdi, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                            return meta._meta_table['Odu.Controllers.Controller.Info.Alarm.Tcm2Bdi']['meta_info']


                    class Tcm2Tim(_Entity_):
                        """
                        TCM2 Trail Trace Identifier Mismatch 
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-odu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Odu.Controllers.Controller.Info.Alarm.Tcm2Tim, self).__init__()

                            self.yang_name = "tcm2-tim"
                            self.yang_parent_name = "alarm"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "tcm2-tim"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Odu.Controllers.Controller.Info.Alarm.Tcm2Tim, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                            return meta._meta_table['Odu.Controllers.Controller.Info.Alarm.Tcm2Tim']['meta_info']


                    class Tcm2SfBer(_Entity_):
                        """
                        TCM2 SF BER alarm
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-odu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Odu.Controllers.Controller.Info.Alarm.Tcm2SfBer, self).__init__()

                            self.yang_name = "tcm2-sf-ber"
                            self.yang_parent_name = "alarm"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "tcm2-sf-ber"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Odu.Controllers.Controller.Info.Alarm.Tcm2SfBer, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                            return meta._meta_table['Odu.Controllers.Controller.Info.Alarm.Tcm2SfBer']['meta_info']


                    class Tcm2SdBer(_Entity_):
                        """
                        TCM2 SD BER alarm
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-odu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Odu.Controllers.Controller.Info.Alarm.Tcm2SdBer, self).__init__()

                            self.yang_name = "tcm2-sd-ber"
                            self.yang_parent_name = "alarm"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "tcm2-sd-ber"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Odu.Controllers.Controller.Info.Alarm.Tcm2SdBer, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                            return meta._meta_table['Odu.Controllers.Controller.Info.Alarm.Tcm2SdBer']['meta_info']


                    class Tcm3Ais(_Entity_):
                        """
                        TCM3 Alarm Indication Signal
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-odu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Odu.Controllers.Controller.Info.Alarm.Tcm3Ais, self).__init__()

                            self.yang_name = "tcm3-ais"
                            self.yang_parent_name = "alarm"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "tcm3-ais"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Odu.Controllers.Controller.Info.Alarm.Tcm3Ais, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                            return meta._meta_table['Odu.Controllers.Controller.Info.Alarm.Tcm3Ais']['meta_info']


                    class Tcm3Ltc(_Entity_):
                        """
                        TCM3 Loss of Tandem connection Monitoring
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-odu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Odu.Controllers.Controller.Info.Alarm.Tcm3Ltc, self).__init__()

                            self.yang_name = "tcm3-ltc"
                            self.yang_parent_name = "alarm"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "tcm3-ltc"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Odu.Controllers.Controller.Info.Alarm.Tcm3Ltc, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                            return meta._meta_table['Odu.Controllers.Controller.Info.Alarm.Tcm3Ltc']['meta_info']


                    class Tcm3Oci(_Entity_):
                        """
                        TCM3 Open Connection Indiction
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-odu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Odu.Controllers.Controller.Info.Alarm.Tcm3Oci, self).__init__()

                            self.yang_name = "tcm3-oci"
                            self.yang_parent_name = "alarm"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "tcm3-oci"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Odu.Controllers.Controller.Info.Alarm.Tcm3Oci, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                            return meta._meta_table['Odu.Controllers.Controller.Info.Alarm.Tcm3Oci']['meta_info']


                    class Tcm3Lck(_Entity_):
                        """
                        TCM3  Upstream Connection Locked
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-odu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Odu.Controllers.Controller.Info.Alarm.Tcm3Lck, self).__init__()

                            self.yang_name = "tcm3-lck"
                            self.yang_parent_name = "alarm"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "tcm3-lck"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Odu.Controllers.Controller.Info.Alarm.Tcm3Lck, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                            return meta._meta_table['Odu.Controllers.Controller.Info.Alarm.Tcm3Lck']['meta_info']


                    class Tcm3Iae(_Entity_):
                        """
                        TCM3 Incoming Alignment Error
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-odu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Odu.Controllers.Controller.Info.Alarm.Tcm3Iae, self).__init__()

                            self.yang_name = "tcm3-iae"
                            self.yang_parent_name = "alarm"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "tcm3-iae"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Odu.Controllers.Controller.Info.Alarm.Tcm3Iae, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                            return meta._meta_table['Odu.Controllers.Controller.Info.Alarm.Tcm3Iae']['meta_info']


                    class Tcm3Biae(_Entity_):
                        """
                        TCM3 Backward Incoming Alignment Error
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-odu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Odu.Controllers.Controller.Info.Alarm.Tcm3Biae, self).__init__()

                            self.yang_name = "tcm3-biae"
                            self.yang_parent_name = "alarm"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "tcm3-biae"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Odu.Controllers.Controller.Info.Alarm.Tcm3Biae, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                            return meta._meta_table['Odu.Controllers.Controller.Info.Alarm.Tcm3Biae']['meta_info']


                    class Tcm3Bdi(_Entity_):
                        """
                        TCM3 Backward Defect Monitoring
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-odu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Odu.Controllers.Controller.Info.Alarm.Tcm3Bdi, self).__init__()

                            self.yang_name = "tcm3-bdi"
                            self.yang_parent_name = "alarm"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "tcm3-bdi"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Odu.Controllers.Controller.Info.Alarm.Tcm3Bdi, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                            return meta._meta_table['Odu.Controllers.Controller.Info.Alarm.Tcm3Bdi']['meta_info']


                    class Tcm3Tim(_Entity_):
                        """
                        TCM3 Trail Trace Identifier Mismatch 
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-odu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Odu.Controllers.Controller.Info.Alarm.Tcm3Tim, self).__init__()

                            self.yang_name = "tcm3-tim"
                            self.yang_parent_name = "alarm"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "tcm3-tim"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Odu.Controllers.Controller.Info.Alarm.Tcm3Tim, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                            return meta._meta_table['Odu.Controllers.Controller.Info.Alarm.Tcm3Tim']['meta_info']


                    class Tcm3SfBer(_Entity_):
                        """
                        TCM3 SF BER alarm
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-odu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Odu.Controllers.Controller.Info.Alarm.Tcm3SfBer, self).__init__()

                            self.yang_name = "tcm3-sf-ber"
                            self.yang_parent_name = "alarm"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "tcm3-sf-ber"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Odu.Controllers.Controller.Info.Alarm.Tcm3SfBer, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                            return meta._meta_table['Odu.Controllers.Controller.Info.Alarm.Tcm3SfBer']['meta_info']


                    class Tcm3SdBer(_Entity_):
                        """
                        TCM3 SD BER alarm
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-odu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Odu.Controllers.Controller.Info.Alarm.Tcm3SdBer, self).__init__()

                            self.yang_name = "tcm3-sd-ber"
                            self.yang_parent_name = "alarm"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "tcm3-sd-ber"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Odu.Controllers.Controller.Info.Alarm.Tcm3SdBer, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                            return meta._meta_table['Odu.Controllers.Controller.Info.Alarm.Tcm3SdBer']['meta_info']


                    class Tcm4Ais(_Entity_):
                        """
                        TCM4 Alarm Indication Signal
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-odu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Odu.Controllers.Controller.Info.Alarm.Tcm4Ais, self).__init__()

                            self.yang_name = "tcm4-ais"
                            self.yang_parent_name = "alarm"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "tcm4-ais"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Odu.Controllers.Controller.Info.Alarm.Tcm4Ais, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                            return meta._meta_table['Odu.Controllers.Controller.Info.Alarm.Tcm4Ais']['meta_info']


                    class Tcm4Ltc(_Entity_):
                        """
                        TCM4 Loss of Tandem connection Monitoring
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-odu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Odu.Controllers.Controller.Info.Alarm.Tcm4Ltc, self).__init__()

                            self.yang_name = "tcm4-ltc"
                            self.yang_parent_name = "alarm"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "tcm4-ltc"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Odu.Controllers.Controller.Info.Alarm.Tcm4Ltc, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                            return meta._meta_table['Odu.Controllers.Controller.Info.Alarm.Tcm4Ltc']['meta_info']


                    class Tcm4Oci(_Entity_):
                        """
                        TCM4 Open Connection Indiction
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-odu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Odu.Controllers.Controller.Info.Alarm.Tcm4Oci, self).__init__()

                            self.yang_name = "tcm4-oci"
                            self.yang_parent_name = "alarm"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "tcm4-oci"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Odu.Controllers.Controller.Info.Alarm.Tcm4Oci, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                            return meta._meta_table['Odu.Controllers.Controller.Info.Alarm.Tcm4Oci']['meta_info']


                    class Tcm4Lck(_Entity_):
                        """
                        TCM4  Upstream Connection Locked
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-odu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Odu.Controllers.Controller.Info.Alarm.Tcm4Lck, self).__init__()

                            self.yang_name = "tcm4-lck"
                            self.yang_parent_name = "alarm"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "tcm4-lck"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Odu.Controllers.Controller.Info.Alarm.Tcm4Lck, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                            return meta._meta_table['Odu.Controllers.Controller.Info.Alarm.Tcm4Lck']['meta_info']


                    class Tcm4Iae(_Entity_):
                        """
                        TCM4 Incoming Alignment Error
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-odu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Odu.Controllers.Controller.Info.Alarm.Tcm4Iae, self).__init__()

                            self.yang_name = "tcm4-iae"
                            self.yang_parent_name = "alarm"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "tcm4-iae"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Odu.Controllers.Controller.Info.Alarm.Tcm4Iae, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                            return meta._meta_table['Odu.Controllers.Controller.Info.Alarm.Tcm4Iae']['meta_info']


                    class Tcm4Biae(_Entity_):
                        """
                        TCM4 Backward Incoming Alignment Error
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-odu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Odu.Controllers.Controller.Info.Alarm.Tcm4Biae, self).__init__()

                            self.yang_name = "tcm4-biae"
                            self.yang_parent_name = "alarm"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "tcm4-biae"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Odu.Controllers.Controller.Info.Alarm.Tcm4Biae, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                            return meta._meta_table['Odu.Controllers.Controller.Info.Alarm.Tcm4Biae']['meta_info']


                    class Tcm4Bdi(_Entity_):
                        """
                        TCM4 Backward Defect Monitoring
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-odu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Odu.Controllers.Controller.Info.Alarm.Tcm4Bdi, self).__init__()

                            self.yang_name = "tcm4-bdi"
                            self.yang_parent_name = "alarm"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "tcm4-bdi"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Odu.Controllers.Controller.Info.Alarm.Tcm4Bdi, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                            return meta._meta_table['Odu.Controllers.Controller.Info.Alarm.Tcm4Bdi']['meta_info']


                    class Tcm4Tim(_Entity_):
                        """
                        TCM4 Trail Trace Identifier Mismatch 
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-odu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Odu.Controllers.Controller.Info.Alarm.Tcm4Tim, self).__init__()

                            self.yang_name = "tcm4-tim"
                            self.yang_parent_name = "alarm"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "tcm4-tim"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Odu.Controllers.Controller.Info.Alarm.Tcm4Tim, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                            return meta._meta_table['Odu.Controllers.Controller.Info.Alarm.Tcm4Tim']['meta_info']


                    class Tcm4SfBer(_Entity_):
                        """
                        TCM4 SF BER alarm
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-odu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Odu.Controllers.Controller.Info.Alarm.Tcm4SfBer, self).__init__()

                            self.yang_name = "tcm4-sf-ber"
                            self.yang_parent_name = "alarm"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "tcm4-sf-ber"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Odu.Controllers.Controller.Info.Alarm.Tcm4SfBer, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                            return meta._meta_table['Odu.Controllers.Controller.Info.Alarm.Tcm4SfBer']['meta_info']


                    class Tcm4SdBer(_Entity_):
                        """
                        TCM4 SD BER alarm
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-odu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Odu.Controllers.Controller.Info.Alarm.Tcm4SdBer, self).__init__()

                            self.yang_name = "tcm4-sd-ber"
                            self.yang_parent_name = "alarm"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "tcm4-sd-ber"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Odu.Controllers.Controller.Info.Alarm.Tcm4SdBer, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                            return meta._meta_table['Odu.Controllers.Controller.Info.Alarm.Tcm4SdBer']['meta_info']


                    class Tcm5Ais(_Entity_):
                        """
                        TCM5 Alarm Indication Signal
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-odu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Odu.Controllers.Controller.Info.Alarm.Tcm5Ais, self).__init__()

                            self.yang_name = "tcm5-ais"
                            self.yang_parent_name = "alarm"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "tcm5-ais"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Odu.Controllers.Controller.Info.Alarm.Tcm5Ais, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                            return meta._meta_table['Odu.Controllers.Controller.Info.Alarm.Tcm5Ais']['meta_info']


                    class Tcm5Ltc(_Entity_):
                        """
                        TCM5 Loss of Tandem connection Monitoring
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-odu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Odu.Controllers.Controller.Info.Alarm.Tcm5Ltc, self).__init__()

                            self.yang_name = "tcm5-ltc"
                            self.yang_parent_name = "alarm"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "tcm5-ltc"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Odu.Controllers.Controller.Info.Alarm.Tcm5Ltc, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                            return meta._meta_table['Odu.Controllers.Controller.Info.Alarm.Tcm5Ltc']['meta_info']


                    class Tcm5Oci(_Entity_):
                        """
                        TCM5 Open Connection Indiction
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-odu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Odu.Controllers.Controller.Info.Alarm.Tcm5Oci, self).__init__()

                            self.yang_name = "tcm5-oci"
                            self.yang_parent_name = "alarm"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "tcm5-oci"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Odu.Controllers.Controller.Info.Alarm.Tcm5Oci, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                            return meta._meta_table['Odu.Controllers.Controller.Info.Alarm.Tcm5Oci']['meta_info']


                    class Tcm5Lck(_Entity_):
                        """
                        TCM5  Upstream Connection Locked
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-odu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Odu.Controllers.Controller.Info.Alarm.Tcm5Lck, self).__init__()

                            self.yang_name = "tcm5-lck"
                            self.yang_parent_name = "alarm"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "tcm5-lck"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Odu.Controllers.Controller.Info.Alarm.Tcm5Lck, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                            return meta._meta_table['Odu.Controllers.Controller.Info.Alarm.Tcm5Lck']['meta_info']


                    class Tcm5Iae(_Entity_):
                        """
                        TCM5 Incoming Alignment Error
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-odu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Odu.Controllers.Controller.Info.Alarm.Tcm5Iae, self).__init__()

                            self.yang_name = "tcm5-iae"
                            self.yang_parent_name = "alarm"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "tcm5-iae"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Odu.Controllers.Controller.Info.Alarm.Tcm5Iae, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                            return meta._meta_table['Odu.Controllers.Controller.Info.Alarm.Tcm5Iae']['meta_info']


                    class Tcm5Biae(_Entity_):
                        """
                        TCM5 Backward Incoming Alignment Error
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-odu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Odu.Controllers.Controller.Info.Alarm.Tcm5Biae, self).__init__()

                            self.yang_name = "tcm5-biae"
                            self.yang_parent_name = "alarm"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "tcm5-biae"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Odu.Controllers.Controller.Info.Alarm.Tcm5Biae, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                            return meta._meta_table['Odu.Controllers.Controller.Info.Alarm.Tcm5Biae']['meta_info']


                    class Tcm5Bdi(_Entity_):
                        """
                        TCM5 Backward Defect Monitoring
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-odu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Odu.Controllers.Controller.Info.Alarm.Tcm5Bdi, self).__init__()

                            self.yang_name = "tcm5-bdi"
                            self.yang_parent_name = "alarm"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "tcm5-bdi"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Odu.Controllers.Controller.Info.Alarm.Tcm5Bdi, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                            return meta._meta_table['Odu.Controllers.Controller.Info.Alarm.Tcm5Bdi']['meta_info']


                    class Tcm5Tim(_Entity_):
                        """
                        TCM5 Trail Trace Identifier Mismatch 
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-odu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Odu.Controllers.Controller.Info.Alarm.Tcm5Tim, self).__init__()

                            self.yang_name = "tcm5-tim"
                            self.yang_parent_name = "alarm"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "tcm5-tim"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Odu.Controllers.Controller.Info.Alarm.Tcm5Tim, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                            return meta._meta_table['Odu.Controllers.Controller.Info.Alarm.Tcm5Tim']['meta_info']


                    class Tcm5SfBer(_Entity_):
                        """
                        TCM5 SF BER alarm
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-odu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Odu.Controllers.Controller.Info.Alarm.Tcm5SfBer, self).__init__()

                            self.yang_name = "tcm5-sf-ber"
                            self.yang_parent_name = "alarm"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "tcm5-sf-ber"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Odu.Controllers.Controller.Info.Alarm.Tcm5SfBer, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                            return meta._meta_table['Odu.Controllers.Controller.Info.Alarm.Tcm5SfBer']['meta_info']


                    class Tcm5SdBer(_Entity_):
                        """
                        TCM5 SD BER alarm
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-odu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Odu.Controllers.Controller.Info.Alarm.Tcm5SdBer, self).__init__()

                            self.yang_name = "tcm5-sd-ber"
                            self.yang_parent_name = "alarm"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "tcm5-sd-ber"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Odu.Controllers.Controller.Info.Alarm.Tcm5SdBer, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                            return meta._meta_table['Odu.Controllers.Controller.Info.Alarm.Tcm5SdBer']['meta_info']


                    class Tcm6Ais(_Entity_):
                        """
                        TCM6 Alarm Indication Signal
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-odu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Odu.Controllers.Controller.Info.Alarm.Tcm6Ais, self).__init__()

                            self.yang_name = "tcm6-ais"
                            self.yang_parent_name = "alarm"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "tcm6-ais"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Odu.Controllers.Controller.Info.Alarm.Tcm6Ais, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                            return meta._meta_table['Odu.Controllers.Controller.Info.Alarm.Tcm6Ais']['meta_info']


                    class Tcm6Ltc(_Entity_):
                        """
                        TCM6 Loss of Tandem connection Monitoring
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-odu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Odu.Controllers.Controller.Info.Alarm.Tcm6Ltc, self).__init__()

                            self.yang_name = "tcm6-ltc"
                            self.yang_parent_name = "alarm"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "tcm6-ltc"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Odu.Controllers.Controller.Info.Alarm.Tcm6Ltc, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                            return meta._meta_table['Odu.Controllers.Controller.Info.Alarm.Tcm6Ltc']['meta_info']


                    class Tcm6Oci(_Entity_):
                        """
                        TCM6 Open Connection Indiction
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-odu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Odu.Controllers.Controller.Info.Alarm.Tcm6Oci, self).__init__()

                            self.yang_name = "tcm6-oci"
                            self.yang_parent_name = "alarm"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "tcm6-oci"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Odu.Controllers.Controller.Info.Alarm.Tcm6Oci, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                            return meta._meta_table['Odu.Controllers.Controller.Info.Alarm.Tcm6Oci']['meta_info']


                    class Tcm6Lck(_Entity_):
                        """
                        TCM6  Upstream Connection Locked
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-odu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Odu.Controllers.Controller.Info.Alarm.Tcm6Lck, self).__init__()

                            self.yang_name = "tcm6-lck"
                            self.yang_parent_name = "alarm"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "tcm6-lck"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Odu.Controllers.Controller.Info.Alarm.Tcm6Lck, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                            return meta._meta_table['Odu.Controllers.Controller.Info.Alarm.Tcm6Lck']['meta_info']


                    class Tcm6Iae(_Entity_):
                        """
                        TCM6 Incoming Alignment Error
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-odu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Odu.Controllers.Controller.Info.Alarm.Tcm6Iae, self).__init__()

                            self.yang_name = "tcm6-iae"
                            self.yang_parent_name = "alarm"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "tcm6-iae"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Odu.Controllers.Controller.Info.Alarm.Tcm6Iae, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                            return meta._meta_table['Odu.Controllers.Controller.Info.Alarm.Tcm6Iae']['meta_info']


                    class Tcm6Biae(_Entity_):
                        """
                        TCM6 Backward Incoming Alignment Error
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-odu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Odu.Controllers.Controller.Info.Alarm.Tcm6Biae, self).__init__()

                            self.yang_name = "tcm6-biae"
                            self.yang_parent_name = "alarm"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "tcm6-biae"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Odu.Controllers.Controller.Info.Alarm.Tcm6Biae, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                            return meta._meta_table['Odu.Controllers.Controller.Info.Alarm.Tcm6Biae']['meta_info']


                    class Tcm6Bdi(_Entity_):
                        """
                        TCM6 Backward Defect Monitoring
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-odu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Odu.Controllers.Controller.Info.Alarm.Tcm6Bdi, self).__init__()

                            self.yang_name = "tcm6-bdi"
                            self.yang_parent_name = "alarm"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "tcm6-bdi"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Odu.Controllers.Controller.Info.Alarm.Tcm6Bdi, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                            return meta._meta_table['Odu.Controllers.Controller.Info.Alarm.Tcm6Bdi']['meta_info']


                    class Tcm6Tim(_Entity_):
                        """
                        TCM6 Trail Trace Identifier Mismatch 
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-odu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Odu.Controllers.Controller.Info.Alarm.Tcm6Tim, self).__init__()

                            self.yang_name = "tcm6-tim"
                            self.yang_parent_name = "alarm"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "tcm6-tim"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Odu.Controllers.Controller.Info.Alarm.Tcm6Tim, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                            return meta._meta_table['Odu.Controllers.Controller.Info.Alarm.Tcm6Tim']['meta_info']


                    class Tcm6SfBer(_Entity_):
                        """
                        TCM6 SF BER alarm
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-odu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Odu.Controllers.Controller.Info.Alarm.Tcm6SfBer, self).__init__()

                            self.yang_name = "tcm6-sf-ber"
                            self.yang_parent_name = "alarm"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "tcm6-sf-ber"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Odu.Controllers.Controller.Info.Alarm.Tcm6SfBer, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                            return meta._meta_table['Odu.Controllers.Controller.Info.Alarm.Tcm6SfBer']['meta_info']


                    class Tcm6SdBer(_Entity_):
                        """
                        TCM6 SD BER alarm
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-odu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Odu.Controllers.Controller.Info.Alarm.Tcm6SdBer, self).__init__()

                            self.yang_name = "tcm6-sd-ber"
                            self.yang_parent_name = "alarm"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "tcm6-sd-ber"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Odu.Controllers.Controller.Info.Alarm.Tcm6SdBer, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                            return meta._meta_table['Odu.Controllers.Controller.Info.Alarm.Tcm6SdBer']['meta_info']


                    class GfpLfd(_Entity_):
                        """
                        Loss Of Frame Delineation
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-odu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Odu.Controllers.Controller.Info.Alarm.GfpLfd, self).__init__()

                            self.yang_name = "gfp-lfd"
                            self.yang_parent_name = "alarm"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "gfp-lfd"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Odu.Controllers.Controller.Info.Alarm.GfpLfd, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                            return meta._meta_table['Odu.Controllers.Controller.Info.Alarm.GfpLfd']['meta_info']


                    class GfpLocs(_Entity_):
                        """
                        Loss Of Client Signal
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-odu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Odu.Controllers.Controller.Info.Alarm.GfpLocs, self).__init__()

                            self.yang_name = "gfp-locs"
                            self.yang_parent_name = "alarm"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "gfp-locs"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Odu.Controllers.Controller.Info.Alarm.GfpLocs, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                            return meta._meta_table['Odu.Controllers.Controller.Info.Alarm.GfpLocs']['meta_info']


                    class GfpLoccs(_Entity_):
                        """
                        Loss Of Character Synchronization
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-odu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Odu.Controllers.Controller.Info.Alarm.GfpLoccs, self).__init__()

                            self.yang_name = "gfp-loccs"
                            self.yang_parent_name = "alarm"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "gfp-loccs"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Odu.Controllers.Controller.Info.Alarm.GfpLoccs, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                            return meta._meta_table['Odu.Controllers.Controller.Info.Alarm.GfpLoccs']['meta_info']


                    class GfpUpm(_Entity_):
                        """
                        User Payload Mismatch
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-odu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Odu.Controllers.Controller.Info.Alarm.GfpUpm, self).__init__()

                            self.yang_name = "gfp-upm"
                            self.yang_parent_name = "alarm"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "gfp-upm"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Odu.Controllers.Controller.Info.Alarm.GfpUpm, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                            return meta._meta_table['Odu.Controllers.Controller.Info.Alarm.GfpUpm']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                        return meta._meta_table['Odu.Controllers.Controller.Info.Alarm']['meta_info']


                class TeCtxData(_Entity_):
                    """
                    Label Get Data
                    
                    .. attribute:: te_tunnel_info
                    
                    	Tunnel Information
                    	**type**\:  :py:class:`TeTunnelInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.TeCtxData.TeTunnelInfo>`
                    
                    	**config**\: False
                    
                    .. attribute:: gmpls_req_time
                    
                    	Req Time
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: ctxt_type
                    
                    	Ctxt Type
                    	**type**\:  :py:class:`OtmOpticalRmCtxt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.OtmOpticalRmCtxt>`
                    
                    	**config**\: False
                    
                    .. attribute:: rm_type
                    
                    	Rm Type
                    	**type**\:  :py:class:`OtmOpticalRmCtxtRm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.OtmOpticalRmCtxtRm>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'controller-odu-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Odu.Controllers.Controller.Info.TeCtxData, self).__init__()

                        self.yang_name = "te-ctx-data"
                        self.yang_parent_name = "info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("te-tunnel-info", ("te_tunnel_info", Odu.Controllers.Controller.Info.TeCtxData.TeTunnelInfo))])
                        self._leafs = OrderedDict([
                            ('gmpls_req_time', (YLeaf(YType.uint32, 'gmpls-req-time'), ['int'])),
                            ('ctxt_type', (YLeaf(YType.enumeration, 'ctxt-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper', 'OtmOpticalRmCtxt', '')])),
                            ('rm_type', (YLeaf(YType.enumeration, 'rm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper', 'OtmOpticalRmCtxtRm', '')])),
                        ])
                        self.gmpls_req_time = None
                        self.ctxt_type = None
                        self.rm_type = None

                        self.te_tunnel_info = Odu.Controllers.Controller.Info.TeCtxData.TeTunnelInfo()
                        self.te_tunnel_info.parent = self
                        self._children_name_map["te_tunnel_info"] = "te-tunnel-info"
                        self._segment_path = lambda: "te-ctx-data"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Odu.Controllers.Controller.Info.TeCtxData, ['gmpls_req_time', 'ctxt_type', 'rm_type'], name, value)


                    class TeTunnelInfo(_Entity_):
                        """
                        Tunnel Information
                        
                        .. attribute:: lb_ctxt
                        
                        	Lbl Ctxt
                        	**type**\:  :py:class:`LbCtxt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.TeCtxData.TeTunnelInfo.LbCtxt>`
                        
                        	**config**\: False
                        
                        .. attribute:: passive_match
                        
                        	Passive Match
                        	**type**\:  :py:class:`PassiveMatch <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.TeCtxData.TeTunnelInfo.PassiveMatch>`
                        
                        	**config**\: False
                        
                        .. attribute:: info_type
                        
                        	INFO TYPE
                        	**type**\:  :py:class:`OtmTeTunnelInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.OtmTeTunnelInfo>`
                        
                        	**config**\: False
                        
                        .. attribute:: tunnel_id
                        
                        	Tunnel Id
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-odu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Odu.Controllers.Controller.Info.TeCtxData.TeTunnelInfo, self).__init__()

                            self.yang_name = "te-tunnel-info"
                            self.yang_parent_name = "te-ctx-data"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("lb-ctxt", ("lb_ctxt", Odu.Controllers.Controller.Info.TeCtxData.TeTunnelInfo.LbCtxt)), ("passive-match", ("passive_match", Odu.Controllers.Controller.Info.TeCtxData.TeTunnelInfo.PassiveMatch))])
                            self._leafs = OrderedDict([
                                ('info_type', (YLeaf(YType.enumeration, 'info-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper', 'OtmTeTunnelInfo', '')])),
                                ('tunnel_id', (YLeaf(YType.uint32, 'tunnel-id'), ['int'])),
                            ])
                            self.info_type = None
                            self.tunnel_id = None

                            self.lb_ctxt = Odu.Controllers.Controller.Info.TeCtxData.TeTunnelInfo.LbCtxt()
                            self.lb_ctxt.parent = self
                            self._children_name_map["lb_ctxt"] = "lb-ctxt"

                            self.passive_match = Odu.Controllers.Controller.Info.TeCtxData.TeTunnelInfo.PassiveMatch()
                            self.passive_match.parent = self
                            self._children_name_map["passive_match"] = "passive-match"
                            self._segment_path = lambda: "te-tunnel-info"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Odu.Controllers.Controller.Info.TeCtxData.TeTunnelInfo, ['info_type', 'tunnel_id'], name, value)


                        class LbCtxt(_Entity_):
                            """
                            Lbl Ctxt
                            
                            .. attribute:: s2l_fec_sub_group_id
                            
                            	SubGroup Id
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            	**config**\: False
                            
                            .. attribute:: s2l_fec_lsp_id
                            
                            	Lsp Id
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            	**config**\: False
                            
                            .. attribute:: s2l_fec_tunnel_id
                            
                            	Tunnel Id
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            	**config**\: False
                            
                            .. attribute:: ext_tunnel_id
                            
                            	Ext Tunnel Id
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: fec_source
                            
                            	FEC Source
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: fec_dest
                            
                            	FEC Dest
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: s2l_fec_p2mp_id
                            
                            	P2MP Id
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: sub_group_origin_ator
                            
                            	SubGroup Originator
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: fec_c_type
                            
                            	Ctype
                            	**type**\:  :py:class:`OtmMplsLibC <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.OtmMplsLibC>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'controller-odu-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Odu.Controllers.Controller.Info.TeCtxData.TeTunnelInfo.LbCtxt, self).__init__()

                                self.yang_name = "lb-ctxt"
                                self.yang_parent_name = "te-tunnel-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('s2l_fec_sub_group_id', (YLeaf(YType.uint16, 's2l-fec-sub-group-id'), ['int'])),
                                    ('s2l_fec_lsp_id', (YLeaf(YType.uint16, 's2l-fec-lsp-id'), ['int'])),
                                    ('s2l_fec_tunnel_id', (YLeaf(YType.uint16, 's2l-fec-tunnel-id'), ['int'])),
                                    ('ext_tunnel_id', (YLeaf(YType.uint32, 'ext-tunnel-id'), ['int'])),
                                    ('fec_source', (YLeaf(YType.uint32, 'fec-source'), ['int'])),
                                    ('fec_dest', (YLeaf(YType.uint32, 'fec-dest'), ['int'])),
                                    ('s2l_fec_p2mp_id', (YLeaf(YType.uint32, 's2l-fec-p2mp-id'), ['int'])),
                                    ('sub_group_origin_ator', (YLeaf(YType.uint32, 'sub-group-origin-ator'), ['int'])),
                                    ('fec_c_type', (YLeaf(YType.enumeration, 'fec-c-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper', 'OtmMplsLibC', '')])),
                                ])
                                self.s2l_fec_sub_group_id = None
                                self.s2l_fec_lsp_id = None
                                self.s2l_fec_tunnel_id = None
                                self.ext_tunnel_id = None
                                self.fec_source = None
                                self.fec_dest = None
                                self.s2l_fec_p2mp_id = None
                                self.sub_group_origin_ator = None
                                self.fec_c_type = None
                                self._segment_path = lambda: "lb-ctxt"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Odu.Controllers.Controller.Info.TeCtxData.TeTunnelInfo.LbCtxt, ['s2l_fec_sub_group_id', 's2l_fec_lsp_id', 's2l_fec_tunnel_id', 'ext_tunnel_id', 'fec_source', 'fec_dest', 's2l_fec_p2mp_id', 'sub_group_origin_ator', 'fec_c_type'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                                return meta._meta_table['Odu.Controllers.Controller.Info.TeCtxData.TeTunnelInfo.LbCtxt']['meta_info']


                        class PassiveMatch(_Entity_):
                            """
                            Passive Match
                            
                            .. attribute:: src_tid
                            
                            	Src TId
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            	**config**\: False
                            
                            .. attribute:: src_rid
                            
                            	Src RId
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'controller-odu-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Odu.Controllers.Controller.Info.TeCtxData.TeTunnelInfo.PassiveMatch, self).__init__()

                                self.yang_name = "passive-match"
                                self.yang_parent_name = "te-tunnel-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('src_tid', (YLeaf(YType.uint16, 'src-tid'), ['int'])),
                                    ('src_rid', (YLeaf(YType.uint32, 'src-rid'), ['int'])),
                                ])
                                self.src_tid = None
                                self.src_rid = None
                                self._segment_path = lambda: "passive-match"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Odu.Controllers.Controller.Info.TeCtxData.TeTunnelInfo.PassiveMatch, ['src_tid', 'src_rid'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                                return meta._meta_table['Odu.Controllers.Controller.Info.TeCtxData.TeTunnelInfo.PassiveMatch']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                            return meta._meta_table['Odu.Controllers.Controller.Info.TeCtxData.TeTunnelInfo']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                        return meta._meta_table['Odu.Controllers.Controller.Info.TeCtxData']['meta_info']


                class XcAddCtxData(_Entity_):
                    """
                    Xconnect Add Data
                    
                    .. attribute:: te_tunnel_info
                    
                    	Tunnel Information
                    	**type**\:  :py:class:`TeTunnelInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.XcAddCtxData.TeTunnelInfo>`
                    
                    	**config**\: False
                    
                    .. attribute:: gmpls_req_time
                    
                    	Req Time
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: ctxt_type
                    
                    	Ctxt Type
                    	**type**\:  :py:class:`OtmOpticalRmCtxt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.OtmOpticalRmCtxt>`
                    
                    	**config**\: False
                    
                    .. attribute:: rm_type
                    
                    	Rm Type
                    	**type**\:  :py:class:`OtmOpticalRmCtxtRm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.OtmOpticalRmCtxtRm>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'controller-odu-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Odu.Controllers.Controller.Info.XcAddCtxData, self).__init__()

                        self.yang_name = "xc-add-ctx-data"
                        self.yang_parent_name = "info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("te-tunnel-info", ("te_tunnel_info", Odu.Controllers.Controller.Info.XcAddCtxData.TeTunnelInfo))])
                        self._leafs = OrderedDict([
                            ('gmpls_req_time', (YLeaf(YType.uint32, 'gmpls-req-time'), ['int'])),
                            ('ctxt_type', (YLeaf(YType.enumeration, 'ctxt-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper', 'OtmOpticalRmCtxt', '')])),
                            ('rm_type', (YLeaf(YType.enumeration, 'rm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper', 'OtmOpticalRmCtxtRm', '')])),
                        ])
                        self.gmpls_req_time = None
                        self.ctxt_type = None
                        self.rm_type = None

                        self.te_tunnel_info = Odu.Controllers.Controller.Info.XcAddCtxData.TeTunnelInfo()
                        self.te_tunnel_info.parent = self
                        self._children_name_map["te_tunnel_info"] = "te-tunnel-info"
                        self._segment_path = lambda: "xc-add-ctx-data"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Odu.Controllers.Controller.Info.XcAddCtxData, ['gmpls_req_time', 'ctxt_type', 'rm_type'], name, value)


                    class TeTunnelInfo(_Entity_):
                        """
                        Tunnel Information
                        
                        .. attribute:: lb_ctxt
                        
                        	Lbl Ctxt
                        	**type**\:  :py:class:`LbCtxt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.XcAddCtxData.TeTunnelInfo.LbCtxt>`
                        
                        	**config**\: False
                        
                        .. attribute:: passive_match
                        
                        	Passive Match
                        	**type**\:  :py:class:`PassiveMatch <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.XcAddCtxData.TeTunnelInfo.PassiveMatch>`
                        
                        	**config**\: False
                        
                        .. attribute:: info_type
                        
                        	INFO TYPE
                        	**type**\:  :py:class:`OtmTeTunnelInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.OtmTeTunnelInfo>`
                        
                        	**config**\: False
                        
                        .. attribute:: tunnel_id
                        
                        	Tunnel Id
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-odu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Odu.Controllers.Controller.Info.XcAddCtxData.TeTunnelInfo, self).__init__()

                            self.yang_name = "te-tunnel-info"
                            self.yang_parent_name = "xc-add-ctx-data"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("lb-ctxt", ("lb_ctxt", Odu.Controllers.Controller.Info.XcAddCtxData.TeTunnelInfo.LbCtxt)), ("passive-match", ("passive_match", Odu.Controllers.Controller.Info.XcAddCtxData.TeTunnelInfo.PassiveMatch))])
                            self._leafs = OrderedDict([
                                ('info_type', (YLeaf(YType.enumeration, 'info-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper', 'OtmTeTunnelInfo', '')])),
                                ('tunnel_id', (YLeaf(YType.uint32, 'tunnel-id'), ['int'])),
                            ])
                            self.info_type = None
                            self.tunnel_id = None

                            self.lb_ctxt = Odu.Controllers.Controller.Info.XcAddCtxData.TeTunnelInfo.LbCtxt()
                            self.lb_ctxt.parent = self
                            self._children_name_map["lb_ctxt"] = "lb-ctxt"

                            self.passive_match = Odu.Controllers.Controller.Info.XcAddCtxData.TeTunnelInfo.PassiveMatch()
                            self.passive_match.parent = self
                            self._children_name_map["passive_match"] = "passive-match"
                            self._segment_path = lambda: "te-tunnel-info"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Odu.Controllers.Controller.Info.XcAddCtxData.TeTunnelInfo, ['info_type', 'tunnel_id'], name, value)


                        class LbCtxt(_Entity_):
                            """
                            Lbl Ctxt
                            
                            .. attribute:: s2l_fec_sub_group_id
                            
                            	SubGroup Id
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            	**config**\: False
                            
                            .. attribute:: s2l_fec_lsp_id
                            
                            	Lsp Id
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            	**config**\: False
                            
                            .. attribute:: s2l_fec_tunnel_id
                            
                            	Tunnel Id
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            	**config**\: False
                            
                            .. attribute:: ext_tunnel_id
                            
                            	Ext Tunnel Id
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: fec_source
                            
                            	FEC Source
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: fec_dest
                            
                            	FEC Dest
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: s2l_fec_p2mp_id
                            
                            	P2MP Id
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: sub_group_origin_ator
                            
                            	SubGroup Originator
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: fec_c_type
                            
                            	Ctype
                            	**type**\:  :py:class:`OtmMplsLibC <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.OtmMplsLibC>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'controller-odu-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Odu.Controllers.Controller.Info.XcAddCtxData.TeTunnelInfo.LbCtxt, self).__init__()

                                self.yang_name = "lb-ctxt"
                                self.yang_parent_name = "te-tunnel-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('s2l_fec_sub_group_id', (YLeaf(YType.uint16, 's2l-fec-sub-group-id'), ['int'])),
                                    ('s2l_fec_lsp_id', (YLeaf(YType.uint16, 's2l-fec-lsp-id'), ['int'])),
                                    ('s2l_fec_tunnel_id', (YLeaf(YType.uint16, 's2l-fec-tunnel-id'), ['int'])),
                                    ('ext_tunnel_id', (YLeaf(YType.uint32, 'ext-tunnel-id'), ['int'])),
                                    ('fec_source', (YLeaf(YType.uint32, 'fec-source'), ['int'])),
                                    ('fec_dest', (YLeaf(YType.uint32, 'fec-dest'), ['int'])),
                                    ('s2l_fec_p2mp_id', (YLeaf(YType.uint32, 's2l-fec-p2mp-id'), ['int'])),
                                    ('sub_group_origin_ator', (YLeaf(YType.uint32, 'sub-group-origin-ator'), ['int'])),
                                    ('fec_c_type', (YLeaf(YType.enumeration, 'fec-c-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper', 'OtmMplsLibC', '')])),
                                ])
                                self.s2l_fec_sub_group_id = None
                                self.s2l_fec_lsp_id = None
                                self.s2l_fec_tunnel_id = None
                                self.ext_tunnel_id = None
                                self.fec_source = None
                                self.fec_dest = None
                                self.s2l_fec_p2mp_id = None
                                self.sub_group_origin_ator = None
                                self.fec_c_type = None
                                self._segment_path = lambda: "lb-ctxt"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Odu.Controllers.Controller.Info.XcAddCtxData.TeTunnelInfo.LbCtxt, ['s2l_fec_sub_group_id', 's2l_fec_lsp_id', 's2l_fec_tunnel_id', 'ext_tunnel_id', 'fec_source', 'fec_dest', 's2l_fec_p2mp_id', 'sub_group_origin_ator', 'fec_c_type'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                                return meta._meta_table['Odu.Controllers.Controller.Info.XcAddCtxData.TeTunnelInfo.LbCtxt']['meta_info']


                        class PassiveMatch(_Entity_):
                            """
                            Passive Match
                            
                            .. attribute:: src_tid
                            
                            	Src TId
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            	**config**\: False
                            
                            .. attribute:: src_rid
                            
                            	Src RId
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'controller-odu-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Odu.Controllers.Controller.Info.XcAddCtxData.TeTunnelInfo.PassiveMatch, self).__init__()

                                self.yang_name = "passive-match"
                                self.yang_parent_name = "te-tunnel-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('src_tid', (YLeaf(YType.uint16, 'src-tid'), ['int'])),
                                    ('src_rid', (YLeaf(YType.uint32, 'src-rid'), ['int'])),
                                ])
                                self.src_tid = None
                                self.src_rid = None
                                self._segment_path = lambda: "passive-match"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Odu.Controllers.Controller.Info.XcAddCtxData.TeTunnelInfo.PassiveMatch, ['src_tid', 'src_rid'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                                return meta._meta_table['Odu.Controllers.Controller.Info.XcAddCtxData.TeTunnelInfo.PassiveMatch']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                            return meta._meta_table['Odu.Controllers.Controller.Info.XcAddCtxData.TeTunnelInfo']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                        return meta._meta_table['Odu.Controllers.Controller.Info.XcAddCtxData']['meta_info']


                class XcRemCtxData(_Entity_):
                    """
                    Xconnect Remove Data
                    
                    .. attribute:: te_tunnel_info
                    
                    	Tunnel Information
                    	**type**\:  :py:class:`TeTunnelInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.XcRemCtxData.TeTunnelInfo>`
                    
                    	**config**\: False
                    
                    .. attribute:: gmpls_req_time
                    
                    	Req Time
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: ctxt_type
                    
                    	Ctxt Type
                    	**type**\:  :py:class:`OtmOpticalRmCtxt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.OtmOpticalRmCtxt>`
                    
                    	**config**\: False
                    
                    .. attribute:: rm_type
                    
                    	Rm Type
                    	**type**\:  :py:class:`OtmOpticalRmCtxtRm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.OtmOpticalRmCtxtRm>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'controller-odu-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Odu.Controllers.Controller.Info.XcRemCtxData, self).__init__()

                        self.yang_name = "xc-rem-ctx-data"
                        self.yang_parent_name = "info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("te-tunnel-info", ("te_tunnel_info", Odu.Controllers.Controller.Info.XcRemCtxData.TeTunnelInfo))])
                        self._leafs = OrderedDict([
                            ('gmpls_req_time', (YLeaf(YType.uint32, 'gmpls-req-time'), ['int'])),
                            ('ctxt_type', (YLeaf(YType.enumeration, 'ctxt-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper', 'OtmOpticalRmCtxt', '')])),
                            ('rm_type', (YLeaf(YType.enumeration, 'rm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper', 'OtmOpticalRmCtxtRm', '')])),
                        ])
                        self.gmpls_req_time = None
                        self.ctxt_type = None
                        self.rm_type = None

                        self.te_tunnel_info = Odu.Controllers.Controller.Info.XcRemCtxData.TeTunnelInfo()
                        self.te_tunnel_info.parent = self
                        self._children_name_map["te_tunnel_info"] = "te-tunnel-info"
                        self._segment_path = lambda: "xc-rem-ctx-data"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Odu.Controllers.Controller.Info.XcRemCtxData, ['gmpls_req_time', 'ctxt_type', 'rm_type'], name, value)


                    class TeTunnelInfo(_Entity_):
                        """
                        Tunnel Information
                        
                        .. attribute:: lb_ctxt
                        
                        	Lbl Ctxt
                        	**type**\:  :py:class:`LbCtxt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.XcRemCtxData.TeTunnelInfo.LbCtxt>`
                        
                        	**config**\: False
                        
                        .. attribute:: passive_match
                        
                        	Passive Match
                        	**type**\:  :py:class:`PassiveMatch <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.XcRemCtxData.TeTunnelInfo.PassiveMatch>`
                        
                        	**config**\: False
                        
                        .. attribute:: info_type
                        
                        	INFO TYPE
                        	**type**\:  :py:class:`OtmTeTunnelInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.OtmTeTunnelInfo>`
                        
                        	**config**\: False
                        
                        .. attribute:: tunnel_id
                        
                        	Tunnel Id
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-odu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Odu.Controllers.Controller.Info.XcRemCtxData.TeTunnelInfo, self).__init__()

                            self.yang_name = "te-tunnel-info"
                            self.yang_parent_name = "xc-rem-ctx-data"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("lb-ctxt", ("lb_ctxt", Odu.Controllers.Controller.Info.XcRemCtxData.TeTunnelInfo.LbCtxt)), ("passive-match", ("passive_match", Odu.Controllers.Controller.Info.XcRemCtxData.TeTunnelInfo.PassiveMatch))])
                            self._leafs = OrderedDict([
                                ('info_type', (YLeaf(YType.enumeration, 'info-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper', 'OtmTeTunnelInfo', '')])),
                                ('tunnel_id', (YLeaf(YType.uint32, 'tunnel-id'), ['int'])),
                            ])
                            self.info_type = None
                            self.tunnel_id = None

                            self.lb_ctxt = Odu.Controllers.Controller.Info.XcRemCtxData.TeTunnelInfo.LbCtxt()
                            self.lb_ctxt.parent = self
                            self._children_name_map["lb_ctxt"] = "lb-ctxt"

                            self.passive_match = Odu.Controllers.Controller.Info.XcRemCtxData.TeTunnelInfo.PassiveMatch()
                            self.passive_match.parent = self
                            self._children_name_map["passive_match"] = "passive-match"
                            self._segment_path = lambda: "te-tunnel-info"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Odu.Controllers.Controller.Info.XcRemCtxData.TeTunnelInfo, ['info_type', 'tunnel_id'], name, value)


                        class LbCtxt(_Entity_):
                            """
                            Lbl Ctxt
                            
                            .. attribute:: s2l_fec_sub_group_id
                            
                            	SubGroup Id
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            	**config**\: False
                            
                            .. attribute:: s2l_fec_lsp_id
                            
                            	Lsp Id
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            	**config**\: False
                            
                            .. attribute:: s2l_fec_tunnel_id
                            
                            	Tunnel Id
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            	**config**\: False
                            
                            .. attribute:: ext_tunnel_id
                            
                            	Ext Tunnel Id
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: fec_source
                            
                            	FEC Source
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: fec_dest
                            
                            	FEC Dest
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: s2l_fec_p2mp_id
                            
                            	P2MP Id
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: sub_group_origin_ator
                            
                            	SubGroup Originator
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: fec_c_type
                            
                            	Ctype
                            	**type**\:  :py:class:`OtmMplsLibC <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.OtmMplsLibC>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'controller-odu-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Odu.Controllers.Controller.Info.XcRemCtxData.TeTunnelInfo.LbCtxt, self).__init__()

                                self.yang_name = "lb-ctxt"
                                self.yang_parent_name = "te-tunnel-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('s2l_fec_sub_group_id', (YLeaf(YType.uint16, 's2l-fec-sub-group-id'), ['int'])),
                                    ('s2l_fec_lsp_id', (YLeaf(YType.uint16, 's2l-fec-lsp-id'), ['int'])),
                                    ('s2l_fec_tunnel_id', (YLeaf(YType.uint16, 's2l-fec-tunnel-id'), ['int'])),
                                    ('ext_tunnel_id', (YLeaf(YType.uint32, 'ext-tunnel-id'), ['int'])),
                                    ('fec_source', (YLeaf(YType.uint32, 'fec-source'), ['int'])),
                                    ('fec_dest', (YLeaf(YType.uint32, 'fec-dest'), ['int'])),
                                    ('s2l_fec_p2mp_id', (YLeaf(YType.uint32, 's2l-fec-p2mp-id'), ['int'])),
                                    ('sub_group_origin_ator', (YLeaf(YType.uint32, 'sub-group-origin-ator'), ['int'])),
                                    ('fec_c_type', (YLeaf(YType.enumeration, 'fec-c-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper', 'OtmMplsLibC', '')])),
                                ])
                                self.s2l_fec_sub_group_id = None
                                self.s2l_fec_lsp_id = None
                                self.s2l_fec_tunnel_id = None
                                self.ext_tunnel_id = None
                                self.fec_source = None
                                self.fec_dest = None
                                self.s2l_fec_p2mp_id = None
                                self.sub_group_origin_ator = None
                                self.fec_c_type = None
                                self._segment_path = lambda: "lb-ctxt"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Odu.Controllers.Controller.Info.XcRemCtxData.TeTunnelInfo.LbCtxt, ['s2l_fec_sub_group_id', 's2l_fec_lsp_id', 's2l_fec_tunnel_id', 'ext_tunnel_id', 'fec_source', 'fec_dest', 's2l_fec_p2mp_id', 'sub_group_origin_ator', 'fec_c_type'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                                return meta._meta_table['Odu.Controllers.Controller.Info.XcRemCtxData.TeTunnelInfo.LbCtxt']['meta_info']


                        class PassiveMatch(_Entity_):
                            """
                            Passive Match
                            
                            .. attribute:: src_tid
                            
                            	Src TId
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            	**config**\: False
                            
                            .. attribute:: src_rid
                            
                            	Src RId
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'controller-odu-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Odu.Controllers.Controller.Info.XcRemCtxData.TeTunnelInfo.PassiveMatch, self).__init__()

                                self.yang_name = "passive-match"
                                self.yang_parent_name = "te-tunnel-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('src_tid', (YLeaf(YType.uint16, 'src-tid'), ['int'])),
                                    ('src_rid', (YLeaf(YType.uint32, 'src-rid'), ['int'])),
                                ])
                                self.src_tid = None
                                self.src_rid = None
                                self._segment_path = lambda: "passive-match"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Odu.Controllers.Controller.Info.XcRemCtxData.TeTunnelInfo.PassiveMatch, ['src_tid', 'src_rid'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                                return meta._meta_table['Odu.Controllers.Controller.Info.XcRemCtxData.TeTunnelInfo.PassiveMatch']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                            return meta._meta_table['Odu.Controllers.Controller.Info.XcRemCtxData.TeTunnelInfo']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                        return meta._meta_table['Odu.Controllers.Controller.Info.XcRemCtxData']['meta_info']


                class OduDelay(_Entity_):
                    """
                    ODU Delay
                    
                    .. attribute:: mode
                    
                    	Latency Mode
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: delay
                    
                    	Delay Value
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'controller-odu-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Odu.Controllers.Controller.Info.OduDelay, self).__init__()

                        self.yang_name = "odu-delay"
                        self.yang_parent_name = "info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('mode', (YLeaf(YType.uint8, 'mode'), ['int'])),
                            ('delay', (YLeaf(YType.uint32, 'delay'), ['int'])),
                        ])
                        self.mode = None
                        self.delay = None
                        self._segment_path = lambda: "odu-delay"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Odu.Controllers.Controller.Info.OduDelay, ['mode', 'delay'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                        return meta._meta_table['Odu.Controllers.Controller.Info.OduDelay']['meta_info']


                class OduTerminateEther(_Entity_):
                    """
                    odu terminate ether
                    
                    .. attribute:: vether_ifhandle
                    
                    	interface handle
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: ethernet_mapping
                    
                    	ethernet mapping
                    	**type**\:  :py:class:`OduEtherMapPingEt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.OduEtherMapPingEt>`
                    
                    	**config**\: False
                    
                    .. attribute:: ethernet_interface
                    
                    	Ethernet interface name
                    	**type**\: str
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'controller-odu-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Odu.Controllers.Controller.Info.OduTerminateEther, self).__init__()

                        self.yang_name = "odu-terminate-ether"
                        self.yang_parent_name = "info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('vether_ifhandle', (YLeaf(YType.uint32, 'vether-ifhandle'), ['int'])),
                            ('ethernet_mapping', (YLeaf(YType.enumeration, 'ethernet-mapping'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper', 'OduEtherMapPingEt', '')])),
                            ('ethernet_interface', (YLeaf(YType.str, 'ethernet-interface'), ['str'])),
                        ])
                        self.vether_ifhandle = None
                        self.ethernet_mapping = None
                        self.ethernet_interface = None
                        self._segment_path = lambda: "odu-terminate-ether"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Odu.Controllers.Controller.Info.OduTerminateEther, ['vether_ifhandle', 'ethernet_mapping', 'ethernet_interface'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                        return meta._meta_table['Odu.Controllers.Controller.Info.OduTerminateEther']['meta_info']


                class AinsInfo(_Entity_):
                    """
                    AINS information
                    
                    .. attribute:: ains_state
                    
                    	AINS State
                    	**type**\:  :py:class:`OduAinsStateEt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.OduAinsStateEt>`
                    
                    	**config**\: False
                    
                    .. attribute:: ains_timer_minutes
                    
                    	AINS Timer in Minutes
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    	**units**\: minute
                    
                    .. attribute:: ains_remaining_secs
                    
                    	AINS Remaining Seconds
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    	**units**\: second
                    
                    

                    """

                    _prefix = 'controller-odu-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Odu.Controllers.Controller.Info.AinsInfo, self).__init__()

                        self.yang_name = "ains-info"
                        self.yang_parent_name = "info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('ains_state', (YLeaf(YType.enumeration, 'ains-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper', 'OduAinsStateEt', '')])),
                            ('ains_timer_minutes', (YLeaf(YType.uint32, 'ains-timer-minutes'), ['int'])),
                            ('ains_remaining_secs', (YLeaf(YType.uint32, 'ains-remaining-secs'), ['int'])),
                        ])
                        self.ains_state = None
                        self.ains_timer_minutes = None
                        self.ains_remaining_secs = None
                        self._segment_path = lambda: "ains-info"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Odu.Controllers.Controller.Info.AinsInfo, ['ains_state', 'ains_timer_minutes', 'ains_remaining_secs'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                        return meta._meta_table['Odu.Controllers.Controller.Info.AinsInfo']['meta_info']


                class Odu_(_Entity_):
                    """
                    Child Ts
                    
                    .. attribute:: intf_name
                    
                    	Child Interface Name
                    	**type**\: str
                    
                    	**length:** 0..64
                    
                    	**config**\: False
                    
                    .. attribute:: tpn_value
                    
                    	Tpn Bitmap
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: ts_bitmap
                    
                    	Ts Bitmap
                    	**type**\: str
                    
                    	**length:** 0..256
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'controller-odu-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Odu.Controllers.Controller.Info.Odu_, self).__init__()

                        self.yang_name = "odu"
                        self.yang_parent_name = "info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('intf_name', (YLeaf(YType.str, 'intf-name'), ['str'])),
                            ('tpn_value', (YLeaf(YType.uint8, 'tpn-value'), ['int'])),
                            ('ts_bitmap', (YLeaf(YType.str, 'ts-bitmap'), ['str'])),
                        ])
                        self.intf_name = None
                        self.tpn_value = None
                        self.ts_bitmap = None
                        self._segment_path = lambda: "odu"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Odu.Controllers.Controller.Info.Odu_, ['intf_name', 'tpn_value', 'ts_bitmap'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                        return meta._meta_table['Odu.Controllers.Controller.Info.Odu_']['meta_info']


                class Odutcm(_Entity_):
                    """
                    ODU TCM
                    
                    .. attribute:: tcmtti_mode
                    
                    	TTI
                    	**type**\:  :py:class:`TcmttiMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.Odutcm.TcmttiMode>`
                    
                    	**config**\: False
                    
                    .. attribute:: tcmsf
                    
                    	ODU TCM SF in the form of 1.0E \- <SF>
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: tcmsd
                    
                    	ODU TCM SD in the form of 1.0E \- <SD>
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: tcm_state
                    
                    	ODU TCM state
                    	**type**\:  :py:class:`OduTcmStateEt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.OduTcmStateEt>`
                    
                    	**config**\: False
                    
                    .. attribute:: tcmper_mon
                    
                    	Performance Monitoring
                    	**type**\:  :py:class:`OduTcmPerMon <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.OduTcmPerMon>`
                    
                    	**config**\: False
                    
                    .. attribute:: tcm_mode
                    
                    	ODU TCM Mode
                    	**type**\:  :py:class:`OduTcmMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.OduTcmMode>`
                    
                    	**config**\: False
                    
                    .. attribute:: actual_tcm_mode
                    
                    	TCM Mode in H/W
                    	**type**\:  :py:class:`OduTcmMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.OduTcmMode>`
                    
                    	**config**\: False
                    
                    .. attribute:: tcmltc_state
                    
                    	ODU TCM LTC CA state
                    	**type**\:  :py:class:`OduTcmStateEt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.OduTcmStateEt>`
                    
                    	**config**\: False
                    
                    .. attribute:: tcmtim_state
                    
                    	ODU TCM  TIM CAstate
                    	**type**\:  :py:class:`OduTcmStateEt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.OduTcmStateEt>`
                    
                    	**config**\: False
                    
                    .. attribute:: tcm_delay
                    
                    	ODU TCM DELAY
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'controller-odu-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Odu.Controllers.Controller.Info.Odutcm, self).__init__()

                        self.yang_name = "odutcm"
                        self.yang_parent_name = "info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("tcmtti-mode", ("tcmtti_mode", Odu.Controllers.Controller.Info.Odutcm.TcmttiMode))])
                        self._leafs = OrderedDict([
                            ('tcmsf', (YLeaf(YType.uint8, 'tcmsf'), ['int'])),
                            ('tcmsd', (YLeaf(YType.uint8, 'tcmsd'), ['int'])),
                            ('tcm_state', (YLeaf(YType.enumeration, 'tcm-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper', 'OduTcmStateEt', '')])),
                            ('tcmper_mon', (YLeaf(YType.enumeration, 'tcmper-mon'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper', 'OduTcmPerMon', '')])),
                            ('tcm_mode', (YLeaf(YType.enumeration, 'tcm-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper', 'OduTcmMode', '')])),
                            ('actual_tcm_mode', (YLeaf(YType.enumeration, 'actual-tcm-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper', 'OduTcmMode', '')])),
                            ('tcmltc_state', (YLeaf(YType.enumeration, 'tcmltc-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper', 'OduTcmStateEt', '')])),
                            ('tcmtim_state', (YLeaf(YType.enumeration, 'tcmtim-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper', 'OduTcmStateEt', '')])),
                            ('tcm_delay', (YLeaf(YType.uint32, 'tcm-delay'), ['int'])),
                        ])
                        self.tcmsf = None
                        self.tcmsd = None
                        self.tcm_state = None
                        self.tcmper_mon = None
                        self.tcm_mode = None
                        self.actual_tcm_mode = None
                        self.tcmltc_state = None
                        self.tcmtim_state = None
                        self.tcm_delay = None

                        self.tcmtti_mode = Odu.Controllers.Controller.Info.Odutcm.TcmttiMode()
                        self.tcmtti_mode.parent = self
                        self._children_name_map["tcmtti_mode"] = "tcmtti-mode"
                        self._segment_path = lambda: "odutcm"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Odu.Controllers.Controller.Info.Odutcm, ['tcmsf', 'tcmsd', 'tcm_state', 'tcmper_mon', 'tcm_mode', 'actual_tcm_mode', 'tcmltc_state', 'tcmtim_state', 'tcm_delay'], name, value)


                    class TcmttiMode(_Entity_):
                        """
                        TTI
                        
                        .. attribute:: tx
                        
                        	String Sent
                        	**type**\:  :py:class:`Tx <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.Odutcm.TcmttiMode.Tx>`
                        
                        	**config**\: False
                        
                        .. attribute:: exp
                        
                        	String Expected
                        	**type**\:  :py:class:`Exp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.Odutcm.TcmttiMode.Exp>`
                        
                        	**config**\: False
                        
                        .. attribute:: rec
                        
                        	String Received
                        	**type**\:  :py:class:`Rec <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.Odu.Controllers.Controller.Info.Odutcm.TcmttiMode.Rec>`
                        
                        	**config**\: False
                        
                        .. attribute:: g709tti_sent_mode
                        
                        	G709TTI Sent
                        	**type**\:  :py:class:`OduTtiEt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.OduTtiEt>`
                        
                        	**config**\: False
                        
                        .. attribute:: g709tti_exp_mode
                        
                        	G709TTI Expected
                        	**type**\:  :py:class:`OduTtiEt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.OduTtiEt>`
                        
                        	**config**\: False
                        
                        .. attribute:: g709tti_rec_mode
                        
                        	G709TTI Recieved
                        	**type**\:  :py:class:`OduTtiEt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper.OduTtiEt>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-odu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Odu.Controllers.Controller.Info.Odutcm.TcmttiMode, self).__init__()

                            self.yang_name = "tcmtti-mode"
                            self.yang_parent_name = "odutcm"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("tx", ("tx", Odu.Controllers.Controller.Info.Odutcm.TcmttiMode.Tx)), ("exp", ("exp", Odu.Controllers.Controller.Info.Odutcm.TcmttiMode.Exp)), ("rec", ("rec", Odu.Controllers.Controller.Info.Odutcm.TcmttiMode.Rec))])
                            self._leafs = OrderedDict([
                                ('g709tti_sent_mode', (YLeaf(YType.enumeration, 'g709tti-sent-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper', 'OduTtiEt', '')])),
                                ('g709tti_exp_mode', (YLeaf(YType.enumeration, 'g709tti-exp-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper', 'OduTtiEt', '')])),
                                ('g709tti_rec_mode', (YLeaf(YType.enumeration, 'g709tti-rec-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_odu_oper', 'OduTtiEt', '')])),
                            ])
                            self.g709tti_sent_mode = None
                            self.g709tti_exp_mode = None
                            self.g709tti_rec_mode = None

                            self.tx = Odu.Controllers.Controller.Info.Odutcm.TcmttiMode.Tx()
                            self.tx.parent = self
                            self._children_name_map["tx"] = "tx"

                            self.exp = Odu.Controllers.Controller.Info.Odutcm.TcmttiMode.Exp()
                            self.exp.parent = self
                            self._children_name_map["exp"] = "exp"

                            self.rec = Odu.Controllers.Controller.Info.Odutcm.TcmttiMode.Rec()
                            self.rec.parent = self
                            self._children_name_map["rec"] = "rec"
                            self._segment_path = lambda: "tcmtti-mode"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Odu.Controllers.Controller.Info.Odutcm.TcmttiMode, ['g709tti_sent_mode', 'g709tti_exp_mode', 'g709tti_rec_mode'], name, value)


                        class Tx(_Entity_):
                            """
                            String Sent
                            
                            .. attribute:: sapi
                            
                            	tx String
                            	**type**\: list of int
                            
                            	**range:** 0..255
                            
                            	**config**\: False
                            
                            .. attribute:: dapi
                            
                            	exp String
                            	**type**\: list of int
                            
                            	**range:** 0..255
                            
                            	**config**\: False
                            
                            .. attribute:: operator_specific
                            
                            	rec String
                            	**type**\: list of int
                            
                            	**range:** 0..255
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'controller-odu-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Odu.Controllers.Controller.Info.Odutcm.TcmttiMode.Tx, self).__init__()

                                self.yang_name = "tx"
                                self.yang_parent_name = "tcmtti-mode"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('sapi', (YLeafList(YType.uint8, 'sapi'), ['int'])),
                                    ('dapi', (YLeafList(YType.uint8, 'dapi'), ['int'])),
                                    ('operator_specific', (YLeafList(YType.uint8, 'operator-specific'), ['int'])),
                                ])
                                self.sapi = []
                                self.dapi = []
                                self.operator_specific = []
                                self._segment_path = lambda: "tx"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Odu.Controllers.Controller.Info.Odutcm.TcmttiMode.Tx, ['sapi', 'dapi', 'operator_specific'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                                return meta._meta_table['Odu.Controllers.Controller.Info.Odutcm.TcmttiMode.Tx']['meta_info']


                        class Exp(_Entity_):
                            """
                            String Expected
                            
                            .. attribute:: sapi
                            
                            	tx String
                            	**type**\: list of int
                            
                            	**range:** 0..255
                            
                            	**config**\: False
                            
                            .. attribute:: dapi
                            
                            	exp String
                            	**type**\: list of int
                            
                            	**range:** 0..255
                            
                            	**config**\: False
                            
                            .. attribute:: operator_specific
                            
                            	rec String
                            	**type**\: list of int
                            
                            	**range:** 0..255
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'controller-odu-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Odu.Controllers.Controller.Info.Odutcm.TcmttiMode.Exp, self).__init__()

                                self.yang_name = "exp"
                                self.yang_parent_name = "tcmtti-mode"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('sapi', (YLeafList(YType.uint8, 'sapi'), ['int'])),
                                    ('dapi', (YLeafList(YType.uint8, 'dapi'), ['int'])),
                                    ('operator_specific', (YLeafList(YType.uint8, 'operator-specific'), ['int'])),
                                ])
                                self.sapi = []
                                self.dapi = []
                                self.operator_specific = []
                                self._segment_path = lambda: "exp"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Odu.Controllers.Controller.Info.Odutcm.TcmttiMode.Exp, ['sapi', 'dapi', 'operator_specific'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                                return meta._meta_table['Odu.Controllers.Controller.Info.Odutcm.TcmttiMode.Exp']['meta_info']


                        class Rec(_Entity_):
                            """
                            String Received
                            
                            .. attribute:: sapi
                            
                            	tx String
                            	**type**\: list of int
                            
                            	**range:** 0..255
                            
                            	**config**\: False
                            
                            .. attribute:: dapi
                            
                            	exp String
                            	**type**\: list of int
                            
                            	**range:** 0..255
                            
                            	**config**\: False
                            
                            .. attribute:: operator_specific
                            
                            	rec String
                            	**type**\: list of int
                            
                            	**range:** 0..255
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'controller-odu-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Odu.Controllers.Controller.Info.Odutcm.TcmttiMode.Rec, self).__init__()

                                self.yang_name = "rec"
                                self.yang_parent_name = "tcmtti-mode"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('sapi', (YLeafList(YType.uint8, 'sapi'), ['int'])),
                                    ('dapi', (YLeafList(YType.uint8, 'dapi'), ['int'])),
                                    ('operator_specific', (YLeafList(YType.uint8, 'operator-specific'), ['int'])),
                                ])
                                self.sapi = []
                                self.dapi = []
                                self.operator_specific = []
                                self._segment_path = lambda: "rec"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Odu.Controllers.Controller.Info.Odutcm.TcmttiMode.Rec, ['sapi', 'dapi', 'operator_specific'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                                return meta._meta_table['Odu.Controllers.Controller.Info.Odutcm.TcmttiMode.Rec']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                            return meta._meta_table['Odu.Controllers.Controller.Info.Odutcm.TcmttiMode']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                        return meta._meta_table['Odu.Controllers.Controller.Info.Odutcm']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                    return meta._meta_table['Odu.Controllers.Controller.Info']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
                return meta._meta_table['Odu.Controllers.Controller']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
            return meta._meta_table['Odu.Controllers']['meta_info']

    def clone_ptr(self):
        self._top_entity = Odu()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_odu_oper as meta
        return meta._meta_table['Odu']['meta_info']


