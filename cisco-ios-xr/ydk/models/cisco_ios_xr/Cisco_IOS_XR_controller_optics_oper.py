""" Cisco_IOS_XR_controller_optics_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR controller\-optics package operational data.

This module contains definitions
for the following management objects\:
  optics\-oper\: Optics operational data

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class EthernetPmd(Enum):
    """
    EthernetPmd (Enum Class)

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
    FiberConnector (Enum Class)

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
    Optics (Enum Class)

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


class OpticsAinsStateEt(Enum):
    """
    OpticsAinsStateEt (Enum Class)

    Optics ains state et

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


class OpticsAmplifierControlMode(Enum):
    """
    OpticsAmplifierControlMode (Enum Class)

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
    OpticsAmplifierGainRange (Enum Class)

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
    OpticsAmplifierSafetyControlMode (Enum Class)

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
    OpticsControllerState (Enum Class)

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
    OpticsFec (Enum Class)

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

    .. data:: fec_not_set = 32

    	FEC DISABLED

    .. data:: fec_cl91 = 64

    	FEC CL91

    """

    fec_none = Enum.YLeaf(0, "fec-none")

    fec_hg15 = Enum.YLeaf(1, "fec-hg15")

    fec_hg25 = Enum.YLeaf(2, "fec-hg25")

    fec_hg15_de = Enum.YLeaf(4, "fec-hg15-de")

    fec_hg25_de = Enum.YLeaf(8, "fec-hg25-de")

    fec_enabled = Enum.YLeaf(16, "fec-enabled")

    fec_not_set = Enum.YLeaf(32, "fec-not-set")

    fec_cl91 = Enum.YLeaf(64, "fec-cl91")


class OpticsFormFactor(Enum):
    """
    OpticsFormFactor (Enum Class)

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

    .. data:: cfp2_aco = 11

    	CFP2 ACO

    .. data:: cfp2_dco = 12

    	CFP2 DCO

    .. data:: cfp4 = 13

    	CFP4

    .. data:: xfp = 14

    	XFP

    .. data:: x2 = 15

    	X2

    .. data:: non_pluggable = 16

    	Non pluggable

    .. data:: other = 17

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

    cfp2_aco = Enum.YLeaf(11, "cfp2-aco")

    cfp2_dco = Enum.YLeaf(12, "cfp2-dco")

    cfp4 = Enum.YLeaf(13, "cfp4")

    xfp = Enum.YLeaf(14, "xfp")

    x2 = Enum.YLeaf(15, "x2")

    non_pluggable = Enum.YLeaf(16, "non-pluggable")

    other = Enum.YLeaf(17, "other")


class OpticsLaserState(Enum):
    """
    OpticsLaserState (Enum Class)

    Optics laser state

    .. data:: on = 0

    	On

    .. data:: off = 1

    	Off

    .. data:: unknown = 2

    	Unknown

    .. data:: apr = 3

    	Apr

    .. data:: na = 4

    	N/A

    """

    on = Enum.YLeaf(0, "on")

    off = Enum.YLeaf(1, "off")

    unknown = Enum.YLeaf(2, "unknown")

    apr = Enum.YLeaf(3, "apr")

    na = Enum.YLeaf(4, "na")


class OpticsLedState(Enum):
    """
    OpticsLedState (Enum Class)

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


class OpticsModulation(Enum):
    """
    OpticsModulation (Enum Class)

    Optics modulation

    .. data:: mod_bpsk = 1

    	BPSK

    .. data:: mod_qpsk = 2

    	QPSK

    .. data:: mod_8qam = 3

    	8QAM

    .. data:: mod_16qam = 4

    	16QAM

    .. data:: mod_32qam = 5

    	32QAM

    .. data:: mod_64qam = 6

    	64QAM

    .. data:: mod_bpsk_qpsk = 7

    	BPSK QPSK

    .. data:: mod_qpsk_8qam = 8

    	QPSK 8QAM

    .. data:: mod_8qam_16qam = 9

    	8QAM 16QAM

    .. data:: mode_16qam_32qam = 10

    	16QAM 32QAM

    .. data:: mod_32qam_64qam = 11

    	32QAM 64QAM

    """

    mod_bpsk = Enum.YLeaf(1, "mod-bpsk")

    mod_qpsk = Enum.YLeaf(2, "mod-qpsk")

    mod_8qam = Enum.YLeaf(3, "mod-8qam")

    mod_16qam = Enum.YLeaf(4, "mod-16qam")

    mod_32qam = Enum.YLeaf(5, "mod-32qam")

    mod_64qam = Enum.YLeaf(6, "mod-64qam")

    mod_bpsk_qpsk = Enum.YLeaf(7, "mod-bpsk-qpsk")

    mod_qpsk_8qam = Enum.YLeaf(8, "mod-qpsk-8qam")

    mod_8qam_16qam = Enum.YLeaf(9, "mod-8qam-16qam")

    mode_16qam_32qam = Enum.YLeaf(10, "mode-16qam-32qam")

    mod_32qam_64qam = Enum.YLeaf(11, "mod-32qam-64qam")


class OpticsPhy(Enum):
    """
    OpticsPhy (Enum Class)

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

    .. data:: ten_x_ten_gig_e_long_reach_one_lane = 57

    	Long Reach 1 Lane

    .. data:: ten_x_ten_gig_e_extended_reach_one_lane = 58

    	Extended Reach 1 Lane

    .. data:: passive_copper_one_lane = 59

    	Passive Copper One Lane

    .. data:: ten_gig_ecwdm = 60

    	TenGigE CWDM One Lane

    .. data:: one_gig_ecwdm = 61

    	One GigE CWDM One Lane

    .. data:: one_gig_edwdm = 62

    	One GigE DWDM One Lane

    .. data:: fx_one_lane = 63

    	FX One Lane

    .. data:: ten_gig_emrdwdm = 64

    	TenGigE Multi Rate DWDM 1 Lane

    .. data:: ten_gig_e_edge_performance = 65

    	TenGigE Edge Performance 1 Lane

    .. data:: one_gig_csfp = 66

    	OneGig CSFP optics

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

    ten_x_ten_gig_e_long_reach_one_lane = Enum.YLeaf(57, "ten-x-ten-gig-e-long-reach-one-lane")

    ten_x_ten_gig_e_extended_reach_one_lane = Enum.YLeaf(58, "ten-x-ten-gig-e-extended-reach-one-lane")

    passive_copper_one_lane = Enum.YLeaf(59, "passive-copper-one-lane")

    ten_gig_ecwdm = Enum.YLeaf(60, "ten-gig-ecwdm")

    one_gig_ecwdm = Enum.YLeaf(61, "one-gig-ecwdm")

    one_gig_edwdm = Enum.YLeaf(62, "one-gig-edwdm")

    fx_one_lane = Enum.YLeaf(63, "fx-one-lane")

    ten_gig_emrdwdm = Enum.YLeaf(64, "ten-gig-emrdwdm")

    ten_gig_e_edge_performance = Enum.YLeaf(65, "ten-gig-e-edge-performance")

    one_gig_csfp = Enum.YLeaf(66, "one-gig-csfp")


