""" Cisco_IOS_XR_controller_optics_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR controller\-optics package operational data.

This module contains definitions
for the following management objects\:
  optics\-oper\: Optics operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class EthernetPmd(Enum):
    """
    EthernetPmd

    Ethernet Pmd Type

    .. data:: optics_eth_not_set = 0

    	Not set

    .. data:: optics_eth_10gbase_lrm = 1

    	10GBASE LRM

    .. data:: optics_eth_10gbase_lr = 2

    	10GBASE LR

    .. data:: optics_eth_10gbase_zr = 3

    	10GBASE ZR

    .. data:: optics_eth_10gbase_er = 4

    	10GBASE ER

    .. data:: optics_eth_10gbase_sr = 5

    	10GBASE SR

    .. data:: optics_eth_10gbase = 6

    	10GBASE T

    .. data:: optics_eth_40gbase_cr4 = 7

    	40GBASE CR4

    .. data:: optics_eth_40gbase_sr4 = 8

    	40GBASE SR4

    .. data:: optics_eth_40gbase_lr4 = 9

    	40GBASE LR4

    .. data:: optics_eth_40gbase_er4 = 10

    	40GBASE ER4

    .. data:: optics_eth_40gbase_psm4 = 11

    	40GBASE PSM4

    .. data:: optics_eth_40gbase_csr4 = 12

    	40GBASE CSR4

    .. data:: optics_eth_40gbase_sr_bd = 13

    	40GBASE SR BD

    .. data:: optics_eth_40g_aoc = 14

    	40G AOC

    .. data:: optics_eth_4x10gbase_lr = 15

    	4X10GBASE LR

    .. data:: optics_eth_4x10gbase_sr = 16

    	4X10GBASE SR

    .. data:: optics_eth_100g_aoc = 17

    	100G AOC

    .. data:: optics_eth_100g_acc = 18

    	100G ACC

    .. data:: optics_eth_100gbase_sr10 = 19

    	100GBASE SR10

    .. data:: optics_eth_100gbase_sr4 = 20

    	100GBASE SR4

    .. data:: optics_eth_100gbase_lr4 = 21

    	100GBASE LR4

    .. data:: optics_eth_100gbase_er4 = 22

    	100GBASE ER4

    .. data:: optics_eth_100gbase_cwdm4 = 23

    	100GBASE CWDM4

    .. data:: optics_eth_100gbase_clr4 = 24

    	100GBASE CLR4

    .. data:: optics_eth_100gbase_psm4 = 25

    	100GBASE PSM4

    .. data:: optics_eth_100gbase_cr4 = 26

    	100GBASE CR4

    .. data:: optics_eth_100gbase_al = 27

    	100GBASE AL

    .. data:: optics_eth_100gbase_pl = 28

    	100GBASE PL

    .. data:: optics_eth_undefined = 29

    	Eth Undefined

    """

    optics_eth_not_set = Enum.YLeaf(0, "optics-eth-not-set")

    optics_eth_10gbase_lrm = Enum.YLeaf(1, "optics-eth-10gbase-lrm")

    optics_eth_10gbase_lr = Enum.YLeaf(2, "optics-eth-10gbase-lr")

    optics_eth_10gbase_zr = Enum.YLeaf(3, "optics-eth-10gbase-zr")

    optics_eth_10gbase_er = Enum.YLeaf(4, "optics-eth-10gbase-er")

    optics_eth_10gbase_sr = Enum.YLeaf(5, "optics-eth-10gbase-sr")

    optics_eth_10gbase = Enum.YLeaf(6, "optics-eth-10gbase")

    optics_eth_40gbase_cr4 = Enum.YLeaf(7, "optics-eth-40gbase-cr4")

    optics_eth_40gbase_sr4 = Enum.YLeaf(8, "optics-eth-40gbase-sr4")

    optics_eth_40gbase_lr4 = Enum.YLeaf(9, "optics-eth-40gbase-lr4")

    optics_eth_40gbase_er4 = Enum.YLeaf(10, "optics-eth-40gbase-er4")

    optics_eth_40gbase_psm4 = Enum.YLeaf(11, "optics-eth-40gbase-psm4")

    optics_eth_40gbase_csr4 = Enum.YLeaf(12, "optics-eth-40gbase-csr4")

    optics_eth_40gbase_sr_bd = Enum.YLeaf(13, "optics-eth-40gbase-sr-bd")

    optics_eth_40g_aoc = Enum.YLeaf(14, "optics-eth-40g-aoc")

    optics_eth_4x10gbase_lr = Enum.YLeaf(15, "optics-eth-4x10gbase-lr")

    optics_eth_4x10gbase_sr = Enum.YLeaf(16, "optics-eth-4x10gbase-sr")

    optics_eth_100g_aoc = Enum.YLeaf(17, "optics-eth-100g-aoc")

    optics_eth_100g_acc = Enum.YLeaf(18, "optics-eth-100g-acc")

    optics_eth_100gbase_sr10 = Enum.YLeaf(19, "optics-eth-100gbase-sr10")

    optics_eth_100gbase_sr4 = Enum.YLeaf(20, "optics-eth-100gbase-sr4")

    optics_eth_100gbase_lr4 = Enum.YLeaf(21, "optics-eth-100gbase-lr4")

    optics_eth_100gbase_er4 = Enum.YLeaf(22, "optics-eth-100gbase-er4")

    optics_eth_100gbase_cwdm4 = Enum.YLeaf(23, "optics-eth-100gbase-cwdm4")

    optics_eth_100gbase_clr4 = Enum.YLeaf(24, "optics-eth-100gbase-clr4")

    optics_eth_100gbase_psm4 = Enum.YLeaf(25, "optics-eth-100gbase-psm4")

    optics_eth_100gbase_cr4 = Enum.YLeaf(26, "optics-eth-100gbase-cr4")

    optics_eth_100gbase_al = Enum.YLeaf(27, "optics-eth-100gbase-al")

    optics_eth_100gbase_pl = Enum.YLeaf(28, "optics-eth-100gbase-pl")

    optics_eth_undefined = Enum.YLeaf(29, "optics-eth-undefined")


class FiberConnector(Enum):
    """
    FiberConnector

    Fiber connector

    .. data:: optics_connect_or_not_set = 0

    	Not Set

    .. data:: optics_sc_connect_or = 1

    	SC

    .. data:: optics_lc_connect_or = 2

    	LC

    .. data:: optics_mpo_connect_or = 3

    	MPO

    .. data:: optics_undefined_connect_or = 4

    	Undefined

    """

    optics_connect_or_not_set = Enum.YLeaf(0, "optics-connect-or-not-set")

    optics_sc_connect_or = Enum.YLeaf(1, "optics-sc-connect-or")

    optics_lc_connect_or = Enum.YLeaf(2, "optics-lc-connect-or")

    optics_mpo_connect_or = Enum.YLeaf(3, "optics-mpo-connect-or")

    optics_undefined_connect_or = Enum.YLeaf(4, "optics-undefined-connect-or")


class Optics(Enum):
    """
    Optics

    Optics

    .. data:: optics_unknown = 0

    	Unknow Optics Type

    .. data:: optics_grey = 1

    	Grey Optics

    .. data:: optics_dwdm = 2

    	DWDM Optics

    .. data:: optics_cwdm = 3

    	CWDM Optics

    """

    optics_unknown = Enum.YLeaf(0, "optics-unknown")

    optics_grey = Enum.YLeaf(1, "optics-grey")

    optics_dwdm = Enum.YLeaf(2, "optics-dwdm")

    optics_cwdm = Enum.YLeaf(3, "optics-cwdm")


class OpticsAmplifierControlMode(Enum):
    """
    OpticsAmplifierControlMode

    Optics amplifier control mode

    .. data:: automatic = 1

    	Automatic

    .. data:: manual = 2

    	Manual

    """

    automatic = Enum.YLeaf(1, "automatic")

    manual = Enum.YLeaf(2, "manual")


class OpticsAmplifierGainRange(Enum):
    """
    OpticsAmplifierGainRange

    Optics amplifier gain range

    .. data:: optics_amplifier_gain_range_normal = 1

    	Normal

    .. data:: optics_amplifier_gain_range_ext_end_ed = 2

    	Extended

    """

    optics_amplifier_gain_range_normal = Enum.YLeaf(1, "optics-amplifier-gain-range-normal")

    optics_amplifier_gain_range_ext_end_ed = Enum.YLeaf(2, "optics-amplifier-gain-range-ext-end-ed")


class OpticsAmplifierSafetyControlMode(Enum):
    """
    OpticsAmplifierSafetyControlMode

    Optics amplifier safety control mode

    .. data:: optics_amplifier_safety_mode_auto = 1

    	auto

    .. data:: optics_amplifier_safety_mode_disabled = 2

    	disabled

    """

    optics_amplifier_safety_mode_auto = Enum.YLeaf(1, "optics-amplifier-safety-mode-auto")

    optics_amplifier_safety_mode_disabled = Enum.YLeaf(2, "optics-amplifier-safety-mode-disabled")


class OpticsControllerState(Enum):
    """
    OpticsControllerState

    Optics controller state

    .. data:: optics_state_up = 0

    	Up

    .. data:: optics_state_down = 1

    	Down

    .. data:: optics_state_admin_down = 2

    	Administratively Down

    """

    optics_state_up = Enum.YLeaf(0, "optics-state-up")

    optics_state_down = Enum.YLeaf(1, "optics-state-down")

    optics_state_admin_down = Enum.YLeaf(2, "optics-state-admin-down")


class OpticsFec(Enum):
    """
    OpticsFec

    Optics fec

    .. data:: fec_none = 0

    	FEC NONE

    .. data:: fec_hg15 = 1

    	ENHANCED FEC H15

    .. data:: fec_hg25 = 2

    	ENHANCED FEC H25

    .. data:: fec_hg15_de = 4

    	FEC HG15 DE

    .. data:: fec_hg25_de = 8

    	FEC HG25 DE

    .. data:: fec_enabled = 16

    	FEC ENABLED

    """

    fec_none = Enum.YLeaf(0, "fec-none")

    fec_hg15 = Enum.YLeaf(1, "fec-hg15")

    fec_hg25 = Enum.YLeaf(2, "fec-hg25")

    fec_hg15_de = Enum.YLeaf(4, "fec-hg15-de")

    fec_hg25_de = Enum.YLeaf(8, "fec-hg25-de")

    fec_enabled = Enum.YLeaf(16, "fec-enabled")


class OpticsFormFactor(Enum):
    """
    OpticsFormFactor

    Optics form factor

    .. data:: not_set = 0

    	Not set

    .. data:: invalid = 1

    	Invalid

    .. data:: cpak = 2

    	CPAK

    .. data:: cxp = 3

    	CXP

    .. data:: sfp_plus = 4

    	SFP+

    .. data:: qsfp = 5

    	QSFP

    .. data:: qsfp_plus = 6

    	QSFP+

    .. data:: qsfp28 = 7

    	QSFP28

    .. data:: sfp = 8

    	SFP

    .. data:: cfp = 9

    	CFP

    .. data:: cfp2 = 10

    	CFP2

    .. data:: cfp4 = 11

    	CFP4

    .. data:: xfp = 12

    	XFP

    .. data:: x2 = 13

    	X2

    .. data:: non_pluggable = 14

    	Non pluggable

    .. data:: other = 15

    	Other

    """

    not_set = Enum.YLeaf(0, "not-set")

    invalid = Enum.YLeaf(1, "invalid")

    cpak = Enum.YLeaf(2, "cpak")

    cxp = Enum.YLeaf(3, "cxp")

    sfp_plus = Enum.YLeaf(4, "sfp-plus")

    qsfp = Enum.YLeaf(5, "qsfp")

    qsfp_plus = Enum.YLeaf(6, "qsfp-plus")

    qsfp28 = Enum.YLeaf(7, "qsfp28")

    sfp = Enum.YLeaf(8, "sfp")

    cfp = Enum.YLeaf(9, "cfp")

    cfp2 = Enum.YLeaf(10, "cfp2")

    cfp4 = Enum.YLeaf(11, "cfp4")

    xfp = Enum.YLeaf(12, "xfp")

    x2 = Enum.YLeaf(13, "x2")

    non_pluggable = Enum.YLeaf(14, "non-pluggable")

    other = Enum.YLeaf(15, "other")


class OpticsLaserState(Enum):
    """
    OpticsLaserState

    Optics laser state

    .. data:: on = 0

    	On

    .. data:: off = 1

    	Off

    .. data:: unknown = 2

    	Unknown

    .. data:: apr = 3

    	Apr

    """

    on = Enum.YLeaf(0, "on")

    off = Enum.YLeaf(1, "off")

    unknown = Enum.YLeaf(2, "unknown")

    apr = Enum.YLeaf(3, "apr")


class OpticsLedState(Enum):
    """
    OpticsLedState

    Optics led state

    .. data:: off = 0

    	Off

    .. data:: green_on = 1

    	Green

    .. data:: green_flashing = 2

    	Green Flashing

    .. data:: yellow_on = 3

    	Yellow

    .. data:: yellow_flashing = 4

    	Yellow Flashing

    .. data:: red_on = 5

    	Red

    .. data:: red_flashing = 6

    	Red Flashing

    """

    off = Enum.YLeaf(0, "off")

    green_on = Enum.YLeaf(1, "green-on")

    green_flashing = Enum.YLeaf(2, "green-flashing")

    yellow_on = Enum.YLeaf(3, "yellow-on")

    yellow_flashing = Enum.YLeaf(4, "yellow-flashing")

    red_on = Enum.YLeaf(5, "red-on")

    red_flashing = Enum.YLeaf(6, "red-flashing")


class OpticsPhy(Enum):
    """
    OpticsPhy

    Optics phy type

    .. data:: not_set = 0

    	Not set

    .. data:: invalid = 1

    	Invalid

    .. data:: long_reach_four_lanes = 2

    	Long reach 4 lanes

    .. data:: short_reach_ten_lanes = 3

    	Short reach 10 lanes

    .. data:: short_reach_one_lane = 4

    	Short reach 1 lane

    .. data:: long_reach_one_lane = 5

    	Long reach 1 lane

    .. data:: short_reach_four_lanes = 6

    	Short reach 4 lanes

    .. data:: copper_four_lanes = 7

    	Copper 4 lanes

    .. data:: active_optical_cable = 8

    	Active optical cable

    .. data:: fourty_gig_e_long_reach_four_lanes = 9

    	Long reach 4 lanes

    .. data:: fourty_gig_e_short_reach_four_lanes = 10

    	Short reach 4 lanes

    .. data:: cwdm_four_lanes = 11

    	CWDM 4 lanes

    .. data:: extended_reach_four_lanes = 12

    	Extended reach 4 lanes

    .. data:: psm_four_lanes = 13

    	PSM 4 lanes

    .. data:: active_copper_cable = 14

    	Active copper cable

    .. data:: fourty_gig_e_extended_reach_four_lanes = 15

    	Extended reach 4 lanes

    .. data:: four_x_ten_gig_e_short_reach_one_lane = 16

    	Short reach 1 lane

    .. data:: fourty_gig_epsm_four_lanes = 17

    	PSM 4 lanes

    .. data:: fourty_gig_e_copper_four_lanes = 18

    	Copper 4 lanes

    .. data:: long_reach_mm_one_lane = 19

    	Long reach MM 1 lane

    .. data:: copper_short_reach = 20

    	Copper Short reach 4 lanes

    .. data:: short_reach_srbd = 21

    	Short reach BD 4 lanes

    .. data:: copper_one_lane = 22

    	Copper One Lane

    .. data:: four_x_ten_gig_e_long_reach_one_lane = 23

    	Long reach 1 lane

    .. data:: fourty_gig_eaoc_four_lanes = 24

    	Active optical cable

    .. data:: extended_one_lane = 25

    	Extended One Lane

    .. data:: zr_one_lane = 26

    	ZR One Lane

    .. data:: dwdm_one_lane = 27

    	DWDM One Lane

    .. data:: sx_one_lane = 28

    	SX One Lane

    .. data:: lx_one_lane = 29

    	LX One Lane

    .. data:: ex_one_lane = 30

    	EX One Lane

    .. data:: zx_one_lane = 31

    	ZX One Lane

    .. data:: ba_set_one_lane = 32

    	BASE_T One Lane

    .. data:: aoc_one_lane = 33

    	Active Optical 1 Lane

    .. data:: active_copper_one_lane = 34

    	Active Copper 1 Lane

    .. data:: fourty_gig_eacu_four_lanes = 35

    	Active Copper 4 Lanes

    .. data:: four_x_ten_gig_eacu_one_lanes = 36

    	Active Copper 1 Lane

    .. data:: four_x_ten_gig_ecu_one_lanes = 37

    	Copper 1 Lanes

    .. data:: four_x_ten_gig_eaoc_one_lanes = 38

    	Active Optics 1 Lane

    .. data:: twenty_five_gig_short_reach_one_lane = 39

    	Short reach 1 lane

    .. data:: twenty_five_gig_long_reach_one_lane = 40

    	Long reach 1 lane

    .. data:: twenty_five_gig_extended_reach_one_lane = 41

    	Extended reach 1 lane

    .. data:: twenty_five_gig_copper_one_lane = 42

    	Copper One Lane

    .. data:: twenty_five_gig_active_optical_one_lane = 43

    	Active Optical One Lane

    .. data:: hundred_gig_edwdm_two = 44

    	100GE DWDM Optics

    .. data:: fourty_gig_plr4_four_lanes = 45

    	PLR4 Optics

    .. data:: fourty_gig_esr4_four_lanes = 46

    	ESR4 Optics

    .. data:: smsr_four_lanes = 47

    	SMSR Optics

    .. data:: cazadero_rqsa = 48

    	Cazadero R

    .. data:: trunk_port_cfp2 = 49

    	CFP2 DWDM Optics

    .. data:: short_reach1_lane = 50

    	Short reach 1 lane

    .. data:: inmd_reach1lane = 51

    	Inmd reach 1 lane

    .. data:: long_reach1_lane = 52

    	Long reach 1 lane

    .. data:: twenty_five_gig_ecu_one_lanes = 53

    	Copper 1 Lanes

    .. data:: hundred_gig_e = 54

    	ExtentedReach4Lane

    """

    not_set = Enum.YLeaf(0, "not-set")

    invalid = Enum.YLeaf(1, "invalid")

    long_reach_four_lanes = Enum.YLeaf(2, "long-reach-four-lanes")

    short_reach_ten_lanes = Enum.YLeaf(3, "short-reach-ten-lanes")

    short_reach_one_lane = Enum.YLeaf(4, "short-reach-one-lane")

    long_reach_one_lane = Enum.YLeaf(5, "long-reach-one-lane")

    short_reach_four_lanes = Enum.YLeaf(6, "short-reach-four-lanes")

    copper_four_lanes = Enum.YLeaf(7, "copper-four-lanes")

    active_optical_cable = Enum.YLeaf(8, "active-optical-cable")

    fourty_gig_e_long_reach_four_lanes = Enum.YLeaf(9, "fourty-gig-e-long-reach-four-lanes")

    fourty_gig_e_short_reach_four_lanes = Enum.YLeaf(10, "fourty-gig-e-short-reach-four-lanes")

    cwdm_four_lanes = Enum.YLeaf(11, "cwdm-four-lanes")

    extended_reach_four_lanes = Enum.YLeaf(12, "extended-reach-four-lanes")

    psm_four_lanes = Enum.YLeaf(13, "psm-four-lanes")

    active_copper_cable = Enum.YLeaf(14, "active-copper-cable")

    fourty_gig_e_extended_reach_four_lanes = Enum.YLeaf(15, "fourty-gig-e-extended-reach-four-lanes")

    four_x_ten_gig_e_short_reach_one_lane = Enum.YLeaf(16, "four-x-ten-gig-e-short-reach-one-lane")

    fourty_gig_epsm_four_lanes = Enum.YLeaf(17, "fourty-gig-epsm-four-lanes")

    fourty_gig_e_copper_four_lanes = Enum.YLeaf(18, "fourty-gig-e-copper-four-lanes")

    long_reach_mm_one_lane = Enum.YLeaf(19, "long-reach-mm-one-lane")

    copper_short_reach = Enum.YLeaf(20, "copper-short-reach")

    short_reach_srbd = Enum.YLeaf(21, "short-reach-srbd")

    copper_one_lane = Enum.YLeaf(22, "copper-one-lane")

    four_x_ten_gig_e_long_reach_one_lane = Enum.YLeaf(23, "four-x-ten-gig-e-long-reach-one-lane")

    fourty_gig_eaoc_four_lanes = Enum.YLeaf(24, "fourty-gig-eaoc-four-lanes")

    extended_one_lane = Enum.YLeaf(25, "extended-one-lane")

    zr_one_lane = Enum.YLeaf(26, "zr-one-lane")

    dwdm_one_lane = Enum.YLeaf(27, "dwdm-one-lane")

    sx_one_lane = Enum.YLeaf(28, "sx-one-lane")

    lx_one_lane = Enum.YLeaf(29, "lx-one-lane")

    ex_one_lane = Enum.YLeaf(30, "ex-one-lane")

    zx_one_lane = Enum.YLeaf(31, "zx-one-lane")

    ba_set_one_lane = Enum.YLeaf(32, "ba-set-one-lane")

    aoc_one_lane = Enum.YLeaf(33, "aoc-one-lane")

    active_copper_one_lane = Enum.YLeaf(34, "active-copper-one-lane")

    fourty_gig_eacu_four_lanes = Enum.YLeaf(35, "fourty-gig-eacu-four-lanes")

    four_x_ten_gig_eacu_one_lanes = Enum.YLeaf(36, "four-x-ten-gig-eacu-one-lanes")

    four_x_ten_gig_ecu_one_lanes = Enum.YLeaf(37, "four-x-ten-gig-ecu-one-lanes")

    four_x_ten_gig_eaoc_one_lanes = Enum.YLeaf(38, "four-x-ten-gig-eaoc-one-lanes")

    twenty_five_gig_short_reach_one_lane = Enum.YLeaf(39, "twenty-five-gig-short-reach-one-lane")

    twenty_five_gig_long_reach_one_lane = Enum.YLeaf(40, "twenty-five-gig-long-reach-one-lane")

    twenty_five_gig_extended_reach_one_lane = Enum.YLeaf(41, "twenty-five-gig-extended-reach-one-lane")

    twenty_five_gig_copper_one_lane = Enum.YLeaf(42, "twenty-five-gig-copper-one-lane")

    twenty_five_gig_active_optical_one_lane = Enum.YLeaf(43, "twenty-five-gig-active-optical-one-lane")

    hundred_gig_edwdm_two = Enum.YLeaf(44, "hundred-gig-edwdm-two")

    fourty_gig_plr4_four_lanes = Enum.YLeaf(45, "fourty-gig-plr4-four-lanes")

    fourty_gig_esr4_four_lanes = Enum.YLeaf(46, "fourty-gig-esr4-four-lanes")

    smsr_four_lanes = Enum.YLeaf(47, "smsr-four-lanes")

    cazadero_rqsa = Enum.YLeaf(48, "cazadero-rqsa")

    trunk_port_cfp2 = Enum.YLeaf(49, "trunk-port-cfp2")

    short_reach1_lane = Enum.YLeaf(50, "short-reach1-lane")

    inmd_reach1lane = Enum.YLeaf(51, "inmd-reach1lane")

    long_reach1_lane = Enum.YLeaf(52, "long-reach1-lane")

    twenty_five_gig_ecu_one_lanes = Enum.YLeaf(53, "twenty-five-gig-ecu-one-lanes")

    hundred_gig_e = Enum.YLeaf(54, "hundred-gig-e")


class OpticsPort(Enum):
    """
    OpticsPort

    Optics port

    .. data:: com = 0

    	Com

    .. data:: line = 1

    	Line

    .. data:: osc = 2

    	Osc

    .. data:: com_check = 3

    	Com Check

    .. data:: work = 4

    	Working

    .. data:: prot = 5

    	Protected

    """

    com = Enum.YLeaf(0, "com")

    line = Enum.YLeaf(1, "line")

    osc = Enum.YLeaf(2, "osc")

    com_check = Enum.YLeaf(3, "com-check")

    work = Enum.YLeaf(4, "work")

    prot = Enum.YLeaf(5, "prot")


class OpticsPortStatus(Enum):
    """
    OpticsPortStatus

    Optics port status

    .. data:: active = 0

    	Active

    .. data:: standby = 1

    	Standby

    """

    active = Enum.YLeaf(0, "active")

    standby = Enum.YLeaf(1, "standby")


class OpticsTas(Enum):
    """
    OpticsTas

    Optics tas

    .. data:: tas_ui_oos = 0

    	Out Of Service

    .. data:: tas_ui_main = 1

    	Maintenance

    .. data:: tas_ui_is = 2

    	In Service

    .. data:: tas_ui_ains = 3

    	Automatic In Service

    """

    tas_ui_oos = Enum.YLeaf(0, "tas-ui-oos")

    tas_ui_main = Enum.YLeaf(1, "tas-ui-main")

    tas_ui_is = Enum.YLeaf(2, "tas-ui-is")

    tas_ui_ains = Enum.YLeaf(3, "tas-ui-ains")


class OpticsWaveBand(Enum):
    """
    OpticsWaveBand

    Optics wave band

    .. data:: c_band = 0

    	C BAND

    .. data:: l_band = 1

    	L BAND

    .. data:: c_band_odd = 2

    	C ODD

    .. data:: c_band_even = 3

    	C EVEN

    .. data:: invalid_band = 4

    	Invalid

    """

    c_band = Enum.YLeaf(0, "c-band")

    l_band = Enum.YLeaf(1, "l-band")

    c_band_odd = Enum.YLeaf(2, "c-band-odd")

    c_band_even = Enum.YLeaf(3, "c-band-even")

    invalid_band = Enum.YLeaf(4, "invalid-band")


class OtnApplicationCode(Enum):
    """
    OtnApplicationCode

    Otn application code

    .. data:: optics_not_set = 0

    	Not Set

    .. data:: optics_p1l1_2d1 = 1

    	P1L1 2D1

    .. data:: optics_p1s1_2d2 = 2

    	P1S1 2D2

    .. data:: optics_p1l1_2d2 = 3

    	P1L1 2D2

    .. data:: optics_undefined = 4

    	Undefined

    """

    optics_not_set = Enum.YLeaf(0, "optics-not-set")

    optics_p1l1_2d1 = Enum.YLeaf(1, "optics-p1l1-2d1")

    optics_p1s1_2d2 = Enum.YLeaf(2, "optics-p1s1-2d2")

    optics_p1l1_2d2 = Enum.YLeaf(3, "optics-p1l1-2d2")

    optics_undefined = Enum.YLeaf(4, "optics-undefined")


class SonetApplicationCode(Enum):
    """
    SonetApplicationCode

    Sonet application code

    .. data:: optics_sonet_not_set = 0

    	Not Set

    .. data:: optics_vsr2000_3r2 = 1

    	VSR2000 3R2

    .. data:: optics_vsr2000_3r3 = 2

    	VSR2000 3R3

    .. data:: optics_vsr2000_3r5 = 3

    	VSR2000 3R5

    .. data:: optics_sonet_undefined = 4

    	Undefined

    """

    optics_sonet_not_set = Enum.YLeaf(0, "optics-sonet-not-set")

    optics_vsr2000_3r2 = Enum.YLeaf(1, "optics-vsr2000-3r2")

    optics_vsr2000_3r3 = Enum.YLeaf(2, "optics-vsr2000-3r3")

    optics_vsr2000_3r5 = Enum.YLeaf(3, "optics-vsr2000-3r5")

    optics_sonet_undefined = Enum.YLeaf(4, "optics-sonet-undefined")



class OpticsOper(Entity):
    """
    Optics operational data
    
    .. attribute:: optics_ports
    
    	All Optics Port operational data
    	**type**\:   :py:class:`OpticsPorts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts>`
    
    

    """

    _prefix = 'controller-optics-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(OpticsOper, self).__init__()
        self._top_entity = None

        self.yang_name = "optics-oper"
        self.yang_parent_name = "Cisco-IOS-XR-controller-optics-oper"

        self.optics_ports = OpticsOper.OpticsPorts()
        self.optics_ports.parent = self
        self._children_name_map["optics_ports"] = "optics-ports"
        self._children_yang_names.add("optics-ports")


    class OpticsPorts(Entity):
        """
        All Optics Port operational data
        
        .. attribute:: optics_port
        
        	Optics operational data
        	**type**\: list of    :py:class:`OpticsPort <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort>`
        
        

        """

        _prefix = 'controller-optics-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(OpticsOper.OpticsPorts, self).__init__()

            self.yang_name = "optics-ports"
            self.yang_parent_name = "optics-oper"

            self.optics_port = YList(self)

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
                        super(OpticsOper.OpticsPorts, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(OpticsOper.OpticsPorts, self).__setattr__(name, value)


        class OpticsPort(Entity):
            """
            Optics operational data
            
            .. attribute:: name  <key>
            
            	Port name
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: optics_db_info
            
            	Optics operational data
            	**type**\:   :py:class:`OpticsDbInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsDbInfo>`
            
            .. attribute:: optics_dwdm_carrrier_channel_map
            
            	Optics operational data
            	**type**\:   :py:class:`OpticsDwdmCarrrierChannelMap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsDwdmCarrrierChannelMap>`
            
            .. attribute:: optics_info
            
            	Optics operational data
            	**type**\:   :py:class:`OpticsInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo>`
            
            .. attribute:: optics_lanes
            
            	All Optics Port operational data
            	**type**\:   :py:class:`OpticsLanes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsLanes>`
            
            

            """

            _prefix = 'controller-optics-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(OpticsOper.OpticsPorts.OpticsPort, self).__init__()

                self.yang_name = "optics-port"
                self.yang_parent_name = "optics-ports"

                self.name = YLeaf(YType.str, "name")

                self.optics_db_info = OpticsOper.OpticsPorts.OpticsPort.OpticsDbInfo()
                self.optics_db_info.parent = self
                self._children_name_map["optics_db_info"] = "optics-db-info"
                self._children_yang_names.add("optics-db-info")

                self.optics_dwdm_carrrier_channel_map = OpticsOper.OpticsPorts.OpticsPort.OpticsDwdmCarrrierChannelMap()
                self.optics_dwdm_carrrier_channel_map.parent = self
                self._children_name_map["optics_dwdm_carrrier_channel_map"] = "optics-dwdm-carrrier-channel-map"
                self._children_yang_names.add("optics-dwdm-carrrier-channel-map")

                self.optics_info = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo()
                self.optics_info.parent = self
                self._children_name_map["optics_info"] = "optics-info"
                self._children_yang_names.add("optics-info")

                self.optics_lanes = OpticsOper.OpticsPorts.OpticsPort.OpticsLanes()
                self.optics_lanes.parent = self
                self._children_name_map["optics_lanes"] = "optics-lanes"
                self._children_yang_names.add("optics-lanes")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("name") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(OpticsOper.OpticsPorts.OpticsPort, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(OpticsOper.OpticsPorts.OpticsPort, self).__setattr__(name, value)


            class OpticsDwdmCarrrierChannelMap(Entity):
                """
                Optics operational data
                
                .. attribute:: dwdm_carrier_band
                
                	DWDM carrier band
                	**type**\:   :py:class:`OpticsWaveBand <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsWaveBand>`
                
                .. attribute:: dwdm_carrier_map_info
                
                	DWDM carrier mapping info
                	**type**\: list of    :py:class:`DwdmCarrierMapInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsDwdmCarrrierChannelMap.DwdmCarrierMapInfo>`
                
                .. attribute:: dwdm_carrier_max
                
                	Highest DWDM carrier supported
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: dwdm_carrier_min
                
                	Lowest DWDM carrier supported
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'controller-optics-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(OpticsOper.OpticsPorts.OpticsPort.OpticsDwdmCarrrierChannelMap, self).__init__()

                    self.yang_name = "optics-dwdm-carrrier-channel-map"
                    self.yang_parent_name = "optics-port"

                    self.dwdm_carrier_band = YLeaf(YType.enumeration, "dwdm-carrier-band")

                    self.dwdm_carrier_max = YLeaf(YType.uint32, "dwdm-carrier-max")

                    self.dwdm_carrier_min = YLeaf(YType.uint32, "dwdm-carrier-min")

                    self.dwdm_carrier_map_info = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("dwdm_carrier_band",
                                    "dwdm_carrier_max",
                                    "dwdm_carrier_min") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(OpticsOper.OpticsPorts.OpticsPort.OpticsDwdmCarrrierChannelMap, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsDwdmCarrrierChannelMap, self).__setattr__(name, value)


                class DwdmCarrierMapInfo(Entity):
                    """
                    DWDM carrier mapping info
                    
                    .. attribute:: frequency
                    
                    	Frequency
                    	**type**\:  str
                    
                    	**length:** 0..32
                    
                    .. attribute:: g694_chan_num
                    
                    	G694 channel number
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: itu_chan_num
                    
                    	ITU channel number
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: wavelength
                    
                    	Wavelength
                    	**type**\:  str
                    
                    	**length:** 0..32
                    
                    

                    """

                    _prefix = 'controller-optics-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsDwdmCarrrierChannelMap.DwdmCarrierMapInfo, self).__init__()

                        self.yang_name = "dwdm-carrier-map-info"
                        self.yang_parent_name = "optics-dwdm-carrrier-channel-map"

                        self.frequency = YLeaf(YType.str, "frequency")

                        self.g694_chan_num = YLeaf(YType.int32, "g694-chan-num")

                        self.itu_chan_num = YLeaf(YType.uint32, "itu-chan-num")

                        self.wavelength = YLeaf(YType.str, "wavelength")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("frequency",
                                        "g694_chan_num",
                                        "itu_chan_num",
                                        "wavelength") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(OpticsOper.OpticsPorts.OpticsPort.OpticsDwdmCarrrierChannelMap.DwdmCarrierMapInfo, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(OpticsOper.OpticsPorts.OpticsPort.OpticsDwdmCarrrierChannelMap.DwdmCarrierMapInfo, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.frequency.is_set or
                            self.g694_chan_num.is_set or
                            self.itu_chan_num.is_set or
                            self.wavelength.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.frequency.yfilter != YFilter.not_set or
                            self.g694_chan_num.yfilter != YFilter.not_set or
                            self.itu_chan_num.yfilter != YFilter.not_set or
                            self.wavelength.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "dwdm-carrier-map-info" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.frequency.is_set or self.frequency.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.frequency.get_name_leafdata())
                        if (self.g694_chan_num.is_set or self.g694_chan_num.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.g694_chan_num.get_name_leafdata())
                        if (self.itu_chan_num.is_set or self.itu_chan_num.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.itu_chan_num.get_name_leafdata())
                        if (self.wavelength.is_set or self.wavelength.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.wavelength.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "frequency" or name == "g694-chan-num" or name == "itu-chan-num" or name == "wavelength"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "frequency"):
                            self.frequency = value
                            self.frequency.value_namespace = name_space
                            self.frequency.value_namespace_prefix = name_space_prefix
                        if(value_path == "g694-chan-num"):
                            self.g694_chan_num = value
                            self.g694_chan_num.value_namespace = name_space
                            self.g694_chan_num.value_namespace_prefix = name_space_prefix
                        if(value_path == "itu-chan-num"):
                            self.itu_chan_num = value
                            self.itu_chan_num.value_namespace = name_space
                            self.itu_chan_num.value_namespace_prefix = name_space_prefix
                        if(value_path == "wavelength"):
                            self.wavelength = value
                            self.wavelength.value_namespace = name_space
                            self.wavelength.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.dwdm_carrier_map_info:
                        if (c.has_data()):
                            return True
                    return (
                        self.dwdm_carrier_band.is_set or
                        self.dwdm_carrier_max.is_set or
                        self.dwdm_carrier_min.is_set)

                def has_operation(self):
                    for c in self.dwdm_carrier_map_info:
                        if (c.has_operation()):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        self.dwdm_carrier_band.yfilter != YFilter.not_set or
                        self.dwdm_carrier_max.yfilter != YFilter.not_set or
                        self.dwdm_carrier_min.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "optics-dwdm-carrrier-channel-map" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.dwdm_carrier_band.is_set or self.dwdm_carrier_band.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.dwdm_carrier_band.get_name_leafdata())
                    if (self.dwdm_carrier_max.is_set or self.dwdm_carrier_max.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.dwdm_carrier_max.get_name_leafdata())
                    if (self.dwdm_carrier_min.is_set or self.dwdm_carrier_min.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.dwdm_carrier_min.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "dwdm-carrier-map-info"):
                        for c in self.dwdm_carrier_map_info:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = OpticsOper.OpticsPorts.OpticsPort.OpticsDwdmCarrrierChannelMap.DwdmCarrierMapInfo()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.dwdm_carrier_map_info.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "dwdm-carrier-map-info" or name == "dwdm-carrier-band" or name == "dwdm-carrier-max" or name == "dwdm-carrier-min"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "dwdm-carrier-band"):
                        self.dwdm_carrier_band = value
                        self.dwdm_carrier_band.value_namespace = name_space
                        self.dwdm_carrier_band.value_namespace_prefix = name_space_prefix
                    if(value_path == "dwdm-carrier-max"):
                        self.dwdm_carrier_max = value
                        self.dwdm_carrier_max.value_namespace = name_space
                        self.dwdm_carrier_max.value_namespace_prefix = name_space_prefix
                    if(value_path == "dwdm-carrier-min"):
                        self.dwdm_carrier_min = value
                        self.dwdm_carrier_min.value_namespace = name_space
                        self.dwdm_carrier_min.value_namespace_prefix = name_space_prefix


            class OpticsInfo(Entity):
                """
                Optics operational data
                
                .. attribute:: alarm_detected
                
                	Are there any alarms ?
                	**type**\:  bool
                
                .. attribute:: ampli_channel_power_config_val
                
                	ampli channel power config val
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: ampli_control_mode_config_val
                
                	ampli control mode config val
                	**type**\:   :py:class:`OpticsAmplifierControlMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsAmplifierControlMode>`
                
                .. attribute:: ampli_gain
                
                	Ampli Gain in the unit of 0.01dBm
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: ampli_gain_config_val
                
                	ampli gain config val
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: ampli_gain_range_config_val
                
                	ampli gain range config val
                	**type**\:   :py:class:`OpticsAmplifierGainRange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsAmplifierGainRange>`
                
                .. attribute:: ampli_gain_thr_deg_high_config_val
                
                	ampli gain thr deg high config val
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: ampli_gain_thr_deg_low_config_val
                
                	ampli gain thr deg low config val
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: ampli_tilt
                
                	Ampli Tilt in the unit of 0.01dBm
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: ampli_tilt_config_val
                
                	ampli tilt config val
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: cd
                
                	Chromatic Dispersion ps/nm
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: cd_configurable
                
                	CD Configurable is supported or not
                	**type**\:  bool
                
                .. attribute:: cd_high_threshold
                
                	Chromatic Dispersion high threshold ps/nm
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: cd_low_threshold
                
                	Chromatic Dispersion low threshold ps/nm
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: cd_max
                
                	Chromatic Dispersion Max ps/nm
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: cd_min
                
                	Chromatic Dispersion Min ps/nm
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: cfg_tx_power
                
                	Configured Tx power value in 0.1 dB
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: cfg_tx_power_configurable
                
                	TX Power Configuration is supported or not
                	**type**\:  bool
                
                .. attribute:: channel_power_max_delta_config_val
                
                	channel power max delta config val
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: controller_state
                
                	Optics controller state\: Up, Down or Administratively Down
                	**type**\:   :py:class:`OpticsControllerState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsControllerState>`
                
                .. attribute:: dgd_high_threshold
                
                	DGD high threshold in 0.1 ps
                	**type**\:  str
                
                .. attribute:: differential_group_delay
                
                	Differential Group Delay ps
                	**type**\:  str
                
                .. attribute:: display_volt_temp
                
                	Display Volt/Temp ?
                	**type**\:  bool
                
                .. attribute:: dwdm_carrier_band
                
                	DWDM Carrier Band information
                	**type**\:   :py:class:`OpticsWaveBand <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsWaveBand>`
                
                .. attribute:: dwdm_carrier_channel
                
                	Current ITU DWDM Carrier channel number
                	**type**\:  str
                
                .. attribute:: dwdm_carrier_frequency
                
                	DWDM Carrier frequency read from hw in the unit 0.01THz
                	**type**\:  str
                
                .. attribute:: dwdm_carrier_wavelength
                
                	Wavelength of color optics 0.001nm
                	**type**\:  str
                
                .. attribute:: ext_param_threshold_val
                
                	Extended optics parameters threshold values
                	**type**\:   :py:class:`ExtParamThresholdVal <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtParamThresholdVal>`
                
                .. attribute:: ext_param_val
                
                	Extended optics parameters
                	**type**\:   :py:class:`ExtParamVal <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtParamVal>`
                
                .. attribute:: form_factor
                
                	Optics form factor
                	**type**\:   :py:class:`OpticsFormFactor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsFormFactor>`
                
                .. attribute:: grey_wavelength
                
                	Wavelength of grey optics 0.01nm
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: is_bo_configured
                
                	Is BO configured ?
                	**type**\:  bool
                
                .. attribute:: is_ext_param_valid
                
                	Are the Extended Parameters Valid ?
                	**type**\:  bool
                
                .. attribute:: lane_data
                
                	Lane information
                	**type**\: list of    :py:class:`LaneData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData>`
                
                .. attribute:: laser_state
                
                	Showing laser state.Either ON or OFF or unknown
                	**type**\:   :py:class:`OpticsLaserState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsLaserState>`
                
                .. attribute:: lbc_high_threshold
                
                	LBC High threshold value in units of percentage
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                	**units**\: percentage
                
                .. attribute:: lbc_th_high_default
                
                	LBC high threshold default value in unit of 0 .001mA
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: lbc_th_high_warning_default
                
                	LBC high Warning threshold default value in unit of 0.001mA
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: lbc_th_low_default
                
                	LBC low threshold default value in units of 0 .001mA
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: lbc_th_low_warning_default
                
                	LBC low warning threshold default value in units of 0.001mA
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: led_state
                
                	Showing Current Colour of led state
                	**type**\:   :py:class:`OpticsLedState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsLedState>`
                
                .. attribute:: network_srlg_info
                
                	Network SRLG information
                	**type**\:   :py:class:`NetworkSrlgInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.NetworkSrlgInfo>`
                
                .. attribute:: optical_signal_to_noise_ratio
                
                	Optical Signal to Noise Ratio dB
                	**type**\:  str
                
                .. attribute:: optics_alarm_info
                
                	Optics Alarm Information
                	**type**\:   :py:class:`OpticsAlarmInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo>`
                
                .. attribute:: optics_fec
                
                	Optics FEC
                	**type**\:   :py:class:`OpticsFec <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsFec>`
                
                .. attribute:: optics_module
                
                	Optics module name
                	**type**\:  str
                
                .. attribute:: optics_present
                
                	Is Optics Present?
                	**type**\:  bool
                
                .. attribute:: optics_type
                
                	Optics type name
                	**type**\:   :py:class:`Optics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.Optics>`
                
                .. attribute:: osnr_low_threshold
                
                	OSNR low threshold in 0.01 dB
                	**type**\:  str
                
                .. attribute:: osri_config_val
                
                	osri config val
                	**type**\:  bool
                
                .. attribute:: ots_alarm_info
                
                	Ots Alarm Information
                	**type**\:   :py:class:`OtsAlarmInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo>`
                
                .. attribute:: phase_noise
                
                	Phase Noise dB
                	**type**\:  str
                
                .. attribute:: phy_type
                
                	Optics physical type
                	**type**\:   :py:class:`OpticsPhy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsPhy>`
                
                .. attribute:: pm_enable
                
                	PmEable or Disable
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: polarization_change_rate
                
                	Polarization Change Rate rad/s
                	**type**\:  str
                
                .. attribute:: polarization_dependent_loss
                
                	Polarization Dependent Loss dB
                	**type**\:  str
                
                .. attribute:: polarization_mode_dispersion
                
                	Polarization Mode Dispersion 0.1ps
                	**type**\:  str
                
                .. attribute:: port_status
                
                	Showing port status
                	**type**\:   :py:class:`OpticsPortStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsPortStatus>`
                
                .. attribute:: port_type
                
                	Showing port type
                	**type**\:   :py:class:`OpticsPort <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsPort>`
                
                .. attribute:: rx_high_threshold
                
                	Rx High threshold value in units of 0.1dBm
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: rx_high_warning_threshold
                
                	Rx High Warning threshold value in units of 0 .1dBm
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: rx_low_threshold
                
                	Rx Low threshold value in units of 0.1dBm
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: rx_low_warning_threshold
                
                	Rx Low Warning threshold value in units of 0 .1dBm
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: rx_power_th_configurable
                
                	rx power th configurable
                	**type**\:  bool
                
                .. attribute:: rx_voa_attenuation
                
                	Rx Voa Attenuation in the unit of 0.01dBm
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: rx_voa_attenuation_config_val
                
                	rx voa attenuation config val
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: safety_control_mode_config_val
                
                	safety control mode config val
                	**type**\:   :py:class:`OpticsAmplifierSafetyControlMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsAmplifierSafetyControlMode>`
                
                .. attribute:: second_order_polarization_mode_dispersion
                
                	Second Order Polarization Mode Dispersion 0 .1ps^2
                	**type**\:  str
                
                .. attribute:: temp_high_threshold
                
                	Temp High threshold value in the units of 0.01 C
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: temp_high_warning_threshold
                
                	Temp High warning threshold value in the units of 0.01 C
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: temp_low_threshold
                
                	Temp Low threshold value in the units 0.01 C
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: temp_low_warning_threshold
                
                	Temp Low warning threshold value in the units 0 .01 C
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: temperature
                
                	Temperature value
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: total_rx_power
                
                	Total Receive Power for Multi\-Lane Optics in dBm
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: total_tx_power
                
                	Total Transmit Power for Multi\-Lane Optics in dBm
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: transceiver_info
                
                	Transceiver Vendor Details
                	**type**\:   :py:class:`TransceiverInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.TransceiverInfo>`
                
                .. attribute:: transport_admin_state
                
                	Transport Admin State
                	**type**\:   :py:class:`OpticsTas <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsTas>`
                
                .. attribute:: tx_high_threshold
                
                	Tx High threshold value in units of 0.1dBm
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: tx_high_warning_threshold
                
                	Tx High Warning threshold value in units of 0 .1dBm
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: tx_low_threshold
                
                	Tx Low threshold value in units of 0.1dBm
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: tx_low_warning_threshold
                
                	Tx Low Warning threshold value in units of 0 .1dBm
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: tx_power_th_configurable
                
                	tx power th configurable
                	**type**\:  bool
                
                .. attribute:: tx_voa_attenuation
                
                	Tx Voa Attenuation in the unit of 0.01dBm
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: tx_voa_attenuation_config_val
                
                	tx voa attenuation config val
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: volt_high_threshold
                
                	Volt High threshold value
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: volt_high_warning_threshold
                
                	Volt High warning threshold value
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: volt_low_threshold
                
                	Volt Low threshold value
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: volt_low_warning_threshold
                
                	Volt Low warning threshold value
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: voltage
                
                	Voltage value
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                

                """

                _prefix = 'controller-optics-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo, self).__init__()

                    self.yang_name = "optics-info"
                    self.yang_parent_name = "optics-port"

                    self.alarm_detected = YLeaf(YType.boolean, "alarm-detected")

                    self.ampli_channel_power_config_val = YLeaf(YType.int32, "ampli-channel-power-config-val")

                    self.ampli_control_mode_config_val = YLeaf(YType.enumeration, "ampli-control-mode-config-val")

                    self.ampli_gain = YLeaf(YType.int32, "ampli-gain")

                    self.ampli_gain_config_val = YLeaf(YType.int32, "ampli-gain-config-val")

                    self.ampli_gain_range_config_val = YLeaf(YType.enumeration, "ampli-gain-range-config-val")

                    self.ampli_gain_thr_deg_high_config_val = YLeaf(YType.int32, "ampli-gain-thr-deg-high-config-val")

                    self.ampli_gain_thr_deg_low_config_val = YLeaf(YType.int32, "ampli-gain-thr-deg-low-config-val")

                    self.ampli_tilt = YLeaf(YType.int32, "ampli-tilt")

                    self.ampli_tilt_config_val = YLeaf(YType.int32, "ampli-tilt-config-val")

                    self.cd = YLeaf(YType.int32, "cd")

                    self.cd_configurable = YLeaf(YType.boolean, "cd-configurable")

                    self.cd_high_threshold = YLeaf(YType.int32, "cd-high-threshold")

                    self.cd_low_threshold = YLeaf(YType.int32, "cd-low-threshold")

                    self.cd_max = YLeaf(YType.int32, "cd-max")

                    self.cd_min = YLeaf(YType.int32, "cd-min")

                    self.cfg_tx_power = YLeaf(YType.int32, "cfg-tx-power")

                    self.cfg_tx_power_configurable = YLeaf(YType.boolean, "cfg-tx-power-configurable")

                    self.channel_power_max_delta_config_val = YLeaf(YType.int32, "channel-power-max-delta-config-val")

                    self.controller_state = YLeaf(YType.enumeration, "controller-state")

                    self.dgd_high_threshold = YLeaf(YType.str, "dgd-high-threshold")

                    self.differential_group_delay = YLeaf(YType.str, "differential-group-delay")

                    self.display_volt_temp = YLeaf(YType.boolean, "display-volt-temp")

                    self.dwdm_carrier_band = YLeaf(YType.enumeration, "dwdm-carrier-band")

                    self.dwdm_carrier_channel = YLeaf(YType.str, "dwdm-carrier-channel")

                    self.dwdm_carrier_frequency = YLeaf(YType.str, "dwdm-carrier-frequency")

                    self.dwdm_carrier_wavelength = YLeaf(YType.str, "dwdm-carrier-wavelength")

                    self.form_factor = YLeaf(YType.enumeration, "form-factor")

                    self.grey_wavelength = YLeaf(YType.uint32, "grey-wavelength")

                    self.is_bo_configured = YLeaf(YType.boolean, "is-bo-configured")

                    self.is_ext_param_valid = YLeaf(YType.boolean, "is-ext-param-valid")

                    self.laser_state = YLeaf(YType.enumeration, "laser-state")

                    self.lbc_high_threshold = YLeaf(YType.int32, "lbc-high-threshold")

                    self.lbc_th_high_default = YLeaf(YType.int32, "lbc-th-high-default")

                    self.lbc_th_high_warning_default = YLeaf(YType.int32, "lbc-th-high-warning-default")

                    self.lbc_th_low_default = YLeaf(YType.int32, "lbc-th-low-default")

                    self.lbc_th_low_warning_default = YLeaf(YType.int32, "lbc-th-low-warning-default")

                    self.led_state = YLeaf(YType.enumeration, "led-state")

                    self.optical_signal_to_noise_ratio = YLeaf(YType.str, "optical-signal-to-noise-ratio")

                    self.optics_fec = YLeaf(YType.enumeration, "optics-fec")

                    self.optics_module = YLeaf(YType.str, "optics-module")

                    self.optics_present = YLeaf(YType.boolean, "optics-present")

                    self.optics_type = YLeaf(YType.enumeration, "optics-type")

                    self.osnr_low_threshold = YLeaf(YType.str, "osnr-low-threshold")

                    self.osri_config_val = YLeaf(YType.boolean, "osri-config-val")

                    self.phase_noise = YLeaf(YType.str, "phase-noise")

                    self.phy_type = YLeaf(YType.enumeration, "phy-type")

                    self.pm_enable = YLeaf(YType.uint32, "pm-enable")

                    self.polarization_change_rate = YLeaf(YType.str, "polarization-change-rate")

                    self.polarization_dependent_loss = YLeaf(YType.str, "polarization-dependent-loss")

                    self.polarization_mode_dispersion = YLeaf(YType.str, "polarization-mode-dispersion")

                    self.port_status = YLeaf(YType.enumeration, "port-status")

                    self.port_type = YLeaf(YType.enumeration, "port-type")

                    self.rx_high_threshold = YLeaf(YType.int32, "rx-high-threshold")

                    self.rx_high_warning_threshold = YLeaf(YType.int32, "rx-high-warning-threshold")

                    self.rx_low_threshold = YLeaf(YType.int32, "rx-low-threshold")

                    self.rx_low_warning_threshold = YLeaf(YType.int32, "rx-low-warning-threshold")

                    self.rx_power_th_configurable = YLeaf(YType.boolean, "rx-power-th-configurable")

                    self.rx_voa_attenuation = YLeaf(YType.int32, "rx-voa-attenuation")

                    self.rx_voa_attenuation_config_val = YLeaf(YType.int32, "rx-voa-attenuation-config-val")

                    self.safety_control_mode_config_val = YLeaf(YType.enumeration, "safety-control-mode-config-val")

                    self.second_order_polarization_mode_dispersion = YLeaf(YType.str, "second-order-polarization-mode-dispersion")

                    self.temp_high_threshold = YLeaf(YType.int32, "temp-high-threshold")

                    self.temp_high_warning_threshold = YLeaf(YType.int32, "temp-high-warning-threshold")

                    self.temp_low_threshold = YLeaf(YType.int32, "temp-low-threshold")

                    self.temp_low_warning_threshold = YLeaf(YType.int32, "temp-low-warning-threshold")

                    self.temperature = YLeaf(YType.int32, "temperature")

                    self.total_rx_power = YLeaf(YType.int32, "total-rx-power")

                    self.total_tx_power = YLeaf(YType.int32, "total-tx-power")

                    self.transport_admin_state = YLeaf(YType.enumeration, "transport-admin-state")

                    self.tx_high_threshold = YLeaf(YType.int32, "tx-high-threshold")

                    self.tx_high_warning_threshold = YLeaf(YType.int32, "tx-high-warning-threshold")

                    self.tx_low_threshold = YLeaf(YType.int32, "tx-low-threshold")

                    self.tx_low_warning_threshold = YLeaf(YType.int32, "tx-low-warning-threshold")

                    self.tx_power_th_configurable = YLeaf(YType.boolean, "tx-power-th-configurable")

                    self.tx_voa_attenuation = YLeaf(YType.int32, "tx-voa-attenuation")

                    self.tx_voa_attenuation_config_val = YLeaf(YType.int32, "tx-voa-attenuation-config-val")

                    self.volt_high_threshold = YLeaf(YType.int32, "volt-high-threshold")

                    self.volt_high_warning_threshold = YLeaf(YType.int32, "volt-high-warning-threshold")

                    self.volt_low_threshold = YLeaf(YType.int32, "volt-low-threshold")

                    self.volt_low_warning_threshold = YLeaf(YType.int32, "volt-low-warning-threshold")

                    self.voltage = YLeaf(YType.int32, "voltage")

                    self.ext_param_threshold_val = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtParamThresholdVal()
                    self.ext_param_threshold_val.parent = self
                    self._children_name_map["ext_param_threshold_val"] = "ext-param-threshold-val"
                    self._children_yang_names.add("ext-param-threshold-val")

                    self.ext_param_val = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtParamVal()
                    self.ext_param_val.parent = self
                    self._children_name_map["ext_param_val"] = "ext-param-val"
                    self._children_yang_names.add("ext-param-val")

                    self.network_srlg_info = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.NetworkSrlgInfo()
                    self.network_srlg_info.parent = self
                    self._children_name_map["network_srlg_info"] = "network-srlg-info"
                    self._children_yang_names.add("network-srlg-info")

                    self.optics_alarm_info = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo()
                    self.optics_alarm_info.parent = self
                    self._children_name_map["optics_alarm_info"] = "optics-alarm-info"
                    self._children_yang_names.add("optics-alarm-info")

                    self.ots_alarm_info = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo()
                    self.ots_alarm_info.parent = self
                    self._children_name_map["ots_alarm_info"] = "ots-alarm-info"
                    self._children_yang_names.add("ots-alarm-info")

                    self.transceiver_info = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.TransceiverInfo()
                    self.transceiver_info.parent = self
                    self._children_name_map["transceiver_info"] = "transceiver-info"
                    self._children_yang_names.add("transceiver-info")

                    self.lane_data = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("alarm_detected",
                                    "ampli_channel_power_config_val",
                                    "ampli_control_mode_config_val",
                                    "ampli_gain",
                                    "ampli_gain_config_val",
                                    "ampli_gain_range_config_val",
                                    "ampli_gain_thr_deg_high_config_val",
                                    "ampli_gain_thr_deg_low_config_val",
                                    "ampli_tilt",
                                    "ampli_tilt_config_val",
                                    "cd",
                                    "cd_configurable",
                                    "cd_high_threshold",
                                    "cd_low_threshold",
                                    "cd_max",
                                    "cd_min",
                                    "cfg_tx_power",
                                    "cfg_tx_power_configurable",
                                    "channel_power_max_delta_config_val",
                                    "controller_state",
                                    "dgd_high_threshold",
                                    "differential_group_delay",
                                    "display_volt_temp",
                                    "dwdm_carrier_band",
                                    "dwdm_carrier_channel",
                                    "dwdm_carrier_frequency",
                                    "dwdm_carrier_wavelength",
                                    "form_factor",
                                    "grey_wavelength",
                                    "is_bo_configured",
                                    "is_ext_param_valid",
                                    "laser_state",
                                    "lbc_high_threshold",
                                    "lbc_th_high_default",
                                    "lbc_th_high_warning_default",
                                    "lbc_th_low_default",
                                    "lbc_th_low_warning_default",
                                    "led_state",
                                    "optical_signal_to_noise_ratio",
                                    "optics_fec",
                                    "optics_module",
                                    "optics_present",
                                    "optics_type",
                                    "osnr_low_threshold",
                                    "osri_config_val",
                                    "phase_noise",
                                    "phy_type",
                                    "pm_enable",
                                    "polarization_change_rate",
                                    "polarization_dependent_loss",
                                    "polarization_mode_dispersion",
                                    "port_status",
                                    "port_type",
                                    "rx_high_threshold",
                                    "rx_high_warning_threshold",
                                    "rx_low_threshold",
                                    "rx_low_warning_threshold",
                                    "rx_power_th_configurable",
                                    "rx_voa_attenuation",
                                    "rx_voa_attenuation_config_val",
                                    "safety_control_mode_config_val",
                                    "second_order_polarization_mode_dispersion",
                                    "temp_high_threshold",
                                    "temp_high_warning_threshold",
                                    "temp_low_threshold",
                                    "temp_low_warning_threshold",
                                    "temperature",
                                    "total_rx_power",
                                    "total_tx_power",
                                    "transport_admin_state",
                                    "tx_high_threshold",
                                    "tx_high_warning_threshold",
                                    "tx_low_threshold",
                                    "tx_low_warning_threshold",
                                    "tx_power_th_configurable",
                                    "tx_voa_attenuation",
                                    "tx_voa_attenuation_config_val",
                                    "volt_high_threshold",
                                    "volt_high_warning_threshold",
                                    "volt_low_threshold",
                                    "volt_low_warning_threshold",
                                    "voltage") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo, self).__setattr__(name, value)


                class NetworkSrlgInfo(Entity):
                    """
                    Network SRLG information
                    
                    .. attribute:: network_srlg_array
                    
                    	Network Srlg Array
                    	**type**\: list of    :py:class:`NetworkSrlgArray <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.NetworkSrlgInfo.NetworkSrlgArray>`
                    
                    

                    """

                    _prefix = 'controller-optics-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.NetworkSrlgInfo, self).__init__()

                        self.yang_name = "network-srlg-info"
                        self.yang_parent_name = "optics-info"

                        self.network_srlg_array = YList(self)

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
                                    super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.NetworkSrlgInfo, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.NetworkSrlgInfo, self).__setattr__(name, value)


                    class NetworkSrlgArray(Entity):
                        """
                        Network Srlg Array
                        
                        .. attribute:: network_srlg
                        
                        	Network Srlg
                        	**type**\:  list of int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: set_number
                        
                        	Array to maintain set number
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.NetworkSrlgInfo.NetworkSrlgArray, self).__init__()

                            self.yang_name = "network-srlg-array"
                            self.yang_parent_name = "network-srlg-info"

                            self.network_srlg = YLeafList(YType.uint32, "network-srlg")

                            self.set_number = YLeaf(YType.uint32, "set-number")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("network_srlg",
                                            "set_number") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.NetworkSrlgInfo.NetworkSrlgArray, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.NetworkSrlgInfo.NetworkSrlgArray, self).__setattr__(name, value)

                        def has_data(self):
                            for leaf in self.network_srlg.getYLeafs():
                                if (leaf.yfilter != YFilter.not_set):
                                    return True
                            return self.set_number.is_set

                        def has_operation(self):
                            for leaf in self.network_srlg.getYLeafs():
                                if (leaf.is_set):
                                    return True
                            return (
                                self.yfilter != YFilter.not_set or
                                self.network_srlg.yfilter != YFilter.not_set or
                                self.set_number.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "network-srlg-array" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.set_number.is_set or self.set_number.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.set_number.get_name_leafdata())

                            leaf_name_data.extend(self.network_srlg.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "network-srlg" or name == "set-number"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "network-srlg"):
                                self.network_srlg.append(value)
                            if(value_path == "set-number"):
                                self.set_number = value
                                self.set_number.value_namespace = name_space
                                self.set_number.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.network_srlg_array:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.network_srlg_array:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "network-srlg-info" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "network-srlg-array"):
                            for c in self.network_srlg_array:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.NetworkSrlgInfo.NetworkSrlgArray()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.network_srlg_array.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "network-srlg-array"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class OpticsAlarmInfo(Entity):
                    """
                    Optics Alarm Information
                    
                    .. attribute:: amp_gain_deg_high
                    
                    	Ampli Gain Deg High
                    	**type**\:   :py:class:`AmpGainDegHigh <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.AmpGainDegHigh>`
                    
                    .. attribute:: amp_gain_deg_low
                    
                    	Ampli Gain Deg Low
                    	**type**\:   :py:class:`AmpGainDegLow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.AmpGainDegLow>`
                    
                    .. attribute:: hidgd
                    
                    	HI DGD
                    	**type**\:   :py:class:`Hidgd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Hidgd>`
                    
                    .. attribute:: high_lbc
                    
                    	High laser bias current in units of percentage
                    	**type**\:   :py:class:`HighLbc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighLbc>`
                    
                    .. attribute:: high_rx1_power
                    
                    	High Rx1 Power in uints of 0.1 dBm
                    	**type**\:   :py:class:`HighRx1Power <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx1Power>`
                    
                    .. attribute:: high_rx2_power
                    
                    	High Rx2 Power in uints of 0.1 dBm
                    	**type**\:   :py:class:`HighRx2Power <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx2Power>`
                    
                    .. attribute:: high_rx3_power
                    
                    	High Rx3 Power in uints of 0.1 dBm
                    	**type**\:   :py:class:`HighRx3Power <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx3Power>`
                    
                    .. attribute:: high_rx4_power
                    
                    	High Rx4 Power in uints of 0.1 dBm
                    	**type**\:   :py:class:`HighRx4Power <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx4Power>`
                    
                    .. attribute:: high_rx_power
                    
                    	High Rx Power in uints of 0.1 dBm
                    	**type**\:   :py:class:`HighRxPower <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRxPower>`
                    
                    .. attribute:: high_tx1_power
                    
                    	High Tx1 Power in uints of 0.1 dBm
                    	**type**\:   :py:class:`HighTx1Power <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx1Power>`
                    
                    .. attribute:: high_tx1lbc
                    
                    	High Tx1 laser bias current in units of percentage
                    	**type**\:   :py:class:`HighTx1Lbc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx1Lbc>`
                    
                    .. attribute:: high_tx2_power
                    
                    	High Tx2 Power in uints of 0.1 dBm
                    	**type**\:   :py:class:`HighTx2Power <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx2Power>`
                    
                    .. attribute:: high_tx2lbc
                    
                    	High Tx2 laser bias current in units of percentage
                    	**type**\:   :py:class:`HighTx2Lbc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx2Lbc>`
                    
                    .. attribute:: high_tx3_power
                    
                    	High Tx3 Power in uints of 0.1 dBm
                    	**type**\:   :py:class:`HighTx3Power <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx3Power>`
                    
                    .. attribute:: high_tx3lbc
                    
                    	High Tx3 laser bias current in units of percentage
                    	**type**\:   :py:class:`HighTx3Lbc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx3Lbc>`
                    
                    .. attribute:: high_tx4_power
                    
                    	High Tx4 Power in uints of 0.1 dBm
                    	**type**\:   :py:class:`HighTx4Power <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx4Power>`
                    
                    .. attribute:: high_tx4lbc
                    
                    	High Tx4 laser bias current in units of percentage
                    	**type**\:   :py:class:`HighTx4Lbc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx4Lbc>`
                    
                    .. attribute:: high_tx_power
                    
                    	High Tx Power in uints of 0.1 dBm
                    	**type**\:   :py:class:`HighTxPower <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTxPower>`
                    
                    .. attribute:: imp_removal
                    
                    	IMPROPER REM
                    	**type**\:   :py:class:`ImpRemoval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.ImpRemoval>`
                    
                    .. attribute:: low_rx1_power
                    
                    	Low Rx1 Power in uints of 0.1 dBm
                    	**type**\:   :py:class:`LowRx1Power <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx1Power>`
                    
                    .. attribute:: low_rx2_power
                    
                    	Low Rx2 Power in uints of 0.1 dBm
                    	**type**\:   :py:class:`LowRx2Power <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx2Power>`
                    
                    .. attribute:: low_rx3_power
                    
                    	Low Rx3 Power in uints of 0.1 dBm
                    	**type**\:   :py:class:`LowRx3Power <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx3Power>`
                    
                    .. attribute:: low_rx4_power
                    
                    	Low Rx4 Power in uints of 0.1 dBm
                    	**type**\:   :py:class:`LowRx4Power <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx4Power>`
                    
                    .. attribute:: low_rx_power
                    
                    	Low Rx Power in uints of 0.1 dBm
                    	**type**\:   :py:class:`LowRxPower <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRxPower>`
                    
                    .. attribute:: low_tx1_power
                    
                    	Low Tx1 Power in uints of 0.1 dBm
                    	**type**\:   :py:class:`LowTx1Power <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx1Power>`
                    
                    .. attribute:: low_tx1lbc
                    
                    	Low Tx1 laser bias current in units of percentage
                    	**type**\:   :py:class:`LowTx1Lbc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx1Lbc>`
                    
                    .. attribute:: low_tx2_power
                    
                    	Low Tx2 Power in uints of 0.1 dBm
                    	**type**\:   :py:class:`LowTx2Power <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx2Power>`
                    
                    .. attribute:: low_tx2lbc
                    
                    	Low Tx2 laser bias current in units of percentage
                    	**type**\:   :py:class:`LowTx2Lbc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx2Lbc>`
                    
                    .. attribute:: low_tx3_power
                    
                    	Low Tx3 Power in uints of 0.1 dBm
                    	**type**\:   :py:class:`LowTx3Power <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx3Power>`
                    
                    .. attribute:: low_tx3lbc
                    
                    	Low Tx3 laser bias current in units of percentage
                    	**type**\:   :py:class:`LowTx3Lbc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx3Lbc>`
                    
                    .. attribute:: low_tx4_power
                    
                    	Low Tx4 Power in uints of 0.1 dBm
                    	**type**\:   :py:class:`LowTx4Power <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx4Power>`
                    
                    .. attribute:: low_tx4lbc
                    
                    	Low Tx4 laser bias current in units of percentage
                    	**type**\:   :py:class:`LowTx4Lbc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx4Lbc>`
                    
                    .. attribute:: low_tx_power
                    
                    	Low Tx Power in uints of 0.1 dBm
                    	**type**\:   :py:class:`LowTxPower <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTxPower>`
                    
                    .. attribute:: mea
                    
                    	MEA
                    	**type**\:   :py:class:`Mea <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Mea>`
                    
                    .. attribute:: oorcd
                    
                    	OOR CD
                    	**type**\:   :py:class:`Oorcd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Oorcd>`
                    
                    .. attribute:: osnr
                    
                    	OSNR
                    	**type**\:   :py:class:`Osnr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Osnr>`
                    
                    .. attribute:: rx_loc
                    
                    	Rx LOC
                    	**type**\:   :py:class:`RxLoc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.RxLoc>`
                    
                    .. attribute:: rx_lol
                    
                    	RX LOL
                    	**type**\:   :py:class:`RxLol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.RxLol>`
                    
                    .. attribute:: rx_los
                    
                    	RX LOS
                    	**type**\:   :py:class:`RxLos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.RxLos>`
                    
                    .. attribute:: tx_fault
                    
                    	TX Fault
                    	**type**\:   :py:class:`TxFault <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxFault>`
                    
                    .. attribute:: tx_lol
                    
                    	TX LOL
                    	**type**\:   :py:class:`TxLol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxLol>`
                    
                    .. attribute:: tx_los
                    
                    	TX LOS
                    	**type**\:   :py:class:`TxLos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxLos>`
                    
                    .. attribute:: txpwr_mismatch
                    
                    	TX POWER PROV MISMATCH
                    	**type**\:   :py:class:`TxpwrMismatch <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxpwrMismatch>`
                    
                    .. attribute:: wvlool
                    
                    	WVL OOL
                    	**type**\:   :py:class:`Wvlool <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Wvlool>`
                    
                    

                    """

                    _prefix = 'controller-optics-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo, self).__init__()

                        self.yang_name = "optics-alarm-info"
                        self.yang_parent_name = "optics-info"

                        self.amp_gain_deg_high = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.AmpGainDegHigh()
                        self.amp_gain_deg_high.parent = self
                        self._children_name_map["amp_gain_deg_high"] = "amp-gain-deg-high"
                        self._children_yang_names.add("amp-gain-deg-high")

                        self.amp_gain_deg_low = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.AmpGainDegLow()
                        self.amp_gain_deg_low.parent = self
                        self._children_name_map["amp_gain_deg_low"] = "amp-gain-deg-low"
                        self._children_yang_names.add("amp-gain-deg-low")

                        self.hidgd = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Hidgd()
                        self.hidgd.parent = self
                        self._children_name_map["hidgd"] = "hidgd"
                        self._children_yang_names.add("hidgd")

                        self.high_lbc = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighLbc()
                        self.high_lbc.parent = self
                        self._children_name_map["high_lbc"] = "high-lbc"
                        self._children_yang_names.add("high-lbc")

                        self.high_rx1_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx1Power()
                        self.high_rx1_power.parent = self
                        self._children_name_map["high_rx1_power"] = "high-rx1-power"
                        self._children_yang_names.add("high-rx1-power")

                        self.high_rx2_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx2Power()
                        self.high_rx2_power.parent = self
                        self._children_name_map["high_rx2_power"] = "high-rx2-power"
                        self._children_yang_names.add("high-rx2-power")

                        self.high_rx3_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx3Power()
                        self.high_rx3_power.parent = self
                        self._children_name_map["high_rx3_power"] = "high-rx3-power"
                        self._children_yang_names.add("high-rx3-power")

                        self.high_rx4_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx4Power()
                        self.high_rx4_power.parent = self
                        self._children_name_map["high_rx4_power"] = "high-rx4-power"
                        self._children_yang_names.add("high-rx4-power")

                        self.high_rx_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRxPower()
                        self.high_rx_power.parent = self
                        self._children_name_map["high_rx_power"] = "high-rx-power"
                        self._children_yang_names.add("high-rx-power")

                        self.high_tx1_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx1Power()
                        self.high_tx1_power.parent = self
                        self._children_name_map["high_tx1_power"] = "high-tx1-power"
                        self._children_yang_names.add("high-tx1-power")

                        self.high_tx1lbc = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx1Lbc()
                        self.high_tx1lbc.parent = self
                        self._children_name_map["high_tx1lbc"] = "high-tx1lbc"
                        self._children_yang_names.add("high-tx1lbc")

                        self.high_tx2_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx2Power()
                        self.high_tx2_power.parent = self
                        self._children_name_map["high_tx2_power"] = "high-tx2-power"
                        self._children_yang_names.add("high-tx2-power")

                        self.high_tx2lbc = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx2Lbc()
                        self.high_tx2lbc.parent = self
                        self._children_name_map["high_tx2lbc"] = "high-tx2lbc"
                        self._children_yang_names.add("high-tx2lbc")

                        self.high_tx3_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx3Power()
                        self.high_tx3_power.parent = self
                        self._children_name_map["high_tx3_power"] = "high-tx3-power"
                        self._children_yang_names.add("high-tx3-power")

                        self.high_tx3lbc = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx3Lbc()
                        self.high_tx3lbc.parent = self
                        self._children_name_map["high_tx3lbc"] = "high-tx3lbc"
                        self._children_yang_names.add("high-tx3lbc")

                        self.high_tx4_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx4Power()
                        self.high_tx4_power.parent = self
                        self._children_name_map["high_tx4_power"] = "high-tx4-power"
                        self._children_yang_names.add("high-tx4-power")

                        self.high_tx4lbc = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx4Lbc()
                        self.high_tx4lbc.parent = self
                        self._children_name_map["high_tx4lbc"] = "high-tx4lbc"
                        self._children_yang_names.add("high-tx4lbc")

                        self.high_tx_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTxPower()
                        self.high_tx_power.parent = self
                        self._children_name_map["high_tx_power"] = "high-tx-power"
                        self._children_yang_names.add("high-tx-power")

                        self.imp_removal = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.ImpRemoval()
                        self.imp_removal.parent = self
                        self._children_name_map["imp_removal"] = "imp-removal"
                        self._children_yang_names.add("imp-removal")

                        self.low_rx1_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx1Power()
                        self.low_rx1_power.parent = self
                        self._children_name_map["low_rx1_power"] = "low-rx1-power"
                        self._children_yang_names.add("low-rx1-power")

                        self.low_rx2_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx2Power()
                        self.low_rx2_power.parent = self
                        self._children_name_map["low_rx2_power"] = "low-rx2-power"
                        self._children_yang_names.add("low-rx2-power")

                        self.low_rx3_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx3Power()
                        self.low_rx3_power.parent = self
                        self._children_name_map["low_rx3_power"] = "low-rx3-power"
                        self._children_yang_names.add("low-rx3-power")

                        self.low_rx4_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx4Power()
                        self.low_rx4_power.parent = self
                        self._children_name_map["low_rx4_power"] = "low-rx4-power"
                        self._children_yang_names.add("low-rx4-power")

                        self.low_rx_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRxPower()
                        self.low_rx_power.parent = self
                        self._children_name_map["low_rx_power"] = "low-rx-power"
                        self._children_yang_names.add("low-rx-power")

                        self.low_tx1_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx1Power()
                        self.low_tx1_power.parent = self
                        self._children_name_map["low_tx1_power"] = "low-tx1-power"
                        self._children_yang_names.add("low-tx1-power")

                        self.low_tx1lbc = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx1Lbc()
                        self.low_tx1lbc.parent = self
                        self._children_name_map["low_tx1lbc"] = "low-tx1lbc"
                        self._children_yang_names.add("low-tx1lbc")

                        self.low_tx2_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx2Power()
                        self.low_tx2_power.parent = self
                        self._children_name_map["low_tx2_power"] = "low-tx2-power"
                        self._children_yang_names.add("low-tx2-power")

                        self.low_tx2lbc = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx2Lbc()
                        self.low_tx2lbc.parent = self
                        self._children_name_map["low_tx2lbc"] = "low-tx2lbc"
                        self._children_yang_names.add("low-tx2lbc")

                        self.low_tx3_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx3Power()
                        self.low_tx3_power.parent = self
                        self._children_name_map["low_tx3_power"] = "low-tx3-power"
                        self._children_yang_names.add("low-tx3-power")

                        self.low_tx3lbc = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx3Lbc()
                        self.low_tx3lbc.parent = self
                        self._children_name_map["low_tx3lbc"] = "low-tx3lbc"
                        self._children_yang_names.add("low-tx3lbc")

                        self.low_tx4_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx4Power()
                        self.low_tx4_power.parent = self
                        self._children_name_map["low_tx4_power"] = "low-tx4-power"
                        self._children_yang_names.add("low-tx4-power")

                        self.low_tx4lbc = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx4Lbc()
                        self.low_tx4lbc.parent = self
                        self._children_name_map["low_tx4lbc"] = "low-tx4lbc"
                        self._children_yang_names.add("low-tx4lbc")

                        self.low_tx_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTxPower()
                        self.low_tx_power.parent = self
                        self._children_name_map["low_tx_power"] = "low-tx-power"
                        self._children_yang_names.add("low-tx-power")

                        self.mea = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Mea()
                        self.mea.parent = self
                        self._children_name_map["mea"] = "mea"
                        self._children_yang_names.add("mea")

                        self.oorcd = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Oorcd()
                        self.oorcd.parent = self
                        self._children_name_map["oorcd"] = "oorcd"
                        self._children_yang_names.add("oorcd")

                        self.osnr = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Osnr()
                        self.osnr.parent = self
                        self._children_name_map["osnr"] = "osnr"
                        self._children_yang_names.add("osnr")

                        self.rx_loc = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.RxLoc()
                        self.rx_loc.parent = self
                        self._children_name_map["rx_loc"] = "rx-loc"
                        self._children_yang_names.add("rx-loc")

                        self.rx_lol = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.RxLol()
                        self.rx_lol.parent = self
                        self._children_name_map["rx_lol"] = "rx-lol"
                        self._children_yang_names.add("rx-lol")

                        self.rx_los = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.RxLos()
                        self.rx_los.parent = self
                        self._children_name_map["rx_los"] = "rx-los"
                        self._children_yang_names.add("rx-los")

                        self.tx_fault = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxFault()
                        self.tx_fault.parent = self
                        self._children_name_map["tx_fault"] = "tx-fault"
                        self._children_yang_names.add("tx-fault")

                        self.tx_lol = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxLol()
                        self.tx_lol.parent = self
                        self._children_name_map["tx_lol"] = "tx-lol"
                        self._children_yang_names.add("tx-lol")

                        self.tx_los = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxLos()
                        self.tx_los.parent = self
                        self._children_name_map["tx_los"] = "tx-los"
                        self._children_yang_names.add("tx-los")

                        self.txpwr_mismatch = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxpwrMismatch()
                        self.txpwr_mismatch.parent = self
                        self._children_name_map["txpwr_mismatch"] = "txpwr-mismatch"
                        self._children_yang_names.add("txpwr-mismatch")

                        self.wvlool = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Wvlool()
                        self.wvlool.parent = self
                        self._children_name_map["wvlool"] = "wvlool"
                        self._children_yang_names.add("wvlool")


                    class HighRxPower(Entity):
                        """
                        High Rx Power in uints of 0.1 dBm
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRxPower, self).__init__()

                            self.yang_name = "high-rx-power"
                            self.yang_parent_name = "optics-alarm-info"

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("counter",
                                            "is_detected") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRxPower, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRxPower, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.counter.is_set or
                                self.is_detected.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.counter.yfilter != YFilter.not_set or
                                self.is_detected.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "high-rx-power" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.counter.is_set or self.counter.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.counter.get_name_leafdata())
                            if (self.is_detected.is_set or self.is_detected.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_detected.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "counter" or name == "is-detected"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "counter"):
                                self.counter = value
                                self.counter.value_namespace = name_space
                                self.counter.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-detected"):
                                self.is_detected = value
                                self.is_detected.value_namespace = name_space
                                self.is_detected.value_namespace_prefix = name_space_prefix


                    class LowRxPower(Entity):
                        """
                        Low Rx Power in uints of 0.1 dBm
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRxPower, self).__init__()

                            self.yang_name = "low-rx-power"
                            self.yang_parent_name = "optics-alarm-info"

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("counter",
                                            "is_detected") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRxPower, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRxPower, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.counter.is_set or
                                self.is_detected.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.counter.yfilter != YFilter.not_set or
                                self.is_detected.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "low-rx-power" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.counter.is_set or self.counter.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.counter.get_name_leafdata())
                            if (self.is_detected.is_set or self.is_detected.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_detected.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "counter" or name == "is-detected"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "counter"):
                                self.counter = value
                                self.counter.value_namespace = name_space
                                self.counter.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-detected"):
                                self.is_detected = value
                                self.is_detected.value_namespace = name_space
                                self.is_detected.value_namespace_prefix = name_space_prefix


                    class HighTxPower(Entity):
                        """
                        High Tx Power in uints of 0.1 dBm
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTxPower, self).__init__()

                            self.yang_name = "high-tx-power"
                            self.yang_parent_name = "optics-alarm-info"

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("counter",
                                            "is_detected") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTxPower, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTxPower, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.counter.is_set or
                                self.is_detected.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.counter.yfilter != YFilter.not_set or
                                self.is_detected.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "high-tx-power" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.counter.is_set or self.counter.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.counter.get_name_leafdata())
                            if (self.is_detected.is_set or self.is_detected.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_detected.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "counter" or name == "is-detected"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "counter"):
                                self.counter = value
                                self.counter.value_namespace = name_space
                                self.counter.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-detected"):
                                self.is_detected = value
                                self.is_detected.value_namespace = name_space
                                self.is_detected.value_namespace_prefix = name_space_prefix


                    class LowTxPower(Entity):
                        """
                        Low Tx Power in uints of 0.1 dBm
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTxPower, self).__init__()

                            self.yang_name = "low-tx-power"
                            self.yang_parent_name = "optics-alarm-info"

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("counter",
                                            "is_detected") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTxPower, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTxPower, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.counter.is_set or
                                self.is_detected.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.counter.yfilter != YFilter.not_set or
                                self.is_detected.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "low-tx-power" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.counter.is_set or self.counter.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.counter.get_name_leafdata())
                            if (self.is_detected.is_set or self.is_detected.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_detected.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "counter" or name == "is-detected"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "counter"):
                                self.counter = value
                                self.counter.value_namespace = name_space
                                self.counter.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-detected"):
                                self.is_detected = value
                                self.is_detected.value_namespace = name_space
                                self.is_detected.value_namespace_prefix = name_space_prefix


                    class HighLbc(Entity):
                        """
                        High laser bias current in units of percentage
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighLbc, self).__init__()

                            self.yang_name = "high-lbc"
                            self.yang_parent_name = "optics-alarm-info"

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("counter",
                                            "is_detected") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighLbc, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighLbc, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.counter.is_set or
                                self.is_detected.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.counter.yfilter != YFilter.not_set or
                                self.is_detected.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "high-lbc" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.counter.is_set or self.counter.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.counter.get_name_leafdata())
                            if (self.is_detected.is_set or self.is_detected.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_detected.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "counter" or name == "is-detected"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "counter"):
                                self.counter = value
                                self.counter.value_namespace = name_space
                                self.counter.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-detected"):
                                self.is_detected = value
                                self.is_detected.value_namespace = name_space
                                self.is_detected.value_namespace_prefix = name_space_prefix


                    class HighRx1Power(Entity):
                        """
                        High Rx1 Power in uints of 0.1 dBm
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx1Power, self).__init__()

                            self.yang_name = "high-rx1-power"
                            self.yang_parent_name = "optics-alarm-info"

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("counter",
                                            "is_detected") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx1Power, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx1Power, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.counter.is_set or
                                self.is_detected.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.counter.yfilter != YFilter.not_set or
                                self.is_detected.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "high-rx1-power" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.counter.is_set or self.counter.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.counter.get_name_leafdata())
                            if (self.is_detected.is_set or self.is_detected.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_detected.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "counter" or name == "is-detected"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "counter"):
                                self.counter = value
                                self.counter.value_namespace = name_space
                                self.counter.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-detected"):
                                self.is_detected = value
                                self.is_detected.value_namespace = name_space
                                self.is_detected.value_namespace_prefix = name_space_prefix


                    class HighRx2Power(Entity):
                        """
                        High Rx2 Power in uints of 0.1 dBm
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx2Power, self).__init__()

                            self.yang_name = "high-rx2-power"
                            self.yang_parent_name = "optics-alarm-info"

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("counter",
                                            "is_detected") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx2Power, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx2Power, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.counter.is_set or
                                self.is_detected.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.counter.yfilter != YFilter.not_set or
                                self.is_detected.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "high-rx2-power" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.counter.is_set or self.counter.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.counter.get_name_leafdata())
                            if (self.is_detected.is_set or self.is_detected.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_detected.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "counter" or name == "is-detected"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "counter"):
                                self.counter = value
                                self.counter.value_namespace = name_space
                                self.counter.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-detected"):
                                self.is_detected = value
                                self.is_detected.value_namespace = name_space
                                self.is_detected.value_namespace_prefix = name_space_prefix


                    class HighRx3Power(Entity):
                        """
                        High Rx3 Power in uints of 0.1 dBm
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx3Power, self).__init__()

                            self.yang_name = "high-rx3-power"
                            self.yang_parent_name = "optics-alarm-info"

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("counter",
                                            "is_detected") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx3Power, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx3Power, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.counter.is_set or
                                self.is_detected.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.counter.yfilter != YFilter.not_set or
                                self.is_detected.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "high-rx3-power" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.counter.is_set or self.counter.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.counter.get_name_leafdata())
                            if (self.is_detected.is_set or self.is_detected.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_detected.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "counter" or name == "is-detected"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "counter"):
                                self.counter = value
                                self.counter.value_namespace = name_space
                                self.counter.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-detected"):
                                self.is_detected = value
                                self.is_detected.value_namespace = name_space
                                self.is_detected.value_namespace_prefix = name_space_prefix


                    class HighRx4Power(Entity):
                        """
                        High Rx4 Power in uints of 0.1 dBm
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx4Power, self).__init__()

                            self.yang_name = "high-rx4-power"
                            self.yang_parent_name = "optics-alarm-info"

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("counter",
                                            "is_detected") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx4Power, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx4Power, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.counter.is_set or
                                self.is_detected.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.counter.yfilter != YFilter.not_set or
                                self.is_detected.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "high-rx4-power" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.counter.is_set or self.counter.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.counter.get_name_leafdata())
                            if (self.is_detected.is_set or self.is_detected.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_detected.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "counter" or name == "is-detected"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "counter"):
                                self.counter = value
                                self.counter.value_namespace = name_space
                                self.counter.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-detected"):
                                self.is_detected = value
                                self.is_detected.value_namespace = name_space
                                self.is_detected.value_namespace_prefix = name_space_prefix


                    class LowRx1Power(Entity):
                        """
                        Low Rx1 Power in uints of 0.1 dBm
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx1Power, self).__init__()

                            self.yang_name = "low-rx1-power"
                            self.yang_parent_name = "optics-alarm-info"

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("counter",
                                            "is_detected") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx1Power, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx1Power, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.counter.is_set or
                                self.is_detected.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.counter.yfilter != YFilter.not_set or
                                self.is_detected.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "low-rx1-power" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.counter.is_set or self.counter.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.counter.get_name_leafdata())
                            if (self.is_detected.is_set or self.is_detected.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_detected.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "counter" or name == "is-detected"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "counter"):
                                self.counter = value
                                self.counter.value_namespace = name_space
                                self.counter.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-detected"):
                                self.is_detected = value
                                self.is_detected.value_namespace = name_space
                                self.is_detected.value_namespace_prefix = name_space_prefix


                    class LowRx2Power(Entity):
                        """
                        Low Rx2 Power in uints of 0.1 dBm
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx2Power, self).__init__()

                            self.yang_name = "low-rx2-power"
                            self.yang_parent_name = "optics-alarm-info"

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("counter",
                                            "is_detected") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx2Power, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx2Power, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.counter.is_set or
                                self.is_detected.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.counter.yfilter != YFilter.not_set or
                                self.is_detected.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "low-rx2-power" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.counter.is_set or self.counter.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.counter.get_name_leafdata())
                            if (self.is_detected.is_set or self.is_detected.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_detected.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "counter" or name == "is-detected"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "counter"):
                                self.counter = value
                                self.counter.value_namespace = name_space
                                self.counter.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-detected"):
                                self.is_detected = value
                                self.is_detected.value_namespace = name_space
                                self.is_detected.value_namespace_prefix = name_space_prefix


                    class LowRx3Power(Entity):
                        """
                        Low Rx3 Power in uints of 0.1 dBm
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx3Power, self).__init__()

                            self.yang_name = "low-rx3-power"
                            self.yang_parent_name = "optics-alarm-info"

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("counter",
                                            "is_detected") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx3Power, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx3Power, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.counter.is_set or
                                self.is_detected.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.counter.yfilter != YFilter.not_set or
                                self.is_detected.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "low-rx3-power" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.counter.is_set or self.counter.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.counter.get_name_leafdata())
                            if (self.is_detected.is_set or self.is_detected.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_detected.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "counter" or name == "is-detected"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "counter"):
                                self.counter = value
                                self.counter.value_namespace = name_space
                                self.counter.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-detected"):
                                self.is_detected = value
                                self.is_detected.value_namespace = name_space
                                self.is_detected.value_namespace_prefix = name_space_prefix


                    class LowRx4Power(Entity):
                        """
                        Low Rx4 Power in uints of 0.1 dBm
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx4Power, self).__init__()

                            self.yang_name = "low-rx4-power"
                            self.yang_parent_name = "optics-alarm-info"

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("counter",
                                            "is_detected") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx4Power, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx4Power, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.counter.is_set or
                                self.is_detected.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.counter.yfilter != YFilter.not_set or
                                self.is_detected.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "low-rx4-power" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.counter.is_set or self.counter.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.counter.get_name_leafdata())
                            if (self.is_detected.is_set or self.is_detected.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_detected.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "counter" or name == "is-detected"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "counter"):
                                self.counter = value
                                self.counter.value_namespace = name_space
                                self.counter.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-detected"):
                                self.is_detected = value
                                self.is_detected.value_namespace = name_space
                                self.is_detected.value_namespace_prefix = name_space_prefix


                    class HighTx1Power(Entity):
                        """
                        High Tx1 Power in uints of 0.1 dBm
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx1Power, self).__init__()

                            self.yang_name = "high-tx1-power"
                            self.yang_parent_name = "optics-alarm-info"

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("counter",
                                            "is_detected") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx1Power, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx1Power, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.counter.is_set or
                                self.is_detected.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.counter.yfilter != YFilter.not_set or
                                self.is_detected.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "high-tx1-power" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.counter.is_set or self.counter.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.counter.get_name_leafdata())
                            if (self.is_detected.is_set or self.is_detected.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_detected.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "counter" or name == "is-detected"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "counter"):
                                self.counter = value
                                self.counter.value_namespace = name_space
                                self.counter.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-detected"):
                                self.is_detected = value
                                self.is_detected.value_namespace = name_space
                                self.is_detected.value_namespace_prefix = name_space_prefix


                    class HighTx2Power(Entity):
                        """
                        High Tx2 Power in uints of 0.1 dBm
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx2Power, self).__init__()

                            self.yang_name = "high-tx2-power"
                            self.yang_parent_name = "optics-alarm-info"

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("counter",
                                            "is_detected") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx2Power, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx2Power, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.counter.is_set or
                                self.is_detected.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.counter.yfilter != YFilter.not_set or
                                self.is_detected.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "high-tx2-power" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.counter.is_set or self.counter.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.counter.get_name_leafdata())
                            if (self.is_detected.is_set or self.is_detected.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_detected.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "counter" or name == "is-detected"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "counter"):
                                self.counter = value
                                self.counter.value_namespace = name_space
                                self.counter.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-detected"):
                                self.is_detected = value
                                self.is_detected.value_namespace = name_space
                                self.is_detected.value_namespace_prefix = name_space_prefix


                    class HighTx3Power(Entity):
                        """
                        High Tx3 Power in uints of 0.1 dBm
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx3Power, self).__init__()

                            self.yang_name = "high-tx3-power"
                            self.yang_parent_name = "optics-alarm-info"

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("counter",
                                            "is_detected") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx3Power, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx3Power, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.counter.is_set or
                                self.is_detected.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.counter.yfilter != YFilter.not_set or
                                self.is_detected.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "high-tx3-power" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.counter.is_set or self.counter.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.counter.get_name_leafdata())
                            if (self.is_detected.is_set or self.is_detected.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_detected.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "counter" or name == "is-detected"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "counter"):
                                self.counter = value
                                self.counter.value_namespace = name_space
                                self.counter.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-detected"):
                                self.is_detected = value
                                self.is_detected.value_namespace = name_space
                                self.is_detected.value_namespace_prefix = name_space_prefix


                    class HighTx4Power(Entity):
                        """
                        High Tx4 Power in uints of 0.1 dBm
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx4Power, self).__init__()

                            self.yang_name = "high-tx4-power"
                            self.yang_parent_name = "optics-alarm-info"

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("counter",
                                            "is_detected") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx4Power, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx4Power, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.counter.is_set or
                                self.is_detected.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.counter.yfilter != YFilter.not_set or
                                self.is_detected.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "high-tx4-power" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.counter.is_set or self.counter.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.counter.get_name_leafdata())
                            if (self.is_detected.is_set or self.is_detected.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_detected.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "counter" or name == "is-detected"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "counter"):
                                self.counter = value
                                self.counter.value_namespace = name_space
                                self.counter.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-detected"):
                                self.is_detected = value
                                self.is_detected.value_namespace = name_space
                                self.is_detected.value_namespace_prefix = name_space_prefix


                    class LowTx1Power(Entity):
                        """
                        Low Tx1 Power in uints of 0.1 dBm
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx1Power, self).__init__()

                            self.yang_name = "low-tx1-power"
                            self.yang_parent_name = "optics-alarm-info"

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("counter",
                                            "is_detected") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx1Power, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx1Power, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.counter.is_set or
                                self.is_detected.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.counter.yfilter != YFilter.not_set or
                                self.is_detected.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "low-tx1-power" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.counter.is_set or self.counter.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.counter.get_name_leafdata())
                            if (self.is_detected.is_set or self.is_detected.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_detected.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "counter" or name == "is-detected"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "counter"):
                                self.counter = value
                                self.counter.value_namespace = name_space
                                self.counter.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-detected"):
                                self.is_detected = value
                                self.is_detected.value_namespace = name_space
                                self.is_detected.value_namespace_prefix = name_space_prefix


                    class LowTx2Power(Entity):
                        """
                        Low Tx2 Power in uints of 0.1 dBm
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx2Power, self).__init__()

                            self.yang_name = "low-tx2-power"
                            self.yang_parent_name = "optics-alarm-info"

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("counter",
                                            "is_detected") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx2Power, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx2Power, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.counter.is_set or
                                self.is_detected.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.counter.yfilter != YFilter.not_set or
                                self.is_detected.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "low-tx2-power" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.counter.is_set or self.counter.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.counter.get_name_leafdata())
                            if (self.is_detected.is_set or self.is_detected.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_detected.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "counter" or name == "is-detected"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "counter"):
                                self.counter = value
                                self.counter.value_namespace = name_space
                                self.counter.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-detected"):
                                self.is_detected = value
                                self.is_detected.value_namespace = name_space
                                self.is_detected.value_namespace_prefix = name_space_prefix


                    class LowTx3Power(Entity):
                        """
                        Low Tx3 Power in uints of 0.1 dBm
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx3Power, self).__init__()

                            self.yang_name = "low-tx3-power"
                            self.yang_parent_name = "optics-alarm-info"

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("counter",
                                            "is_detected") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx3Power, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx3Power, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.counter.is_set or
                                self.is_detected.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.counter.yfilter != YFilter.not_set or
                                self.is_detected.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "low-tx3-power" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.counter.is_set or self.counter.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.counter.get_name_leafdata())
                            if (self.is_detected.is_set or self.is_detected.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_detected.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "counter" or name == "is-detected"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "counter"):
                                self.counter = value
                                self.counter.value_namespace = name_space
                                self.counter.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-detected"):
                                self.is_detected = value
                                self.is_detected.value_namespace = name_space
                                self.is_detected.value_namespace_prefix = name_space_prefix


                    class LowTx4Power(Entity):
                        """
                        Low Tx4 Power in uints of 0.1 dBm
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx4Power, self).__init__()

                            self.yang_name = "low-tx4-power"
                            self.yang_parent_name = "optics-alarm-info"

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("counter",
                                            "is_detected") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx4Power, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx4Power, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.counter.is_set or
                                self.is_detected.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.counter.yfilter != YFilter.not_set or
                                self.is_detected.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "low-tx4-power" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.counter.is_set or self.counter.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.counter.get_name_leafdata())
                            if (self.is_detected.is_set or self.is_detected.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_detected.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "counter" or name == "is-detected"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "counter"):
                                self.counter = value
                                self.counter.value_namespace = name_space
                                self.counter.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-detected"):
                                self.is_detected = value
                                self.is_detected.value_namespace = name_space
                                self.is_detected.value_namespace_prefix = name_space_prefix


                    class HighTx1Lbc(Entity):
                        """
                        High Tx1 laser bias current in units of
                        percentage
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx1Lbc, self).__init__()

                            self.yang_name = "high-tx1lbc"
                            self.yang_parent_name = "optics-alarm-info"

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("counter",
                                            "is_detected") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx1Lbc, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx1Lbc, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.counter.is_set or
                                self.is_detected.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.counter.yfilter != YFilter.not_set or
                                self.is_detected.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "high-tx1lbc" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.counter.is_set or self.counter.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.counter.get_name_leafdata())
                            if (self.is_detected.is_set or self.is_detected.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_detected.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "counter" or name == "is-detected"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "counter"):
                                self.counter = value
                                self.counter.value_namespace = name_space
                                self.counter.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-detected"):
                                self.is_detected = value
                                self.is_detected.value_namespace = name_space
                                self.is_detected.value_namespace_prefix = name_space_prefix


                    class HighTx2Lbc(Entity):
                        """
                        High Tx2 laser bias current in units of
                        percentage
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx2Lbc, self).__init__()

                            self.yang_name = "high-tx2lbc"
                            self.yang_parent_name = "optics-alarm-info"

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("counter",
                                            "is_detected") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx2Lbc, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx2Lbc, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.counter.is_set or
                                self.is_detected.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.counter.yfilter != YFilter.not_set or
                                self.is_detected.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "high-tx2lbc" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.counter.is_set or self.counter.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.counter.get_name_leafdata())
                            if (self.is_detected.is_set or self.is_detected.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_detected.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "counter" or name == "is-detected"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "counter"):
                                self.counter = value
                                self.counter.value_namespace = name_space
                                self.counter.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-detected"):
                                self.is_detected = value
                                self.is_detected.value_namespace = name_space
                                self.is_detected.value_namespace_prefix = name_space_prefix


                    class HighTx3Lbc(Entity):
                        """
                        High Tx3 laser bias current in units of
                        percentage
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx3Lbc, self).__init__()

                            self.yang_name = "high-tx3lbc"
                            self.yang_parent_name = "optics-alarm-info"

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("counter",
                                            "is_detected") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx3Lbc, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx3Lbc, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.counter.is_set or
                                self.is_detected.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.counter.yfilter != YFilter.not_set or
                                self.is_detected.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "high-tx3lbc" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.counter.is_set or self.counter.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.counter.get_name_leafdata())
                            if (self.is_detected.is_set or self.is_detected.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_detected.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "counter" or name == "is-detected"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "counter"):
                                self.counter = value
                                self.counter.value_namespace = name_space
                                self.counter.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-detected"):
                                self.is_detected = value
                                self.is_detected.value_namespace = name_space
                                self.is_detected.value_namespace_prefix = name_space_prefix


                    class HighTx4Lbc(Entity):
                        """
                        High Tx4 laser bias current in units of
                        percentage
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx4Lbc, self).__init__()

                            self.yang_name = "high-tx4lbc"
                            self.yang_parent_name = "optics-alarm-info"

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("counter",
                                            "is_detected") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx4Lbc, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx4Lbc, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.counter.is_set or
                                self.is_detected.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.counter.yfilter != YFilter.not_set or
                                self.is_detected.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "high-tx4lbc" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.counter.is_set or self.counter.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.counter.get_name_leafdata())
                            if (self.is_detected.is_set or self.is_detected.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_detected.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "counter" or name == "is-detected"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "counter"):
                                self.counter = value
                                self.counter.value_namespace = name_space
                                self.counter.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-detected"):
                                self.is_detected = value
                                self.is_detected.value_namespace = name_space
                                self.is_detected.value_namespace_prefix = name_space_prefix


                    class LowTx1Lbc(Entity):
                        """
                        Low Tx1 laser bias current in units of
                        percentage
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx1Lbc, self).__init__()

                            self.yang_name = "low-tx1lbc"
                            self.yang_parent_name = "optics-alarm-info"

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("counter",
                                            "is_detected") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx1Lbc, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx1Lbc, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.counter.is_set or
                                self.is_detected.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.counter.yfilter != YFilter.not_set or
                                self.is_detected.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "low-tx1lbc" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.counter.is_set or self.counter.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.counter.get_name_leafdata())
                            if (self.is_detected.is_set or self.is_detected.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_detected.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "counter" or name == "is-detected"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "counter"):
                                self.counter = value
                                self.counter.value_namespace = name_space
                                self.counter.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-detected"):
                                self.is_detected = value
                                self.is_detected.value_namespace = name_space
                                self.is_detected.value_namespace_prefix = name_space_prefix


                    class LowTx2Lbc(Entity):
                        """
                        Low Tx2 laser bias current in units of
                        percentage
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx2Lbc, self).__init__()

                            self.yang_name = "low-tx2lbc"
                            self.yang_parent_name = "optics-alarm-info"

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("counter",
                                            "is_detected") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx2Lbc, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx2Lbc, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.counter.is_set or
                                self.is_detected.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.counter.yfilter != YFilter.not_set or
                                self.is_detected.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "low-tx2lbc" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.counter.is_set or self.counter.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.counter.get_name_leafdata())
                            if (self.is_detected.is_set or self.is_detected.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_detected.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "counter" or name == "is-detected"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "counter"):
                                self.counter = value
                                self.counter.value_namespace = name_space
                                self.counter.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-detected"):
                                self.is_detected = value
                                self.is_detected.value_namespace = name_space
                                self.is_detected.value_namespace_prefix = name_space_prefix


                    class LowTx3Lbc(Entity):
                        """
                        Low Tx3 laser bias current in units of
                        percentage
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx3Lbc, self).__init__()

                            self.yang_name = "low-tx3lbc"
                            self.yang_parent_name = "optics-alarm-info"

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("counter",
                                            "is_detected") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx3Lbc, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx3Lbc, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.counter.is_set or
                                self.is_detected.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.counter.yfilter != YFilter.not_set or
                                self.is_detected.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "low-tx3lbc" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.counter.is_set or self.counter.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.counter.get_name_leafdata())
                            if (self.is_detected.is_set or self.is_detected.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_detected.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "counter" or name == "is-detected"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "counter"):
                                self.counter = value
                                self.counter.value_namespace = name_space
                                self.counter.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-detected"):
                                self.is_detected = value
                                self.is_detected.value_namespace = name_space
                                self.is_detected.value_namespace_prefix = name_space_prefix


                    class LowTx4Lbc(Entity):
                        """
                        Low Tx4 laser bias current in units of
                        percentage
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx4Lbc, self).__init__()

                            self.yang_name = "low-tx4lbc"
                            self.yang_parent_name = "optics-alarm-info"

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("counter",
                                            "is_detected") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx4Lbc, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx4Lbc, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.counter.is_set or
                                self.is_detected.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.counter.yfilter != YFilter.not_set or
                                self.is_detected.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "low-tx4lbc" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.counter.is_set or self.counter.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.counter.get_name_leafdata())
                            if (self.is_detected.is_set or self.is_detected.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_detected.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "counter" or name == "is-detected"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "counter"):
                                self.counter = value
                                self.counter.value_namespace = name_space
                                self.counter.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-detected"):
                                self.is_detected = value
                                self.is_detected.value_namespace = name_space
                                self.is_detected.value_namespace_prefix = name_space_prefix


                    class RxLos(Entity):
                        """
                        RX LOS
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.RxLos, self).__init__()

                            self.yang_name = "rx-los"
                            self.yang_parent_name = "optics-alarm-info"

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("counter",
                                            "is_detected") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.RxLos, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.RxLos, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.counter.is_set or
                                self.is_detected.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.counter.yfilter != YFilter.not_set or
                                self.is_detected.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "rx-los" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.counter.is_set or self.counter.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.counter.get_name_leafdata())
                            if (self.is_detected.is_set or self.is_detected.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_detected.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "counter" or name == "is-detected"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "counter"):
                                self.counter = value
                                self.counter.value_namespace = name_space
                                self.counter.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-detected"):
                                self.is_detected = value
                                self.is_detected.value_namespace = name_space
                                self.is_detected.value_namespace_prefix = name_space_prefix


                    class TxLos(Entity):
                        """
                        TX LOS
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxLos, self).__init__()

                            self.yang_name = "tx-los"
                            self.yang_parent_name = "optics-alarm-info"

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("counter",
                                            "is_detected") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxLos, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxLos, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.counter.is_set or
                                self.is_detected.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.counter.yfilter != YFilter.not_set or
                                self.is_detected.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "tx-los" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.counter.is_set or self.counter.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.counter.get_name_leafdata())
                            if (self.is_detected.is_set or self.is_detected.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_detected.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "counter" or name == "is-detected"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "counter"):
                                self.counter = value
                                self.counter.value_namespace = name_space
                                self.counter.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-detected"):
                                self.is_detected = value
                                self.is_detected.value_namespace = name_space
                                self.is_detected.value_namespace_prefix = name_space_prefix


                    class RxLol(Entity):
                        """
                        RX LOL
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.RxLol, self).__init__()

                            self.yang_name = "rx-lol"
                            self.yang_parent_name = "optics-alarm-info"

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("counter",
                                            "is_detected") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.RxLol, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.RxLol, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.counter.is_set or
                                self.is_detected.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.counter.yfilter != YFilter.not_set or
                                self.is_detected.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "rx-lol" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.counter.is_set or self.counter.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.counter.get_name_leafdata())
                            if (self.is_detected.is_set or self.is_detected.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_detected.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "counter" or name == "is-detected"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "counter"):
                                self.counter = value
                                self.counter.value_namespace = name_space
                                self.counter.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-detected"):
                                self.is_detected = value
                                self.is_detected.value_namespace = name_space
                                self.is_detected.value_namespace_prefix = name_space_prefix


                    class TxLol(Entity):
                        """
                        TX LOL
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxLol, self).__init__()

                            self.yang_name = "tx-lol"
                            self.yang_parent_name = "optics-alarm-info"

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("counter",
                                            "is_detected") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxLol, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxLol, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.counter.is_set or
                                self.is_detected.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.counter.yfilter != YFilter.not_set or
                                self.is_detected.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "tx-lol" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.counter.is_set or self.counter.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.counter.get_name_leafdata())
                            if (self.is_detected.is_set or self.is_detected.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_detected.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "counter" or name == "is-detected"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "counter"):
                                self.counter = value
                                self.counter.value_namespace = name_space
                                self.counter.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-detected"):
                                self.is_detected = value
                                self.is_detected.value_namespace = name_space
                                self.is_detected.value_namespace_prefix = name_space_prefix


                    class TxFault(Entity):
                        """
                        TX Fault
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxFault, self).__init__()

                            self.yang_name = "tx-fault"
                            self.yang_parent_name = "optics-alarm-info"

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("counter",
                                            "is_detected") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxFault, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxFault, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.counter.is_set or
                                self.is_detected.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.counter.yfilter != YFilter.not_set or
                                self.is_detected.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "tx-fault" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.counter.is_set or self.counter.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.counter.get_name_leafdata())
                            if (self.is_detected.is_set or self.is_detected.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_detected.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "counter" or name == "is-detected"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "counter"):
                                self.counter = value
                                self.counter.value_namespace = name_space
                                self.counter.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-detected"):
                                self.is_detected = value
                                self.is_detected.value_namespace = name_space
                                self.is_detected.value_namespace_prefix = name_space_prefix


                    class Hidgd(Entity):
                        """
                        HI DGD
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Hidgd, self).__init__()

                            self.yang_name = "hidgd"
                            self.yang_parent_name = "optics-alarm-info"

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("counter",
                                            "is_detected") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Hidgd, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Hidgd, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.counter.is_set or
                                self.is_detected.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.counter.yfilter != YFilter.not_set or
                                self.is_detected.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "hidgd" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.counter.is_set or self.counter.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.counter.get_name_leafdata())
                            if (self.is_detected.is_set or self.is_detected.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_detected.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "counter" or name == "is-detected"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "counter"):
                                self.counter = value
                                self.counter.value_namespace = name_space
                                self.counter.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-detected"):
                                self.is_detected = value
                                self.is_detected.value_namespace = name_space
                                self.is_detected.value_namespace_prefix = name_space_prefix


                    class Oorcd(Entity):
                        """
                        OOR CD
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Oorcd, self).__init__()

                            self.yang_name = "oorcd"
                            self.yang_parent_name = "optics-alarm-info"

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("counter",
                                            "is_detected") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Oorcd, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Oorcd, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.counter.is_set or
                                self.is_detected.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.counter.yfilter != YFilter.not_set or
                                self.is_detected.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "oorcd" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.counter.is_set or self.counter.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.counter.get_name_leafdata())
                            if (self.is_detected.is_set or self.is_detected.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_detected.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "counter" or name == "is-detected"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "counter"):
                                self.counter = value
                                self.counter.value_namespace = name_space
                                self.counter.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-detected"):
                                self.is_detected = value
                                self.is_detected.value_namespace = name_space
                                self.is_detected.value_namespace_prefix = name_space_prefix


                    class Osnr(Entity):
                        """
                        OSNR
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Osnr, self).__init__()

                            self.yang_name = "osnr"
                            self.yang_parent_name = "optics-alarm-info"

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("counter",
                                            "is_detected") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Osnr, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Osnr, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.counter.is_set or
                                self.is_detected.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.counter.yfilter != YFilter.not_set or
                                self.is_detected.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "osnr" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.counter.is_set or self.counter.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.counter.get_name_leafdata())
                            if (self.is_detected.is_set or self.is_detected.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_detected.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "counter" or name == "is-detected"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "counter"):
                                self.counter = value
                                self.counter.value_namespace = name_space
                                self.counter.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-detected"):
                                self.is_detected = value
                                self.is_detected.value_namespace = name_space
                                self.is_detected.value_namespace_prefix = name_space_prefix


                    class Wvlool(Entity):
                        """
                        WVL OOL
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Wvlool, self).__init__()

                            self.yang_name = "wvlool"
                            self.yang_parent_name = "optics-alarm-info"

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("counter",
                                            "is_detected") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Wvlool, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Wvlool, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.counter.is_set or
                                self.is_detected.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.counter.yfilter != YFilter.not_set or
                                self.is_detected.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "wvlool" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.counter.is_set or self.counter.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.counter.get_name_leafdata())
                            if (self.is_detected.is_set or self.is_detected.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_detected.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "counter" or name == "is-detected"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "counter"):
                                self.counter = value
                                self.counter.value_namespace = name_space
                                self.counter.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-detected"):
                                self.is_detected = value
                                self.is_detected.value_namespace = name_space
                                self.is_detected.value_namespace_prefix = name_space_prefix


                    class Mea(Entity):
                        """
                        MEA
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Mea, self).__init__()

                            self.yang_name = "mea"
                            self.yang_parent_name = "optics-alarm-info"

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("counter",
                                            "is_detected") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Mea, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Mea, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.counter.is_set or
                                self.is_detected.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.counter.yfilter != YFilter.not_set or
                                self.is_detected.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "mea" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.counter.is_set or self.counter.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.counter.get_name_leafdata())
                            if (self.is_detected.is_set or self.is_detected.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_detected.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "counter" or name == "is-detected"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "counter"):
                                self.counter = value
                                self.counter.value_namespace = name_space
                                self.counter.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-detected"):
                                self.is_detected = value
                                self.is_detected.value_namespace = name_space
                                self.is_detected.value_namespace_prefix = name_space_prefix


                    class ImpRemoval(Entity):
                        """
                        IMPROPER REM
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.ImpRemoval, self).__init__()

                            self.yang_name = "imp-removal"
                            self.yang_parent_name = "optics-alarm-info"

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("counter",
                                            "is_detected") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.ImpRemoval, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.ImpRemoval, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.counter.is_set or
                                self.is_detected.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.counter.yfilter != YFilter.not_set or
                                self.is_detected.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "imp-removal" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.counter.is_set or self.counter.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.counter.get_name_leafdata())
                            if (self.is_detected.is_set or self.is_detected.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_detected.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "counter" or name == "is-detected"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "counter"):
                                self.counter = value
                                self.counter.value_namespace = name_space
                                self.counter.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-detected"):
                                self.is_detected = value
                                self.is_detected.value_namespace = name_space
                                self.is_detected.value_namespace_prefix = name_space_prefix


                    class RxLoc(Entity):
                        """
                        Rx LOC
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.RxLoc, self).__init__()

                            self.yang_name = "rx-loc"
                            self.yang_parent_name = "optics-alarm-info"

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("counter",
                                            "is_detected") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.RxLoc, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.RxLoc, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.counter.is_set or
                                self.is_detected.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.counter.yfilter != YFilter.not_set or
                                self.is_detected.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "rx-loc" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.counter.is_set or self.counter.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.counter.get_name_leafdata())
                            if (self.is_detected.is_set or self.is_detected.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_detected.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "counter" or name == "is-detected"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "counter"):
                                self.counter = value
                                self.counter.value_namespace = name_space
                                self.counter.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-detected"):
                                self.is_detected = value
                                self.is_detected.value_namespace = name_space
                                self.is_detected.value_namespace_prefix = name_space_prefix


                    class AmpGainDegLow(Entity):
                        """
                        Ampli Gain Deg Low
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.AmpGainDegLow, self).__init__()

                            self.yang_name = "amp-gain-deg-low"
                            self.yang_parent_name = "optics-alarm-info"

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("counter",
                                            "is_detected") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.AmpGainDegLow, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.AmpGainDegLow, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.counter.is_set or
                                self.is_detected.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.counter.yfilter != YFilter.not_set or
                                self.is_detected.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "amp-gain-deg-low" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.counter.is_set or self.counter.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.counter.get_name_leafdata())
                            if (self.is_detected.is_set or self.is_detected.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_detected.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "counter" or name == "is-detected"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "counter"):
                                self.counter = value
                                self.counter.value_namespace = name_space
                                self.counter.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-detected"):
                                self.is_detected = value
                                self.is_detected.value_namespace = name_space
                                self.is_detected.value_namespace_prefix = name_space_prefix


                    class AmpGainDegHigh(Entity):
                        """
                        Ampli Gain Deg High
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.AmpGainDegHigh, self).__init__()

                            self.yang_name = "amp-gain-deg-high"
                            self.yang_parent_name = "optics-alarm-info"

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("counter",
                                            "is_detected") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.AmpGainDegHigh, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.AmpGainDegHigh, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.counter.is_set or
                                self.is_detected.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.counter.yfilter != YFilter.not_set or
                                self.is_detected.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "amp-gain-deg-high" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.counter.is_set or self.counter.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.counter.get_name_leafdata())
                            if (self.is_detected.is_set or self.is_detected.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_detected.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "counter" or name == "is-detected"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "counter"):
                                self.counter = value
                                self.counter.value_namespace = name_space
                                self.counter.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-detected"):
                                self.is_detected = value
                                self.is_detected.value_namespace = name_space
                                self.is_detected.value_namespace_prefix = name_space_prefix


                    class TxpwrMismatch(Entity):
                        """
                        TX POWER PROV MISMATCH
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxpwrMismatch, self).__init__()

                            self.yang_name = "txpwr-mismatch"
                            self.yang_parent_name = "optics-alarm-info"

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("counter",
                                            "is_detected") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxpwrMismatch, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxpwrMismatch, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.counter.is_set or
                                self.is_detected.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.counter.yfilter != YFilter.not_set or
                                self.is_detected.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "txpwr-mismatch" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.counter.is_set or self.counter.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.counter.get_name_leafdata())
                            if (self.is_detected.is_set or self.is_detected.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_detected.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "counter" or name == "is-detected"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "counter"):
                                self.counter = value
                                self.counter.value_namespace = name_space
                                self.counter.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-detected"):
                                self.is_detected = value
                                self.is_detected.value_namespace = name_space
                                self.is_detected.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            (self.amp_gain_deg_high is not None and self.amp_gain_deg_high.has_data()) or
                            (self.amp_gain_deg_low is not None and self.amp_gain_deg_low.has_data()) or
                            (self.hidgd is not None and self.hidgd.has_data()) or
                            (self.high_lbc is not None and self.high_lbc.has_data()) or
                            (self.high_rx1_power is not None and self.high_rx1_power.has_data()) or
                            (self.high_rx2_power is not None and self.high_rx2_power.has_data()) or
                            (self.high_rx3_power is not None and self.high_rx3_power.has_data()) or
                            (self.high_rx4_power is not None and self.high_rx4_power.has_data()) or
                            (self.high_rx_power is not None and self.high_rx_power.has_data()) or
                            (self.high_tx1_power is not None and self.high_tx1_power.has_data()) or
                            (self.high_tx1lbc is not None and self.high_tx1lbc.has_data()) or
                            (self.high_tx2_power is not None and self.high_tx2_power.has_data()) or
                            (self.high_tx2lbc is not None and self.high_tx2lbc.has_data()) or
                            (self.high_tx3_power is not None and self.high_tx3_power.has_data()) or
                            (self.high_tx3lbc is not None and self.high_tx3lbc.has_data()) or
                            (self.high_tx4_power is not None and self.high_tx4_power.has_data()) or
                            (self.high_tx4lbc is not None and self.high_tx4lbc.has_data()) or
                            (self.high_tx_power is not None and self.high_tx_power.has_data()) or
                            (self.imp_removal is not None and self.imp_removal.has_data()) or
                            (self.low_rx1_power is not None and self.low_rx1_power.has_data()) or
                            (self.low_rx2_power is not None and self.low_rx2_power.has_data()) or
                            (self.low_rx3_power is not None and self.low_rx3_power.has_data()) or
                            (self.low_rx4_power is not None and self.low_rx4_power.has_data()) or
                            (self.low_rx_power is not None and self.low_rx_power.has_data()) or
                            (self.low_tx1_power is not None and self.low_tx1_power.has_data()) or
                            (self.low_tx1lbc is not None and self.low_tx1lbc.has_data()) or
                            (self.low_tx2_power is not None and self.low_tx2_power.has_data()) or
                            (self.low_tx2lbc is not None and self.low_tx2lbc.has_data()) or
                            (self.low_tx3_power is not None and self.low_tx3_power.has_data()) or
                            (self.low_tx3lbc is not None and self.low_tx3lbc.has_data()) or
                            (self.low_tx4_power is not None and self.low_tx4_power.has_data()) or
                            (self.low_tx4lbc is not None and self.low_tx4lbc.has_data()) or
                            (self.low_tx_power is not None and self.low_tx_power.has_data()) or
                            (self.mea is not None and self.mea.has_data()) or
                            (self.oorcd is not None and self.oorcd.has_data()) or
                            (self.osnr is not None and self.osnr.has_data()) or
                            (self.rx_loc is not None and self.rx_loc.has_data()) or
                            (self.rx_lol is not None and self.rx_lol.has_data()) or
                            (self.rx_los is not None and self.rx_los.has_data()) or
                            (self.tx_fault is not None and self.tx_fault.has_data()) or
                            (self.tx_lol is not None and self.tx_lol.has_data()) or
                            (self.tx_los is not None and self.tx_los.has_data()) or
                            (self.txpwr_mismatch is not None and self.txpwr_mismatch.has_data()) or
                            (self.wvlool is not None and self.wvlool.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            (self.amp_gain_deg_high is not None and self.amp_gain_deg_high.has_operation()) or
                            (self.amp_gain_deg_low is not None and self.amp_gain_deg_low.has_operation()) or
                            (self.hidgd is not None and self.hidgd.has_operation()) or
                            (self.high_lbc is not None and self.high_lbc.has_operation()) or
                            (self.high_rx1_power is not None and self.high_rx1_power.has_operation()) or
                            (self.high_rx2_power is not None and self.high_rx2_power.has_operation()) or
                            (self.high_rx3_power is not None and self.high_rx3_power.has_operation()) or
                            (self.high_rx4_power is not None and self.high_rx4_power.has_operation()) or
                            (self.high_rx_power is not None and self.high_rx_power.has_operation()) or
                            (self.high_tx1_power is not None and self.high_tx1_power.has_operation()) or
                            (self.high_tx1lbc is not None and self.high_tx1lbc.has_operation()) or
                            (self.high_tx2_power is not None and self.high_tx2_power.has_operation()) or
                            (self.high_tx2lbc is not None and self.high_tx2lbc.has_operation()) or
                            (self.high_tx3_power is not None and self.high_tx3_power.has_operation()) or
                            (self.high_tx3lbc is not None and self.high_tx3lbc.has_operation()) or
                            (self.high_tx4_power is not None and self.high_tx4_power.has_operation()) or
                            (self.high_tx4lbc is not None and self.high_tx4lbc.has_operation()) or
                            (self.high_tx_power is not None and self.high_tx_power.has_operation()) or
                            (self.imp_removal is not None and self.imp_removal.has_operation()) or
                            (self.low_rx1_power is not None and self.low_rx1_power.has_operation()) or
                            (self.low_rx2_power is not None and self.low_rx2_power.has_operation()) or
                            (self.low_rx3_power is not None and self.low_rx3_power.has_operation()) or
                            (self.low_rx4_power is not None and self.low_rx4_power.has_operation()) or
                            (self.low_rx_power is not None and self.low_rx_power.has_operation()) or
                            (self.low_tx1_power is not None and self.low_tx1_power.has_operation()) or
                            (self.low_tx1lbc is not None and self.low_tx1lbc.has_operation()) or
                            (self.low_tx2_power is not None and self.low_tx2_power.has_operation()) or
                            (self.low_tx2lbc is not None and self.low_tx2lbc.has_operation()) or
                            (self.low_tx3_power is not None and self.low_tx3_power.has_operation()) or
                            (self.low_tx3lbc is not None and self.low_tx3lbc.has_operation()) or
                            (self.low_tx4_power is not None and self.low_tx4_power.has_operation()) or
                            (self.low_tx4lbc is not None and self.low_tx4lbc.has_operation()) or
                            (self.low_tx_power is not None and self.low_tx_power.has_operation()) or
                            (self.mea is not None and self.mea.has_operation()) or
                            (self.oorcd is not None and self.oorcd.has_operation()) or
                            (self.osnr is not None and self.osnr.has_operation()) or
                            (self.rx_loc is not None and self.rx_loc.has_operation()) or
                            (self.rx_lol is not None and self.rx_lol.has_operation()) or
                            (self.rx_los is not None and self.rx_los.has_operation()) or
                            (self.tx_fault is not None and self.tx_fault.has_operation()) or
                            (self.tx_lol is not None and self.tx_lol.has_operation()) or
                            (self.tx_los is not None and self.tx_los.has_operation()) or
                            (self.txpwr_mismatch is not None and self.txpwr_mismatch.has_operation()) or
                            (self.wvlool is not None and self.wvlool.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "optics-alarm-info" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "amp-gain-deg-high"):
                            if (self.amp_gain_deg_high is None):
                                self.amp_gain_deg_high = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.AmpGainDegHigh()
                                self.amp_gain_deg_high.parent = self
                                self._children_name_map["amp_gain_deg_high"] = "amp-gain-deg-high"
                            return self.amp_gain_deg_high

                        if (child_yang_name == "amp-gain-deg-low"):
                            if (self.amp_gain_deg_low is None):
                                self.amp_gain_deg_low = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.AmpGainDegLow()
                                self.amp_gain_deg_low.parent = self
                                self._children_name_map["amp_gain_deg_low"] = "amp-gain-deg-low"
                            return self.amp_gain_deg_low

                        if (child_yang_name == "hidgd"):
                            if (self.hidgd is None):
                                self.hidgd = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Hidgd()
                                self.hidgd.parent = self
                                self._children_name_map["hidgd"] = "hidgd"
                            return self.hidgd

                        if (child_yang_name == "high-lbc"):
                            if (self.high_lbc is None):
                                self.high_lbc = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighLbc()
                                self.high_lbc.parent = self
                                self._children_name_map["high_lbc"] = "high-lbc"
                            return self.high_lbc

                        if (child_yang_name == "high-rx1-power"):
                            if (self.high_rx1_power is None):
                                self.high_rx1_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx1Power()
                                self.high_rx1_power.parent = self
                                self._children_name_map["high_rx1_power"] = "high-rx1-power"
                            return self.high_rx1_power

                        if (child_yang_name == "high-rx2-power"):
                            if (self.high_rx2_power is None):
                                self.high_rx2_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx2Power()
                                self.high_rx2_power.parent = self
                                self._children_name_map["high_rx2_power"] = "high-rx2-power"
                            return self.high_rx2_power

                        if (child_yang_name == "high-rx3-power"):
                            if (self.high_rx3_power is None):
                                self.high_rx3_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx3Power()
                                self.high_rx3_power.parent = self
                                self._children_name_map["high_rx3_power"] = "high-rx3-power"
                            return self.high_rx3_power

                        if (child_yang_name == "high-rx4-power"):
                            if (self.high_rx4_power is None):
                                self.high_rx4_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx4Power()
                                self.high_rx4_power.parent = self
                                self._children_name_map["high_rx4_power"] = "high-rx4-power"
                            return self.high_rx4_power

                        if (child_yang_name == "high-rx-power"):
                            if (self.high_rx_power is None):
                                self.high_rx_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRxPower()
                                self.high_rx_power.parent = self
                                self._children_name_map["high_rx_power"] = "high-rx-power"
                            return self.high_rx_power

                        if (child_yang_name == "high-tx1-power"):
                            if (self.high_tx1_power is None):
                                self.high_tx1_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx1Power()
                                self.high_tx1_power.parent = self
                                self._children_name_map["high_tx1_power"] = "high-tx1-power"
                            return self.high_tx1_power

                        if (child_yang_name == "high-tx1lbc"):
                            if (self.high_tx1lbc is None):
                                self.high_tx1lbc = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx1Lbc()
                                self.high_tx1lbc.parent = self
                                self._children_name_map["high_tx1lbc"] = "high-tx1lbc"
                            return self.high_tx1lbc

                        if (child_yang_name == "high-tx2-power"):
                            if (self.high_tx2_power is None):
                                self.high_tx2_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx2Power()
                                self.high_tx2_power.parent = self
                                self._children_name_map["high_tx2_power"] = "high-tx2-power"
                            return self.high_tx2_power

                        if (child_yang_name == "high-tx2lbc"):
                            if (self.high_tx2lbc is None):
                                self.high_tx2lbc = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx2Lbc()
                                self.high_tx2lbc.parent = self
                                self._children_name_map["high_tx2lbc"] = "high-tx2lbc"
                            return self.high_tx2lbc

                        if (child_yang_name == "high-tx3-power"):
                            if (self.high_tx3_power is None):
                                self.high_tx3_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx3Power()
                                self.high_tx3_power.parent = self
                                self._children_name_map["high_tx3_power"] = "high-tx3-power"
                            return self.high_tx3_power

                        if (child_yang_name == "high-tx3lbc"):
                            if (self.high_tx3lbc is None):
                                self.high_tx3lbc = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx3Lbc()
                                self.high_tx3lbc.parent = self
                                self._children_name_map["high_tx3lbc"] = "high-tx3lbc"
                            return self.high_tx3lbc

                        if (child_yang_name == "high-tx4-power"):
                            if (self.high_tx4_power is None):
                                self.high_tx4_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx4Power()
                                self.high_tx4_power.parent = self
                                self._children_name_map["high_tx4_power"] = "high-tx4-power"
                            return self.high_tx4_power

                        if (child_yang_name == "high-tx4lbc"):
                            if (self.high_tx4lbc is None):
                                self.high_tx4lbc = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx4Lbc()
                                self.high_tx4lbc.parent = self
                                self._children_name_map["high_tx4lbc"] = "high-tx4lbc"
                            return self.high_tx4lbc

                        if (child_yang_name == "high-tx-power"):
                            if (self.high_tx_power is None):
                                self.high_tx_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTxPower()
                                self.high_tx_power.parent = self
                                self._children_name_map["high_tx_power"] = "high-tx-power"
                            return self.high_tx_power

                        if (child_yang_name == "imp-removal"):
                            if (self.imp_removal is None):
                                self.imp_removal = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.ImpRemoval()
                                self.imp_removal.parent = self
                                self._children_name_map["imp_removal"] = "imp-removal"
                            return self.imp_removal

                        if (child_yang_name == "low-rx1-power"):
                            if (self.low_rx1_power is None):
                                self.low_rx1_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx1Power()
                                self.low_rx1_power.parent = self
                                self._children_name_map["low_rx1_power"] = "low-rx1-power"
                            return self.low_rx1_power

                        if (child_yang_name == "low-rx2-power"):
                            if (self.low_rx2_power is None):
                                self.low_rx2_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx2Power()
                                self.low_rx2_power.parent = self
                                self._children_name_map["low_rx2_power"] = "low-rx2-power"
                            return self.low_rx2_power

                        if (child_yang_name == "low-rx3-power"):
                            if (self.low_rx3_power is None):
                                self.low_rx3_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx3Power()
                                self.low_rx3_power.parent = self
                                self._children_name_map["low_rx3_power"] = "low-rx3-power"
                            return self.low_rx3_power

                        if (child_yang_name == "low-rx4-power"):
                            if (self.low_rx4_power is None):
                                self.low_rx4_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx4Power()
                                self.low_rx4_power.parent = self
                                self._children_name_map["low_rx4_power"] = "low-rx4-power"
                            return self.low_rx4_power

                        if (child_yang_name == "low-rx-power"):
                            if (self.low_rx_power is None):
                                self.low_rx_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRxPower()
                                self.low_rx_power.parent = self
                                self._children_name_map["low_rx_power"] = "low-rx-power"
                            return self.low_rx_power

                        if (child_yang_name == "low-tx1-power"):
                            if (self.low_tx1_power is None):
                                self.low_tx1_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx1Power()
                                self.low_tx1_power.parent = self
                                self._children_name_map["low_tx1_power"] = "low-tx1-power"
                            return self.low_tx1_power

                        if (child_yang_name == "low-tx1lbc"):
                            if (self.low_tx1lbc is None):
                                self.low_tx1lbc = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx1Lbc()
                                self.low_tx1lbc.parent = self
                                self._children_name_map["low_tx1lbc"] = "low-tx1lbc"
                            return self.low_tx1lbc

                        if (child_yang_name == "low-tx2-power"):
                            if (self.low_tx2_power is None):
                                self.low_tx2_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx2Power()
                                self.low_tx2_power.parent = self
                                self._children_name_map["low_tx2_power"] = "low-tx2-power"
                            return self.low_tx2_power

                        if (child_yang_name == "low-tx2lbc"):
                            if (self.low_tx2lbc is None):
                                self.low_tx2lbc = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx2Lbc()
                                self.low_tx2lbc.parent = self
                                self._children_name_map["low_tx2lbc"] = "low-tx2lbc"
                            return self.low_tx2lbc

                        if (child_yang_name == "low-tx3-power"):
                            if (self.low_tx3_power is None):
                                self.low_tx3_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx3Power()
                                self.low_tx3_power.parent = self
                                self._children_name_map["low_tx3_power"] = "low-tx3-power"
                            return self.low_tx3_power

                        if (child_yang_name == "low-tx3lbc"):
                            if (self.low_tx3lbc is None):
                                self.low_tx3lbc = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx3Lbc()
                                self.low_tx3lbc.parent = self
                                self._children_name_map["low_tx3lbc"] = "low-tx3lbc"
                            return self.low_tx3lbc

                        if (child_yang_name == "low-tx4-power"):
                            if (self.low_tx4_power is None):
                                self.low_tx4_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx4Power()
                                self.low_tx4_power.parent = self
                                self._children_name_map["low_tx4_power"] = "low-tx4-power"
                            return self.low_tx4_power

                        if (child_yang_name == "low-tx4lbc"):
                            if (self.low_tx4lbc is None):
                                self.low_tx4lbc = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx4Lbc()
                                self.low_tx4lbc.parent = self
                                self._children_name_map["low_tx4lbc"] = "low-tx4lbc"
                            return self.low_tx4lbc

                        if (child_yang_name == "low-tx-power"):
                            if (self.low_tx_power is None):
                                self.low_tx_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTxPower()
                                self.low_tx_power.parent = self
                                self._children_name_map["low_tx_power"] = "low-tx-power"
                            return self.low_tx_power

                        if (child_yang_name == "mea"):
                            if (self.mea is None):
                                self.mea = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Mea()
                                self.mea.parent = self
                                self._children_name_map["mea"] = "mea"
                            return self.mea

                        if (child_yang_name == "oorcd"):
                            if (self.oorcd is None):
                                self.oorcd = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Oorcd()
                                self.oorcd.parent = self
                                self._children_name_map["oorcd"] = "oorcd"
                            return self.oorcd

                        if (child_yang_name == "osnr"):
                            if (self.osnr is None):
                                self.osnr = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Osnr()
                                self.osnr.parent = self
                                self._children_name_map["osnr"] = "osnr"
                            return self.osnr

                        if (child_yang_name == "rx-loc"):
                            if (self.rx_loc is None):
                                self.rx_loc = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.RxLoc()
                                self.rx_loc.parent = self
                                self._children_name_map["rx_loc"] = "rx-loc"
                            return self.rx_loc

                        if (child_yang_name == "rx-lol"):
                            if (self.rx_lol is None):
                                self.rx_lol = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.RxLol()
                                self.rx_lol.parent = self
                                self._children_name_map["rx_lol"] = "rx-lol"
                            return self.rx_lol

                        if (child_yang_name == "rx-los"):
                            if (self.rx_los is None):
                                self.rx_los = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.RxLos()
                                self.rx_los.parent = self
                                self._children_name_map["rx_los"] = "rx-los"
                            return self.rx_los

                        if (child_yang_name == "tx-fault"):
                            if (self.tx_fault is None):
                                self.tx_fault = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxFault()
                                self.tx_fault.parent = self
                                self._children_name_map["tx_fault"] = "tx-fault"
                            return self.tx_fault

                        if (child_yang_name == "tx-lol"):
                            if (self.tx_lol is None):
                                self.tx_lol = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxLol()
                                self.tx_lol.parent = self
                                self._children_name_map["tx_lol"] = "tx-lol"
                            return self.tx_lol

                        if (child_yang_name == "tx-los"):
                            if (self.tx_los is None):
                                self.tx_los = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxLos()
                                self.tx_los.parent = self
                                self._children_name_map["tx_los"] = "tx-los"
                            return self.tx_los

                        if (child_yang_name == "txpwr-mismatch"):
                            if (self.txpwr_mismatch is None):
                                self.txpwr_mismatch = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxpwrMismatch()
                                self.txpwr_mismatch.parent = self
                                self._children_name_map["txpwr_mismatch"] = "txpwr-mismatch"
                            return self.txpwr_mismatch

                        if (child_yang_name == "wvlool"):
                            if (self.wvlool is None):
                                self.wvlool = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Wvlool()
                                self.wvlool.parent = self
                                self._children_name_map["wvlool"] = "wvlool"
                            return self.wvlool

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "amp-gain-deg-high" or name == "amp-gain-deg-low" or name == "hidgd" or name == "high-lbc" or name == "high-rx1-power" or name == "high-rx2-power" or name == "high-rx3-power" or name == "high-rx4-power" or name == "high-rx-power" or name == "high-tx1-power" or name == "high-tx1lbc" or name == "high-tx2-power" or name == "high-tx2lbc" or name == "high-tx3-power" or name == "high-tx3lbc" or name == "high-tx4-power" or name == "high-tx4lbc" or name == "high-tx-power" or name == "imp-removal" or name == "low-rx1-power" or name == "low-rx2-power" or name == "low-rx3-power" or name == "low-rx4-power" or name == "low-rx-power" or name == "low-tx1-power" or name == "low-tx1lbc" or name == "low-tx2-power" or name == "low-tx2lbc" or name == "low-tx3-power" or name == "low-tx3lbc" or name == "low-tx4-power" or name == "low-tx4lbc" or name == "low-tx-power" or name == "mea" or name == "oorcd" or name == "osnr" or name == "rx-loc" or name == "rx-lol" or name == "rx-los" or name == "tx-fault" or name == "tx-lol" or name == "tx-los" or name == "txpwr-mismatch" or name == "wvlool"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class OtsAlarmInfo(Entity):
                    """
                    Ots Alarm Information
                    
                    .. attribute:: amp_gain_deg_high
                    
                    	Ampli Gain Deg High
                    	**type**\:   :py:class:`AmpGainDegHigh <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AmpGainDegHigh>`
                    
                    .. attribute:: amp_gain_deg_low
                    
                    	Ampli Gain Deg Low
                    	**type**\:   :py:class:`AmpGainDegLow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AmpGainDegLow>`
                    
                    .. attribute:: auto_ampli_ctrl_config_mismatch
                    
                    	Auto Ampli Ctrl Config Mismatch
                    	**type**\:   :py:class:`AutoAmpliCtrlConfigMismatch <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AutoAmpliCtrlConfigMismatch>`
                    
                    .. attribute:: auto_ampli_ctrl_disabled
                    
                    	Auto Ampli Ctrl Disabled
                    	**type**\:   :py:class:`AutoAmpliCtrlDisabled <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AutoAmpliCtrlDisabled>`
                    
                    .. attribute:: auto_laser_shut
                    
                    	Auto Laser Shut
                    	**type**\:   :py:class:`AutoLaserShut <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AutoLaserShut>`
                    
                    .. attribute:: auto_power_red
                    
                    	Auto Power Red
                    	**type**\:   :py:class:`AutoPowerRed <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AutoPowerRed>`
                    
                    .. attribute:: low_rx_power
                    
                    	Low Rx Power in uints of 0.1 dBm
                    	**type**\:   :py:class:`LowRxPower <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.LowRxPower>`
                    
                    .. attribute:: low_tx_power
                    
                    	Low Tx Power in uints of 0.1 dBm
                    	**type**\:   :py:class:`LowTxPower <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.LowTxPower>`
                    
                    .. attribute:: rx_loc
                    
                    	Rx LOC
                    	**type**\:   :py:class:`RxLoc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.RxLoc>`
                    
                    .. attribute:: rx_los_p
                    
                    	Rx LOS\_P
                    	**type**\:   :py:class:`RxLosP <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.RxLosP>`
                    
                    .. attribute:: switch_to_protect
                    
                    	Switch To Protect
                    	**type**\:   :py:class:`SwitchToProtect <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.SwitchToProtect>`
                    
                    

                    """

                    _prefix = 'controller-optics-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo, self).__init__()

                        self.yang_name = "ots-alarm-info"
                        self.yang_parent_name = "optics-info"

                        self.amp_gain_deg_high = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AmpGainDegHigh()
                        self.amp_gain_deg_high.parent = self
                        self._children_name_map["amp_gain_deg_high"] = "amp-gain-deg-high"
                        self._children_yang_names.add("amp-gain-deg-high")

                        self.amp_gain_deg_low = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AmpGainDegLow()
                        self.amp_gain_deg_low.parent = self
                        self._children_name_map["amp_gain_deg_low"] = "amp-gain-deg-low"
                        self._children_yang_names.add("amp-gain-deg-low")

                        self.auto_ampli_ctrl_config_mismatch = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AutoAmpliCtrlConfigMismatch()
                        self.auto_ampli_ctrl_config_mismatch.parent = self
                        self._children_name_map["auto_ampli_ctrl_config_mismatch"] = "auto-ampli-ctrl-config-mismatch"
                        self._children_yang_names.add("auto-ampli-ctrl-config-mismatch")

                        self.auto_ampli_ctrl_disabled = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AutoAmpliCtrlDisabled()
                        self.auto_ampli_ctrl_disabled.parent = self
                        self._children_name_map["auto_ampli_ctrl_disabled"] = "auto-ampli-ctrl-disabled"
                        self._children_yang_names.add("auto-ampli-ctrl-disabled")

                        self.auto_laser_shut = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AutoLaserShut()
                        self.auto_laser_shut.parent = self
                        self._children_name_map["auto_laser_shut"] = "auto-laser-shut"
                        self._children_yang_names.add("auto-laser-shut")

                        self.auto_power_red = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AutoPowerRed()
                        self.auto_power_red.parent = self
                        self._children_name_map["auto_power_red"] = "auto-power-red"
                        self._children_yang_names.add("auto-power-red")

                        self.low_rx_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.LowRxPower()
                        self.low_rx_power.parent = self
                        self._children_name_map["low_rx_power"] = "low-rx-power"
                        self._children_yang_names.add("low-rx-power")

                        self.low_tx_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.LowTxPower()
                        self.low_tx_power.parent = self
                        self._children_name_map["low_tx_power"] = "low-tx-power"
                        self._children_yang_names.add("low-tx-power")

                        self.rx_loc = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.RxLoc()
                        self.rx_loc.parent = self
                        self._children_name_map["rx_loc"] = "rx-loc"
                        self._children_yang_names.add("rx-loc")

                        self.rx_los_p = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.RxLosP()
                        self.rx_los_p.parent = self
                        self._children_name_map["rx_los_p"] = "rx-los-p"
                        self._children_yang_names.add("rx-los-p")

                        self.switch_to_protect = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.SwitchToProtect()
                        self.switch_to_protect.parent = self
                        self._children_name_map["switch_to_protect"] = "switch-to-protect"
                        self._children_yang_names.add("switch-to-protect")


                    class LowTxPower(Entity):
                        """
                        Low Tx Power in uints of 0.1 dBm
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.LowTxPower, self).__init__()

                            self.yang_name = "low-tx-power"
                            self.yang_parent_name = "ots-alarm-info"

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("counter",
                                            "is_detected") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.LowTxPower, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.LowTxPower, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.counter.is_set or
                                self.is_detected.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.counter.yfilter != YFilter.not_set or
                                self.is_detected.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "low-tx-power" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.counter.is_set or self.counter.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.counter.get_name_leafdata())
                            if (self.is_detected.is_set or self.is_detected.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_detected.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "counter" or name == "is-detected"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "counter"):
                                self.counter = value
                                self.counter.value_namespace = name_space
                                self.counter.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-detected"):
                                self.is_detected = value
                                self.is_detected.value_namespace = name_space
                                self.is_detected.value_namespace_prefix = name_space_prefix


                    class LowRxPower(Entity):
                        """
                        Low Rx Power in uints of 0.1 dBm
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.LowRxPower, self).__init__()

                            self.yang_name = "low-rx-power"
                            self.yang_parent_name = "ots-alarm-info"

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("counter",
                                            "is_detected") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.LowRxPower, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.LowRxPower, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.counter.is_set or
                                self.is_detected.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.counter.yfilter != YFilter.not_set or
                                self.is_detected.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "low-rx-power" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.counter.is_set or self.counter.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.counter.get_name_leafdata())
                            if (self.is_detected.is_set or self.is_detected.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_detected.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "counter" or name == "is-detected"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "counter"):
                                self.counter = value
                                self.counter.value_namespace = name_space
                                self.counter.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-detected"):
                                self.is_detected = value
                                self.is_detected.value_namespace = name_space
                                self.is_detected.value_namespace_prefix = name_space_prefix


                    class RxLosP(Entity):
                        """
                        Rx LOS\_P
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.RxLosP, self).__init__()

                            self.yang_name = "rx-los-p"
                            self.yang_parent_name = "ots-alarm-info"

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("counter",
                                            "is_detected") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.RxLosP, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.RxLosP, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.counter.is_set or
                                self.is_detected.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.counter.yfilter != YFilter.not_set or
                                self.is_detected.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "rx-los-p" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.counter.is_set or self.counter.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.counter.get_name_leafdata())
                            if (self.is_detected.is_set or self.is_detected.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_detected.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "counter" or name == "is-detected"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "counter"):
                                self.counter = value
                                self.counter.value_namespace = name_space
                                self.counter.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-detected"):
                                self.is_detected = value
                                self.is_detected.value_namespace = name_space
                                self.is_detected.value_namespace_prefix = name_space_prefix


                    class RxLoc(Entity):
                        """
                        Rx LOC
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.RxLoc, self).__init__()

                            self.yang_name = "rx-loc"
                            self.yang_parent_name = "ots-alarm-info"

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("counter",
                                            "is_detected") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.RxLoc, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.RxLoc, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.counter.is_set or
                                self.is_detected.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.counter.yfilter != YFilter.not_set or
                                self.is_detected.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "rx-loc" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.counter.is_set or self.counter.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.counter.get_name_leafdata())
                            if (self.is_detected.is_set or self.is_detected.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_detected.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "counter" or name == "is-detected"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "counter"):
                                self.counter = value
                                self.counter.value_namespace = name_space
                                self.counter.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-detected"):
                                self.is_detected = value
                                self.is_detected.value_namespace = name_space
                                self.is_detected.value_namespace_prefix = name_space_prefix


                    class AmpGainDegLow(Entity):
                        """
                        Ampli Gain Deg Low
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AmpGainDegLow, self).__init__()

                            self.yang_name = "amp-gain-deg-low"
                            self.yang_parent_name = "ots-alarm-info"

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("counter",
                                            "is_detected") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AmpGainDegLow, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AmpGainDegLow, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.counter.is_set or
                                self.is_detected.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.counter.yfilter != YFilter.not_set or
                                self.is_detected.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "amp-gain-deg-low" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.counter.is_set or self.counter.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.counter.get_name_leafdata())
                            if (self.is_detected.is_set or self.is_detected.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_detected.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "counter" or name == "is-detected"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "counter"):
                                self.counter = value
                                self.counter.value_namespace = name_space
                                self.counter.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-detected"):
                                self.is_detected = value
                                self.is_detected.value_namespace = name_space
                                self.is_detected.value_namespace_prefix = name_space_prefix


                    class AmpGainDegHigh(Entity):
                        """
                        Ampli Gain Deg High
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AmpGainDegHigh, self).__init__()

                            self.yang_name = "amp-gain-deg-high"
                            self.yang_parent_name = "ots-alarm-info"

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("counter",
                                            "is_detected") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AmpGainDegHigh, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AmpGainDegHigh, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.counter.is_set or
                                self.is_detected.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.counter.yfilter != YFilter.not_set or
                                self.is_detected.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "amp-gain-deg-high" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.counter.is_set or self.counter.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.counter.get_name_leafdata())
                            if (self.is_detected.is_set or self.is_detected.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_detected.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "counter" or name == "is-detected"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "counter"):
                                self.counter = value
                                self.counter.value_namespace = name_space
                                self.counter.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-detected"):
                                self.is_detected = value
                                self.is_detected.value_namespace = name_space
                                self.is_detected.value_namespace_prefix = name_space_prefix


                    class AutoLaserShut(Entity):
                        """
                        Auto Laser Shut
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AutoLaserShut, self).__init__()

                            self.yang_name = "auto-laser-shut"
                            self.yang_parent_name = "ots-alarm-info"

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("counter",
                                            "is_detected") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AutoLaserShut, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AutoLaserShut, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.counter.is_set or
                                self.is_detected.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.counter.yfilter != YFilter.not_set or
                                self.is_detected.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "auto-laser-shut" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.counter.is_set or self.counter.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.counter.get_name_leafdata())
                            if (self.is_detected.is_set or self.is_detected.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_detected.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "counter" or name == "is-detected"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "counter"):
                                self.counter = value
                                self.counter.value_namespace = name_space
                                self.counter.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-detected"):
                                self.is_detected = value
                                self.is_detected.value_namespace = name_space
                                self.is_detected.value_namespace_prefix = name_space_prefix


                    class AutoPowerRed(Entity):
                        """
                        Auto Power Red
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AutoPowerRed, self).__init__()

                            self.yang_name = "auto-power-red"
                            self.yang_parent_name = "ots-alarm-info"

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("counter",
                                            "is_detected") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AutoPowerRed, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AutoPowerRed, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.counter.is_set or
                                self.is_detected.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.counter.yfilter != YFilter.not_set or
                                self.is_detected.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "auto-power-red" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.counter.is_set or self.counter.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.counter.get_name_leafdata())
                            if (self.is_detected.is_set or self.is_detected.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_detected.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "counter" or name == "is-detected"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "counter"):
                                self.counter = value
                                self.counter.value_namespace = name_space
                                self.counter.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-detected"):
                                self.is_detected = value
                                self.is_detected.value_namespace = name_space
                                self.is_detected.value_namespace_prefix = name_space_prefix


                    class AutoAmpliCtrlDisabled(Entity):
                        """
                        Auto Ampli Ctrl Disabled
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AutoAmpliCtrlDisabled, self).__init__()

                            self.yang_name = "auto-ampli-ctrl-disabled"
                            self.yang_parent_name = "ots-alarm-info"

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("counter",
                                            "is_detected") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AutoAmpliCtrlDisabled, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AutoAmpliCtrlDisabled, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.counter.is_set or
                                self.is_detected.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.counter.yfilter != YFilter.not_set or
                                self.is_detected.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "auto-ampli-ctrl-disabled" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.counter.is_set or self.counter.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.counter.get_name_leafdata())
                            if (self.is_detected.is_set or self.is_detected.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_detected.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "counter" or name == "is-detected"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "counter"):
                                self.counter = value
                                self.counter.value_namespace = name_space
                                self.counter.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-detected"):
                                self.is_detected = value
                                self.is_detected.value_namespace = name_space
                                self.is_detected.value_namespace_prefix = name_space_prefix


                    class AutoAmpliCtrlConfigMismatch(Entity):
                        """
                        Auto Ampli Ctrl Config Mismatch
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AutoAmpliCtrlConfigMismatch, self).__init__()

                            self.yang_name = "auto-ampli-ctrl-config-mismatch"
                            self.yang_parent_name = "ots-alarm-info"

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("counter",
                                            "is_detected") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AutoAmpliCtrlConfigMismatch, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AutoAmpliCtrlConfigMismatch, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.counter.is_set or
                                self.is_detected.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.counter.yfilter != YFilter.not_set or
                                self.is_detected.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "auto-ampli-ctrl-config-mismatch" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.counter.is_set or self.counter.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.counter.get_name_leafdata())
                            if (self.is_detected.is_set or self.is_detected.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_detected.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "counter" or name == "is-detected"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "counter"):
                                self.counter = value
                                self.counter.value_namespace = name_space
                                self.counter.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-detected"):
                                self.is_detected = value
                                self.is_detected.value_namespace = name_space
                                self.is_detected.value_namespace_prefix = name_space_prefix


                    class SwitchToProtect(Entity):
                        """
                        Switch To Protect
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.SwitchToProtect, self).__init__()

                            self.yang_name = "switch-to-protect"
                            self.yang_parent_name = "ots-alarm-info"

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("counter",
                                            "is_detected") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.SwitchToProtect, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.SwitchToProtect, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.counter.is_set or
                                self.is_detected.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.counter.yfilter != YFilter.not_set or
                                self.is_detected.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "switch-to-protect" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.counter.is_set or self.counter.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.counter.get_name_leafdata())
                            if (self.is_detected.is_set or self.is_detected.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_detected.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "counter" or name == "is-detected"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "counter"):
                                self.counter = value
                                self.counter.value_namespace = name_space
                                self.counter.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-detected"):
                                self.is_detected = value
                                self.is_detected.value_namespace = name_space
                                self.is_detected.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            (self.amp_gain_deg_high is not None and self.amp_gain_deg_high.has_data()) or
                            (self.amp_gain_deg_low is not None and self.amp_gain_deg_low.has_data()) or
                            (self.auto_ampli_ctrl_config_mismatch is not None and self.auto_ampli_ctrl_config_mismatch.has_data()) or
                            (self.auto_ampli_ctrl_disabled is not None and self.auto_ampli_ctrl_disabled.has_data()) or
                            (self.auto_laser_shut is not None and self.auto_laser_shut.has_data()) or
                            (self.auto_power_red is not None and self.auto_power_red.has_data()) or
                            (self.low_rx_power is not None and self.low_rx_power.has_data()) or
                            (self.low_tx_power is not None and self.low_tx_power.has_data()) or
                            (self.rx_loc is not None and self.rx_loc.has_data()) or
                            (self.rx_los_p is not None and self.rx_los_p.has_data()) or
                            (self.switch_to_protect is not None and self.switch_to_protect.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            (self.amp_gain_deg_high is not None and self.amp_gain_deg_high.has_operation()) or
                            (self.amp_gain_deg_low is not None and self.amp_gain_deg_low.has_operation()) or
                            (self.auto_ampli_ctrl_config_mismatch is not None and self.auto_ampli_ctrl_config_mismatch.has_operation()) or
                            (self.auto_ampli_ctrl_disabled is not None and self.auto_ampli_ctrl_disabled.has_operation()) or
                            (self.auto_laser_shut is not None and self.auto_laser_shut.has_operation()) or
                            (self.auto_power_red is not None and self.auto_power_red.has_operation()) or
                            (self.low_rx_power is not None and self.low_rx_power.has_operation()) or
                            (self.low_tx_power is not None and self.low_tx_power.has_operation()) or
                            (self.rx_loc is not None and self.rx_loc.has_operation()) or
                            (self.rx_los_p is not None and self.rx_los_p.has_operation()) or
                            (self.switch_to_protect is not None and self.switch_to_protect.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "ots-alarm-info" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "amp-gain-deg-high"):
                            if (self.amp_gain_deg_high is None):
                                self.amp_gain_deg_high = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AmpGainDegHigh()
                                self.amp_gain_deg_high.parent = self
                                self._children_name_map["amp_gain_deg_high"] = "amp-gain-deg-high"
                            return self.amp_gain_deg_high

                        if (child_yang_name == "amp-gain-deg-low"):
                            if (self.amp_gain_deg_low is None):
                                self.amp_gain_deg_low = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AmpGainDegLow()
                                self.amp_gain_deg_low.parent = self
                                self._children_name_map["amp_gain_deg_low"] = "amp-gain-deg-low"
                            return self.amp_gain_deg_low

                        if (child_yang_name == "auto-ampli-ctrl-config-mismatch"):
                            if (self.auto_ampli_ctrl_config_mismatch is None):
                                self.auto_ampli_ctrl_config_mismatch = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AutoAmpliCtrlConfigMismatch()
                                self.auto_ampli_ctrl_config_mismatch.parent = self
                                self._children_name_map["auto_ampli_ctrl_config_mismatch"] = "auto-ampli-ctrl-config-mismatch"
                            return self.auto_ampli_ctrl_config_mismatch

                        if (child_yang_name == "auto-ampli-ctrl-disabled"):
                            if (self.auto_ampli_ctrl_disabled is None):
                                self.auto_ampli_ctrl_disabled = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AutoAmpliCtrlDisabled()
                                self.auto_ampli_ctrl_disabled.parent = self
                                self._children_name_map["auto_ampli_ctrl_disabled"] = "auto-ampli-ctrl-disabled"
                            return self.auto_ampli_ctrl_disabled

                        if (child_yang_name == "auto-laser-shut"):
                            if (self.auto_laser_shut is None):
                                self.auto_laser_shut = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AutoLaserShut()
                                self.auto_laser_shut.parent = self
                                self._children_name_map["auto_laser_shut"] = "auto-laser-shut"
                            return self.auto_laser_shut

                        if (child_yang_name == "auto-power-red"):
                            if (self.auto_power_red is None):
                                self.auto_power_red = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AutoPowerRed()
                                self.auto_power_red.parent = self
                                self._children_name_map["auto_power_red"] = "auto-power-red"
                            return self.auto_power_red

                        if (child_yang_name == "low-rx-power"):
                            if (self.low_rx_power is None):
                                self.low_rx_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.LowRxPower()
                                self.low_rx_power.parent = self
                                self._children_name_map["low_rx_power"] = "low-rx-power"
                            return self.low_rx_power

                        if (child_yang_name == "low-tx-power"):
                            if (self.low_tx_power is None):
                                self.low_tx_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.LowTxPower()
                                self.low_tx_power.parent = self
                                self._children_name_map["low_tx_power"] = "low-tx-power"
                            return self.low_tx_power

                        if (child_yang_name == "rx-loc"):
                            if (self.rx_loc is None):
                                self.rx_loc = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.RxLoc()
                                self.rx_loc.parent = self
                                self._children_name_map["rx_loc"] = "rx-loc"
                            return self.rx_loc

                        if (child_yang_name == "rx-los-p"):
                            if (self.rx_los_p is None):
                                self.rx_los_p = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.RxLosP()
                                self.rx_los_p.parent = self
                                self._children_name_map["rx_los_p"] = "rx-los-p"
                            return self.rx_los_p

                        if (child_yang_name == "switch-to-protect"):
                            if (self.switch_to_protect is None):
                                self.switch_to_protect = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.SwitchToProtect()
                                self.switch_to_protect.parent = self
                                self._children_name_map["switch_to_protect"] = "switch-to-protect"
                            return self.switch_to_protect

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "amp-gain-deg-high" or name == "amp-gain-deg-low" or name == "auto-ampli-ctrl-config-mismatch" or name == "auto-ampli-ctrl-disabled" or name == "auto-laser-shut" or name == "auto-power-red" or name == "low-rx-power" or name == "low-tx-power" or name == "rx-loc" or name == "rx-los-p" or name == "switch-to-protect"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class TransceiverInfo(Entity):
                    """
                    Transceiver Vendor Details
                    
                    .. attribute:: adapter_vendor_info
                    
                    	Adapter Vendor Information
                    	**type**\:  str
                    
                    .. attribute:: connector_type
                    
                    	Connector type
                    	**type**\:   :py:class:`FiberConnector <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.FiberConnector>`
                    
                    .. attribute:: date
                    
                    	Date in Transceiver
                    	**type**\:  str
                    
                    .. attribute:: ethernet_compliance_code
                    
                    	Ethernet Compliance Code
                    	**type**\:   :py:class:`EthernetPmd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.EthernetPmd>`
                    
                    .. attribute:: internal_temperature
                    
                    	Internal Temperature in C
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: optics_serial_no
                    
                    	Transceiver serial number
                    	**type**\:  str
                    
                    .. attribute:: optics_vendor_part
                    
                    	Transceiver vendors part number
                    	**type**\:  str
                    
                    .. attribute:: optics_vendor_rev
                    
                    	Transceiver vendors revision number
                    	**type**\:  str
                    
                    .. attribute:: otn_application_code
                    
                    	Otn Application Code
                    	**type**\:   :py:class:`OtnApplicationCode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OtnApplicationCode>`
                    
                    .. attribute:: sonet_application_code
                    
                    	Sonet Application Code
                    	**type**\:   :py:class:`SonetApplicationCode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.SonetApplicationCode>`
                    
                    .. attribute:: vendor_info
                    
                    	Vendor Information
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'controller-optics-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.TransceiverInfo, self).__init__()

                        self.yang_name = "transceiver-info"
                        self.yang_parent_name = "optics-info"

                        self.adapter_vendor_info = YLeaf(YType.str, "adapter-vendor-info")

                        self.connector_type = YLeaf(YType.enumeration, "connector-type")

                        self.date = YLeaf(YType.str, "date")

                        self.ethernet_compliance_code = YLeaf(YType.enumeration, "ethernet-compliance-code")

                        self.internal_temperature = YLeaf(YType.int32, "internal-temperature")

                        self.optics_serial_no = YLeaf(YType.str, "optics-serial-no")

                        self.optics_vendor_part = YLeaf(YType.str, "optics-vendor-part")

                        self.optics_vendor_rev = YLeaf(YType.str, "optics-vendor-rev")

                        self.otn_application_code = YLeaf(YType.enumeration, "otn-application-code")

                        self.sonet_application_code = YLeaf(YType.enumeration, "sonet-application-code")

                        self.vendor_info = YLeaf(YType.str, "vendor-info")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("adapter_vendor_info",
                                        "connector_type",
                                        "date",
                                        "ethernet_compliance_code",
                                        "internal_temperature",
                                        "optics_serial_no",
                                        "optics_vendor_part",
                                        "optics_vendor_rev",
                                        "otn_application_code",
                                        "sonet_application_code",
                                        "vendor_info") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.TransceiverInfo, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.TransceiverInfo, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.adapter_vendor_info.is_set or
                            self.connector_type.is_set or
                            self.date.is_set or
                            self.ethernet_compliance_code.is_set or
                            self.internal_temperature.is_set or
                            self.optics_serial_no.is_set or
                            self.optics_vendor_part.is_set or
                            self.optics_vendor_rev.is_set or
                            self.otn_application_code.is_set or
                            self.sonet_application_code.is_set or
                            self.vendor_info.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.adapter_vendor_info.yfilter != YFilter.not_set or
                            self.connector_type.yfilter != YFilter.not_set or
                            self.date.yfilter != YFilter.not_set or
                            self.ethernet_compliance_code.yfilter != YFilter.not_set or
                            self.internal_temperature.yfilter != YFilter.not_set or
                            self.optics_serial_no.yfilter != YFilter.not_set or
                            self.optics_vendor_part.yfilter != YFilter.not_set or
                            self.optics_vendor_rev.yfilter != YFilter.not_set or
                            self.otn_application_code.yfilter != YFilter.not_set or
                            self.sonet_application_code.yfilter != YFilter.not_set or
                            self.vendor_info.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "transceiver-info" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.adapter_vendor_info.is_set or self.adapter_vendor_info.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.adapter_vendor_info.get_name_leafdata())
                        if (self.connector_type.is_set or self.connector_type.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.connector_type.get_name_leafdata())
                        if (self.date.is_set or self.date.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.date.get_name_leafdata())
                        if (self.ethernet_compliance_code.is_set or self.ethernet_compliance_code.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ethernet_compliance_code.get_name_leafdata())
                        if (self.internal_temperature.is_set or self.internal_temperature.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.internal_temperature.get_name_leafdata())
                        if (self.optics_serial_no.is_set or self.optics_serial_no.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.optics_serial_no.get_name_leafdata())
                        if (self.optics_vendor_part.is_set or self.optics_vendor_part.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.optics_vendor_part.get_name_leafdata())
                        if (self.optics_vendor_rev.is_set or self.optics_vendor_rev.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.optics_vendor_rev.get_name_leafdata())
                        if (self.otn_application_code.is_set or self.otn_application_code.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.otn_application_code.get_name_leafdata())
                        if (self.sonet_application_code.is_set or self.sonet_application_code.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.sonet_application_code.get_name_leafdata())
                        if (self.vendor_info.is_set or self.vendor_info.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.vendor_info.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "adapter-vendor-info" or name == "connector-type" or name == "date" or name == "ethernet-compliance-code" or name == "internal-temperature" or name == "optics-serial-no" or name == "optics-vendor-part" or name == "optics-vendor-rev" or name == "otn-application-code" or name == "sonet-application-code" or name == "vendor-info"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "adapter-vendor-info"):
                            self.adapter_vendor_info = value
                            self.adapter_vendor_info.value_namespace = name_space
                            self.adapter_vendor_info.value_namespace_prefix = name_space_prefix
                        if(value_path == "connector-type"):
                            self.connector_type = value
                            self.connector_type.value_namespace = name_space
                            self.connector_type.value_namespace_prefix = name_space_prefix
                        if(value_path == "date"):
                            self.date = value
                            self.date.value_namespace = name_space
                            self.date.value_namespace_prefix = name_space_prefix
                        if(value_path == "ethernet-compliance-code"):
                            self.ethernet_compliance_code = value
                            self.ethernet_compliance_code.value_namespace = name_space
                            self.ethernet_compliance_code.value_namespace_prefix = name_space_prefix
                        if(value_path == "internal-temperature"):
                            self.internal_temperature = value
                            self.internal_temperature.value_namespace = name_space
                            self.internal_temperature.value_namespace_prefix = name_space_prefix
                        if(value_path == "optics-serial-no"):
                            self.optics_serial_no = value
                            self.optics_serial_no.value_namespace = name_space
                            self.optics_serial_no.value_namespace_prefix = name_space_prefix
                        if(value_path == "optics-vendor-part"):
                            self.optics_vendor_part = value
                            self.optics_vendor_part.value_namespace = name_space
                            self.optics_vendor_part.value_namespace_prefix = name_space_prefix
                        if(value_path == "optics-vendor-rev"):
                            self.optics_vendor_rev = value
                            self.optics_vendor_rev.value_namespace = name_space
                            self.optics_vendor_rev.value_namespace_prefix = name_space_prefix
                        if(value_path == "otn-application-code"):
                            self.otn_application_code = value
                            self.otn_application_code.value_namespace = name_space
                            self.otn_application_code.value_namespace_prefix = name_space_prefix
                        if(value_path == "sonet-application-code"):
                            self.sonet_application_code = value
                            self.sonet_application_code.value_namespace = name_space
                            self.sonet_application_code.value_namespace_prefix = name_space_prefix
                        if(value_path == "vendor-info"):
                            self.vendor_info = value
                            self.vendor_info.value_namespace = name_space
                            self.vendor_info.value_namespace_prefix = name_space_prefix


                class ExtParamVal(Entity):
                    """
                    Extended optics parameters
                    
                    .. attribute:: isi_correction_lane1
                    
                    	Inter symbol Interference correction on Lane 1
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: isi_correction_lane2
                    
                    	Inter symbol Interference correction on Lane 2
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: laser_diff_frequency_lane1
                    
                    	Difference between target and actual center frequency on Lane 1
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: laser_diff_frequency_lane2
                    
                    	Difference between target and actual center frequency on Lane 2
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: laser_diff_temperature_lane1
                    
                    	Difference between target and actual temperature on Lane 1
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: laser_diff_temperature_lane2
                    
                    	Difference between target and actual temperature on Lane 2
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: pam_rate_lane1
                    
                    	PAM Histogram parameter on Lane 1
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: pam_rate_lane2
                    
                    	PAM Histogram parameter on Lane 2
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: pre_fec_ber
                    
                    	Pre FEC BER since last counter reset
                    	**type**\:  int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: pre_fec_ber_accumulated
                    
                    	Pre FEC BER value prior accumulation period, line ingress
                    	**type**\:  int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: pre_fec_ber_instantaneous
                    
                    	Pre FEC BER value instantaneous line ingress
                    	**type**\:  int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: pre_fec_ber_latched_max
                    
                    	Latched maximum Pre FEC BER value since last read, line ingress
                    	**type**\:  int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: pre_fec_ber_latched_min
                    
                    	Latched minimum Pre FEC BER value since last read, line ingress
                    	**type**\:  int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: snr_lane1
                    
                    	Signal to Noise Ratio on Lane 1
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: snr_lane2
                    
                    	Signal to Noise Ratio on Lane 2
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: tec_current_lane1
                    
                    	Current flowing to the TEC of a cooled laser on Lane 1
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: tec_current_lane2
                    
                    	Current flowing to the TEC of a cooled laser on Lane 2
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: uncorrected_ber
                    
                    	Uncorrected BER since last counter reset
                    	**type**\:  int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: uncorrected_ber_accumulated
                    
                    	Uncorrected BER value prior accumulation period, line ingress
                    	**type**\:  int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: uncorrected_ber_instantaneous
                    
                    	Uncorrected BER value instantaneous line line ingress
                    	**type**\:  int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: uncorrected_ber_latched_max
                    
                    	Latched maximum Uncorrected BER value since last read, line ingress
                    	**type**\:  int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: uncorrected_ber_latched_min
                    
                    	Latched minimum Uncorrected BER value since last read, line ingress
                    	**type**\:  int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    

                    """

                    _prefix = 'controller-optics-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtParamVal, self).__init__()

                        self.yang_name = "ext-param-val"
                        self.yang_parent_name = "optics-info"

                        self.isi_correction_lane1 = YLeaf(YType.int32, "isi-correction-lane1")

                        self.isi_correction_lane2 = YLeaf(YType.int32, "isi-correction-lane2")

                        self.laser_diff_frequency_lane1 = YLeaf(YType.int32, "laser-diff-frequency-lane1")

                        self.laser_diff_frequency_lane2 = YLeaf(YType.int32, "laser-diff-frequency-lane2")

                        self.laser_diff_temperature_lane1 = YLeaf(YType.int32, "laser-diff-temperature-lane1")

                        self.laser_diff_temperature_lane2 = YLeaf(YType.int32, "laser-diff-temperature-lane2")

                        self.pam_rate_lane1 = YLeaf(YType.int32, "pam-rate-lane1")

                        self.pam_rate_lane2 = YLeaf(YType.int32, "pam-rate-lane2")

                        self.pre_fec_ber = YLeaf(YType.int64, "pre-fec-ber")

                        self.pre_fec_ber_accumulated = YLeaf(YType.int64, "pre-fec-ber-accumulated")

                        self.pre_fec_ber_instantaneous = YLeaf(YType.int64, "pre-fec-ber-instantaneous")

                        self.pre_fec_ber_latched_max = YLeaf(YType.int64, "pre-fec-ber-latched-max")

                        self.pre_fec_ber_latched_min = YLeaf(YType.int64, "pre-fec-ber-latched-min")

                        self.snr_lane1 = YLeaf(YType.int32, "snr-lane1")

                        self.snr_lane2 = YLeaf(YType.int32, "snr-lane2")

                        self.tec_current_lane1 = YLeaf(YType.int32, "tec-current-lane1")

                        self.tec_current_lane2 = YLeaf(YType.int32, "tec-current-lane2")

                        self.uncorrected_ber = YLeaf(YType.int64, "uncorrected-ber")

                        self.uncorrected_ber_accumulated = YLeaf(YType.int64, "uncorrected-ber-accumulated")

                        self.uncorrected_ber_instantaneous = YLeaf(YType.int64, "uncorrected-ber-instantaneous")

                        self.uncorrected_ber_latched_max = YLeaf(YType.int64, "uncorrected-ber-latched-max")

                        self.uncorrected_ber_latched_min = YLeaf(YType.int64, "uncorrected-ber-latched-min")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("isi_correction_lane1",
                                        "isi_correction_lane2",
                                        "laser_diff_frequency_lane1",
                                        "laser_diff_frequency_lane2",
                                        "laser_diff_temperature_lane1",
                                        "laser_diff_temperature_lane2",
                                        "pam_rate_lane1",
                                        "pam_rate_lane2",
                                        "pre_fec_ber",
                                        "pre_fec_ber_accumulated",
                                        "pre_fec_ber_instantaneous",
                                        "pre_fec_ber_latched_max",
                                        "pre_fec_ber_latched_min",
                                        "snr_lane1",
                                        "snr_lane2",
                                        "tec_current_lane1",
                                        "tec_current_lane2",
                                        "uncorrected_ber",
                                        "uncorrected_ber_accumulated",
                                        "uncorrected_ber_instantaneous",
                                        "uncorrected_ber_latched_max",
                                        "uncorrected_ber_latched_min") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtParamVal, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtParamVal, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.isi_correction_lane1.is_set or
                            self.isi_correction_lane2.is_set or
                            self.laser_diff_frequency_lane1.is_set or
                            self.laser_diff_frequency_lane2.is_set or
                            self.laser_diff_temperature_lane1.is_set or
                            self.laser_diff_temperature_lane2.is_set or
                            self.pam_rate_lane1.is_set or
                            self.pam_rate_lane2.is_set or
                            self.pre_fec_ber.is_set or
                            self.pre_fec_ber_accumulated.is_set or
                            self.pre_fec_ber_instantaneous.is_set or
                            self.pre_fec_ber_latched_max.is_set or
                            self.pre_fec_ber_latched_min.is_set or
                            self.snr_lane1.is_set or
                            self.snr_lane2.is_set or
                            self.tec_current_lane1.is_set or
                            self.tec_current_lane2.is_set or
                            self.uncorrected_ber.is_set or
                            self.uncorrected_ber_accumulated.is_set or
                            self.uncorrected_ber_instantaneous.is_set or
                            self.uncorrected_ber_latched_max.is_set or
                            self.uncorrected_ber_latched_min.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.isi_correction_lane1.yfilter != YFilter.not_set or
                            self.isi_correction_lane2.yfilter != YFilter.not_set or
                            self.laser_diff_frequency_lane1.yfilter != YFilter.not_set or
                            self.laser_diff_frequency_lane2.yfilter != YFilter.not_set or
                            self.laser_diff_temperature_lane1.yfilter != YFilter.not_set or
                            self.laser_diff_temperature_lane2.yfilter != YFilter.not_set or
                            self.pam_rate_lane1.yfilter != YFilter.not_set or
                            self.pam_rate_lane2.yfilter != YFilter.not_set or
                            self.pre_fec_ber.yfilter != YFilter.not_set or
                            self.pre_fec_ber_accumulated.yfilter != YFilter.not_set or
                            self.pre_fec_ber_instantaneous.yfilter != YFilter.not_set or
                            self.pre_fec_ber_latched_max.yfilter != YFilter.not_set or
                            self.pre_fec_ber_latched_min.yfilter != YFilter.not_set or
                            self.snr_lane1.yfilter != YFilter.not_set or
                            self.snr_lane2.yfilter != YFilter.not_set or
                            self.tec_current_lane1.yfilter != YFilter.not_set or
                            self.tec_current_lane2.yfilter != YFilter.not_set or
                            self.uncorrected_ber.yfilter != YFilter.not_set or
                            self.uncorrected_ber_accumulated.yfilter != YFilter.not_set or
                            self.uncorrected_ber_instantaneous.yfilter != YFilter.not_set or
                            self.uncorrected_ber_latched_max.yfilter != YFilter.not_set or
                            self.uncorrected_ber_latched_min.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "ext-param-val" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.isi_correction_lane1.is_set or self.isi_correction_lane1.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.isi_correction_lane1.get_name_leafdata())
                        if (self.isi_correction_lane2.is_set or self.isi_correction_lane2.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.isi_correction_lane2.get_name_leafdata())
                        if (self.laser_diff_frequency_lane1.is_set or self.laser_diff_frequency_lane1.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.laser_diff_frequency_lane1.get_name_leafdata())
                        if (self.laser_diff_frequency_lane2.is_set or self.laser_diff_frequency_lane2.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.laser_diff_frequency_lane2.get_name_leafdata())
                        if (self.laser_diff_temperature_lane1.is_set or self.laser_diff_temperature_lane1.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.laser_diff_temperature_lane1.get_name_leafdata())
                        if (self.laser_diff_temperature_lane2.is_set or self.laser_diff_temperature_lane2.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.laser_diff_temperature_lane2.get_name_leafdata())
                        if (self.pam_rate_lane1.is_set or self.pam_rate_lane1.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.pam_rate_lane1.get_name_leafdata())
                        if (self.pam_rate_lane2.is_set or self.pam_rate_lane2.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.pam_rate_lane2.get_name_leafdata())
                        if (self.pre_fec_ber.is_set or self.pre_fec_ber.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.pre_fec_ber.get_name_leafdata())
                        if (self.pre_fec_ber_accumulated.is_set or self.pre_fec_ber_accumulated.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.pre_fec_ber_accumulated.get_name_leafdata())
                        if (self.pre_fec_ber_instantaneous.is_set or self.pre_fec_ber_instantaneous.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.pre_fec_ber_instantaneous.get_name_leafdata())
                        if (self.pre_fec_ber_latched_max.is_set or self.pre_fec_ber_latched_max.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.pre_fec_ber_latched_max.get_name_leafdata())
                        if (self.pre_fec_ber_latched_min.is_set or self.pre_fec_ber_latched_min.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.pre_fec_ber_latched_min.get_name_leafdata())
                        if (self.snr_lane1.is_set or self.snr_lane1.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.snr_lane1.get_name_leafdata())
                        if (self.snr_lane2.is_set or self.snr_lane2.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.snr_lane2.get_name_leafdata())
                        if (self.tec_current_lane1.is_set or self.tec_current_lane1.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.tec_current_lane1.get_name_leafdata())
                        if (self.tec_current_lane2.is_set or self.tec_current_lane2.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.tec_current_lane2.get_name_leafdata())
                        if (self.uncorrected_ber.is_set or self.uncorrected_ber.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.uncorrected_ber.get_name_leafdata())
                        if (self.uncorrected_ber_accumulated.is_set or self.uncorrected_ber_accumulated.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.uncorrected_ber_accumulated.get_name_leafdata())
                        if (self.uncorrected_ber_instantaneous.is_set or self.uncorrected_ber_instantaneous.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.uncorrected_ber_instantaneous.get_name_leafdata())
                        if (self.uncorrected_ber_latched_max.is_set or self.uncorrected_ber_latched_max.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.uncorrected_ber_latched_max.get_name_leafdata())
                        if (self.uncorrected_ber_latched_min.is_set or self.uncorrected_ber_latched_min.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.uncorrected_ber_latched_min.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "isi-correction-lane1" or name == "isi-correction-lane2" or name == "laser-diff-frequency-lane1" or name == "laser-diff-frequency-lane2" or name == "laser-diff-temperature-lane1" or name == "laser-diff-temperature-lane2" or name == "pam-rate-lane1" or name == "pam-rate-lane2" or name == "pre-fec-ber" or name == "pre-fec-ber-accumulated" or name == "pre-fec-ber-instantaneous" or name == "pre-fec-ber-latched-max" or name == "pre-fec-ber-latched-min" or name == "snr-lane1" or name == "snr-lane2" or name == "tec-current-lane1" or name == "tec-current-lane2" or name == "uncorrected-ber" or name == "uncorrected-ber-accumulated" or name == "uncorrected-ber-instantaneous" or name == "uncorrected-ber-latched-max" or name == "uncorrected-ber-latched-min"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "isi-correction-lane1"):
                            self.isi_correction_lane1 = value
                            self.isi_correction_lane1.value_namespace = name_space
                            self.isi_correction_lane1.value_namespace_prefix = name_space_prefix
                        if(value_path == "isi-correction-lane2"):
                            self.isi_correction_lane2 = value
                            self.isi_correction_lane2.value_namespace = name_space
                            self.isi_correction_lane2.value_namespace_prefix = name_space_prefix
                        if(value_path == "laser-diff-frequency-lane1"):
                            self.laser_diff_frequency_lane1 = value
                            self.laser_diff_frequency_lane1.value_namespace = name_space
                            self.laser_diff_frequency_lane1.value_namespace_prefix = name_space_prefix
                        if(value_path == "laser-diff-frequency-lane2"):
                            self.laser_diff_frequency_lane2 = value
                            self.laser_diff_frequency_lane2.value_namespace = name_space
                            self.laser_diff_frequency_lane2.value_namespace_prefix = name_space_prefix
                        if(value_path == "laser-diff-temperature-lane1"):
                            self.laser_diff_temperature_lane1 = value
                            self.laser_diff_temperature_lane1.value_namespace = name_space
                            self.laser_diff_temperature_lane1.value_namespace_prefix = name_space_prefix
                        if(value_path == "laser-diff-temperature-lane2"):
                            self.laser_diff_temperature_lane2 = value
                            self.laser_diff_temperature_lane2.value_namespace = name_space
                            self.laser_diff_temperature_lane2.value_namespace_prefix = name_space_prefix
                        if(value_path == "pam-rate-lane1"):
                            self.pam_rate_lane1 = value
                            self.pam_rate_lane1.value_namespace = name_space
                            self.pam_rate_lane1.value_namespace_prefix = name_space_prefix
                        if(value_path == "pam-rate-lane2"):
                            self.pam_rate_lane2 = value
                            self.pam_rate_lane2.value_namespace = name_space
                            self.pam_rate_lane2.value_namespace_prefix = name_space_prefix
                        if(value_path == "pre-fec-ber"):
                            self.pre_fec_ber = value
                            self.pre_fec_ber.value_namespace = name_space
                            self.pre_fec_ber.value_namespace_prefix = name_space_prefix
                        if(value_path == "pre-fec-ber-accumulated"):
                            self.pre_fec_ber_accumulated = value
                            self.pre_fec_ber_accumulated.value_namespace = name_space
                            self.pre_fec_ber_accumulated.value_namespace_prefix = name_space_prefix
                        if(value_path == "pre-fec-ber-instantaneous"):
                            self.pre_fec_ber_instantaneous = value
                            self.pre_fec_ber_instantaneous.value_namespace = name_space
                            self.pre_fec_ber_instantaneous.value_namespace_prefix = name_space_prefix
                        if(value_path == "pre-fec-ber-latched-max"):
                            self.pre_fec_ber_latched_max = value
                            self.pre_fec_ber_latched_max.value_namespace = name_space
                            self.pre_fec_ber_latched_max.value_namespace_prefix = name_space_prefix
                        if(value_path == "pre-fec-ber-latched-min"):
                            self.pre_fec_ber_latched_min = value
                            self.pre_fec_ber_latched_min.value_namespace = name_space
                            self.pre_fec_ber_latched_min.value_namespace_prefix = name_space_prefix
                        if(value_path == "snr-lane1"):
                            self.snr_lane1 = value
                            self.snr_lane1.value_namespace = name_space
                            self.snr_lane1.value_namespace_prefix = name_space_prefix
                        if(value_path == "snr-lane2"):
                            self.snr_lane2 = value
                            self.snr_lane2.value_namespace = name_space
                            self.snr_lane2.value_namespace_prefix = name_space_prefix
                        if(value_path == "tec-current-lane1"):
                            self.tec_current_lane1 = value
                            self.tec_current_lane1.value_namespace = name_space
                            self.tec_current_lane1.value_namespace_prefix = name_space_prefix
                        if(value_path == "tec-current-lane2"):
                            self.tec_current_lane2 = value
                            self.tec_current_lane2.value_namespace = name_space
                            self.tec_current_lane2.value_namespace_prefix = name_space_prefix
                        if(value_path == "uncorrected-ber"):
                            self.uncorrected_ber = value
                            self.uncorrected_ber.value_namespace = name_space
                            self.uncorrected_ber.value_namespace_prefix = name_space_prefix
                        if(value_path == "uncorrected-ber-accumulated"):
                            self.uncorrected_ber_accumulated = value
                            self.uncorrected_ber_accumulated.value_namespace = name_space
                            self.uncorrected_ber_accumulated.value_namespace_prefix = name_space_prefix
                        if(value_path == "uncorrected-ber-instantaneous"):
                            self.uncorrected_ber_instantaneous = value
                            self.uncorrected_ber_instantaneous.value_namespace = name_space
                            self.uncorrected_ber_instantaneous.value_namespace_prefix = name_space_prefix
                        if(value_path == "uncorrected-ber-latched-max"):
                            self.uncorrected_ber_latched_max = value
                            self.uncorrected_ber_latched_max.value_namespace = name_space
                            self.uncorrected_ber_latched_max.value_namespace_prefix = name_space_prefix
                        if(value_path == "uncorrected-ber-latched-min"):
                            self.uncorrected_ber_latched_min = value
                            self.uncorrected_ber_latched_min.value_namespace = name_space
                            self.uncorrected_ber_latched_min.value_namespace_prefix = name_space_prefix


                class ExtParamThresholdVal(Entity):
                    """
                    Extended optics parameters threshold values
                    
                    .. attribute:: isi_correction_alarm_high_threshold
                    
                    	High threshold alarm for ISI Correction
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: isi_correction_alarm_low_threshold
                    
                    	Low threshold alarm for ISI Correction
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: isi_correction_warn_high_threshold
                    
                    	High threshold warning for ISI Correction
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: isi_correction_warn_low_threshold
                    
                    	Low threshold warning for ISI Correction
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: laser_diff_frequency_alarm_high_threshold
                    
                    	High Threshold Alarm for Differential Laser Frequency
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: laser_diff_frequency_alarm_low_threshold
                    
                    	Low Threshold Alarm for Differential Laser Frequency
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: laser_diff_frequency_warn_high_threshold
                    
                    	High Threshold Warning for Differential Laser Frequency
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: laser_diff_frequency_warn_low_threshold
                    
                    	Low Threshold Warning for Differential Laser Frequency
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: laser_diff_temperature_alarm_high_threshold
                    
                    	High Threshold Alarm for Differential Laser Temperature
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: laser_diff_temperature_alarm_low_threshold
                    
                    	Low Threshold Alarm for Differential Laser Temperature
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: laser_diff_temperature_warn_high_threshold
                    
                    	High Threshold Warning for Differential Laser Temperature
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: laser_diff_temperature_warn_low_threshold
                    
                    	Low Threshold Warning for Differential Laser Temperature
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: pam_rate_alarm_high_threshold
                    
                    	High threshold alarm for PAM Rate
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: pam_rate_alarm_low_threshold
                    
                    	Low threshold alarm for PAM Rate
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: pam_rate_warn_high_threshold
                    
                    	High threshold warning for PAM Rate
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: pam_rate_warn_low_threshold
                    
                    	Low threshold warning for PAM Rate
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: pre_fec_ber_accumulated_alarm_high_threshold
                    
                    	High threshold alarm for Accumulated Pre FEC BER
                    	**type**\:  int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: pre_fec_ber_accumulated_alarm_low_threshold
                    
                    	Low threshold alarm for Accumulated Pre FEC BER
                    	**type**\:  int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: pre_fec_ber_accumulated_warn_high_threshold
                    
                    	High threshold warning for Accumulated Pre FEC BER
                    	**type**\:  int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: pre_fec_ber_accumulated_warn_low_threshold
                    
                    	Low threshold warning for Accumulated Pre FEC BER
                    	**type**\:  int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: pre_fec_ber_alarm_high_threshold
                    
                    	High threshold alarm for Pre FEC BER
                    	**type**\:  int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: pre_fec_ber_alarm_low_threshold
                    
                    	Low threshold alarm for Pre FEC BER
                    	**type**\:  int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: pre_fec_ber_instantaneous_alarm_high_threshold
                    
                    	High threshold alarm for Instantaneous Pre FEC BER
                    	**type**\:  int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: pre_fec_ber_instantaneous_alarm_low_threshold
                    
                    	Low threshold alarm for Instantaneous Pre FEC BER
                    	**type**\:  int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: pre_fec_ber_instantaneous_warn_high_threshold
                    
                    	High threshold warning for Instantaneous Pre FEC BER
                    	**type**\:  int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: pre_fec_ber_instantaneous_warn_low_threshold
                    
                    	Low threshold warning for Instantaneous Pre FEC BER
                    	**type**\:  int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: pre_fec_ber_latched_max_alarm_high_threshold
                    
                    	High threshold alarm for Latched Max Pre FEC BER
                    	**type**\:  int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: pre_fec_ber_latched_max_alarm_low_threshold
                    
                    	Low threshold alarm for Latched Max Pre FEC BER
                    	**type**\:  int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: pre_fec_ber_latched_max_warn_high_threshold
                    
                    	High threshold warning for Latched Max Pre FEC BER
                    	**type**\:  int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: pre_fec_ber_latched_max_warn_low_threshold
                    
                    	Low threshold warning for Latched Max Pre FEC BER
                    	**type**\:  int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: pre_fec_ber_latched_min_alarm_high_threshold
                    
                    	High threshold alarm for Latched Min Pre FEC BER
                    	**type**\:  int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: pre_fec_ber_latched_min_alarm_low_threshold
                    
                    	Low threshold alarm for Latched Min Pre FEC BER
                    	**type**\:  int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: pre_fec_ber_latched_min_warn_high_threshold
                    
                    	High threshold warning for Latched Min Pre FEC BER
                    	**type**\:  int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: pre_fec_ber_latched_min_warn_low_threshold
                    
                    	Low threshold warning for Latched Min Pre FEC BER
                    	**type**\:  int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: pre_fec_ber_warn_high_threshold
                    
                    	High threshold warning for Pre FEC BER
                    	**type**\:  int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: pre_fec_ber_warn_low_threshold
                    
                    	Low threshold warning for Pre FEC BER
                    	**type**\:  int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: snr_alarm_high_threshold
                    
                    	High threshold alarm for SNR
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: snr_alarm_low_threshold
                    
                    	Low threshold alarm for SNR
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: snr_warn_high_threshold
                    
                    	High threshold warning for SNR
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: snr_warn_low_threshold
                    
                    	Low threshold warning for SNR
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: tec_current_alarm_high_threshold
                    
                    	High threshold alarm for TEC Current
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: tec_current_alarm_low_threshold
                    
                    	Low threshold alarm for TEC Current
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: tec_current_warn_high_threshold
                    
                    	High threshold warning for TEC Current
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: tec_current_warn_low_threshold
                    
                    	Low threshold warning for TEC Current
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: uncorrected_ber_accumulated_alarm_high_threshold
                    
                    	High threshold alarm for Accumulated Uncorrected BER
                    	**type**\:  int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: uncorrected_ber_accumulated_alarm_low_threshold
                    
                    	Low threshold alarm for Accumulated Uncorrected BER
                    	**type**\:  int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: uncorrected_ber_accumulated_warn_high_threshold
                    
                    	High threshold warning for Accumulated Uncorrected BER
                    	**type**\:  int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: uncorrected_ber_accumulated_warn_low_threshold
                    
                    	Low threshold warning for Accumulated Uncorrected BER
                    	**type**\:  int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: uncorrected_ber_alarm_high_threshold
                    
                    	High threshold alarm for Uncorrected BER
                    	**type**\:  int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: uncorrected_ber_alarm_low_threshold
                    
                    	Low threshold alarm for Uncorrected BER
                    	**type**\:  int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: uncorrected_ber_instantaneous_alarm_high_threshold
                    
                    	High threshold alarm for Instantaneous Uncorrected BER
                    	**type**\:  int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: uncorrected_ber_instantaneous_alarm_low_threshold
                    
                    	Low threshold alarm for Instantaneous Uncorrected BER
                    	**type**\:  int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: uncorrected_ber_instantaneous_warn_high_threshold
                    
                    	High threshold warning for Instantaneous Uncorrected BER
                    	**type**\:  int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: uncorrected_ber_instantaneous_warn_low_threshold
                    
                    	Low threshold warning for Instantaneous Uncorrected BER
                    	**type**\:  int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: uncorrected_ber_latched_max_alarm_high_threshold
                    
                    	High threshold alarm for Latched\_Max Uncorrected BER
                    	**type**\:  int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: uncorrected_ber_latched_max_alarm_low_threshold
                    
                    	Low threshold alarm for Latched\_Max Uncorrected BER
                    	**type**\:  int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: uncorrected_ber_latched_max_warn_high_threshold
                    
                    	High threshold warning Latched\_Max for Uncorrected BER
                    	**type**\:  int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: uncorrected_ber_latched_max_warn_low_threshold
                    
                    	Low threshold warning Latched\_Max for Uncorrected BER
                    	**type**\:  int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: uncorrected_ber_latched_min_alarm_high_threshold
                    
                    	High threshold alarm for  Latched Min Uncorrected BER
                    	**type**\:  int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: uncorrected_ber_latched_min_alarm_low_threshold
                    
                    	Low threshold alarm for  Latched Min Uncorrected BER
                    	**type**\:  int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: uncorrected_ber_latched_min_warn_high_threshold
                    
                    	High threshold warning for  Latched Min Uncorrected BER
                    	**type**\:  int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: uncorrected_ber_latched_min_warn_low_threshold
                    
                    	Low threshold alarm for Latched Min Uncorrected BER
                    	**type**\:  int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: uncorrected_ber_warn_high_threshold
                    
                    	High threshold warning for Uncorrected BER
                    	**type**\:  int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: uncorrected_ber_warn_low_threshold
                    
                    	Low threshold warning for Uncorrected BER
                    	**type**\:  int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    

                    """

                    _prefix = 'controller-optics-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtParamThresholdVal, self).__init__()

                        self.yang_name = "ext-param-threshold-val"
                        self.yang_parent_name = "optics-info"

                        self.isi_correction_alarm_high_threshold = YLeaf(YType.int32, "isi-correction-alarm-high-threshold")

                        self.isi_correction_alarm_low_threshold = YLeaf(YType.int32, "isi-correction-alarm-low-threshold")

                        self.isi_correction_warn_high_threshold = YLeaf(YType.int32, "isi-correction-warn-high-threshold")

                        self.isi_correction_warn_low_threshold = YLeaf(YType.int32, "isi-correction-warn-low-threshold")

                        self.laser_diff_frequency_alarm_high_threshold = YLeaf(YType.int32, "laser-diff-frequency-alarm-high-threshold")

                        self.laser_diff_frequency_alarm_low_threshold = YLeaf(YType.int32, "laser-diff-frequency-alarm-low-threshold")

                        self.laser_diff_frequency_warn_high_threshold = YLeaf(YType.int32, "laser-diff-frequency-warn-high-threshold")

                        self.laser_diff_frequency_warn_low_threshold = YLeaf(YType.int32, "laser-diff-frequency-warn-low-threshold")

                        self.laser_diff_temperature_alarm_high_threshold = YLeaf(YType.int32, "laser-diff-temperature-alarm-high-threshold")

                        self.laser_diff_temperature_alarm_low_threshold = YLeaf(YType.int32, "laser-diff-temperature-alarm-low-threshold")

                        self.laser_diff_temperature_warn_high_threshold = YLeaf(YType.int32, "laser-diff-temperature-warn-high-threshold")

                        self.laser_diff_temperature_warn_low_threshold = YLeaf(YType.int32, "laser-diff-temperature-warn-low-threshold")

                        self.pam_rate_alarm_high_threshold = YLeaf(YType.int32, "pam-rate-alarm-high-threshold")

                        self.pam_rate_alarm_low_threshold = YLeaf(YType.int32, "pam-rate-alarm-low-threshold")

                        self.pam_rate_warn_high_threshold = YLeaf(YType.int32, "pam-rate-warn-high-threshold")

                        self.pam_rate_warn_low_threshold = YLeaf(YType.int32, "pam-rate-warn-low-threshold")

                        self.pre_fec_ber_accumulated_alarm_high_threshold = YLeaf(YType.int64, "pre-fec-ber-accumulated-alarm-high-threshold")

                        self.pre_fec_ber_accumulated_alarm_low_threshold = YLeaf(YType.int64, "pre-fec-ber-accumulated-alarm-low-threshold")

                        self.pre_fec_ber_accumulated_warn_high_threshold = YLeaf(YType.int64, "pre-fec-ber-accumulated-warn-high-threshold")

                        self.pre_fec_ber_accumulated_warn_low_threshold = YLeaf(YType.int64, "pre-fec-ber-accumulated-warn-low-threshold")

                        self.pre_fec_ber_alarm_high_threshold = YLeaf(YType.int64, "pre-fec-ber-alarm-high-threshold")

                        self.pre_fec_ber_alarm_low_threshold = YLeaf(YType.int64, "pre-fec-ber-alarm-low-threshold")

                        self.pre_fec_ber_instantaneous_alarm_high_threshold = YLeaf(YType.int64, "pre-fec-ber-instantaneous-alarm-high-threshold")

                        self.pre_fec_ber_instantaneous_alarm_low_threshold = YLeaf(YType.int64, "pre-fec-ber-instantaneous-alarm-low-threshold")

                        self.pre_fec_ber_instantaneous_warn_high_threshold = YLeaf(YType.int64, "pre-fec-ber-instantaneous-warn-high-threshold")

                        self.pre_fec_ber_instantaneous_warn_low_threshold = YLeaf(YType.int64, "pre-fec-ber-instantaneous-warn-low-threshold")

                        self.pre_fec_ber_latched_max_alarm_high_threshold = YLeaf(YType.int64, "pre-fec-ber-latched-max-alarm-high-threshold")

                        self.pre_fec_ber_latched_max_alarm_low_threshold = YLeaf(YType.int64, "pre-fec-ber-latched-max-alarm-low-threshold")

                        self.pre_fec_ber_latched_max_warn_high_threshold = YLeaf(YType.int64, "pre-fec-ber-latched-max-warn-high-threshold")

                        self.pre_fec_ber_latched_max_warn_low_threshold = YLeaf(YType.int64, "pre-fec-ber-latched-max-warn-low-threshold")

                        self.pre_fec_ber_latched_min_alarm_high_threshold = YLeaf(YType.int64, "pre-fec-ber-latched-min-alarm-high-threshold")

                        self.pre_fec_ber_latched_min_alarm_low_threshold = YLeaf(YType.int64, "pre-fec-ber-latched-min-alarm-low-threshold")

                        self.pre_fec_ber_latched_min_warn_high_threshold = YLeaf(YType.int64, "pre-fec-ber-latched-min-warn-high-threshold")

                        self.pre_fec_ber_latched_min_warn_low_threshold = YLeaf(YType.int64, "pre-fec-ber-latched-min-warn-low-threshold")

                        self.pre_fec_ber_warn_high_threshold = YLeaf(YType.int64, "pre-fec-ber-warn-high-threshold")

                        self.pre_fec_ber_warn_low_threshold = YLeaf(YType.int64, "pre-fec-ber-warn-low-threshold")

                        self.snr_alarm_high_threshold = YLeaf(YType.int32, "snr-alarm-high-threshold")

                        self.snr_alarm_low_threshold = YLeaf(YType.int32, "snr-alarm-low-threshold")

                        self.snr_warn_high_threshold = YLeaf(YType.int32, "snr-warn-high-threshold")

                        self.snr_warn_low_threshold = YLeaf(YType.int32, "snr-warn-low-threshold")

                        self.tec_current_alarm_high_threshold = YLeaf(YType.int32, "tec-current-alarm-high-threshold")

                        self.tec_current_alarm_low_threshold = YLeaf(YType.int32, "tec-current-alarm-low-threshold")

                        self.tec_current_warn_high_threshold = YLeaf(YType.int32, "tec-current-warn-high-threshold")

                        self.tec_current_warn_low_threshold = YLeaf(YType.int32, "tec-current-warn-low-threshold")

                        self.uncorrected_ber_accumulated_alarm_high_threshold = YLeaf(YType.int64, "uncorrected-ber-accumulated-alarm-high-threshold")

                        self.uncorrected_ber_accumulated_alarm_low_threshold = YLeaf(YType.int64, "uncorrected-ber-accumulated-alarm-low-threshold")

                        self.uncorrected_ber_accumulated_warn_high_threshold = YLeaf(YType.int64, "uncorrected-ber-accumulated-warn-high-threshold")

                        self.uncorrected_ber_accumulated_warn_low_threshold = YLeaf(YType.int64, "uncorrected-ber-accumulated-warn-low-threshold")

                        self.uncorrected_ber_alarm_high_threshold = YLeaf(YType.int64, "uncorrected-ber-alarm-high-threshold")

                        self.uncorrected_ber_alarm_low_threshold = YLeaf(YType.int64, "uncorrected-ber-alarm-low-threshold")

                        self.uncorrected_ber_instantaneous_alarm_high_threshold = YLeaf(YType.int64, "uncorrected-ber-instantaneous-alarm-high-threshold")

                        self.uncorrected_ber_instantaneous_alarm_low_threshold = YLeaf(YType.int64, "uncorrected-ber-instantaneous-alarm-low-threshold")

                        self.uncorrected_ber_instantaneous_warn_high_threshold = YLeaf(YType.int64, "uncorrected-ber-instantaneous-warn-high-threshold")

                        self.uncorrected_ber_instantaneous_warn_low_threshold = YLeaf(YType.int64, "uncorrected-ber-instantaneous-warn-low-threshold")

                        self.uncorrected_ber_latched_max_alarm_high_threshold = YLeaf(YType.int64, "uncorrected-ber-latched-max-alarm-high-threshold")

                        self.uncorrected_ber_latched_max_alarm_low_threshold = YLeaf(YType.int64, "uncorrected-ber-latched-max-alarm-low-threshold")

                        self.uncorrected_ber_latched_max_warn_high_threshold = YLeaf(YType.int64, "uncorrected-ber-latched-max-warn-high-threshold")

                        self.uncorrected_ber_latched_max_warn_low_threshold = YLeaf(YType.int64, "uncorrected-ber-latched-max-warn-low-threshold")

                        self.uncorrected_ber_latched_min_alarm_high_threshold = YLeaf(YType.int64, "uncorrected-ber-latched-min-alarm-high-threshold")

                        self.uncorrected_ber_latched_min_alarm_low_threshold = YLeaf(YType.int64, "uncorrected-ber-latched-min-alarm-low-threshold")

                        self.uncorrected_ber_latched_min_warn_high_threshold = YLeaf(YType.int64, "uncorrected-ber-latched-min-warn-high-threshold")

                        self.uncorrected_ber_latched_min_warn_low_threshold = YLeaf(YType.int64, "uncorrected-ber-latched-min-warn-low-threshold")

                        self.uncorrected_ber_warn_high_threshold = YLeaf(YType.int64, "uncorrected-ber-warn-high-threshold")

                        self.uncorrected_ber_warn_low_threshold = YLeaf(YType.int64, "uncorrected-ber-warn-low-threshold")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("isi_correction_alarm_high_threshold",
                                        "isi_correction_alarm_low_threshold",
                                        "isi_correction_warn_high_threshold",
                                        "isi_correction_warn_low_threshold",
                                        "laser_diff_frequency_alarm_high_threshold",
                                        "laser_diff_frequency_alarm_low_threshold",
                                        "laser_diff_frequency_warn_high_threshold",
                                        "laser_diff_frequency_warn_low_threshold",
                                        "laser_diff_temperature_alarm_high_threshold",
                                        "laser_diff_temperature_alarm_low_threshold",
                                        "laser_diff_temperature_warn_high_threshold",
                                        "laser_diff_temperature_warn_low_threshold",
                                        "pam_rate_alarm_high_threshold",
                                        "pam_rate_alarm_low_threshold",
                                        "pam_rate_warn_high_threshold",
                                        "pam_rate_warn_low_threshold",
                                        "pre_fec_ber_accumulated_alarm_high_threshold",
                                        "pre_fec_ber_accumulated_alarm_low_threshold",
                                        "pre_fec_ber_accumulated_warn_high_threshold",
                                        "pre_fec_ber_accumulated_warn_low_threshold",
                                        "pre_fec_ber_alarm_high_threshold",
                                        "pre_fec_ber_alarm_low_threshold",
                                        "pre_fec_ber_instantaneous_alarm_high_threshold",
                                        "pre_fec_ber_instantaneous_alarm_low_threshold",
                                        "pre_fec_ber_instantaneous_warn_high_threshold",
                                        "pre_fec_ber_instantaneous_warn_low_threshold",
                                        "pre_fec_ber_latched_max_alarm_high_threshold",
                                        "pre_fec_ber_latched_max_alarm_low_threshold",
                                        "pre_fec_ber_latched_max_warn_high_threshold",
                                        "pre_fec_ber_latched_max_warn_low_threshold",
                                        "pre_fec_ber_latched_min_alarm_high_threshold",
                                        "pre_fec_ber_latched_min_alarm_low_threshold",
                                        "pre_fec_ber_latched_min_warn_high_threshold",
                                        "pre_fec_ber_latched_min_warn_low_threshold",
                                        "pre_fec_ber_warn_high_threshold",
                                        "pre_fec_ber_warn_low_threshold",
                                        "snr_alarm_high_threshold",
                                        "snr_alarm_low_threshold",
                                        "snr_warn_high_threshold",
                                        "snr_warn_low_threshold",
                                        "tec_current_alarm_high_threshold",
                                        "tec_current_alarm_low_threshold",
                                        "tec_current_warn_high_threshold",
                                        "tec_current_warn_low_threshold",
                                        "uncorrected_ber_accumulated_alarm_high_threshold",
                                        "uncorrected_ber_accumulated_alarm_low_threshold",
                                        "uncorrected_ber_accumulated_warn_high_threshold",
                                        "uncorrected_ber_accumulated_warn_low_threshold",
                                        "uncorrected_ber_alarm_high_threshold",
                                        "uncorrected_ber_alarm_low_threshold",
                                        "uncorrected_ber_instantaneous_alarm_high_threshold",
                                        "uncorrected_ber_instantaneous_alarm_low_threshold",
                                        "uncorrected_ber_instantaneous_warn_high_threshold",
                                        "uncorrected_ber_instantaneous_warn_low_threshold",
                                        "uncorrected_ber_latched_max_alarm_high_threshold",
                                        "uncorrected_ber_latched_max_alarm_low_threshold",
                                        "uncorrected_ber_latched_max_warn_high_threshold",
                                        "uncorrected_ber_latched_max_warn_low_threshold",
                                        "uncorrected_ber_latched_min_alarm_high_threshold",
                                        "uncorrected_ber_latched_min_alarm_low_threshold",
                                        "uncorrected_ber_latched_min_warn_high_threshold",
                                        "uncorrected_ber_latched_min_warn_low_threshold",
                                        "uncorrected_ber_warn_high_threshold",
                                        "uncorrected_ber_warn_low_threshold") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtParamThresholdVal, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtParamThresholdVal, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.isi_correction_alarm_high_threshold.is_set or
                            self.isi_correction_alarm_low_threshold.is_set or
                            self.isi_correction_warn_high_threshold.is_set or
                            self.isi_correction_warn_low_threshold.is_set or
                            self.laser_diff_frequency_alarm_high_threshold.is_set or
                            self.laser_diff_frequency_alarm_low_threshold.is_set or
                            self.laser_diff_frequency_warn_high_threshold.is_set or
                            self.laser_diff_frequency_warn_low_threshold.is_set or
                            self.laser_diff_temperature_alarm_high_threshold.is_set or
                            self.laser_diff_temperature_alarm_low_threshold.is_set or
                            self.laser_diff_temperature_warn_high_threshold.is_set or
                            self.laser_diff_temperature_warn_low_threshold.is_set or
                            self.pam_rate_alarm_high_threshold.is_set or
                            self.pam_rate_alarm_low_threshold.is_set or
                            self.pam_rate_warn_high_threshold.is_set or
                            self.pam_rate_warn_low_threshold.is_set or
                            self.pre_fec_ber_accumulated_alarm_high_threshold.is_set or
                            self.pre_fec_ber_accumulated_alarm_low_threshold.is_set or
                            self.pre_fec_ber_accumulated_warn_high_threshold.is_set or
                            self.pre_fec_ber_accumulated_warn_low_threshold.is_set or
                            self.pre_fec_ber_alarm_high_threshold.is_set or
                            self.pre_fec_ber_alarm_low_threshold.is_set or
                            self.pre_fec_ber_instantaneous_alarm_high_threshold.is_set or
                            self.pre_fec_ber_instantaneous_alarm_low_threshold.is_set or
                            self.pre_fec_ber_instantaneous_warn_high_threshold.is_set or
                            self.pre_fec_ber_instantaneous_warn_low_threshold.is_set or
                            self.pre_fec_ber_latched_max_alarm_high_threshold.is_set or
                            self.pre_fec_ber_latched_max_alarm_low_threshold.is_set or
                            self.pre_fec_ber_latched_max_warn_high_threshold.is_set or
                            self.pre_fec_ber_latched_max_warn_low_threshold.is_set or
                            self.pre_fec_ber_latched_min_alarm_high_threshold.is_set or
                            self.pre_fec_ber_latched_min_alarm_low_threshold.is_set or
                            self.pre_fec_ber_latched_min_warn_high_threshold.is_set or
                            self.pre_fec_ber_latched_min_warn_low_threshold.is_set or
                            self.pre_fec_ber_warn_high_threshold.is_set or
                            self.pre_fec_ber_warn_low_threshold.is_set or
                            self.snr_alarm_high_threshold.is_set or
                            self.snr_alarm_low_threshold.is_set or
                            self.snr_warn_high_threshold.is_set or
                            self.snr_warn_low_threshold.is_set or
                            self.tec_current_alarm_high_threshold.is_set or
                            self.tec_current_alarm_low_threshold.is_set or
                            self.tec_current_warn_high_threshold.is_set or
                            self.tec_current_warn_low_threshold.is_set or
                            self.uncorrected_ber_accumulated_alarm_high_threshold.is_set or
                            self.uncorrected_ber_accumulated_alarm_low_threshold.is_set or
                            self.uncorrected_ber_accumulated_warn_high_threshold.is_set or
                            self.uncorrected_ber_accumulated_warn_low_threshold.is_set or
                            self.uncorrected_ber_alarm_high_threshold.is_set or
                            self.uncorrected_ber_alarm_low_threshold.is_set or
                            self.uncorrected_ber_instantaneous_alarm_high_threshold.is_set or
                            self.uncorrected_ber_instantaneous_alarm_low_threshold.is_set or
                            self.uncorrected_ber_instantaneous_warn_high_threshold.is_set or
                            self.uncorrected_ber_instantaneous_warn_low_threshold.is_set or
                            self.uncorrected_ber_latched_max_alarm_high_threshold.is_set or
                            self.uncorrected_ber_latched_max_alarm_low_threshold.is_set or
                            self.uncorrected_ber_latched_max_warn_high_threshold.is_set or
                            self.uncorrected_ber_latched_max_warn_low_threshold.is_set or
                            self.uncorrected_ber_latched_min_alarm_high_threshold.is_set or
                            self.uncorrected_ber_latched_min_alarm_low_threshold.is_set or
                            self.uncorrected_ber_latched_min_warn_high_threshold.is_set or
                            self.uncorrected_ber_latched_min_warn_low_threshold.is_set or
                            self.uncorrected_ber_warn_high_threshold.is_set or
                            self.uncorrected_ber_warn_low_threshold.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.isi_correction_alarm_high_threshold.yfilter != YFilter.not_set or
                            self.isi_correction_alarm_low_threshold.yfilter != YFilter.not_set or
                            self.isi_correction_warn_high_threshold.yfilter != YFilter.not_set or
                            self.isi_correction_warn_low_threshold.yfilter != YFilter.not_set or
                            self.laser_diff_frequency_alarm_high_threshold.yfilter != YFilter.not_set or
                            self.laser_diff_frequency_alarm_low_threshold.yfilter != YFilter.not_set or
                            self.laser_diff_frequency_warn_high_threshold.yfilter != YFilter.not_set or
                            self.laser_diff_frequency_warn_low_threshold.yfilter != YFilter.not_set or
                            self.laser_diff_temperature_alarm_high_threshold.yfilter != YFilter.not_set or
                            self.laser_diff_temperature_alarm_low_threshold.yfilter != YFilter.not_set or
                            self.laser_diff_temperature_warn_high_threshold.yfilter != YFilter.not_set or
                            self.laser_diff_temperature_warn_low_threshold.yfilter != YFilter.not_set or
                            self.pam_rate_alarm_high_threshold.yfilter != YFilter.not_set or
                            self.pam_rate_alarm_low_threshold.yfilter != YFilter.not_set or
                            self.pam_rate_warn_high_threshold.yfilter != YFilter.not_set or
                            self.pam_rate_warn_low_threshold.yfilter != YFilter.not_set or
                            self.pre_fec_ber_accumulated_alarm_high_threshold.yfilter != YFilter.not_set or
                            self.pre_fec_ber_accumulated_alarm_low_threshold.yfilter != YFilter.not_set or
                            self.pre_fec_ber_accumulated_warn_high_threshold.yfilter != YFilter.not_set or
                            self.pre_fec_ber_accumulated_warn_low_threshold.yfilter != YFilter.not_set or
                            self.pre_fec_ber_alarm_high_threshold.yfilter != YFilter.not_set or
                            self.pre_fec_ber_alarm_low_threshold.yfilter != YFilter.not_set or
                            self.pre_fec_ber_instantaneous_alarm_high_threshold.yfilter != YFilter.not_set or
                            self.pre_fec_ber_instantaneous_alarm_low_threshold.yfilter != YFilter.not_set or
                            self.pre_fec_ber_instantaneous_warn_high_threshold.yfilter != YFilter.not_set or
                            self.pre_fec_ber_instantaneous_warn_low_threshold.yfilter != YFilter.not_set or
                            self.pre_fec_ber_latched_max_alarm_high_threshold.yfilter != YFilter.not_set or
                            self.pre_fec_ber_latched_max_alarm_low_threshold.yfilter != YFilter.not_set or
                            self.pre_fec_ber_latched_max_warn_high_threshold.yfilter != YFilter.not_set or
                            self.pre_fec_ber_latched_max_warn_low_threshold.yfilter != YFilter.not_set or
                            self.pre_fec_ber_latched_min_alarm_high_threshold.yfilter != YFilter.not_set or
                            self.pre_fec_ber_latched_min_alarm_low_threshold.yfilter != YFilter.not_set or
                            self.pre_fec_ber_latched_min_warn_high_threshold.yfilter != YFilter.not_set or
                            self.pre_fec_ber_latched_min_warn_low_threshold.yfilter != YFilter.not_set or
                            self.pre_fec_ber_warn_high_threshold.yfilter != YFilter.not_set or
                            self.pre_fec_ber_warn_low_threshold.yfilter != YFilter.not_set or
                            self.snr_alarm_high_threshold.yfilter != YFilter.not_set or
                            self.snr_alarm_low_threshold.yfilter != YFilter.not_set or
                            self.snr_warn_high_threshold.yfilter != YFilter.not_set or
                            self.snr_warn_low_threshold.yfilter != YFilter.not_set or
                            self.tec_current_alarm_high_threshold.yfilter != YFilter.not_set or
                            self.tec_current_alarm_low_threshold.yfilter != YFilter.not_set or
                            self.tec_current_warn_high_threshold.yfilter != YFilter.not_set or
                            self.tec_current_warn_low_threshold.yfilter != YFilter.not_set or
                            self.uncorrected_ber_accumulated_alarm_high_threshold.yfilter != YFilter.not_set or
                            self.uncorrected_ber_accumulated_alarm_low_threshold.yfilter != YFilter.not_set or
                            self.uncorrected_ber_accumulated_warn_high_threshold.yfilter != YFilter.not_set or
                            self.uncorrected_ber_accumulated_warn_low_threshold.yfilter != YFilter.not_set or
                            self.uncorrected_ber_alarm_high_threshold.yfilter != YFilter.not_set or
                            self.uncorrected_ber_alarm_low_threshold.yfilter != YFilter.not_set or
                            self.uncorrected_ber_instantaneous_alarm_high_threshold.yfilter != YFilter.not_set or
                            self.uncorrected_ber_instantaneous_alarm_low_threshold.yfilter != YFilter.not_set or
                            self.uncorrected_ber_instantaneous_warn_high_threshold.yfilter != YFilter.not_set or
                            self.uncorrected_ber_instantaneous_warn_low_threshold.yfilter != YFilter.not_set or
                            self.uncorrected_ber_latched_max_alarm_high_threshold.yfilter != YFilter.not_set or
                            self.uncorrected_ber_latched_max_alarm_low_threshold.yfilter != YFilter.not_set or
                            self.uncorrected_ber_latched_max_warn_high_threshold.yfilter != YFilter.not_set or
                            self.uncorrected_ber_latched_max_warn_low_threshold.yfilter != YFilter.not_set or
                            self.uncorrected_ber_latched_min_alarm_high_threshold.yfilter != YFilter.not_set or
                            self.uncorrected_ber_latched_min_alarm_low_threshold.yfilter != YFilter.not_set or
                            self.uncorrected_ber_latched_min_warn_high_threshold.yfilter != YFilter.not_set or
                            self.uncorrected_ber_latched_min_warn_low_threshold.yfilter != YFilter.not_set or
                            self.uncorrected_ber_warn_high_threshold.yfilter != YFilter.not_set or
                            self.uncorrected_ber_warn_low_threshold.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "ext-param-threshold-val" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.isi_correction_alarm_high_threshold.is_set or self.isi_correction_alarm_high_threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.isi_correction_alarm_high_threshold.get_name_leafdata())
                        if (self.isi_correction_alarm_low_threshold.is_set or self.isi_correction_alarm_low_threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.isi_correction_alarm_low_threshold.get_name_leafdata())
                        if (self.isi_correction_warn_high_threshold.is_set or self.isi_correction_warn_high_threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.isi_correction_warn_high_threshold.get_name_leafdata())
                        if (self.isi_correction_warn_low_threshold.is_set or self.isi_correction_warn_low_threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.isi_correction_warn_low_threshold.get_name_leafdata())
                        if (self.laser_diff_frequency_alarm_high_threshold.is_set or self.laser_diff_frequency_alarm_high_threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.laser_diff_frequency_alarm_high_threshold.get_name_leafdata())
                        if (self.laser_diff_frequency_alarm_low_threshold.is_set or self.laser_diff_frequency_alarm_low_threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.laser_diff_frequency_alarm_low_threshold.get_name_leafdata())
                        if (self.laser_diff_frequency_warn_high_threshold.is_set or self.laser_diff_frequency_warn_high_threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.laser_diff_frequency_warn_high_threshold.get_name_leafdata())
                        if (self.laser_diff_frequency_warn_low_threshold.is_set or self.laser_diff_frequency_warn_low_threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.laser_diff_frequency_warn_low_threshold.get_name_leafdata())
                        if (self.laser_diff_temperature_alarm_high_threshold.is_set or self.laser_diff_temperature_alarm_high_threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.laser_diff_temperature_alarm_high_threshold.get_name_leafdata())
                        if (self.laser_diff_temperature_alarm_low_threshold.is_set or self.laser_diff_temperature_alarm_low_threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.laser_diff_temperature_alarm_low_threshold.get_name_leafdata())
                        if (self.laser_diff_temperature_warn_high_threshold.is_set or self.laser_diff_temperature_warn_high_threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.laser_diff_temperature_warn_high_threshold.get_name_leafdata())
                        if (self.laser_diff_temperature_warn_low_threshold.is_set or self.laser_diff_temperature_warn_low_threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.laser_diff_temperature_warn_low_threshold.get_name_leafdata())
                        if (self.pam_rate_alarm_high_threshold.is_set or self.pam_rate_alarm_high_threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.pam_rate_alarm_high_threshold.get_name_leafdata())
                        if (self.pam_rate_alarm_low_threshold.is_set or self.pam_rate_alarm_low_threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.pam_rate_alarm_low_threshold.get_name_leafdata())
                        if (self.pam_rate_warn_high_threshold.is_set or self.pam_rate_warn_high_threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.pam_rate_warn_high_threshold.get_name_leafdata())
                        if (self.pam_rate_warn_low_threshold.is_set or self.pam_rate_warn_low_threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.pam_rate_warn_low_threshold.get_name_leafdata())
                        if (self.pre_fec_ber_accumulated_alarm_high_threshold.is_set or self.pre_fec_ber_accumulated_alarm_high_threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.pre_fec_ber_accumulated_alarm_high_threshold.get_name_leafdata())
                        if (self.pre_fec_ber_accumulated_alarm_low_threshold.is_set or self.pre_fec_ber_accumulated_alarm_low_threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.pre_fec_ber_accumulated_alarm_low_threshold.get_name_leafdata())
                        if (self.pre_fec_ber_accumulated_warn_high_threshold.is_set or self.pre_fec_ber_accumulated_warn_high_threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.pre_fec_ber_accumulated_warn_high_threshold.get_name_leafdata())
                        if (self.pre_fec_ber_accumulated_warn_low_threshold.is_set or self.pre_fec_ber_accumulated_warn_low_threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.pre_fec_ber_accumulated_warn_low_threshold.get_name_leafdata())
                        if (self.pre_fec_ber_alarm_high_threshold.is_set or self.pre_fec_ber_alarm_high_threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.pre_fec_ber_alarm_high_threshold.get_name_leafdata())
                        if (self.pre_fec_ber_alarm_low_threshold.is_set or self.pre_fec_ber_alarm_low_threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.pre_fec_ber_alarm_low_threshold.get_name_leafdata())
                        if (self.pre_fec_ber_instantaneous_alarm_high_threshold.is_set or self.pre_fec_ber_instantaneous_alarm_high_threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.pre_fec_ber_instantaneous_alarm_high_threshold.get_name_leafdata())
                        if (self.pre_fec_ber_instantaneous_alarm_low_threshold.is_set or self.pre_fec_ber_instantaneous_alarm_low_threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.pre_fec_ber_instantaneous_alarm_low_threshold.get_name_leafdata())
                        if (self.pre_fec_ber_instantaneous_warn_high_threshold.is_set or self.pre_fec_ber_instantaneous_warn_high_threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.pre_fec_ber_instantaneous_warn_high_threshold.get_name_leafdata())
                        if (self.pre_fec_ber_instantaneous_warn_low_threshold.is_set or self.pre_fec_ber_instantaneous_warn_low_threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.pre_fec_ber_instantaneous_warn_low_threshold.get_name_leafdata())
                        if (self.pre_fec_ber_latched_max_alarm_high_threshold.is_set or self.pre_fec_ber_latched_max_alarm_high_threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.pre_fec_ber_latched_max_alarm_high_threshold.get_name_leafdata())
                        if (self.pre_fec_ber_latched_max_alarm_low_threshold.is_set or self.pre_fec_ber_latched_max_alarm_low_threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.pre_fec_ber_latched_max_alarm_low_threshold.get_name_leafdata())
                        if (self.pre_fec_ber_latched_max_warn_high_threshold.is_set or self.pre_fec_ber_latched_max_warn_high_threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.pre_fec_ber_latched_max_warn_high_threshold.get_name_leafdata())
                        if (self.pre_fec_ber_latched_max_warn_low_threshold.is_set or self.pre_fec_ber_latched_max_warn_low_threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.pre_fec_ber_latched_max_warn_low_threshold.get_name_leafdata())
                        if (self.pre_fec_ber_latched_min_alarm_high_threshold.is_set or self.pre_fec_ber_latched_min_alarm_high_threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.pre_fec_ber_latched_min_alarm_high_threshold.get_name_leafdata())
                        if (self.pre_fec_ber_latched_min_alarm_low_threshold.is_set or self.pre_fec_ber_latched_min_alarm_low_threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.pre_fec_ber_latched_min_alarm_low_threshold.get_name_leafdata())
                        if (self.pre_fec_ber_latched_min_warn_high_threshold.is_set or self.pre_fec_ber_latched_min_warn_high_threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.pre_fec_ber_latched_min_warn_high_threshold.get_name_leafdata())
                        if (self.pre_fec_ber_latched_min_warn_low_threshold.is_set or self.pre_fec_ber_latched_min_warn_low_threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.pre_fec_ber_latched_min_warn_low_threshold.get_name_leafdata())
                        if (self.pre_fec_ber_warn_high_threshold.is_set or self.pre_fec_ber_warn_high_threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.pre_fec_ber_warn_high_threshold.get_name_leafdata())
                        if (self.pre_fec_ber_warn_low_threshold.is_set or self.pre_fec_ber_warn_low_threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.pre_fec_ber_warn_low_threshold.get_name_leafdata())
                        if (self.snr_alarm_high_threshold.is_set or self.snr_alarm_high_threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.snr_alarm_high_threshold.get_name_leafdata())
                        if (self.snr_alarm_low_threshold.is_set or self.snr_alarm_low_threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.snr_alarm_low_threshold.get_name_leafdata())
                        if (self.snr_warn_high_threshold.is_set or self.snr_warn_high_threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.snr_warn_high_threshold.get_name_leafdata())
                        if (self.snr_warn_low_threshold.is_set or self.snr_warn_low_threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.snr_warn_low_threshold.get_name_leafdata())
                        if (self.tec_current_alarm_high_threshold.is_set or self.tec_current_alarm_high_threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.tec_current_alarm_high_threshold.get_name_leafdata())
                        if (self.tec_current_alarm_low_threshold.is_set or self.tec_current_alarm_low_threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.tec_current_alarm_low_threshold.get_name_leafdata())
                        if (self.tec_current_warn_high_threshold.is_set or self.tec_current_warn_high_threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.tec_current_warn_high_threshold.get_name_leafdata())
                        if (self.tec_current_warn_low_threshold.is_set or self.tec_current_warn_low_threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.tec_current_warn_low_threshold.get_name_leafdata())
                        if (self.uncorrected_ber_accumulated_alarm_high_threshold.is_set or self.uncorrected_ber_accumulated_alarm_high_threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.uncorrected_ber_accumulated_alarm_high_threshold.get_name_leafdata())
                        if (self.uncorrected_ber_accumulated_alarm_low_threshold.is_set or self.uncorrected_ber_accumulated_alarm_low_threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.uncorrected_ber_accumulated_alarm_low_threshold.get_name_leafdata())
                        if (self.uncorrected_ber_accumulated_warn_high_threshold.is_set or self.uncorrected_ber_accumulated_warn_high_threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.uncorrected_ber_accumulated_warn_high_threshold.get_name_leafdata())
                        if (self.uncorrected_ber_accumulated_warn_low_threshold.is_set or self.uncorrected_ber_accumulated_warn_low_threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.uncorrected_ber_accumulated_warn_low_threshold.get_name_leafdata())
                        if (self.uncorrected_ber_alarm_high_threshold.is_set or self.uncorrected_ber_alarm_high_threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.uncorrected_ber_alarm_high_threshold.get_name_leafdata())
                        if (self.uncorrected_ber_alarm_low_threshold.is_set or self.uncorrected_ber_alarm_low_threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.uncorrected_ber_alarm_low_threshold.get_name_leafdata())
                        if (self.uncorrected_ber_instantaneous_alarm_high_threshold.is_set or self.uncorrected_ber_instantaneous_alarm_high_threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.uncorrected_ber_instantaneous_alarm_high_threshold.get_name_leafdata())
                        if (self.uncorrected_ber_instantaneous_alarm_low_threshold.is_set or self.uncorrected_ber_instantaneous_alarm_low_threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.uncorrected_ber_instantaneous_alarm_low_threshold.get_name_leafdata())
                        if (self.uncorrected_ber_instantaneous_warn_high_threshold.is_set or self.uncorrected_ber_instantaneous_warn_high_threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.uncorrected_ber_instantaneous_warn_high_threshold.get_name_leafdata())
                        if (self.uncorrected_ber_instantaneous_warn_low_threshold.is_set or self.uncorrected_ber_instantaneous_warn_low_threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.uncorrected_ber_instantaneous_warn_low_threshold.get_name_leafdata())
                        if (self.uncorrected_ber_latched_max_alarm_high_threshold.is_set or self.uncorrected_ber_latched_max_alarm_high_threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.uncorrected_ber_latched_max_alarm_high_threshold.get_name_leafdata())
                        if (self.uncorrected_ber_latched_max_alarm_low_threshold.is_set or self.uncorrected_ber_latched_max_alarm_low_threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.uncorrected_ber_latched_max_alarm_low_threshold.get_name_leafdata())
                        if (self.uncorrected_ber_latched_max_warn_high_threshold.is_set or self.uncorrected_ber_latched_max_warn_high_threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.uncorrected_ber_latched_max_warn_high_threshold.get_name_leafdata())
                        if (self.uncorrected_ber_latched_max_warn_low_threshold.is_set or self.uncorrected_ber_latched_max_warn_low_threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.uncorrected_ber_latched_max_warn_low_threshold.get_name_leafdata())
                        if (self.uncorrected_ber_latched_min_alarm_high_threshold.is_set or self.uncorrected_ber_latched_min_alarm_high_threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.uncorrected_ber_latched_min_alarm_high_threshold.get_name_leafdata())
                        if (self.uncorrected_ber_latched_min_alarm_low_threshold.is_set or self.uncorrected_ber_latched_min_alarm_low_threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.uncorrected_ber_latched_min_alarm_low_threshold.get_name_leafdata())
                        if (self.uncorrected_ber_latched_min_warn_high_threshold.is_set or self.uncorrected_ber_latched_min_warn_high_threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.uncorrected_ber_latched_min_warn_high_threshold.get_name_leafdata())
                        if (self.uncorrected_ber_latched_min_warn_low_threshold.is_set or self.uncorrected_ber_latched_min_warn_low_threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.uncorrected_ber_latched_min_warn_low_threshold.get_name_leafdata())
                        if (self.uncorrected_ber_warn_high_threshold.is_set or self.uncorrected_ber_warn_high_threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.uncorrected_ber_warn_high_threshold.get_name_leafdata())
                        if (self.uncorrected_ber_warn_low_threshold.is_set or self.uncorrected_ber_warn_low_threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.uncorrected_ber_warn_low_threshold.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "isi-correction-alarm-high-threshold" or name == "isi-correction-alarm-low-threshold" or name == "isi-correction-warn-high-threshold" or name == "isi-correction-warn-low-threshold" or name == "laser-diff-frequency-alarm-high-threshold" or name == "laser-diff-frequency-alarm-low-threshold" or name == "laser-diff-frequency-warn-high-threshold" or name == "laser-diff-frequency-warn-low-threshold" or name == "laser-diff-temperature-alarm-high-threshold" or name == "laser-diff-temperature-alarm-low-threshold" or name == "laser-diff-temperature-warn-high-threshold" or name == "laser-diff-temperature-warn-low-threshold" or name == "pam-rate-alarm-high-threshold" or name == "pam-rate-alarm-low-threshold" or name == "pam-rate-warn-high-threshold" or name == "pam-rate-warn-low-threshold" or name == "pre-fec-ber-accumulated-alarm-high-threshold" or name == "pre-fec-ber-accumulated-alarm-low-threshold" or name == "pre-fec-ber-accumulated-warn-high-threshold" or name == "pre-fec-ber-accumulated-warn-low-threshold" or name == "pre-fec-ber-alarm-high-threshold" or name == "pre-fec-ber-alarm-low-threshold" or name == "pre-fec-ber-instantaneous-alarm-high-threshold" or name == "pre-fec-ber-instantaneous-alarm-low-threshold" or name == "pre-fec-ber-instantaneous-warn-high-threshold" or name == "pre-fec-ber-instantaneous-warn-low-threshold" or name == "pre-fec-ber-latched-max-alarm-high-threshold" or name == "pre-fec-ber-latched-max-alarm-low-threshold" or name == "pre-fec-ber-latched-max-warn-high-threshold" or name == "pre-fec-ber-latched-max-warn-low-threshold" or name == "pre-fec-ber-latched-min-alarm-high-threshold" or name == "pre-fec-ber-latched-min-alarm-low-threshold" or name == "pre-fec-ber-latched-min-warn-high-threshold" or name == "pre-fec-ber-latched-min-warn-low-threshold" or name == "pre-fec-ber-warn-high-threshold" or name == "pre-fec-ber-warn-low-threshold" or name == "snr-alarm-high-threshold" or name == "snr-alarm-low-threshold" or name == "snr-warn-high-threshold" or name == "snr-warn-low-threshold" or name == "tec-current-alarm-high-threshold" or name == "tec-current-alarm-low-threshold" or name == "tec-current-warn-high-threshold" or name == "tec-current-warn-low-threshold" or name == "uncorrected-ber-accumulated-alarm-high-threshold" or name == "uncorrected-ber-accumulated-alarm-low-threshold" or name == "uncorrected-ber-accumulated-warn-high-threshold" or name == "uncorrected-ber-accumulated-warn-low-threshold" or name == "uncorrected-ber-alarm-high-threshold" or name == "uncorrected-ber-alarm-low-threshold" or name == "uncorrected-ber-instantaneous-alarm-high-threshold" or name == "uncorrected-ber-instantaneous-alarm-low-threshold" or name == "uncorrected-ber-instantaneous-warn-high-threshold" or name == "uncorrected-ber-instantaneous-warn-low-threshold" or name == "uncorrected-ber-latched-max-alarm-high-threshold" or name == "uncorrected-ber-latched-max-alarm-low-threshold" or name == "uncorrected-ber-latched-max-warn-high-threshold" or name == "uncorrected-ber-latched-max-warn-low-threshold" or name == "uncorrected-ber-latched-min-alarm-high-threshold" or name == "uncorrected-ber-latched-min-alarm-low-threshold" or name == "uncorrected-ber-latched-min-warn-high-threshold" or name == "uncorrected-ber-latched-min-warn-low-threshold" or name == "uncorrected-ber-warn-high-threshold" or name == "uncorrected-ber-warn-low-threshold"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "isi-correction-alarm-high-threshold"):
                            self.isi_correction_alarm_high_threshold = value
                            self.isi_correction_alarm_high_threshold.value_namespace = name_space
                            self.isi_correction_alarm_high_threshold.value_namespace_prefix = name_space_prefix
                        if(value_path == "isi-correction-alarm-low-threshold"):
                            self.isi_correction_alarm_low_threshold = value
                            self.isi_correction_alarm_low_threshold.value_namespace = name_space
                            self.isi_correction_alarm_low_threshold.value_namespace_prefix = name_space_prefix
                        if(value_path == "isi-correction-warn-high-threshold"):
                            self.isi_correction_warn_high_threshold = value
                            self.isi_correction_warn_high_threshold.value_namespace = name_space
                            self.isi_correction_warn_high_threshold.value_namespace_prefix = name_space_prefix
                        if(value_path == "isi-correction-warn-low-threshold"):
                            self.isi_correction_warn_low_threshold = value
                            self.isi_correction_warn_low_threshold.value_namespace = name_space
                            self.isi_correction_warn_low_threshold.value_namespace_prefix = name_space_prefix
                        if(value_path == "laser-diff-frequency-alarm-high-threshold"):
                            self.laser_diff_frequency_alarm_high_threshold = value
                            self.laser_diff_frequency_alarm_high_threshold.value_namespace = name_space
                            self.laser_diff_frequency_alarm_high_threshold.value_namespace_prefix = name_space_prefix
                        if(value_path == "laser-diff-frequency-alarm-low-threshold"):
                            self.laser_diff_frequency_alarm_low_threshold = value
                            self.laser_diff_frequency_alarm_low_threshold.value_namespace = name_space
                            self.laser_diff_frequency_alarm_low_threshold.value_namespace_prefix = name_space_prefix
                        if(value_path == "laser-diff-frequency-warn-high-threshold"):
                            self.laser_diff_frequency_warn_high_threshold = value
                            self.laser_diff_frequency_warn_high_threshold.value_namespace = name_space
                            self.laser_diff_frequency_warn_high_threshold.value_namespace_prefix = name_space_prefix
                        if(value_path == "laser-diff-frequency-warn-low-threshold"):
                            self.laser_diff_frequency_warn_low_threshold = value
                            self.laser_diff_frequency_warn_low_threshold.value_namespace = name_space
                            self.laser_diff_frequency_warn_low_threshold.value_namespace_prefix = name_space_prefix
                        if(value_path == "laser-diff-temperature-alarm-high-threshold"):
                            self.laser_diff_temperature_alarm_high_threshold = value
                            self.laser_diff_temperature_alarm_high_threshold.value_namespace = name_space
                            self.laser_diff_temperature_alarm_high_threshold.value_namespace_prefix = name_space_prefix
                        if(value_path == "laser-diff-temperature-alarm-low-threshold"):
                            self.laser_diff_temperature_alarm_low_threshold = value
                            self.laser_diff_temperature_alarm_low_threshold.value_namespace = name_space
                            self.laser_diff_temperature_alarm_low_threshold.value_namespace_prefix = name_space_prefix
                        if(value_path == "laser-diff-temperature-warn-high-threshold"):
                            self.laser_diff_temperature_warn_high_threshold = value
                            self.laser_diff_temperature_warn_high_threshold.value_namespace = name_space
                            self.laser_diff_temperature_warn_high_threshold.value_namespace_prefix = name_space_prefix
                        if(value_path == "laser-diff-temperature-warn-low-threshold"):
                            self.laser_diff_temperature_warn_low_threshold = value
                            self.laser_diff_temperature_warn_low_threshold.value_namespace = name_space
                            self.laser_diff_temperature_warn_low_threshold.value_namespace_prefix = name_space_prefix
                        if(value_path == "pam-rate-alarm-high-threshold"):
                            self.pam_rate_alarm_high_threshold = value
                            self.pam_rate_alarm_high_threshold.value_namespace = name_space
                            self.pam_rate_alarm_high_threshold.value_namespace_prefix = name_space_prefix
                        if(value_path == "pam-rate-alarm-low-threshold"):
                            self.pam_rate_alarm_low_threshold = value
                            self.pam_rate_alarm_low_threshold.value_namespace = name_space
                            self.pam_rate_alarm_low_threshold.value_namespace_prefix = name_space_prefix
                        if(value_path == "pam-rate-warn-high-threshold"):
                            self.pam_rate_warn_high_threshold = value
                            self.pam_rate_warn_high_threshold.value_namespace = name_space
                            self.pam_rate_warn_high_threshold.value_namespace_prefix = name_space_prefix
                        if(value_path == "pam-rate-warn-low-threshold"):
                            self.pam_rate_warn_low_threshold = value
                            self.pam_rate_warn_low_threshold.value_namespace = name_space
                            self.pam_rate_warn_low_threshold.value_namespace_prefix = name_space_prefix
                        if(value_path == "pre-fec-ber-accumulated-alarm-high-threshold"):
                            self.pre_fec_ber_accumulated_alarm_high_threshold = value
                            self.pre_fec_ber_accumulated_alarm_high_threshold.value_namespace = name_space
                            self.pre_fec_ber_accumulated_alarm_high_threshold.value_namespace_prefix = name_space_prefix
                        if(value_path == "pre-fec-ber-accumulated-alarm-low-threshold"):
                            self.pre_fec_ber_accumulated_alarm_low_threshold = value
                            self.pre_fec_ber_accumulated_alarm_low_threshold.value_namespace = name_space
                            self.pre_fec_ber_accumulated_alarm_low_threshold.value_namespace_prefix = name_space_prefix
                        if(value_path == "pre-fec-ber-accumulated-warn-high-threshold"):
                            self.pre_fec_ber_accumulated_warn_high_threshold = value
                            self.pre_fec_ber_accumulated_warn_high_threshold.value_namespace = name_space
                            self.pre_fec_ber_accumulated_warn_high_threshold.value_namespace_prefix = name_space_prefix
                        if(value_path == "pre-fec-ber-accumulated-warn-low-threshold"):
                            self.pre_fec_ber_accumulated_warn_low_threshold = value
                            self.pre_fec_ber_accumulated_warn_low_threshold.value_namespace = name_space
                            self.pre_fec_ber_accumulated_warn_low_threshold.value_namespace_prefix = name_space_prefix
                        if(value_path == "pre-fec-ber-alarm-high-threshold"):
                            self.pre_fec_ber_alarm_high_threshold = value
                            self.pre_fec_ber_alarm_high_threshold.value_namespace = name_space
                            self.pre_fec_ber_alarm_high_threshold.value_namespace_prefix = name_space_prefix
                        if(value_path == "pre-fec-ber-alarm-low-threshold"):
                            self.pre_fec_ber_alarm_low_threshold = value
                            self.pre_fec_ber_alarm_low_threshold.value_namespace = name_space
                            self.pre_fec_ber_alarm_low_threshold.value_namespace_prefix = name_space_prefix
                        if(value_path == "pre-fec-ber-instantaneous-alarm-high-threshold"):
                            self.pre_fec_ber_instantaneous_alarm_high_threshold = value
                            self.pre_fec_ber_instantaneous_alarm_high_threshold.value_namespace = name_space
                            self.pre_fec_ber_instantaneous_alarm_high_threshold.value_namespace_prefix = name_space_prefix
                        if(value_path == "pre-fec-ber-instantaneous-alarm-low-threshold"):
                            self.pre_fec_ber_instantaneous_alarm_low_threshold = value
                            self.pre_fec_ber_instantaneous_alarm_low_threshold.value_namespace = name_space
                            self.pre_fec_ber_instantaneous_alarm_low_threshold.value_namespace_prefix = name_space_prefix
                        if(value_path == "pre-fec-ber-instantaneous-warn-high-threshold"):
                            self.pre_fec_ber_instantaneous_warn_high_threshold = value
                            self.pre_fec_ber_instantaneous_warn_high_threshold.value_namespace = name_space
                            self.pre_fec_ber_instantaneous_warn_high_threshold.value_namespace_prefix = name_space_prefix
                        if(value_path == "pre-fec-ber-instantaneous-warn-low-threshold"):
                            self.pre_fec_ber_instantaneous_warn_low_threshold = value
                            self.pre_fec_ber_instantaneous_warn_low_threshold.value_namespace = name_space
                            self.pre_fec_ber_instantaneous_warn_low_threshold.value_namespace_prefix = name_space_prefix
                        if(value_path == "pre-fec-ber-latched-max-alarm-high-threshold"):
                            self.pre_fec_ber_latched_max_alarm_high_threshold = value
                            self.pre_fec_ber_latched_max_alarm_high_threshold.value_namespace = name_space
                            self.pre_fec_ber_latched_max_alarm_high_threshold.value_namespace_prefix = name_space_prefix
                        if(value_path == "pre-fec-ber-latched-max-alarm-low-threshold"):
                            self.pre_fec_ber_latched_max_alarm_low_threshold = value
                            self.pre_fec_ber_latched_max_alarm_low_threshold.value_namespace = name_space
                            self.pre_fec_ber_latched_max_alarm_low_threshold.value_namespace_prefix = name_space_prefix
                        if(value_path == "pre-fec-ber-latched-max-warn-high-threshold"):
                            self.pre_fec_ber_latched_max_warn_high_threshold = value
                            self.pre_fec_ber_latched_max_warn_high_threshold.value_namespace = name_space
                            self.pre_fec_ber_latched_max_warn_high_threshold.value_namespace_prefix = name_space_prefix
                        if(value_path == "pre-fec-ber-latched-max-warn-low-threshold"):
                            self.pre_fec_ber_latched_max_warn_low_threshold = value
                            self.pre_fec_ber_latched_max_warn_low_threshold.value_namespace = name_space
                            self.pre_fec_ber_latched_max_warn_low_threshold.value_namespace_prefix = name_space_prefix
                        if(value_path == "pre-fec-ber-latched-min-alarm-high-threshold"):
                            self.pre_fec_ber_latched_min_alarm_high_threshold = value
                            self.pre_fec_ber_latched_min_alarm_high_threshold.value_namespace = name_space
                            self.pre_fec_ber_latched_min_alarm_high_threshold.value_namespace_prefix = name_space_prefix
                        if(value_path == "pre-fec-ber-latched-min-alarm-low-threshold"):
                            self.pre_fec_ber_latched_min_alarm_low_threshold = value
                            self.pre_fec_ber_latched_min_alarm_low_threshold.value_namespace = name_space
                            self.pre_fec_ber_latched_min_alarm_low_threshold.value_namespace_prefix = name_space_prefix
                        if(value_path == "pre-fec-ber-latched-min-warn-high-threshold"):
                            self.pre_fec_ber_latched_min_warn_high_threshold = value
                            self.pre_fec_ber_latched_min_warn_high_threshold.value_namespace = name_space
                            self.pre_fec_ber_latched_min_warn_high_threshold.value_namespace_prefix = name_space_prefix
                        if(value_path == "pre-fec-ber-latched-min-warn-low-threshold"):
                            self.pre_fec_ber_latched_min_warn_low_threshold = value
                            self.pre_fec_ber_latched_min_warn_low_threshold.value_namespace = name_space
                            self.pre_fec_ber_latched_min_warn_low_threshold.value_namespace_prefix = name_space_prefix
                        if(value_path == "pre-fec-ber-warn-high-threshold"):
                            self.pre_fec_ber_warn_high_threshold = value
                            self.pre_fec_ber_warn_high_threshold.value_namespace = name_space
                            self.pre_fec_ber_warn_high_threshold.value_namespace_prefix = name_space_prefix
                        if(value_path == "pre-fec-ber-warn-low-threshold"):
                            self.pre_fec_ber_warn_low_threshold = value
                            self.pre_fec_ber_warn_low_threshold.value_namespace = name_space
                            self.pre_fec_ber_warn_low_threshold.value_namespace_prefix = name_space_prefix
                        if(value_path == "snr-alarm-high-threshold"):
                            self.snr_alarm_high_threshold = value
                            self.snr_alarm_high_threshold.value_namespace = name_space
                            self.snr_alarm_high_threshold.value_namespace_prefix = name_space_prefix
                        if(value_path == "snr-alarm-low-threshold"):
                            self.snr_alarm_low_threshold = value
                            self.snr_alarm_low_threshold.value_namespace = name_space
                            self.snr_alarm_low_threshold.value_namespace_prefix = name_space_prefix
                        if(value_path == "snr-warn-high-threshold"):
                            self.snr_warn_high_threshold = value
                            self.snr_warn_high_threshold.value_namespace = name_space
                            self.snr_warn_high_threshold.value_namespace_prefix = name_space_prefix
                        if(value_path == "snr-warn-low-threshold"):
                            self.snr_warn_low_threshold = value
                            self.snr_warn_low_threshold.value_namespace = name_space
                            self.snr_warn_low_threshold.value_namespace_prefix = name_space_prefix
                        if(value_path == "tec-current-alarm-high-threshold"):
                            self.tec_current_alarm_high_threshold = value
                            self.tec_current_alarm_high_threshold.value_namespace = name_space
                            self.tec_current_alarm_high_threshold.value_namespace_prefix = name_space_prefix
                        if(value_path == "tec-current-alarm-low-threshold"):
                            self.tec_current_alarm_low_threshold = value
                            self.tec_current_alarm_low_threshold.value_namespace = name_space
                            self.tec_current_alarm_low_threshold.value_namespace_prefix = name_space_prefix
                        if(value_path == "tec-current-warn-high-threshold"):
                            self.tec_current_warn_high_threshold = value
                            self.tec_current_warn_high_threshold.value_namespace = name_space
                            self.tec_current_warn_high_threshold.value_namespace_prefix = name_space_prefix
                        if(value_path == "tec-current-warn-low-threshold"):
                            self.tec_current_warn_low_threshold = value
                            self.tec_current_warn_low_threshold.value_namespace = name_space
                            self.tec_current_warn_low_threshold.value_namespace_prefix = name_space_prefix
                        if(value_path == "uncorrected-ber-accumulated-alarm-high-threshold"):
                            self.uncorrected_ber_accumulated_alarm_high_threshold = value
                            self.uncorrected_ber_accumulated_alarm_high_threshold.value_namespace = name_space
                            self.uncorrected_ber_accumulated_alarm_high_threshold.value_namespace_prefix = name_space_prefix
                        if(value_path == "uncorrected-ber-accumulated-alarm-low-threshold"):
                            self.uncorrected_ber_accumulated_alarm_low_threshold = value
                            self.uncorrected_ber_accumulated_alarm_low_threshold.value_namespace = name_space
                            self.uncorrected_ber_accumulated_alarm_low_threshold.value_namespace_prefix = name_space_prefix
                        if(value_path == "uncorrected-ber-accumulated-warn-high-threshold"):
                            self.uncorrected_ber_accumulated_warn_high_threshold = value
                            self.uncorrected_ber_accumulated_warn_high_threshold.value_namespace = name_space
                            self.uncorrected_ber_accumulated_warn_high_threshold.value_namespace_prefix = name_space_prefix
                        if(value_path == "uncorrected-ber-accumulated-warn-low-threshold"):
                            self.uncorrected_ber_accumulated_warn_low_threshold = value
                            self.uncorrected_ber_accumulated_warn_low_threshold.value_namespace = name_space
                            self.uncorrected_ber_accumulated_warn_low_threshold.value_namespace_prefix = name_space_prefix
                        if(value_path == "uncorrected-ber-alarm-high-threshold"):
                            self.uncorrected_ber_alarm_high_threshold = value
                            self.uncorrected_ber_alarm_high_threshold.value_namespace = name_space
                            self.uncorrected_ber_alarm_high_threshold.value_namespace_prefix = name_space_prefix
                        if(value_path == "uncorrected-ber-alarm-low-threshold"):
                            self.uncorrected_ber_alarm_low_threshold = value
                            self.uncorrected_ber_alarm_low_threshold.value_namespace = name_space
                            self.uncorrected_ber_alarm_low_threshold.value_namespace_prefix = name_space_prefix
                        if(value_path == "uncorrected-ber-instantaneous-alarm-high-threshold"):
                            self.uncorrected_ber_instantaneous_alarm_high_threshold = value
                            self.uncorrected_ber_instantaneous_alarm_high_threshold.value_namespace = name_space
                            self.uncorrected_ber_instantaneous_alarm_high_threshold.value_namespace_prefix = name_space_prefix
                        if(value_path == "uncorrected-ber-instantaneous-alarm-low-threshold"):
                            self.uncorrected_ber_instantaneous_alarm_low_threshold = value
                            self.uncorrected_ber_instantaneous_alarm_low_threshold.value_namespace = name_space
                            self.uncorrected_ber_instantaneous_alarm_low_threshold.value_namespace_prefix = name_space_prefix
                        if(value_path == "uncorrected-ber-instantaneous-warn-high-threshold"):
                            self.uncorrected_ber_instantaneous_warn_high_threshold = value
                            self.uncorrected_ber_instantaneous_warn_high_threshold.value_namespace = name_space
                            self.uncorrected_ber_instantaneous_warn_high_threshold.value_namespace_prefix = name_space_prefix
                        if(value_path == "uncorrected-ber-instantaneous-warn-low-threshold"):
                            self.uncorrected_ber_instantaneous_warn_low_threshold = value
                            self.uncorrected_ber_instantaneous_warn_low_threshold.value_namespace = name_space
                            self.uncorrected_ber_instantaneous_warn_low_threshold.value_namespace_prefix = name_space_prefix
                        if(value_path == "uncorrected-ber-latched-max-alarm-high-threshold"):
                            self.uncorrected_ber_latched_max_alarm_high_threshold = value
                            self.uncorrected_ber_latched_max_alarm_high_threshold.value_namespace = name_space
                            self.uncorrected_ber_latched_max_alarm_high_threshold.value_namespace_prefix = name_space_prefix
                        if(value_path == "uncorrected-ber-latched-max-alarm-low-threshold"):
                            self.uncorrected_ber_latched_max_alarm_low_threshold = value
                            self.uncorrected_ber_latched_max_alarm_low_threshold.value_namespace = name_space
                            self.uncorrected_ber_latched_max_alarm_low_threshold.value_namespace_prefix = name_space_prefix
                        if(value_path == "uncorrected-ber-latched-max-warn-high-threshold"):
                            self.uncorrected_ber_latched_max_warn_high_threshold = value
                            self.uncorrected_ber_latched_max_warn_high_threshold.value_namespace = name_space
                            self.uncorrected_ber_latched_max_warn_high_threshold.value_namespace_prefix = name_space_prefix
                        if(value_path == "uncorrected-ber-latched-max-warn-low-threshold"):
                            self.uncorrected_ber_latched_max_warn_low_threshold = value
                            self.uncorrected_ber_latched_max_warn_low_threshold.value_namespace = name_space
                            self.uncorrected_ber_latched_max_warn_low_threshold.value_namespace_prefix = name_space_prefix
                        if(value_path == "uncorrected-ber-latched-min-alarm-high-threshold"):
                            self.uncorrected_ber_latched_min_alarm_high_threshold = value
                            self.uncorrected_ber_latched_min_alarm_high_threshold.value_namespace = name_space
                            self.uncorrected_ber_latched_min_alarm_high_threshold.value_namespace_prefix = name_space_prefix
                        if(value_path == "uncorrected-ber-latched-min-alarm-low-threshold"):
                            self.uncorrected_ber_latched_min_alarm_low_threshold = value
                            self.uncorrected_ber_latched_min_alarm_low_threshold.value_namespace = name_space
                            self.uncorrected_ber_latched_min_alarm_low_threshold.value_namespace_prefix = name_space_prefix
                        if(value_path == "uncorrected-ber-latched-min-warn-high-threshold"):
                            self.uncorrected_ber_latched_min_warn_high_threshold = value
                            self.uncorrected_ber_latched_min_warn_high_threshold.value_namespace = name_space
                            self.uncorrected_ber_latched_min_warn_high_threshold.value_namespace_prefix = name_space_prefix
                        if(value_path == "uncorrected-ber-latched-min-warn-low-threshold"):
                            self.uncorrected_ber_latched_min_warn_low_threshold = value
                            self.uncorrected_ber_latched_min_warn_low_threshold.value_namespace = name_space
                            self.uncorrected_ber_latched_min_warn_low_threshold.value_namespace_prefix = name_space_prefix
                        if(value_path == "uncorrected-ber-warn-high-threshold"):
                            self.uncorrected_ber_warn_high_threshold = value
                            self.uncorrected_ber_warn_high_threshold.value_namespace = name_space
                            self.uncorrected_ber_warn_high_threshold.value_namespace_prefix = name_space_prefix
                        if(value_path == "uncorrected-ber-warn-low-threshold"):
                            self.uncorrected_ber_warn_low_threshold = value
                            self.uncorrected_ber_warn_low_threshold.value_namespace = name_space
                            self.uncorrected_ber_warn_low_threshold.value_namespace_prefix = name_space_prefix


                class LaneData(Entity):
                    """
                    Lane information
                    
                    .. attribute:: lane_alarm_info
                    
                    	Lane Alarm Information
                    	**type**\:   :py:class:`LaneAlarmInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo>`
                    
                    .. attribute:: lane_index
                    
                    	The index number of the lane
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: laser_bias_current_milli_amps
                    
                    	Laser Bias Current in units of 0.01mA
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: laser_bias_current_percent
                    
                    	Laser Bias Current in units of 0.01 percentage
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: percentage
                    
                    .. attribute:: output_frequency
                    
                    	Output frequency read from hw in the unit 0 .01THz
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: receive_power
                    
                    	Transponder receive power in the unit of 0.01dBm
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: receive_signal_power
                    
                    	Transponder receive signal power in the unit of 0.01dBm
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: transmit_power
                    
                    	Transmit power in the unit of 0.01dBm
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: transmit_signal_power
                    
                    	Transmit Signal power in the unit of 0.01dBm
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    

                    """

                    _prefix = 'controller-optics-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData, self).__init__()

                        self.yang_name = "lane-data"
                        self.yang_parent_name = "optics-info"

                        self.lane_index = YLeaf(YType.uint32, "lane-index")

                        self.laser_bias_current_milli_amps = YLeaf(YType.uint32, "laser-bias-current-milli-amps")

                        self.laser_bias_current_percent = YLeaf(YType.uint32, "laser-bias-current-percent")

                        self.output_frequency = YLeaf(YType.int32, "output-frequency")

                        self.receive_power = YLeaf(YType.int32, "receive-power")

                        self.receive_signal_power = YLeaf(YType.int32, "receive-signal-power")

                        self.transmit_power = YLeaf(YType.int32, "transmit-power")

                        self.transmit_signal_power = YLeaf(YType.int32, "transmit-signal-power")

                        self.lane_alarm_info = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo()
                        self.lane_alarm_info.parent = self
                        self._children_name_map["lane_alarm_info"] = "lane-alarm-info"
                        self._children_yang_names.add("lane-alarm-info")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("lane_index",
                                        "laser_bias_current_milli_amps",
                                        "laser_bias_current_percent",
                                        "output_frequency",
                                        "receive_power",
                                        "receive_signal_power",
                                        "transmit_power",
                                        "transmit_signal_power") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData, self).__setattr__(name, value)


                    class LaneAlarmInfo(Entity):
                        """
                        Lane Alarm Information
                        
                        .. attribute:: high_lbc
                        
                        	High laser bias current
                        	**type**\:   :py:class:`HighLbc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.HighLbc>`
                        
                        .. attribute:: high_rx_power
                        
                        	High Rx Power
                        	**type**\:   :py:class:`HighRxPower <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.HighRxPower>`
                        
                        .. attribute:: high_tx_power
                        
                        	High Tx Power
                        	**type**\:   :py:class:`HighTxPower <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.HighTxPower>`
                        
                        .. attribute:: low_rx_power
                        
                        	Low Rx Power
                        	**type**\:   :py:class:`LowRxPower <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.LowRxPower>`
                        
                        .. attribute:: low_tx_power
                        
                        	Low Tx Power
                        	**type**\:   :py:class:`LowTxPower <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.LowTxPower>`
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo, self).__init__()

                            self.yang_name = "lane-alarm-info"
                            self.yang_parent_name = "lane-data"

                            self.high_lbc = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.HighLbc()
                            self.high_lbc.parent = self
                            self._children_name_map["high_lbc"] = "high-lbc"
                            self._children_yang_names.add("high-lbc")

                            self.high_rx_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.HighRxPower()
                            self.high_rx_power.parent = self
                            self._children_name_map["high_rx_power"] = "high-rx-power"
                            self._children_yang_names.add("high-rx-power")

                            self.high_tx_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.HighTxPower()
                            self.high_tx_power.parent = self
                            self._children_name_map["high_tx_power"] = "high-tx-power"
                            self._children_yang_names.add("high-tx-power")

                            self.low_rx_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.LowRxPower()
                            self.low_rx_power.parent = self
                            self._children_name_map["low_rx_power"] = "low-rx-power"
                            self._children_yang_names.add("low-rx-power")

                            self.low_tx_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.LowTxPower()
                            self.low_tx_power.parent = self
                            self._children_name_map["low_tx_power"] = "low-tx-power"
                            self._children_yang_names.add("low-tx-power")


                        class HighRxPower(Entity):
                            """
                            High Rx Power
                            
                            .. attribute:: counter
                            
                            	Alarm counter
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: is_detected
                            
                            	Is defect detected?
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'controller-optics-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.HighRxPower, self).__init__()

                                self.yang_name = "high-rx-power"
                                self.yang_parent_name = "lane-alarm-info"

                                self.counter = YLeaf(YType.uint32, "counter")

                                self.is_detected = YLeaf(YType.boolean, "is-detected")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("counter",
                                                "is_detected") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.HighRxPower, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.HighRxPower, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.counter.is_set or
                                    self.is_detected.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.counter.yfilter != YFilter.not_set or
                                    self.is_detected.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "high-rx-power" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.counter.is_set or self.counter.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.counter.get_name_leafdata())
                                if (self.is_detected.is_set or self.is_detected.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.is_detected.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "counter" or name == "is-detected"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "counter"):
                                    self.counter = value
                                    self.counter.value_namespace = name_space
                                    self.counter.value_namespace_prefix = name_space_prefix
                                if(value_path == "is-detected"):
                                    self.is_detected = value
                                    self.is_detected.value_namespace = name_space
                                    self.is_detected.value_namespace_prefix = name_space_prefix


                        class LowRxPower(Entity):
                            """
                            Low Rx Power
                            
                            .. attribute:: counter
                            
                            	Alarm counter
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: is_detected
                            
                            	Is defect detected?
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'controller-optics-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.LowRxPower, self).__init__()

                                self.yang_name = "low-rx-power"
                                self.yang_parent_name = "lane-alarm-info"

                                self.counter = YLeaf(YType.uint32, "counter")

                                self.is_detected = YLeaf(YType.boolean, "is-detected")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("counter",
                                                "is_detected") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.LowRxPower, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.LowRxPower, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.counter.is_set or
                                    self.is_detected.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.counter.yfilter != YFilter.not_set or
                                    self.is_detected.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "low-rx-power" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.counter.is_set or self.counter.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.counter.get_name_leafdata())
                                if (self.is_detected.is_set or self.is_detected.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.is_detected.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "counter" or name == "is-detected"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "counter"):
                                    self.counter = value
                                    self.counter.value_namespace = name_space
                                    self.counter.value_namespace_prefix = name_space_prefix
                                if(value_path == "is-detected"):
                                    self.is_detected = value
                                    self.is_detected.value_namespace = name_space
                                    self.is_detected.value_namespace_prefix = name_space_prefix


                        class HighTxPower(Entity):
                            """
                            High Tx Power
                            
                            .. attribute:: counter
                            
                            	Alarm counter
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: is_detected
                            
                            	Is defect detected?
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'controller-optics-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.HighTxPower, self).__init__()

                                self.yang_name = "high-tx-power"
                                self.yang_parent_name = "lane-alarm-info"

                                self.counter = YLeaf(YType.uint32, "counter")

                                self.is_detected = YLeaf(YType.boolean, "is-detected")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("counter",
                                                "is_detected") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.HighTxPower, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.HighTxPower, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.counter.is_set or
                                    self.is_detected.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.counter.yfilter != YFilter.not_set or
                                    self.is_detected.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "high-tx-power" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.counter.is_set or self.counter.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.counter.get_name_leafdata())
                                if (self.is_detected.is_set or self.is_detected.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.is_detected.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "counter" or name == "is-detected"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "counter"):
                                    self.counter = value
                                    self.counter.value_namespace = name_space
                                    self.counter.value_namespace_prefix = name_space_prefix
                                if(value_path == "is-detected"):
                                    self.is_detected = value
                                    self.is_detected.value_namespace = name_space
                                    self.is_detected.value_namespace_prefix = name_space_prefix


                        class LowTxPower(Entity):
                            """
                            Low Tx Power
                            
                            .. attribute:: counter
                            
                            	Alarm counter
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: is_detected
                            
                            	Is defect detected?
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'controller-optics-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.LowTxPower, self).__init__()

                                self.yang_name = "low-tx-power"
                                self.yang_parent_name = "lane-alarm-info"

                                self.counter = YLeaf(YType.uint32, "counter")

                                self.is_detected = YLeaf(YType.boolean, "is-detected")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("counter",
                                                "is_detected") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.LowTxPower, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.LowTxPower, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.counter.is_set or
                                    self.is_detected.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.counter.yfilter != YFilter.not_set or
                                    self.is_detected.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "low-tx-power" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.counter.is_set or self.counter.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.counter.get_name_leafdata())
                                if (self.is_detected.is_set or self.is_detected.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.is_detected.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "counter" or name == "is-detected"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "counter"):
                                    self.counter = value
                                    self.counter.value_namespace = name_space
                                    self.counter.value_namespace_prefix = name_space_prefix
                                if(value_path == "is-detected"):
                                    self.is_detected = value
                                    self.is_detected.value_namespace = name_space
                                    self.is_detected.value_namespace_prefix = name_space_prefix


                        class HighLbc(Entity):
                            """
                            High laser bias current
                            
                            .. attribute:: counter
                            
                            	Alarm counter
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: is_detected
                            
                            	Is defect detected?
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'controller-optics-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.HighLbc, self).__init__()

                                self.yang_name = "high-lbc"
                                self.yang_parent_name = "lane-alarm-info"

                                self.counter = YLeaf(YType.uint32, "counter")

                                self.is_detected = YLeaf(YType.boolean, "is-detected")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("counter",
                                                "is_detected") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.HighLbc, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.HighLbc, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.counter.is_set or
                                    self.is_detected.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.counter.yfilter != YFilter.not_set or
                                    self.is_detected.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "high-lbc" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.counter.is_set or self.counter.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.counter.get_name_leafdata())
                                if (self.is_detected.is_set or self.is_detected.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.is_detected.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "counter" or name == "is-detected"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "counter"):
                                    self.counter = value
                                    self.counter.value_namespace = name_space
                                    self.counter.value_namespace_prefix = name_space_prefix
                                if(value_path == "is-detected"):
                                    self.is_detected = value
                                    self.is_detected.value_namespace = name_space
                                    self.is_detected.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                (self.high_lbc is not None and self.high_lbc.has_data()) or
                                (self.high_rx_power is not None and self.high_rx_power.has_data()) or
                                (self.high_tx_power is not None and self.high_tx_power.has_data()) or
                                (self.low_rx_power is not None and self.low_rx_power.has_data()) or
                                (self.low_tx_power is not None and self.low_tx_power.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                (self.high_lbc is not None and self.high_lbc.has_operation()) or
                                (self.high_rx_power is not None and self.high_rx_power.has_operation()) or
                                (self.high_tx_power is not None and self.high_tx_power.has_operation()) or
                                (self.low_rx_power is not None and self.low_rx_power.has_operation()) or
                                (self.low_tx_power is not None and self.low_tx_power.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "lane-alarm-info" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "high-lbc"):
                                if (self.high_lbc is None):
                                    self.high_lbc = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.HighLbc()
                                    self.high_lbc.parent = self
                                    self._children_name_map["high_lbc"] = "high-lbc"
                                return self.high_lbc

                            if (child_yang_name == "high-rx-power"):
                                if (self.high_rx_power is None):
                                    self.high_rx_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.HighRxPower()
                                    self.high_rx_power.parent = self
                                    self._children_name_map["high_rx_power"] = "high-rx-power"
                                return self.high_rx_power

                            if (child_yang_name == "high-tx-power"):
                                if (self.high_tx_power is None):
                                    self.high_tx_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.HighTxPower()
                                    self.high_tx_power.parent = self
                                    self._children_name_map["high_tx_power"] = "high-tx-power"
                                return self.high_tx_power

                            if (child_yang_name == "low-rx-power"):
                                if (self.low_rx_power is None):
                                    self.low_rx_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.LowRxPower()
                                    self.low_rx_power.parent = self
                                    self._children_name_map["low_rx_power"] = "low-rx-power"
                                return self.low_rx_power

                            if (child_yang_name == "low-tx-power"):
                                if (self.low_tx_power is None):
                                    self.low_tx_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.LowTxPower()
                                    self.low_tx_power.parent = self
                                    self._children_name_map["low_tx_power"] = "low-tx-power"
                                return self.low_tx_power

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "high-lbc" or name == "high-rx-power" or name == "high-tx-power" or name == "low-rx-power" or name == "low-tx-power"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (
                            self.lane_index.is_set or
                            self.laser_bias_current_milli_amps.is_set or
                            self.laser_bias_current_percent.is_set or
                            self.output_frequency.is_set or
                            self.receive_power.is_set or
                            self.receive_signal_power.is_set or
                            self.transmit_power.is_set or
                            self.transmit_signal_power.is_set or
                            (self.lane_alarm_info is not None and self.lane_alarm_info.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.lane_index.yfilter != YFilter.not_set or
                            self.laser_bias_current_milli_amps.yfilter != YFilter.not_set or
                            self.laser_bias_current_percent.yfilter != YFilter.not_set or
                            self.output_frequency.yfilter != YFilter.not_set or
                            self.receive_power.yfilter != YFilter.not_set or
                            self.receive_signal_power.yfilter != YFilter.not_set or
                            self.transmit_power.yfilter != YFilter.not_set or
                            self.transmit_signal_power.yfilter != YFilter.not_set or
                            (self.lane_alarm_info is not None and self.lane_alarm_info.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "lane-data" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.lane_index.is_set or self.lane_index.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.lane_index.get_name_leafdata())
                        if (self.laser_bias_current_milli_amps.is_set or self.laser_bias_current_milli_amps.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.laser_bias_current_milli_amps.get_name_leafdata())
                        if (self.laser_bias_current_percent.is_set or self.laser_bias_current_percent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.laser_bias_current_percent.get_name_leafdata())
                        if (self.output_frequency.is_set or self.output_frequency.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.output_frequency.get_name_leafdata())
                        if (self.receive_power.is_set or self.receive_power.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.receive_power.get_name_leafdata())
                        if (self.receive_signal_power.is_set or self.receive_signal_power.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.receive_signal_power.get_name_leafdata())
                        if (self.transmit_power.is_set or self.transmit_power.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.transmit_power.get_name_leafdata())
                        if (self.transmit_signal_power.is_set or self.transmit_signal_power.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.transmit_signal_power.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "lane-alarm-info"):
                            if (self.lane_alarm_info is None):
                                self.lane_alarm_info = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo()
                                self.lane_alarm_info.parent = self
                                self._children_name_map["lane_alarm_info"] = "lane-alarm-info"
                            return self.lane_alarm_info

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "lane-alarm-info" or name == "lane-index" or name == "laser-bias-current-milli-amps" or name == "laser-bias-current-percent" or name == "output-frequency" or name == "receive-power" or name == "receive-signal-power" or name == "transmit-power" or name == "transmit-signal-power"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "lane-index"):
                            self.lane_index = value
                            self.lane_index.value_namespace = name_space
                            self.lane_index.value_namespace_prefix = name_space_prefix
                        if(value_path == "laser-bias-current-milli-amps"):
                            self.laser_bias_current_milli_amps = value
                            self.laser_bias_current_milli_amps.value_namespace = name_space
                            self.laser_bias_current_milli_amps.value_namespace_prefix = name_space_prefix
                        if(value_path == "laser-bias-current-percent"):
                            self.laser_bias_current_percent = value
                            self.laser_bias_current_percent.value_namespace = name_space
                            self.laser_bias_current_percent.value_namespace_prefix = name_space_prefix
                        if(value_path == "output-frequency"):
                            self.output_frequency = value
                            self.output_frequency.value_namespace = name_space
                            self.output_frequency.value_namespace_prefix = name_space_prefix
                        if(value_path == "receive-power"):
                            self.receive_power = value
                            self.receive_power.value_namespace = name_space
                            self.receive_power.value_namespace_prefix = name_space_prefix
                        if(value_path == "receive-signal-power"):
                            self.receive_signal_power = value
                            self.receive_signal_power.value_namespace = name_space
                            self.receive_signal_power.value_namespace_prefix = name_space_prefix
                        if(value_path == "transmit-power"):
                            self.transmit_power = value
                            self.transmit_power.value_namespace = name_space
                            self.transmit_power.value_namespace_prefix = name_space_prefix
                        if(value_path == "transmit-signal-power"):
                            self.transmit_signal_power = value
                            self.transmit_signal_power.value_namespace = name_space
                            self.transmit_signal_power.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.lane_data:
                        if (c.has_data()):
                            return True
                    return (
                        self.alarm_detected.is_set or
                        self.ampli_channel_power_config_val.is_set or
                        self.ampli_control_mode_config_val.is_set or
                        self.ampli_gain.is_set or
                        self.ampli_gain_config_val.is_set or
                        self.ampli_gain_range_config_val.is_set or
                        self.ampli_gain_thr_deg_high_config_val.is_set or
                        self.ampli_gain_thr_deg_low_config_val.is_set or
                        self.ampli_tilt.is_set or
                        self.ampli_tilt_config_val.is_set or
                        self.cd.is_set or
                        self.cd_configurable.is_set or
                        self.cd_high_threshold.is_set or
                        self.cd_low_threshold.is_set or
                        self.cd_max.is_set or
                        self.cd_min.is_set or
                        self.cfg_tx_power.is_set or
                        self.cfg_tx_power_configurable.is_set or
                        self.channel_power_max_delta_config_val.is_set or
                        self.controller_state.is_set or
                        self.dgd_high_threshold.is_set or
                        self.differential_group_delay.is_set or
                        self.display_volt_temp.is_set or
                        self.dwdm_carrier_band.is_set or
                        self.dwdm_carrier_channel.is_set or
                        self.dwdm_carrier_frequency.is_set or
                        self.dwdm_carrier_wavelength.is_set or
                        self.form_factor.is_set or
                        self.grey_wavelength.is_set or
                        self.is_bo_configured.is_set or
                        self.is_ext_param_valid.is_set or
                        self.laser_state.is_set or
                        self.lbc_high_threshold.is_set or
                        self.lbc_th_high_default.is_set or
                        self.lbc_th_high_warning_default.is_set or
                        self.lbc_th_low_default.is_set or
                        self.lbc_th_low_warning_default.is_set or
                        self.led_state.is_set or
                        self.optical_signal_to_noise_ratio.is_set or
                        self.optics_fec.is_set or
                        self.optics_module.is_set or
                        self.optics_present.is_set or
                        self.optics_type.is_set or
                        self.osnr_low_threshold.is_set or
                        self.osri_config_val.is_set or
                        self.phase_noise.is_set or
                        self.phy_type.is_set or
                        self.pm_enable.is_set or
                        self.polarization_change_rate.is_set or
                        self.polarization_dependent_loss.is_set or
                        self.polarization_mode_dispersion.is_set or
                        self.port_status.is_set or
                        self.port_type.is_set or
                        self.rx_high_threshold.is_set or
                        self.rx_high_warning_threshold.is_set or
                        self.rx_low_threshold.is_set or
                        self.rx_low_warning_threshold.is_set or
                        self.rx_power_th_configurable.is_set or
                        self.rx_voa_attenuation.is_set or
                        self.rx_voa_attenuation_config_val.is_set or
                        self.safety_control_mode_config_val.is_set or
                        self.second_order_polarization_mode_dispersion.is_set or
                        self.temp_high_threshold.is_set or
                        self.temp_high_warning_threshold.is_set or
                        self.temp_low_threshold.is_set or
                        self.temp_low_warning_threshold.is_set or
                        self.temperature.is_set or
                        self.total_rx_power.is_set or
                        self.total_tx_power.is_set or
                        self.transport_admin_state.is_set or
                        self.tx_high_threshold.is_set or
                        self.tx_high_warning_threshold.is_set or
                        self.tx_low_threshold.is_set or
                        self.tx_low_warning_threshold.is_set or
                        self.tx_power_th_configurable.is_set or
                        self.tx_voa_attenuation.is_set or
                        self.tx_voa_attenuation_config_val.is_set or
                        self.volt_high_threshold.is_set or
                        self.volt_high_warning_threshold.is_set or
                        self.volt_low_threshold.is_set or
                        self.volt_low_warning_threshold.is_set or
                        self.voltage.is_set or
                        (self.ext_param_threshold_val is not None and self.ext_param_threshold_val.has_data()) or
                        (self.ext_param_val is not None and self.ext_param_val.has_data()) or
                        (self.network_srlg_info is not None and self.network_srlg_info.has_data()) or
                        (self.optics_alarm_info is not None and self.optics_alarm_info.has_data()) or
                        (self.ots_alarm_info is not None and self.ots_alarm_info.has_data()) or
                        (self.transceiver_info is not None and self.transceiver_info.has_data()))

                def has_operation(self):
                    for c in self.lane_data:
                        if (c.has_operation()):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        self.alarm_detected.yfilter != YFilter.not_set or
                        self.ampli_channel_power_config_val.yfilter != YFilter.not_set or
                        self.ampli_control_mode_config_val.yfilter != YFilter.not_set or
                        self.ampli_gain.yfilter != YFilter.not_set or
                        self.ampli_gain_config_val.yfilter != YFilter.not_set or
                        self.ampli_gain_range_config_val.yfilter != YFilter.not_set or
                        self.ampli_gain_thr_deg_high_config_val.yfilter != YFilter.not_set or
                        self.ampli_gain_thr_deg_low_config_val.yfilter != YFilter.not_set or
                        self.ampli_tilt.yfilter != YFilter.not_set or
                        self.ampli_tilt_config_val.yfilter != YFilter.not_set or
                        self.cd.yfilter != YFilter.not_set or
                        self.cd_configurable.yfilter != YFilter.not_set or
                        self.cd_high_threshold.yfilter != YFilter.not_set or
                        self.cd_low_threshold.yfilter != YFilter.not_set or
                        self.cd_max.yfilter != YFilter.not_set or
                        self.cd_min.yfilter != YFilter.not_set or
                        self.cfg_tx_power.yfilter != YFilter.not_set or
                        self.cfg_tx_power_configurable.yfilter != YFilter.not_set or
                        self.channel_power_max_delta_config_val.yfilter != YFilter.not_set or
                        self.controller_state.yfilter != YFilter.not_set or
                        self.dgd_high_threshold.yfilter != YFilter.not_set or
                        self.differential_group_delay.yfilter != YFilter.not_set or
                        self.display_volt_temp.yfilter != YFilter.not_set or
                        self.dwdm_carrier_band.yfilter != YFilter.not_set or
                        self.dwdm_carrier_channel.yfilter != YFilter.not_set or
                        self.dwdm_carrier_frequency.yfilter != YFilter.not_set or
                        self.dwdm_carrier_wavelength.yfilter != YFilter.not_set or
                        self.form_factor.yfilter != YFilter.not_set or
                        self.grey_wavelength.yfilter != YFilter.not_set or
                        self.is_bo_configured.yfilter != YFilter.not_set or
                        self.is_ext_param_valid.yfilter != YFilter.not_set or
                        self.laser_state.yfilter != YFilter.not_set or
                        self.lbc_high_threshold.yfilter != YFilter.not_set or
                        self.lbc_th_high_default.yfilter != YFilter.not_set or
                        self.lbc_th_high_warning_default.yfilter != YFilter.not_set or
                        self.lbc_th_low_default.yfilter != YFilter.not_set or
                        self.lbc_th_low_warning_default.yfilter != YFilter.not_set or
                        self.led_state.yfilter != YFilter.not_set or
                        self.optical_signal_to_noise_ratio.yfilter != YFilter.not_set or
                        self.optics_fec.yfilter != YFilter.not_set or
                        self.optics_module.yfilter != YFilter.not_set or
                        self.optics_present.yfilter != YFilter.not_set or
                        self.optics_type.yfilter != YFilter.not_set or
                        self.osnr_low_threshold.yfilter != YFilter.not_set or
                        self.osri_config_val.yfilter != YFilter.not_set or
                        self.phase_noise.yfilter != YFilter.not_set or
                        self.phy_type.yfilter != YFilter.not_set or
                        self.pm_enable.yfilter != YFilter.not_set or
                        self.polarization_change_rate.yfilter != YFilter.not_set or
                        self.polarization_dependent_loss.yfilter != YFilter.not_set or
                        self.polarization_mode_dispersion.yfilter != YFilter.not_set or
                        self.port_status.yfilter != YFilter.not_set or
                        self.port_type.yfilter != YFilter.not_set or
                        self.rx_high_threshold.yfilter != YFilter.not_set or
                        self.rx_high_warning_threshold.yfilter != YFilter.not_set or
                        self.rx_low_threshold.yfilter != YFilter.not_set or
                        self.rx_low_warning_threshold.yfilter != YFilter.not_set or
                        self.rx_power_th_configurable.yfilter != YFilter.not_set or
                        self.rx_voa_attenuation.yfilter != YFilter.not_set or
                        self.rx_voa_attenuation_config_val.yfilter != YFilter.not_set or
                        self.safety_control_mode_config_val.yfilter != YFilter.not_set or
                        self.second_order_polarization_mode_dispersion.yfilter != YFilter.not_set or
                        self.temp_high_threshold.yfilter != YFilter.not_set or
                        self.temp_high_warning_threshold.yfilter != YFilter.not_set or
                        self.temp_low_threshold.yfilter != YFilter.not_set or
                        self.temp_low_warning_threshold.yfilter != YFilter.not_set or
                        self.temperature.yfilter != YFilter.not_set or
                        self.total_rx_power.yfilter != YFilter.not_set or
                        self.total_tx_power.yfilter != YFilter.not_set or
                        self.transport_admin_state.yfilter != YFilter.not_set or
                        self.tx_high_threshold.yfilter != YFilter.not_set or
                        self.tx_high_warning_threshold.yfilter != YFilter.not_set or
                        self.tx_low_threshold.yfilter != YFilter.not_set or
                        self.tx_low_warning_threshold.yfilter != YFilter.not_set or
                        self.tx_power_th_configurable.yfilter != YFilter.not_set or
                        self.tx_voa_attenuation.yfilter != YFilter.not_set or
                        self.tx_voa_attenuation_config_val.yfilter != YFilter.not_set or
                        self.volt_high_threshold.yfilter != YFilter.not_set or
                        self.volt_high_warning_threshold.yfilter != YFilter.not_set or
                        self.volt_low_threshold.yfilter != YFilter.not_set or
                        self.volt_low_warning_threshold.yfilter != YFilter.not_set or
                        self.voltage.yfilter != YFilter.not_set or
                        (self.ext_param_threshold_val is not None and self.ext_param_threshold_val.has_operation()) or
                        (self.ext_param_val is not None and self.ext_param_val.has_operation()) or
                        (self.network_srlg_info is not None and self.network_srlg_info.has_operation()) or
                        (self.optics_alarm_info is not None and self.optics_alarm_info.has_operation()) or
                        (self.ots_alarm_info is not None and self.ots_alarm_info.has_operation()) or
                        (self.transceiver_info is not None and self.transceiver_info.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "optics-info" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.alarm_detected.is_set or self.alarm_detected.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.alarm_detected.get_name_leafdata())
                    if (self.ampli_channel_power_config_val.is_set or self.ampli_channel_power_config_val.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ampli_channel_power_config_val.get_name_leafdata())
                    if (self.ampli_control_mode_config_val.is_set or self.ampli_control_mode_config_val.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ampli_control_mode_config_val.get_name_leafdata())
                    if (self.ampli_gain.is_set or self.ampli_gain.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ampli_gain.get_name_leafdata())
                    if (self.ampli_gain_config_val.is_set or self.ampli_gain_config_val.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ampli_gain_config_val.get_name_leafdata())
                    if (self.ampli_gain_range_config_val.is_set or self.ampli_gain_range_config_val.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ampli_gain_range_config_val.get_name_leafdata())
                    if (self.ampli_gain_thr_deg_high_config_val.is_set or self.ampli_gain_thr_deg_high_config_val.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ampli_gain_thr_deg_high_config_val.get_name_leafdata())
                    if (self.ampli_gain_thr_deg_low_config_val.is_set or self.ampli_gain_thr_deg_low_config_val.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ampli_gain_thr_deg_low_config_val.get_name_leafdata())
                    if (self.ampli_tilt.is_set or self.ampli_tilt.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ampli_tilt.get_name_leafdata())
                    if (self.ampli_tilt_config_val.is_set or self.ampli_tilt_config_val.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ampli_tilt_config_val.get_name_leafdata())
                    if (self.cd.is_set or self.cd.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.cd.get_name_leafdata())
                    if (self.cd_configurable.is_set or self.cd_configurable.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.cd_configurable.get_name_leafdata())
                    if (self.cd_high_threshold.is_set or self.cd_high_threshold.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.cd_high_threshold.get_name_leafdata())
                    if (self.cd_low_threshold.is_set or self.cd_low_threshold.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.cd_low_threshold.get_name_leafdata())
                    if (self.cd_max.is_set or self.cd_max.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.cd_max.get_name_leafdata())
                    if (self.cd_min.is_set or self.cd_min.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.cd_min.get_name_leafdata())
                    if (self.cfg_tx_power.is_set or self.cfg_tx_power.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.cfg_tx_power.get_name_leafdata())
                    if (self.cfg_tx_power_configurable.is_set or self.cfg_tx_power_configurable.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.cfg_tx_power_configurable.get_name_leafdata())
                    if (self.channel_power_max_delta_config_val.is_set or self.channel_power_max_delta_config_val.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.channel_power_max_delta_config_val.get_name_leafdata())
                    if (self.controller_state.is_set or self.controller_state.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.controller_state.get_name_leafdata())
                    if (self.dgd_high_threshold.is_set or self.dgd_high_threshold.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.dgd_high_threshold.get_name_leafdata())
                    if (self.differential_group_delay.is_set or self.differential_group_delay.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.differential_group_delay.get_name_leafdata())
                    if (self.display_volt_temp.is_set or self.display_volt_temp.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.display_volt_temp.get_name_leafdata())
                    if (self.dwdm_carrier_band.is_set or self.dwdm_carrier_band.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.dwdm_carrier_band.get_name_leafdata())
                    if (self.dwdm_carrier_channel.is_set or self.dwdm_carrier_channel.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.dwdm_carrier_channel.get_name_leafdata())
                    if (self.dwdm_carrier_frequency.is_set or self.dwdm_carrier_frequency.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.dwdm_carrier_frequency.get_name_leafdata())
                    if (self.dwdm_carrier_wavelength.is_set or self.dwdm_carrier_wavelength.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.dwdm_carrier_wavelength.get_name_leafdata())
                    if (self.form_factor.is_set or self.form_factor.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.form_factor.get_name_leafdata())
                    if (self.grey_wavelength.is_set or self.grey_wavelength.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.grey_wavelength.get_name_leafdata())
                    if (self.is_bo_configured.is_set or self.is_bo_configured.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.is_bo_configured.get_name_leafdata())
                    if (self.is_ext_param_valid.is_set or self.is_ext_param_valid.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.is_ext_param_valid.get_name_leafdata())
                    if (self.laser_state.is_set or self.laser_state.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.laser_state.get_name_leafdata())
                    if (self.lbc_high_threshold.is_set or self.lbc_high_threshold.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.lbc_high_threshold.get_name_leafdata())
                    if (self.lbc_th_high_default.is_set or self.lbc_th_high_default.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.lbc_th_high_default.get_name_leafdata())
                    if (self.lbc_th_high_warning_default.is_set or self.lbc_th_high_warning_default.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.lbc_th_high_warning_default.get_name_leafdata())
                    if (self.lbc_th_low_default.is_set or self.lbc_th_low_default.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.lbc_th_low_default.get_name_leafdata())
                    if (self.lbc_th_low_warning_default.is_set or self.lbc_th_low_warning_default.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.lbc_th_low_warning_default.get_name_leafdata())
                    if (self.led_state.is_set or self.led_state.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.led_state.get_name_leafdata())
                    if (self.optical_signal_to_noise_ratio.is_set or self.optical_signal_to_noise_ratio.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.optical_signal_to_noise_ratio.get_name_leafdata())
                    if (self.optics_fec.is_set or self.optics_fec.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.optics_fec.get_name_leafdata())
                    if (self.optics_module.is_set or self.optics_module.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.optics_module.get_name_leafdata())
                    if (self.optics_present.is_set or self.optics_present.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.optics_present.get_name_leafdata())
                    if (self.optics_type.is_set or self.optics_type.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.optics_type.get_name_leafdata())
                    if (self.osnr_low_threshold.is_set or self.osnr_low_threshold.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.osnr_low_threshold.get_name_leafdata())
                    if (self.osri_config_val.is_set or self.osri_config_val.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.osri_config_val.get_name_leafdata())
                    if (self.phase_noise.is_set or self.phase_noise.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.phase_noise.get_name_leafdata())
                    if (self.phy_type.is_set or self.phy_type.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.phy_type.get_name_leafdata())
                    if (self.pm_enable.is_set or self.pm_enable.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.pm_enable.get_name_leafdata())
                    if (self.polarization_change_rate.is_set or self.polarization_change_rate.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.polarization_change_rate.get_name_leafdata())
                    if (self.polarization_dependent_loss.is_set or self.polarization_dependent_loss.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.polarization_dependent_loss.get_name_leafdata())
                    if (self.polarization_mode_dispersion.is_set or self.polarization_mode_dispersion.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.polarization_mode_dispersion.get_name_leafdata())
                    if (self.port_status.is_set or self.port_status.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.port_status.get_name_leafdata())
                    if (self.port_type.is_set or self.port_type.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.port_type.get_name_leafdata())
                    if (self.rx_high_threshold.is_set or self.rx_high_threshold.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.rx_high_threshold.get_name_leafdata())
                    if (self.rx_high_warning_threshold.is_set or self.rx_high_warning_threshold.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.rx_high_warning_threshold.get_name_leafdata())
                    if (self.rx_low_threshold.is_set or self.rx_low_threshold.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.rx_low_threshold.get_name_leafdata())
                    if (self.rx_low_warning_threshold.is_set or self.rx_low_warning_threshold.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.rx_low_warning_threshold.get_name_leafdata())
                    if (self.rx_power_th_configurable.is_set or self.rx_power_th_configurable.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.rx_power_th_configurable.get_name_leafdata())
                    if (self.rx_voa_attenuation.is_set or self.rx_voa_attenuation.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.rx_voa_attenuation.get_name_leafdata())
                    if (self.rx_voa_attenuation_config_val.is_set or self.rx_voa_attenuation_config_val.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.rx_voa_attenuation_config_val.get_name_leafdata())
                    if (self.safety_control_mode_config_val.is_set or self.safety_control_mode_config_val.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.safety_control_mode_config_val.get_name_leafdata())
                    if (self.second_order_polarization_mode_dispersion.is_set or self.second_order_polarization_mode_dispersion.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.second_order_polarization_mode_dispersion.get_name_leafdata())
                    if (self.temp_high_threshold.is_set or self.temp_high_threshold.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.temp_high_threshold.get_name_leafdata())
                    if (self.temp_high_warning_threshold.is_set or self.temp_high_warning_threshold.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.temp_high_warning_threshold.get_name_leafdata())
                    if (self.temp_low_threshold.is_set or self.temp_low_threshold.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.temp_low_threshold.get_name_leafdata())
                    if (self.temp_low_warning_threshold.is_set or self.temp_low_warning_threshold.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.temp_low_warning_threshold.get_name_leafdata())
                    if (self.temperature.is_set or self.temperature.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.temperature.get_name_leafdata())
                    if (self.total_rx_power.is_set or self.total_rx_power.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.total_rx_power.get_name_leafdata())
                    if (self.total_tx_power.is_set or self.total_tx_power.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.total_tx_power.get_name_leafdata())
                    if (self.transport_admin_state.is_set or self.transport_admin_state.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.transport_admin_state.get_name_leafdata())
                    if (self.tx_high_threshold.is_set or self.tx_high_threshold.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.tx_high_threshold.get_name_leafdata())
                    if (self.tx_high_warning_threshold.is_set or self.tx_high_warning_threshold.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.tx_high_warning_threshold.get_name_leafdata())
                    if (self.tx_low_threshold.is_set or self.tx_low_threshold.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.tx_low_threshold.get_name_leafdata())
                    if (self.tx_low_warning_threshold.is_set or self.tx_low_warning_threshold.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.tx_low_warning_threshold.get_name_leafdata())
                    if (self.tx_power_th_configurable.is_set or self.tx_power_th_configurable.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.tx_power_th_configurable.get_name_leafdata())
                    if (self.tx_voa_attenuation.is_set or self.tx_voa_attenuation.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.tx_voa_attenuation.get_name_leafdata())
                    if (self.tx_voa_attenuation_config_val.is_set or self.tx_voa_attenuation_config_val.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.tx_voa_attenuation_config_val.get_name_leafdata())
                    if (self.volt_high_threshold.is_set or self.volt_high_threshold.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.volt_high_threshold.get_name_leafdata())
                    if (self.volt_high_warning_threshold.is_set or self.volt_high_warning_threshold.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.volt_high_warning_threshold.get_name_leafdata())
                    if (self.volt_low_threshold.is_set or self.volt_low_threshold.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.volt_low_threshold.get_name_leafdata())
                    if (self.volt_low_warning_threshold.is_set or self.volt_low_warning_threshold.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.volt_low_warning_threshold.get_name_leafdata())
                    if (self.voltage.is_set or self.voltage.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.voltage.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "ext-param-threshold-val"):
                        if (self.ext_param_threshold_val is None):
                            self.ext_param_threshold_val = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtParamThresholdVal()
                            self.ext_param_threshold_val.parent = self
                            self._children_name_map["ext_param_threshold_val"] = "ext-param-threshold-val"
                        return self.ext_param_threshold_val

                    if (child_yang_name == "ext-param-val"):
                        if (self.ext_param_val is None):
                            self.ext_param_val = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtParamVal()
                            self.ext_param_val.parent = self
                            self._children_name_map["ext_param_val"] = "ext-param-val"
                        return self.ext_param_val

                    if (child_yang_name == "lane-data"):
                        for c in self.lane_data:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.lane_data.append(c)
                        return c

                    if (child_yang_name == "network-srlg-info"):
                        if (self.network_srlg_info is None):
                            self.network_srlg_info = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.NetworkSrlgInfo()
                            self.network_srlg_info.parent = self
                            self._children_name_map["network_srlg_info"] = "network-srlg-info"
                        return self.network_srlg_info

                    if (child_yang_name == "optics-alarm-info"):
                        if (self.optics_alarm_info is None):
                            self.optics_alarm_info = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo()
                            self.optics_alarm_info.parent = self
                            self._children_name_map["optics_alarm_info"] = "optics-alarm-info"
                        return self.optics_alarm_info

                    if (child_yang_name == "ots-alarm-info"):
                        if (self.ots_alarm_info is None):
                            self.ots_alarm_info = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo()
                            self.ots_alarm_info.parent = self
                            self._children_name_map["ots_alarm_info"] = "ots-alarm-info"
                        return self.ots_alarm_info

                    if (child_yang_name == "transceiver-info"):
                        if (self.transceiver_info is None):
                            self.transceiver_info = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.TransceiverInfo()
                            self.transceiver_info.parent = self
                            self._children_name_map["transceiver_info"] = "transceiver-info"
                        return self.transceiver_info

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "ext-param-threshold-val" or name == "ext-param-val" or name == "lane-data" or name == "network-srlg-info" or name == "optics-alarm-info" or name == "ots-alarm-info" or name == "transceiver-info" or name == "alarm-detected" or name == "ampli-channel-power-config-val" or name == "ampli-control-mode-config-val" or name == "ampli-gain" or name == "ampli-gain-config-val" or name == "ampli-gain-range-config-val" or name == "ampli-gain-thr-deg-high-config-val" or name == "ampli-gain-thr-deg-low-config-val" or name == "ampli-tilt" or name == "ampli-tilt-config-val" or name == "cd" or name == "cd-configurable" or name == "cd-high-threshold" or name == "cd-low-threshold" or name == "cd-max" or name == "cd-min" or name == "cfg-tx-power" or name == "cfg-tx-power-configurable" or name == "channel-power-max-delta-config-val" or name == "controller-state" or name == "dgd-high-threshold" or name == "differential-group-delay" or name == "display-volt-temp" or name == "dwdm-carrier-band" or name == "dwdm-carrier-channel" or name == "dwdm-carrier-frequency" or name == "dwdm-carrier-wavelength" or name == "form-factor" or name == "grey-wavelength" or name == "is-bo-configured" or name == "is-ext-param-valid" or name == "laser-state" or name == "lbc-high-threshold" or name == "lbc-th-high-default" or name == "lbc-th-high-warning-default" or name == "lbc-th-low-default" or name == "lbc-th-low-warning-default" or name == "led-state" or name == "optical-signal-to-noise-ratio" or name == "optics-fec" or name == "optics-module" or name == "optics-present" or name == "optics-type" or name == "osnr-low-threshold" or name == "osri-config-val" or name == "phase-noise" or name == "phy-type" or name == "pm-enable" or name == "polarization-change-rate" or name == "polarization-dependent-loss" or name == "polarization-mode-dispersion" or name == "port-status" or name == "port-type" or name == "rx-high-threshold" or name == "rx-high-warning-threshold" or name == "rx-low-threshold" or name == "rx-low-warning-threshold" or name == "rx-power-th-configurable" or name == "rx-voa-attenuation" or name == "rx-voa-attenuation-config-val" or name == "safety-control-mode-config-val" or name == "second-order-polarization-mode-dispersion" or name == "temp-high-threshold" or name == "temp-high-warning-threshold" or name == "temp-low-threshold" or name == "temp-low-warning-threshold" or name == "temperature" or name == "total-rx-power" or name == "total-tx-power" or name == "transport-admin-state" or name == "tx-high-threshold" or name == "tx-high-warning-threshold" or name == "tx-low-threshold" or name == "tx-low-warning-threshold" or name == "tx-power-th-configurable" or name == "tx-voa-attenuation" or name == "tx-voa-attenuation-config-val" or name == "volt-high-threshold" or name == "volt-high-warning-threshold" or name == "volt-low-threshold" or name == "volt-low-warning-threshold" or name == "voltage"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "alarm-detected"):
                        self.alarm_detected = value
                        self.alarm_detected.value_namespace = name_space
                        self.alarm_detected.value_namespace_prefix = name_space_prefix
                    if(value_path == "ampli-channel-power-config-val"):
                        self.ampli_channel_power_config_val = value
                        self.ampli_channel_power_config_val.value_namespace = name_space
                        self.ampli_channel_power_config_val.value_namespace_prefix = name_space_prefix
                    if(value_path == "ampli-control-mode-config-val"):
                        self.ampli_control_mode_config_val = value
                        self.ampli_control_mode_config_val.value_namespace = name_space
                        self.ampli_control_mode_config_val.value_namespace_prefix = name_space_prefix
                    if(value_path == "ampli-gain"):
                        self.ampli_gain = value
                        self.ampli_gain.value_namespace = name_space
                        self.ampli_gain.value_namespace_prefix = name_space_prefix
                    if(value_path == "ampli-gain-config-val"):
                        self.ampli_gain_config_val = value
                        self.ampli_gain_config_val.value_namespace = name_space
                        self.ampli_gain_config_val.value_namespace_prefix = name_space_prefix
                    if(value_path == "ampli-gain-range-config-val"):
                        self.ampli_gain_range_config_val = value
                        self.ampli_gain_range_config_val.value_namespace = name_space
                        self.ampli_gain_range_config_val.value_namespace_prefix = name_space_prefix
                    if(value_path == "ampli-gain-thr-deg-high-config-val"):
                        self.ampli_gain_thr_deg_high_config_val = value
                        self.ampli_gain_thr_deg_high_config_val.value_namespace = name_space
                        self.ampli_gain_thr_deg_high_config_val.value_namespace_prefix = name_space_prefix
                    if(value_path == "ampli-gain-thr-deg-low-config-val"):
                        self.ampli_gain_thr_deg_low_config_val = value
                        self.ampli_gain_thr_deg_low_config_val.value_namespace = name_space
                        self.ampli_gain_thr_deg_low_config_val.value_namespace_prefix = name_space_prefix
                    if(value_path == "ampli-tilt"):
                        self.ampli_tilt = value
                        self.ampli_tilt.value_namespace = name_space
                        self.ampli_tilt.value_namespace_prefix = name_space_prefix
                    if(value_path == "ampli-tilt-config-val"):
                        self.ampli_tilt_config_val = value
                        self.ampli_tilt_config_val.value_namespace = name_space
                        self.ampli_tilt_config_val.value_namespace_prefix = name_space_prefix
                    if(value_path == "cd"):
                        self.cd = value
                        self.cd.value_namespace = name_space
                        self.cd.value_namespace_prefix = name_space_prefix
                    if(value_path == "cd-configurable"):
                        self.cd_configurable = value
                        self.cd_configurable.value_namespace = name_space
                        self.cd_configurable.value_namespace_prefix = name_space_prefix
                    if(value_path == "cd-high-threshold"):
                        self.cd_high_threshold = value
                        self.cd_high_threshold.value_namespace = name_space
                        self.cd_high_threshold.value_namespace_prefix = name_space_prefix
                    if(value_path == "cd-low-threshold"):
                        self.cd_low_threshold = value
                        self.cd_low_threshold.value_namespace = name_space
                        self.cd_low_threshold.value_namespace_prefix = name_space_prefix
                    if(value_path == "cd-max"):
                        self.cd_max = value
                        self.cd_max.value_namespace = name_space
                        self.cd_max.value_namespace_prefix = name_space_prefix
                    if(value_path == "cd-min"):
                        self.cd_min = value
                        self.cd_min.value_namespace = name_space
                        self.cd_min.value_namespace_prefix = name_space_prefix
                    if(value_path == "cfg-tx-power"):
                        self.cfg_tx_power = value
                        self.cfg_tx_power.value_namespace = name_space
                        self.cfg_tx_power.value_namespace_prefix = name_space_prefix
                    if(value_path == "cfg-tx-power-configurable"):
                        self.cfg_tx_power_configurable = value
                        self.cfg_tx_power_configurable.value_namespace = name_space
                        self.cfg_tx_power_configurable.value_namespace_prefix = name_space_prefix
                    if(value_path == "channel-power-max-delta-config-val"):
                        self.channel_power_max_delta_config_val = value
                        self.channel_power_max_delta_config_val.value_namespace = name_space
                        self.channel_power_max_delta_config_val.value_namespace_prefix = name_space_prefix
                    if(value_path == "controller-state"):
                        self.controller_state = value
                        self.controller_state.value_namespace = name_space
                        self.controller_state.value_namespace_prefix = name_space_prefix
                    if(value_path == "dgd-high-threshold"):
                        self.dgd_high_threshold = value
                        self.dgd_high_threshold.value_namespace = name_space
                        self.dgd_high_threshold.value_namespace_prefix = name_space_prefix
                    if(value_path == "differential-group-delay"):
                        self.differential_group_delay = value
                        self.differential_group_delay.value_namespace = name_space
                        self.differential_group_delay.value_namespace_prefix = name_space_prefix
                    if(value_path == "display-volt-temp"):
                        self.display_volt_temp = value
                        self.display_volt_temp.value_namespace = name_space
                        self.display_volt_temp.value_namespace_prefix = name_space_prefix
                    if(value_path == "dwdm-carrier-band"):
                        self.dwdm_carrier_band = value
                        self.dwdm_carrier_band.value_namespace = name_space
                        self.dwdm_carrier_band.value_namespace_prefix = name_space_prefix
                    if(value_path == "dwdm-carrier-channel"):
                        self.dwdm_carrier_channel = value
                        self.dwdm_carrier_channel.value_namespace = name_space
                        self.dwdm_carrier_channel.value_namespace_prefix = name_space_prefix
                    if(value_path == "dwdm-carrier-frequency"):
                        self.dwdm_carrier_frequency = value
                        self.dwdm_carrier_frequency.value_namespace = name_space
                        self.dwdm_carrier_frequency.value_namespace_prefix = name_space_prefix
                    if(value_path == "dwdm-carrier-wavelength"):
                        self.dwdm_carrier_wavelength = value
                        self.dwdm_carrier_wavelength.value_namespace = name_space
                        self.dwdm_carrier_wavelength.value_namespace_prefix = name_space_prefix
                    if(value_path == "form-factor"):
                        self.form_factor = value
                        self.form_factor.value_namespace = name_space
                        self.form_factor.value_namespace_prefix = name_space_prefix
                    if(value_path == "grey-wavelength"):
                        self.grey_wavelength = value
                        self.grey_wavelength.value_namespace = name_space
                        self.grey_wavelength.value_namespace_prefix = name_space_prefix
                    if(value_path == "is-bo-configured"):
                        self.is_bo_configured = value
                        self.is_bo_configured.value_namespace = name_space
                        self.is_bo_configured.value_namespace_prefix = name_space_prefix
                    if(value_path == "is-ext-param-valid"):
                        self.is_ext_param_valid = value
                        self.is_ext_param_valid.value_namespace = name_space
                        self.is_ext_param_valid.value_namespace_prefix = name_space_prefix
                    if(value_path == "laser-state"):
                        self.laser_state = value
                        self.laser_state.value_namespace = name_space
                        self.laser_state.value_namespace_prefix = name_space_prefix
                    if(value_path == "lbc-high-threshold"):
                        self.lbc_high_threshold = value
                        self.lbc_high_threshold.value_namespace = name_space
                        self.lbc_high_threshold.value_namespace_prefix = name_space_prefix
                    if(value_path == "lbc-th-high-default"):
                        self.lbc_th_high_default = value
                        self.lbc_th_high_default.value_namespace = name_space
                        self.lbc_th_high_default.value_namespace_prefix = name_space_prefix
                    if(value_path == "lbc-th-high-warning-default"):
                        self.lbc_th_high_warning_default = value
                        self.lbc_th_high_warning_default.value_namespace = name_space
                        self.lbc_th_high_warning_default.value_namespace_prefix = name_space_prefix
                    if(value_path == "lbc-th-low-default"):
                        self.lbc_th_low_default = value
                        self.lbc_th_low_default.value_namespace = name_space
                        self.lbc_th_low_default.value_namespace_prefix = name_space_prefix
                    if(value_path == "lbc-th-low-warning-default"):
                        self.lbc_th_low_warning_default = value
                        self.lbc_th_low_warning_default.value_namespace = name_space
                        self.lbc_th_low_warning_default.value_namespace_prefix = name_space_prefix
                    if(value_path == "led-state"):
                        self.led_state = value
                        self.led_state.value_namespace = name_space
                        self.led_state.value_namespace_prefix = name_space_prefix
                    if(value_path == "optical-signal-to-noise-ratio"):
                        self.optical_signal_to_noise_ratio = value
                        self.optical_signal_to_noise_ratio.value_namespace = name_space
                        self.optical_signal_to_noise_ratio.value_namespace_prefix = name_space_prefix
                    if(value_path == "optics-fec"):
                        self.optics_fec = value
                        self.optics_fec.value_namespace = name_space
                        self.optics_fec.value_namespace_prefix = name_space_prefix
                    if(value_path == "optics-module"):
                        self.optics_module = value
                        self.optics_module.value_namespace = name_space
                        self.optics_module.value_namespace_prefix = name_space_prefix
                    if(value_path == "optics-present"):
                        self.optics_present = value
                        self.optics_present.value_namespace = name_space
                        self.optics_present.value_namespace_prefix = name_space_prefix
                    if(value_path == "optics-type"):
                        self.optics_type = value
                        self.optics_type.value_namespace = name_space
                        self.optics_type.value_namespace_prefix = name_space_prefix
                    if(value_path == "osnr-low-threshold"):
                        self.osnr_low_threshold = value
                        self.osnr_low_threshold.value_namespace = name_space
                        self.osnr_low_threshold.value_namespace_prefix = name_space_prefix
                    if(value_path == "osri-config-val"):
                        self.osri_config_val = value
                        self.osri_config_val.value_namespace = name_space
                        self.osri_config_val.value_namespace_prefix = name_space_prefix
                    if(value_path == "phase-noise"):
                        self.phase_noise = value
                        self.phase_noise.value_namespace = name_space
                        self.phase_noise.value_namespace_prefix = name_space_prefix
                    if(value_path == "phy-type"):
                        self.phy_type = value
                        self.phy_type.value_namespace = name_space
                        self.phy_type.value_namespace_prefix = name_space_prefix
                    if(value_path == "pm-enable"):
                        self.pm_enable = value
                        self.pm_enable.value_namespace = name_space
                        self.pm_enable.value_namespace_prefix = name_space_prefix
                    if(value_path == "polarization-change-rate"):
                        self.polarization_change_rate = value
                        self.polarization_change_rate.value_namespace = name_space
                        self.polarization_change_rate.value_namespace_prefix = name_space_prefix
                    if(value_path == "polarization-dependent-loss"):
                        self.polarization_dependent_loss = value
                        self.polarization_dependent_loss.value_namespace = name_space
                        self.polarization_dependent_loss.value_namespace_prefix = name_space_prefix
                    if(value_path == "polarization-mode-dispersion"):
                        self.polarization_mode_dispersion = value
                        self.polarization_mode_dispersion.value_namespace = name_space
                        self.polarization_mode_dispersion.value_namespace_prefix = name_space_prefix
                    if(value_path == "port-status"):
                        self.port_status = value
                        self.port_status.value_namespace = name_space
                        self.port_status.value_namespace_prefix = name_space_prefix
                    if(value_path == "port-type"):
                        self.port_type = value
                        self.port_type.value_namespace = name_space
                        self.port_type.value_namespace_prefix = name_space_prefix
                    if(value_path == "rx-high-threshold"):
                        self.rx_high_threshold = value
                        self.rx_high_threshold.value_namespace = name_space
                        self.rx_high_threshold.value_namespace_prefix = name_space_prefix
                    if(value_path == "rx-high-warning-threshold"):
                        self.rx_high_warning_threshold = value
                        self.rx_high_warning_threshold.value_namespace = name_space
                        self.rx_high_warning_threshold.value_namespace_prefix = name_space_prefix
                    if(value_path == "rx-low-threshold"):
                        self.rx_low_threshold = value
                        self.rx_low_threshold.value_namespace = name_space
                        self.rx_low_threshold.value_namespace_prefix = name_space_prefix
                    if(value_path == "rx-low-warning-threshold"):
                        self.rx_low_warning_threshold = value
                        self.rx_low_warning_threshold.value_namespace = name_space
                        self.rx_low_warning_threshold.value_namespace_prefix = name_space_prefix
                    if(value_path == "rx-power-th-configurable"):
                        self.rx_power_th_configurable = value
                        self.rx_power_th_configurable.value_namespace = name_space
                        self.rx_power_th_configurable.value_namespace_prefix = name_space_prefix
                    if(value_path == "rx-voa-attenuation"):
                        self.rx_voa_attenuation = value
                        self.rx_voa_attenuation.value_namespace = name_space
                        self.rx_voa_attenuation.value_namespace_prefix = name_space_prefix
                    if(value_path == "rx-voa-attenuation-config-val"):
                        self.rx_voa_attenuation_config_val = value
                        self.rx_voa_attenuation_config_val.value_namespace = name_space
                        self.rx_voa_attenuation_config_val.value_namespace_prefix = name_space_prefix
                    if(value_path == "safety-control-mode-config-val"):
                        self.safety_control_mode_config_val = value
                        self.safety_control_mode_config_val.value_namespace = name_space
                        self.safety_control_mode_config_val.value_namespace_prefix = name_space_prefix
                    if(value_path == "second-order-polarization-mode-dispersion"):
                        self.second_order_polarization_mode_dispersion = value
                        self.second_order_polarization_mode_dispersion.value_namespace = name_space
                        self.second_order_polarization_mode_dispersion.value_namespace_prefix = name_space_prefix
                    if(value_path == "temp-high-threshold"):
                        self.temp_high_threshold = value
                        self.temp_high_threshold.value_namespace = name_space
                        self.temp_high_threshold.value_namespace_prefix = name_space_prefix
                    if(value_path == "temp-high-warning-threshold"):
                        self.temp_high_warning_threshold = value
                        self.temp_high_warning_threshold.value_namespace = name_space
                        self.temp_high_warning_threshold.value_namespace_prefix = name_space_prefix
                    if(value_path == "temp-low-threshold"):
                        self.temp_low_threshold = value
                        self.temp_low_threshold.value_namespace = name_space
                        self.temp_low_threshold.value_namespace_prefix = name_space_prefix
                    if(value_path == "temp-low-warning-threshold"):
                        self.temp_low_warning_threshold = value
                        self.temp_low_warning_threshold.value_namespace = name_space
                        self.temp_low_warning_threshold.value_namespace_prefix = name_space_prefix
                    if(value_path == "temperature"):
                        self.temperature = value
                        self.temperature.value_namespace = name_space
                        self.temperature.value_namespace_prefix = name_space_prefix
                    if(value_path == "total-rx-power"):
                        self.total_rx_power = value
                        self.total_rx_power.value_namespace = name_space
                        self.total_rx_power.value_namespace_prefix = name_space_prefix
                    if(value_path == "total-tx-power"):
                        self.total_tx_power = value
                        self.total_tx_power.value_namespace = name_space
                        self.total_tx_power.value_namespace_prefix = name_space_prefix
                    if(value_path == "transport-admin-state"):
                        self.transport_admin_state = value
                        self.transport_admin_state.value_namespace = name_space
                        self.transport_admin_state.value_namespace_prefix = name_space_prefix
                    if(value_path == "tx-high-threshold"):
                        self.tx_high_threshold = value
                        self.tx_high_threshold.value_namespace = name_space
                        self.tx_high_threshold.value_namespace_prefix = name_space_prefix
                    if(value_path == "tx-high-warning-threshold"):
                        self.tx_high_warning_threshold = value
                        self.tx_high_warning_threshold.value_namespace = name_space
                        self.tx_high_warning_threshold.value_namespace_prefix = name_space_prefix
                    if(value_path == "tx-low-threshold"):
                        self.tx_low_threshold = value
                        self.tx_low_threshold.value_namespace = name_space
                        self.tx_low_threshold.value_namespace_prefix = name_space_prefix
                    if(value_path == "tx-low-warning-threshold"):
                        self.tx_low_warning_threshold = value
                        self.tx_low_warning_threshold.value_namespace = name_space
                        self.tx_low_warning_threshold.value_namespace_prefix = name_space_prefix
                    if(value_path == "tx-power-th-configurable"):
                        self.tx_power_th_configurable = value
                        self.tx_power_th_configurable.value_namespace = name_space
                        self.tx_power_th_configurable.value_namespace_prefix = name_space_prefix
                    if(value_path == "tx-voa-attenuation"):
                        self.tx_voa_attenuation = value
                        self.tx_voa_attenuation.value_namespace = name_space
                        self.tx_voa_attenuation.value_namespace_prefix = name_space_prefix
                    if(value_path == "tx-voa-attenuation-config-val"):
                        self.tx_voa_attenuation_config_val = value
                        self.tx_voa_attenuation_config_val.value_namespace = name_space
                        self.tx_voa_attenuation_config_val.value_namespace_prefix = name_space_prefix
                    if(value_path == "volt-high-threshold"):
                        self.volt_high_threshold = value
                        self.volt_high_threshold.value_namespace = name_space
                        self.volt_high_threshold.value_namespace_prefix = name_space_prefix
                    if(value_path == "volt-high-warning-threshold"):
                        self.volt_high_warning_threshold = value
                        self.volt_high_warning_threshold.value_namespace = name_space
                        self.volt_high_warning_threshold.value_namespace_prefix = name_space_prefix
                    if(value_path == "volt-low-threshold"):
                        self.volt_low_threshold = value
                        self.volt_low_threshold.value_namespace = name_space
                        self.volt_low_threshold.value_namespace_prefix = name_space_prefix
                    if(value_path == "volt-low-warning-threshold"):
                        self.volt_low_warning_threshold = value
                        self.volt_low_warning_threshold.value_namespace = name_space
                        self.volt_low_warning_threshold.value_namespace_prefix = name_space_prefix
                    if(value_path == "voltage"):
                        self.voltage = value
                        self.voltage.value_namespace = name_space
                        self.voltage.value_namespace_prefix = name_space_prefix


            class OpticsLanes(Entity):
                """
                All Optics Port operational data
                
                .. attribute:: optics_lane
                
                	Lane Information
                	**type**\: list of    :py:class:`OpticsLane <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane>`
                
                

                """

                _prefix = 'controller-optics-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(OpticsOper.OpticsPorts.OpticsPort.OpticsLanes, self).__init__()

                    self.yang_name = "optics-lanes"
                    self.yang_parent_name = "optics-port"

                    self.optics_lane = YList(self)

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
                                super(OpticsOper.OpticsPorts.OpticsPort.OpticsLanes, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsLanes, self).__setattr__(name, value)


                class OpticsLane(Entity):
                    """
                    Lane Information
                    
                    .. attribute:: number  <key>
                    
                    	Lane Index
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: lane_alarm_info
                    
                    	Lane Alarm Information
                    	**type**\:   :py:class:`LaneAlarmInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo>`
                    
                    .. attribute:: lane_index
                    
                    	The index number of the lane
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: laser_bias_current_milli_amps
                    
                    	Laser Bias Current in units of 0.01mA
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: laser_bias_current_percent
                    
                    	Laser Bias Current in units of 0.01 percentage
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: percentage
                    
                    .. attribute:: output_frequency
                    
                    	Output frequency read from hw in the unit 0 .01THz
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: receive_power
                    
                    	Transponder receive power in the unit of 0.01dBm
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: receive_signal_power
                    
                    	Transponder receive signal power in the unit of 0.01dBm
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: transmit_power
                    
                    	Transmit power in the unit of 0.01dBm
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: transmit_signal_power
                    
                    	Transmit Signal power in the unit of 0.01dBm
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    

                    """

                    _prefix = 'controller-optics-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane, self).__init__()

                        self.yang_name = "optics-lane"
                        self.yang_parent_name = "optics-lanes"

                        self.number = YLeaf(YType.int32, "number")

                        self.lane_index = YLeaf(YType.uint32, "lane-index")

                        self.laser_bias_current_milli_amps = YLeaf(YType.uint32, "laser-bias-current-milli-amps")

                        self.laser_bias_current_percent = YLeaf(YType.uint32, "laser-bias-current-percent")

                        self.output_frequency = YLeaf(YType.int32, "output-frequency")

                        self.receive_power = YLeaf(YType.int32, "receive-power")

                        self.receive_signal_power = YLeaf(YType.int32, "receive-signal-power")

                        self.transmit_power = YLeaf(YType.int32, "transmit-power")

                        self.transmit_signal_power = YLeaf(YType.int32, "transmit-signal-power")

                        self.lane_alarm_info = OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo()
                        self.lane_alarm_info.parent = self
                        self._children_name_map["lane_alarm_info"] = "lane-alarm-info"
                        self._children_yang_names.add("lane-alarm-info")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("number",
                                        "lane_index",
                                        "laser_bias_current_milli_amps",
                                        "laser_bias_current_percent",
                                        "output_frequency",
                                        "receive_power",
                                        "receive_signal_power",
                                        "transmit_power",
                                        "transmit_signal_power") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane, self).__setattr__(name, value)


                    class LaneAlarmInfo(Entity):
                        """
                        Lane Alarm Information
                        
                        .. attribute:: high_lbc
                        
                        	High laser bias current
                        	**type**\:   :py:class:`HighLbc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.HighLbc>`
                        
                        .. attribute:: high_rx_power
                        
                        	High Rx Power
                        	**type**\:   :py:class:`HighRxPower <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.HighRxPower>`
                        
                        .. attribute:: high_tx_power
                        
                        	High Tx Power
                        	**type**\:   :py:class:`HighTxPower <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.HighTxPower>`
                        
                        .. attribute:: low_rx_power
                        
                        	Low Rx Power
                        	**type**\:   :py:class:`LowRxPower <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.LowRxPower>`
                        
                        .. attribute:: low_tx_power
                        
                        	Low Tx Power
                        	**type**\:   :py:class:`LowTxPower <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.LowTxPower>`
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo, self).__init__()

                            self.yang_name = "lane-alarm-info"
                            self.yang_parent_name = "optics-lane"

                            self.high_lbc = OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.HighLbc()
                            self.high_lbc.parent = self
                            self._children_name_map["high_lbc"] = "high-lbc"
                            self._children_yang_names.add("high-lbc")

                            self.high_rx_power = OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.HighRxPower()
                            self.high_rx_power.parent = self
                            self._children_name_map["high_rx_power"] = "high-rx-power"
                            self._children_yang_names.add("high-rx-power")

                            self.high_tx_power = OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.HighTxPower()
                            self.high_tx_power.parent = self
                            self._children_name_map["high_tx_power"] = "high-tx-power"
                            self._children_yang_names.add("high-tx-power")

                            self.low_rx_power = OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.LowRxPower()
                            self.low_rx_power.parent = self
                            self._children_name_map["low_rx_power"] = "low-rx-power"
                            self._children_yang_names.add("low-rx-power")

                            self.low_tx_power = OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.LowTxPower()
                            self.low_tx_power.parent = self
                            self._children_name_map["low_tx_power"] = "low-tx-power"
                            self._children_yang_names.add("low-tx-power")


                        class HighRxPower(Entity):
                            """
                            High Rx Power
                            
                            .. attribute:: counter
                            
                            	Alarm counter
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: is_detected
                            
                            	Is defect detected?
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'controller-optics-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.HighRxPower, self).__init__()

                                self.yang_name = "high-rx-power"
                                self.yang_parent_name = "lane-alarm-info"

                                self.counter = YLeaf(YType.uint32, "counter")

                                self.is_detected = YLeaf(YType.boolean, "is-detected")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("counter",
                                                "is_detected") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.HighRxPower, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.HighRxPower, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.counter.is_set or
                                    self.is_detected.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.counter.yfilter != YFilter.not_set or
                                    self.is_detected.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "high-rx-power" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.counter.is_set or self.counter.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.counter.get_name_leafdata())
                                if (self.is_detected.is_set or self.is_detected.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.is_detected.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "counter" or name == "is-detected"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "counter"):
                                    self.counter = value
                                    self.counter.value_namespace = name_space
                                    self.counter.value_namespace_prefix = name_space_prefix
                                if(value_path == "is-detected"):
                                    self.is_detected = value
                                    self.is_detected.value_namespace = name_space
                                    self.is_detected.value_namespace_prefix = name_space_prefix


                        class LowRxPower(Entity):
                            """
                            Low Rx Power
                            
                            .. attribute:: counter
                            
                            	Alarm counter
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: is_detected
                            
                            	Is defect detected?
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'controller-optics-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.LowRxPower, self).__init__()

                                self.yang_name = "low-rx-power"
                                self.yang_parent_name = "lane-alarm-info"

                                self.counter = YLeaf(YType.uint32, "counter")

                                self.is_detected = YLeaf(YType.boolean, "is-detected")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("counter",
                                                "is_detected") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.LowRxPower, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.LowRxPower, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.counter.is_set or
                                    self.is_detected.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.counter.yfilter != YFilter.not_set or
                                    self.is_detected.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "low-rx-power" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.counter.is_set or self.counter.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.counter.get_name_leafdata())
                                if (self.is_detected.is_set or self.is_detected.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.is_detected.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "counter" or name == "is-detected"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "counter"):
                                    self.counter = value
                                    self.counter.value_namespace = name_space
                                    self.counter.value_namespace_prefix = name_space_prefix
                                if(value_path == "is-detected"):
                                    self.is_detected = value
                                    self.is_detected.value_namespace = name_space
                                    self.is_detected.value_namespace_prefix = name_space_prefix


                        class HighTxPower(Entity):
                            """
                            High Tx Power
                            
                            .. attribute:: counter
                            
                            	Alarm counter
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: is_detected
                            
                            	Is defect detected?
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'controller-optics-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.HighTxPower, self).__init__()

                                self.yang_name = "high-tx-power"
                                self.yang_parent_name = "lane-alarm-info"

                                self.counter = YLeaf(YType.uint32, "counter")

                                self.is_detected = YLeaf(YType.boolean, "is-detected")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("counter",
                                                "is_detected") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.HighTxPower, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.HighTxPower, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.counter.is_set or
                                    self.is_detected.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.counter.yfilter != YFilter.not_set or
                                    self.is_detected.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "high-tx-power" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.counter.is_set or self.counter.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.counter.get_name_leafdata())
                                if (self.is_detected.is_set or self.is_detected.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.is_detected.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "counter" or name == "is-detected"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "counter"):
                                    self.counter = value
                                    self.counter.value_namespace = name_space
                                    self.counter.value_namespace_prefix = name_space_prefix
                                if(value_path == "is-detected"):
                                    self.is_detected = value
                                    self.is_detected.value_namespace = name_space
                                    self.is_detected.value_namespace_prefix = name_space_prefix


                        class LowTxPower(Entity):
                            """
                            Low Tx Power
                            
                            .. attribute:: counter
                            
                            	Alarm counter
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: is_detected
                            
                            	Is defect detected?
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'controller-optics-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.LowTxPower, self).__init__()

                                self.yang_name = "low-tx-power"
                                self.yang_parent_name = "lane-alarm-info"

                                self.counter = YLeaf(YType.uint32, "counter")

                                self.is_detected = YLeaf(YType.boolean, "is-detected")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("counter",
                                                "is_detected") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.LowTxPower, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.LowTxPower, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.counter.is_set or
                                    self.is_detected.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.counter.yfilter != YFilter.not_set or
                                    self.is_detected.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "low-tx-power" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.counter.is_set or self.counter.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.counter.get_name_leafdata())
                                if (self.is_detected.is_set or self.is_detected.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.is_detected.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "counter" or name == "is-detected"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "counter"):
                                    self.counter = value
                                    self.counter.value_namespace = name_space
                                    self.counter.value_namespace_prefix = name_space_prefix
                                if(value_path == "is-detected"):
                                    self.is_detected = value
                                    self.is_detected.value_namespace = name_space
                                    self.is_detected.value_namespace_prefix = name_space_prefix


                        class HighLbc(Entity):
                            """
                            High laser bias current
                            
                            .. attribute:: counter
                            
                            	Alarm counter
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: is_detected
                            
                            	Is defect detected?
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'controller-optics-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.HighLbc, self).__init__()

                                self.yang_name = "high-lbc"
                                self.yang_parent_name = "lane-alarm-info"

                                self.counter = YLeaf(YType.uint32, "counter")

                                self.is_detected = YLeaf(YType.boolean, "is-detected")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("counter",
                                                "is_detected") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.HighLbc, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.HighLbc, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.counter.is_set or
                                    self.is_detected.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.counter.yfilter != YFilter.not_set or
                                    self.is_detected.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "high-lbc" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.counter.is_set or self.counter.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.counter.get_name_leafdata())
                                if (self.is_detected.is_set or self.is_detected.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.is_detected.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "counter" or name == "is-detected"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "counter"):
                                    self.counter = value
                                    self.counter.value_namespace = name_space
                                    self.counter.value_namespace_prefix = name_space_prefix
                                if(value_path == "is-detected"):
                                    self.is_detected = value
                                    self.is_detected.value_namespace = name_space
                                    self.is_detected.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                (self.high_lbc is not None and self.high_lbc.has_data()) or
                                (self.high_rx_power is not None and self.high_rx_power.has_data()) or
                                (self.high_tx_power is not None and self.high_tx_power.has_data()) or
                                (self.low_rx_power is not None and self.low_rx_power.has_data()) or
                                (self.low_tx_power is not None and self.low_tx_power.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                (self.high_lbc is not None and self.high_lbc.has_operation()) or
                                (self.high_rx_power is not None and self.high_rx_power.has_operation()) or
                                (self.high_tx_power is not None and self.high_tx_power.has_operation()) or
                                (self.low_rx_power is not None and self.low_rx_power.has_operation()) or
                                (self.low_tx_power is not None and self.low_tx_power.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "lane-alarm-info" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "high-lbc"):
                                if (self.high_lbc is None):
                                    self.high_lbc = OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.HighLbc()
                                    self.high_lbc.parent = self
                                    self._children_name_map["high_lbc"] = "high-lbc"
                                return self.high_lbc

                            if (child_yang_name == "high-rx-power"):
                                if (self.high_rx_power is None):
                                    self.high_rx_power = OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.HighRxPower()
                                    self.high_rx_power.parent = self
                                    self._children_name_map["high_rx_power"] = "high-rx-power"
                                return self.high_rx_power

                            if (child_yang_name == "high-tx-power"):
                                if (self.high_tx_power is None):
                                    self.high_tx_power = OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.HighTxPower()
                                    self.high_tx_power.parent = self
                                    self._children_name_map["high_tx_power"] = "high-tx-power"
                                return self.high_tx_power

                            if (child_yang_name == "low-rx-power"):
                                if (self.low_rx_power is None):
                                    self.low_rx_power = OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.LowRxPower()
                                    self.low_rx_power.parent = self
                                    self._children_name_map["low_rx_power"] = "low-rx-power"
                                return self.low_rx_power

                            if (child_yang_name == "low-tx-power"):
                                if (self.low_tx_power is None):
                                    self.low_tx_power = OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.LowTxPower()
                                    self.low_tx_power.parent = self
                                    self._children_name_map["low_tx_power"] = "low-tx-power"
                                return self.low_tx_power

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "high-lbc" or name == "high-rx-power" or name == "high-tx-power" or name == "low-rx-power" or name == "low-tx-power"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (
                            self.number.is_set or
                            self.lane_index.is_set or
                            self.laser_bias_current_milli_amps.is_set or
                            self.laser_bias_current_percent.is_set or
                            self.output_frequency.is_set or
                            self.receive_power.is_set or
                            self.receive_signal_power.is_set or
                            self.transmit_power.is_set or
                            self.transmit_signal_power.is_set or
                            (self.lane_alarm_info is not None and self.lane_alarm_info.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.number.yfilter != YFilter.not_set or
                            self.lane_index.yfilter != YFilter.not_set or
                            self.laser_bias_current_milli_amps.yfilter != YFilter.not_set or
                            self.laser_bias_current_percent.yfilter != YFilter.not_set or
                            self.output_frequency.yfilter != YFilter.not_set or
                            self.receive_power.yfilter != YFilter.not_set or
                            self.receive_signal_power.yfilter != YFilter.not_set or
                            self.transmit_power.yfilter != YFilter.not_set or
                            self.transmit_signal_power.yfilter != YFilter.not_set or
                            (self.lane_alarm_info is not None and self.lane_alarm_info.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "optics-lane" + "[number='" + self.number.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.number.is_set or self.number.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.number.get_name_leafdata())
                        if (self.lane_index.is_set or self.lane_index.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.lane_index.get_name_leafdata())
                        if (self.laser_bias_current_milli_amps.is_set or self.laser_bias_current_milli_amps.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.laser_bias_current_milli_amps.get_name_leafdata())
                        if (self.laser_bias_current_percent.is_set or self.laser_bias_current_percent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.laser_bias_current_percent.get_name_leafdata())
                        if (self.output_frequency.is_set or self.output_frequency.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.output_frequency.get_name_leafdata())
                        if (self.receive_power.is_set or self.receive_power.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.receive_power.get_name_leafdata())
                        if (self.receive_signal_power.is_set or self.receive_signal_power.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.receive_signal_power.get_name_leafdata())
                        if (self.transmit_power.is_set or self.transmit_power.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.transmit_power.get_name_leafdata())
                        if (self.transmit_signal_power.is_set or self.transmit_signal_power.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.transmit_signal_power.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "lane-alarm-info"):
                            if (self.lane_alarm_info is None):
                                self.lane_alarm_info = OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo()
                                self.lane_alarm_info.parent = self
                                self._children_name_map["lane_alarm_info"] = "lane-alarm-info"
                            return self.lane_alarm_info

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "lane-alarm-info" or name == "number" or name == "lane-index" or name == "laser-bias-current-milli-amps" or name == "laser-bias-current-percent" or name == "output-frequency" or name == "receive-power" or name == "receive-signal-power" or name == "transmit-power" or name == "transmit-signal-power"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "number"):
                            self.number = value
                            self.number.value_namespace = name_space
                            self.number.value_namespace_prefix = name_space_prefix
                        if(value_path == "lane-index"):
                            self.lane_index = value
                            self.lane_index.value_namespace = name_space
                            self.lane_index.value_namespace_prefix = name_space_prefix
                        if(value_path == "laser-bias-current-milli-amps"):
                            self.laser_bias_current_milli_amps = value
                            self.laser_bias_current_milli_amps.value_namespace = name_space
                            self.laser_bias_current_milli_amps.value_namespace_prefix = name_space_prefix
                        if(value_path == "laser-bias-current-percent"):
                            self.laser_bias_current_percent = value
                            self.laser_bias_current_percent.value_namespace = name_space
                            self.laser_bias_current_percent.value_namespace_prefix = name_space_prefix
                        if(value_path == "output-frequency"):
                            self.output_frequency = value
                            self.output_frequency.value_namespace = name_space
                            self.output_frequency.value_namespace_prefix = name_space_prefix
                        if(value_path == "receive-power"):
                            self.receive_power = value
                            self.receive_power.value_namespace = name_space
                            self.receive_power.value_namespace_prefix = name_space_prefix
                        if(value_path == "receive-signal-power"):
                            self.receive_signal_power = value
                            self.receive_signal_power.value_namespace = name_space
                            self.receive_signal_power.value_namespace_prefix = name_space_prefix
                        if(value_path == "transmit-power"):
                            self.transmit_power = value
                            self.transmit_power.value_namespace = name_space
                            self.transmit_power.value_namespace_prefix = name_space_prefix
                        if(value_path == "transmit-signal-power"):
                            self.transmit_signal_power = value
                            self.transmit_signal_power.value_namespace = name_space
                            self.transmit_signal_power.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.optics_lane:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.optics_lane:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "optics-lanes" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "optics-lane"):
                        for c in self.optics_lane:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.optics_lane.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "optics-lane"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class OpticsDbInfo(Entity):
                """
                Optics operational data
                
                .. attribute:: controller_state
                
                	Optics controller state\: Up, Down or Administratively Down
                	**type**\:   :py:class:`OpticsControllerState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsControllerState>`
                
                .. attribute:: network_srlg_info
                
                	Network SRLG information
                	**type**\:   :py:class:`NetworkSrlgInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsDbInfo.NetworkSrlgInfo>`
                
                .. attribute:: transport_admin_state
                
                	Transport Admin State
                	**type**\:   :py:class:`OpticsTas <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsTas>`
                
                

                """

                _prefix = 'controller-optics-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(OpticsOper.OpticsPorts.OpticsPort.OpticsDbInfo, self).__init__()

                    self.yang_name = "optics-db-info"
                    self.yang_parent_name = "optics-port"

                    self.controller_state = YLeaf(YType.enumeration, "controller-state")

                    self.transport_admin_state = YLeaf(YType.enumeration, "transport-admin-state")

                    self.network_srlg_info = OpticsOper.OpticsPorts.OpticsPort.OpticsDbInfo.NetworkSrlgInfo()
                    self.network_srlg_info.parent = self
                    self._children_name_map["network_srlg_info"] = "network-srlg-info"
                    self._children_yang_names.add("network-srlg-info")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("controller_state",
                                    "transport_admin_state") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(OpticsOper.OpticsPorts.OpticsPort.OpticsDbInfo, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsDbInfo, self).__setattr__(name, value)


                class NetworkSrlgInfo(Entity):
                    """
                    Network SRLG information
                    
                    .. attribute:: network_srlg_array
                    
                    	Network Srlg Array
                    	**type**\: list of    :py:class:`NetworkSrlgArray <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsDbInfo.NetworkSrlgInfo.NetworkSrlgArray>`
                    
                    

                    """

                    _prefix = 'controller-optics-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsDbInfo.NetworkSrlgInfo, self).__init__()

                        self.yang_name = "network-srlg-info"
                        self.yang_parent_name = "optics-db-info"

                        self.network_srlg_array = YList(self)

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
                                    super(OpticsOper.OpticsPorts.OpticsPort.OpticsDbInfo.NetworkSrlgInfo, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(OpticsOper.OpticsPorts.OpticsPort.OpticsDbInfo.NetworkSrlgInfo, self).__setattr__(name, value)


                    class NetworkSrlgArray(Entity):
                        """
                        Network Srlg Array
                        
                        .. attribute:: network_srlg
                        
                        	Network Srlg
                        	**type**\:  list of int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: set_number
                        
                        	Array to maintain set number
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsDbInfo.NetworkSrlgInfo.NetworkSrlgArray, self).__init__()

                            self.yang_name = "network-srlg-array"
                            self.yang_parent_name = "network-srlg-info"

                            self.network_srlg = YLeafList(YType.uint32, "network-srlg")

                            self.set_number = YLeaf(YType.uint32, "set-number")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("network_srlg",
                                            "set_number") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsDbInfo.NetworkSrlgInfo.NetworkSrlgArray, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(OpticsOper.OpticsPorts.OpticsPort.OpticsDbInfo.NetworkSrlgInfo.NetworkSrlgArray, self).__setattr__(name, value)

                        def has_data(self):
                            for leaf in self.network_srlg.getYLeafs():
                                if (leaf.yfilter != YFilter.not_set):
                                    return True
                            return self.set_number.is_set

                        def has_operation(self):
                            for leaf in self.network_srlg.getYLeafs():
                                if (leaf.is_set):
                                    return True
                            return (
                                self.yfilter != YFilter.not_set or
                                self.network_srlg.yfilter != YFilter.not_set or
                                self.set_number.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "network-srlg-array" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.set_number.is_set or self.set_number.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.set_number.get_name_leafdata())

                            leaf_name_data.extend(self.network_srlg.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "network-srlg" or name == "set-number"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "network-srlg"):
                                self.network_srlg.append(value)
                            if(value_path == "set-number"):
                                self.set_number = value
                                self.set_number.value_namespace = name_space
                                self.set_number.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.network_srlg_array:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.network_srlg_array:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "network-srlg-info" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "network-srlg-array"):
                            for c in self.network_srlg_array:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = OpticsOper.OpticsPorts.OpticsPort.OpticsDbInfo.NetworkSrlgInfo.NetworkSrlgArray()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.network_srlg_array.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "network-srlg-array"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (
                        self.controller_state.is_set or
                        self.transport_admin_state.is_set or
                        (self.network_srlg_info is not None and self.network_srlg_info.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.controller_state.yfilter != YFilter.not_set or
                        self.transport_admin_state.yfilter != YFilter.not_set or
                        (self.network_srlg_info is not None and self.network_srlg_info.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "optics-db-info" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.controller_state.is_set or self.controller_state.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.controller_state.get_name_leafdata())
                    if (self.transport_admin_state.is_set or self.transport_admin_state.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.transport_admin_state.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "network-srlg-info"):
                        if (self.network_srlg_info is None):
                            self.network_srlg_info = OpticsOper.OpticsPorts.OpticsPort.OpticsDbInfo.NetworkSrlgInfo()
                            self.network_srlg_info.parent = self
                            self._children_name_map["network_srlg_info"] = "network-srlg-info"
                        return self.network_srlg_info

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "network-srlg-info" or name == "controller-state" or name == "transport-admin-state"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "controller-state"):
                        self.controller_state = value
                        self.controller_state.value_namespace = name_space
                        self.controller_state.value_namespace_prefix = name_space_prefix
                    if(value_path == "transport-admin-state"):
                        self.transport_admin_state = value
                        self.transport_admin_state.value_namespace = name_space
                        self.transport_admin_state.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.name.is_set or
                    (self.optics_db_info is not None and self.optics_db_info.has_data()) or
                    (self.optics_dwdm_carrrier_channel_map is not None and self.optics_dwdm_carrrier_channel_map.has_data()) or
                    (self.optics_info is not None and self.optics_info.has_data()) or
                    (self.optics_lanes is not None and self.optics_lanes.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.name.yfilter != YFilter.not_set or
                    (self.optics_db_info is not None and self.optics_db_info.has_operation()) or
                    (self.optics_dwdm_carrrier_channel_map is not None and self.optics_dwdm_carrrier_channel_map.has_operation()) or
                    (self.optics_info is not None and self.optics_info.has_operation()) or
                    (self.optics_lanes is not None and self.optics_lanes.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "optics-port" + "[name='" + self.name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-controller-optics-oper:optics-oper/optics-ports/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.name.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "optics-db-info"):
                    if (self.optics_db_info is None):
                        self.optics_db_info = OpticsOper.OpticsPorts.OpticsPort.OpticsDbInfo()
                        self.optics_db_info.parent = self
                        self._children_name_map["optics_db_info"] = "optics-db-info"
                    return self.optics_db_info

                if (child_yang_name == "optics-dwdm-carrrier-channel-map"):
                    if (self.optics_dwdm_carrrier_channel_map is None):
                        self.optics_dwdm_carrrier_channel_map = OpticsOper.OpticsPorts.OpticsPort.OpticsDwdmCarrrierChannelMap()
                        self.optics_dwdm_carrrier_channel_map.parent = self
                        self._children_name_map["optics_dwdm_carrrier_channel_map"] = "optics-dwdm-carrrier-channel-map"
                    return self.optics_dwdm_carrrier_channel_map

                if (child_yang_name == "optics-info"):
                    if (self.optics_info is None):
                        self.optics_info = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo()
                        self.optics_info.parent = self
                        self._children_name_map["optics_info"] = "optics-info"
                    return self.optics_info

                if (child_yang_name == "optics-lanes"):
                    if (self.optics_lanes is None):
                        self.optics_lanes = OpticsOper.OpticsPorts.OpticsPort.OpticsLanes()
                        self.optics_lanes.parent = self
                        self._children_name_map["optics_lanes"] = "optics-lanes"
                    return self.optics_lanes

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "optics-db-info" or name == "optics-dwdm-carrrier-channel-map" or name == "optics-info" or name == "optics-lanes" or name == "name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "name"):
                    self.name = value
                    self.name.value_namespace = name_space
                    self.name.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.optics_port:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.optics_port:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "optics-ports" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-controller-optics-oper:optics-oper/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "optics-port"):
                for c in self.optics_port:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = OpticsOper.OpticsPorts.OpticsPort()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.optics_port.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "optics-port"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (self.optics_ports is not None and self.optics_ports.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.optics_ports is not None and self.optics_ports.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-controller-optics-oper:optics-oper" + path_buffer

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

        if (child_yang_name == "optics-ports"):
            if (self.optics_ports is None):
                self.optics_ports = OpticsOper.OpticsPorts()
                self.optics_ports.parent = self
                self._children_name_map["optics_ports"] = "optics-ports"
            return self.optics_ports

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "optics-ports"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = OpticsOper()
        return self._top_entity

