""" Cisco_IOS_XR_controller_optics_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR controller\-optics package operational data.

This module contains definitions
for the following management objects\:
  optics\-oper\: Optics operational data

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
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

    .. data:: optics_amplifier_gain_range_invalid = 0

    	Invalid

    .. data:: optics_amplifier_gain_range_normal = 1

    	Normal

    .. data:: optics_amplifier_gain_range_ext_end_ed = 2

    	Extended

    """

    optics_amplifier_gain_range_invalid = Enum.YLeaf(0, "optics-amplifier-gain-range-invalid")

    optics_amplifier_gain_range_normal = Enum.YLeaf(1, "optics-amplifier-gain-range-normal")

    optics_amplifier_gain_range_ext_end_ed = Enum.YLeaf(2, "optics-amplifier-gain-range-ext-end-ed")


class OpticsAmplifierSafetyControlMode(Enum):
    """
    OpticsAmplifierSafetyControlMode

    Optics amplifier safety control mode

    .. data:: optics_amplifier_safety_mode_invalid = 0

    	Invalid

    .. data:: optics_amplifier_safety_mode_auto = 1

    	auto

    .. data:: optics_amplifier_safety_mode_disabled = 2

    	disabled

    """

    optics_amplifier_safety_mode_invalid = Enum.YLeaf(0, "optics-amplifier-safety-mode-invalid")

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

    .. data:: ten_gig_bx = 55

    	10G BX optics

    .. data:: one_geige = 56

    	1G BX optics

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

    ten_gig_bx = Enum.YLeaf(55, "ten-gig-bx")

    one_geige = Enum.YLeaf(56, "one-geige")


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
    _revision = '2017-05-01'

    def __init__(self):
        super(OpticsOper, self).__init__()
        self._top_entity = None

        self.yang_name = "optics-oper"
        self.yang_parent_name = "Cisco-IOS-XR-controller-optics-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"optics-ports" : ("optics_ports", OpticsOper.OpticsPorts)}
        self._child_list_classes = {}

        self.optics_ports = OpticsOper.OpticsPorts()
        self.optics_ports.parent = self
        self._children_name_map["optics_ports"] = "optics-ports"
        self._children_yang_names.add("optics-ports")
        self._segment_path = lambda: "Cisco-IOS-XR-controller-optics-oper:optics-oper"


    class OpticsPorts(Entity):
        """
        All Optics Port operational data
        
        .. attribute:: optics_port
        
        	Optics operational data
        	**type**\: list of    :py:class:`OpticsPort <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort>`
        
        

        """

        _prefix = 'controller-optics-oper'
        _revision = '2017-05-01'

        def __init__(self):
            super(OpticsOper.OpticsPorts, self).__init__()

            self.yang_name = "optics-ports"
            self.yang_parent_name = "optics-oper"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"optics-port" : ("optics_port", OpticsOper.OpticsPorts.OpticsPort)}

            self.optics_port = YList(self)
            self._segment_path = lambda: "optics-ports"
            self._absolute_path = lambda: "Cisco-IOS-XR-controller-optics-oper:optics-oper/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(OpticsOper.OpticsPorts, [], name, value)


        class OpticsPort(Entity):
            """
            Optics operational data
            
            .. attribute:: name  <key>
            
            	Port name
            	**type**\:  str
            
            	**pattern:** [a\-zA\-Z0\-9./\-]+
            
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
            _revision = '2017-05-01'

            def __init__(self):
                super(OpticsOper.OpticsPorts.OpticsPort, self).__init__()

                self.yang_name = "optics-port"
                self.yang_parent_name = "optics-ports"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"optics-db-info" : ("optics_db_info", OpticsOper.OpticsPorts.OpticsPort.OpticsDbInfo), "optics-dwdm-carrrier-channel-map" : ("optics_dwdm_carrrier_channel_map", OpticsOper.OpticsPorts.OpticsPort.OpticsDwdmCarrrierChannelMap), "optics-info" : ("optics_info", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo), "optics-lanes" : ("optics_lanes", OpticsOper.OpticsPorts.OpticsPort.OpticsLanes)}
                self._child_list_classes = {}

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
                self._segment_path = lambda: "optics-port" + "[name='" + self.name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-controller-optics-oper:optics-oper/optics-ports/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort, ['name'], name, value)


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
                _revision = '2017-05-01'

                def __init__(self):
                    super(OpticsOper.OpticsPorts.OpticsPort.OpticsDbInfo, self).__init__()

                    self.yang_name = "optics-db-info"
                    self.yang_parent_name = "optics-port"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"network-srlg-info" : ("network_srlg_info", OpticsOper.OpticsPorts.OpticsPort.OpticsDbInfo.NetworkSrlgInfo)}
                    self._child_list_classes = {}

                    self.controller_state = YLeaf(YType.enumeration, "controller-state")

                    self.transport_admin_state = YLeaf(YType.enumeration, "transport-admin-state")

                    self.network_srlg_info = OpticsOper.OpticsPorts.OpticsPort.OpticsDbInfo.NetworkSrlgInfo()
                    self.network_srlg_info.parent = self
                    self._children_name_map["network_srlg_info"] = "network-srlg-info"
                    self._children_yang_names.add("network-srlg-info")
                    self._segment_path = lambda: "optics-db-info"

                def __setattr__(self, name, value):
                    self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsDbInfo, ['controller_state', 'transport_admin_state'], name, value)


                class NetworkSrlgInfo(Entity):
                    """
                    Network SRLG information
                    
                    .. attribute:: network_srlg_array
                    
                    	Network Srlg Array
                    	**type**\: list of    :py:class:`NetworkSrlgArray <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsDbInfo.NetworkSrlgInfo.NetworkSrlgArray>`
                    
                    

                    """

                    _prefix = 'controller-optics-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsDbInfo.NetworkSrlgInfo, self).__init__()

                        self.yang_name = "network-srlg-info"
                        self.yang_parent_name = "optics-db-info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"network-srlg-array" : ("network_srlg_array", OpticsOper.OpticsPorts.OpticsPort.OpticsDbInfo.NetworkSrlgInfo.NetworkSrlgArray)}

                        self.network_srlg_array = YList(self)
                        self._segment_path = lambda: "network-srlg-info"

                    def __setattr__(self, name, value):
                        self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsDbInfo.NetworkSrlgInfo, [], name, value)


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
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsDbInfo.NetworkSrlgInfo.NetworkSrlgArray, self).__init__()

                            self.yang_name = "network-srlg-array"
                            self.yang_parent_name = "network-srlg-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.network_srlg = YLeafList(YType.uint32, "network-srlg")

                            self.set_number = YLeaf(YType.uint32, "set-number")
                            self._segment_path = lambda: "network-srlg-array"

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsDbInfo.NetworkSrlgInfo.NetworkSrlgArray, ['network_srlg', 'set_number'], name, value)


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
                _revision = '2017-05-01'

                def __init__(self):
                    super(OpticsOper.OpticsPorts.OpticsPort.OpticsDwdmCarrrierChannelMap, self).__init__()

                    self.yang_name = "optics-dwdm-carrrier-channel-map"
                    self.yang_parent_name = "optics-port"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"dwdm-carrier-map-info" : ("dwdm_carrier_map_info", OpticsOper.OpticsPorts.OpticsPort.OpticsDwdmCarrrierChannelMap.DwdmCarrierMapInfo)}

                    self.dwdm_carrier_band = YLeaf(YType.enumeration, "dwdm-carrier-band")

                    self.dwdm_carrier_max = YLeaf(YType.uint32, "dwdm-carrier-max")

                    self.dwdm_carrier_min = YLeaf(YType.uint32, "dwdm-carrier-min")

                    self.dwdm_carrier_map_info = YList(self)
                    self._segment_path = lambda: "optics-dwdm-carrrier-channel-map"

                def __setattr__(self, name, value):
                    self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsDwdmCarrrierChannelMap, ['dwdm_carrier_band', 'dwdm_carrier_max', 'dwdm_carrier_min'], name, value)


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
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsDwdmCarrrierChannelMap.DwdmCarrierMapInfo, self).__init__()

                        self.yang_name = "dwdm-carrier-map-info"
                        self.yang_parent_name = "optics-dwdm-carrrier-channel-map"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.frequency = YLeaf(YType.str, "frequency")

                        self.g694_chan_num = YLeaf(YType.int32, "g694-chan-num")

                        self.itu_chan_num = YLeaf(YType.uint32, "itu-chan-num")

                        self.wavelength = YLeaf(YType.str, "wavelength")
                        self._segment_path = lambda: "dwdm-carrier-map-info"

                    def __setattr__(self, name, value):
                        self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsDwdmCarrrierChannelMap.DwdmCarrierMapInfo, ['frequency', 'g694_chan_num', 'itu_chan_num', 'wavelength'], name, value)


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
                
                .. attribute:: ampli_gain_range
                
                	Ampli gain range
                	**type**\:   :py:class:`OpticsAmplifierGainRange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsAmplifierGainRange>`
                
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
                
                .. attribute:: derived_optics_type
                
                	Derived Optics type name
                	**type**\:  str
                
                .. attribute:: description
                
                	Controller description string
                	**type**\:  str
                
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
                
                	DWDM Carrier frequency read from hw in the unit 1THz
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
                
                .. attribute:: is_optics_type_string_valid
                
                	Is the Optics type string valid ?
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
                
                	Old Optics type name, Use Derived Optics type
                	**type**\:   :py:class:`Optics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.Optics>`
                
                .. attribute:: optics_type_str
                
                	optics type String
                	**type**\:  str
                
                .. attribute:: osnr_low_threshold
                
                	OSNR low threshold in 0.01 dB
                	**type**\:  str
                
                .. attribute:: osri
                
                	OSRI
                	**type**\:  bool
                
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
                
                .. attribute:: safety_control_mode
                
                	Safety control mode
                	**type**\:   :py:class:`OpticsAmplifierSafetyControlMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsAmplifierSafetyControlMode>`
                
                .. attribute:: safety_control_mode_config_val
                
                	safety control mode config val
                	**type**\:   :py:class:`OpticsAmplifierSafetyControlMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsAmplifierSafetyControlMode>`
                
                .. attribute:: second_order_polarization_mode_dispersion
                
                	Second Order Polarization Mode Dispersion 0 .1ps^2
                	**type**\:  str
                
                .. attribute:: spectrum_info
                
                	OTS Spectrum information
                	**type**\:   :py:class:`SpectrumInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.SpectrumInfo>`
                
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
                _revision = '2017-05-01'

                def __init__(self):
                    super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo, self).__init__()

                    self.yang_name = "optics-info"
                    self.yang_parent_name = "optics-port"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"ext-param-threshold-val" : ("ext_param_threshold_val", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtParamThresholdVal), "ext-param-val" : ("ext_param_val", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtParamVal), "network-srlg-info" : ("network_srlg_info", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.NetworkSrlgInfo), "optics-alarm-info" : ("optics_alarm_info", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo), "ots-alarm-info" : ("ots_alarm_info", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo), "spectrum-info" : ("spectrum_info", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.SpectrumInfo), "transceiver-info" : ("transceiver_info", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.TransceiverInfo)}
                    self._child_list_classes = {"lane-data" : ("lane_data", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData)}

                    self.alarm_detected = YLeaf(YType.boolean, "alarm-detected")

                    self.ampli_channel_power_config_val = YLeaf(YType.int32, "ampli-channel-power-config-val")

                    self.ampli_control_mode_config_val = YLeaf(YType.enumeration, "ampli-control-mode-config-val")

                    self.ampli_gain = YLeaf(YType.int32, "ampli-gain")

                    self.ampli_gain_config_val = YLeaf(YType.int32, "ampli-gain-config-val")

                    self.ampli_gain_range = YLeaf(YType.enumeration, "ampli-gain-range")

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

                    self.derived_optics_type = YLeaf(YType.str, "derived-optics-type")

                    self.description = YLeaf(YType.str, "description")

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

                    self.is_optics_type_string_valid = YLeaf(YType.boolean, "is-optics-type-string-valid")

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

                    self.optics_type_str = YLeaf(YType.str, "optics-type-str")

                    self.osnr_low_threshold = YLeaf(YType.str, "osnr-low-threshold")

                    self.osri = YLeaf(YType.boolean, "osri")

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

                    self.safety_control_mode = YLeaf(YType.enumeration, "safety-control-mode")

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

                    self.spectrum_info = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.SpectrumInfo()
                    self.spectrum_info.parent = self
                    self._children_name_map["spectrum_info"] = "spectrum-info"
                    self._children_yang_names.add("spectrum-info")

                    self.transceiver_info = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.TransceiverInfo()
                    self.transceiver_info.parent = self
                    self._children_name_map["transceiver_info"] = "transceiver-info"
                    self._children_yang_names.add("transceiver-info")

                    self.lane_data = YList(self)
                    self._segment_path = lambda: "optics-info"

                def __setattr__(self, name, value):
                    self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo, ['alarm_detected', 'ampli_channel_power_config_val', 'ampli_control_mode_config_val', 'ampli_gain', 'ampli_gain_config_val', 'ampli_gain_range', 'ampli_gain_range_config_val', 'ampli_gain_thr_deg_high_config_val', 'ampli_gain_thr_deg_low_config_val', 'ampli_tilt', 'ampli_tilt_config_val', 'cd', 'cd_configurable', 'cd_high_threshold', 'cd_low_threshold', 'cd_max', 'cd_min', 'cfg_tx_power', 'cfg_tx_power_configurable', 'channel_power_max_delta_config_val', 'controller_state', 'derived_optics_type', 'description', 'dgd_high_threshold', 'differential_group_delay', 'display_volt_temp', 'dwdm_carrier_band', 'dwdm_carrier_channel', 'dwdm_carrier_frequency', 'dwdm_carrier_wavelength', 'form_factor', 'grey_wavelength', 'is_bo_configured', 'is_ext_param_valid', 'is_optics_type_string_valid', 'laser_state', 'lbc_high_threshold', 'lbc_th_high_default', 'lbc_th_high_warning_default', 'lbc_th_low_default', 'lbc_th_low_warning_default', 'led_state', 'optical_signal_to_noise_ratio', 'optics_fec', 'optics_module', 'optics_present', 'optics_type', 'optics_type_str', 'osnr_low_threshold', 'osri', 'osri_config_val', 'phase_noise', 'phy_type', 'pm_enable', 'polarization_change_rate', 'polarization_dependent_loss', 'polarization_mode_dispersion', 'port_status', 'port_type', 'rx_high_threshold', 'rx_high_warning_threshold', 'rx_low_threshold', 'rx_low_warning_threshold', 'rx_power_th_configurable', 'rx_voa_attenuation', 'rx_voa_attenuation_config_val', 'safety_control_mode', 'safety_control_mode_config_val', 'second_order_polarization_mode_dispersion', 'temp_high_threshold', 'temp_high_warning_threshold', 'temp_low_threshold', 'temp_low_warning_threshold', 'temperature', 'total_rx_power', 'total_tx_power', 'transport_admin_state', 'tx_high_threshold', 'tx_high_warning_threshold', 'tx_low_threshold', 'tx_low_warning_threshold', 'tx_power_th_configurable', 'tx_voa_attenuation', 'tx_voa_attenuation_config_val', 'volt_high_threshold', 'volt_high_warning_threshold', 'volt_low_threshold', 'volt_low_warning_threshold', 'voltage'], name, value)


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
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtParamThresholdVal, self).__init__()

                        self.yang_name = "ext-param-threshold-val"
                        self.yang_parent_name = "optics-info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

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
                        self._segment_path = lambda: "ext-param-threshold-val"

                    def __setattr__(self, name, value):
                        self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtParamThresholdVal, ['isi_correction_alarm_high_threshold', 'isi_correction_alarm_low_threshold', 'isi_correction_warn_high_threshold', 'isi_correction_warn_low_threshold', 'laser_diff_frequency_alarm_high_threshold', 'laser_diff_frequency_alarm_low_threshold', 'laser_diff_frequency_warn_high_threshold', 'laser_diff_frequency_warn_low_threshold', 'laser_diff_temperature_alarm_high_threshold', 'laser_diff_temperature_alarm_low_threshold', 'laser_diff_temperature_warn_high_threshold', 'laser_diff_temperature_warn_low_threshold', 'pam_rate_alarm_high_threshold', 'pam_rate_alarm_low_threshold', 'pam_rate_warn_high_threshold', 'pam_rate_warn_low_threshold', 'pre_fec_ber_accumulated_alarm_high_threshold', 'pre_fec_ber_accumulated_alarm_low_threshold', 'pre_fec_ber_accumulated_warn_high_threshold', 'pre_fec_ber_accumulated_warn_low_threshold', 'pre_fec_ber_alarm_high_threshold', 'pre_fec_ber_alarm_low_threshold', 'pre_fec_ber_instantaneous_alarm_high_threshold', 'pre_fec_ber_instantaneous_alarm_low_threshold', 'pre_fec_ber_instantaneous_warn_high_threshold', 'pre_fec_ber_instantaneous_warn_low_threshold', 'pre_fec_ber_latched_max_alarm_high_threshold', 'pre_fec_ber_latched_max_alarm_low_threshold', 'pre_fec_ber_latched_max_warn_high_threshold', 'pre_fec_ber_latched_max_warn_low_threshold', 'pre_fec_ber_latched_min_alarm_high_threshold', 'pre_fec_ber_latched_min_alarm_low_threshold', 'pre_fec_ber_latched_min_warn_high_threshold', 'pre_fec_ber_latched_min_warn_low_threshold', 'pre_fec_ber_warn_high_threshold', 'pre_fec_ber_warn_low_threshold', 'snr_alarm_high_threshold', 'snr_alarm_low_threshold', 'snr_warn_high_threshold', 'snr_warn_low_threshold', 'tec_current_alarm_high_threshold', 'tec_current_alarm_low_threshold', 'tec_current_warn_high_threshold', 'tec_current_warn_low_threshold', 'uncorrected_ber_accumulated_alarm_high_threshold', 'uncorrected_ber_accumulated_alarm_low_threshold', 'uncorrected_ber_accumulated_warn_high_threshold', 'uncorrected_ber_accumulated_warn_low_threshold', 'uncorrected_ber_alarm_high_threshold', 'uncorrected_ber_alarm_low_threshold', 'uncorrected_ber_instantaneous_alarm_high_threshold', 'uncorrected_ber_instantaneous_alarm_low_threshold', 'uncorrected_ber_instantaneous_warn_high_threshold', 'uncorrected_ber_instantaneous_warn_low_threshold', 'uncorrected_ber_latched_max_alarm_high_threshold', 'uncorrected_ber_latched_max_alarm_low_threshold', 'uncorrected_ber_latched_max_warn_high_threshold', 'uncorrected_ber_latched_max_warn_low_threshold', 'uncorrected_ber_latched_min_alarm_high_threshold', 'uncorrected_ber_latched_min_alarm_low_threshold', 'uncorrected_ber_latched_min_warn_high_threshold', 'uncorrected_ber_latched_min_warn_low_threshold', 'uncorrected_ber_warn_high_threshold', 'uncorrected_ber_warn_low_threshold'], name, value)


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
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtParamVal, self).__init__()

                        self.yang_name = "ext-param-val"
                        self.yang_parent_name = "optics-info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

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
                        self._segment_path = lambda: "ext-param-val"

                    def __setattr__(self, name, value):
                        self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtParamVal, ['isi_correction_lane1', 'isi_correction_lane2', 'laser_diff_frequency_lane1', 'laser_diff_frequency_lane2', 'laser_diff_temperature_lane1', 'laser_diff_temperature_lane2', 'pam_rate_lane1', 'pam_rate_lane2', 'pre_fec_ber', 'pre_fec_ber_accumulated', 'pre_fec_ber_instantaneous', 'pre_fec_ber_latched_max', 'pre_fec_ber_latched_min', 'snr_lane1', 'snr_lane2', 'tec_current_lane1', 'tec_current_lane2', 'uncorrected_ber', 'uncorrected_ber_accumulated', 'uncorrected_ber_instantaneous', 'uncorrected_ber_latched_max', 'uncorrected_ber_latched_min'], name, value)


                class LaneData(Entity):
                    """
                    Lane information
                    
                    .. attribute:: frequency_offset
                    
                    	Frequency Offset read from hw in unit of MHz
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
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
                    
                    	Output frequency read from hw in the unit 100MHz
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
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData, self).__init__()

                        self.yang_name = "lane-data"
                        self.yang_parent_name = "optics-info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"lane-alarm-info" : ("lane_alarm_info", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo)}
                        self._child_list_classes = {}

                        self.frequency_offset = YLeaf(YType.int32, "frequency-offset")

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
                        self._segment_path = lambda: "lane-data"

                    def __setattr__(self, name, value):
                        self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData, ['frequency_offset', 'lane_index', 'laser_bias_current_milli_amps', 'laser_bias_current_percent', 'output_frequency', 'receive_power', 'receive_signal_power', 'transmit_power', 'transmit_signal_power'], name, value)


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
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo, self).__init__()

                            self.yang_name = "lane-alarm-info"
                            self.yang_parent_name = "lane-data"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"high-lbc" : ("high_lbc", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.HighLbc), "high-rx-power" : ("high_rx_power", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.HighRxPower), "high-tx-power" : ("high_tx_power", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.HighTxPower), "low-rx-power" : ("low_rx_power", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.LowRxPower), "low-tx-power" : ("low_tx_power", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.LowTxPower)}
                            self._child_list_classes = {}

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
                            self._segment_path = lambda: "lane-alarm-info"


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
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.HighLbc, self).__init__()

                                self.yang_name = "high-lbc"
                                self.yang_parent_name = "lane-alarm-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.counter = YLeaf(YType.uint32, "counter")

                                self.is_detected = YLeaf(YType.boolean, "is-detected")
                                self._segment_path = lambda: "high-lbc"

                            def __setattr__(self, name, value):
                                self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.HighLbc, ['counter', 'is_detected'], name, value)


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
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.HighRxPower, self).__init__()

                                self.yang_name = "high-rx-power"
                                self.yang_parent_name = "lane-alarm-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.counter = YLeaf(YType.uint32, "counter")

                                self.is_detected = YLeaf(YType.boolean, "is-detected")
                                self._segment_path = lambda: "high-rx-power"

                            def __setattr__(self, name, value):
                                self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.HighRxPower, ['counter', 'is_detected'], name, value)


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
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.HighTxPower, self).__init__()

                                self.yang_name = "high-tx-power"
                                self.yang_parent_name = "lane-alarm-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.counter = YLeaf(YType.uint32, "counter")

                                self.is_detected = YLeaf(YType.boolean, "is-detected")
                                self._segment_path = lambda: "high-tx-power"

                            def __setattr__(self, name, value):
                                self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.HighTxPower, ['counter', 'is_detected'], name, value)


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
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.LowRxPower, self).__init__()

                                self.yang_name = "low-rx-power"
                                self.yang_parent_name = "lane-alarm-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.counter = YLeaf(YType.uint32, "counter")

                                self.is_detected = YLeaf(YType.boolean, "is-detected")
                                self._segment_path = lambda: "low-rx-power"

                            def __setattr__(self, name, value):
                                self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.LowRxPower, ['counter', 'is_detected'], name, value)


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
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.LowTxPower, self).__init__()

                                self.yang_name = "low-tx-power"
                                self.yang_parent_name = "lane-alarm-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.counter = YLeaf(YType.uint32, "counter")

                                self.is_detected = YLeaf(YType.boolean, "is-detected")
                                self._segment_path = lambda: "low-tx-power"

                            def __setattr__(self, name, value):
                                self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.LowTxPower, ['counter', 'is_detected'], name, value)


                class NetworkSrlgInfo(Entity):
                    """
                    Network SRLG information
                    
                    .. attribute:: network_srlg_array
                    
                    	Network Srlg Array
                    	**type**\: list of    :py:class:`NetworkSrlgArray <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.NetworkSrlgInfo.NetworkSrlgArray>`
                    
                    

                    """

                    _prefix = 'controller-optics-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.NetworkSrlgInfo, self).__init__()

                        self.yang_name = "network-srlg-info"
                        self.yang_parent_name = "optics-info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"network-srlg-array" : ("network_srlg_array", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.NetworkSrlgInfo.NetworkSrlgArray)}

                        self.network_srlg_array = YList(self)
                        self._segment_path = lambda: "network-srlg-info"

                    def __setattr__(self, name, value):
                        self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.NetworkSrlgInfo, [], name, value)


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
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.NetworkSrlgInfo.NetworkSrlgArray, self).__init__()

                            self.yang_name = "network-srlg-array"
                            self.yang_parent_name = "network-srlg-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.network_srlg = YLeafList(YType.uint32, "network-srlg")

                            self.set_number = YLeaf(YType.uint32, "set-number")
                            self._segment_path = lambda: "network-srlg-array"

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.NetworkSrlgInfo.NetworkSrlgArray, ['network_srlg', 'set_number'], name, value)


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
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo, self).__init__()

                        self.yang_name = "optics-alarm-info"
                        self.yang_parent_name = "optics-info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"amp-gain-deg-high" : ("amp_gain_deg_high", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.AmpGainDegHigh), "amp-gain-deg-low" : ("amp_gain_deg_low", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.AmpGainDegLow), "hidgd" : ("hidgd", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Hidgd), "high-lbc" : ("high_lbc", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighLbc), "high-rx1-power" : ("high_rx1_power", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx1Power), "high-rx2-power" : ("high_rx2_power", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx2Power), "high-rx3-power" : ("high_rx3_power", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx3Power), "high-rx4-power" : ("high_rx4_power", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx4Power), "high-rx-power" : ("high_rx_power", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRxPower), "high-tx1-power" : ("high_tx1_power", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx1Power), "high-tx1lbc" : ("high_tx1lbc", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx1Lbc), "high-tx2-power" : ("high_tx2_power", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx2Power), "high-tx2lbc" : ("high_tx2lbc", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx2Lbc), "high-tx3-power" : ("high_tx3_power", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx3Power), "high-tx3lbc" : ("high_tx3lbc", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx3Lbc), "high-tx4-power" : ("high_tx4_power", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx4Power), "high-tx4lbc" : ("high_tx4lbc", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx4Lbc), "high-tx-power" : ("high_tx_power", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTxPower), "imp-removal" : ("imp_removal", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.ImpRemoval), "low-rx1-power" : ("low_rx1_power", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx1Power), "low-rx2-power" : ("low_rx2_power", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx2Power), "low-rx3-power" : ("low_rx3_power", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx3Power), "low-rx4-power" : ("low_rx4_power", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx4Power), "low-rx-power" : ("low_rx_power", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRxPower), "low-tx1-power" : ("low_tx1_power", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx1Power), "low-tx1lbc" : ("low_tx1lbc", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx1Lbc), "low-tx2-power" : ("low_tx2_power", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx2Power), "low-tx2lbc" : ("low_tx2lbc", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx2Lbc), "low-tx3-power" : ("low_tx3_power", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx3Power), "low-tx3lbc" : ("low_tx3lbc", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx3Lbc), "low-tx4-power" : ("low_tx4_power", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx4Power), "low-tx4lbc" : ("low_tx4lbc", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx4Lbc), "low-tx-power" : ("low_tx_power", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTxPower), "mea" : ("mea", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Mea), "oorcd" : ("oorcd", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Oorcd), "osnr" : ("osnr", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Osnr), "rx-loc" : ("rx_loc", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.RxLoc), "rx-lol" : ("rx_lol", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.RxLol), "rx-los" : ("rx_los", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.RxLos), "tx-fault" : ("tx_fault", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxFault), "tx-lol" : ("tx_lol", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxLol), "tx-los" : ("tx_los", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxLos), "txpwr-mismatch" : ("txpwr_mismatch", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxpwrMismatch), "wvlool" : ("wvlool", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Wvlool)}
                        self._child_list_classes = {}

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
                        self._segment_path = lambda: "optics-alarm-info"


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
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.AmpGainDegHigh, self).__init__()

                            self.yang_name = "amp-gain-deg-high"
                            self.yang_parent_name = "optics-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")
                            self._segment_path = lambda: "amp-gain-deg-high"

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.AmpGainDegHigh, ['counter', 'is_detected'], name, value)


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
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.AmpGainDegLow, self).__init__()

                            self.yang_name = "amp-gain-deg-low"
                            self.yang_parent_name = "optics-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")
                            self._segment_path = lambda: "amp-gain-deg-low"

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.AmpGainDegLow, ['counter', 'is_detected'], name, value)


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
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Hidgd, self).__init__()

                            self.yang_name = "hidgd"
                            self.yang_parent_name = "optics-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")
                            self._segment_path = lambda: "hidgd"

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Hidgd, ['counter', 'is_detected'], name, value)


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
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighLbc, self).__init__()

                            self.yang_name = "high-lbc"
                            self.yang_parent_name = "optics-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")
                            self._segment_path = lambda: "high-lbc"

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighLbc, ['counter', 'is_detected'], name, value)


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
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx1Power, self).__init__()

                            self.yang_name = "high-rx1-power"
                            self.yang_parent_name = "optics-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")
                            self._segment_path = lambda: "high-rx1-power"

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx1Power, ['counter', 'is_detected'], name, value)


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
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx2Power, self).__init__()

                            self.yang_name = "high-rx2-power"
                            self.yang_parent_name = "optics-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")
                            self._segment_path = lambda: "high-rx2-power"

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx2Power, ['counter', 'is_detected'], name, value)


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
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx3Power, self).__init__()

                            self.yang_name = "high-rx3-power"
                            self.yang_parent_name = "optics-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")
                            self._segment_path = lambda: "high-rx3-power"

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx3Power, ['counter', 'is_detected'], name, value)


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
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx4Power, self).__init__()

                            self.yang_name = "high-rx4-power"
                            self.yang_parent_name = "optics-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")
                            self._segment_path = lambda: "high-rx4-power"

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx4Power, ['counter', 'is_detected'], name, value)


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
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRxPower, self).__init__()

                            self.yang_name = "high-rx-power"
                            self.yang_parent_name = "optics-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")
                            self._segment_path = lambda: "high-rx-power"

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRxPower, ['counter', 'is_detected'], name, value)


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
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx1Lbc, self).__init__()

                            self.yang_name = "high-tx1lbc"
                            self.yang_parent_name = "optics-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")
                            self._segment_path = lambda: "high-tx1lbc"

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx1Lbc, ['counter', 'is_detected'], name, value)


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
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx1Power, self).__init__()

                            self.yang_name = "high-tx1-power"
                            self.yang_parent_name = "optics-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")
                            self._segment_path = lambda: "high-tx1-power"

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx1Power, ['counter', 'is_detected'], name, value)


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
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx2Lbc, self).__init__()

                            self.yang_name = "high-tx2lbc"
                            self.yang_parent_name = "optics-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")
                            self._segment_path = lambda: "high-tx2lbc"

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx2Lbc, ['counter', 'is_detected'], name, value)


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
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx2Power, self).__init__()

                            self.yang_name = "high-tx2-power"
                            self.yang_parent_name = "optics-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")
                            self._segment_path = lambda: "high-tx2-power"

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx2Power, ['counter', 'is_detected'], name, value)


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
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx3Lbc, self).__init__()

                            self.yang_name = "high-tx3lbc"
                            self.yang_parent_name = "optics-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")
                            self._segment_path = lambda: "high-tx3lbc"

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx3Lbc, ['counter', 'is_detected'], name, value)


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
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx3Power, self).__init__()

                            self.yang_name = "high-tx3-power"
                            self.yang_parent_name = "optics-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")
                            self._segment_path = lambda: "high-tx3-power"

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx3Power, ['counter', 'is_detected'], name, value)


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
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx4Lbc, self).__init__()

                            self.yang_name = "high-tx4lbc"
                            self.yang_parent_name = "optics-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")
                            self._segment_path = lambda: "high-tx4lbc"

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx4Lbc, ['counter', 'is_detected'], name, value)


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
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx4Power, self).__init__()

                            self.yang_name = "high-tx4-power"
                            self.yang_parent_name = "optics-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")
                            self._segment_path = lambda: "high-tx4-power"

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx4Power, ['counter', 'is_detected'], name, value)


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
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTxPower, self).__init__()

                            self.yang_name = "high-tx-power"
                            self.yang_parent_name = "optics-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")
                            self._segment_path = lambda: "high-tx-power"

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTxPower, ['counter', 'is_detected'], name, value)


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
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.ImpRemoval, self).__init__()

                            self.yang_name = "imp-removal"
                            self.yang_parent_name = "optics-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")
                            self._segment_path = lambda: "imp-removal"

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.ImpRemoval, ['counter', 'is_detected'], name, value)


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
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx1Power, self).__init__()

                            self.yang_name = "low-rx1-power"
                            self.yang_parent_name = "optics-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")
                            self._segment_path = lambda: "low-rx1-power"

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx1Power, ['counter', 'is_detected'], name, value)


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
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx2Power, self).__init__()

                            self.yang_name = "low-rx2-power"
                            self.yang_parent_name = "optics-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")
                            self._segment_path = lambda: "low-rx2-power"

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx2Power, ['counter', 'is_detected'], name, value)


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
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx3Power, self).__init__()

                            self.yang_name = "low-rx3-power"
                            self.yang_parent_name = "optics-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")
                            self._segment_path = lambda: "low-rx3-power"

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx3Power, ['counter', 'is_detected'], name, value)


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
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx4Power, self).__init__()

                            self.yang_name = "low-rx4-power"
                            self.yang_parent_name = "optics-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")
                            self._segment_path = lambda: "low-rx4-power"

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx4Power, ['counter', 'is_detected'], name, value)


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
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRxPower, self).__init__()

                            self.yang_name = "low-rx-power"
                            self.yang_parent_name = "optics-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")
                            self._segment_path = lambda: "low-rx-power"

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRxPower, ['counter', 'is_detected'], name, value)


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
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx1Lbc, self).__init__()

                            self.yang_name = "low-tx1lbc"
                            self.yang_parent_name = "optics-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")
                            self._segment_path = lambda: "low-tx1lbc"

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx1Lbc, ['counter', 'is_detected'], name, value)


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
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx1Power, self).__init__()

                            self.yang_name = "low-tx1-power"
                            self.yang_parent_name = "optics-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")
                            self._segment_path = lambda: "low-tx1-power"

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx1Power, ['counter', 'is_detected'], name, value)


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
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx2Lbc, self).__init__()

                            self.yang_name = "low-tx2lbc"
                            self.yang_parent_name = "optics-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")
                            self._segment_path = lambda: "low-tx2lbc"

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx2Lbc, ['counter', 'is_detected'], name, value)


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
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx2Power, self).__init__()

                            self.yang_name = "low-tx2-power"
                            self.yang_parent_name = "optics-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")
                            self._segment_path = lambda: "low-tx2-power"

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx2Power, ['counter', 'is_detected'], name, value)


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
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx3Lbc, self).__init__()

                            self.yang_name = "low-tx3lbc"
                            self.yang_parent_name = "optics-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")
                            self._segment_path = lambda: "low-tx3lbc"

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx3Lbc, ['counter', 'is_detected'], name, value)


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
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx3Power, self).__init__()

                            self.yang_name = "low-tx3-power"
                            self.yang_parent_name = "optics-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")
                            self._segment_path = lambda: "low-tx3-power"

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx3Power, ['counter', 'is_detected'], name, value)


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
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx4Lbc, self).__init__()

                            self.yang_name = "low-tx4lbc"
                            self.yang_parent_name = "optics-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")
                            self._segment_path = lambda: "low-tx4lbc"

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx4Lbc, ['counter', 'is_detected'], name, value)


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
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx4Power, self).__init__()

                            self.yang_name = "low-tx4-power"
                            self.yang_parent_name = "optics-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")
                            self._segment_path = lambda: "low-tx4-power"

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx4Power, ['counter', 'is_detected'], name, value)


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
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTxPower, self).__init__()

                            self.yang_name = "low-tx-power"
                            self.yang_parent_name = "optics-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")
                            self._segment_path = lambda: "low-tx-power"

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTxPower, ['counter', 'is_detected'], name, value)


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
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Mea, self).__init__()

                            self.yang_name = "mea"
                            self.yang_parent_name = "optics-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")
                            self._segment_path = lambda: "mea"

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Mea, ['counter', 'is_detected'], name, value)


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
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Oorcd, self).__init__()

                            self.yang_name = "oorcd"
                            self.yang_parent_name = "optics-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")
                            self._segment_path = lambda: "oorcd"

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Oorcd, ['counter', 'is_detected'], name, value)


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
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Osnr, self).__init__()

                            self.yang_name = "osnr"
                            self.yang_parent_name = "optics-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")
                            self._segment_path = lambda: "osnr"

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Osnr, ['counter', 'is_detected'], name, value)


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
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.RxLoc, self).__init__()

                            self.yang_name = "rx-loc"
                            self.yang_parent_name = "optics-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")
                            self._segment_path = lambda: "rx-loc"

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.RxLoc, ['counter', 'is_detected'], name, value)


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
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.RxLol, self).__init__()

                            self.yang_name = "rx-lol"
                            self.yang_parent_name = "optics-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")
                            self._segment_path = lambda: "rx-lol"

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.RxLol, ['counter', 'is_detected'], name, value)


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
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.RxLos, self).__init__()

                            self.yang_name = "rx-los"
                            self.yang_parent_name = "optics-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")
                            self._segment_path = lambda: "rx-los"

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.RxLos, ['counter', 'is_detected'], name, value)


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
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxFault, self).__init__()

                            self.yang_name = "tx-fault"
                            self.yang_parent_name = "optics-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")
                            self._segment_path = lambda: "tx-fault"

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxFault, ['counter', 'is_detected'], name, value)


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
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxLol, self).__init__()

                            self.yang_name = "tx-lol"
                            self.yang_parent_name = "optics-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")
                            self._segment_path = lambda: "tx-lol"

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxLol, ['counter', 'is_detected'], name, value)


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
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxLos, self).__init__()

                            self.yang_name = "tx-los"
                            self.yang_parent_name = "optics-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")
                            self._segment_path = lambda: "tx-los"

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxLos, ['counter', 'is_detected'], name, value)


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
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxpwrMismatch, self).__init__()

                            self.yang_name = "txpwr-mismatch"
                            self.yang_parent_name = "optics-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")
                            self._segment_path = lambda: "txpwr-mismatch"

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxpwrMismatch, ['counter', 'is_detected'], name, value)


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
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Wvlool, self).__init__()

                            self.yang_name = "wvlool"
                            self.yang_parent_name = "optics-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")
                            self._segment_path = lambda: "wvlool"

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Wvlool, ['counter', 'is_detected'], name, value)


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
                    
                    .. attribute:: auto_ampli_ctrl_running
                    
                    	Auto Ampli Ctrl Running
                    	**type**\:   :py:class:`AutoAmpliCtrlRunning <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AutoAmpliCtrlRunning>`
                    
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
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo, self).__init__()

                        self.yang_name = "ots-alarm-info"
                        self.yang_parent_name = "optics-info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"amp-gain-deg-high" : ("amp_gain_deg_high", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AmpGainDegHigh), "amp-gain-deg-low" : ("amp_gain_deg_low", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AmpGainDegLow), "auto-ampli-ctrl-config-mismatch" : ("auto_ampli_ctrl_config_mismatch", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AutoAmpliCtrlConfigMismatch), "auto-ampli-ctrl-disabled" : ("auto_ampli_ctrl_disabled", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AutoAmpliCtrlDisabled), "auto-ampli-ctrl-running" : ("auto_ampli_ctrl_running", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AutoAmpliCtrlRunning), "auto-laser-shut" : ("auto_laser_shut", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AutoLaserShut), "auto-power-red" : ("auto_power_red", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AutoPowerRed), "low-rx-power" : ("low_rx_power", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.LowRxPower), "low-tx-power" : ("low_tx_power", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.LowTxPower), "rx-loc" : ("rx_loc", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.RxLoc), "rx-los-p" : ("rx_los_p", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.RxLosP), "switch-to-protect" : ("switch_to_protect", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.SwitchToProtect)}
                        self._child_list_classes = {}

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

                        self.auto_ampli_ctrl_running = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AutoAmpliCtrlRunning()
                        self.auto_ampli_ctrl_running.parent = self
                        self._children_name_map["auto_ampli_ctrl_running"] = "auto-ampli-ctrl-running"
                        self._children_yang_names.add("auto-ampli-ctrl-running")

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
                        self._segment_path = lambda: "ots-alarm-info"


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
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AmpGainDegHigh, self).__init__()

                            self.yang_name = "amp-gain-deg-high"
                            self.yang_parent_name = "ots-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")
                            self._segment_path = lambda: "amp-gain-deg-high"

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AmpGainDegHigh, ['counter', 'is_detected'], name, value)


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
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AmpGainDegLow, self).__init__()

                            self.yang_name = "amp-gain-deg-low"
                            self.yang_parent_name = "ots-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")
                            self._segment_path = lambda: "amp-gain-deg-low"

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AmpGainDegLow, ['counter', 'is_detected'], name, value)


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
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AutoAmpliCtrlConfigMismatch, self).__init__()

                            self.yang_name = "auto-ampli-ctrl-config-mismatch"
                            self.yang_parent_name = "ots-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")
                            self._segment_path = lambda: "auto-ampli-ctrl-config-mismatch"

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AutoAmpliCtrlConfigMismatch, ['counter', 'is_detected'], name, value)


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
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AutoAmpliCtrlDisabled, self).__init__()

                            self.yang_name = "auto-ampli-ctrl-disabled"
                            self.yang_parent_name = "ots-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")
                            self._segment_path = lambda: "auto-ampli-ctrl-disabled"

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AutoAmpliCtrlDisabled, ['counter', 'is_detected'], name, value)


                    class AutoAmpliCtrlRunning(Entity):
                        """
                        Auto Ampli Ctrl Running
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AutoAmpliCtrlRunning, self).__init__()

                            self.yang_name = "auto-ampli-ctrl-running"
                            self.yang_parent_name = "ots-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")
                            self._segment_path = lambda: "auto-ampli-ctrl-running"

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AutoAmpliCtrlRunning, ['counter', 'is_detected'], name, value)


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
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AutoLaserShut, self).__init__()

                            self.yang_name = "auto-laser-shut"
                            self.yang_parent_name = "ots-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")
                            self._segment_path = lambda: "auto-laser-shut"

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AutoLaserShut, ['counter', 'is_detected'], name, value)


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
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AutoPowerRed, self).__init__()

                            self.yang_name = "auto-power-red"
                            self.yang_parent_name = "ots-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")
                            self._segment_path = lambda: "auto-power-red"

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AutoPowerRed, ['counter', 'is_detected'], name, value)


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
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.LowRxPower, self).__init__()

                            self.yang_name = "low-rx-power"
                            self.yang_parent_name = "ots-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")
                            self._segment_path = lambda: "low-rx-power"

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.LowRxPower, ['counter', 'is_detected'], name, value)


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
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.LowTxPower, self).__init__()

                            self.yang_name = "low-tx-power"
                            self.yang_parent_name = "ots-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")
                            self._segment_path = lambda: "low-tx-power"

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.LowTxPower, ['counter', 'is_detected'], name, value)


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
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.RxLoc, self).__init__()

                            self.yang_name = "rx-loc"
                            self.yang_parent_name = "ots-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")
                            self._segment_path = lambda: "rx-loc"

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.RxLoc, ['counter', 'is_detected'], name, value)


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
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.RxLosP, self).__init__()

                            self.yang_name = "rx-los-p"
                            self.yang_parent_name = "ots-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")
                            self._segment_path = lambda: "rx-los-p"

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.RxLosP, ['counter', 'is_detected'], name, value)


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
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.SwitchToProtect, self).__init__()

                            self.yang_name = "switch-to-protect"
                            self.yang_parent_name = "ots-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.counter = YLeaf(YType.uint32, "counter")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")
                            self._segment_path = lambda: "switch-to-protect"

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.SwitchToProtect, ['counter', 'is_detected'], name, value)


                class SpectrumInfo(Entity):
                    """
                    OTS Spectrum information
                    
                    .. attribute:: first_slice_wavelength
                    
                    	Wavelength of first slice
                    	**type**\:  str
                    
                    	**length:** 0..32
                    
                    .. attribute:: spectrum_slice_power_info
                    
                    	Power information of spectrum slice info
                    	**type**\: list of    :py:class:`SpectrumSlicePowerInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.SpectrumInfo.SpectrumSlicePowerInfo>`
                    
                    .. attribute:: spectrum_slice_spacing
                    
                    	Spacing between spectrum slices
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: total_spectrum_slice_count
                    
                    	Total number of slices in Spectrum
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'controller-optics-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.SpectrumInfo, self).__init__()

                        self.yang_name = "spectrum-info"
                        self.yang_parent_name = "optics-info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"spectrum-slice-power-info" : ("spectrum_slice_power_info", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.SpectrumInfo.SpectrumSlicePowerInfo)}

                        self.first_slice_wavelength = YLeaf(YType.str, "first-slice-wavelength")

                        self.spectrum_slice_spacing = YLeaf(YType.uint32, "spectrum-slice-spacing")

                        self.total_spectrum_slice_count = YLeaf(YType.uint32, "total-spectrum-slice-count")

                        self.spectrum_slice_power_info = YList(self)
                        self._segment_path = lambda: "spectrum-info"

                    def __setattr__(self, name, value):
                        self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.SpectrumInfo, ['first_slice_wavelength', 'spectrum_slice_spacing', 'total_spectrum_slice_count'], name, value)


                    class SpectrumSlicePowerInfo(Entity):
                        """
                        Power information of spectrum slice info
                        
                        .. attribute:: lower_frequency
                        
                        	Lower frequency of the specified PSD
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: rx_power
                        
                        	Received Power in dBm
                        	**type**\:  str
                        
                        	**length:** 0..32
                        
                        .. attribute:: rx_psd
                        
                        	Received Power spectral density in microwatts per megahertz, uW/MHz
                        	**type**\:  str
                        
                        	**length:** 0..32
                        
                        .. attribute:: slice_num
                        
                        	spectrum slice number
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: tx_power
                        
                        	Transmit Power in dBm
                        	**type**\:  str
                        
                        	**length:** 0..32
                        
                        .. attribute:: tx_psd
                        
                        	Transmit Power spectral density in microwatts per megahertz, uW/MHz
                        	**type**\:  str
                        
                        	**length:** 0..32
                        
                        .. attribute:: upper_frequency
                        
                        	Upper frequency of the specified PSD
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.SpectrumInfo.SpectrumSlicePowerInfo, self).__init__()

                            self.yang_name = "spectrum-slice-power-info"
                            self.yang_parent_name = "spectrum-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.lower_frequency = YLeaf(YType.uint64, "lower-frequency")

                            self.rx_power = YLeaf(YType.str, "rx-power")

                            self.rx_psd = YLeaf(YType.str, "rx-psd")

                            self.slice_num = YLeaf(YType.uint32, "slice-num")

                            self.tx_power = YLeaf(YType.str, "tx-power")

                            self.tx_psd = YLeaf(YType.str, "tx-psd")

                            self.upper_frequency = YLeaf(YType.uint64, "upper-frequency")
                            self._segment_path = lambda: "spectrum-slice-power-info"

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.SpectrumInfo.SpectrumSlicePowerInfo, ['lower_frequency', 'rx_power', 'rx_psd', 'slice_num', 'tx_power', 'tx_psd', 'upper_frequency'], name, value)


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
                    
                    .. attribute:: optics_pid
                    
                    	Transceiver optics pid
                    	**type**\:  str
                    
                    .. attribute:: optics_serial_no
                    
                    	Transceiver serial number
                    	**type**\:  str
                    
                    .. attribute:: optics_type
                    
                    	Transceiver optics type
                    	**type**\:  str
                    
                    .. attribute:: optics_vendor_part
                    
                    	Transceiver vendors part number
                    	**type**\:  str
                    
                    .. attribute:: optics_vendor_rev
                    
                    	Transceiver vendors revision number
                    	**type**\:  str
                    
                    .. attribute:: optics_vid
                    
                    	Transceiver optics vid
                    	**type**\:  str
                    
                    .. attribute:: otn_application_code
                    
                    	Otn Application Code
                    	**type**\:   :py:class:`OtnApplicationCode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OtnApplicationCode>`
                    
                    .. attribute:: oui_no
                    
                    	Transceiver optics type
                    	**type**\:  str
                    
                    .. attribute:: sonet_application_code
                    
                    	Sonet Application Code
                    	**type**\:   :py:class:`SonetApplicationCode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.SonetApplicationCode>`
                    
                    .. attribute:: vendor_info
                    
                    	Vendor Information
                    	**type**\:  str
                    
                    .. attribute:: vendor_name
                    
                    	Transceiver optics vendor name
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'controller-optics-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.TransceiverInfo, self).__init__()

                        self.yang_name = "transceiver-info"
                        self.yang_parent_name = "optics-info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.adapter_vendor_info = YLeaf(YType.str, "adapter-vendor-info")

                        self.connector_type = YLeaf(YType.enumeration, "connector-type")

                        self.date = YLeaf(YType.str, "date")

                        self.ethernet_compliance_code = YLeaf(YType.enumeration, "ethernet-compliance-code")

                        self.internal_temperature = YLeaf(YType.int32, "internal-temperature")

                        self.optics_pid = YLeaf(YType.str, "optics-pid")

                        self.optics_serial_no = YLeaf(YType.str, "optics-serial-no")

                        self.optics_type = YLeaf(YType.str, "optics-type")

                        self.optics_vendor_part = YLeaf(YType.str, "optics-vendor-part")

                        self.optics_vendor_rev = YLeaf(YType.str, "optics-vendor-rev")

                        self.optics_vid = YLeaf(YType.str, "optics-vid")

                        self.otn_application_code = YLeaf(YType.enumeration, "otn-application-code")

                        self.oui_no = YLeaf(YType.str, "oui-no")

                        self.sonet_application_code = YLeaf(YType.enumeration, "sonet-application-code")

                        self.vendor_info = YLeaf(YType.str, "vendor-info")

                        self.vendor_name = YLeaf(YType.str, "vendor-name")
                        self._segment_path = lambda: "transceiver-info"

                    def __setattr__(self, name, value):
                        self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.TransceiverInfo, ['adapter_vendor_info', 'connector_type', 'date', 'ethernet_compliance_code', 'internal_temperature', 'optics_pid', 'optics_serial_no', 'optics_type', 'optics_vendor_part', 'optics_vendor_rev', 'optics_vid', 'otn_application_code', 'oui_no', 'sonet_application_code', 'vendor_info', 'vendor_name'], name, value)


            class OpticsLanes(Entity):
                """
                All Optics Port operational data
                
                .. attribute:: optics_lane
                
                	Lane Information
                	**type**\: list of    :py:class:`OpticsLane <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane>`
                
                

                """

                _prefix = 'controller-optics-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(OpticsOper.OpticsPorts.OpticsPort.OpticsLanes, self).__init__()

                    self.yang_name = "optics-lanes"
                    self.yang_parent_name = "optics-port"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"optics-lane" : ("optics_lane", OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane)}

                    self.optics_lane = YList(self)
                    self._segment_path = lambda: "optics-lanes"

                def __setattr__(self, name, value):
                    self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsLanes, [], name, value)


                class OpticsLane(Entity):
                    """
                    Lane Information
                    
                    .. attribute:: number  <key>
                    
                    	Lane Index
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: frequency_offset
                    
                    	Frequency Offset read from hw in unit of MHz
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
                    
                    	Output frequency read from hw in the unit 100MHz
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
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane, self).__init__()

                        self.yang_name = "optics-lane"
                        self.yang_parent_name = "optics-lanes"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"lane-alarm-info" : ("lane_alarm_info", OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo)}
                        self._child_list_classes = {}

                        self.number = YLeaf(YType.int32, "number")

                        self.frequency_offset = YLeaf(YType.int32, "frequency-offset")

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
                        self._segment_path = lambda: "optics-lane" + "[number='" + self.number.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane, ['number', 'frequency_offset', 'lane_index', 'laser_bias_current_milli_amps', 'laser_bias_current_percent', 'output_frequency', 'receive_power', 'receive_signal_power', 'transmit_power', 'transmit_signal_power'], name, value)


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
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo, self).__init__()

                            self.yang_name = "lane-alarm-info"
                            self.yang_parent_name = "optics-lane"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"high-lbc" : ("high_lbc", OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.HighLbc), "high-rx-power" : ("high_rx_power", OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.HighRxPower), "high-tx-power" : ("high_tx_power", OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.HighTxPower), "low-rx-power" : ("low_rx_power", OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.LowRxPower), "low-tx-power" : ("low_tx_power", OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.LowTxPower)}
                            self._child_list_classes = {}

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
                            self._segment_path = lambda: "lane-alarm-info"


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
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.HighLbc, self).__init__()

                                self.yang_name = "high-lbc"
                                self.yang_parent_name = "lane-alarm-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.counter = YLeaf(YType.uint32, "counter")

                                self.is_detected = YLeaf(YType.boolean, "is-detected")
                                self._segment_path = lambda: "high-lbc"

                            def __setattr__(self, name, value):
                                self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.HighLbc, ['counter', 'is_detected'], name, value)


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
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.HighRxPower, self).__init__()

                                self.yang_name = "high-rx-power"
                                self.yang_parent_name = "lane-alarm-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.counter = YLeaf(YType.uint32, "counter")

                                self.is_detected = YLeaf(YType.boolean, "is-detected")
                                self._segment_path = lambda: "high-rx-power"

                            def __setattr__(self, name, value):
                                self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.HighRxPower, ['counter', 'is_detected'], name, value)


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
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.HighTxPower, self).__init__()

                                self.yang_name = "high-tx-power"
                                self.yang_parent_name = "lane-alarm-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.counter = YLeaf(YType.uint32, "counter")

                                self.is_detected = YLeaf(YType.boolean, "is-detected")
                                self._segment_path = lambda: "high-tx-power"

                            def __setattr__(self, name, value):
                                self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.HighTxPower, ['counter', 'is_detected'], name, value)


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
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.LowRxPower, self).__init__()

                                self.yang_name = "low-rx-power"
                                self.yang_parent_name = "lane-alarm-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.counter = YLeaf(YType.uint32, "counter")

                                self.is_detected = YLeaf(YType.boolean, "is-detected")
                                self._segment_path = lambda: "low-rx-power"

                            def __setattr__(self, name, value):
                                self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.LowRxPower, ['counter', 'is_detected'], name, value)


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
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.LowTxPower, self).__init__()

                                self.yang_name = "low-tx-power"
                                self.yang_parent_name = "lane-alarm-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.counter = YLeaf(YType.uint32, "counter")

                                self.is_detected = YLeaf(YType.boolean, "is-detected")
                                self._segment_path = lambda: "low-tx-power"

                            def __setattr__(self, name, value):
                                self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.LowTxPower, ['counter', 'is_detected'], name, value)

    def clone_ptr(self):
        self._top_entity = OpticsOper()
        return self._top_entity

