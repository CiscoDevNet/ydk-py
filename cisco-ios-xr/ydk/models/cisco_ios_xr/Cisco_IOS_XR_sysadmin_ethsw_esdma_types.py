""" Cisco_IOS_XR_sysadmin_ethsw_esdma_types 

This module contains definitions
for the Calvados model objects.

This module contains the YANG enumerated type
definitions used by the Cisco IOS\-XR SysAdmin
Control Ethernet commands.

Copyright(c) 2011\-2017 by Cisco Systems, Inc.
All rights reserved.

Copyright (c) 2012\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class EsdCirEirType(Enum):
    """
    EsdCirEirType (Enum Class)

    .. data:: CIR = 0

    .. data:: PIR = 1

    """

    CIR = Enum.YLeaf(0, "CIR")

    PIR = Enum.YLeaf(1, "PIR")


class EsdmaCpu(Enum):
    """
    EsdmaCpu (Enum Class)

    The set of CPU enumerations that have control plane Ethernet switches or run the MLAP protocol.

    .. data:: Unknown = 0

    .. data:: RP0 = 1

    .. data:: RP1 = 2

    .. data:: SC0 = 3

    .. data:: SC1 = 4

    .. data:: LC0 = 5

    .. data:: LC1 = 6

    .. data:: LC2 = 7

    .. data:: LC3 = 8

    .. data:: LC4 = 9

    .. data:: LC5 = 10

    .. data:: LC6 = 11

    .. data:: LC7 = 12

    .. data:: LC8 = 13

    .. data:: LC9 = 14

    .. data:: LC10 = 15

    .. data:: LC11 = 16

    .. data:: LC12 = 17

    .. data:: LC13 = 18

    .. data:: LC14 = 19

    .. data:: LC15 = 20

    .. data:: LC16 = 21

    .. data:: LC17 = 22

    .. data:: LC18 = 23

    .. data:: LC19 = 24

    .. data:: FC0 = 25

    .. data:: FC1 = 26

    .. data:: FC2 = 27

    .. data:: FC3 = 28

    .. data:: FC4 = 29

    .. data:: FC5 = 30

    .. data:: CB0 = 31

    """

    Unknown = Enum.YLeaf(0, "Unknown")

    RP0 = Enum.YLeaf(1, "RP0")

    RP1 = Enum.YLeaf(2, "RP1")

    SC0 = Enum.YLeaf(3, "SC0")

    SC1 = Enum.YLeaf(4, "SC1")

    LC0 = Enum.YLeaf(5, "LC0")

    LC1 = Enum.YLeaf(6, "LC1")

    LC2 = Enum.YLeaf(7, "LC2")

    LC3 = Enum.YLeaf(8, "LC3")

    LC4 = Enum.YLeaf(9, "LC4")

    LC5 = Enum.YLeaf(10, "LC5")

    LC6 = Enum.YLeaf(11, "LC6")

    LC7 = Enum.YLeaf(12, "LC7")

    LC8 = Enum.YLeaf(13, "LC8")

    LC9 = Enum.YLeaf(14, "LC9")

    LC10 = Enum.YLeaf(15, "LC10")

    LC11 = Enum.YLeaf(16, "LC11")

    LC12 = Enum.YLeaf(17, "LC12")

    LC13 = Enum.YLeaf(18, "LC13")

    LC14 = Enum.YLeaf(19, "LC14")

    LC15 = Enum.YLeaf(20, "LC15")

    LC16 = Enum.YLeaf(21, "LC16")

    LC17 = Enum.YLeaf(22, "LC17")

    LC18 = Enum.YLeaf(23, "LC18")

    LC19 = Enum.YLeaf(24, "LC19")

    FC0 = Enum.YLeaf(25, "FC0")

    FC1 = Enum.YLeaf(26, "FC1")

    FC2 = Enum.YLeaf(27, "FC2")

    FC3 = Enum.YLeaf(28, "FC3")

    FC4 = Enum.YLeaf(29, "FC4")

    FC5 = Enum.YLeaf(30, "FC5")

    CB0 = Enum.YLeaf(31, "CB0")


class EsdmaQsfpTransceiverEnum(Enum):
    """
    EsdmaQsfpTransceiverEnum (Enum Class)

    .. data:: QSFP_40G_LR4 = 0

    .. data:: QSFP_40G_SR4 = 1

    .. data:: QSFP_40G_CR4_Active = 2

    .. data:: QSFP_40G_CR4_Passive = 3

    .. data:: Unknown = 4

    """

    QSFP_40G_LR4 = Enum.YLeaf(0, "QSFP-40G-LR4")

    QSFP_40G_SR4 = Enum.YLeaf(1, "QSFP-40G-SR4")

    QSFP_40G_CR4_Active = Enum.YLeaf(2, "QSFP-40G-CR4-Active")

    QSFP_40G_CR4_Passive = Enum.YLeaf(3, "QSFP-40G-CR4-Passive")

    Unknown = Enum.YLeaf(4, "Unknown")


class EsdmaRackNumEnum(Enum):
    """
    EsdmaRackNumEnum (Enum Class)

    The valid rack numbers supported in Sysadmin.

    .. data:: Y_0 = 0

    .. data:: Y_1 = 1

    .. data:: Y_2 = 2

    .. data:: Y_3 = 3

    .. data:: Y_4 = 4

    .. data:: Y_5 = 5

    .. data:: Y_6 = 6

    .. data:: Y_7 = 7

    .. data:: Y_8 = 8

    .. data:: Y_9 = 9

    .. data:: Y_10 = 10

    .. data:: Y_11 = 11

    .. data:: Y_12 = 12

    .. data:: Y_13 = 13

    .. data:: Y_14 = 14

    .. data:: Y_15 = 15

    .. data:: F0 = 16

    .. data:: F1 = 17

    .. data:: F2 = 18

    .. data:: F3 = 19

    .. data:: B0 = 20

    .. data:: B1 = 21

    """

    Y_0 = Enum.YLeaf(0, "0")

    Y_1 = Enum.YLeaf(1, "1")

    Y_2 = Enum.YLeaf(2, "2")

    Y_3 = Enum.YLeaf(3, "3")

    Y_4 = Enum.YLeaf(4, "4")

    Y_5 = Enum.YLeaf(5, "5")

    Y_6 = Enum.YLeaf(6, "6")

    Y_7 = Enum.YLeaf(7, "7")

    Y_8 = Enum.YLeaf(8, "8")

    Y_9 = Enum.YLeaf(9, "9")

    Y_10 = Enum.YLeaf(10, "10")

    Y_11 = Enum.YLeaf(11, "11")

    Y_12 = Enum.YLeaf(12, "12")

    Y_13 = Enum.YLeaf(13, "13")

    Y_14 = Enum.YLeaf(14, "14")

    Y_15 = Enum.YLeaf(15, "15")

    F0 = Enum.YLeaf(16, "F0")

    F1 = Enum.YLeaf(17, "F1")

    F2 = Enum.YLeaf(18, "F2")

    F3 = Enum.YLeaf(19, "F3")

    B0 = Enum.YLeaf(20, "B0")

    B1 = Enum.YLeaf(21, "B1")


class EsdmaRackTypeEnum(Enum):
    """
    EsdmaRackTypeEnum (Enum Class)

    The valid chassis types supported supported in Sysadmin.

    .. data:: Unknown = 0

    .. data:: FCC = 1

    .. data:: LCC = 2

    .. data:: BSC = 3

    .. data:: COMPUTE = 4

    """

    Unknown = Enum.YLeaf(0, "Unknown")

    FCC = Enum.YLeaf(1, "FCC")

    LCC = Enum.YLeaf(2, "LCC")

    BSC = Enum.YLeaf(3, "BSC")

    COMPUTE = Enum.YLeaf(4, "COMPUTE")


class EsdmaSdrTrafficType(Enum):
    """
    EsdmaSdrTrafficType (Enum Class)

    .. data:: Unknown = 0

    .. data:: IPC = 1

    .. data:: MgmtEth = 2

    .. data:: All = 3

    .. data:: Invalid = 4

    """

    Unknown = Enum.YLeaf(0, "Unknown")

    IPC = Enum.YLeaf(1, "IPC")

    MgmtEth = Enum.YLeaf(2, "MgmtEth")

    All = Enum.YLeaf(3, "All")

    Invalid = Enum.YLeaf(4, "Invalid")


class EsdmaSfpEncodingEnum(Enum):
    """
    EsdmaSfpEncodingEnum (Enum Class)

    .. data:: Unspecified = 0

    .. data:: Y_8B__FWD_SLASH__10B = 1

    .. data:: Y_4B__FWD_SLASH__5B = 2

    .. data:: NRZ = 3

    .. data:: Manchester = 4

    .. data:: SONET_Scrambled = 5

    .. data:: Y_64B__FWD_SLASH__66B = 6

    .. data:: Unknown = 7

    """

    Unspecified = Enum.YLeaf(0, "Unspecified")

    Y_8B__FWD_SLASH__10B = Enum.YLeaf(1, "8B/10B")

    Y_4B__FWD_SLASH__5B = Enum.YLeaf(2, "4B/5B")

    NRZ = Enum.YLeaf(3, "NRZ")

    Manchester = Enum.YLeaf(4, "Manchester")

    SONET_Scrambled = Enum.YLeaf(5, "SONET Scrambled")

    Y_64B__FWD_SLASH__66B = Enum.YLeaf(6, "64B/66B")

    Unknown = Enum.YLeaf(7, "Unknown")


class EsdmaSwitchPortState(Enum):
    """
    EsdmaSwitchPortState (Enum Class)

    The switch port up and down states

    .. data:: Unknown = 0

    .. data:: Test = 1

    .. data:: Down = 2

    .. data:: Up = 3

    """

    Unknown = Enum.YLeaf(0, "Unknown")

    Test = Enum.YLeaf(1, "Test")

    Down = Enum.YLeaf(2, "Down")

    Up = Enum.YLeaf(3, "Up")


class EsdmaSwitchSfpControllerEnum(Enum):
    """
    EsdmaSwitchSfpControllerEnum (Enum Class)

    .. data:: Unknown = 0

    .. data:: Switch = 1

    .. data:: PHY = 2

    """

    Unknown = Enum.YLeaf(0, "Unknown")

    Switch = Enum.YLeaf(1, "Switch")

    PHY = Enum.YLeaf(2, "PHY")


class EsdmaSwitchSfpInsertedEnum(Enum):
    """
    EsdmaSwitchSfpInsertedEnum (Enum Class)

    .. data:: Unknown = 0

    .. data:: Yes = 1

    .. data:: No = 2

    .. data:: Failed = 3

    """

    Unknown = Enum.YLeaf(0, "Unknown")

    Yes = Enum.YLeaf(1, "Yes")

    No = Enum.YLeaf(2, "No")

    Failed = Enum.YLeaf(3, "Failed")


class EsdmaSwitchSfpTranceiverTypeEnum(Enum):
    """
    EsdmaSwitchSfpTranceiverTypeEnum (Enum Class)

    .. data:: Unspecified = 0

    .. data:: SFP = 1

    .. data:: QSFP = 2

    .. data:: Unknown = 3

    """

    Unspecified = Enum.YLeaf(0, "Unspecified")

    SFP = Enum.YLeaf(1, "SFP")

    QSFP = Enum.YLeaf(2, "QSFP")

    Unknown = Enum.YLeaf(3, "Unknown")


class EsdmaSwitchSfpTypeEnum(Enum):
    """
    EsdmaSwitchSfpTypeEnum (Enum Class)

    .. data:: None_ = 0

    .. data:: SFP_10G_SR = 1

    .. data:: SFP_10G_LR = 2

    .. data:: SFP_10G_LRM = 3

    .. data:: SFP_1G_SX = 4

    .. data:: SFP_1G_LX = 5

    .. data:: SFP_1000Base_T = 6

    .. data:: SFP_40G_SR4 = 7

    .. data:: SFP_40G_LR4 = 8

    .. data:: Unsupported = 9

    """

    None_ = Enum.YLeaf(0, "None")

    SFP_10G_SR = Enum.YLeaf(1, "SFP-10G-SR")

    SFP_10G_LR = Enum.YLeaf(2, "SFP-10G-LR")

    SFP_10G_LRM = Enum.YLeaf(3, "SFP-10G-LRM")

    SFP_1G_SX = Enum.YLeaf(4, "SFP-1G-SX")

    SFP_1G_LX = Enum.YLeaf(5, "SFP-1G-LX")

    SFP_1000Base_T = Enum.YLeaf(6, "SFP-1000Base-T")

    SFP_40G_SR4 = Enum.YLeaf(7, "SFP-40G-SR4")

    SFP_40G_LR4 = Enum.YLeaf(8, "SFP-40G-LR4")

    Unsupported = Enum.YLeaf(9, "Unsupported")


class EsdmaSwitchTypeEnum(Enum):
    """
    EsdmaSwitchTypeEnum (Enum Class)

    The list of Ethernet switch types

    .. data:: RP_SW = 0

    .. data:: SC_SW = 1

    .. data:: LC_SW = 2

    .. data:: F_SW0 = 3

    .. data:: F_SW1 = 4

    .. data:: FC_SW = 5

    .. data:: EOBC_SW = 6

    .. data:: EPC_SW = 7

    .. data:: CB_SW = 8

    .. data:: Unknown = 9

    .. data:: RP_SW1 = 10

    """

    RP_SW = Enum.YLeaf(0, "RP-SW")

    SC_SW = Enum.YLeaf(1, "SC-SW")

    LC_SW = Enum.YLeaf(2, "LC-SW")

    F_SW0 = Enum.YLeaf(3, "F-SW0")

    F_SW1 = Enum.YLeaf(4, "F-SW1")

    FC_SW = Enum.YLeaf(5, "FC-SW")

    EOBC_SW = Enum.YLeaf(6, "EOBC-SW")

    EPC_SW = Enum.YLeaf(7, "EPC-SW")

    CB_SW = Enum.YLeaf(8, "CB-SW")

    Unknown = Enum.YLeaf(9, "Unknown")

    RP_SW1 = Enum.YLeaf(10, "RP-SW1")


class EsdmaSwitchYesNoEnum(Enum):
    """
    EsdmaSwitchYesNoEnum (Enum Class)

    .. data:: Yes = 0

    .. data:: No = 1

    """

    Yes = Enum.YLeaf(0, "Yes")

    No = Enum.YLeaf(1, "No")


class EsdmaTrunkMemberStatus(Enum):
    """
    EsdmaTrunkMemberStatus (Enum Class)

    .. data:: Disabled = 0

    .. data:: Enabled = 1

    .. data:: Y_ = 2

    """

    Disabled = Enum.YLeaf(0, "Disabled")

    Enabled = Enum.YLeaf(1, "Enabled")

    Y_ = Enum.YLeaf(2, "-")


class MlapEpType(Enum):
    """
    MlapEpType (Enum Class)

    .. data:: Unknown = 0

    .. data:: RP = 1

    .. data:: SC = 2

    .. data:: FC = 3

    .. data:: LC = 4

    .. data:: F_SW = 5

    .. data:: CB = 6

    """

    Unknown = Enum.YLeaf(0, "Unknown")

    RP = Enum.YLeaf(1, "RP")

    SC = Enum.YLeaf(2, "SC")

    FC = Enum.YLeaf(3, "FC")

    LC = Enum.YLeaf(4, "LC")

    F_SW = Enum.YLeaf(5, "F-SW")

    CB = Enum.YLeaf(6, "CB")


class MlapProtocolEnum(Enum):
    """
    MlapProtocolEnum (Enum Class)

    The types of MLAP protocol

    .. data:: Internal = 0

    .. data:: External = 1

    """

    Internal = Enum.YLeaf(0, "Internal")

    External = Enum.YLeaf(1, "External")


class MlapStateEnum(Enum):
    """
    MlapStateEnum (Enum Class)

    The set of enumerated values that MLAP uses to manage a port's protocol state

    .. data:: Y_ = 0

    .. data:: Down = 1

    .. data:: Up = 2

    .. data:: Admin_Down = 3

    .. data:: Do_Not_Use = 4

    .. data:: Invalid = 5

    .. data:: Active = 6

    .. data:: Standby = 7

    .. data:: Rem_Managed = 8

    """

    Y_ = Enum.YLeaf(0, "-")

    Down = Enum.YLeaf(1, "Down")

    Up = Enum.YLeaf(2, "Up")

    Admin_Down = Enum.YLeaf(3, "Admin Down")

    Do_Not_Use = Enum.YLeaf(4, "Do Not Use")

    Invalid = Enum.YLeaf(5, "Invalid")

    Active = Enum.YLeaf(6, "Active")

    Standby = Enum.YLeaf(7, "Standby")

    Rem_Managed = Enum.YLeaf(8, "Rem Managed")


class MlapTraceVerbosity(Enum):
    """
    MlapTraceVerbosity (Enum Class)

    .. data:: Off = 0

    .. data:: Low = 1

    .. data:: Medium = 2

    .. data:: High = 3

    """

    Off = Enum.YLeaf(0, "Off")

    Low = Enum.YLeaf(1, "Low")

    Medium = Enum.YLeaf(2, "Medium")

    High = Enum.YLeaf(3, "High")


class SwitchActionTypeEnum(Enum):
    """
    SwitchActionTypeEnum (Enum Class)

    .. data:: Y_ = 0

    .. data:: Translate = 1

    .. data:: Remove_Outer = 2

    .. data:: Add_Outer = 3

    .. data:: Drop = 4

    .. data:: Forward = 5

    .. data:: Unknown = 6

    """

    Y_ = Enum.YLeaf(0, "-")

    Translate = Enum.YLeaf(1, "Translate")

    Remove_Outer = Enum.YLeaf(2, "Remove Outer")

    Add_Outer = Enum.YLeaf(3, "Add Outer")

    Drop = Enum.YLeaf(4, "Drop")

    Forward = Enum.YLeaf(5, "Forward")

    Unknown = Enum.YLeaf(6, "Unknown")


class SwitchDataDirectionEnum(Enum):
    """
    SwitchDataDirectionEnum (Enum Class)

    Switch data direction

    .. data:: Y_ = 0

    .. data:: Both = 1

    .. data:: Rx = 2

    .. data:: Tx = 3

    .. data:: Unknown = 4

    .. data:: Invalid = 5

    """

    Y_ = Enum.YLeaf(0, "-")

    Both = Enum.YLeaf(1, "Both")

    Rx = Enum.YLeaf(2, "Rx")

    Tx = Enum.YLeaf(3, "Tx")

    Unknown = Enum.YLeaf(4, "Unknown")

    Invalid = Enum.YLeaf(5, "Invalid")


class SwitchForwardingState(Enum):
    """
    SwitchForwardingState (Enum Class)

    The set of switch port forwarding states

    .. data:: Unknown = 0

    .. data:: Y_ = 1

    .. data:: Disabled = 2

    .. data:: Blocking = 3

    .. data:: Learning = 4

    .. data:: Forwarding = 5

    """

    Unknown = Enum.YLeaf(0, "Unknown")

    Y_ = Enum.YLeaf(1, "-")

    Disabled = Enum.YLeaf(2, "Disabled")

    Blocking = Enum.YLeaf(3, "Blocking")

    Learning = Enum.YLeaf(4, "Learning")

    Forwarding = Enum.YLeaf(5, "Forwarding")


class SwitchMatchTypeEnum(Enum):
    """
    SwitchMatchTypeEnum (Enum Class)

    .. data:: Y_ = 0

    .. data:: Any = 1

    .. data:: Tagged = 2

    .. data:: Untagged = 3

    .. data:: Unknown = 4

    """

    Y_ = Enum.YLeaf(0, "-")

    Any = Enum.YLeaf(1, "Any")

    Tagged = Enum.YLeaf(2, "Tagged")

    Untagged = Enum.YLeaf(3, "Untagged")

    Unknown = Enum.YLeaf(4, "Unknown")


class SwitchTableTypeEnum(Enum):
    """
    SwitchTableTypeEnum (Enum Class)

    .. data:: Y_ = 0

    .. data:: Port = 1

    .. data:: VLAN = 2

    .. data:: TCAM = 3

    .. data:: Unknown = 4

    """

    Y_ = Enum.YLeaf(0, "-")

    Port = Enum.YLeaf(1, "Port")

    VLAN = Enum.YLeaf(2, "VLAN")

    TCAM = Enum.YLeaf(3, "TCAM")

    Unknown = Enum.YLeaf(4, "Unknown")



