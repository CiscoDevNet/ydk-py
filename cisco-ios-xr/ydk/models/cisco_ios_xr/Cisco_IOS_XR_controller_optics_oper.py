""" Cisco_IOS_XR_controller_optics_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR controller\-optics package operational data.

This module contains definitions
for the following management objects\:
  optics\-oper\: Optics operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class EthernetPmdEnum(Enum):
    """
    EthernetPmdEnum

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

    optics_eth_not_set = 0

    optics_eth_10gbase_lrm = 1

    optics_eth_10gbase_lr = 2

    optics_eth_10gbase_zr = 3

    optics_eth_10gbase_er = 4

    optics_eth_10gbase_sr = 5

    optics_eth_10gbase = 6

    optics_eth_40gbase_cr4 = 7

    optics_eth_40gbase_sr4 = 8

    optics_eth_40gbase_lr4 = 9

    optics_eth_40gbase_er4 = 10

    optics_eth_40gbase_psm4 = 11

    optics_eth_40gbase_csr4 = 12

    optics_eth_40gbase_sr_bd = 13

    optics_eth_40g_aoc = 14

    optics_eth_4x10gbase_lr = 15

    optics_eth_4x10gbase_sr = 16

    optics_eth_100g_aoc = 17

    optics_eth_100g_acc = 18

    optics_eth_100gbase_sr10 = 19

    optics_eth_100gbase_sr4 = 20

    optics_eth_100gbase_lr4 = 21

    optics_eth_100gbase_er4 = 22

    optics_eth_100gbase_cwdm4 = 23

    optics_eth_100gbase_clr4 = 24

    optics_eth_100gbase_psm4 = 25

    optics_eth_100gbase_cr4 = 26

    optics_eth_100gbase_al = 27

    optics_eth_100gbase_pl = 28

    optics_eth_undefined = 29


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
        return meta._meta_table['EthernetPmdEnum']


class FiberConnectorEnum(Enum):
    """
    FiberConnectorEnum

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

    optics_connect_or_not_set = 0

    optics_sc_connect_or = 1

    optics_lc_connect_or = 2

    optics_mpo_connect_or = 3

    optics_undefined_connect_or = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
        return meta._meta_table['FiberConnectorEnum']


class OpticsAmplifierControlModeEnum(Enum):
    """
    OpticsAmplifierControlModeEnum

    Optics amplifier control mode

    .. data:: automatic = 1

    	Automatic

    .. data:: manual = 2

    	Manual

    """

    automatic = 1

    manual = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
        return meta._meta_table['OpticsAmplifierControlModeEnum']


class OpticsAmplifierGainRangeEnum(Enum):
    """
    OpticsAmplifierGainRangeEnum

    Optics amplifier gain range

    .. data:: optics_amplifier_gain_range_normal = 1

    	Normal

    .. data:: optics_amplifier_gain_range_ext_end_ed = 2

    	Extended

    """

    optics_amplifier_gain_range_normal = 1

    optics_amplifier_gain_range_ext_end_ed = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
        return meta._meta_table['OpticsAmplifierGainRangeEnum']


class OpticsAmplifierSafetyControlModeEnum(Enum):
    """
    OpticsAmplifierSafetyControlModeEnum

    Optics amplifier safety control mode

    .. data:: optics_amplifier_safety_mode_auto = 1

    	auto

    .. data:: optics_amplifier_safety_mode_disabled = 2

    	disabled

    """

    optics_amplifier_safety_mode_auto = 1

    optics_amplifier_safety_mode_disabled = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
        return meta._meta_table['OpticsAmplifierSafetyControlModeEnum']


class OpticsControllerStateEnum(Enum):
    """
    OpticsControllerStateEnum

    Optics controller state

    .. data:: optics_state_up = 0

    	Up

    .. data:: optics_state_down = 1

    	Down

    .. data:: optics_state_admin_down = 2

    	Administratively Down

    """

    optics_state_up = 0

    optics_state_down = 1

    optics_state_admin_down = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
        return meta._meta_table['OpticsControllerStateEnum']


class OpticsEnum(Enum):
    """
    OpticsEnum

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

    optics_unknown = 0

    optics_grey = 1

    optics_dwdm = 2

    optics_cwdm = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
        return meta._meta_table['OpticsEnum']


class OpticsFecEnum(Enum):
    """
    OpticsFecEnum

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

    fec_none = 0

    fec_hg15 = 1

    fec_hg25 = 2

    fec_hg15_de = 4

    fec_hg25_de = 8

    fec_enabled = 16


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
        return meta._meta_table['OpticsFecEnum']


class OpticsFormFactorEnum(Enum):
    """
    OpticsFormFactorEnum

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

    not_set = 0

    invalid = 1

    cpak = 2

    cxp = 3

    sfp_plus = 4

    qsfp = 5

    qsfp_plus = 6

    qsfp28 = 7

    sfp = 8

    cfp = 9

    cfp2 = 10

    cfp4 = 11

    xfp = 12

    x2 = 13

    non_pluggable = 14

    other = 15


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
        return meta._meta_table['OpticsFormFactorEnum']


class OpticsLaserStateEnum(Enum):
    """
    OpticsLaserStateEnum

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

    on = 0

    off = 1

    unknown = 2

    apr = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
        return meta._meta_table['OpticsLaserStateEnum']


class OpticsLedStateEnum(Enum):
    """
    OpticsLedStateEnum

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

    off = 0

    green_on = 1

    green_flashing = 2

    yellow_on = 3

    yellow_flashing = 4

    red_on = 5

    red_flashing = 6


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
        return meta._meta_table['OpticsLedStateEnum']


class OpticsPhyEnum(Enum):
    """
    OpticsPhyEnum

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

    .. data:: trunk_port_cfp2 = 48

    	CFP2 DWDM Optics

    .. data:: short_reach1_lane = 49

    	Short reach 1 lane

    .. data:: inmd_reach1lane = 50

    	Inmd reach 1 lane

    .. data:: long_reach1_lane = 51

    	Long reach 1 lane

    """

    not_set = 0

    invalid = 1

    long_reach_four_lanes = 2

    short_reach_ten_lanes = 3

    short_reach_one_lane = 4

    long_reach_one_lane = 5

    short_reach_four_lanes = 6

    copper_four_lanes = 7

    active_optical_cable = 8

    fourty_gig_e_long_reach_four_lanes = 9

    fourty_gig_e_short_reach_four_lanes = 10

    cwdm_four_lanes = 11

    extended_reach_four_lanes = 12

    psm_four_lanes = 13

    active_copper_cable = 14

    fourty_gig_e_extended_reach_four_lanes = 15

    four_x_ten_gig_e_short_reach_one_lane = 16

    fourty_gig_epsm_four_lanes = 17

    fourty_gig_e_copper_four_lanes = 18

    long_reach_mm_one_lane = 19

    copper_short_reach = 20

    short_reach_srbd = 21

    copper_one_lane = 22

    four_x_ten_gig_e_long_reach_one_lane = 23

    fourty_gig_eaoc_four_lanes = 24

    extended_one_lane = 25

    zr_one_lane = 26

    dwdm_one_lane = 27

    sx_one_lane = 28

    lx_one_lane = 29

    ex_one_lane = 30

    zx_one_lane = 31

    ba_set_one_lane = 32

    aoc_one_lane = 33

    active_copper_one_lane = 34

    fourty_gig_eacu_four_lanes = 35

    four_x_ten_gig_eacu_one_lanes = 36

    four_x_ten_gig_ecu_one_lanes = 37

    four_x_ten_gig_eaoc_one_lanes = 38

    twenty_five_gig_short_reach_one_lane = 39

    twenty_five_gig_long_reach_one_lane = 40

    twenty_five_gig_extended_reach_one_lane = 41

    twenty_five_gig_copper_one_lane = 42

    twenty_five_gig_active_optical_one_lane = 43

    hundred_gig_edwdm_two = 44

    fourty_gig_plr4_four_lanes = 45

    fourty_gig_esr4_four_lanes = 46

    smsr_four_lanes = 47

    trunk_port_cfp2 = 48

    short_reach1_lane = 49

    inmd_reach1lane = 50

    long_reach1_lane = 51


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
        return meta._meta_table['OpticsPhyEnum']


class OpticsPortEnum(Enum):
    """
    OpticsPortEnum

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

    com = 0

    line = 1

    osc = 2

    com_check = 3

    work = 4

    prot = 5


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
        return meta._meta_table['OpticsPortEnum']


class OpticsPortStatusEnum(Enum):
    """
    OpticsPortStatusEnum

    Optics port status

    .. data:: active = 0

    	Active

    .. data:: standby = 1

    	Standby

    """

    active = 0

    standby = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
        return meta._meta_table['OpticsPortStatusEnum']


class OpticsTasEnum(Enum):
    """
    OpticsTasEnum

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

    tas_ui_oos = 0

    tas_ui_main = 1

    tas_ui_is = 2

    tas_ui_ains = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
        return meta._meta_table['OpticsTasEnum']