class OpticsPort(Enum):
    """
    OpticsPort (Enum Class)

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
    OpticsPortStatus (Enum Class)

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
    OpticsTas (Enum Class)

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
    OpticsWaveBand (Enum Class)

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
    OtnApplicationCode (Enum Class)

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
    SonetApplicationCode (Enum Class)

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
    	**type**\:  :py:class:`OpticsPorts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts>`
    
    

    """

    _prefix = 'controller-optics-oper'
    _revision = '2017-09-07'

    def __init__(self):
        super(OpticsOper, self).__init__()
        self._top_entity = None

        self.yang_name = "optics-oper"
        self.yang_parent_name = "Cisco-IOS-XR-controller-optics-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("optics-ports", ("optics_ports", OpticsOper.OpticsPorts))])
        self._leafs = OrderedDict()

        self.optics_ports = OpticsOper.OpticsPorts()
        self.optics_ports.parent = self
        self._children_name_map["optics_ports"] = "optics-ports"
        self._segment_path = lambda: "Cisco-IOS-XR-controller-optics-oper:optics-oper"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(OpticsOper, [], name, value)


    class OpticsPorts(Entity):
        """
        All Optics Port operational data
        
        .. attribute:: optics_port
        
        	Optics operational data
        	**type**\: list of  		 :py:class:`OpticsPort <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort>`
        
        

        """

        _prefix = 'controller-optics-oper'
        _revision = '2017-09-07'

        def __init__(self):
            super(OpticsOper.OpticsPorts, self).__init__()

            self.yang_name = "optics-ports"
            self.yang_parent_name = "optics-oper"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("optics-port", ("optics_port", OpticsOper.OpticsPorts.OpticsPort))])
            self._leafs = OrderedDict()

            self.optics_port = YList(self)
            self._segment_path = lambda: "optics-ports"
            self._absolute_path = lambda: "Cisco-IOS-XR-controller-optics-oper:optics-oper/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(OpticsOper.OpticsPorts, [], name, value)


        class OpticsPort(Entity):
            """
            Optics operational data
            
            .. attribute:: name  (key)
            
            	Port name
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
            
            .. attribute:: optics_dwdm_carrier_channel_map
            
            	Optics operational data
            	**type**\:  :py:class:`OpticsDwdmCarrierChannelMap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsDwdmCarrierChannelMap>`
            
            .. attribute:: ots_spectrum_info
            
            	Ots Spectrum Operational data
            	**type**\:  :py:class:`OtsSpectrumInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OtsSpectrumInfo>`
            
            .. attribute:: optics_dwdm_carrier_channel_map_flexi
            
            	Optics operational data
            	**type**\:  :py:class:`OpticsDwdmCarrierChannelMapFlexi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsDwdmCarrierChannelMapFlexi>`
            
            .. attribute:: optics_info
            
            	Optics operational data
            	**type**\:  :py:class:`OpticsInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo>`
            
            .. attribute:: optics_lanes
            
            	All Optics Port operational data
            	**type**\:  :py:class:`OpticsLanes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsLanes>`
            
            .. attribute:: optics_db_info
            
            	Optics operational data
            	**type**\:  :py:class:`OpticsDbInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsDbInfo>`
            
            

            """

            _prefix = 'controller-optics-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(OpticsOper.OpticsPorts.OpticsPort, self).__init__()

                self.yang_name = "optics-port"
                self.yang_parent_name = "optics-ports"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['name']
                self._child_classes = OrderedDict([("optics-dwdm-carrier-channel-map", ("optics_dwdm_carrier_channel_map", OpticsOper.OpticsPorts.OpticsPort.OpticsDwdmCarrierChannelMap)), ("ots-spectrum-info", ("ots_spectrum_info", OpticsOper.OpticsPorts.OpticsPort.OtsSpectrumInfo)), ("optics-dwdm-carrier-channel-map-flexi", ("optics_dwdm_carrier_channel_map_flexi", OpticsOper.OpticsPorts.OpticsPort.OpticsDwdmCarrierChannelMapFlexi)), ("optics-info", ("optics_info", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo)), ("optics-lanes", ("optics_lanes", OpticsOper.OpticsPorts.OpticsPort.OpticsLanes)), ("optics-db-info", ("optics_db_info", OpticsOper.OpticsPorts.OpticsPort.OpticsDbInfo))])
                self._leafs = OrderedDict([
                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                ])
                self.name = None

                self.optics_dwdm_carrier_channel_map = OpticsOper.OpticsPorts.OpticsPort.OpticsDwdmCarrierChannelMap()
                self.optics_dwdm_carrier_channel_map.parent = self
                self._children_name_map["optics_dwdm_carrier_channel_map"] = "optics-dwdm-carrier-channel-map"

                self.ots_spectrum_info = OpticsOper.OpticsPorts.OpticsPort.OtsSpectrumInfo()
                self.ots_spectrum_info.parent = self
                self._children_name_map["ots_spectrum_info"] = "ots-spectrum-info"

                self.optics_dwdm_carrier_channel_map_flexi = OpticsOper.OpticsPorts.OpticsPort.OpticsDwdmCarrierChannelMapFlexi()
                self.optics_dwdm_carrier_channel_map_flexi.parent = self
                self._children_name_map["optics_dwdm_carrier_channel_map_flexi"] = "optics-dwdm-carrier-channel-map-flexi"

                self.optics_info = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo()
                self.optics_info.parent = self
                self._children_name_map["optics_info"] = "optics-info"

                self.optics_lanes = OpticsOper.OpticsPorts.OpticsPort.OpticsLanes()
                self.optics_lanes.parent = self
                self._children_name_map["optics_lanes"] = "optics-lanes"

                self.optics_db_info = OpticsOper.OpticsPorts.OpticsPort.OpticsDbInfo()
                self.optics_db_info.parent = self
                self._children_name_map["optics_db_info"] = "optics-db-info"
                self._segment_path = lambda: "optics-port" + "[name='" + str(self.name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-controller-optics-oper:optics-oper/optics-ports/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort, ['name'], name, value)


            class OpticsDwdmCarrierChannelMap(Entity):
                """
                Optics operational data
                
                .. attribute:: dwdm_carrier_band
                
                	DWDM carrier band
                	**type**\:  :py:class:`OpticsWaveBand <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsWaveBand>`
                
                .. attribute:: dwdm_carrier_min
                
                	Lowest DWDM carrier supported
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: dwdm_carrier_max
                
                	Highest DWDM carrier supported
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: dwdm_carrier_map_info
                
                	DWDM carrier mapping info
                	**type**\: list of  		 :py:class:`DwdmCarrierMapInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsDwdmCarrierChannelMap.DwdmCarrierMapInfo>`
                
                

                """

                _prefix = 'controller-optics-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(OpticsOper.OpticsPorts.OpticsPort.OpticsDwdmCarrierChannelMap, self).__init__()

                    self.yang_name = "optics-dwdm-carrier-channel-map"
                    self.yang_parent_name = "optics-port"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("dwdm-carrier-map-info", ("dwdm_carrier_map_info", OpticsOper.OpticsPorts.OpticsPort.OpticsDwdmCarrierChannelMap.DwdmCarrierMapInfo))])
                    self._leafs = OrderedDict([
                        ('dwdm_carrier_band', (YLeaf(YType.enumeration, 'dwdm-carrier-band'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsWaveBand', '')])),
                        ('dwdm_carrier_min', (YLeaf(YType.uint32, 'dwdm-carrier-min'), ['int'])),
                        ('dwdm_carrier_max', (YLeaf(YType.uint32, 'dwdm-carrier-max'), ['int'])),
                    ])
                    self.dwdm_carrier_band = None
                    self.dwdm_carrier_min = None
                    self.dwdm_carrier_max = None

                    self.dwdm_carrier_map_info = YList(self)
                    self._segment_path = lambda: "optics-dwdm-carrier-channel-map"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsDwdmCarrierChannelMap, ['dwdm_carrier_band', 'dwdm_carrier_min', 'dwdm_carrier_max'], name, value)


                class DwdmCarrierMapInfo(Entity):
                    """
                    DWDM carrier mapping info
                    
                    .. attribute:: itu_chan_num
                    
                    	ITU channel number
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: g694_chan_num
                    
                    	G694 channel number
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: frequency
                    
                    	Frequency
                    	**type**\: str
                    
                    	**length:** 0..32
                    
                    .. attribute:: wavelength
                    
                    	Wavelength
                    	**type**\: str
                    
                    	**length:** 0..32
                    
                    

                    """

                    _prefix = 'controller-optics-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsDwdmCarrierChannelMap.DwdmCarrierMapInfo, self).__init__()

                        self.yang_name = "dwdm-carrier-map-info"
                        self.yang_parent_name = "optics-dwdm-carrier-channel-map"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('itu_chan_num', (YLeaf(YType.uint32, 'itu-chan-num'), ['int'])),
                            ('g694_chan_num', (YLeaf(YType.int32, 'g694-chan-num'), ['int'])),
                            ('frequency', (YLeaf(YType.str, 'frequency'), ['str'])),
                            ('wavelength', (YLeaf(YType.str, 'wavelength'), ['str'])),
                        ])
                        self.itu_chan_num = None
                        self.g694_chan_num = None
                        self.frequency = None
                        self.wavelength = None
                        self._segment_path = lambda: "dwdm-carrier-map-info"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsDwdmCarrierChannelMap.DwdmCarrierMapInfo, ['itu_chan_num', 'g694_chan_num', 'frequency', 'wavelength'], name, value)


            class OtsSpectrumInfo(Entity):
                """
                Ots Spectrum Operational data
                
                .. attribute:: spectrum_info
                
                	OTS Spectrum information
                	**type**\:  :py:class:`SpectrumInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OtsSpectrumInfo.SpectrumInfo>`
                
                

                """

                _prefix = 'controller-optics-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(OpticsOper.OpticsPorts.OpticsPort.OtsSpectrumInfo, self).__init__()

                    self.yang_name = "ots-spectrum-info"
                    self.yang_parent_name = "optics-port"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("spectrum-info", ("spectrum_info", OpticsOper.OpticsPorts.OpticsPort.OtsSpectrumInfo.SpectrumInfo))])
                    self._leafs = OrderedDict()

                    self.spectrum_info = OpticsOper.OpticsPorts.OpticsPort.OtsSpectrumInfo.SpectrumInfo()
                    self.spectrum_info.parent = self
                    self._children_name_map["spectrum_info"] = "spectrum-info"
                    self._segment_path = lambda: "ots-spectrum-info"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OtsSpectrumInfo, [], name, value)


                class SpectrumInfo(Entity):
                    """
                    OTS Spectrum information
                    
                    .. attribute:: total_spectrum_slice_count
                    
                    	Total number of slices in Spectrum
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: spectrum_slice_spacing
                    
                    	Spacing between spectrum slices
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: first_slice_wavelength
                    
                    	Wavelength of first slice
                    	**type**\: str
                    
                    	**length:** 0..32
                    
                    .. attribute:: spectrum_slice_power_info
                    
                    	Power information of spectrum slice info
                    	**type**\: list of  		 :py:class:`SpectrumSlicePowerInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OtsSpectrumInfo.SpectrumInfo.SpectrumSlicePowerInfo>`
                    
                    

                    """

                    _prefix = 'controller-optics-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(OpticsOper.OpticsPorts.OpticsPort.OtsSpectrumInfo.SpectrumInfo, self).__init__()

                        self.yang_name = "spectrum-info"
                        self.yang_parent_name = "ots-spectrum-info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("spectrum-slice-power-info", ("spectrum_slice_power_info", OpticsOper.OpticsPorts.OpticsPort.OtsSpectrumInfo.SpectrumInfo.SpectrumSlicePowerInfo))])
                        self._leafs = OrderedDict([
                            ('total_spectrum_slice_count', (YLeaf(YType.uint32, 'total-spectrum-slice-count'), ['int'])),
                            ('spectrum_slice_spacing', (YLeaf(YType.uint32, 'spectrum-slice-spacing'), ['int'])),
                            ('first_slice_wavelength', (YLeaf(YType.str, 'first-slice-wavelength'), ['str'])),
                        ])
                        self.total_spectrum_slice_count = None
                        self.spectrum_slice_spacing = None
                        self.first_slice_wavelength = None

                        self.spectrum_slice_power_info = YList(self)
                        self._segment_path = lambda: "spectrum-info"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OtsSpectrumInfo.SpectrumInfo, ['total_spectrum_slice_count', 'spectrum_slice_spacing', 'first_slice_wavelength'], name, value)


                    class SpectrumSlicePowerInfo(Entity):
                        """
                        Power information of spectrum slice info
                        
                        .. attribute:: slice_num
                        
                        	spectrum slice number
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: lower_frequency
                        
                        	Lower frequency of the specified PSD
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: upper_frequency
                        
                        	Upper frequency of the specified PSD
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: rx_power
                        
                        	Received Power in dBm multiplied by 100
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: tx_power
                        
                        	Transmit Power in dBm multiplied by 100
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: rx_psd
                        
                        	Received Power spectral density in microwatts per megahertz, uW/MHz
                        	**type**\: str
                        
                        	**length:** 0..16
                        
                        .. attribute:: tx_psd
                        
                        	Transmit Power spectral density in microwatts per megahertz, uW/MHz
                        	**type**\: str
                        
                        	**length:** 0..16
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OtsSpectrumInfo.SpectrumInfo.SpectrumSlicePowerInfo, self).__init__()

                            self.yang_name = "spectrum-slice-power-info"
                            self.yang_parent_name = "spectrum-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('slice_num', (YLeaf(YType.uint32, 'slice-num'), ['int'])),
                                ('lower_frequency', (YLeaf(YType.uint64, 'lower-frequency'), ['int'])),
                                ('upper_frequency', (YLeaf(YType.uint64, 'upper-frequency'), ['int'])),
                                ('rx_power', (YLeaf(YType.int32, 'rx-power'), ['int'])),
                                ('tx_power', (YLeaf(YType.int32, 'tx-power'), ['int'])),
                                ('rx_psd', (YLeaf(YType.str, 'rx-psd'), ['str'])),
                                ('tx_psd', (YLeaf(YType.str, 'tx-psd'), ['str'])),
                            ])
                            self.slice_num = None
                            self.lower_frequency = None
                            self.upper_frequency = None
                            self.rx_power = None
                            self.tx_power = None
                            self.rx_psd = None
                            self.tx_psd = None
                            self._segment_path = lambda: "spectrum-slice-power-info"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OtsSpectrumInfo.SpectrumInfo.SpectrumSlicePowerInfo, ['slice_num', 'lower_frequency', 'upper_frequency', 'rx_power', 'tx_power', 'rx_psd', 'tx_psd'], name, value)


            class OpticsDwdmCarrierChannelMapFlexi(Entity):
                """
                Optics operational data
                
                .. attribute:: dwdm_carrier_band
                
                	DWDM carrier band
                	**type**\:  :py:class:`OpticsWaveBand <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsWaveBand>`
                
                .. attribute:: dwdm_carrier_min
                
                	Lowest DWDM carrier supported
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: dwdm_carrier_max
                
                	Highest DWDM carrier supported
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: dwdm_carrier_map_info
                
                	DWDM carrier mapping info
                	**type**\: list of  		 :py:class:`DwdmCarrierMapInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsDwdmCarrierChannelMapFlexi.DwdmCarrierMapInfo>`
                
                

                """

                _prefix = 'controller-optics-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(OpticsOper.OpticsPorts.OpticsPort.OpticsDwdmCarrierChannelMapFlexi, self).__init__()

                    self.yang_name = "optics-dwdm-carrier-channel-map-flexi"
                    self.yang_parent_name = "optics-port"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("dwdm-carrier-map-info", ("dwdm_carrier_map_info", OpticsOper.OpticsPorts.OpticsPort.OpticsDwdmCarrierChannelMapFlexi.DwdmCarrierMapInfo))])
                    self._leafs = OrderedDict([
                        ('dwdm_carrier_band', (YLeaf(YType.enumeration, 'dwdm-carrier-band'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsWaveBand', '')])),
                        ('dwdm_carrier_min', (YLeaf(YType.uint32, 'dwdm-carrier-min'), ['int'])),
                        ('dwdm_carrier_max', (YLeaf(YType.uint32, 'dwdm-carrier-max'), ['int'])),
                    ])
                    self.dwdm_carrier_band = None
                    self.dwdm_carrier_min = None
                    self.dwdm_carrier_max = None

                    self.dwdm_carrier_map_info = YList(self)
                    self._segment_path = lambda: "optics-dwdm-carrier-channel-map-flexi"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsDwdmCarrierChannelMapFlexi, ['dwdm_carrier_band', 'dwdm_carrier_min', 'dwdm_carrier_max'], name, value)


                class DwdmCarrierMapInfo(Entity):
                    """
                    DWDM carrier mapping info
                    
                    .. attribute:: itu_chan_num
                    
                    	ITU channel number
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: g694_chan_num
                    
                    	G694 channel number
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: frequency
                    
                    	Frequency
                    	**type**\: str
                    
                    	**length:** 0..32
                    
                    .. attribute:: wavelength
                    
                    	Wavelength
                    	**type**\: str
                    
                    	**length:** 0..32
                    
                    

                    """

                    _prefix = 'controller-optics-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsDwdmCarrierChannelMapFlexi.DwdmCarrierMapInfo, self).__init__()

                        self.yang_name = "dwdm-carrier-map-info"
                        self.yang_parent_name = "optics-dwdm-carrier-channel-map-flexi"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('itu_chan_num', (YLeaf(YType.uint32, 'itu-chan-num'), ['int'])),
                            ('g694_chan_num', (YLeaf(YType.int32, 'g694-chan-num'), ['int'])),
                            ('frequency', (YLeaf(YType.str, 'frequency'), ['str'])),
                            ('wavelength', (YLeaf(YType.str, 'wavelength'), ['str'])),
                        ])
                        self.itu_chan_num = None
                        self.g694_chan_num = None
                        self.frequency = None
                        self.wavelength = None
                        self._segment_path = lambda: "dwdm-carrier-map-info"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsDwdmCarrierChannelMapFlexi.DwdmCarrierMapInfo, ['itu_chan_num', 'g694_chan_num', 'frequency', 'wavelength'], name, value)


            class OpticsInfo(Entity):
                """
                Optics operational data
                
                .. attribute:: network_srlg_info
                
                	Network SRLG information
                	**type**\:  :py:class:`NetworkSrlgInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.NetworkSrlgInfo>`
                
                .. attribute:: optics_alarm_info
                
                	Optics Alarm Information
                	**type**\:  :py:class:`OpticsAlarmInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo>`
                
                .. attribute:: ots_alarm_info
                
                	Ots Alarm Information
                	**type**\:  :py:class:`OtsAlarmInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo>`
                
                .. attribute:: transceiver_info
                
                	Transceiver Vendor Details
                	**type**\:  :py:class:`TransceiverInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.TransceiverInfo>`
                
                .. attribute:: ext_param_val
                
                	Extended optics parameters
                	**type**\:  :py:class:`ExtParamVal <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtParamVal>`
                
                .. attribute:: ext_param_threshold_val
                
                	Extended optics parameters threshold values
                	**type**\:  :py:class:`ExtParamThresholdVal <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtParamThresholdVal>`
                
                .. attribute:: extended_alarm_alarm_info
                
                	Extended DOM alarm Information
                	**type**\:  :py:class:`ExtendedAlarmAlarmInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo>`
                
                .. attribute:: ains_info
                
                	AINS information
                	**type**\:  :py:class:`AinsInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.AinsInfo>`
                
                .. attribute:: transport_admin_state
                
                	Transport Admin State
                	**type**\:  :py:class:`OpticsTas <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsTas>`
                
                .. attribute:: optics_present
                
                	Is Optics Present?
                	**type**\: bool
                
                .. attribute:: optics_type
                
                	Old Optics type name, Use Derived Optics type
                	**type**\:  :py:class:`Optics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.Optics>`
                
                .. attribute:: derived_optics_type
                
                	Derived Optics type name
                	**type**\: str
                
                .. attribute:: optics_module
                
                	Optics module name
                	**type**\: str
                
                .. attribute:: dwdm_carrier_band
                
                	DWDM Carrier Band information
                	**type**\:  :py:class:`OpticsWaveBand <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsWaveBand>`
                
                .. attribute:: dwdm_carrier_channel
                
                	Current ITU DWDM Carrier channel number
                	**type**\: str
                
                .. attribute:: dwdm_carrier_frequency
                
                	DWDM Carrier frequency read from hw in the units of  1THz
                	**type**\: str
                
                .. attribute:: dwdm_carrier_wavelength
                
                	Wavelength of color optics 0.001nm
                	**type**\: str
                
                .. attribute:: grey_wavelength
                
                	Wavelength of grey optics 0.01nm
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: rx_low_threshold
                
                	Rx Low threshold value in units of 0.1dBm
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: rx_high_threshold
                
                	Rx High threshold value in units of 0.1dBm
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: lbc_high_threshold
                
                	LBC High threshold value in units of percentage
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                	**units**\: percentage
                
                .. attribute:: tx_low_threshold
                
                	Tx Low threshold value in units of 0.1dBm
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: tx_high_threshold
                
                	Tx High threshold value in units of 0.1dBm
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: lbc_th_high_default
                
                	LBC high threshold default value in units of 0 .001mA
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: lbc_th_low_default
                
                	LBC low threshold default value in units of 0 .001mA
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: temp_low_threshold
                
                	Temp Low threshold value in the units 0.01C
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: temp_high_threshold
                
                	Temp High threshold value in the units of 0.01C
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: volt_low_threshold
                
                	Volt Low threshold value in the units of 0.01V
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: volt_high_threshold
                
                	Volt High threshold value in the units of 0.01V
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: cd
                
                	Chromatic Dispersion ps/nm
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: cd_min
                
                	Chromatic Dispersion Min ps/nm
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: cd_max
                
                	Chromatic Dispersion Max ps/nm
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: cd_low_threshold
                
                	Chromatic Dispersion low threshold ps/nm
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: cd_high_threshold
                
                	Chromatic Dispersion high threshold ps/nm
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: osnr_low_threshold
                
                	OSNR low threshold in 0.01 dB
                	**type**\: str
                
                .. attribute:: dgd_high_threshold
                
                	DGD high threshold in 0.1 ps
                	**type**\: str
                
                .. attribute:: polarization_mode_dispersion
                
                	Polarization Mode Dispersion 0.1ps
                	**type**\: str
                
                .. attribute:: second_order_polarization_mode_dispersion
                
                	Second Order Polarization Mode Dispersion 0 .1ps^2
                	**type**\: str
                
                .. attribute:: optical_signal_to_noise_ratio
                
                	Optical Signal to Noise Ratio dB
                	**type**\: str
                
                .. attribute:: polarization_dependent_loss
                
                	Polarization Dependent Loss dB
                	**type**\: str
                
                .. attribute:: polarization_change_rate
                
                	Polarization Change Rate rad/s
                	**type**\: str
                
                .. attribute:: differential_group_delay
                
                	Differential Group Delay ps
                	**type**\: str
                
                .. attribute:: phase_noise
                
                	Phase Noise dB
                	**type**\: str
                
                .. attribute:: pm_enable
                
                	PmEable or Disable
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: laser_state
                
                	Showing laser state.Either ON or OFF or unknown
                	**type**\:  :py:class:`OpticsLaserState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsLaserState>`
                
                .. attribute:: modulation_type
                
                	Available Modulation Types
                	**type**\:  :py:class:`OpticsModulation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsModulation>`
                
                .. attribute:: led_state
                
                	Showing Current Colour of led state
                	**type**\:  :py:class:`OpticsLedState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsLedState>`
                
                .. attribute:: controller_state
                
                	Optics controller state\: Up, Down or Administratively Down
                	**type**\:  :py:class:`OpticsControllerState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsControllerState>`
                
                .. attribute:: form_factor
                
                	Optics form factor
                	**type**\:  :py:class:`OpticsFormFactor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsFormFactor>`
                
                .. attribute:: phy_type
                
                	Optics physical type
                	**type**\:  :py:class:`OpticsPhy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsPhy>`
                
                .. attribute:: cfg_tx_power
                
                	Configured Tx power value in units of 0.1dB
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: cfg_tx_power_configurable
                
                	TX Power Configuration is supported or not
                	**type**\: bool
                
                .. attribute:: temperature
                
                	Temperature value in units of 0.01 C
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: voltage
                
                	Voltage value in units of 0.01V
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: display_volt_temp
                
                	Display Volt/Temp ?
                	**type**\: bool
                
                .. attribute:: cd_configurable
                
                	CD Configurable is supported or not
                	**type**\: bool
                
                .. attribute:: optics_fec
                
                	Optics FEC
                	**type**\:  :py:class:`OpticsFec <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsFec>`
                
                .. attribute:: skip_snmp_pm_table
                
                	PM enabled or not
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: port_type
                
                	Showing port type
                	**type**\:  :py:class:`OpticsPort <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsPort>`
                
                .. attribute:: port_status
                
                	Showing port status
                	**type**\:  :py:class:`OpticsPortStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsPortStatus>`
                
                .. attribute:: rx_voa_attenuation
                
                	Rx Voa Attenuation in the units of 0.01dBm
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: tx_voa_attenuation
                
                	Tx Voa Attenuation in the units of 0.01dBm
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: ampli_gain
                
                	Ampli Gain in the units of 0.01dBm
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: ampli_tilt
                
                	Ampli Tilt in the units of 0.01dBm
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: rx_power_th_configurable
                
                	rx power th configurable
                	**type**\: bool
                
                .. attribute:: tx_power_th_configurable
                
                	tx power th configurable
                	**type**\: bool
                
                .. attribute:: rx_voa_attenuation_config_val
                
                	RX VOA attenuation configured value in units of 0.1dB
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: tx_voa_attenuation_config_val
                
                	TX VOA attenuation configured value in units of 0.1dB
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: ampli_control_mode_config_val
                
                	ampli control mode config val
                	**type**\:  :py:class:`OpticsAmplifierControlMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsAmplifierControlMode>`
                
                .. attribute:: ampli_gain_range_config_val
                
                	ampli gain range config val
                	**type**\:  :py:class:`OpticsAmplifierGainRange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsAmplifierGainRange>`
                
                .. attribute:: ampli_gain_config_val
                
                	Ampli gain configured value in units of 0.1dB
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: ampli_tilt_config_val
                
                	Ampli tilt configured value in units of 0.1dB
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: ampli_channel_power_config_val
                
                	Ampli channel power configured value in units of 0.1dBm
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: channel_power_max_delta_config_val
                
                	Channel power max delta configured value in units of 0.1 dBm
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: ampli_gain_thr_deg_low_config_val
                
                	Ampli gain low degrade threshold configured value in units of 0.1dBm
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: ampli_gain_thr_deg_high_config_val
                
                	Ampli gain high degrade threshold configured value in units of 0.1dBm
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: osri_config_val
                
                	osri config val
                	**type**\: bool
                
                .. attribute:: tx_config_val
                
                	tx config val
                	**type**\: bool
                
                .. attribute:: rx_config_val
                
                	rx config val
                	**type**\: bool
                
                .. attribute:: safety_control_mode_config_val
                
                	safety control mode config val
                	**type**\:  :py:class:`OpticsAmplifierSafetyControlMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsAmplifierSafetyControlMode>`
                
                .. attribute:: total_rx_power
                
                	Total Receive Power for Multi\-Lane Optics in units of 0.01 dBm
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: total_tx_power
                
                	Total Transmit Power for Multi\-Lane Optics in units of 0.01 dBm
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: is_bo_configured
                
                	Is BO configured ?
                	**type**\: bool
                
                .. attribute:: is_ext_param_valid
                
                	Are the Extended Parameters Valid ?
                	**type**\: bool
                
                .. attribute:: alarm_detected
                
                	Are there any alarms ?
                	**type**\: bool
                
                .. attribute:: rx_low_warning_threshold
                
                	Rx Low Warning threshold value in units of 0 .1dBm
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: rx_high_warning_threshold
                
                	Rx High Warning threshold value in units of 0 .1dBm
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: tx_low_warning_threshold
                
                	Tx Low Warning threshold value in units of 0 .1dBm
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: tx_high_warning_threshold
                
                	Tx High Warning threshold value in units of 0 .1dBm
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: lbc_th_high_warning_default
                
                	LBC high Warning threshold default value in units of 0.001mA
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: lbc_th_low_warning_default
                
                	LBC low warning threshold default value in units of 0.001mA
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: temp_low_warning_threshold
                
                	Temp Low warning threshold value in the units 0 .01C
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: temp_high_warning_threshold
                
                	Temp High warning threshold value in the units of 0.01C
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: volt_low_warning_threshold
                
                	Volt Low warning threshold value in the units of 0.01V
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: volt_high_warning_threshold
                
                	Volt High warning threshold value in the units of 0.01V
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: description
                
                	Controller description string
                	**type**\: str
                
                .. attribute:: ampli_gain_range
                
                	Ampli gain range
                	**type**\:  :py:class:`OpticsAmplifierGainRange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsAmplifierGainRange>`
                
                .. attribute:: safety_control_mode
                
                	Safety control mode
                	**type**\:  :py:class:`OpticsAmplifierSafetyControlMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsAmplifierSafetyControlMode>`
                
                .. attribute:: osri
                
                	OSRI
                	**type**\: bool
                
                .. attribute:: tx_enable
                
                	TX Enable
                	**type**\: bool
                
                .. attribute:: rx_enable
                
                	RX Enable
                	**type**\: bool
                
                .. attribute:: is_optics_type_string_valid
                
                	Is the Optics type string valid ?
                	**type**\: bool
                
                .. attribute:: optics_type_str
                
                	optics type String
                	**type**\: str
                
                .. attribute:: rx_low_threshold_current
                
                	Rx Low threshold actual value in units of 0.1dBm
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: rx_span_loss
                
                	RX Span Loss in units of 0.01 dB
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: tx_span_loss
                
                	TX Span Loss in units of 0.01 dB
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: baud_rate
                
                	Baud Rate in GBd
                	**type**\: str
                
                .. attribute:: bits_per_symbol
                
                	Bits per Symbol
                	**type**\: str
                
                .. attribute:: lane_data
                
                	Lane information
                	**type**\: list of  		 :py:class:`LaneData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData>`
                
                

                """

                _prefix = 'controller-optics-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo, self).__init__()

                    self.yang_name = "optics-info"
                    self.yang_parent_name = "optics-port"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("network-srlg-info", ("network_srlg_info", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.NetworkSrlgInfo)), ("optics-alarm-info", ("optics_alarm_info", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo)), ("ots-alarm-info", ("ots_alarm_info", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo)), ("transceiver-info", ("transceiver_info", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.TransceiverInfo)), ("ext-param-val", ("ext_param_val", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtParamVal)), ("ext-param-threshold-val", ("ext_param_threshold_val", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtParamThresholdVal)), ("extended-alarm-alarm-info", ("extended_alarm_alarm_info", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo)), ("ains-info", ("ains_info", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.AinsInfo)), ("lane-data", ("lane_data", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData))])
                    self._leafs = OrderedDict([
                        ('transport_admin_state', (YLeaf(YType.enumeration, 'transport-admin-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsTas', '')])),
                        ('optics_present', (YLeaf(YType.boolean, 'optics-present'), ['bool'])),
                        ('optics_type', (YLeaf(YType.enumeration, 'optics-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'Optics', '')])),
                        ('derived_optics_type', (YLeaf(YType.str, 'derived-optics-type'), ['str'])),
                        ('optics_module', (YLeaf(YType.str, 'optics-module'), ['str'])),
                        ('dwdm_carrier_band', (YLeaf(YType.enumeration, 'dwdm-carrier-band'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsWaveBand', '')])),
                        ('dwdm_carrier_channel', (YLeaf(YType.str, 'dwdm-carrier-channel'), ['str'])),
                        ('dwdm_carrier_frequency', (YLeaf(YType.str, 'dwdm-carrier-frequency'), ['str'])),
                        ('dwdm_carrier_wavelength', (YLeaf(YType.str, 'dwdm-carrier-wavelength'), ['str'])),
                        ('grey_wavelength', (YLeaf(YType.uint32, 'grey-wavelength'), ['int'])),
                        ('rx_low_threshold', (YLeaf(YType.int32, 'rx-low-threshold'), ['int'])),
                        ('rx_high_threshold', (YLeaf(YType.int32, 'rx-high-threshold'), ['int'])),
                        ('lbc_high_threshold', (YLeaf(YType.int32, 'lbc-high-threshold'), ['int'])),
                        ('tx_low_threshold', (YLeaf(YType.int32, 'tx-low-threshold'), ['int'])),
                        ('tx_high_threshold', (YLeaf(YType.int32, 'tx-high-threshold'), ['int'])),
                        ('lbc_th_high_default', (YLeaf(YType.int32, 'lbc-th-high-default'), ['int'])),
                        ('lbc_th_low_default', (YLeaf(YType.int32, 'lbc-th-low-default'), ['int'])),
                        ('temp_low_threshold', (YLeaf(YType.int32, 'temp-low-threshold'), ['int'])),
                        ('temp_high_threshold', (YLeaf(YType.int32, 'temp-high-threshold'), ['int'])),
                        ('volt_low_threshold', (YLeaf(YType.int32, 'volt-low-threshold'), ['int'])),
                        ('volt_high_threshold', (YLeaf(YType.int32, 'volt-high-threshold'), ['int'])),
                        ('cd', (YLeaf(YType.int32, 'cd'), ['int'])),
                        ('cd_min', (YLeaf(YType.int32, 'cd-min'), ['int'])),
                        ('cd_max', (YLeaf(YType.int32, 'cd-max'), ['int'])),
                        ('cd_low_threshold', (YLeaf(YType.int32, 'cd-low-threshold'), ['int'])),
                        ('cd_high_threshold', (YLeaf(YType.int32, 'cd-high-threshold'), ['int'])),
                        ('osnr_low_threshold', (YLeaf(YType.str, 'osnr-low-threshold'), ['str'])),
                        ('dgd_high_threshold', (YLeaf(YType.str, 'dgd-high-threshold'), ['str'])),
                        ('polarization_mode_dispersion', (YLeaf(YType.str, 'polarization-mode-dispersion'), ['str'])),
                        ('second_order_polarization_mode_dispersion', (YLeaf(YType.str, 'second-order-polarization-mode-dispersion'), ['str'])),
                        ('optical_signal_to_noise_ratio', (YLeaf(YType.str, 'optical-signal-to-noise-ratio'), ['str'])),
                        ('polarization_dependent_loss', (YLeaf(YType.str, 'polarization-dependent-loss'), ['str'])),
                        ('polarization_change_rate', (YLeaf(YType.str, 'polarization-change-rate'), ['str'])),
                        ('differential_group_delay', (YLeaf(YType.str, 'differential-group-delay'), ['str'])),
                        ('phase_noise', (YLeaf(YType.str, 'phase-noise'), ['str'])),
                        ('pm_enable', (YLeaf(YType.uint32, 'pm-enable'), ['int'])),
                        ('laser_state', (YLeaf(YType.enumeration, 'laser-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsLaserState', '')])),
                        ('modulation_type', (YLeaf(YType.enumeration, 'modulation-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsModulation', '')])),
                        ('led_state', (YLeaf(YType.enumeration, 'led-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsLedState', '')])),
                        ('controller_state', (YLeaf(YType.enumeration, 'controller-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsControllerState', '')])),
                        ('form_factor', (YLeaf(YType.enumeration, 'form-factor'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsFormFactor', '')])),
                        ('phy_type', (YLeaf(YType.enumeration, 'phy-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsPhy', '')])),
                        ('cfg_tx_power', (YLeaf(YType.int32, 'cfg-tx-power'), ['int'])),
                        ('cfg_tx_power_configurable', (YLeaf(YType.boolean, 'cfg-tx-power-configurable'), ['bool'])),
                        ('temperature', (YLeaf(YType.int32, 'temperature'), ['int'])),
                        ('voltage', (YLeaf(YType.int32, 'voltage'), ['int'])),
                        ('display_volt_temp', (YLeaf(YType.boolean, 'display-volt-temp'), ['bool'])),
                        ('cd_configurable', (YLeaf(YType.boolean, 'cd-configurable'), ['bool'])),
                        ('optics_fec', (YLeaf(YType.enumeration, 'optics-fec'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsFec', '')])),
                        ('skip_snmp_pm_table', (YLeaf(YType.int32, 'skip-snmp-pm-table'), ['int'])),
                        ('port_type', (YLeaf(YType.enumeration, 'port-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsPort', '')])),
                        ('port_status', (YLeaf(YType.enumeration, 'port-status'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsPortStatus', '')])),
                        ('rx_voa_attenuation', (YLeaf(YType.int32, 'rx-voa-attenuation'), ['int'])),
                        ('tx_voa_attenuation', (YLeaf(YType.int32, 'tx-voa-attenuation'), ['int'])),
                        ('ampli_gain', (YLeaf(YType.int32, 'ampli-gain'), ['int'])),
                        ('ampli_tilt', (YLeaf(YType.int32, 'ampli-tilt'), ['int'])),
                        ('rx_power_th_configurable', (YLeaf(YType.boolean, 'rx-power-th-configurable'), ['bool'])),
                        ('tx_power_th_configurable', (YLeaf(YType.boolean, 'tx-power-th-configurable'), ['bool'])),
                        ('rx_voa_attenuation_config_val', (YLeaf(YType.int32, 'rx-voa-attenuation-config-val'), ['int'])),
                        ('tx_voa_attenuation_config_val', (YLeaf(YType.int32, 'tx-voa-attenuation-config-val'), ['int'])),
                        ('ampli_control_mode_config_val', (YLeaf(YType.enumeration, 'ampli-control-mode-config-val'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsAmplifierControlMode', '')])),
                        ('ampli_gain_range_config_val', (YLeaf(YType.enumeration, 'ampli-gain-range-config-val'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsAmplifierGainRange', '')])),
                        ('ampli_gain_config_val', (YLeaf(YType.int32, 'ampli-gain-config-val'), ['int'])),
                        ('ampli_tilt_config_val', (YLeaf(YType.int32, 'ampli-tilt-config-val'), ['int'])),
                        ('ampli_channel_power_config_val', (YLeaf(YType.int32, 'ampli-channel-power-config-val'), ['int'])),
                        ('channel_power_max_delta_config_val', (YLeaf(YType.int32, 'channel-power-max-delta-config-val'), ['int'])),
                        ('ampli_gain_thr_deg_low_config_val', (YLeaf(YType.int32, 'ampli-gain-thr-deg-low-config-val'), ['int'])),
                        ('ampli_gain_thr_deg_high_config_val', (YLeaf(YType.int32, 'ampli-gain-thr-deg-high-config-val'), ['int'])),
                        ('osri_config_val', (YLeaf(YType.boolean, 'osri-config-val'), ['bool'])),
                        ('tx_config_val', (YLeaf(YType.boolean, 'tx-config-val'), ['bool'])),
                        ('rx_config_val', (YLeaf(YType.boolean, 'rx-config-val'), ['bool'])),
                        ('safety_control_mode_config_val', (YLeaf(YType.enumeration, 'safety-control-mode-config-val'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsAmplifierSafetyControlMode', '')])),
                        ('total_rx_power', (YLeaf(YType.int32, 'total-rx-power'), ['int'])),
                        ('total_tx_power', (YLeaf(YType.int32, 'total-tx-power'), ['int'])),
                        ('is_bo_configured', (YLeaf(YType.boolean, 'is-bo-configured'), ['bool'])),
                        ('is_ext_param_valid', (YLeaf(YType.boolean, 'is-ext-param-valid'), ['bool'])),
                        ('alarm_detected', (YLeaf(YType.boolean, 'alarm-detected'), ['bool'])),
                        ('rx_low_warning_threshold', (YLeaf(YType.int32, 'rx-low-warning-threshold'), ['int'])),
                        ('rx_high_warning_threshold', (YLeaf(YType.int32, 'rx-high-warning-threshold'), ['int'])),
                        ('tx_low_warning_threshold', (YLeaf(YType.int32, 'tx-low-warning-threshold'), ['int'])),
                        ('tx_high_warning_threshold', (YLeaf(YType.int32, 'tx-high-warning-threshold'), ['int'])),
                        ('lbc_th_high_warning_default', (YLeaf(YType.int32, 'lbc-th-high-warning-default'), ['int'])),
                        ('lbc_th_low_warning_default', (YLeaf(YType.int32, 'lbc-th-low-warning-default'), ['int'])),
                        ('temp_low_warning_threshold', (YLeaf(YType.int32, 'temp-low-warning-threshold'), ['int'])),
                        ('temp_high_warning_threshold', (YLeaf(YType.int32, 'temp-high-warning-threshold'), ['int'])),
                        ('volt_low_warning_threshold', (YLeaf(YType.int32, 'volt-low-warning-threshold'), ['int'])),
                        ('volt_high_warning_threshold', (YLeaf(YType.int32, 'volt-high-warning-threshold'), ['int'])),
                        ('description', (YLeaf(YType.str, 'description'), ['str'])),
                        ('ampli_gain_range', (YLeaf(YType.enumeration, 'ampli-gain-range'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsAmplifierGainRange', '')])),
                        ('safety_control_mode', (YLeaf(YType.enumeration, 'safety-control-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsAmplifierSafetyControlMode', '')])),
                        ('osri', (YLeaf(YType.boolean, 'osri'), ['bool'])),
                        ('tx_enable', (YLeaf(YType.boolean, 'tx-enable'), ['bool'])),
                        ('rx_enable', (YLeaf(YType.boolean, 'rx-enable'), ['bool'])),
                        ('is_optics_type_string_valid', (YLeaf(YType.boolean, 'is-optics-type-string-valid'), ['bool'])),
                        ('optics_type_str', (YLeaf(YType.str, 'optics-type-str'), ['str'])),
                        ('rx_low_threshold_current', (YLeaf(YType.int32, 'rx-low-threshold-current'), ['int'])),
                        ('rx_span_loss', (YLeaf(YType.int32, 'rx-span-loss'), ['int'])),
                        ('tx_span_loss', (YLeaf(YType.int32, 'tx-span-loss'), ['int'])),
                        ('baud_rate', (YLeaf(YType.str, 'baud-rate'), ['str'])),
                        ('bits_per_symbol', (YLeaf(YType.str, 'bits-per-symbol'), ['str'])),
                    ])
                    self.transport_admin_state = None
                    self.optics_present = None
                    self.optics_type = None
                    self.derived_optics_type = None
                    self.optics_module = None
                    self.dwdm_carrier_band = None
                    self.dwdm_carrier_channel = None
                    self.dwdm_carrier_frequency = None
                    self.dwdm_carrier_wavelength = None
                    self.grey_wavelength = None
                    self.rx_low_threshold = None
                    self.rx_high_threshold = None
                    self.lbc_high_threshold = None
                    self.tx_low_threshold = None
                    self.tx_high_threshold = None
                    self.lbc_th_high_default = None
                    self.lbc_th_low_default = None
                    self.temp_low_threshold = None
                    self.temp_high_threshold = None
                    self.volt_low_threshold = None
                    self.volt_high_threshold = None
                    self.cd = None
                    self.cd_min = None
                    self.cd_max = None
                    self.cd_low_threshold = None
                    self.cd_high_threshold = None
                    self.osnr_low_threshold = None
                    self.dgd_high_threshold = None
                    self.polarization_mode_dispersion = None
                    self.second_order_polarization_mode_dispersion = None
                    self.optical_signal_to_noise_ratio = None
                    self.polarization_dependent_loss = None
                    self.polarization_change_rate = None
                    self.differential_group_delay = None
                    self.phase_noise = None
                    self.pm_enable = None
                    self.laser_state = None
                    self.modulation_type = None
                    self.led_state = None
                    self.controller_state = None
                    self.form_factor = None
                    self.phy_type = None
                    self.cfg_tx_power = None
                    self.cfg_tx_power_configurable = None
                    self.temperature = None
                    self.voltage = None
                    self.display_volt_temp = None
                    self.cd_configurable = None
                    self.optics_fec = None
                    self.skip_snmp_pm_table = None
                    self.port_type = None
                    self.port_status = None
                    self.rx_voa_attenuation = None
                    self.tx_voa_attenuation = None
                    self.ampli_gain = None
                    self.ampli_tilt = None
                    self.rx_power_th_configurable = None
                    self.tx_power_th_configurable = None
                    self.rx_voa_attenuation_config_val = None
                    self.tx_voa_attenuation_config_val = None
                    self.ampli_control_mode_config_val = None
                    self.ampli_gain_range_config_val = None
                    self.ampli_gain_config_val = None
                    self.ampli_tilt_config_val = None
                    self.ampli_channel_power_config_val = None
                    self.channel_power_max_delta_config_val = None
                    self.ampli_gain_thr_deg_low_config_val = None
                    self.ampli_gain_thr_deg_high_config_val = None
                    self.osri_config_val = None
                    self.tx_config_val = None
                    self.rx_config_val = None
                    self.safety_control_mode_config_val = None
                    self.total_rx_power = None
                    self.total_tx_power = None
                    self.is_bo_configured = None
                    self.is_ext_param_valid = None
                    self.alarm_detected = None
                    self.rx_low_warning_threshold = None
                    self.rx_high_warning_threshold = None
                    self.tx_low_warning_threshold = None
                    self.tx_high_warning_threshold = None
                    self.lbc_th_high_warning_default = None
                    self.lbc_th_low_warning_default = None
                    self.temp_low_warning_threshold = None
                    self.temp_high_warning_threshold = None
                    self.volt_low_warning_threshold = None
                    self.volt_high_warning_threshold = None
                    self.description = None
                    self.ampli_gain_range = None
                    self.safety_control_mode = None
                    self.osri = None
                    self.tx_enable = None
                    self.rx_enable = None
                    self.is_optics_type_string_valid = None
                    self.optics_type_str = None
                    self.rx_low_threshold_current = None
                    self.rx_span_loss = None
                    self.tx_span_loss = None
                    self.baud_rate = None
                    self.bits_per_symbol = None

                    self.network_srlg_info = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.NetworkSrlgInfo()
                    self.network_srlg_info.parent = self
                    self._children_name_map["network_srlg_info"] = "network-srlg-info"

                    self.optics_alarm_info = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo()
                    self.optics_alarm_info.parent = self
                    self._children_name_map["optics_alarm_info"] = "optics-alarm-info"

                    self.ots_alarm_info = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo()
                    self.ots_alarm_info.parent = self
                    self._children_name_map["ots_alarm_info"] = "ots-alarm-info"

                    self.transceiver_info = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.TransceiverInfo()
                    self.transceiver_info.parent = self
                    self._children_name_map["transceiver_info"] = "transceiver-info"

                    self.ext_param_val = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtParamVal()
                    self.ext_param_val.parent = self
                    self._children_name_map["ext_param_val"] = "ext-param-val"

                    self.ext_param_threshold_val = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtParamThresholdVal()
                    self.ext_param_threshold_val.parent = self
                    self._children_name_map["ext_param_threshold_val"] = "ext-param-threshold-val"

                    self.extended_alarm_alarm_info = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo()
                    self.extended_alarm_alarm_info.parent = self
                    self._children_name_map["extended_alarm_alarm_info"] = "extended-alarm-alarm-info"

                    self.ains_info = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.AinsInfo()
                    self.ains_info.parent = self
                    self._children_name_map["ains_info"] = "ains-info"

                    self.lane_data = YList(self)
                    self._segment_path = lambda: "optics-info"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo, ['transport_admin_state', 'optics_present', 'optics_type', 'derived_optics_type', 'optics_module', 'dwdm_carrier_band', 'dwdm_carrier_channel', 'dwdm_carrier_frequency', 'dwdm_carrier_wavelength', 'grey_wavelength', 'rx_low_threshold', 'rx_high_threshold', 'lbc_high_threshold', 'tx_low_threshold', 'tx_high_threshold', 'lbc_th_high_default', 'lbc_th_low_default', 'temp_low_threshold', 'temp_high_threshold', 'volt_low_threshold', 'volt_high_threshold', 'cd', 'cd_min', 'cd_max', 'cd_low_threshold', 'cd_high_threshold', 'osnr_low_threshold', 'dgd_high_threshold', 'polarization_mode_dispersion', 'second_order_polarization_mode_dispersion', 'optical_signal_to_noise_ratio', 'polarization_dependent_loss', 'polarization_change_rate', 'differential_group_delay', 'phase_noise', 'pm_enable', 'laser_state', 'modulation_type', 'led_state', 'controller_state', 'form_factor', 'phy_type', 'cfg_tx_power', 'cfg_tx_power_configurable', 'temperature', 'voltage', 'display_volt_temp', 'cd_configurable', 'optics_fec', 'skip_snmp_pm_table', 'port_type', 'port_status', 'rx_voa_attenuation', 'tx_voa_attenuation', 'ampli_gain', 'ampli_tilt', 'rx_power_th_configurable', 'tx_power_th_configurable', 'rx_voa_attenuation_config_val', 'tx_voa_attenuation_config_val', 'ampli_control_mode_config_val', 'ampli_gain_range_config_val', 'ampli_gain_config_val', 'ampli_tilt_config_val', 'ampli_channel_power_config_val', 'channel_power_max_delta_config_val', 'ampli_gain_thr_deg_low_config_val', 'ampli_gain_thr_deg_high_config_val', 'osri_config_val', 'tx_config_val', 'rx_config_val', 'safety_control_mode_config_val', 'total_rx_power', 'total_tx_power', 'is_bo_configured', 'is_ext_param_valid', 'alarm_detected', 'rx_low_warning_threshold', 'rx_high_warning_threshold', 'tx_low_warning_threshold', 'tx_high_warning_threshold', 'lbc_th_high_warning_default', 'lbc_th_low_warning_default', 'temp_low_warning_threshold', 'temp_high_warning_threshold', 'volt_low_warning_threshold', 'volt_high_warning_threshold', 'description', 'ampli_gain_range', 'safety_control_mode', 'osri', 'tx_enable', 'rx_enable', 'is_optics_type_string_valid', 'optics_type_str', 'rx_low_threshold_current', 'rx_span_loss', 'tx_span_loss', 'baud_rate', 'bits_per_symbol'], name, value)


                class NetworkSrlgInfo(Entity):
                    """
                    Network SRLG information
                    
                    .. attribute:: network_srlg_array
                    
                    	Network Srlg Array
                    	**type**\: list of  		 :py:class:`NetworkSrlgArray <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.NetworkSrlgInfo.NetworkSrlgArray>`
                    
                    

                    """

                    _prefix = 'controller-optics-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.NetworkSrlgInfo, self).__init__()

                        self.yang_name = "network-srlg-info"
                        self.yang_parent_name = "optics-info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("network-srlg-array", ("network_srlg_array", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.NetworkSrlgInfo.NetworkSrlgArray))])
                        self._leafs = OrderedDict()

                        self.network_srlg_array = YList(self)
                        self._segment_path = lambda: "network-srlg-info"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.NetworkSrlgInfo, [], name, value)


                    class NetworkSrlgArray(Entity):
                        """
                        Network Srlg Array
                        
                        .. attribute:: set_number
                        
                        	Array to maintain set number
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: network_srlg
                        
                        	Network Srlg
                        	**type**\: list of int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.NetworkSrlgInfo.NetworkSrlgArray, self).__init__()

                            self.yang_name = "network-srlg-array"
                            self.yang_parent_name = "network-srlg-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('set_number', (YLeaf(YType.uint32, 'set-number'), ['int'])),
                                ('network_srlg', (YLeafList(YType.uint32, 'network-srlg'), ['int'])),
                            ])
                            self.set_number = None
                            self.network_srlg = []
                            self._segment_path = lambda: "network-srlg-array"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.NetworkSrlgInfo.NetworkSrlgArray, ['set_number', 'network_srlg'], name, value)


                class OpticsAlarmInfo(Entity):
                    """
                    Optics Alarm Information
                    
                    .. attribute:: high_rx_power
                    
                    	High Rx Power in units of 0.1 dBm
                    	**type**\:  :py:class:`HighRxPower <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRxPower>`
                    
                    .. attribute:: low_rx_power
                    
                    	Low Rx Power in units of 0.1 dBm
                    	**type**\:  :py:class:`LowRxPower <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRxPower>`
                    
                    .. attribute:: high_tx_power
                    
                    	High Tx Power in units of 0.1 dBm
                    	**type**\:  :py:class:`HighTxPower <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTxPower>`
                    
                    .. attribute:: low_tx_power
                    
                    	Low Tx Power in units of 0.1 dBm
                    	**type**\:  :py:class:`LowTxPower <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTxPower>`
                    
                    .. attribute:: high_lbc
                    
                    	High laser bias current in units of percentage
                    	**type**\:  :py:class:`HighLbc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighLbc>`
                    
                    .. attribute:: low_temperature
                    
                    	Low Temperature alarm
                    	**type**\:  :py:class:`LowTemperature <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTemperature>`
                    
                    .. attribute:: high_temperature
                    
                    	High Temperature alarm
                    	**type**\:  :py:class:`HighTemperature <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTemperature>`
                    
                    .. attribute:: low_voltage
                    
                    	Low Voltage alarm
                    	**type**\:  :py:class:`LowVoltage <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowVoltage>`
                    
                    .. attribute:: high_voltage
                    
                    	High Voltage alarm
                    	**type**\:  :py:class:`HighVoltage <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighVoltage>`
                    
                    .. attribute:: high_rx1_power
                    
                    	High Rx1 Power in units of 0.1 dBm
                    	**type**\:  :py:class:`HighRx1Power <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx1Power>`
                    
                    .. attribute:: high_rx2_power
                    
                    	High Rx2 Power in units of 0.1 dBm
                    	**type**\:  :py:class:`HighRx2Power <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx2Power>`
                    
                    .. attribute:: high_rx3_power
                    
                    	High Rx3 Power in units of 0.1 dBm
                    	**type**\:  :py:class:`HighRx3Power <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx3Power>`
                    
                    .. attribute:: high_rx4_power
                    
                    	High Rx4 Power in units of 0.1 dBm
                    	**type**\:  :py:class:`HighRx4Power <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx4Power>`
                    
                    .. attribute:: low_rx1_power
                    
                    	Low Rx1 Power in units of 0.1 dBm
                    	**type**\:  :py:class:`LowRx1Power <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx1Power>`
                    
                    .. attribute:: low_rx2_power
                    
                    	Low Rx2 Power in units of 0.1 dBm
                    	**type**\:  :py:class:`LowRx2Power <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx2Power>`
                    
                    .. attribute:: low_rx3_power
                    
                    	Low Rx3 Power in units of 0.1 dBm
                    	**type**\:  :py:class:`LowRx3Power <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx3Power>`
                    
                    .. attribute:: low_rx4_power
                    
                    	Low Rx4 Power in units of 0.1 dBm
                    	**type**\:  :py:class:`LowRx4Power <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx4Power>`
                    
                    .. attribute:: high_tx1_power
                    
                    	High Tx1 Power in units of 0.1 dBm
                    	**type**\:  :py:class:`HighTx1Power <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx1Power>`
                    
                    .. attribute:: high_tx2_power
                    
                    	High Tx2 Power in units of 0.1 dBm
                    	**type**\:  :py:class:`HighTx2Power <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx2Power>`
                    
                    .. attribute:: high_tx3_power
                    
                    	High Tx3 Power in units of 0.1 dBm
                    	**type**\:  :py:class:`HighTx3Power <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx3Power>`
                    
                    .. attribute:: high_tx4_power
                    
                    	High Tx4 Power in units of 0.1 dBm
                    	**type**\:  :py:class:`HighTx4Power <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx4Power>`
                    
                    .. attribute:: low_tx1_power
                    
                    	Low Tx1 Power in units of 0.1 dBm
                    	**type**\:  :py:class:`LowTx1Power <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx1Power>`
                    
                    .. attribute:: low_tx2_power
                    
                    	Low Tx2 Power in units of 0.1 dBm
                    	**type**\:  :py:class:`LowTx2Power <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx2Power>`
                    
                    .. attribute:: low_tx3_power
                    
                    	Low Tx3 Power in units of 0.1 dBm
                    	**type**\:  :py:class:`LowTx3Power <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx3Power>`
                    
                    .. attribute:: low_tx4_power
                    
                    	Low Tx4 Power in units of 0.1 dBm
                    	**type**\:  :py:class:`LowTx4Power <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx4Power>`
                    
                    .. attribute:: high_tx1lbc
                    
                    	High Tx1 laser bias current in units of percentage
                    	**type**\:  :py:class:`HighTx1lbc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx1lbc>`
                    
                    .. attribute:: high_tx2lbc
                    
                    	High Tx2 laser bias current in units of percentage
                    	**type**\:  :py:class:`HighTx2lbc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx2lbc>`
                    
                    .. attribute:: high_tx3lbc
                    
                    	High Tx3 laser bias current in units of percentage
                    	**type**\:  :py:class:`HighTx3lbc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx3lbc>`
                    
                    .. attribute:: high_tx4lbc
                    
                    	High Tx4 laser bias current in units of percentage
                    	**type**\:  :py:class:`HighTx4lbc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx4lbc>`
                    
                    .. attribute:: low_tx1lbc
                    
                    	Low Tx1 laser bias current in units of percentage
                    	**type**\:  :py:class:`LowTx1lbc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx1lbc>`
                    
                    .. attribute:: low_tx2lbc
                    
                    	Low Tx2 laser bias current in units of percentage
                    	**type**\:  :py:class:`LowTx2lbc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx2lbc>`
                    
                    .. attribute:: low_tx3lbc
                    
                    	Low Tx3 laser bias current in units of percentage
                    	**type**\:  :py:class:`LowTx3lbc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx3lbc>`
                    
                    .. attribute:: low_tx4lbc
                    
                    	Low Tx4 laser bias current in units of percentage
                    	**type**\:  :py:class:`LowTx4lbc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx4lbc>`
                    
                    .. attribute:: rx_los
                    
                    	RX LOS
                    	**type**\:  :py:class:`RxLos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.RxLos>`
                    
                    .. attribute:: tx_los
                    
                    	TX LOS
                    	**type**\:  :py:class:`TxLos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxLos>`
                    
                    .. attribute:: rx_lol
                    
                    	RX LOL
                    	**type**\:  :py:class:`RxLol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.RxLol>`
                    
                    .. attribute:: tx_lol
                    
                    	TX LOL
                    	**type**\:  :py:class:`TxLol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxLol>`
                    
                    .. attribute:: tx_fault
                    
                    	TX Fault
                    	**type**\:  :py:class:`TxFault <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxFault>`
                    
                    .. attribute:: hidgd
                    
                    	HI DGD
                    	**type**\:  :py:class:`Hidgd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Hidgd>`
                    
                    .. attribute:: oorcd
                    
                    	OOR CD
                    	**type**\:  :py:class:`Oorcd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Oorcd>`
                    
                    .. attribute:: osnr
                    
                    	OSNR
                    	**type**\:  :py:class:`Osnr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Osnr>`
                    
                    .. attribute:: wvlool
                    
                    	WVL OOL
                    	**type**\:  :py:class:`Wvlool <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Wvlool>`
                    
                    .. attribute:: mea
                    
                    	MEA
                    	**type**\:  :py:class:`Mea <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Mea>`
                    
                    .. attribute:: imp_removal
                    
                    	IMPROPER REM
                    	**type**\:  :py:class:`ImpRemoval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.ImpRemoval>`
                    
                    .. attribute:: rx_loc
                    
                    	Rx LOC
                    	**type**\:  :py:class:`RxLoc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.RxLoc>`
                    
                    .. attribute:: amp_gain_deg_low
                    
                    	Ampli Gain Deg Low
                    	**type**\:  :py:class:`AmpGainDegLow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.AmpGainDegLow>`
                    
                    .. attribute:: amp_gain_deg_high
                    
                    	Ampli Gain Deg High
                    	**type**\:  :py:class:`AmpGainDegHigh <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.AmpGainDegHigh>`
                    
                    .. attribute:: txpwr_mismatch
                    
                    	TX POWER PROV MISMATCH
                    	**type**\:  :py:class:`TxpwrMismatch <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxpwrMismatch>`
                    
                    

                    """

                    _prefix = 'controller-optics-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo, self).__init__()

                        self.yang_name = "optics-alarm-info"
                        self.yang_parent_name = "optics-info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("high-rx-power", ("high_rx_power", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRxPower)), ("low-rx-power", ("low_rx_power", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRxPower)), ("high-tx-power", ("high_tx_power", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTxPower)), ("low-tx-power", ("low_tx_power", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTxPower)), ("high-lbc", ("high_lbc", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighLbc)), ("low-temperature", ("low_temperature", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTemperature)), ("high-temperature", ("high_temperature", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTemperature)), ("low-voltage", ("low_voltage", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowVoltage)), ("high-voltage", ("high_voltage", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighVoltage)), ("high-rx1-power", ("high_rx1_power", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx1Power)), ("high-rx2-power", ("high_rx2_power", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx2Power)), ("high-rx3-power", ("high_rx3_power", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx3Power)), ("high-rx4-power", ("high_rx4_power", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx4Power)), ("low-rx1-power", ("low_rx1_power", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx1Power)), ("low-rx2-power", ("low_rx2_power", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx2Power)), ("low-rx3-power", ("low_rx3_power", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx3Power)), ("low-rx4-power", ("low_rx4_power", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx4Power)), ("high-tx1-power", ("high_tx1_power", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx1Power)), ("high-tx2-power", ("high_tx2_power", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx2Power)), ("high-tx3-power", ("high_tx3_power", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx3Power)), ("high-tx4-power", ("high_tx4_power", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx4Power)), ("low-tx1-power", ("low_tx1_power", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx1Power)), ("low-tx2-power", ("low_tx2_power", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx2Power)), ("low-tx3-power", ("low_tx3_power", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx3Power)), ("low-tx4-power", ("low_tx4_power", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx4Power)), ("high-tx1lbc", ("high_tx1lbc", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx1lbc)), ("high-tx2lbc", ("high_tx2lbc", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx2lbc)), ("high-tx3lbc", ("high_tx3lbc", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx3lbc)), ("high-tx4lbc", ("high_tx4lbc", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx4lbc)), ("low-tx1lbc", ("low_tx1lbc", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx1lbc)), ("low-tx2lbc", ("low_tx2lbc", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx2lbc)), ("low-tx3lbc", ("low_tx3lbc", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx3lbc)), ("low-tx4lbc", ("low_tx4lbc", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx4lbc)), ("rx-los", ("rx_los", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.RxLos)), ("tx-los", ("tx_los", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxLos)), ("rx-lol", ("rx_lol", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.RxLol)), ("tx-lol", ("tx_lol", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxLol)), ("tx-fault", ("tx_fault", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxFault)), ("hidgd", ("hidgd", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Hidgd)), ("oorcd", ("oorcd", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Oorcd)), ("osnr", ("osnr", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Osnr)), ("wvlool", ("wvlool", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Wvlool)), ("mea", ("mea", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Mea)), ("imp-removal", ("imp_removal", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.ImpRemoval)), ("rx-loc", ("rx_loc", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.RxLoc)), ("amp-gain-deg-low", ("amp_gain_deg_low", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.AmpGainDegLow)), ("amp-gain-deg-high", ("amp_gain_deg_high", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.AmpGainDegHigh)), ("txpwr-mismatch", ("txpwr_mismatch", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxpwrMismatch))])
                        self._leafs = OrderedDict()

                        self.high_rx_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRxPower()
                        self.high_rx_power.parent = self
                        self._children_name_map["high_rx_power"] = "high-rx-power"

                        self.low_rx_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRxPower()
                        self.low_rx_power.parent = self
                        self._children_name_map["low_rx_power"] = "low-rx-power"

                        self.high_tx_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTxPower()
                        self.high_tx_power.parent = self
                        self._children_name_map["high_tx_power"] = "high-tx-power"

                        self.low_tx_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTxPower()
                        self.low_tx_power.parent = self
                        self._children_name_map["low_tx_power"] = "low-tx-power"

                        self.high_lbc = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighLbc()
                        self.high_lbc.parent = self
                        self._children_name_map["high_lbc"] = "high-lbc"

                        self.low_temperature = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTemperature()
                        self.low_temperature.parent = self
                        self._children_name_map["low_temperature"] = "low-temperature"

                        self.high_temperature = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTemperature()
                        self.high_temperature.parent = self
                        self._children_name_map["high_temperature"] = "high-temperature"

                        self.low_voltage = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowVoltage()
                        self.low_voltage.parent = self
                        self._children_name_map["low_voltage"] = "low-voltage"

                        self.high_voltage = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighVoltage()
                        self.high_voltage.parent = self
                        self._children_name_map["high_voltage"] = "high-voltage"

                        self.high_rx1_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx1Power()
                        self.high_rx1_power.parent = self
                        self._children_name_map["high_rx1_power"] = "high-rx1-power"

                        self.high_rx2_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx2Power()
                        self.high_rx2_power.parent = self
                        self._children_name_map["high_rx2_power"] = "high-rx2-power"

                        self.high_rx3_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx3Power()
                        self.high_rx3_power.parent = self
                        self._children_name_map["high_rx3_power"] = "high-rx3-power"

                        self.high_rx4_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx4Power()
                        self.high_rx4_power.parent = self
                        self._children_name_map["high_rx4_power"] = "high-rx4-power"

                        self.low_rx1_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx1Power()
                        self.low_rx1_power.parent = self
                        self._children_name_map["low_rx1_power"] = "low-rx1-power"

                        self.low_rx2_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx2Power()
                        self.low_rx2_power.parent = self
                        self._children_name_map["low_rx2_power"] = "low-rx2-power"

                        self.low_rx3_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx3Power()
                        self.low_rx3_power.parent = self
                        self._children_name_map["low_rx3_power"] = "low-rx3-power"

                        self.low_rx4_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx4Power()
                        self.low_rx4_power.parent = self
                        self._children_name_map["low_rx4_power"] = "low-rx4-power"

                        self.high_tx1_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx1Power()
                        self.high_tx1_power.parent = self
                        self._children_name_map["high_tx1_power"] = "high-tx1-power"

                        self.high_tx2_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx2Power()
                        self.high_tx2_power.parent = self
                        self._children_name_map["high_tx2_power"] = "high-tx2-power"

                        self.high_tx3_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx3Power()
                        self.high_tx3_power.parent = self
                        self._children_name_map["high_tx3_power"] = "high-tx3-power"

                        self.high_tx4_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx4Power()
                        self.high_tx4_power.parent = self
                        self._children_name_map["high_tx4_power"] = "high-tx4-power"

                        self.low_tx1_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx1Power()
                        self.low_tx1_power.parent = self
                        self._children_name_map["low_tx1_power"] = "low-tx1-power"

                        self.low_tx2_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx2Power()
                        self.low_tx2_power.parent = self
                        self._children_name_map["low_tx2_power"] = "low-tx2-power"

                        self.low_tx3_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx3Power()
                        self.low_tx3_power.parent = self
                        self._children_name_map["low_tx3_power"] = "low-tx3-power"

                        self.low_tx4_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx4Power()
                        self.low_tx4_power.parent = self
                        self._children_name_map["low_tx4_power"] = "low-tx4-power"

                        self.high_tx1lbc = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx1lbc()
                        self.high_tx1lbc.parent = self
                        self._children_name_map["high_tx1lbc"] = "high-tx1lbc"

                        self.high_tx2lbc = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx2lbc()
                        self.high_tx2lbc.parent = self
                        self._children_name_map["high_tx2lbc"] = "high-tx2lbc"

                        self.high_tx3lbc = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx3lbc()
                        self.high_tx3lbc.parent = self
                        self._children_name_map["high_tx3lbc"] = "high-tx3lbc"

                        self.high_tx4lbc = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx4lbc()
                        self.high_tx4lbc.parent = self
                        self._children_name_map["high_tx4lbc"] = "high-tx4lbc"

                        self.low_tx1lbc = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx1lbc()
                        self.low_tx1lbc.parent = self
                        self._children_name_map["low_tx1lbc"] = "low-tx1lbc"

                        self.low_tx2lbc = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx2lbc()
                        self.low_tx2lbc.parent = self
                        self._children_name_map["low_tx2lbc"] = "low-tx2lbc"

                        self.low_tx3lbc = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx3lbc()
                        self.low_tx3lbc.parent = self
                        self._children_name_map["low_tx3lbc"] = "low-tx3lbc"

                        self.low_tx4lbc = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx4lbc()
                        self.low_tx4lbc.parent = self
                        self._children_name_map["low_tx4lbc"] = "low-tx4lbc"

                        self.rx_los = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.RxLos()
                        self.rx_los.parent = self
                        self._children_name_map["rx_los"] = "rx-los"

                        self.tx_los = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxLos()
                        self.tx_los.parent = self
                        self._children_name_map["tx_los"] = "tx-los"

                        self.rx_lol = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.RxLol()
                        self.rx_lol.parent = self
                        self._children_name_map["rx_lol"] = "rx-lol"

                        self.tx_lol = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxLol()
                        self.tx_lol.parent = self
                        self._children_name_map["tx_lol"] = "tx-lol"

                        self.tx_fault = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxFault()
                        self.tx_fault.parent = self
                        self._children_name_map["tx_fault"] = "tx-fault"

                        self.hidgd = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Hidgd()
                        self.hidgd.parent = self
                        self._children_name_map["hidgd"] = "hidgd"

                        self.oorcd = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Oorcd()
                        self.oorcd.parent = self
                        self._children_name_map["oorcd"] = "oorcd"

                        self.osnr = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Osnr()
                        self.osnr.parent = self
                        self._children_name_map["osnr"] = "osnr"

                        self.wvlool = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Wvlool()
                        self.wvlool.parent = self
                        self._children_name_map["wvlool"] = "wvlool"

                        self.mea = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Mea()
                        self.mea.parent = self
                        self._children_name_map["mea"] = "mea"

                        self.imp_removal = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.ImpRemoval()
                        self.imp_removal.parent = self
                        self._children_name_map["imp_removal"] = "imp-removal"

                        self.rx_loc = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.RxLoc()
                        self.rx_loc.parent = self
                        self._children_name_map["rx_loc"] = "rx-loc"

                        self.amp_gain_deg_low = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.AmpGainDegLow()
                        self.amp_gain_deg_low.parent = self
                        self._children_name_map["amp_gain_deg_low"] = "amp-gain-deg-low"

                        self.amp_gain_deg_high = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.AmpGainDegHigh()
                        self.amp_gain_deg_high.parent = self
                        self._children_name_map["amp_gain_deg_high"] = "amp-gain-deg-high"

                        self.txpwr_mismatch = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxpwrMismatch()
                        self.txpwr_mismatch.parent = self
                        self._children_name_map["txpwr_mismatch"] = "txpwr-mismatch"
                        self._segment_path = lambda: "optics-alarm-info"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo, [], name, value)


                    class HighRxPower(Entity):
                        """
                        High Rx Power in units of 0.1 dBm
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRxPower, self).__init__()

                            self.yang_name = "high-rx-power"
                            self.yang_parent_name = "optics-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                            ])
                            self.is_detected = None
                            self.counter = None
                            self._segment_path = lambda: "high-rx-power"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRxPower, ['is_detected', 'counter'], name, value)


                    class LowRxPower(Entity):
                        """
                        Low Rx Power in units of 0.1 dBm
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRxPower, self).__init__()

                            self.yang_name = "low-rx-power"
                            self.yang_parent_name = "optics-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                            ])
                            self.is_detected = None
                            self.counter = None
                            self._segment_path = lambda: "low-rx-power"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRxPower, ['is_detected', 'counter'], name, value)


                    class HighTxPower(Entity):
                        """
                        High Tx Power in units of 0.1 dBm
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTxPower, self).__init__()

                            self.yang_name = "high-tx-power"
                            self.yang_parent_name = "optics-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                            ])
                            self.is_detected = None
                            self.counter = None
                            self._segment_path = lambda: "high-tx-power"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTxPower, ['is_detected', 'counter'], name, value)


                    class LowTxPower(Entity):
                        """
                        Low Tx Power in units of 0.1 dBm
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTxPower, self).__init__()

                            self.yang_name = "low-tx-power"
                            self.yang_parent_name = "optics-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                            ])
                            self.is_detected = None
                            self.counter = None
                            self._segment_path = lambda: "low-tx-power"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTxPower, ['is_detected', 'counter'], name, value)


                    class HighLbc(Entity):
                        """
                        High laser bias current in units of percentage
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighLbc, self).__init__()

                            self.yang_name = "high-lbc"
                            self.yang_parent_name = "optics-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                            ])
                            self.is_detected = None
                            self.counter = None
                            self._segment_path = lambda: "high-lbc"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighLbc, ['is_detected', 'counter'], name, value)


                    class LowTemperature(Entity):
                        """
                        Low Temperature alarm
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTemperature, self).__init__()

                            self.yang_name = "low-temperature"
                            self.yang_parent_name = "optics-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                            ])
                            self.is_detected = None
                            self.counter = None
                            self._segment_path = lambda: "low-temperature"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTemperature, ['is_detected', 'counter'], name, value)


                    class HighTemperature(Entity):
                        """
                        High Temperature alarm
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTemperature, self).__init__()

                            self.yang_name = "high-temperature"
                            self.yang_parent_name = "optics-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                            ])
                            self.is_detected = None
                            self.counter = None
                            self._segment_path = lambda: "high-temperature"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTemperature, ['is_detected', 'counter'], name, value)


                    class LowVoltage(Entity):
                        """
                        Low Voltage alarm
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowVoltage, self).__init__()

                            self.yang_name = "low-voltage"
                            self.yang_parent_name = "optics-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                            ])
                            self.is_detected = None
                            self.counter = None
                            self._segment_path = lambda: "low-voltage"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowVoltage, ['is_detected', 'counter'], name, value)


                    class HighVoltage(Entity):
                        """
                        High Voltage alarm
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighVoltage, self).__init__()

                            self.yang_name = "high-voltage"
                            self.yang_parent_name = "optics-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                            ])
                            self.is_detected = None
                            self.counter = None
                            self._segment_path = lambda: "high-voltage"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighVoltage, ['is_detected', 'counter'], name, value)


                    class HighRx1Power(Entity):
                        """
                        High Rx1 Power in units of 0.1 dBm
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx1Power, self).__init__()

                            self.yang_name = "high-rx1-power"
                            self.yang_parent_name = "optics-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                            ])
                            self.is_detected = None
                            self.counter = None
                            self._segment_path = lambda: "high-rx1-power"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx1Power, ['is_detected', 'counter'], name, value)


                    class HighRx2Power(Entity):
                        """
                        High Rx2 Power in units of 0.1 dBm
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx2Power, self).__init__()

                            self.yang_name = "high-rx2-power"
                            self.yang_parent_name = "optics-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                            ])
                            self.is_detected = None
                            self.counter = None
                            self._segment_path = lambda: "high-rx2-power"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx2Power, ['is_detected', 'counter'], name, value)


                    class HighRx3Power(Entity):
                        """
                        High Rx3 Power in units of 0.1 dBm
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx3Power, self).__init__()

                            self.yang_name = "high-rx3-power"
                            self.yang_parent_name = "optics-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                            ])
                            self.is_detected = None
                            self.counter = None
                            self._segment_path = lambda: "high-rx3-power"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx3Power, ['is_detected', 'counter'], name, value)


                    class HighRx4Power(Entity):
                        """
                        High Rx4 Power in units of 0.1 dBm
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx4Power, self).__init__()

                            self.yang_name = "high-rx4-power"
                            self.yang_parent_name = "optics-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                            ])
                            self.is_detected = None
                            self.counter = None
                            self._segment_path = lambda: "high-rx4-power"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx4Power, ['is_detected', 'counter'], name, value)


                    class LowRx1Power(Entity):
                        """
                        Low Rx1 Power in units of 0.1 dBm
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx1Power, self).__init__()

                            self.yang_name = "low-rx1-power"
                            self.yang_parent_name = "optics-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                            ])
                            self.is_detected = None
                            self.counter = None
                            self._segment_path = lambda: "low-rx1-power"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx1Power, ['is_detected', 'counter'], name, value)


                    class LowRx2Power(Entity):
                        """
                        Low Rx2 Power in units of 0.1 dBm
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx2Power, self).__init__()

                            self.yang_name = "low-rx2-power"
                            self.yang_parent_name = "optics-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                            ])
                            self.is_detected = None
                            self.counter = None
                            self._segment_path = lambda: "low-rx2-power"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx2Power, ['is_detected', 'counter'], name, value)


                    class LowRx3Power(Entity):
                        """
                        Low Rx3 Power in units of 0.1 dBm
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx3Power, self).__init__()

                            self.yang_name = "low-rx3-power"
                            self.yang_parent_name = "optics-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                            ])
                            self.is_detected = None
                            self.counter = None
                            self._segment_path = lambda: "low-rx3-power"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx3Power, ['is_detected', 'counter'], name, value)


                    class LowRx4Power(Entity):
                        """
                        Low Rx4 Power in units of 0.1 dBm
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx4Power, self).__init__()

                            self.yang_name = "low-rx4-power"
                            self.yang_parent_name = "optics-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                            ])
                            self.is_detected = None
                            self.counter = None
                            self._segment_path = lambda: "low-rx4-power"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx4Power, ['is_detected', 'counter'], name, value)


                    class HighTx1Power(Entity):
                        """
                        High Tx1 Power in units of 0.1 dBm
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx1Power, self).__init__()

                            self.yang_name = "high-tx1-power"
                            self.yang_parent_name = "optics-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                            ])
                            self.is_detected = None
                            self.counter = None
                            self._segment_path = lambda: "high-tx1-power"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx1Power, ['is_detected', 'counter'], name, value)


                    class HighTx2Power(Entity):
                        """
                        High Tx2 Power in units of 0.1 dBm
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx2Power, self).__init__()

                            self.yang_name = "high-tx2-power"
                            self.yang_parent_name = "optics-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                            ])
                            self.is_detected = None
                            self.counter = None
                            self._segment_path = lambda: "high-tx2-power"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx2Power, ['is_detected', 'counter'], name, value)


                    class HighTx3Power(Entity):
                        """
                        High Tx3 Power in units of 0.1 dBm
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx3Power, self).__init__()

                            self.yang_name = "high-tx3-power"
                            self.yang_parent_name = "optics-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                            ])
                            self.is_detected = None
                            self.counter = None
                            self._segment_path = lambda: "high-tx3-power"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx3Power, ['is_detected', 'counter'], name, value)


                    class HighTx4Power(Entity):
                        """
                        High Tx4 Power in units of 0.1 dBm
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx4Power, self).__init__()

                            self.yang_name = "high-tx4-power"
                            self.yang_parent_name = "optics-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                            ])
                            self.is_detected = None
                            self.counter = None
                            self._segment_path = lambda: "high-tx4-power"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx4Power, ['is_detected', 'counter'], name, value)


                    class LowTx1Power(Entity):
                        """
                        Low Tx1 Power in units of 0.1 dBm
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx1Power, self).__init__()

                            self.yang_name = "low-tx1-power"
                            self.yang_parent_name = "optics-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                            ])
                            self.is_detected = None
                            self.counter = None
                            self._segment_path = lambda: "low-tx1-power"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx1Power, ['is_detected', 'counter'], name, value)


                    class LowTx2Power(Entity):
                        """
                        Low Tx2 Power in units of 0.1 dBm
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx2Power, self).__init__()

                            self.yang_name = "low-tx2-power"
                            self.yang_parent_name = "optics-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                            ])
                            self.is_detected = None
                            self.counter = None
                            self._segment_path = lambda: "low-tx2-power"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx2Power, ['is_detected', 'counter'], name, value)


                    class LowTx3Power(Entity):
                        """
                        Low Tx3 Power in units of 0.1 dBm
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx3Power, self).__init__()

                            self.yang_name = "low-tx3-power"
                            self.yang_parent_name = "optics-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                            ])
                            self.is_detected = None
                            self.counter = None
                            self._segment_path = lambda: "low-tx3-power"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx3Power, ['is_detected', 'counter'], name, value)


                    class LowTx4Power(Entity):
                        """
                        Low Tx4 Power in units of 0.1 dBm
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx4Power, self).__init__()

                            self.yang_name = "low-tx4-power"
                            self.yang_parent_name = "optics-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                            ])
                            self.is_detected = None
                            self.counter = None
                            self._segment_path = lambda: "low-tx4-power"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx4Power, ['is_detected', 'counter'], name, value)


                    class HighTx1lbc(Entity):
                        """
                        High Tx1 laser bias current in units of
                        percentage
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx1lbc, self).__init__()

                            self.yang_name = "high-tx1lbc"
                            self.yang_parent_name = "optics-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                            ])
                            self.is_detected = None
                            self.counter = None
                            self._segment_path = lambda: "high-tx1lbc"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx1lbc, ['is_detected', 'counter'], name, value)


                    class HighTx2lbc(Entity):
                        """
                        High Tx2 laser bias current in units of
                        percentage
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx2lbc, self).__init__()

                            self.yang_name = "high-tx2lbc"
                            self.yang_parent_name = "optics-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                            ])
                            self.is_detected = None
                            self.counter = None
                            self._segment_path = lambda: "high-tx2lbc"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx2lbc, ['is_detected', 'counter'], name, value)


                    class HighTx3lbc(Entity):
                        """
                        High Tx3 laser bias current in units of
                        percentage
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx3lbc, self).__init__()

                            self.yang_name = "high-tx3lbc"
                            self.yang_parent_name = "optics-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                            ])
                            self.is_detected = None
                            self.counter = None
                            self._segment_path = lambda: "high-tx3lbc"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx3lbc, ['is_detected', 'counter'], name, value)


                    class HighTx4lbc(Entity):
                        """
                        High Tx4 laser bias current in units of
                        percentage
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx4lbc, self).__init__()

                            self.yang_name = "high-tx4lbc"
                            self.yang_parent_name = "optics-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                            ])
                            self.is_detected = None
                            self.counter = None
                            self._segment_path = lambda: "high-tx4lbc"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx4lbc, ['is_detected', 'counter'], name, value)


                    class LowTx1lbc(Entity):
                        """
                        Low Tx1 laser bias current in units of
                        percentage
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx1lbc, self).__init__()

                            self.yang_name = "low-tx1lbc"
                            self.yang_parent_name = "optics-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                            ])
                            self.is_detected = None
                            self.counter = None
                            self._segment_path = lambda: "low-tx1lbc"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx1lbc, ['is_detected', 'counter'], name, value)


                    class LowTx2lbc(Entity):
                        """
                        Low Tx2 laser bias current in units of
                        percentage
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx2lbc, self).__init__()

                            self.yang_name = "low-tx2lbc"
                            self.yang_parent_name = "optics-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                            ])
                            self.is_detected = None
                            self.counter = None
                            self._segment_path = lambda: "low-tx2lbc"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx2lbc, ['is_detected', 'counter'], name, value)


                    class LowTx3lbc(Entity):
                        """
                        Low Tx3 laser bias current in units of
                        percentage
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx3lbc, self).__init__()

                            self.yang_name = "low-tx3lbc"
                            self.yang_parent_name = "optics-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                            ])
                            self.is_detected = None
                            self.counter = None
                            self._segment_path = lambda: "low-tx3lbc"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx3lbc, ['is_detected', 'counter'], name, value)


                    class LowTx4lbc(Entity):
                        """
                        Low Tx4 laser bias current in units of
                        percentage
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx4lbc, self).__init__()

                            self.yang_name = "low-tx4lbc"
                            self.yang_parent_name = "optics-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                            ])
                            self.is_detected = None
                            self.counter = None
                            self._segment_path = lambda: "low-tx4lbc"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx4lbc, ['is_detected', 'counter'], name, value)


                    class RxLos(Entity):
                        """
                        RX LOS
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.RxLos, self).__init__()

                            self.yang_name = "rx-los"
                            self.yang_parent_name = "optics-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                            ])
                            self.is_detected = None
                            self.counter = None
                            self._segment_path = lambda: "rx-los"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.RxLos, ['is_detected', 'counter'], name, value)


                    class TxLos(Entity):
                        """
                        TX LOS
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxLos, self).__init__()

                            self.yang_name = "tx-los"
                            self.yang_parent_name = "optics-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                            ])
                            self.is_detected = None
                            self.counter = None
                            self._segment_path = lambda: "tx-los"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxLos, ['is_detected', 'counter'], name, value)


                    class RxLol(Entity):
                        """
                        RX LOL
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.RxLol, self).__init__()

                            self.yang_name = "rx-lol"
                            self.yang_parent_name = "optics-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                            ])
                            self.is_detected = None
                            self.counter = None
                            self._segment_path = lambda: "rx-lol"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.RxLol, ['is_detected', 'counter'], name, value)


                    class TxLol(Entity):
                        """
                        TX LOL
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxLol, self).__init__()

                            self.yang_name = "tx-lol"
                            self.yang_parent_name = "optics-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                            ])
                            self.is_detected = None
                            self.counter = None
                            self._segment_path = lambda: "tx-lol"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxLol, ['is_detected', 'counter'], name, value)


                    class TxFault(Entity):
                        """
                        TX Fault
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxFault, self).__init__()

                            self.yang_name = "tx-fault"
                            self.yang_parent_name = "optics-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                            ])
                            self.is_detected = None
                            self.counter = None
                            self._segment_path = lambda: "tx-fault"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxFault, ['is_detected', 'counter'], name, value)


                    class Hidgd(Entity):
                        """
                        HI DGD
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Hidgd, self).__init__()

                            self.yang_name = "hidgd"
                            self.yang_parent_name = "optics-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                            ])
                            self.is_detected = None
                            self.counter = None
                            self._segment_path = lambda: "hidgd"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Hidgd, ['is_detected', 'counter'], name, value)


                    class Oorcd(Entity):
                        """
                        OOR CD
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Oorcd, self).__init__()

                            self.yang_name = "oorcd"
                            self.yang_parent_name = "optics-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                            ])
                            self.is_detected = None
                            self.counter = None
                            self._segment_path = lambda: "oorcd"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Oorcd, ['is_detected', 'counter'], name, value)


                    class Osnr(Entity):
                        """
                        OSNR
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Osnr, self).__init__()

                            self.yang_name = "osnr"
                            self.yang_parent_name = "optics-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                            ])
                            self.is_detected = None
                            self.counter = None
                            self._segment_path = lambda: "osnr"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Osnr, ['is_detected', 'counter'], name, value)


                    class Wvlool(Entity):
                        """
                        WVL OOL
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Wvlool, self).__init__()

                            self.yang_name = "wvlool"
                            self.yang_parent_name = "optics-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                            ])
                            self.is_detected = None
                            self.counter = None
                            self._segment_path = lambda: "wvlool"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Wvlool, ['is_detected', 'counter'], name, value)


                    class Mea(Entity):
                        """
                        MEA
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Mea, self).__init__()

                            self.yang_name = "mea"
                            self.yang_parent_name = "optics-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                            ])
                            self.is_detected = None
                            self.counter = None
                            self._segment_path = lambda: "mea"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Mea, ['is_detected', 'counter'], name, value)


                    class ImpRemoval(Entity):
                        """
                        IMPROPER REM
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.ImpRemoval, self).__init__()

                            self.yang_name = "imp-removal"
                            self.yang_parent_name = "optics-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                            ])
                            self.is_detected = None
                            self.counter = None
                            self._segment_path = lambda: "imp-removal"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.ImpRemoval, ['is_detected', 'counter'], name, value)


                    class RxLoc(Entity):
                        """
                        Rx LOC
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.RxLoc, self).__init__()

                            self.yang_name = "rx-loc"
                            self.yang_parent_name = "optics-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                            ])
                            self.is_detected = None
                            self.counter = None
                            self._segment_path = lambda: "rx-loc"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.RxLoc, ['is_detected', 'counter'], name, value)


                    class AmpGainDegLow(Entity):
                        """
                        Ampli Gain Deg Low
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.AmpGainDegLow, self).__init__()

                            self.yang_name = "amp-gain-deg-low"
                            self.yang_parent_name = "optics-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                            ])
                            self.is_detected = None
                            self.counter = None
                            self._segment_path = lambda: "amp-gain-deg-low"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.AmpGainDegLow, ['is_detected', 'counter'], name, value)


                    class AmpGainDegHigh(Entity):
                        """
                        Ampli Gain Deg High
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.AmpGainDegHigh, self).__init__()

                            self.yang_name = "amp-gain-deg-high"
                            self.yang_parent_name = "optics-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                            ])
                            self.is_detected = None
                            self.counter = None
                            self._segment_path = lambda: "amp-gain-deg-high"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.AmpGainDegHigh, ['is_detected', 'counter'], name, value)


                    class TxpwrMismatch(Entity):
                        """
                        TX POWER PROV MISMATCH
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxpwrMismatch, self).__init__()

                            self.yang_name = "txpwr-mismatch"
                            self.yang_parent_name = "optics-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                            ])
                            self.is_detected = None
                            self.counter = None
                            self._segment_path = lambda: "txpwr-mismatch"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxpwrMismatch, ['is_detected', 'counter'], name, value)


                class OtsAlarmInfo(Entity):
                    """
                    Ots Alarm Information
                    
                    .. attribute:: low_tx_power
                    
                    	Low Tx Power in units of 0.1 dBm
                    	**type**\:  :py:class:`LowTxPower <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.LowTxPower>`
                    
                    .. attribute:: low_rx_power
                    
                    	Low Rx Power in units of 0.1 dBm
                    	**type**\:  :py:class:`LowRxPower <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.LowRxPower>`
                    
                    .. attribute:: rx_los_p
                    
                    	Rx LOS\_P
                    	**type**\:  :py:class:`RxLosP <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.RxLosP>`
                    
                    .. attribute:: rx_loc
                    
                    	Rx LOC
                    	**type**\:  :py:class:`RxLoc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.RxLoc>`
                    
                    .. attribute:: amp_gain_deg_low
                    
                    	Ampli Gain Deg Low
                    	**type**\:  :py:class:`AmpGainDegLow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AmpGainDegLow>`
                    
                    .. attribute:: amp_gain_deg_high
                    
                    	Ampli Gain Deg High
                    	**type**\:  :py:class:`AmpGainDegHigh <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AmpGainDegHigh>`
                    
                    .. attribute:: auto_laser_shut
                    
                    	Auto Laser Shut
                    	**type**\:  :py:class:`AutoLaserShut <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AutoLaserShut>`
                    
                    .. attribute:: auto_power_red
                    
                    	Auto Power Red
                    	**type**\:  :py:class:`AutoPowerRed <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AutoPowerRed>`
                    
                    .. attribute:: auto_ampli_ctrl_disabled
                    
                    	Auto Ampli Ctrl Disabled
                    	**type**\:  :py:class:`AutoAmpliCtrlDisabled <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AutoAmpliCtrlDisabled>`
                    
                    .. attribute:: auto_ampli_ctrl_config_mismatch
                    
                    	Auto Ampli Ctrl Config Mismatch
                    	**type**\:  :py:class:`AutoAmpliCtrlConfigMismatch <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AutoAmpliCtrlConfigMismatch>`
                    
                    .. attribute:: switch_to_protect
                    
                    	Switch To Protect
                    	**type**\:  :py:class:`SwitchToProtect <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.SwitchToProtect>`
                    
                    .. attribute:: auto_ampli_ctrl_running
                    
                    	Auto Ampli Ctrl Running
                    	**type**\:  :py:class:`AutoAmpliCtrlRunning <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AutoAmpliCtrlRunning>`
                    
                    

                    """

                    _prefix = 'controller-optics-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo, self).__init__()

                        self.yang_name = "ots-alarm-info"
                        self.yang_parent_name = "optics-info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("low-tx-power", ("low_tx_power", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.LowTxPower)), ("low-rx-power", ("low_rx_power", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.LowRxPower)), ("rx-los-p", ("rx_los_p", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.RxLosP)), ("rx-loc", ("rx_loc", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.RxLoc)), ("amp-gain-deg-low", ("amp_gain_deg_low", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AmpGainDegLow)), ("amp-gain-deg-high", ("amp_gain_deg_high", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AmpGainDegHigh)), ("auto-laser-shut", ("auto_laser_shut", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AutoLaserShut)), ("auto-power-red", ("auto_power_red", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AutoPowerRed)), ("auto-ampli-ctrl-disabled", ("auto_ampli_ctrl_disabled", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AutoAmpliCtrlDisabled)), ("auto-ampli-ctrl-config-mismatch", ("auto_ampli_ctrl_config_mismatch", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AutoAmpliCtrlConfigMismatch)), ("switch-to-protect", ("switch_to_protect", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.SwitchToProtect)), ("auto-ampli-ctrl-running", ("auto_ampli_ctrl_running", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AutoAmpliCtrlRunning))])
                        self._leafs = OrderedDict()

                        self.low_tx_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.LowTxPower()
                        self.low_tx_power.parent = self
                        self._children_name_map["low_tx_power"] = "low-tx-power"

                        self.low_rx_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.LowRxPower()
                        self.low_rx_power.parent = self
                        self._children_name_map["low_rx_power"] = "low-rx-power"

                        self.rx_los_p = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.RxLosP()
                        self.rx_los_p.parent = self
                        self._children_name_map["rx_los_p"] = "rx-los-p"

                        self.rx_loc = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.RxLoc()
                        self.rx_loc.parent = self
                        self._children_name_map["rx_loc"] = "rx-loc"

                        self.amp_gain_deg_low = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AmpGainDegLow()
                        self.amp_gain_deg_low.parent = self
                        self._children_name_map["amp_gain_deg_low"] = "amp-gain-deg-low"

                        self.amp_gain_deg_high = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AmpGainDegHigh()
                        self.amp_gain_deg_high.parent = self
                        self._children_name_map["amp_gain_deg_high"] = "amp-gain-deg-high"

                        self.auto_laser_shut = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AutoLaserShut()
                        self.auto_laser_shut.parent = self
                        self._children_name_map["auto_laser_shut"] = "auto-laser-shut"

                        self.auto_power_red = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AutoPowerRed()
                        self.auto_power_red.parent = self
                        self._children_name_map["auto_power_red"] = "auto-power-red"

                        self.auto_ampli_ctrl_disabled = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AutoAmpliCtrlDisabled()
                        self.auto_ampli_ctrl_disabled.parent = self
                        self._children_name_map["auto_ampli_ctrl_disabled"] = "auto-ampli-ctrl-disabled"

                        self.auto_ampli_ctrl_config_mismatch = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AutoAmpliCtrlConfigMismatch()
                        self.auto_ampli_ctrl_config_mismatch.parent = self
                        self._children_name_map["auto_ampli_ctrl_config_mismatch"] = "auto-ampli-ctrl-config-mismatch"

                        self.switch_to_protect = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.SwitchToProtect()
                        self.switch_to_protect.parent = self
                        self._children_name_map["switch_to_protect"] = "switch-to-protect"

                        self.auto_ampli_ctrl_running = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AutoAmpliCtrlRunning()
                        self.auto_ampli_ctrl_running.parent = self
                        self._children_name_map["auto_ampli_ctrl_running"] = "auto-ampli-ctrl-running"
                        self._segment_path = lambda: "ots-alarm-info"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo, [], name, value)


                    class LowTxPower(Entity):
                        """
                        Low Tx Power in units of 0.1 dBm
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.LowTxPower, self).__init__()

                            self.yang_name = "low-tx-power"
                            self.yang_parent_name = "ots-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                            ])
                            self.is_detected = None
                            self.counter = None
                            self._segment_path = lambda: "low-tx-power"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.LowTxPower, ['is_detected', 'counter'], name, value)


                    class LowRxPower(Entity):
                        """
                        Low Rx Power in units of 0.1 dBm
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.LowRxPower, self).__init__()

                            self.yang_name = "low-rx-power"
                            self.yang_parent_name = "ots-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                            ])
                            self.is_detected = None
                            self.counter = None
                            self._segment_path = lambda: "low-rx-power"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.LowRxPower, ['is_detected', 'counter'], name, value)


                    class RxLosP(Entity):
                        """
                        Rx LOS\_P
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.RxLosP, self).__init__()

                            self.yang_name = "rx-los-p"
                            self.yang_parent_name = "ots-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                            ])
                            self.is_detected = None
                            self.counter = None
                            self._segment_path = lambda: "rx-los-p"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.RxLosP, ['is_detected', 'counter'], name, value)


                    class RxLoc(Entity):
                        """
                        Rx LOC
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.RxLoc, self).__init__()

                            self.yang_name = "rx-loc"
                            self.yang_parent_name = "ots-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                            ])
                            self.is_detected = None
                            self.counter = None
                            self._segment_path = lambda: "rx-loc"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.RxLoc, ['is_detected', 'counter'], name, value)


                    class AmpGainDegLow(Entity):
                        """
                        Ampli Gain Deg Low
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AmpGainDegLow, self).__init__()

                            self.yang_name = "amp-gain-deg-low"
                            self.yang_parent_name = "ots-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                            ])
                            self.is_detected = None
                            self.counter = None
                            self._segment_path = lambda: "amp-gain-deg-low"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AmpGainDegLow, ['is_detected', 'counter'], name, value)


                    class AmpGainDegHigh(Entity):
                        """
                        Ampli Gain Deg High
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AmpGainDegHigh, self).__init__()

                            self.yang_name = "amp-gain-deg-high"
                            self.yang_parent_name = "ots-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                            ])
                            self.is_detected = None
                            self.counter = None
                            self._segment_path = lambda: "amp-gain-deg-high"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AmpGainDegHigh, ['is_detected', 'counter'], name, value)


                    class AutoLaserShut(Entity):
                        """
                        Auto Laser Shut
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AutoLaserShut, self).__init__()

                            self.yang_name = "auto-laser-shut"
                            self.yang_parent_name = "ots-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                            ])
                            self.is_detected = None
                            self.counter = None
                            self._segment_path = lambda: "auto-laser-shut"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AutoLaserShut, ['is_detected', 'counter'], name, value)


                    class AutoPowerRed(Entity):
                        """
                        Auto Power Red
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AutoPowerRed, self).__init__()

                            self.yang_name = "auto-power-red"
                            self.yang_parent_name = "ots-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                            ])
                            self.is_detected = None
                            self.counter = None
                            self._segment_path = lambda: "auto-power-red"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AutoPowerRed, ['is_detected', 'counter'], name, value)


                    class AutoAmpliCtrlDisabled(Entity):
                        """
                        Auto Ampli Ctrl Disabled
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AutoAmpliCtrlDisabled, self).__init__()

                            self.yang_name = "auto-ampli-ctrl-disabled"
                            self.yang_parent_name = "ots-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                            ])
                            self.is_detected = None
                            self.counter = None
                            self._segment_path = lambda: "auto-ampli-ctrl-disabled"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AutoAmpliCtrlDisabled, ['is_detected', 'counter'], name, value)


                    class AutoAmpliCtrlConfigMismatch(Entity):
                        """
                        Auto Ampli Ctrl Config Mismatch
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AutoAmpliCtrlConfigMismatch, self).__init__()

                            self.yang_name = "auto-ampli-ctrl-config-mismatch"
                            self.yang_parent_name = "ots-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                            ])
                            self.is_detected = None
                            self.counter = None
                            self._segment_path = lambda: "auto-ampli-ctrl-config-mismatch"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AutoAmpliCtrlConfigMismatch, ['is_detected', 'counter'], name, value)


                    class SwitchToProtect(Entity):
                        """
                        Switch To Protect
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.SwitchToProtect, self).__init__()

                            self.yang_name = "switch-to-protect"
                            self.yang_parent_name = "ots-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                            ])
                            self.is_detected = None
                            self.counter = None
                            self._segment_path = lambda: "switch-to-protect"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.SwitchToProtect, ['is_detected', 'counter'], name, value)


                    class AutoAmpliCtrlRunning(Entity):
                        """
                        Auto Ampli Ctrl Running
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AutoAmpliCtrlRunning, self).__init__()

                            self.yang_name = "auto-ampli-ctrl-running"
                            self.yang_parent_name = "ots-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                            ])
                            self.is_detected = None
                            self.counter = None
                            self._segment_path = lambda: "auto-ampli-ctrl-running"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AutoAmpliCtrlRunning, ['is_detected', 'counter'], name, value)


                class TransceiverInfo(Entity):
                    """
                    Transceiver Vendor Details
                    
                    .. attribute:: vendor_info
                    
                    	Vendor Information
                    	**type**\: str
                    
                    .. attribute:: adapter_vendor_info
                    
                    	Adapter Vendor Information
                    	**type**\: str
                    
                    .. attribute:: date
                    
                    	Date in Transceiver
                    	**type**\: str
                    
                    .. attribute:: optics_vendor_rev
                    
                    	Transceiver vendors revision number
                    	**type**\: str
                    
                    .. attribute:: optics_serial_no
                    
                    	Transceiver serial number
                    	**type**\: str
                    
                    .. attribute:: optics_vendor_part
                    
                    	Transceiver vendors part number
                    	**type**\: str
                    
                    .. attribute:: optics_type
                    
                    	Transceiver optics type
                    	**type**\: str
                    
                    .. attribute:: vendor_name
                    
                    	Transceiver optics vendor name
                    	**type**\: str
                    
                    .. attribute:: oui_no
                    
                    	Transceiver optics type
                    	**type**\: str
                    
                    .. attribute:: optics_pid
                    
                    	Transceiver optics pid
                    	**type**\: str
                    
                    .. attribute:: optics_vid
                    
                    	Transceiver optics vid
                    	**type**\: str
                    
                    .. attribute:: connector_type
                    
                    	Connector type
                    	**type**\:  :py:class:`FiberConnector <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.FiberConnector>`
                    
                    .. attribute:: otn_application_code
                    
                    	Otn Application Code
                    	**type**\:  :py:class:`OtnApplicationCode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OtnApplicationCode>`
                    
                    .. attribute:: sonet_application_code
                    
                    	Sonet Application Code
                    	**type**\:  :py:class:`SonetApplicationCode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.SonetApplicationCode>`
                    
                    .. attribute:: ethernet_compliance_code
                    
                    	Ethernet Compliance Code
                    	**type**\:  :py:class:`EthernetPmd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.EthernetPmd>`
                    
                    .. attribute:: internal_temperature
                    
                    	Internal Temperature in units of C
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    

                    """

                    _prefix = 'controller-optics-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.TransceiverInfo, self).__init__()

                        self.yang_name = "transceiver-info"
                        self.yang_parent_name = "optics-info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('vendor_info', (YLeaf(YType.str, 'vendor-info'), ['str'])),
                            ('adapter_vendor_info', (YLeaf(YType.str, 'adapter-vendor-info'), ['str'])),
                            ('date', (YLeaf(YType.str, 'date'), ['str'])),
                            ('optics_vendor_rev', (YLeaf(YType.str, 'optics-vendor-rev'), ['str'])),
                            ('optics_serial_no', (YLeaf(YType.str, 'optics-serial-no'), ['str'])),
                            ('optics_vendor_part', (YLeaf(YType.str, 'optics-vendor-part'), ['str'])),
                            ('optics_type', (YLeaf(YType.str, 'optics-type'), ['str'])),
                            ('vendor_name', (YLeaf(YType.str, 'vendor-name'), ['str'])),
                            ('oui_no', (YLeaf(YType.str, 'oui-no'), ['str'])),
                            ('optics_pid', (YLeaf(YType.str, 'optics-pid'), ['str'])),
                            ('optics_vid', (YLeaf(YType.str, 'optics-vid'), ['str'])),
                            ('connector_type', (YLeaf(YType.enumeration, 'connector-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'FiberConnector', '')])),
                            ('otn_application_code', (YLeaf(YType.enumeration, 'otn-application-code'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OtnApplicationCode', '')])),
                            ('sonet_application_code', (YLeaf(YType.enumeration, 'sonet-application-code'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'SonetApplicationCode', '')])),
                            ('ethernet_compliance_code', (YLeaf(YType.enumeration, 'ethernet-compliance-code'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'EthernetPmd', '')])),
                            ('internal_temperature', (YLeaf(YType.int32, 'internal-temperature'), ['int'])),
                        ])
                        self.vendor_info = None
                        self.adapter_vendor_info = None
                        self.date = None
                        self.optics_vendor_rev = None
                        self.optics_serial_no = None
                        self.optics_vendor_part = None
                        self.optics_type = None
                        self.vendor_name = None
                        self.oui_no = None
                        self.optics_pid = None
                        self.optics_vid = None
                        self.connector_type = None
                        self.otn_application_code = None
                        self.sonet_application_code = None
                        self.ethernet_compliance_code = None
                        self.internal_temperature = None
                        self._segment_path = lambda: "transceiver-info"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.TransceiverInfo, ['vendor_info', 'adapter_vendor_info', 'date', 'optics_vendor_rev', 'optics_serial_no', 'optics_vendor_part', 'optics_type', 'vendor_name', 'oui_no', 'optics_pid', 'optics_vid', 'connector_type', 'otn_application_code', 'sonet_application_code', 'ethernet_compliance_code', 'internal_temperature'], name, value)


                class ExtParamVal(Entity):
                    """
                    Extended optics parameters
                    
                    .. attribute:: snr_lane1
                    
                    	Signal to Noise Ratio on Lane 1
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: snr_lane2
                    
                    	Signal to Noise Ratio on Lane 2
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: isi_correction_lane1
                    
                    	Inter symbol Interference correction on Lane 1
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: isi_correction_lane2
                    
                    	Inter symbol Interference correction on Lane 2
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: pam_rate_lane1
                    
                    	PAM Histogram parameter on Lane 1
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: pam_rate_lane2
                    
                    	PAM Histogram parameter on Lane 2
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: pre_fec_ber
                    
                    	Pre FEC BER since last counter reset
                    	**type**\: int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: uncorrected_ber
                    
                    	Uncorrected BER since last counter reset
                    	**type**\: int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: tec_current_lane1
                    
                    	Current flowing to the TEC of a cooled laser on Lane 1
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: tec_current_lane2
                    
                    	Current flowing to the TEC of a cooled laser on Lane 2
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: laser_diff_frequency_lane1
                    
                    	Difference between target and actual center frequency on Lane 1
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: laser_diff_frequency_lane2
                    
                    	Difference between target and actual center frequency on Lane 2
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: laser_diff_temperature_lane1
                    
                    	Difference between target and actual temperature on Lane 1
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: laser_diff_temperature_lane2
                    
                    	Difference between target and actual temperature on Lane 2
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: pre_fec_ber_latched_min
                    
                    	Latched minimum Pre FEC BER value since last read, line ingress
                    	**type**\: int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: pre_fec_ber_latched_max
                    
                    	Latched maximum Pre FEC BER value since last read, line ingress
                    	**type**\: int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: pre_fec_ber_accumulated
                    
                    	Pre FEC BER value prior accumulation period, line ingress
                    	**type**\: int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: pre_fec_ber_instantaneous
                    
                    	Pre FEC BER value instantaneous line ingress
                    	**type**\: int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: uncorrected_ber_latched_min
                    
                    	Latched minimum Uncorrected BER value since last read, line ingress
                    	**type**\: int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: uncorrected_ber_latched_max
                    
                    	Latched maximum Uncorrected BER value since last read, line ingress
                    	**type**\: int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: uncorrected_ber_accumulated
                    
                    	Uncorrected BER value prior accumulation period, line ingress
                    	**type**\: int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: uncorrected_ber_instantaneous
                    
                    	Uncorrected BER value instantaneous line line ingress
                    	**type**\: int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    

                    """

                    _prefix = 'controller-optics-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtParamVal, self).__init__()

                        self.yang_name = "ext-param-val"
                        self.yang_parent_name = "optics-info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('snr_lane1', (YLeaf(YType.int32, 'snr-lane1'), ['int'])),
                            ('snr_lane2', (YLeaf(YType.int32, 'snr-lane2'), ['int'])),
                            ('isi_correction_lane1', (YLeaf(YType.int32, 'isi-correction-lane1'), ['int'])),
                            ('isi_correction_lane2', (YLeaf(YType.int32, 'isi-correction-lane2'), ['int'])),
                            ('pam_rate_lane1', (YLeaf(YType.int32, 'pam-rate-lane1'), ['int'])),
                            ('pam_rate_lane2', (YLeaf(YType.int32, 'pam-rate-lane2'), ['int'])),
                            ('pre_fec_ber', (YLeaf(YType.int64, 'pre-fec-ber'), ['int'])),
                            ('uncorrected_ber', (YLeaf(YType.int64, 'uncorrected-ber'), ['int'])),
                            ('tec_current_lane1', (YLeaf(YType.int32, 'tec-current-lane1'), ['int'])),
                            ('tec_current_lane2', (YLeaf(YType.int32, 'tec-current-lane2'), ['int'])),
                            ('laser_diff_frequency_lane1', (YLeaf(YType.int32, 'laser-diff-frequency-lane1'), ['int'])),
                            ('laser_diff_frequency_lane2', (YLeaf(YType.int32, 'laser-diff-frequency-lane2'), ['int'])),
                            ('laser_diff_temperature_lane1', (YLeaf(YType.int32, 'laser-diff-temperature-lane1'), ['int'])),
                            ('laser_diff_temperature_lane2', (YLeaf(YType.int32, 'laser-diff-temperature-lane2'), ['int'])),
                            ('pre_fec_ber_latched_min', (YLeaf(YType.int64, 'pre-fec-ber-latched-min'), ['int'])),
                            ('pre_fec_ber_latched_max', (YLeaf(YType.int64, 'pre-fec-ber-latched-max'), ['int'])),
                            ('pre_fec_ber_accumulated', (YLeaf(YType.int64, 'pre-fec-ber-accumulated'), ['int'])),
                            ('pre_fec_ber_instantaneous', (YLeaf(YType.int64, 'pre-fec-ber-instantaneous'), ['int'])),
                            ('uncorrected_ber_latched_min', (YLeaf(YType.int64, 'uncorrected-ber-latched-min'), ['int'])),
                            ('uncorrected_ber_latched_max', (YLeaf(YType.int64, 'uncorrected-ber-latched-max'), ['int'])),
                            ('uncorrected_ber_accumulated', (YLeaf(YType.int64, 'uncorrected-ber-accumulated'), ['int'])),
                            ('uncorrected_ber_instantaneous', (YLeaf(YType.int64, 'uncorrected-ber-instantaneous'), ['int'])),
                        ])
                        self.snr_lane1 = None
                        self.snr_lane2 = None
                        self.isi_correction_lane1 = None
                        self.isi_correction_lane2 = None
                        self.pam_rate_lane1 = None
                        self.pam_rate_lane2 = None
                        self.pre_fec_ber = None
                        self.uncorrected_ber = None
                        self.tec_current_lane1 = None
                        self.tec_current_lane2 = None
                        self.laser_diff_frequency_lane1 = None
                        self.laser_diff_frequency_lane2 = None
                        self.laser_diff_temperature_lane1 = None
                        self.laser_diff_temperature_lane2 = None
                        self.pre_fec_ber_latched_min = None
                        self.pre_fec_ber_latched_max = None
                        self.pre_fec_ber_accumulated = None
                        self.pre_fec_ber_instantaneous = None
                        self.uncorrected_ber_latched_min = None
                        self.uncorrected_ber_latched_max = None
                        self.uncorrected_ber_accumulated = None
                        self.uncorrected_ber_instantaneous = None
                        self._segment_path = lambda: "ext-param-val"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtParamVal, ['snr_lane1', 'snr_lane2', 'isi_correction_lane1', 'isi_correction_lane2', 'pam_rate_lane1', 'pam_rate_lane2', 'pre_fec_ber', 'uncorrected_ber', 'tec_current_lane1', 'tec_current_lane2', 'laser_diff_frequency_lane1', 'laser_diff_frequency_lane2', 'laser_diff_temperature_lane1', 'laser_diff_temperature_lane2', 'pre_fec_ber_latched_min', 'pre_fec_ber_latched_max', 'pre_fec_ber_accumulated', 'pre_fec_ber_instantaneous', 'uncorrected_ber_latched_min', 'uncorrected_ber_latched_max', 'uncorrected_ber_accumulated', 'uncorrected_ber_instantaneous'], name, value)


                class ExtParamThresholdVal(Entity):
                    """
                    Extended optics parameters threshold values
                    
                    .. attribute:: snr_alarm_high_threshold
                    
                    	High threshold alarm for SNR
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: snr_alarm_low_threshold
                    
                    	Low threshold alarm for SNR
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: snr_warn_high_threshold
                    
                    	High threshold warning for SNR
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: snr_warn_low_threshold
                    
                    	Low threshold warning for SNR
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: isi_correction_alarm_high_threshold
                    
                    	High threshold alarm for ISI Correction
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: isi_correction_alarm_low_threshold
                    
                    	Low threshold alarm for ISI Correction
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: isi_correction_warn_high_threshold
                    
                    	High threshold warning for ISI Correction
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: isi_correction_warn_low_threshold
                    
                    	Low threshold warning for ISI Correction
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: pam_rate_alarm_high_threshold
                    
                    	High threshold alarm for PAM Rate
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: pam_rate_alarm_low_threshold
                    
                    	Low threshold alarm for PAM Rate
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: pam_rate_warn_high_threshold
                    
                    	High threshold warning for PAM Rate
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: pam_rate_warn_low_threshold
                    
                    	Low threshold warning for PAM Rate
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: pre_fec_ber_alarm_high_threshold
                    
                    	High threshold alarm for Pre FEC BER
                    	**type**\: int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: pre_fec_ber_alarm_low_threshold
                    
                    	Low threshold alarm for Pre FEC BER
                    	**type**\: int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: pre_fec_ber_warn_high_threshold
                    
                    	High threshold warning for Pre FEC BER
                    	**type**\: int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: pre_fec_ber_warn_low_threshold
                    
                    	Low threshold warning for Pre FEC BER
                    	**type**\: int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: uncorrected_ber_alarm_high_threshold
                    
                    	High threshold alarm for Uncorrected BER
                    	**type**\: int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: uncorrected_ber_alarm_low_threshold
                    
                    	Low threshold alarm for Uncorrected BER
                    	**type**\: int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: uncorrected_ber_warn_high_threshold
                    
                    	High threshold warning for Uncorrected BER
                    	**type**\: int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: uncorrected_ber_warn_low_threshold
                    
                    	Low threshold warning for Uncorrected BER
                    	**type**\: int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: tec_current_alarm_high_threshold
                    
                    	High threshold alarm for TEC Current
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: tec_current_alarm_low_threshold
                    
                    	Low threshold alarm for TEC Current
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: tec_current_warn_high_threshold
                    
                    	High threshold warning for TEC Current
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: tec_current_warn_low_threshold
                    
                    	Low threshold warning for TEC Current
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: laser_diff_frequency_alarm_high_threshold
                    
                    	High Threshold Alarm for Differential Laser Frequency
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: laser_diff_frequency_alarm_low_threshold
                    
                    	Low Threshold Alarm for Differential Laser Frequency
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: laser_diff_frequency_warn_high_threshold
                    
                    	High Threshold Warning for Differential Laser Frequency
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: laser_diff_frequency_warn_low_threshold
                    
                    	Low Threshold Warning for Differential Laser Frequency
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: laser_diff_temperature_alarm_high_threshold
                    
                    	High Threshold Alarm for Differential Laser Temperature
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: laser_diff_temperature_alarm_low_threshold
                    
                    	Low Threshold Alarm for Differential Laser Temperature
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: laser_diff_temperature_warn_high_threshold
                    
                    	High Threshold Warning for Differential Laser Temperature
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: laser_diff_temperature_warn_low_threshold
                    
                    	Low Threshold Warning for Differential Laser Temperature
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: pre_fec_ber_latched_min_alarm_high_threshold
                    
                    	High threshold alarm for Latched Min Pre FEC BER
                    	**type**\: int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: pre_fec_ber_latched_min_alarm_low_threshold
                    
                    	Low threshold alarm for Latched Min Pre FEC BER
                    	**type**\: int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: pre_fec_ber_latched_min_warn_high_threshold
                    
                    	High threshold warning for Latched Min Pre FEC BER
                    	**type**\: int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: pre_fec_ber_latched_min_warn_low_threshold
                    
                    	Low threshold warning for Latched Min Pre FEC BER
                    	**type**\: int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: pre_fec_ber_latched_max_alarm_high_threshold
                    
                    	High threshold alarm for Latched Max Pre FEC BER
                    	**type**\: int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: pre_fec_ber_latched_max_alarm_low_threshold
                    
                    	Low threshold alarm for Latched Max Pre FEC BER
                    	**type**\: int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: pre_fec_ber_latched_max_warn_high_threshold
                    
                    	High threshold warning for Latched Max Pre FEC BER
                    	**type**\: int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: pre_fec_ber_latched_max_warn_low_threshold
                    
                    	Low threshold warning for Latched Max Pre FEC BER
                    	**type**\: int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: pre_fec_ber_accumulated_alarm_high_threshold
                    
                    	High threshold alarm for Accumulated Pre FEC BER
                    	**type**\: int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: pre_fec_ber_accumulated_alarm_low_threshold
                    
                    	Low threshold alarm for Accumulated Pre FEC BER
                    	**type**\: int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: pre_fec_ber_accumulated_warn_high_threshold
                    
                    	High threshold warning for Accumulated Pre FEC BER
                    	**type**\: int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: pre_fec_ber_accumulated_warn_low_threshold
                    
                    	Low threshold warning for Accumulated Pre FEC BER
                    	**type**\: int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: pre_fec_ber_instantaneous_alarm_high_threshold
                    
                    	High threshold alarm for Instantaneous Pre FEC BER
                    	**type**\: int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: pre_fec_ber_instantaneous_alarm_low_threshold
                    
                    	Low threshold alarm for Instantaneous Pre FEC BER
                    	**type**\: int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: pre_fec_ber_instantaneous_warn_high_threshold
                    
                    	High threshold warning for Instantaneous Pre FEC BER
                    	**type**\: int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: pre_fec_ber_instantaneous_warn_low_threshold
                    
                    	Low threshold warning for Instantaneous Pre FEC BER
                    	**type**\: int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: uncorrected_ber_latched_min_alarm_high_threshold
                    
                    	High threshold alarm for  Latched Min Uncorrected BER
                    	**type**\: int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: uncorrected_ber_latched_min_alarm_low_threshold
                    
                    	Low threshold alarm for  Latched Min Uncorrected BER
                    	**type**\: int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: uncorrected_ber_latched_min_warn_high_threshold
                    
                    	High threshold warning for  Latched Min Uncorrected BER
                    	**type**\: int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: uncorrected_ber_latched_min_warn_low_threshold
                    
                    	Low threshold alarm for Latched Min Uncorrected BER
                    	**type**\: int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: uncorrected_ber_latched_max_alarm_high_threshold
                    
                    	High threshold alarm for Latched\_Max Uncorrected BER
                    	**type**\: int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: uncorrected_ber_latched_max_alarm_low_threshold
                    
                    	Low threshold alarm for Latched\_Max Uncorrected BER
                    	**type**\: int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: uncorrected_ber_latched_max_warn_high_threshold
                    
                    	High threshold warning Latched\_Max for Uncorrected BER
                    	**type**\: int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: uncorrected_ber_latched_max_warn_low_threshold
                    
                    	Low threshold warning Latched\_Max for Uncorrected BER
                    	**type**\: int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: uncorrected_ber_accumulated_alarm_high_threshold
                    
                    	High threshold alarm for Accumulated Uncorrected BER
                    	**type**\: int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: uncorrected_ber_accumulated_alarm_low_threshold
                    
                    	Low threshold alarm for Accumulated Uncorrected BER
                    	**type**\: int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: uncorrected_ber_accumulated_warn_high_threshold
                    
                    	High threshold warning for Accumulated Uncorrected BER
                    	**type**\: int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: uncorrected_ber_accumulated_warn_low_threshold
                    
                    	Low threshold warning for Accumulated Uncorrected BER
                    	**type**\: int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: uncorrected_ber_instantaneous_alarm_high_threshold
                    
                    	High threshold alarm for Instantaneous Uncorrected BER
                    	**type**\: int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: uncorrected_ber_instantaneous_alarm_low_threshold
                    
                    	Low threshold alarm for Instantaneous Uncorrected BER
                    	**type**\: int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: uncorrected_ber_instantaneous_warn_high_threshold
                    
                    	High threshold warning for Instantaneous Uncorrected BER
                    	**type**\: int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: uncorrected_ber_instantaneous_warn_low_threshold
                    
                    	Low threshold warning for Instantaneous Uncorrected BER
                    	**type**\: int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    

                    """

                    _prefix = 'controller-optics-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtParamThresholdVal, self).__init__()

                        self.yang_name = "ext-param-threshold-val"
                        self.yang_parent_name = "optics-info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('snr_alarm_high_threshold', (YLeaf(YType.int32, 'snr-alarm-high-threshold'), ['int'])),
                            ('snr_alarm_low_threshold', (YLeaf(YType.int32, 'snr-alarm-low-threshold'), ['int'])),
                            ('snr_warn_high_threshold', (YLeaf(YType.int32, 'snr-warn-high-threshold'), ['int'])),
                            ('snr_warn_low_threshold', (YLeaf(YType.int32, 'snr-warn-low-threshold'), ['int'])),
                            ('isi_correction_alarm_high_threshold', (YLeaf(YType.int32, 'isi-correction-alarm-high-threshold'), ['int'])),
                            ('isi_correction_alarm_low_threshold', (YLeaf(YType.int32, 'isi-correction-alarm-low-threshold'), ['int'])),
                            ('isi_correction_warn_high_threshold', (YLeaf(YType.int32, 'isi-correction-warn-high-threshold'), ['int'])),
                            ('isi_correction_warn_low_threshold', (YLeaf(YType.int32, 'isi-correction-warn-low-threshold'), ['int'])),
                            ('pam_rate_alarm_high_threshold', (YLeaf(YType.int32, 'pam-rate-alarm-high-threshold'), ['int'])),
                            ('pam_rate_alarm_low_threshold', (YLeaf(YType.int32, 'pam-rate-alarm-low-threshold'), ['int'])),
                            ('pam_rate_warn_high_threshold', (YLeaf(YType.int32, 'pam-rate-warn-high-threshold'), ['int'])),
                            ('pam_rate_warn_low_threshold', (YLeaf(YType.int32, 'pam-rate-warn-low-threshold'), ['int'])),
                            ('pre_fec_ber_alarm_high_threshold', (YLeaf(YType.int64, 'pre-fec-ber-alarm-high-threshold'), ['int'])),
                            ('pre_fec_ber_alarm_low_threshold', (YLeaf(YType.int64, 'pre-fec-ber-alarm-low-threshold'), ['int'])),
                            ('pre_fec_ber_warn_high_threshold', (YLeaf(YType.int64, 'pre-fec-ber-warn-high-threshold'), ['int'])),
                            ('pre_fec_ber_warn_low_threshold', (YLeaf(YType.int64, 'pre-fec-ber-warn-low-threshold'), ['int'])),
                            ('uncorrected_ber_alarm_high_threshold', (YLeaf(YType.int64, 'uncorrected-ber-alarm-high-threshold'), ['int'])),
                            ('uncorrected_ber_alarm_low_threshold', (YLeaf(YType.int64, 'uncorrected-ber-alarm-low-threshold'), ['int'])),
                            ('uncorrected_ber_warn_high_threshold', (YLeaf(YType.int64, 'uncorrected-ber-warn-high-threshold'), ['int'])),
                            ('uncorrected_ber_warn_low_threshold', (YLeaf(YType.int64, 'uncorrected-ber-warn-low-threshold'), ['int'])),
                            ('tec_current_alarm_high_threshold', (YLeaf(YType.int32, 'tec-current-alarm-high-threshold'), ['int'])),
                            ('tec_current_alarm_low_threshold', (YLeaf(YType.int32, 'tec-current-alarm-low-threshold'), ['int'])),
                            ('tec_current_warn_high_threshold', (YLeaf(YType.int32, 'tec-current-warn-high-threshold'), ['int'])),
                            ('tec_current_warn_low_threshold', (YLeaf(YType.int32, 'tec-current-warn-low-threshold'), ['int'])),
                            ('laser_diff_frequency_alarm_high_threshold', (YLeaf(YType.int32, 'laser-diff-frequency-alarm-high-threshold'), ['int'])),
                            ('laser_diff_frequency_alarm_low_threshold', (YLeaf(YType.int32, 'laser-diff-frequency-alarm-low-threshold'), ['int'])),
                            ('laser_diff_frequency_warn_high_threshold', (YLeaf(YType.int32, 'laser-diff-frequency-warn-high-threshold'), ['int'])),
                            ('laser_diff_frequency_warn_low_threshold', (YLeaf(YType.int32, 'laser-diff-frequency-warn-low-threshold'), ['int'])),
                            ('laser_diff_temperature_alarm_high_threshold', (YLeaf(YType.int32, 'laser-diff-temperature-alarm-high-threshold'), ['int'])),
                            ('laser_diff_temperature_alarm_low_threshold', (YLeaf(YType.int32, 'laser-diff-temperature-alarm-low-threshold'), ['int'])),
                            ('laser_diff_temperature_warn_high_threshold', (YLeaf(YType.int32, 'laser-diff-temperature-warn-high-threshold'), ['int'])),
                            ('laser_diff_temperature_warn_low_threshold', (YLeaf(YType.int32, 'laser-diff-temperature-warn-low-threshold'), ['int'])),
                            ('pre_fec_ber_latched_min_alarm_high_threshold', (YLeaf(YType.int64, 'pre-fec-ber-latched-min-alarm-high-threshold'), ['int'])),
                            ('pre_fec_ber_latched_min_alarm_low_threshold', (YLeaf(YType.int64, 'pre-fec-ber-latched-min-alarm-low-threshold'), ['int'])),
                            ('pre_fec_ber_latched_min_warn_high_threshold', (YLeaf(YType.int64, 'pre-fec-ber-latched-min-warn-high-threshold'), ['int'])),
                            ('pre_fec_ber_latched_min_warn_low_threshold', (YLeaf(YType.int64, 'pre-fec-ber-latched-min-warn-low-threshold'), ['int'])),
                            ('pre_fec_ber_latched_max_alarm_high_threshold', (YLeaf(YType.int64, 'pre-fec-ber-latched-max-alarm-high-threshold'), ['int'])),
                            ('pre_fec_ber_latched_max_alarm_low_threshold', (YLeaf(YType.int64, 'pre-fec-ber-latched-max-alarm-low-threshold'), ['int'])),
                            ('pre_fec_ber_latched_max_warn_high_threshold', (YLeaf(YType.int64, 'pre-fec-ber-latched-max-warn-high-threshold'), ['int'])),
                            ('pre_fec_ber_latched_max_warn_low_threshold', (YLeaf(YType.int64, 'pre-fec-ber-latched-max-warn-low-threshold'), ['int'])),
                            ('pre_fec_ber_accumulated_alarm_high_threshold', (YLeaf(YType.int64, 'pre-fec-ber-accumulated-alarm-high-threshold'), ['int'])),
                            ('pre_fec_ber_accumulated_alarm_low_threshold', (YLeaf(YType.int64, 'pre-fec-ber-accumulated-alarm-low-threshold'), ['int'])),
                            ('pre_fec_ber_accumulated_warn_high_threshold', (YLeaf(YType.int64, 'pre-fec-ber-accumulated-warn-high-threshold'), ['int'])),
                            ('pre_fec_ber_accumulated_warn_low_threshold', (YLeaf(YType.int64, 'pre-fec-ber-accumulated-warn-low-threshold'), ['int'])),
                            ('pre_fec_ber_instantaneous_alarm_high_threshold', (YLeaf(YType.int64, 'pre-fec-ber-instantaneous-alarm-high-threshold'), ['int'])),
                            ('pre_fec_ber_instantaneous_alarm_low_threshold', (YLeaf(YType.int64, 'pre-fec-ber-instantaneous-alarm-low-threshold'), ['int'])),
                            ('pre_fec_ber_instantaneous_warn_high_threshold', (YLeaf(YType.int64, 'pre-fec-ber-instantaneous-warn-high-threshold'), ['int'])),
                            ('pre_fec_ber_instantaneous_warn_low_threshold', (YLeaf(YType.int64, 'pre-fec-ber-instantaneous-warn-low-threshold'), ['int'])),
                            ('uncorrected_ber_latched_min_alarm_high_threshold', (YLeaf(YType.int64, 'uncorrected-ber-latched-min-alarm-high-threshold'), ['int'])),
                            ('uncorrected_ber_latched_min_alarm_low_threshold', (YLeaf(YType.int64, 'uncorrected-ber-latched-min-alarm-low-threshold'), ['int'])),
                            ('uncorrected_ber_latched_min_warn_high_threshold', (YLeaf(YType.int64, 'uncorrected-ber-latched-min-warn-high-threshold'), ['int'])),
                            ('uncorrected_ber_latched_min_warn_low_threshold', (YLeaf(YType.int64, 'uncorrected-ber-latched-min-warn-low-threshold'), ['int'])),
                            ('uncorrected_ber_latched_max_alarm_high_threshold', (YLeaf(YType.int64, 'uncorrected-ber-latched-max-alarm-high-threshold'), ['int'])),
                            ('uncorrected_ber_latched_max_alarm_low_threshold', (YLeaf(YType.int64, 'uncorrected-ber-latched-max-alarm-low-threshold'), ['int'])),
                            ('uncorrected_ber_latched_max_warn_high_threshold', (YLeaf(YType.int64, 'uncorrected-ber-latched-max-warn-high-threshold'), ['int'])),
                            ('uncorrected_ber_latched_max_warn_low_threshold', (YLeaf(YType.int64, 'uncorrected-ber-latched-max-warn-low-threshold'), ['int'])),
                            ('uncorrected_ber_accumulated_alarm_high_threshold', (YLeaf(YType.int64, 'uncorrected-ber-accumulated-alarm-high-threshold'), ['int'])),
                            ('uncorrected_ber_accumulated_alarm_low_threshold', (YLeaf(YType.int64, 'uncorrected-ber-accumulated-alarm-low-threshold'), ['int'])),
                            ('uncorrected_ber_accumulated_warn_high_threshold', (YLeaf(YType.int64, 'uncorrected-ber-accumulated-warn-high-threshold'), ['int'])),
                            ('uncorrected_ber_accumulated_warn_low_threshold', (YLeaf(YType.int64, 'uncorrected-ber-accumulated-warn-low-threshold'), ['int'])),
                            ('uncorrected_ber_instantaneous_alarm_high_threshold', (YLeaf(YType.int64, 'uncorrected-ber-instantaneous-alarm-high-threshold'), ['int'])),
                            ('uncorrected_ber_instantaneous_alarm_low_threshold', (YLeaf(YType.int64, 'uncorrected-ber-instantaneous-alarm-low-threshold'), ['int'])),
                            ('uncorrected_ber_instantaneous_warn_high_threshold', (YLeaf(YType.int64, 'uncorrected-ber-instantaneous-warn-high-threshold'), ['int'])),
                            ('uncorrected_ber_instantaneous_warn_low_threshold', (YLeaf(YType.int64, 'uncorrected-ber-instantaneous-warn-low-threshold'), ['int'])),
                        ])
                        self.snr_alarm_high_threshold = None
                        self.snr_alarm_low_threshold = None
                        self.snr_warn_high_threshold = None
                        self.snr_warn_low_threshold = None
                        self.isi_correction_alarm_high_threshold = None
                        self.isi_correction_alarm_low_threshold = None
                        self.isi_correction_warn_high_threshold = None
                        self.isi_correction_warn_low_threshold = None
                        self.pam_rate_alarm_high_threshold = None
                        self.pam_rate_alarm_low_threshold = None
                        self.pam_rate_warn_high_threshold = None
                        self.pam_rate_warn_low_threshold = None
                        self.pre_fec_ber_alarm_high_threshold = None
                        self.pre_fec_ber_alarm_low_threshold = None
                        self.pre_fec_ber_warn_high_threshold = None
                        self.pre_fec_ber_warn_low_threshold = None
                        self.uncorrected_ber_alarm_high_threshold = None
                        self.uncorrected_ber_alarm_low_threshold = None
                        self.uncorrected_ber_warn_high_threshold = None
                        self.uncorrected_ber_warn_low_threshold = None
                        self.tec_current_alarm_high_threshold = None
                        self.tec_current_alarm_low_threshold = None
                        self.tec_current_warn_high_threshold = None
                        self.tec_current_warn_low_threshold = None
                        self.laser_diff_frequency_alarm_high_threshold = None
                        self.laser_diff_frequency_alarm_low_threshold = None
                        self.laser_diff_frequency_warn_high_threshold = None
                        self.laser_diff_frequency_warn_low_threshold = None
                        self.laser_diff_temperature_alarm_high_threshold = None
                        self.laser_diff_temperature_alarm_low_threshold = None
                        self.laser_diff_temperature_warn_high_threshold = None
                        self.laser_diff_temperature_warn_low_threshold = None
                        self.pre_fec_ber_latched_min_alarm_high_threshold = None
                        self.pre_fec_ber_latched_min_alarm_low_threshold = None
                        self.pre_fec_ber_latched_min_warn_high_threshold = None
                        self.pre_fec_ber_latched_min_warn_low_threshold = None
                        self.pre_fec_ber_latched_max_alarm_high_threshold = None
                        self.pre_fec_ber_latched_max_alarm_low_threshold = None
                        self.pre_fec_ber_latched_max_warn_high_threshold = None
                        self.pre_fec_ber_latched_max_warn_low_threshold = None
                        self.pre_fec_ber_accumulated_alarm_high_threshold = None
                        self.pre_fec_ber_accumulated_alarm_low_threshold = None
                        self.pre_fec_ber_accumulated_warn_high_threshold = None
                        self.pre_fec_ber_accumulated_warn_low_threshold = None
                        self.pre_fec_ber_instantaneous_alarm_high_threshold = None
                        self.pre_fec_ber_instantaneous_alarm_low_threshold = None
                        self.pre_fec_ber_instantaneous_warn_high_threshold = None
                        self.pre_fec_ber_instantaneous_warn_low_threshold = None
                        self.uncorrected_ber_latched_min_alarm_high_threshold = None
                        self.uncorrected_ber_latched_min_alarm_low_threshold = None
                        self.uncorrected_ber_latched_min_warn_high_threshold = None
                        self.uncorrected_ber_latched_min_warn_low_threshold = None
                        self.uncorrected_ber_latched_max_alarm_high_threshold = None
                        self.uncorrected_ber_latched_max_alarm_low_threshold = None
                        self.uncorrected_ber_latched_max_warn_high_threshold = None
                        self.uncorrected_ber_latched_max_warn_low_threshold = None
                        self.uncorrected_ber_accumulated_alarm_high_threshold = None
                        self.uncorrected_ber_accumulated_alarm_low_threshold = None
                        self.uncorrected_ber_accumulated_warn_high_threshold = None
                        self.uncorrected_ber_accumulated_warn_low_threshold = None
                        self.uncorrected_ber_instantaneous_alarm_high_threshold = None
                        self.uncorrected_ber_instantaneous_alarm_low_threshold = None
                        self.uncorrected_ber_instantaneous_warn_high_threshold = None
                        self.uncorrected_ber_instantaneous_warn_low_threshold = None
                        self._segment_path = lambda: "ext-param-threshold-val"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtParamThresholdVal, ['snr_alarm_high_threshold', 'snr_alarm_low_threshold', 'snr_warn_high_threshold', 'snr_warn_low_threshold', 'isi_correction_alarm_high_threshold', 'isi_correction_alarm_low_threshold', 'isi_correction_warn_high_threshold', 'isi_correction_warn_low_threshold', 'pam_rate_alarm_high_threshold', 'pam_rate_alarm_low_threshold', 'pam_rate_warn_high_threshold', 'pam_rate_warn_low_threshold', 'pre_fec_ber_alarm_high_threshold', 'pre_fec_ber_alarm_low_threshold', 'pre_fec_ber_warn_high_threshold', 'pre_fec_ber_warn_low_threshold', 'uncorrected_ber_alarm_high_threshold', 'uncorrected_ber_alarm_low_threshold', 'uncorrected_ber_warn_high_threshold', 'uncorrected_ber_warn_low_threshold', 'tec_current_alarm_high_threshold', 'tec_current_alarm_low_threshold', 'tec_current_warn_high_threshold', 'tec_current_warn_low_threshold', 'laser_diff_frequency_alarm_high_threshold', 'laser_diff_frequency_alarm_low_threshold', 'laser_diff_frequency_warn_high_threshold', 'laser_diff_frequency_warn_low_threshold', 'laser_diff_temperature_alarm_high_threshold', 'laser_diff_temperature_alarm_low_threshold', 'laser_diff_temperature_warn_high_threshold', 'laser_diff_temperature_warn_low_threshold', 'pre_fec_ber_latched_min_alarm_high_threshold', 'pre_fec_ber_latched_min_alarm_low_threshold', 'pre_fec_ber_latched_min_warn_high_threshold', 'pre_fec_ber_latched_min_warn_low_threshold', 'pre_fec_ber_latched_max_alarm_high_threshold', 'pre_fec_ber_latched_max_alarm_low_threshold', 'pre_fec_ber_latched_max_warn_high_threshold', 'pre_fec_ber_latched_max_warn_low_threshold', 'pre_fec_ber_accumulated_alarm_high_threshold', 'pre_fec_ber_accumulated_alarm_low_threshold', 'pre_fec_ber_accumulated_warn_high_threshold', 'pre_fec_ber_accumulated_warn_low_threshold', 'pre_fec_ber_instantaneous_alarm_high_threshold', 'pre_fec_ber_instantaneous_alarm_low_threshold', 'pre_fec_ber_instantaneous_warn_high_threshold', 'pre_fec_ber_instantaneous_warn_low_threshold', 'uncorrected_ber_latched_min_alarm_high_threshold', 'uncorrected_ber_latched_min_alarm_low_threshold', 'uncorrected_ber_latched_min_warn_high_threshold', 'uncorrected_ber_latched_min_warn_low_threshold', 'uncorrected_ber_latched_max_alarm_high_threshold', 'uncorrected_ber_latched_max_alarm_low_threshold', 'uncorrected_ber_latched_max_warn_high_threshold', 'uncorrected_ber_latched_max_warn_low_threshold', 'uncorrected_ber_accumulated_alarm_high_threshold', 'uncorrected_ber_accumulated_alarm_low_threshold', 'uncorrected_ber_accumulated_warn_high_threshold', 'uncorrected_ber_accumulated_warn_low_threshold', 'uncorrected_ber_instantaneous_alarm_high_threshold', 'uncorrected_ber_instantaneous_alarm_low_threshold', 'uncorrected_ber_instantaneous_warn_high_threshold', 'uncorrected_ber_instantaneous_warn_low_threshold'], name, value)


                class ExtendedAlarmAlarmInfo(Entity):
                    """
                    Extended DOM alarm Information
                    
                    .. attribute:: lo_snr
                    
                    	Low SNR Alarm for Lane1
                    	**type**\:  :py:class:`LoSnr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.LoSnr>`
                    
                    .. attribute:: hi_snr1
                    
                    	High SNR Alarm for Lane1
                    	**type**\:  :py:class:`HiSnr1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiSnr1>`
                    
                    .. attribute:: lo_snr1
                    
                    	Low SNR Alarm for Lane2
                    	**type**\:  :py:class:`LoSnr1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.LoSnr1>`
                    
                    .. attribute:: hi_snr2
                    
                    	High SNR Alarm for Lane2
                    	**type**\:  :py:class:`HiSnr2 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiSnr2>`
                    
                    .. attribute:: lo_isi1
                    
                    	Low ISI Correction Alarm for Lane1
                    	**type**\:  :py:class:`LoIsi1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.LoIsi1>`
                    
                    .. attribute:: hi_isi1
                    
                    	High ISI Correction Alarm for Lane1
                    	**type**\:  :py:class:`HiIsi1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiIsi1>`
                    
                    .. attribute:: lo_isi2
                    
                    	Low ISI Correction Alarm for Lane2
                    	**type**\:  :py:class:`LoIsi2 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.LoIsi2>`
                    
                    .. attribute:: hi_isi2
                    
                    	High ISI Correction Alarm for Lane2
                    	**type**\:  :py:class:`HiIsi2 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiIsi2>`
                    
                    .. attribute:: lo_pam1
                    
                    	Low PAM Rate Alarm for Lane1
                    	**type**\:  :py:class:`LoPam1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.LoPam1>`
                    
                    .. attribute:: hi_pam1
                    
                    	High PAM Rate Alarm for Lane1
                    	**type**\:  :py:class:`HiPam1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiPam1>`
                    
                    .. attribute:: lo_pam2
                    
                    	Low PAM Rate Alarm for Lane2
                    	**type**\:  :py:class:`LoPam2 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.LoPam2>`
                    
                    .. attribute:: hi_pam2
                    
                    	High PAM Rate Alarm for Lane2
                    	**type**\:  :py:class:`HiPam2 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiPam2>`
                    
                    .. attribute:: lo_tec1
                    
                    	Low TEC Current Alarm for Lane1
                    	**type**\:  :py:class:`LoTec1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.LoTec1>`
                    
                    .. attribute:: hi_tec1
                    
                    	High TEC Current Alarm for Lane1
                    	**type**\:  :py:class:`HiTec1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiTec1>`
                    
                    .. attribute:: lo_tec2
                    
                    	Low TEC Current Alarm for Lane2
                    	**type**\:  :py:class:`LoTec2 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.LoTec2>`
                    
                    .. attribute:: hi_tec2
                    
                    	High TEC Current Alarm for Lane2
                    	**type**\:  :py:class:`HiTec2 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiTec2>`
                    
                    .. attribute:: lo_laser_freq1
                    
                    	Low Laser Differential Frequency Alarm for Lane1
                    	**type**\:  :py:class:`LoLaserFreq1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.LoLaserFreq1>`
                    
                    .. attribute:: hi_laser_freq1
                    
                    	High Laser Differential Frequency Alarm for Lane1
                    	**type**\:  :py:class:`HiLaserFreq1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiLaserFreq1>`
                    
                    .. attribute:: lo_laser_freq2
                    
                    	Low Laser Differential Frequency Alarm for Lane2
                    	**type**\:  :py:class:`LoLaserFreq2 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.LoLaserFreq2>`
                    
                    .. attribute:: hi_laser_freq2
                    
                    	High Laser Differential Frequency Alarm for Lane2
                    	**type**\:  :py:class:`HiLaserFreq2 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiLaserFreq2>`
                    
                    .. attribute:: hi_pre_fecber_cur_acc
                    
                    	High Pre FEC BER Current Accumulated Alarm
                    	**type**\:  :py:class:`HiPreFecberCurAcc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiPreFecberCurAcc>`
                    
                    .. attribute:: hi_pre_fecber_min
                    
                    	High Pre FEC BER Min Alarm
                    	**type**\:  :py:class:`HiPreFecberMin <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiPreFecberMin>`
                    
                    .. attribute:: hi_pre_fecber_max
                    
                    	High Pre FEC BER Max Alarm
                    	**type**\:  :py:class:`HiPreFecberMax <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiPreFecberMax>`
                    
                    .. attribute:: hi_pre_fecber_prior_acc
                    
                    	High Pre FEC BER Prior Accumulated Alarm
                    	**type**\:  :py:class:`HiPreFecberPriorAcc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiPreFecberPriorAcc>`
                    
                    .. attribute:: hi_pre_fecber_cur
                    
                    	High Pre FEC BER Current Alarm
                    	**type**\:  :py:class:`HiPreFecberCur <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiPreFecberCur>`
                    
                    .. attribute:: hi_uncorrected_ber_cur_acc
                    
                    	High Uncorrected BER Current Accumulated Alarm
                    	**type**\:  :py:class:`HiUncorrectedBerCurAcc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiUncorrectedBerCurAcc>`
                    
                    .. attribute:: hi_uncorrected_ber_min
                    
                    	High Uncorrected BER Min Alarm
                    	**type**\:  :py:class:`HiUncorrectedBerMin <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiUncorrectedBerMin>`
                    
                    .. attribute:: hi_uncorrected_ber_max
                    
                    	High Uncorrected BER Max Alarm
                    	**type**\:  :py:class:`HiUncorrectedBerMax <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiUncorrectedBerMax>`
                    
                    .. attribute:: hi_uncorrected_ber_prior_acc
                    
                    	High Uncorrected BER Prior Accumulated Alarm
                    	**type**\:  :py:class:`HiUncorrectedBerPriorAcc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiUncorrectedBerPriorAcc>`
                    
                    .. attribute:: hi_uncorrected_ber_cur
                    
                    	High Uncorrected BER Current Alarm
                    	**type**\:  :py:class:`HiUncorrectedBerCur <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiUncorrectedBerCur>`
                    
                    

                    """

                    _prefix = 'controller-optics-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo, self).__init__()

                        self.yang_name = "extended-alarm-alarm-info"
                        self.yang_parent_name = "optics-info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("lo-snr", ("lo_snr", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.LoSnr)), ("hi-snr1", ("hi_snr1", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiSnr1)), ("lo-snr1", ("lo_snr1", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.LoSnr1)), ("hi-snr2", ("hi_snr2", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiSnr2)), ("lo-isi1", ("lo_isi1", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.LoIsi1)), ("hi-isi1", ("hi_isi1", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiIsi1)), ("lo-isi2", ("lo_isi2", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.LoIsi2)), ("hi-isi2", ("hi_isi2", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiIsi2)), ("lo-pam1", ("lo_pam1", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.LoPam1)), ("hi-pam1", ("hi_pam1", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiPam1)), ("lo-pam2", ("lo_pam2", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.LoPam2)), ("hi-pam2", ("hi_pam2", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiPam2)), ("lo-tec1", ("lo_tec1", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.LoTec1)), ("hi-tec1", ("hi_tec1", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiTec1)), ("lo-tec2", ("lo_tec2", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.LoTec2)), ("hi-tec2", ("hi_tec2", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiTec2)), ("lo-laser-freq1", ("lo_laser_freq1", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.LoLaserFreq1)), ("hi-laser-freq1", ("hi_laser_freq1", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiLaserFreq1)), ("lo-laser-freq2", ("lo_laser_freq2", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.LoLaserFreq2)), ("hi-laser-freq2", ("hi_laser_freq2", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiLaserFreq2)), ("hi-pre-fecber-cur-acc", ("hi_pre_fecber_cur_acc", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiPreFecberCurAcc)), ("hi-pre-fecber-min", ("hi_pre_fecber_min", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiPreFecberMin)), ("hi-pre-fecber-max", ("hi_pre_fecber_max", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiPreFecberMax)), ("hi-pre-fecber-prior-acc", ("hi_pre_fecber_prior_acc", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiPreFecberPriorAcc)), ("hi-pre-fecber-cur", ("hi_pre_fecber_cur", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiPreFecberCur)), ("hi-uncorrected-ber-cur-acc", ("hi_uncorrected_ber_cur_acc", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiUncorrectedBerCurAcc)), ("hi-uncorrected-ber-min", ("hi_uncorrected_ber_min", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiUncorrectedBerMin)), ("hi-uncorrected-ber-max", ("hi_uncorrected_ber_max", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiUncorrectedBerMax)), ("hi-uncorrected-ber-prior-acc", ("hi_uncorrected_ber_prior_acc", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiUncorrectedBerPriorAcc)), ("hi-uncorrected-ber-cur", ("hi_uncorrected_ber_cur", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiUncorrectedBerCur))])
                        self._leafs = OrderedDict()

                        self.lo_snr = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.LoSnr()
                        self.lo_snr.parent = self
                        self._children_name_map["lo_snr"] = "lo-snr"

                        self.hi_snr1 = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiSnr1()
                        self.hi_snr1.parent = self
                        self._children_name_map["hi_snr1"] = "hi-snr1"

                        self.lo_snr1 = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.LoSnr1()
                        self.lo_snr1.parent = self
                        self._children_name_map["lo_snr1"] = "lo-snr1"

                        self.hi_snr2 = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiSnr2()
                        self.hi_snr2.parent = self
                        self._children_name_map["hi_snr2"] = "hi-snr2"

                        self.lo_isi1 = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.LoIsi1()
                        self.lo_isi1.parent = self
                        self._children_name_map["lo_isi1"] = "lo-isi1"

                        self.hi_isi1 = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiIsi1()
                        self.hi_isi1.parent = self
                        self._children_name_map["hi_isi1"] = "hi-isi1"

                        self.lo_isi2 = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.LoIsi2()
                        self.lo_isi2.parent = self
                        self._children_name_map["lo_isi2"] = "lo-isi2"

                        self.hi_isi2 = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiIsi2()
                        self.hi_isi2.parent = self
                        self._children_name_map["hi_isi2"] = "hi-isi2"

                        self.lo_pam1 = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.LoPam1()
                        self.lo_pam1.parent = self
                        self._children_name_map["lo_pam1"] = "lo-pam1"

                        self.hi_pam1 = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiPam1()
                        self.hi_pam1.parent = self
                        self._children_name_map["hi_pam1"] = "hi-pam1"

                        self.lo_pam2 = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.LoPam2()
                        self.lo_pam2.parent = self
                        self._children_name_map["lo_pam2"] = "lo-pam2"

                        self.hi_pam2 = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiPam2()
                        self.hi_pam2.parent = self
                        self._children_name_map["hi_pam2"] = "hi-pam2"

                        self.lo_tec1 = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.LoTec1()
                        self.lo_tec1.parent = self
                        self._children_name_map["lo_tec1"] = "lo-tec1"

                        self.hi_tec1 = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiTec1()
                        self.hi_tec1.parent = self
                        self._children_name_map["hi_tec1"] = "hi-tec1"

                        self.lo_tec2 = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.LoTec2()
                        self.lo_tec2.parent = self
                        self._children_name_map["lo_tec2"] = "lo-tec2"

                        self.hi_tec2 = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiTec2()
                        self.hi_tec2.parent = self
                        self._children_name_map["hi_tec2"] = "hi-tec2"

                        self.lo_laser_freq1 = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.LoLaserFreq1()
                        self.lo_laser_freq1.parent = self
                        self._children_name_map["lo_laser_freq1"] = "lo-laser-freq1"

                        self.hi_laser_freq1 = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiLaserFreq1()
                        self.hi_laser_freq1.parent = self
                        self._children_name_map["hi_laser_freq1"] = "hi-laser-freq1"

                        self.lo_laser_freq2 = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.LoLaserFreq2()
                        self.lo_laser_freq2.parent = self
                        self._children_name_map["lo_laser_freq2"] = "lo-laser-freq2"

                        self.hi_laser_freq2 = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiLaserFreq2()
                        self.hi_laser_freq2.parent = self
                        self._children_name_map["hi_laser_freq2"] = "hi-laser-freq2"

                        self.hi_pre_fecber_cur_acc = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiPreFecberCurAcc()
                        self.hi_pre_fecber_cur_acc.parent = self
                        self._children_name_map["hi_pre_fecber_cur_acc"] = "hi-pre-fecber-cur-acc"

                        self.hi_pre_fecber_min = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiPreFecberMin()
                        self.hi_pre_fecber_min.parent = self
                        self._children_name_map["hi_pre_fecber_min"] = "hi-pre-fecber-min"

                        self.hi_pre_fecber_max = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiPreFecberMax()
                        self.hi_pre_fecber_max.parent = self
                        self._children_name_map["hi_pre_fecber_max"] = "hi-pre-fecber-max"

                        self.hi_pre_fecber_prior_acc = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiPreFecberPriorAcc()
                        self.hi_pre_fecber_prior_acc.parent = self
                        self._children_name_map["hi_pre_fecber_prior_acc"] = "hi-pre-fecber-prior-acc"

                        self.hi_pre_fecber_cur = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiPreFecberCur()
                        self.hi_pre_fecber_cur.parent = self
                        self._children_name_map["hi_pre_fecber_cur"] = "hi-pre-fecber-cur"

                        self.hi_uncorrected_ber_cur_acc = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiUncorrectedBerCurAcc()
                        self.hi_uncorrected_ber_cur_acc.parent = self
                        self._children_name_map["hi_uncorrected_ber_cur_acc"] = "hi-uncorrected-ber-cur-acc"

                        self.hi_uncorrected_ber_min = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiUncorrectedBerMin()
                        self.hi_uncorrected_ber_min.parent = self
                        self._children_name_map["hi_uncorrected_ber_min"] = "hi-uncorrected-ber-min"

                        self.hi_uncorrected_ber_max = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiUncorrectedBerMax()
                        self.hi_uncorrected_ber_max.parent = self
                        self._children_name_map["hi_uncorrected_ber_max"] = "hi-uncorrected-ber-max"

                        self.hi_uncorrected_ber_prior_acc = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiUncorrectedBerPriorAcc()
                        self.hi_uncorrected_ber_prior_acc.parent = self
                        self._children_name_map["hi_uncorrected_ber_prior_acc"] = "hi-uncorrected-ber-prior-acc"

                        self.hi_uncorrected_ber_cur = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiUncorrectedBerCur()
                        self.hi_uncorrected_ber_cur.parent = self
                        self._children_name_map["hi_uncorrected_ber_cur"] = "hi-uncorrected-ber-cur"
                        self._segment_path = lambda: "extended-alarm-alarm-info"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo, [], name, value)


                    class LoSnr(Entity):
                        """
                        Low SNR Alarm for Lane1
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.LoSnr, self).__init__()

                            self.yang_name = "lo-snr"
                            self.yang_parent_name = "extended-alarm-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                            ])
                            self.is_detected = None
                            self.counter = None
                            self._segment_path = lambda: "lo-snr"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.LoSnr, ['is_detected', 'counter'], name, value)


                    class HiSnr1(Entity):
                        """
                        High SNR Alarm for Lane1
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiSnr1, self).__init__()

                            self.yang_name = "hi-snr1"
                            self.yang_parent_name = "extended-alarm-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                            ])
                            self.is_detected = None
                            self.counter = None
                            self._segment_path = lambda: "hi-snr1"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiSnr1, ['is_detected', 'counter'], name, value)


                    class LoSnr1(Entity):
                        """
                        Low SNR Alarm for Lane2
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.LoSnr1, self).__init__()

                            self.yang_name = "lo-snr1"
                            self.yang_parent_name = "extended-alarm-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                            ])
                            self.is_detected = None
                            self.counter = None
                            self._segment_path = lambda: "lo-snr1"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.LoSnr1, ['is_detected', 'counter'], name, value)


                    class HiSnr2(Entity):
                        """
                        High SNR Alarm for Lane2
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiSnr2, self).__init__()

                            self.yang_name = "hi-snr2"
                            self.yang_parent_name = "extended-alarm-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                            ])
                            self.is_detected = None
                            self.counter = None
                            self._segment_path = lambda: "hi-snr2"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiSnr2, ['is_detected', 'counter'], name, value)


                    class LoIsi1(Entity):
                        """
                        Low ISI Correction Alarm for Lane1
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.LoIsi1, self).__init__()

                            self.yang_name = "lo-isi1"
                            self.yang_parent_name = "extended-alarm-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                            ])
                            self.is_detected = None
                            self.counter = None
                            self._segment_path = lambda: "lo-isi1"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.LoIsi1, ['is_detected', 'counter'], name, value)


                    class HiIsi1(Entity):
                        """
                        High ISI Correction Alarm for Lane1
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiIsi1, self).__init__()

                            self.yang_name = "hi-isi1"
                            self.yang_parent_name = "extended-alarm-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                            ])
                            self.is_detected = None
                            self.counter = None
                            self._segment_path = lambda: "hi-isi1"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiIsi1, ['is_detected', 'counter'], name, value)


                    class LoIsi2(Entity):
                        """
                        Low ISI Correction Alarm for Lane2
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.LoIsi2, self).__init__()

                            self.yang_name = "lo-isi2"
                            self.yang_parent_name = "extended-alarm-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                            ])
                            self.is_detected = None
                            self.counter = None
                            self._segment_path = lambda: "lo-isi2"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.LoIsi2, ['is_detected', 'counter'], name, value)


                    class HiIsi2(Entity):
                        """
                        High ISI Correction Alarm for Lane2
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiIsi2, self).__init__()

                            self.yang_name = "hi-isi2"
                            self.yang_parent_name = "extended-alarm-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                            ])
                            self.is_detected = None
                            self.counter = None
                            self._segment_path = lambda: "hi-isi2"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiIsi2, ['is_detected', 'counter'], name, value)


                    class LoPam1(Entity):
                        """
                        Low PAM Rate Alarm for Lane1
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.LoPam1, self).__init__()

                            self.yang_name = "lo-pam1"
                            self.yang_parent_name = "extended-alarm-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                            ])
                            self.is_detected = None
                            self.counter = None
                            self._segment_path = lambda: "lo-pam1"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.LoPam1, ['is_detected', 'counter'], name, value)


                    class HiPam1(Entity):
                        """
                        High PAM Rate Alarm for Lane1
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiPam1, self).__init__()

                            self.yang_name = "hi-pam1"
                            self.yang_parent_name = "extended-alarm-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                            ])
                            self.is_detected = None
                            self.counter = None
                            self._segment_path = lambda: "hi-pam1"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiPam1, ['is_detected', 'counter'], name, value)


                    class LoPam2(Entity):
                        """
                        Low PAM Rate Alarm for Lane2
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.LoPam2, self).__init__()

                            self.yang_name = "lo-pam2"
                            self.yang_parent_name = "extended-alarm-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                            ])
                            self.is_detected = None
                            self.counter = None
                            self._segment_path = lambda: "lo-pam2"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.LoPam2, ['is_detected', 'counter'], name, value)


                    class HiPam2(Entity):
                        """
                        High PAM Rate Alarm for Lane2
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiPam2, self).__init__()

                            self.yang_name = "hi-pam2"
                            self.yang_parent_name = "extended-alarm-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                            ])
                            self.is_detected = None
                            self.counter = None
                            self._segment_path = lambda: "hi-pam2"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiPam2, ['is_detected', 'counter'], name, value)


                    class LoTec1(Entity):
                        """
                        Low TEC Current Alarm for Lane1
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.LoTec1, self).__init__()

                            self.yang_name = "lo-tec1"
                            self.yang_parent_name = "extended-alarm-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                            ])
                            self.is_detected = None
                            self.counter = None
                            self._segment_path = lambda: "lo-tec1"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.LoTec1, ['is_detected', 'counter'], name, value)


                    class HiTec1(Entity):
                        """
                        High TEC Current Alarm for Lane1
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiTec1, self).__init__()

                            self.yang_name = "hi-tec1"
                            self.yang_parent_name = "extended-alarm-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                            ])
                            self.is_detected = None
                            self.counter = None
                            self._segment_path = lambda: "hi-tec1"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiTec1, ['is_detected', 'counter'], name, value)


                    class LoTec2(Entity):
                        """
                        Low TEC Current Alarm for Lane2
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.LoTec2, self).__init__()

                            self.yang_name = "lo-tec2"
                            self.yang_parent_name = "extended-alarm-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                            ])
                            self.is_detected = None
                            self.counter = None
                            self._segment_path = lambda: "lo-tec2"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.LoTec2, ['is_detected', 'counter'], name, value)


                    class HiTec2(Entity):
                        """
                        High TEC Current Alarm for Lane2
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiTec2, self).__init__()

                            self.yang_name = "hi-tec2"
                            self.yang_parent_name = "extended-alarm-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                            ])
                            self.is_detected = None
                            self.counter = None
                            self._segment_path = lambda: "hi-tec2"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiTec2, ['is_detected', 'counter'], name, value)


                    class LoLaserFreq1(Entity):
                        """
                        Low Laser Differential Frequency Alarm for Lane1
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.LoLaserFreq1, self).__init__()

                            self.yang_name = "lo-laser-freq1"
                            self.yang_parent_name = "extended-alarm-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                            ])
                            self.is_detected = None
                            self.counter = None
                            self._segment_path = lambda: "lo-laser-freq1"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.LoLaserFreq1, ['is_detected', 'counter'], name, value)


                    class HiLaserFreq1(Entity):
                        """
                        High Laser Differential Frequency Alarm for
                        Lane1
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiLaserFreq1, self).__init__()

                            self.yang_name = "hi-laser-freq1"
                            self.yang_parent_name = "extended-alarm-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                            ])
                            self.is_detected = None
                            self.counter = None
                            self._segment_path = lambda: "hi-laser-freq1"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiLaserFreq1, ['is_detected', 'counter'], name, value)


                    class LoLaserFreq2(Entity):
                        """
                        Low Laser Differential Frequency Alarm for Lane2
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.LoLaserFreq2, self).__init__()

                            self.yang_name = "lo-laser-freq2"
                            self.yang_parent_name = "extended-alarm-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                            ])
                            self.is_detected = None
                            self.counter = None
                            self._segment_path = lambda: "lo-laser-freq2"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.LoLaserFreq2, ['is_detected', 'counter'], name, value)


                    class HiLaserFreq2(Entity):
                        """
                        High Laser Differential Frequency Alarm for
                        Lane2
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiLaserFreq2, self).__init__()

                            self.yang_name = "hi-laser-freq2"
                            self.yang_parent_name = "extended-alarm-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                            ])
                            self.is_detected = None
                            self.counter = None
                            self._segment_path = lambda: "hi-laser-freq2"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiLaserFreq2, ['is_detected', 'counter'], name, value)


                    class HiPreFecberCurAcc(Entity):
                        """
                        High Pre FEC BER Current Accumulated Alarm
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiPreFecberCurAcc, self).__init__()

                            self.yang_name = "hi-pre-fecber-cur-acc"
                            self.yang_parent_name = "extended-alarm-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                            ])
                            self.is_detected = None
                            self.counter = None
                            self._segment_path = lambda: "hi-pre-fecber-cur-acc"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiPreFecberCurAcc, ['is_detected', 'counter'], name, value)


                    class HiPreFecberMin(Entity):
                        """
                        High Pre FEC BER Min Alarm
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiPreFecberMin, self).__init__()

                            self.yang_name = "hi-pre-fecber-min"
                            self.yang_parent_name = "extended-alarm-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                            ])
                            self.is_detected = None
                            self.counter = None
                            self._segment_path = lambda: "hi-pre-fecber-min"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiPreFecberMin, ['is_detected', 'counter'], name, value)


                    class HiPreFecberMax(Entity):
                        """
                        High Pre FEC BER Max Alarm
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiPreFecberMax, self).__init__()

                            self.yang_name = "hi-pre-fecber-max"
                            self.yang_parent_name = "extended-alarm-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                            ])
                            self.is_detected = None
                            self.counter = None
                            self._segment_path = lambda: "hi-pre-fecber-max"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiPreFecberMax, ['is_detected', 'counter'], name, value)


                    class HiPreFecberPriorAcc(Entity):
                        """
                        High Pre FEC BER Prior Accumulated Alarm
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiPreFecberPriorAcc, self).__init__()

                            self.yang_name = "hi-pre-fecber-prior-acc"
                            self.yang_parent_name = "extended-alarm-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                            ])
                            self.is_detected = None
                            self.counter = None
                            self._segment_path = lambda: "hi-pre-fecber-prior-acc"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiPreFecberPriorAcc, ['is_detected', 'counter'], name, value)


                    class HiPreFecberCur(Entity):
                        """
                        High Pre FEC BER Current Alarm
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiPreFecberCur, self).__init__()

                            self.yang_name = "hi-pre-fecber-cur"
                            self.yang_parent_name = "extended-alarm-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                            ])
                            self.is_detected = None
                            self.counter = None
                            self._segment_path = lambda: "hi-pre-fecber-cur"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiPreFecberCur, ['is_detected', 'counter'], name, value)


                    class HiUncorrectedBerCurAcc(Entity):
                        """
                        High Uncorrected BER Current Accumulated Alarm
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiUncorrectedBerCurAcc, self).__init__()

                            self.yang_name = "hi-uncorrected-ber-cur-acc"
                            self.yang_parent_name = "extended-alarm-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                            ])
                            self.is_detected = None
                            self.counter = None
                            self._segment_path = lambda: "hi-uncorrected-ber-cur-acc"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiUncorrectedBerCurAcc, ['is_detected', 'counter'], name, value)


                    class HiUncorrectedBerMin(Entity):
                        """
                        High Uncorrected BER Min Alarm
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiUncorrectedBerMin, self).__init__()

                            self.yang_name = "hi-uncorrected-ber-min"
                            self.yang_parent_name = "extended-alarm-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                            ])
                            self.is_detected = None
                            self.counter = None
                            self._segment_path = lambda: "hi-uncorrected-ber-min"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiUncorrectedBerMin, ['is_detected', 'counter'], name, value)


                    class HiUncorrectedBerMax(Entity):
                        """
                        High Uncorrected BER Max Alarm
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiUncorrectedBerMax, self).__init__()

                            self.yang_name = "hi-uncorrected-ber-max"
                            self.yang_parent_name = "extended-alarm-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                            ])
                            self.is_detected = None
                            self.counter = None
                            self._segment_path = lambda: "hi-uncorrected-ber-max"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiUncorrectedBerMax, ['is_detected', 'counter'], name, value)


                    class HiUncorrectedBerPriorAcc(Entity):
                        """
                        High Uncorrected BER Prior Accumulated Alarm
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiUncorrectedBerPriorAcc, self).__init__()

                            self.yang_name = "hi-uncorrected-ber-prior-acc"
                            self.yang_parent_name = "extended-alarm-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                            ])
                            self.is_detected = None
                            self.counter = None
                            self._segment_path = lambda: "hi-uncorrected-ber-prior-acc"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiUncorrectedBerPriorAcc, ['is_detected', 'counter'], name, value)


                    class HiUncorrectedBerCur(Entity):
                        """
                        High Uncorrected BER Current Alarm
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiUncorrectedBerCur, self).__init__()

                            self.yang_name = "hi-uncorrected-ber-cur"
                            self.yang_parent_name = "extended-alarm-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                            ])
                            self.is_detected = None
                            self.counter = None
                            self._segment_path = lambda: "hi-uncorrected-ber-cur"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtendedAlarmAlarmInfo.HiUncorrectedBerCur, ['is_detected', 'counter'], name, value)


                class AinsInfo(Entity):
                    """
                    AINS information
                    
                    .. attribute:: ains_state
                    
                    	AINS State
                    	**type**\:  :py:class:`OpticsAinsStateEt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsAinsStateEt>`
                    
                    .. attribute:: ains_timer_minutes
                    
                    	AINS Timer in Minutes
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: minute
                    
                    .. attribute:: ains_remaining_secs
                    
                    	AINS Remaining Seconds
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    

                    """

                    _prefix = 'controller-optics-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.AinsInfo, self).__init__()

                        self.yang_name = "ains-info"
                        self.yang_parent_name = "optics-info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('ains_state', (YLeaf(YType.enumeration, 'ains-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsAinsStateEt', '')])),
                            ('ains_timer_minutes', (YLeaf(YType.uint32, 'ains-timer-minutes'), ['int'])),
                            ('ains_remaining_secs', (YLeaf(YType.uint32, 'ains-remaining-secs'), ['int'])),
                        ])
                        self.ains_state = None
                        self.ains_timer_minutes = None
                        self.ains_remaining_secs = None
                        self._segment_path = lambda: "ains-info"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.AinsInfo, ['ains_state', 'ains_timer_minutes', 'ains_remaining_secs'], name, value)


                class LaneData(Entity):
                    """
                    Lane information
                    
                    .. attribute:: lane_alarm_info
                    
                    	Lane Alarm Information
                    	**type**\:  :py:class:`LaneAlarmInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo>`
                    
                    .. attribute:: lane_index
                    
                    	The index number of the lane
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: laser_bias_current_percent
                    
                    	Laser Bias Current in units of 0.01 percentage
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: percentage
                    
                    .. attribute:: laser_bias_current_milli_amps
                    
                    	Laser Bias Current in units of 0.01mA
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: transmit_power
                    
                    	Transmit power in the units of 0.01dBm
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: receive_power
                    
                    	Transponder receive power in the units of 0 .01dBm
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: receive_signal_power
                    
                    	Transponder receive signal power in the units of 0.01dBm
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: transmit_signal_power
                    
                    	Transmit Signal power in the units of 0.01dBm
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: output_frequency
                    
                    	Output frequency read from hw in the units of 100MHz
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: frequency_offset
                    
                    	Frequency Offset read from hw in units of MHz
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    

                    """

                    _prefix = 'controller-optics-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData, self).__init__()

                        self.yang_name = "lane-data"
                        self.yang_parent_name = "optics-info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("lane-alarm-info", ("lane_alarm_info", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo))])
                        self._leafs = OrderedDict([
                            ('lane_index', (YLeaf(YType.uint32, 'lane-index'), ['int'])),
                            ('laser_bias_current_percent', (YLeaf(YType.uint32, 'laser-bias-current-percent'), ['int'])),
                            ('laser_bias_current_milli_amps', (YLeaf(YType.uint32, 'laser-bias-current-milli-amps'), ['int'])),
                            ('transmit_power', (YLeaf(YType.int32, 'transmit-power'), ['int'])),
                            ('receive_power', (YLeaf(YType.int32, 'receive-power'), ['int'])),
                            ('receive_signal_power', (YLeaf(YType.int32, 'receive-signal-power'), ['int'])),
                            ('transmit_signal_power', (YLeaf(YType.int32, 'transmit-signal-power'), ['int'])),
                            ('output_frequency', (YLeaf(YType.int32, 'output-frequency'), ['int'])),
                            ('frequency_offset', (YLeaf(YType.int32, 'frequency-offset'), ['int'])),
                        ])
                        self.lane_index = None
                        self.laser_bias_current_percent = None
                        self.laser_bias_current_milli_amps = None
                        self.transmit_power = None
                        self.receive_power = None
                        self.receive_signal_power = None
                        self.transmit_signal_power = None
                        self.output_frequency = None
                        self.frequency_offset = None

                        self.lane_alarm_info = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo()
                        self.lane_alarm_info.parent = self
                        self._children_name_map["lane_alarm_info"] = "lane-alarm-info"
                        self._segment_path = lambda: "lane-data"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData, ['lane_index', 'laser_bias_current_percent', 'laser_bias_current_milli_amps', 'transmit_power', 'receive_power', 'receive_signal_power', 'transmit_signal_power', 'output_frequency', 'frequency_offset'], name, value)


                    class LaneAlarmInfo(Entity):
                        """
                        Lane Alarm Information
                        
                        .. attribute:: high_rx_power
                        
                        	High Rx Power
                        	**type**\:  :py:class:`HighRxPower <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.HighRxPower>`
                        
                        .. attribute:: low_rx_power
                        
                        	Low Rx Power
                        	**type**\:  :py:class:`LowRxPower <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.LowRxPower>`
                        
                        .. attribute:: high_tx_power
                        
                        	High Tx Power
                        	**type**\:  :py:class:`HighTxPower <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.HighTxPower>`
                        
                        .. attribute:: low_tx_power
                        
                        	Low Tx Power
                        	**type**\:  :py:class:`LowTxPower <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.LowTxPower>`
                        
                        .. attribute:: high_lbc
                        
                        	High laser bias current
                        	**type**\:  :py:class:`HighLbc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.HighLbc>`
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo, self).__init__()

                            self.yang_name = "lane-alarm-info"
                            self.yang_parent_name = "lane-data"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("high-rx-power", ("high_rx_power", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.HighRxPower)), ("low-rx-power", ("low_rx_power", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.LowRxPower)), ("high-tx-power", ("high_tx_power", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.HighTxPower)), ("low-tx-power", ("low_tx_power", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.LowTxPower)), ("high-lbc", ("high_lbc", OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.HighLbc))])
                            self._leafs = OrderedDict()

                            self.high_rx_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.HighRxPower()
                            self.high_rx_power.parent = self
                            self._children_name_map["high_rx_power"] = "high-rx-power"

                            self.low_rx_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.LowRxPower()
                            self.low_rx_power.parent = self
                            self._children_name_map["low_rx_power"] = "low-rx-power"

                            self.high_tx_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.HighTxPower()
                            self.high_tx_power.parent = self
                            self._children_name_map["high_tx_power"] = "high-tx-power"

                            self.low_tx_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.LowTxPower()
                            self.low_tx_power.parent = self
                            self._children_name_map["low_tx_power"] = "low-tx-power"

                            self.high_lbc = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.HighLbc()
                            self.high_lbc.parent = self
                            self._children_name_map["high_lbc"] = "high-lbc"
                            self._segment_path = lambda: "lane-alarm-info"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo, [], name, value)


                        class HighRxPower(Entity):
                            """
                            High Rx Power
                            
                            .. attribute:: is_detected
                            
                            	Is defect detected?
                            	**type**\: bool
                            
                            .. attribute:: counter
                            
                            	Alarm counter
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'controller-optics-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.HighRxPower, self).__init__()

                                self.yang_name = "high-rx-power"
                                self.yang_parent_name = "lane-alarm-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                    ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                                ])
                                self.is_detected = None
                                self.counter = None
                                self._segment_path = lambda: "high-rx-power"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.HighRxPower, ['is_detected', 'counter'], name, value)


                        class LowRxPower(Entity):
                            """
                            Low Rx Power
                            
                            .. attribute:: is_detected
                            
                            	Is defect detected?
                            	**type**\: bool
                            
                            .. attribute:: counter
                            
                            	Alarm counter
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'controller-optics-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.LowRxPower, self).__init__()

                                self.yang_name = "low-rx-power"
                                self.yang_parent_name = "lane-alarm-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                    ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                                ])
                                self.is_detected = None
                                self.counter = None
                                self._segment_path = lambda: "low-rx-power"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.LowRxPower, ['is_detected', 'counter'], name, value)


                        class HighTxPower(Entity):
                            """
                            High Tx Power
                            
                            .. attribute:: is_detected
                            
                            	Is defect detected?
                            	**type**\: bool
                            
                            .. attribute:: counter
                            
                            	Alarm counter
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'controller-optics-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.HighTxPower, self).__init__()

                                self.yang_name = "high-tx-power"
                                self.yang_parent_name = "lane-alarm-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                    ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                                ])
                                self.is_detected = None
                                self.counter = None
                                self._segment_path = lambda: "high-tx-power"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.HighTxPower, ['is_detected', 'counter'], name, value)


                        class LowTxPower(Entity):
                            """
                            Low Tx Power
                            
                            .. attribute:: is_detected
                            
                            	Is defect detected?
                            	**type**\: bool
                            
                            .. attribute:: counter
                            
                            	Alarm counter
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'controller-optics-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.LowTxPower, self).__init__()

                                self.yang_name = "low-tx-power"
                                self.yang_parent_name = "lane-alarm-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                    ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                                ])
                                self.is_detected = None
                                self.counter = None
                                self._segment_path = lambda: "low-tx-power"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.LowTxPower, ['is_detected', 'counter'], name, value)


                        class HighLbc(Entity):
                            """
                            High laser bias current
                            
                            .. attribute:: is_detected
                            
                            	Is defect detected?
                            	**type**\: bool
                            
                            .. attribute:: counter
                            
                            	Alarm counter
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'controller-optics-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.HighLbc, self).__init__()

                                self.yang_name = "high-lbc"
                                self.yang_parent_name = "lane-alarm-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                    ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                                ])
                                self.is_detected = None
                                self.counter = None
                                self._segment_path = lambda: "high-lbc"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.HighLbc, ['is_detected', 'counter'], name, value)


            class OpticsLanes(Entity):
                """
                All Optics Port operational data
                
                .. attribute:: optics_lane
                
                	Lane Information
                	**type**\: list of  		 :py:class:`OpticsLane <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane>`
                
                

                """

                _prefix = 'controller-optics-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(OpticsOper.OpticsPorts.OpticsPort.OpticsLanes, self).__init__()

                    self.yang_name = "optics-lanes"
                    self.yang_parent_name = "optics-port"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("optics-lane", ("optics_lane", OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane))])
                    self._leafs = OrderedDict()

                    self.optics_lane = YList(self)
                    self._segment_path = lambda: "optics-lanes"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsLanes, [], name, value)


                class OpticsLane(Entity):
                    """
                    Lane Information
                    
                    .. attribute:: number  (key)
                    
                    	Lane Index
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: lane_alarm_info
                    
                    	Lane Alarm Information
                    	**type**\:  :py:class:`LaneAlarmInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo>`
                    
                    .. attribute:: lane_index
                    
                    	The index number of the lane
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: laser_bias_current_percent
                    
                    	Laser Bias Current in units of 0.01 percentage
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: percentage
                    
                    .. attribute:: laser_bias_current_milli_amps
                    
                    	Laser Bias Current in units of 0.01mA
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: transmit_power
                    
                    	Transmit power in the units of 0.01dBm
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: receive_power
                    
                    	Transponder receive power in the units of 0 .01dBm
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: receive_signal_power
                    
                    	Transponder receive signal power in the units of 0.01dBm
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: transmit_signal_power
                    
                    	Transmit Signal power in the units of 0.01dBm
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: output_frequency
                    
                    	Output frequency read from hw in the units of 100MHz
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: frequency_offset
                    
                    	Frequency Offset read from hw in units of MHz
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    

                    """

                    _prefix = 'controller-optics-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane, self).__init__()

                        self.yang_name = "optics-lane"
                        self.yang_parent_name = "optics-lanes"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['number']
                        self._child_classes = OrderedDict([("lane-alarm-info", ("lane_alarm_info", OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo))])
                        self._leafs = OrderedDict([
                            ('number', (YLeaf(YType.uint32, 'number'), ['int'])),
                            ('lane_index', (YLeaf(YType.uint32, 'lane-index'), ['int'])),
                            ('laser_bias_current_percent', (YLeaf(YType.uint32, 'laser-bias-current-percent'), ['int'])),
                            ('laser_bias_current_milli_amps', (YLeaf(YType.uint32, 'laser-bias-current-milli-amps'), ['int'])),
                            ('transmit_power', (YLeaf(YType.int32, 'transmit-power'), ['int'])),
                            ('receive_power', (YLeaf(YType.int32, 'receive-power'), ['int'])),
                            ('receive_signal_power', (YLeaf(YType.int32, 'receive-signal-power'), ['int'])),
                            ('transmit_signal_power', (YLeaf(YType.int32, 'transmit-signal-power'), ['int'])),
                            ('output_frequency', (YLeaf(YType.int32, 'output-frequency'), ['int'])),
                            ('frequency_offset', (YLeaf(YType.int32, 'frequency-offset'), ['int'])),
                        ])
                        self.number = None
                        self.lane_index = None
                        self.laser_bias_current_percent = None
                        self.laser_bias_current_milli_amps = None
                        self.transmit_power = None
                        self.receive_power = None
                        self.receive_signal_power = None
                        self.transmit_signal_power = None
                        self.output_frequency = None
                        self.frequency_offset = None

                        self.lane_alarm_info = OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo()
                        self.lane_alarm_info.parent = self
                        self._children_name_map["lane_alarm_info"] = "lane-alarm-info"
                        self._segment_path = lambda: "optics-lane" + "[number='" + str(self.number) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane, ['number', 'lane_index', 'laser_bias_current_percent', 'laser_bias_current_milli_amps', 'transmit_power', 'receive_power', 'receive_signal_power', 'transmit_signal_power', 'output_frequency', 'frequency_offset'], name, value)


                    class LaneAlarmInfo(Entity):
                        """
                        Lane Alarm Information
                        
                        .. attribute:: high_rx_power
                        
                        	High Rx Power
                        	**type**\:  :py:class:`HighRxPower <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.HighRxPower>`
                        
                        .. attribute:: low_rx_power
                        
                        	Low Rx Power
                        	**type**\:  :py:class:`LowRxPower <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.LowRxPower>`
                        
                        .. attribute:: high_tx_power
                        
                        	High Tx Power
                        	**type**\:  :py:class:`HighTxPower <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.HighTxPower>`
                        
                        .. attribute:: low_tx_power
                        
                        	Low Tx Power
                        	**type**\:  :py:class:`LowTxPower <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.LowTxPower>`
                        
                        .. attribute:: high_lbc
                        
                        	High laser bias current
                        	**type**\:  :py:class:`HighLbc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.HighLbc>`
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo, self).__init__()

                            self.yang_name = "lane-alarm-info"
                            self.yang_parent_name = "optics-lane"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("high-rx-power", ("high_rx_power", OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.HighRxPower)), ("low-rx-power", ("low_rx_power", OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.LowRxPower)), ("high-tx-power", ("high_tx_power", OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.HighTxPower)), ("low-tx-power", ("low_tx_power", OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.LowTxPower)), ("high-lbc", ("high_lbc", OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.HighLbc))])
                            self._leafs = OrderedDict()

                            self.high_rx_power = OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.HighRxPower()
                            self.high_rx_power.parent = self
                            self._children_name_map["high_rx_power"] = "high-rx-power"

                            self.low_rx_power = OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.LowRxPower()
                            self.low_rx_power.parent = self
                            self._children_name_map["low_rx_power"] = "low-rx-power"

                            self.high_tx_power = OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.HighTxPower()
                            self.high_tx_power.parent = self
                            self._children_name_map["high_tx_power"] = "high-tx-power"

                            self.low_tx_power = OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.LowTxPower()
                            self.low_tx_power.parent = self
                            self._children_name_map["low_tx_power"] = "low-tx-power"

                            self.high_lbc = OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.HighLbc()
                            self.high_lbc.parent = self
                            self._children_name_map["high_lbc"] = "high-lbc"
                            self._segment_path = lambda: "lane-alarm-info"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo, [], name, value)


                        class HighRxPower(Entity):
                            """
                            High Rx Power
                            
                            .. attribute:: is_detected
                            
                            	Is defect detected?
                            	**type**\: bool
                            
                            .. attribute:: counter
                            
                            	Alarm counter
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'controller-optics-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.HighRxPower, self).__init__()

                                self.yang_name = "high-rx-power"
                                self.yang_parent_name = "lane-alarm-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                    ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                                ])
                                self.is_detected = None
                                self.counter = None
                                self._segment_path = lambda: "high-rx-power"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.HighRxPower, ['is_detected', 'counter'], name, value)


                        class LowRxPower(Entity):
                            """
                            Low Rx Power
                            
                            .. attribute:: is_detected
                            
                            	Is defect detected?
                            	**type**\: bool
                            
                            .. attribute:: counter
                            
                            	Alarm counter
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'controller-optics-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.LowRxPower, self).__init__()

                                self.yang_name = "low-rx-power"
                                self.yang_parent_name = "lane-alarm-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                    ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                                ])
                                self.is_detected = None
                                self.counter = None
                                self._segment_path = lambda: "low-rx-power"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.LowRxPower, ['is_detected', 'counter'], name, value)


                        class HighTxPower(Entity):
                            """
                            High Tx Power
                            
                            .. attribute:: is_detected
                            
                            	Is defect detected?
                            	**type**\: bool
                            
                            .. attribute:: counter
                            
                            	Alarm counter
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'controller-optics-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.HighTxPower, self).__init__()

                                self.yang_name = "high-tx-power"
                                self.yang_parent_name = "lane-alarm-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                    ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                                ])
                                self.is_detected = None
                                self.counter = None
                                self._segment_path = lambda: "high-tx-power"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.HighTxPower, ['is_detected', 'counter'], name, value)


                        class LowTxPower(Entity):
                            """
                            Low Tx Power
                            
                            .. attribute:: is_detected
                            
                            	Is defect detected?
                            	**type**\: bool
                            
                            .. attribute:: counter
                            
                            	Alarm counter
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'controller-optics-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.LowTxPower, self).__init__()

                                self.yang_name = "low-tx-power"
                                self.yang_parent_name = "lane-alarm-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                    ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                                ])
                                self.is_detected = None
                                self.counter = None
                                self._segment_path = lambda: "low-tx-power"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.LowTxPower, ['is_detected', 'counter'], name, value)


                        class HighLbc(Entity):
                            """
                            High laser bias current
                            
                            .. attribute:: is_detected
                            
                            	Is defect detected?
                            	**type**\: bool
                            
                            .. attribute:: counter
                            
                            	Alarm counter
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'controller-optics-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.HighLbc, self).__init__()

                                self.yang_name = "high-lbc"
                                self.yang_parent_name = "lane-alarm-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                    ('counter', (YLeaf(YType.uint32, 'counter'), ['int'])),
                                ])
                                self.is_detected = None
                                self.counter = None
                                self._segment_path = lambda: "high-lbc"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.HighLbc, ['is_detected', 'counter'], name, value)


            class OpticsDbInfo(Entity):
                """
                Optics operational data
                
                .. attribute:: network_srlg_info
                
                	Network SRLG information
                	**type**\:  :py:class:`NetworkSrlgInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsDbInfo.NetworkSrlgInfo>`
                
                .. attribute:: transport_admin_state
                
                	Transport Admin State
                	**type**\:  :py:class:`OpticsTas <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsTas>`
                
                .. attribute:: controller_state
                
                	Optics controller state\: Up, Down or Administratively Down
                	**type**\:  :py:class:`OpticsControllerState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsControllerState>`
                
                

                """

                _prefix = 'controller-optics-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(OpticsOper.OpticsPorts.OpticsPort.OpticsDbInfo, self).__init__()

                    self.yang_name = "optics-db-info"
                    self.yang_parent_name = "optics-port"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("network-srlg-info", ("network_srlg_info", OpticsOper.OpticsPorts.OpticsPort.OpticsDbInfo.NetworkSrlgInfo))])
                    self._leafs = OrderedDict([
                        ('transport_admin_state', (YLeaf(YType.enumeration, 'transport-admin-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsTas', '')])),
                        ('controller_state', (YLeaf(YType.enumeration, 'controller-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsControllerState', '')])),
                    ])
                    self.transport_admin_state = None
                    self.controller_state = None

                    self.network_srlg_info = OpticsOper.OpticsPorts.OpticsPort.OpticsDbInfo.NetworkSrlgInfo()
                    self.network_srlg_info.parent = self
                    self._children_name_map["network_srlg_info"] = "network-srlg-info"
                    self._segment_path = lambda: "optics-db-info"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsDbInfo, ['transport_admin_state', 'controller_state'], name, value)


                class NetworkSrlgInfo(Entity):
                    """
                    Network SRLG information
                    
                    .. attribute:: network_srlg_array
                    
                    	Network Srlg Array
                    	**type**\: list of  		 :py:class:`NetworkSrlgArray <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsDbInfo.NetworkSrlgInfo.NetworkSrlgArray>`
                    
                    

                    """

                    _prefix = 'controller-optics-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(OpticsOper.OpticsPorts.OpticsPort.OpticsDbInfo.NetworkSrlgInfo, self).__init__()

                        self.yang_name = "network-srlg-info"
                        self.yang_parent_name = "optics-db-info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("network-srlg-array", ("network_srlg_array", OpticsOper.OpticsPorts.OpticsPort.OpticsDbInfo.NetworkSrlgInfo.NetworkSrlgArray))])
                        self._leafs = OrderedDict()

                        self.network_srlg_array = YList(self)
                        self._segment_path = lambda: "network-srlg-info"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsDbInfo.NetworkSrlgInfo, [], name, value)


                    class NetworkSrlgArray(Entity):
                        """
                        Network Srlg Array
                        
                        .. attribute:: set_number
                        
                        	Array to maintain set number
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: network_srlg
                        
                        	Network Srlg
                        	**type**\: list of int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(OpticsOper.OpticsPorts.OpticsPort.OpticsDbInfo.NetworkSrlgInfo.NetworkSrlgArray, self).__init__()

                            self.yang_name = "network-srlg-array"
                            self.yang_parent_name = "network-srlg-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('set_number', (YLeaf(YType.uint32, 'set-number'), ['int'])),
                                ('network_srlg', (YLeafList(YType.uint32, 'network-srlg'), ['int'])),
                            ])
                            self.set_number = None
                            self.network_srlg = []
                            self._segment_path = lambda: "network-srlg-array"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticsOper.OpticsPorts.OpticsPort.OpticsDbInfo.NetworkSrlgInfo.NetworkSrlgArray, ['set_number', 'network_srlg'], name, value)

    def clone_ptr(self):
        self._top_entity = OpticsOper()
        return self._top_entity