class OpticsWaveBandEnum(Enum):
    """
    OpticsWaveBandEnum

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

    c_band = 0

    l_band = 1

    c_band_odd = 2

    c_band_even = 3

    invalid_band = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
        return meta._meta_table['OpticsWaveBandEnum']


class OtnApplicationCodeEnum(Enum):
    """
    OtnApplicationCodeEnum

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

    optics_not_set = 0

    optics_p1l1_2d1 = 1

    optics_p1s1_2d2 = 2

    optics_p1l1_2d2 = 3

    optics_undefined = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
        return meta._meta_table['OtnApplicationCodeEnum']


class SonetApplicationCodeEnum(Enum):
    """
    SonetApplicationCodeEnum

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

    optics_sonet_not_set = 0

    optics_vsr2000_3r2 = 1

    optics_vsr2000_3r3 = 2

    optics_vsr2000_3r5 = 3

    optics_sonet_undefined = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
        return meta._meta_table['SonetApplicationCodeEnum']



class OpticsOper(object):
    """
    Optics operational data
    
    .. attribute:: optics_ports
    
    	All Optics Port operational data
    	**type**\:   :py:class:`OpticsPorts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts>`
    
    

    """

    _prefix = 'controller-optics-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.optics_ports = OpticsOper.OpticsPorts()
        self.optics_ports.parent = self


    class OpticsPorts(object):
        """
        All Optics Port operational data
        
        .. attribute:: optics_port
        
        	Optics operational data
        	**type**\: list of    :py:class:`OpticsPort <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort>`
        
        

        """

        _prefix = 'controller-optics-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.optics_port = YList()
            self.optics_port.parent = self
            self.optics_port.name = 'optics_port'


        class OpticsPort(object):
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
                self.parent = None
                self.name = None
                self.optics_db_info = OpticsOper.OpticsPorts.OpticsPort.OpticsDbInfo()
                self.optics_db_info.parent = self
                self.optics_dwdm_carrrier_channel_map = OpticsOper.OpticsPorts.OpticsPort.OpticsDwdmCarrrierChannelMap()
                self.optics_dwdm_carrrier_channel_map.parent = self
                self.optics_info = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo()
                self.optics_info.parent = self
                self.optics_lanes = OpticsOper.OpticsPorts.OpticsPort.OpticsLanes()
                self.optics_lanes.parent = self


            class OpticsDwdmCarrrierChannelMap(object):
                """
                Optics operational data
                
                .. attribute:: dwdm_carrier_band
                
                	DWDM carrier band
                	**type**\:   :py:class:`OpticsWaveBandEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsWaveBandEnum>`
                
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
                    self.parent = None
                    self.dwdm_carrier_band = None
                    self.dwdm_carrier_map_info = YList()
                    self.dwdm_carrier_map_info.parent = self
                    self.dwdm_carrier_map_info.name = 'dwdm_carrier_map_info'
                    self.dwdm_carrier_max = None
                    self.dwdm_carrier_min = None


                class DwdmCarrierMapInfo(object):
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
                        self.parent = None
                        self.frequency = None
                        self.g694_chan_num = None
                        self.itu_chan_num = None
                        self.wavelength = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:dwdm-carrier-map-info'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.frequency is not None:
                            return True

                        if self.g694_chan_num is not None:
                            return True

                        if self.itu_chan_num is not None:
                            return True

                        if self.wavelength is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                        return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsDwdmCarrrierChannelMap.DwdmCarrierMapInfo']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:optics-dwdm-carrrier-channel-map'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.dwdm_carrier_band is not None:
                        return True

                    if self.dwdm_carrier_map_info is not None:
                        for child_ref in self.dwdm_carrier_map_info:
                            if child_ref._has_data():
                                return True

                    if self.dwdm_carrier_max is not None:
                        return True

                    if self.dwdm_carrier_min is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                    return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsDwdmCarrrierChannelMap']['meta_info']


            class OpticsInfo(object):
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
                	**type**\:   :py:class:`OpticsAmplifierControlModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsAmplifierControlModeEnum>`
                
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
                	**type**\:   :py:class:`OpticsAmplifierGainRangeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsAmplifierGainRangeEnum>`
                
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
                
                	Configured Tx power value in 0.01 dB
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
                	**type**\:   :py:class:`OpticsControllerStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsControllerStateEnum>`
                
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
                	**type**\:   :py:class:`OpticsWaveBandEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsWaveBandEnum>`
                
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
                	**type**\:   :py:class:`OpticsFormFactorEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsFormFactorEnum>`
                
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
                	**type**\:   :py:class:`OpticsLaserStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsLaserStateEnum>`
                
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
                	**type**\:   :py:class:`OpticsLedStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsLedStateEnum>`
                
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
                	**type**\:   :py:class:`OpticsFecEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsFecEnum>`
                
                .. attribute:: optics_module
                
                	Optics module name
                	**type**\:  str
                
                .. attribute:: optics_present
                
                	Is Optics Present?
                	**type**\:  bool
                
                .. attribute:: optics_type
                
                	Optics type name
                	**type**\:   :py:class:`OpticsEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsEnum>`
                
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
                	**type**\:   :py:class:`OpticsPhyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsPhyEnum>`
                
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
                	**type**\:   :py:class:`OpticsPortStatusEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsPortStatusEnum>`
                
                .. attribute:: port_type
                
                	Showing port type
                	**type**\:   :py:class:`OpticsPortEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsPortEnum>`
                
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
                
                .. attribute:: rx_power
                
                	Receive Power in 0.01 dB
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
                	**type**\:   :py:class:`OpticsAmplifierSafetyControlModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsAmplifierSafetyControlModeEnum>`
                
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
                	**type**\:   :py:class:`OpticsTasEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsTasEnum>`
                
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
                
                .. attribute:: tx_power
                
                	Transmit Power in 0.01 dB
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
                    self.parent = None
                    self.alarm_detected = None
                    self.ampli_channel_power_config_val = None
                    self.ampli_control_mode_config_val = None
                    self.ampli_gain = None
                    self.ampli_gain_config_val = None
                    self.ampli_gain_range_config_val = None
                    self.ampli_gain_thr_deg_high_config_val = None
                    self.ampli_gain_thr_deg_low_config_val = None
                    self.ampli_tilt = None
                    self.ampli_tilt_config_val = None
                    self.cd = None
                    self.cd_configurable = None
                    self.cd_high_threshold = None
                    self.cd_low_threshold = None
                    self.cd_max = None
                    self.cd_min = None
                    self.cfg_tx_power = None
                    self.cfg_tx_power_configurable = None
                    self.channel_power_max_delta_config_val = None
                    self.controller_state = None
                    self.dgd_high_threshold = None
                    self.differential_group_delay = None
                    self.display_volt_temp = None
                    self.dwdm_carrier_band = None
                    self.dwdm_carrier_channel = None
                    self.dwdm_carrier_frequency = None
                    self.dwdm_carrier_wavelength = None
                    self.ext_param_threshold_val = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtParamThresholdVal()
                    self.ext_param_threshold_val.parent = self
                    self.ext_param_val = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtParamVal()
                    self.ext_param_val.parent = self
                    self.form_factor = None
                    self.grey_wavelength = None
                    self.is_bo_configured = None
                    self.is_ext_param_valid = None
                    self.lane_data = YList()
                    self.lane_data.parent = self
                    self.lane_data.name = 'lane_data'
                    self.laser_state = None
                    self.lbc_high_threshold = None
                    self.lbc_th_high_default = None
                    self.lbc_th_high_warning_default = None
                    self.lbc_th_low_default = None
                    self.lbc_th_low_warning_default = None
                    self.led_state = None
                    self.network_srlg_info = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.NetworkSrlgInfo()
                    self.network_srlg_info.parent = self
                    self.optical_signal_to_noise_ratio = None
                    self.optics_alarm_info = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo()
                    self.optics_alarm_info.parent = self
                    self.optics_fec = None
                    self.optics_module = None
                    self.optics_present = None
                    self.optics_type = None
                    self.osnr_low_threshold = None
                    self.osri_config_val = None
                    self.ots_alarm_info = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo()
                    self.ots_alarm_info.parent = self
                    self.phase_noise = None
                    self.phy_type = None
                    self.pm_enable = None
                    self.polarization_change_rate = None
                    self.polarization_dependent_loss = None
                    self.polarization_mode_dispersion = None
                    self.port_status = None
                    self.port_type = None
                    self.rx_high_threshold = None
                    self.rx_high_warning_threshold = None
                    self.rx_low_threshold = None
                    self.rx_low_warning_threshold = None
                    self.rx_power = None
                    self.rx_power_th_configurable = None
                    self.rx_voa_attenuation = None
                    self.rx_voa_attenuation_config_val = None
                    self.safety_control_mode_config_val = None
                    self.second_order_polarization_mode_dispersion = None
                    self.temp_high_threshold = None
                    self.temp_high_warning_threshold = None
                    self.temp_low_threshold = None
                    self.temp_low_warning_threshold = None
                    self.temperature = None
                    self.total_rx_power = None
                    self.total_tx_power = None
                    self.transceiver_info = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.TransceiverInfo()
                    self.transceiver_info.parent = self
                    self.transport_admin_state = None
                    self.tx_high_threshold = None
                    self.tx_high_warning_threshold = None
                    self.tx_low_threshold = None
                    self.tx_low_warning_threshold = None
                    self.tx_power = None
                    self.tx_power_th_configurable = None
                    self.tx_voa_attenuation = None
                    self.tx_voa_attenuation_config_val = None
                    self.volt_high_threshold = None
                    self.volt_high_warning_threshold = None
                    self.volt_low_threshold = None
                    self.volt_low_warning_threshold = None
                    self.voltage = None


                class NetworkSrlgInfo(object):
                    """
                    Network SRLG information
                    
                    .. attribute:: network_srlg_array
                    
                    	Network Srlg Array
                    	**type**\: list of    :py:class:`NetworkSrlgArray <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.NetworkSrlgInfo.NetworkSrlgArray>`
                    
                    

                    """

                    _prefix = 'controller-optics-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.network_srlg_array = YList()
                        self.network_srlg_array.parent = self
                        self.network_srlg_array.name = 'network_srlg_array'


                    class NetworkSrlgArray(object):
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
                            self.parent = None
                            self.network_srlg = YLeafList()
                            self.network_srlg.parent = self
                            self.network_srlg.name = 'network_srlg'
                            self.set_number = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:network-srlg-array'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.network_srlg is not None:
                                for child in self.network_srlg:
                                    if child is not None:
                                        return True

                            if self.set_number is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.NetworkSrlgInfo.NetworkSrlgArray']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:network-srlg-info'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.network_srlg_array is not None:
                            for child_ref in self.network_srlg_array:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                        return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.NetworkSrlgInfo']['meta_info']


                class OpticsAlarmInfo(object):
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
                    
                    .. attribute:: wvlool
                    
                    	WVL OOL
                    	**type**\:   :py:class:`Wvlool <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Wvlool>`
                    
                    

                    """

                    _prefix = 'controller-optics-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.amp_gain_deg_high = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.AmpGainDegHigh()
                        self.amp_gain_deg_high.parent = self
                        self.amp_gain_deg_low = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.AmpGainDegLow()
                        self.amp_gain_deg_low.parent = self
                        self.hidgd = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Hidgd()
                        self.hidgd.parent = self
                        self.high_lbc = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighLbc()
                        self.high_lbc.parent = self
                        self.high_rx1_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx1Power()
                        self.high_rx1_power.parent = self
                        self.high_rx2_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx2Power()
                        self.high_rx2_power.parent = self
                        self.high_rx3_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx3Power()
                        self.high_rx3_power.parent = self
                        self.high_rx4_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx4Power()
                        self.high_rx4_power.parent = self
                        self.high_rx_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRxPower()
                        self.high_rx_power.parent = self
                        self.high_tx1_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx1Power()
                        self.high_tx1_power.parent = self
                        self.high_tx1lbc = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx1Lbc()
                        self.high_tx1lbc.parent = self
                        self.high_tx2_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx2Power()
                        self.high_tx2_power.parent = self
                        self.high_tx2lbc = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx2Lbc()
                        self.high_tx2lbc.parent = self
                        self.high_tx3_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx3Power()
                        self.high_tx3_power.parent = self
                        self.high_tx3lbc = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx3Lbc()
                        self.high_tx3lbc.parent = self
                        self.high_tx4_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx4Power()
                        self.high_tx4_power.parent = self
                        self.high_tx4lbc = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx4Lbc()
                        self.high_tx4lbc.parent = self
                        self.high_tx_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTxPower()
                        self.high_tx_power.parent = self
                        self.imp_removal = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.ImpRemoval()
                        self.imp_removal.parent = self
                        self.low_rx1_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx1Power()
                        self.low_rx1_power.parent = self
                        self.low_rx2_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx2Power()
                        self.low_rx2_power.parent = self
                        self.low_rx3_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx3Power()
                        self.low_rx3_power.parent = self
                        self.low_rx4_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx4Power()
                        self.low_rx4_power.parent = self
                        self.low_rx_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRxPower()
                        self.low_rx_power.parent = self
                        self.low_tx1_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx1Power()
                        self.low_tx1_power.parent = self
                        self.low_tx1lbc = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx1Lbc()
                        self.low_tx1lbc.parent = self
                        self.low_tx2_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx2Power()
                        self.low_tx2_power.parent = self
                        self.low_tx2lbc = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx2Lbc()
                        self.low_tx2lbc.parent = self
                        self.low_tx3_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx3Power()
                        self.low_tx3_power.parent = self
                        self.low_tx3lbc = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx3Lbc()
                        self.low_tx3lbc.parent = self
                        self.low_tx4_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx4Power()
                        self.low_tx4_power.parent = self
                        self.low_tx4lbc = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx4Lbc()
                        self.low_tx4lbc.parent = self
                        self.low_tx_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTxPower()
                        self.low_tx_power.parent = self
                        self.mea = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Mea()
                        self.mea.parent = self
                        self.oorcd = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Oorcd()
                        self.oorcd.parent = self
                        self.osnr = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Osnr()
                        self.osnr.parent = self
                        self.rx_loc = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.RxLoc()
                        self.rx_loc.parent = self
                        self.rx_lol = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.RxLol()
                        self.rx_lol.parent = self
                        self.rx_los = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.RxLos()
                        self.rx_los.parent = self
                        self.tx_fault = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxFault()
                        self.tx_fault.parent = self
                        self.tx_lol = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxLol()
                        self.tx_lol.parent = self
                        self.tx_los = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxLos()
                        self.tx_los.parent = self
                        self.wvlool = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Wvlool()
                        self.wvlool.parent = self


                    class HighRxPower(object):
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
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:high-rx-power'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRxPower']['meta_info']


                    class LowRxPower(object):
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
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:low-rx-power'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRxPower']['meta_info']


                    class HighTxPower(object):
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
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:high-tx-power'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTxPower']['meta_info']


                    class LowTxPower(object):
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
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:low-tx-power'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTxPower']['meta_info']


                    class HighLbc(object):
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
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:high-lbc'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighLbc']['meta_info']


                    class HighRx1Power(object):
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
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:high-rx1-power'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx1Power']['meta_info']


                    class HighRx2Power(object):
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
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:high-rx2-power'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx2Power']['meta_info']


                    class HighRx3Power(object):
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
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:high-rx3-power'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx3Power']['meta_info']


                    class HighRx4Power(object):
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
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:high-rx4-power'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx4Power']['meta_info']


                    class LowRx1Power(object):
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
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:low-rx1-power'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx1Power']['meta_info']


                    class LowRx2Power(object):
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
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:low-rx2-power'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx2Power']['meta_info']


                    class LowRx3Power(object):
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
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:low-rx3-power'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx3Power']['meta_info']


                    class LowRx4Power(object):
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
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:low-rx4-power'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx4Power']['meta_info']


                    class HighTx1Power(object):
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
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:high-tx1-power'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx1Power']['meta_info']


                    class HighTx2Power(object):
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
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:high-tx2-power'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx2Power']['meta_info']


                    class HighTx3Power(object):
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
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:high-tx3-power'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx3Power']['meta_info']


                    class HighTx4Power(object):
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
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:high-tx4-power'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx4Power']['meta_info']


                    class LowTx1Power(object):
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
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:low-tx1-power'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx1Power']['meta_info']


                    class LowTx2Power(object):
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
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:low-tx2-power'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx2Power']['meta_info']


                    class LowTx3Power(object):
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
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:low-tx3-power'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx3Power']['meta_info']


                    class LowTx4Power(object):
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
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:low-tx4-power'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx4Power']['meta_info']


                    class HighTx1Lbc(object):
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
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:high-tx1lbc'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx1Lbc']['meta_info']


                    class HighTx2Lbc(object):
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
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:high-tx2lbc'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx2Lbc']['meta_info']


                    class HighTx3Lbc(object):
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
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:high-tx3lbc'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx3Lbc']['meta_info']


                    class HighTx4Lbc(object):
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
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:high-tx4lbc'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx4Lbc']['meta_info']


                    class LowTx1Lbc(object):
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
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:low-tx1lbc'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx1Lbc']['meta_info']


                    class LowTx2Lbc(object):
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
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:low-tx2lbc'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx2Lbc']['meta_info']


                    class LowTx3Lbc(object):
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
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:low-tx3lbc'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx3Lbc']['meta_info']


                    class LowTx4Lbc(object):
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
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:low-tx4lbc'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx4Lbc']['meta_info']


                    class RxLos(object):
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
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:rx-los'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.RxLos']['meta_info']


                    class TxLos(object):
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
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:tx-los'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxLos']['meta_info']


                    class RxLol(object):
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
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:rx-lol'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.RxLol']['meta_info']


                    class TxLol(object):
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
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:tx-lol'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxLol']['meta_info']


                    class TxFault(object):
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
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:tx-fault'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxFault']['meta_info']


                    class Hidgd(object):
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
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:hidgd'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Hidgd']['meta_info']


                    class Oorcd(object):
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
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:oorcd'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Oorcd']['meta_info']


                    class Osnr(object):
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
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:osnr'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Osnr']['meta_info']


                    class Wvlool(object):
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
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:wvlool'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Wvlool']['meta_info']


                    class Mea(object):
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
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:mea'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Mea']['meta_info']


                    class ImpRemoval(object):
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
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:imp-removal'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.ImpRemoval']['meta_info']


                    class RxLoc(object):
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
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:rx-loc'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.RxLoc']['meta_info']


                    class AmpGainDegLow(object):
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
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:amp-gain-deg-low'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.AmpGainDegLow']['meta_info']


                    class AmpGainDegHigh(object):
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
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:amp-gain-deg-high'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.AmpGainDegHigh']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:optics-alarm-info'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.amp_gain_deg_high is not None and self.amp_gain_deg_high._has_data():
                            return True

                        if self.amp_gain_deg_low is not None and self.amp_gain_deg_low._has_data():
                            return True

                        if self.hidgd is not None and self.hidgd._has_data():
                            return True

                        if self.high_lbc is not None and self.high_lbc._has_data():
                            return True

                        if self.high_rx1_power is not None and self.high_rx1_power._has_data():
                            return True

                        if self.high_rx2_power is not None and self.high_rx2_power._has_data():
                            return True

                        if self.high_rx3_power is not None and self.high_rx3_power._has_data():
                            return True

                        if self.high_rx4_power is not None and self.high_rx4_power._has_data():
                            return True

                        if self.high_rx_power is not None and self.high_rx_power._has_data():
                            return True

                        if self.high_tx1_power is not None and self.high_tx1_power._has_data():
                            return True

                        if self.high_tx1lbc is not None and self.high_tx1lbc._has_data():
                            return True

                        if self.high_tx2_power is not None and self.high_tx2_power._has_data():
                            return True

                        if self.high_tx2lbc is not None and self.high_tx2lbc._has_data():
                            return True

                        if self.high_tx3_power is not None and self.high_tx3_power._has_data():
                            return True

                        if self.high_tx3lbc is not None and self.high_tx3lbc._has_data():
                            return True

                        if self.high_tx4_power is not None and self.high_tx4_power._has_data():
                            return True

                        if self.high_tx4lbc is not None and self.high_tx4lbc._has_data():
                            return True

                        if self.high_tx_power is not None and self.high_tx_power._has_data():
                            return True

                        if self.imp_removal is not None and self.imp_removal._has_data():
                            return True

                        if self.low_rx1_power is not None and self.low_rx1_power._has_data():
                            return True

                        if self.low_rx2_power is not None and self.low_rx2_power._has_data():
                            return True

                        if self.low_rx3_power is not None and self.low_rx3_power._has_data():
                            return True

                        if self.low_rx4_power is not None and self.low_rx4_power._has_data():
                            return True

                        if self.low_rx_power is not None and self.low_rx_power._has_data():
                            return True

                        if self.low_tx1_power is not None and self.low_tx1_power._has_data():
                            return True

                        if self.low_tx1lbc is not None and self.low_tx1lbc._has_data():
                            return True

                        if self.low_tx2_power is not None and self.low_tx2_power._has_data():
                            return True

                        if self.low_tx2lbc is not None and self.low_tx2lbc._has_data():
                            return True

                        if self.low_tx3_power is not None and self.low_tx3_power._has_data():
                            return True

                        if self.low_tx3lbc is not None and self.low_tx3lbc._has_data():
                            return True

                        if self.low_tx4_power is not None and self.low_tx4_power._has_data():
                            return True

                        if self.low_tx4lbc is not None and self.low_tx4lbc._has_data():
                            return True

                        if self.low_tx_power is not None and self.low_tx_power._has_data():
                            return True

                        if self.mea is not None and self.mea._has_data():
                            return True

                        if self.oorcd is not None and self.oorcd._has_data():
                            return True

                        if self.osnr is not None and self.osnr._has_data():
                            return True

                        if self.rx_loc is not None and self.rx_loc._has_data():
                            return True

                        if self.rx_lol is not None and self.rx_lol._has_data():
                            return True

                        if self.rx_los is not None and self.rx_los._has_data():
                            return True

                        if self.tx_fault is not None and self.tx_fault._has_data():
                            return True

                        if self.tx_lol is not None and self.tx_lol._has_data():
                            return True

                        if self.tx_los is not None and self.tx_los._has_data():
                            return True

                        if self.wvlool is not None and self.wvlool._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                        return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo']['meta_info']


                class OtsAlarmInfo(object):
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
                        self.parent = None
                        self.amp_gain_deg_high = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AmpGainDegHigh()
                        self.amp_gain_deg_high.parent = self
                        self.amp_gain_deg_low = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AmpGainDegLow()
                        self.amp_gain_deg_low.parent = self
                        self.auto_ampli_ctrl_config_mismatch = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AutoAmpliCtrlConfigMismatch()
                        self.auto_ampli_ctrl_config_mismatch.parent = self
                        self.auto_ampli_ctrl_disabled = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AutoAmpliCtrlDisabled()
                        self.auto_ampli_ctrl_disabled.parent = self
                        self.auto_laser_shut = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AutoLaserShut()
                        self.auto_laser_shut.parent = self
                        self.auto_power_red = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AutoPowerRed()
                        self.auto_power_red.parent = self
                        self.low_rx_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.LowRxPower()
                        self.low_rx_power.parent = self
                        self.low_tx_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.LowTxPower()
                        self.low_tx_power.parent = self
                        self.rx_loc = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.RxLoc()
                        self.rx_loc.parent = self
                        self.rx_los_p = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.RxLosP()
                        self.rx_los_p.parent = self
                        self.switch_to_protect = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.SwitchToProtect()
                        self.switch_to_protect.parent = self


                    class LowTxPower(object):
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
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:low-tx-power'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.LowTxPower']['meta_info']


                    class LowRxPower(object):
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
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:low-rx-power'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.LowRxPower']['meta_info']


                    class RxLosP(object):
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
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:rx-los-p'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.RxLosP']['meta_info']


                    class RxLoc(object):
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
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:rx-loc'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.RxLoc']['meta_info']


                    class AmpGainDegLow(object):
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
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:amp-gain-deg-low'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AmpGainDegLow']['meta_info']


                    class AmpGainDegHigh(object):
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
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:amp-gain-deg-high'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AmpGainDegHigh']['meta_info']


                    class AutoLaserShut(object):
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
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:auto-laser-shut'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AutoLaserShut']['meta_info']


                    class AutoPowerRed(object):
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
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:auto-power-red'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AutoPowerRed']['meta_info']


                    class AutoAmpliCtrlDisabled(object):
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
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:auto-ampli-ctrl-disabled'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AutoAmpliCtrlDisabled']['meta_info']


                    class AutoAmpliCtrlConfigMismatch(object):
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
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:auto-ampli-ctrl-config-mismatch'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AutoAmpliCtrlConfigMismatch']['meta_info']


                    class SwitchToProtect(object):
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
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:switch-to-protect'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.SwitchToProtect']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:ots-alarm-info'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.amp_gain_deg_high is not None and self.amp_gain_deg_high._has_data():
                            return True

                        if self.amp_gain_deg_low is not None and self.amp_gain_deg_low._has_data():
                            return True

                        if self.auto_ampli_ctrl_config_mismatch is not None and self.auto_ampli_ctrl_config_mismatch._has_data():
                            return True

                        if self.auto_ampli_ctrl_disabled is not None and self.auto_ampli_ctrl_disabled._has_data():
                            return True

                        if self.auto_laser_shut is not None and self.auto_laser_shut._has_data():
                            return True

                        if self.auto_power_red is not None and self.auto_power_red._has_data():
                            return True

                        if self.low_rx_power is not None and self.low_rx_power._has_data():
                            return True

                        if self.low_tx_power is not None and self.low_tx_power._has_data():
                            return True

                        if self.rx_loc is not None and self.rx_loc._has_data():
                            return True

                        if self.rx_los_p is not None and self.rx_los_p._has_data():
                            return True

                        if self.switch_to_protect is not None and self.switch_to_protect._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                        return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo']['meta_info']


                class TransceiverInfo(object):
                    """
                    Transceiver Vendor Details
                    
                    .. attribute:: connector_type
                    
                    	Connector type
                    	**type**\:   :py:class:`FiberConnectorEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.FiberConnectorEnum>`
                    
                    .. attribute:: date
                    
                    	Date in Transceiver
                    	**type**\:  str
                    
                    .. attribute:: ethernet_compliance_code
                    
                    	Ethernet Compliance Code
                    	**type**\:   :py:class:`EthernetPmdEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.EthernetPmdEnum>`
                    
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
                    	**type**\:   :py:class:`OtnApplicationCodeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OtnApplicationCodeEnum>`
                    
                    .. attribute:: sonet_application_code
                    
                    	Sonet Application Code
                    	**type**\:   :py:class:`SonetApplicationCodeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.SonetApplicationCodeEnum>`
                    
                    .. attribute:: vendor_info
                    
                    	Vendor Information
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'controller-optics-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.connector_type = None
                        self.date = None
                        self.ethernet_compliance_code = None
                        self.internal_temperature = None
                        self.optics_serial_no = None
                        self.optics_vendor_part = None
                        self.optics_vendor_rev = None
                        self.otn_application_code = None
                        self.sonet_application_code = None
                        self.vendor_info = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:transceiver-info'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.connector_type is not None:
                            return True

                        if self.date is not None:
                            return True

                        if self.ethernet_compliance_code is not None:
                            return True

                        if self.internal_temperature is not None:
                            return True

                        if self.optics_serial_no is not None:
                            return True

                        if self.optics_vendor_part is not None:
                            return True

                        if self.optics_vendor_rev is not None:
                            return True

                        if self.otn_application_code is not None:
                            return True

                        if self.sonet_application_code is not None:
                            return True

                        if self.vendor_info is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                        return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.TransceiverInfo']['meta_info']


                class ExtParamVal(object):
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
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: pre_fec_ber_accumulated
                    
                    	Pre FEC BER value prior accumulation period, line ingress
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: pre_fec_ber_instantaneous
                    
                    	Pre FEC BER value instantaneous line ingress
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: pre_fec_ber_latched_max
                    
                    	Latched maximum Pre FEC BER value since last read, line ingress
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: pre_fec_ber_latched_min
                    
                    	Latched minimum Pre FEC BER value since last read, line ingress
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
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
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: uncorrected_ber_accumulated
                    
                    	Uncorrected BER value prior accumulation period, line ingress
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: uncorrected_ber_instantaneous
                    
                    	Uncorrected BER value instantaneous line line ingress
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: uncorrected_ber_latched_max
                    
                    	Latched maximum Uncorrected BER value since last read, line ingress
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: uncorrected_ber_latched_min
                    
                    	Latched minimum Uncorrected BER value since last read, line ingress
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    

                    """

                    _prefix = 'controller-optics-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.isi_correction_lane1 = None
                        self.isi_correction_lane2 = None
                        self.laser_diff_frequency_lane1 = None
                        self.laser_diff_frequency_lane2 = None
                        self.laser_diff_temperature_lane1 = None
                        self.laser_diff_temperature_lane2 = None
                        self.pam_rate_lane1 = None
                        self.pam_rate_lane2 = None
                        self.pre_fec_ber = None
                        self.pre_fec_ber_accumulated = None
                        self.pre_fec_ber_instantaneous = None
                        self.pre_fec_ber_latched_max = None
                        self.pre_fec_ber_latched_min = None
                        self.snr_lane1 = None
                        self.snr_lane2 = None
                        self.tec_current_lane1 = None
                        self.tec_current_lane2 = None
                        self.uncorrected_ber = None
                        self.uncorrected_ber_accumulated = None
                        self.uncorrected_ber_instantaneous = None
                        self.uncorrected_ber_latched_max = None
                        self.uncorrected_ber_latched_min = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:ext-param-val'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.isi_correction_lane1 is not None:
                            return True

                        if self.isi_correction_lane2 is not None:
                            return True

                        if self.laser_diff_frequency_lane1 is not None:
                            return True

                        if self.laser_diff_frequency_lane2 is not None:
                            return True

                        if self.laser_diff_temperature_lane1 is not None:
                            return True

                        if self.laser_diff_temperature_lane2 is not None:
                            return True

                        if self.pam_rate_lane1 is not None:
                            return True

                        if self.pam_rate_lane2 is not None:
                            return True

                        if self.pre_fec_ber is not None:
                            return True

                        if self.pre_fec_ber_accumulated is not None:
                            return True

                        if self.pre_fec_ber_instantaneous is not None:
                            return True

                        if self.pre_fec_ber_latched_max is not None:
                            return True

                        if self.pre_fec_ber_latched_min is not None:
                            return True

                        if self.snr_lane1 is not None:
                            return True

                        if self.snr_lane2 is not None:
                            return True

                        if self.tec_current_lane1 is not None:
                            return True

                        if self.tec_current_lane2 is not None:
                            return True

                        if self.uncorrected_ber is not None:
                            return True

                        if self.uncorrected_ber_accumulated is not None:
                            return True

                        if self.uncorrected_ber_instantaneous is not None:
                            return True

                        if self.uncorrected_ber_latched_max is not None:
                            return True

                        if self.uncorrected_ber_latched_min is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                        return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtParamVal']['meta_info']


                class ExtParamThresholdVal(object):
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
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: pre_fec_ber_accumulated_alarm_low_threshold
                    
                    	Low threshold alarm for Accumulated Pre FEC BER
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: pre_fec_ber_accumulated_warn_high_threshold
                    
                    	High threshold warning for Accumulated Pre FEC BER
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: pre_fec_ber_accumulated_warn_low_threshold
                    
                    	Low threshold warning for Accumulated Pre FEC BER
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: pre_fec_ber_alarm_high_threshold
                    
                    	High threshold alarm for Pre FEC BER
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: pre_fec_ber_alarm_low_threshold
                    
                    	Low threshold alarm for Pre FEC BER
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: pre_fec_ber_instantaneous_alarm_high_threshold
                    
                    	High threshold alarm for Instantaneous Pre FEC BER
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: pre_fec_ber_instantaneous_alarm_low_threshold
                    
                    	Low threshold alarm for Instantaneous Pre FEC BER
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: pre_fec_ber_instantaneous_warn_high_threshold
                    
                    	High threshold warning for Instantaneous Pre FEC BER
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: pre_fec_ber_instantaneous_warn_low_threshold
                    
                    	Low threshold warning for Instantaneous Pre FEC BER
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: pre_fec_ber_latched_max_alarm_high_threshold
                    
                    	High threshold alarm for Latched Max Pre FEC BER
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: pre_fec_ber_latched_max_alarm_low_threshold
                    
                    	Low threshold alarm for Latched Max Pre FEC BER
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: pre_fec_ber_latched_max_warn_high_threshold
                    
                    	High threshold warning for Latched Max Pre FEC BER
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: pre_fec_ber_latched_max_warn_low_threshold
                    
                    	Low threshold warning for Latched Max Pre FEC BER
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: pre_fec_ber_latched_min_alarm_high_threshold
                    
                    	High threshold alarm for Latched Min Pre FEC BER
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: pre_fec_ber_latched_min_alarm_low_threshold
                    
                    	Low threshold alarm for Latched Min Pre FEC BER
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: pre_fec_ber_latched_min_warn_high_threshold
                    
                    	High threshold warning for Latched Min Pre FEC BER
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: pre_fec_ber_latched_min_warn_low_threshold
                    
                    	Low threshold warning for Latched Min Pre FEC BER
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: pre_fec_ber_warn_high_threshold
                    
                    	High threshold warning for Pre FEC BER
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: pre_fec_ber_warn_low_threshold
                    
                    	Low threshold warning for Pre FEC BER
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
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
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: uncorrected_ber_accumulated_alarm_low_threshold
                    
                    	Low threshold alarm for Accumulated Uncorrected BER
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: uncorrected_ber_accumulated_warn_high_threshold
                    
                    	High threshold warning for Accumulated Uncorrected BER
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: uncorrected_ber_accumulated_warn_low_threshold
                    
                    	Low threshold warning for Accumulated Uncorrected BER
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: uncorrected_ber_alarm_high_threshold
                    
                    	High threshold alarm for Uncorrected BER
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: uncorrected_ber_alarm_low_threshold
                    
                    	Low threshold alarm for Uncorrected BER
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: uncorrected_ber_instantaneous_alarm_high_threshold
                    
                    	High threshold alarm for Instantaneous Uncorrected BER
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: uncorrected_ber_instantaneous_alarm_low_threshold
                    
                    	Low threshold alarm for Instantaneous Uncorrected BER
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: uncorrected_ber_instantaneous_warn_high_threshold
                    
                    	High threshold warning for Instantaneous Uncorrected BER
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: uncorrected_ber_instantaneous_warn_low_threshold
                    
                    	Low threshold warning for Instantaneous Uncorrected BER
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: uncorrected_ber_latched_max_alarm_high_threshold
                    
                    	High threshold alarm for Latched\_Max Uncorrected BER
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: uncorrected_ber_latched_max_alarm_low_threshold
                    
                    	Low threshold alarm for Latched\_Max Uncorrected BER
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: uncorrected_ber_latched_max_warn_high_threshold
                    
                    	High threshold warning Latched\_Max for Uncorrected BER
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: uncorrected_ber_latched_max_warn_low_threshold
                    
                    	Low threshold warning Latched\_Max for Uncorrected BER
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: uncorrected_ber_latched_min_alarm_high_threshold
                    
                    	High threshold alarm for  Latched Min Uncorrected BER
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: uncorrected_ber_latched_min_alarm_low_threshold
                    
                    	Low threshold alarm for  Latched Min Uncorrected BER
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: uncorrected_ber_latched_min_warn_high_threshold
                    
                    	High threshold warning for  Latched Min Uncorrected BER
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: uncorrected_ber_latched_min_warn_low_threshold
                    
                    	Low threshold alarm for Latched Min Uncorrected BER
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: uncorrected_ber_warn_high_threshold
                    
                    	High threshold warning for Uncorrected BER
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: uncorrected_ber_warn_low_threshold
                    
                    	Low threshold warning for Uncorrected BER
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    

                    """

                    _prefix = 'controller-optics-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.isi_correction_alarm_high_threshold = None
                        self.isi_correction_alarm_low_threshold = None
                        self.isi_correction_warn_high_threshold = None
                        self.isi_correction_warn_low_threshold = None
                        self.laser_diff_frequency_alarm_high_threshold = None
                        self.laser_diff_frequency_alarm_low_threshold = None
                        self.laser_diff_frequency_warn_high_threshold = None
                        self.laser_diff_frequency_warn_low_threshold = None
                        self.laser_diff_temperature_alarm_high_threshold = None
                        self.laser_diff_temperature_alarm_low_threshold = None
                        self.laser_diff_temperature_warn_high_threshold = None
                        self.laser_diff_temperature_warn_low_threshold = None
                        self.pam_rate_alarm_high_threshold = None
                        self.pam_rate_alarm_low_threshold = None
                        self.pam_rate_warn_high_threshold = None
                        self.pam_rate_warn_low_threshold = None
                        self.pre_fec_ber_accumulated_alarm_high_threshold = None
                        self.pre_fec_ber_accumulated_alarm_low_threshold = None
                        self.pre_fec_ber_accumulated_warn_high_threshold = None
                        self.pre_fec_ber_accumulated_warn_low_threshold = None
                        self.pre_fec_ber_alarm_high_threshold = None
                        self.pre_fec_ber_alarm_low_threshold = None
                        self.pre_fec_ber_instantaneous_alarm_high_threshold = None
                        self.pre_fec_ber_instantaneous_alarm_low_threshold = None
                        self.pre_fec_ber_instantaneous_warn_high_threshold = None
                        self.pre_fec_ber_instantaneous_warn_low_threshold = None
                        self.pre_fec_ber_latched_max_alarm_high_threshold = None
                        self.pre_fec_ber_latched_max_alarm_low_threshold = None
                        self.pre_fec_ber_latched_max_warn_high_threshold = None
                        self.pre_fec_ber_latched_max_warn_low_threshold = None
                        self.pre_fec_ber_latched_min_alarm_high_threshold = None
                        self.pre_fec_ber_latched_min_alarm_low_threshold = None
                        self.pre_fec_ber_latched_min_warn_high_threshold = None
                        self.pre_fec_ber_latched_min_warn_low_threshold = None
                        self.pre_fec_ber_warn_high_threshold = None
                        self.pre_fec_ber_warn_low_threshold = None
                        self.snr_alarm_high_threshold = None
                        self.snr_alarm_low_threshold = None
                        self.snr_warn_high_threshold = None
                        self.snr_warn_low_threshold = None
                        self.tec_current_alarm_high_threshold = None
                        self.tec_current_alarm_low_threshold = None
                        self.tec_current_warn_high_threshold = None
                        self.tec_current_warn_low_threshold = None
                        self.uncorrected_ber_accumulated_alarm_high_threshold = None
                        self.uncorrected_ber_accumulated_alarm_low_threshold = None
                        self.uncorrected_ber_accumulated_warn_high_threshold = None
                        self.uncorrected_ber_accumulated_warn_low_threshold = None
                        self.uncorrected_ber_alarm_high_threshold = None
                        self.uncorrected_ber_alarm_low_threshold = None
                        self.uncorrected_ber_instantaneous_alarm_high_threshold = None
                        self.uncorrected_ber_instantaneous_alarm_low_threshold = None
                        self.uncorrected_ber_instantaneous_warn_high_threshold = None
                        self.uncorrected_ber_instantaneous_warn_low_threshold = None
                        self.uncorrected_ber_latched_max_alarm_high_threshold = None
                        self.uncorrected_ber_latched_max_alarm_low_threshold = None
                        self.uncorrected_ber_latched_max_warn_high_threshold = None
                        self.uncorrected_ber_latched_max_warn_low_threshold = None
                        self.uncorrected_ber_latched_min_alarm_high_threshold = None
                        self.uncorrected_ber_latched_min_alarm_low_threshold = None
                        self.uncorrected_ber_latched_min_warn_high_threshold = None
                        self.uncorrected_ber_latched_min_warn_low_threshold = None
                        self.uncorrected_ber_warn_high_threshold = None
                        self.uncorrected_ber_warn_low_threshold = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:ext-param-threshold-val'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.isi_correction_alarm_high_threshold is not None:
                            return True

                        if self.isi_correction_alarm_low_threshold is not None:
                            return True

                        if self.isi_correction_warn_high_threshold is not None:
                            return True

                        if self.isi_correction_warn_low_threshold is not None:
                            return True

                        if self.laser_diff_frequency_alarm_high_threshold is not None:
                            return True

                        if self.laser_diff_frequency_alarm_low_threshold is not None:
                            return True

                        if self.laser_diff_frequency_warn_high_threshold is not None:
                            return True

                        if self.laser_diff_frequency_warn_low_threshold is not None:
                            return True

                        if self.laser_diff_temperature_alarm_high_threshold is not None:
                            return True

                        if self.laser_diff_temperature_alarm_low_threshold is not None:
                            return True

                        if self.laser_diff_temperature_warn_high_threshold is not None:
                            return True

                        if self.laser_diff_temperature_warn_low_threshold is not None:
                            return True

                        if self.pam_rate_alarm_high_threshold is not None:
                            return True

                        if self.pam_rate_alarm_low_threshold is not None:
                            return True

                        if self.pam_rate_warn_high_threshold is not None:
                            return True

                        if self.pam_rate_warn_low_threshold is not None:
                            return True

                        if self.pre_fec_ber_accumulated_alarm_high_threshold is not None:
                            return True

                        if self.pre_fec_ber_accumulated_alarm_low_threshold is not None:
                            return True

                        if self.pre_fec_ber_accumulated_warn_high_threshold is not None:
                            return True

                        if self.pre_fec_ber_accumulated_warn_low_threshold is not None:
                            return True

                        if self.pre_fec_ber_alarm_high_threshold is not None:
                            return True

                        if self.pre_fec_ber_alarm_low_threshold is not None:
                            return True

                        if self.pre_fec_ber_instantaneous_alarm_high_threshold is not None:
                            return True

                        if self.pre_fec_ber_instantaneous_alarm_low_threshold is not None:
                            return True

                        if self.pre_fec_ber_instantaneous_warn_high_threshold is not None:
                            return True

                        if self.pre_fec_ber_instantaneous_warn_low_threshold is not None:
                            return True

                        if self.pre_fec_ber_latched_max_alarm_high_threshold is not None:
                            return True

                        if self.pre_fec_ber_latched_max_alarm_low_threshold is not None:
                            return True

                        if self.pre_fec_ber_latched_max_warn_high_threshold is not None:
                            return True

                        if self.pre_fec_ber_latched_max_warn_low_threshold is not None:
                            return True

                        if self.pre_fec_ber_latched_min_alarm_high_threshold is not None:
                            return True

                        if self.pre_fec_ber_latched_min_alarm_low_threshold is not None:
                            return True

                        if self.pre_fec_ber_latched_min_warn_high_threshold is not None:
                            return True

                        if self.pre_fec_ber_latched_min_warn_low_threshold is not None:
                            return True

                        if self.pre_fec_ber_warn_high_threshold is not None:
                            return True

                        if self.pre_fec_ber_warn_low_threshold is not None:
                            return True

                        if self.snr_alarm_high_threshold is not None:
                            return True

                        if self.snr_alarm_low_threshold is not None:
                            return True

                        if self.snr_warn_high_threshold is not None:
                            return True

                        if self.snr_warn_low_threshold is not None:
                            return True

                        if self.tec_current_alarm_high_threshold is not None:
                            return True

                        if self.tec_current_alarm_low_threshold is not None:
                            return True

                        if self.tec_current_warn_high_threshold is not None:
                            return True

                        if self.tec_current_warn_low_threshold is not None:
                            return True

                        if self.uncorrected_ber_accumulated_alarm_high_threshold is not None:
                            return True

                        if self.uncorrected_ber_accumulated_alarm_low_threshold is not None:
                            return True

                        if self.uncorrected_ber_accumulated_warn_high_threshold is not None:
                            return True

                        if self.uncorrected_ber_accumulated_warn_low_threshold is not None:
                            return True

                        if self.uncorrected_ber_alarm_high_threshold is not None:
                            return True

                        if self.uncorrected_ber_alarm_low_threshold is not None:
                            return True

                        if self.uncorrected_ber_instantaneous_alarm_high_threshold is not None:
                            return True

                        if self.uncorrected_ber_instantaneous_alarm_low_threshold is not None:
                            return True

                        if self.uncorrected_ber_instantaneous_warn_high_threshold is not None:
                            return True

                        if self.uncorrected_ber_instantaneous_warn_low_threshold is not None:
                            return True

                        if self.uncorrected_ber_latched_max_alarm_high_threshold is not None:
                            return True

                        if self.uncorrected_ber_latched_max_alarm_low_threshold is not None:
                            return True

                        if self.uncorrected_ber_latched_max_warn_high_threshold is not None:
                            return True

                        if self.uncorrected_ber_latched_max_warn_low_threshold is not None:
                            return True

                        if self.uncorrected_ber_latched_min_alarm_high_threshold is not None:
                            return True

                        if self.uncorrected_ber_latched_min_alarm_low_threshold is not None:
                            return True

                        if self.uncorrected_ber_latched_min_warn_high_threshold is not None:
                            return True

                        if self.uncorrected_ber_latched_min_warn_low_threshold is not None:
                            return True

                        if self.uncorrected_ber_warn_high_threshold is not None:
                            return True

                        if self.uncorrected_ber_warn_low_threshold is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                        return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtParamThresholdVal']['meta_info']


                class LaneData(object):
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
                        self.parent = None
                        self.lane_alarm_info = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo()
                        self.lane_alarm_info.parent = self
                        self.lane_index = None
                        self.laser_bias_current_milli_amps = None
                        self.laser_bias_current_percent = None
                        self.output_frequency = None
                        self.receive_power = None
                        self.receive_signal_power = None
                        self.transmit_power = None
                        self.transmit_signal_power = None


                    class LaneAlarmInfo(object):
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
                            self.parent = None
                            self.high_lbc = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.HighLbc()
                            self.high_lbc.parent = self
                            self.high_rx_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.HighRxPower()
                            self.high_rx_power.parent = self
                            self.high_tx_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.HighTxPower()
                            self.high_tx_power.parent = self
                            self.low_rx_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.LowRxPower()
                            self.low_rx_power.parent = self
                            self.low_tx_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.LowTxPower()
                            self.low_tx_power.parent = self


                        class HighRxPower(object):
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
                                self.parent = None
                                self.counter = None
                                self.is_detected = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:high-rx-power'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.counter is not None:
                                    return True

                                if self.is_detected is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                                return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.HighRxPower']['meta_info']


                        class LowRxPower(object):
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
                                self.parent = None
                                self.counter = None
                                self.is_detected = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:low-rx-power'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.counter is not None:
                                    return True

                                if self.is_detected is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                                return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.LowRxPower']['meta_info']


                        class HighTxPower(object):
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
                                self.parent = None
                                self.counter = None
                                self.is_detected = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:high-tx-power'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.counter is not None:
                                    return True

                                if self.is_detected is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                                return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.HighTxPower']['meta_info']


                        class LowTxPower(object):
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
                                self.parent = None
                                self.counter = None
                                self.is_detected = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:low-tx-power'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.counter is not None:
                                    return True

                                if self.is_detected is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                                return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.LowTxPower']['meta_info']


                        class HighLbc(object):
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
                                self.parent = None
                                self.counter = None
                                self.is_detected = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:high-lbc'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.counter is not None:
                                    return True

                                if self.is_detected is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                                return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.HighLbc']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:lane-alarm-info'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.high_lbc is not None and self.high_lbc._has_data():
                                return True

                            if self.high_rx_power is not None and self.high_rx_power._has_data():
                                return True

                            if self.high_tx_power is not None and self.high_tx_power._has_data():
                                return True

                            if self.low_rx_power is not None and self.low_rx_power._has_data():
                                return True

                            if self.low_tx_power is not None and self.low_tx_power._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:lane-data'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.lane_alarm_info is not None and self.lane_alarm_info._has_data():
                            return True

                        if self.lane_index is not None:
                            return True

                        if self.laser_bias_current_milli_amps is not None:
                            return True

                        if self.laser_bias_current_percent is not None:
                            return True

                        if self.output_frequency is not None:
                            return True

                        if self.receive_power is not None:
                            return True

                        if self.receive_signal_power is not None:
                            return True

                        if self.transmit_power is not None:
                            return True

                        if self.transmit_signal_power is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                        return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:optics-info'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.alarm_detected is not None:
                        return True

                    if self.ampli_channel_power_config_val is not None:
                        return True

                    if self.ampli_control_mode_config_val is not None:
                        return True

                    if self.ampli_gain is not None:
                        return True

                    if self.ampli_gain_config_val is not None:
                        return True

                    if self.ampli_gain_range_config_val is not None:
                        return True

                    if self.ampli_gain_thr_deg_high_config_val is not None:
                        return True

                    if self.ampli_gain_thr_deg_low_config_val is not None:
                        return True

                    if self.ampli_tilt is not None:
                        return True

                    if self.ampli_tilt_config_val is not None:
                        return True

                    if self.cd is not None:
                        return True

                    if self.cd_configurable is not None:
                        return True

                    if self.cd_high_threshold is not None:
                        return True

                    if self.cd_low_threshold is not None:
                        return True

                    if self.cd_max is not None:
                        return True

                    if self.cd_min is not None:
                        return True

                    if self.cfg_tx_power is not None:
                        return True

                    if self.cfg_tx_power_configurable is not None:
                        return True

                    if self.channel_power_max_delta_config_val is not None:
                        return True

                    if self.controller_state is not None:
                        return True

                    if self.dgd_high_threshold is not None:
                        return True

                    if self.differential_group_delay is not None:
                        return True

                    if self.display_volt_temp is not None:
                        return True

                    if self.dwdm_carrier_band is not None:
                        return True

                    if self.dwdm_carrier_channel is not None:
                        return True

                    if self.dwdm_carrier_frequency is not None:
                        return True

                    if self.dwdm_carrier_wavelength is not None:
                        return True

                    if self.ext_param_threshold_val is not None and self.ext_param_threshold_val._has_data():
                        return True

                    if self.ext_param_val is not None and self.ext_param_val._has_data():
                        return True

                    if self.form_factor is not None:
                        return True

                    if self.grey_wavelength is not None:
                        return True

                    if self.is_bo_configured is not None:
                        return True

                    if self.is_ext_param_valid is not None:
                        return True

                    if self.lane_data is not None:
                        for child_ref in self.lane_data:
                            if child_ref._has_data():
                                return True

                    if self.laser_state is not None:
                        return True

                    if self.lbc_high_threshold is not None:
                        return True

                    if self.lbc_th_high_default is not None:
                        return True

                    if self.lbc_th_high_warning_default is not None:
                        return True

                    if self.lbc_th_low_default is not None:
                        return True

                    if self.lbc_th_low_warning_default is not None:
                        return True

                    if self.led_state is not None:
                        return True

                    if self.network_srlg_info is not None and self.network_srlg_info._has_data():
                        return True

                    if self.optical_signal_to_noise_ratio is not None:
                        return True

                    if self.optics_alarm_info is not None and self.optics_alarm_info._has_data():
                        return True

                    if self.optics_fec is not None:
                        return True

                    if self.optics_module is not None:
                        return True

                    if self.optics_present is not None:
                        return True

                    if self.optics_type is not None:
                        return True

                    if self.osnr_low_threshold is not None:
                        return True

                    if self.osri_config_val is not None:
                        return True

                    if self.ots_alarm_info is not None and self.ots_alarm_info._has_data():
                        return True

                    if self.phase_noise is not None:
                        return True

                    if self.phy_type is not None:
                        return True

                    if self.pm_enable is not None:
                        return True

                    if self.polarization_change_rate is not None:
                        return True

                    if self.polarization_dependent_loss is not None:
                        return True

                    if self.polarization_mode_dispersion is not None:
                        return True

                    if self.port_status is not None:
                        return True

                    if self.port_type is not None:
                        return True

                    if self.rx_high_threshold is not None:
                        return True

                    if self.rx_high_warning_threshold is not None:
                        return True

                    if self.rx_low_threshold is not None:
                        return True

                    if self.rx_low_warning_threshold is not None:
                        return True

                    if self.rx_power is not None:
                        return True

                    if self.rx_power_th_configurable is not None:
                        return True

                    if self.rx_voa_attenuation is not None:
                        return True

                    if self.rx_voa_attenuation_config_val is not None:
                        return True

                    if self.safety_control_mode_config_val is not None:
                        return True

                    if self.second_order_polarization_mode_dispersion is not None:
                        return True

                    if self.temp_high_threshold is not None:
                        return True

                    if self.temp_high_warning_threshold is not None:
                        return True

                    if self.temp_low_threshold is not None:
                        return True

                    if self.temp_low_warning_threshold is not None:
                        return True

                    if self.temperature is not None:
                        return True

                    if self.total_rx_power is not None:
                        return True

                    if self.total_tx_power is not None:
                        return True

                    if self.transceiver_info is not None and self.transceiver_info._has_data():
                        return True

                    if self.transport_admin_state is not None:
                        return True

                    if self.tx_high_threshold is not None:
                        return True

                    if self.tx_high_warning_threshold is not None:
                        return True

                    if self.tx_low_threshold is not None:
                        return True

                    if self.tx_low_warning_threshold is not None:
                        return True

                    if self.tx_power is not None:
                        return True

                    if self.tx_power_th_configurable is not None:
                        return True

                    if self.tx_voa_attenuation is not None:
                        return True

                    if self.tx_voa_attenuation_config_val is not None:
                        return True

                    if self.volt_high_threshold is not None:
                        return True

                    if self.volt_high_warning_threshold is not None:
                        return True

                    if self.volt_low_threshold is not None:
                        return True

                    if self.volt_low_warning_threshold is not None:
                        return True

                    if self.voltage is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                    return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo']['meta_info']


            class OpticsLanes(object):
                """
                All Optics Port operational data
                
                .. attribute:: optics_lane
                
                	Lane Information
                	**type**\: list of    :py:class:`OpticsLane <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane>`
                
                

                """

                _prefix = 'controller-optics-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.optics_lane = YList()
                    self.optics_lane.parent = self
                    self.optics_lane.name = 'optics_lane'


                class OpticsLane(object):
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
                        self.parent = None
                        self.number = None
                        self.lane_alarm_info = OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo()
                        self.lane_alarm_info.parent = self
                        self.lane_index = None
                        self.laser_bias_current_milli_amps = None
                        self.laser_bias_current_percent = None
                        self.output_frequency = None
                        self.receive_power = None
                        self.receive_signal_power = None
                        self.transmit_power = None
                        self.transmit_signal_power = None


                    class LaneAlarmInfo(object):
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
                            self.parent = None
                            self.high_lbc = OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.HighLbc()
                            self.high_lbc.parent = self
                            self.high_rx_power = OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.HighRxPower()
                            self.high_rx_power.parent = self
                            self.high_tx_power = OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.HighTxPower()
                            self.high_tx_power.parent = self
                            self.low_rx_power = OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.LowRxPower()
                            self.low_rx_power.parent = self
                            self.low_tx_power = OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.LowTxPower()
                            self.low_tx_power.parent = self


                        class HighRxPower(object):
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
                                self.parent = None
                                self.counter = None
                                self.is_detected = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:high-rx-power'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.counter is not None:
                                    return True

                                if self.is_detected is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                                return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.HighRxPower']['meta_info']


                        class LowRxPower(object):
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
                                self.parent = None
                                self.counter = None
                                self.is_detected = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:low-rx-power'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.counter is not None:
                                    return True

                                if self.is_detected is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                                return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.LowRxPower']['meta_info']


                        class HighTxPower(object):
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
                                self.parent = None
                                self.counter = None
                                self.is_detected = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:high-tx-power'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.counter is not None:
                                    return True

                                if self.is_detected is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                                return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.HighTxPower']['meta_info']


                        class LowTxPower(object):
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
                                self.parent = None
                                self.counter = None
                                self.is_detected = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:low-tx-power'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.counter is not None:
                                    return True

                                if self.is_detected is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                                return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.LowTxPower']['meta_info']


                        class HighLbc(object):
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
                                self.parent = None
                                self.counter = None
                                self.is_detected = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:high-lbc'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.counter is not None:
                                    return True

                                if self.is_detected is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                                return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.HighLbc']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:lane-alarm-info'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.high_lbc is not None and self.high_lbc._has_data():
                                return True

                            if self.high_rx_power is not None and self.high_rx_power._has_data():
                                return True

                            if self.high_tx_power is not None and self.high_tx_power._has_data():
                                return True

                            if self.low_rx_power is not None and self.low_rx_power._has_data():
                                return True

                            if self.low_tx_power is not None and self.low_tx_power._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.number is None:
                            raise YPYModelError('Key property number is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:optics-lane[Cisco-IOS-XR-controller-optics-oper:number = ' + str(self.number) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.number is not None:
                            return True

                        if self.lane_alarm_info is not None and self.lane_alarm_info._has_data():
                            return True

                        if self.lane_index is not None:
                            return True

                        if self.laser_bias_current_milli_amps is not None:
                            return True

                        if self.laser_bias_current_percent is not None:
                            return True

                        if self.output_frequency is not None:
                            return True

                        if self.receive_power is not None:
                            return True

                        if self.receive_signal_power is not None:
                            return True

                        if self.transmit_power is not None:
                            return True

                        if self.transmit_signal_power is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                        return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:optics-lanes'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.optics_lane is not None:
                        for child_ref in self.optics_lane:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                    return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsLanes']['meta_info']


            class OpticsDbInfo(object):
                """
                Optics operational data
                
                .. attribute:: controller_state
                
                	Optics controller state\: Up, Down or Administratively Down
                	**type**\:   :py:class:`OpticsControllerStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsControllerStateEnum>`
                
                .. attribute:: network_srlg_info
                
                	Network SRLG information
                	**type**\:   :py:class:`NetworkSrlgInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsDbInfo.NetworkSrlgInfo>`
                
                .. attribute:: transport_admin_state
                
                	Transport Admin State
                	**type**\:   :py:class:`OpticsTasEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsTasEnum>`
                
                

                """

                _prefix = 'controller-optics-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.controller_state = None
                    self.network_srlg_info = OpticsOper.OpticsPorts.OpticsPort.OpticsDbInfo.NetworkSrlgInfo()
                    self.network_srlg_info.parent = self
                    self.transport_admin_state = None


                class NetworkSrlgInfo(object):
                    """
                    Network SRLG information
                    
                    .. attribute:: network_srlg_array
                    
                    	Network Srlg Array
                    	**type**\: list of    :py:class:`NetworkSrlgArray <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsDbInfo.NetworkSrlgInfo.NetworkSrlgArray>`
                    
                    

                    """

                    _prefix = 'controller-optics-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.network_srlg_array = YList()
                        self.network_srlg_array.parent = self
                        self.network_srlg_array.name = 'network_srlg_array'


                    class NetworkSrlgArray(object):
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
                            self.parent = None
                            self.network_srlg = YLeafList()
                            self.network_srlg.parent = self
                            self.network_srlg.name = 'network_srlg'
                            self.set_number = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:network-srlg-array'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.network_srlg is not None:
                                for child in self.network_srlg:
                                    if child is not None:
                                        return True

                            if self.set_number is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsDbInfo.NetworkSrlgInfo.NetworkSrlgArray']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:network-srlg-info'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.network_srlg_array is not None:
                            for child_ref in self.network_srlg_array:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                        return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsDbInfo.NetworkSrlgInfo']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:optics-db-info'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.controller_state is not None:
                        return True

                    if self.network_srlg_info is not None and self.network_srlg_info._has_data():
                        return True

                    if self.transport_admin_state is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                    return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsDbInfo']['meta_info']

            @property
            def _common_path(self):
                if self.name is None:
                    raise YPYModelError('Key property name is None')

                return '/Cisco-IOS-XR-controller-optics-oper:optics-oper/Cisco-IOS-XR-controller-optics-oper:optics-ports/Cisco-IOS-XR-controller-optics-oper:optics-port[Cisco-IOS-XR-controller-optics-oper:name = ' + str(self.name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.name is not None:
                    return True

                if self.optics_db_info is not None and self.optics_db_info._has_data():
                    return True

                if self.optics_dwdm_carrrier_channel_map is not None and self.optics_dwdm_carrrier_channel_map._has_data():
                    return True

                if self.optics_info is not None and self.optics_info._has_data():
                    return True

                if self.optics_lanes is not None and self.optics_lanes._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-controller-optics-oper:optics-oper/Cisco-IOS-XR-controller-optics-oper:optics-ports'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.optics_port is not None:
                for child_ref in self.optics_port:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
            return meta._meta_table['OpticsOper.OpticsPorts']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-controller-optics-oper:optics-oper'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.optics_ports is not None and self.optics_ports._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_oper as meta
        return meta._meta_table['OpticsOper']['meta_info']


