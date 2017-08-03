""" CISCO_ST_TC 

This module defines textual conventions used in
Storage Area Network technology specific mibs.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Fcaddresstype(Enum):
    """
    Fcaddresstype

    Denotes if a Fibre Channel Address is

    a World Wide Name (WWN) or a Fibre

    Channel Address ID (FCID).

    wwn(1) \- address is WWN.

    fcid(2) \- address is FCID.

    .. data:: wwn = 1

    .. data:: fcid = 2

    """

    wwn = Enum.YLeaf(1, "wwn")

    fcid = Enum.YLeaf(2, "fcid")


class Fcifservicestatetype(Enum):
    """
    Fcifservicestatetype

    Represents the service state of a Fibre Channel

    interface. Following are the meanings of the 

    enumerated values\:

    inService    (1) \- interface is in service and is

                  allowed to become operational.

    outOfService (2) \- interface is removed from service 

                  and is not allowed to become 

                  operational.

    .. data:: inService = 1

    .. data:: outOfService = 2

    """

    inService = Enum.YLeaf(1, "inService")

    outOfService = Enum.YLeaf(2, "outOfService")


class Fcifsfpdiagleveltype(Enum):
    """
    Fcifsfpdiagleveltype

    Represents the severity level of the SFP

    diagnostic information of an interface for 

    temperature, voltage, current, optical 

    transmit and receive power.

    .. data:: unknown = 1

    .. data:: normal = 2

    .. data:: lowWarning = 3

    .. data:: lowAlarm = 4

    .. data:: highWarning = 5

    .. data:: highAlarm = 6

    """

    unknown = Enum.YLeaf(1, "unknown")

    normal = Enum.YLeaf(2, "normal")

    lowWarning = Enum.YLeaf(3, "lowWarning")

    lowAlarm = Enum.YLeaf(4, "lowAlarm")

    highWarning = Enum.YLeaf(5, "highWarning")

    highAlarm = Enum.YLeaf(6, "highAlarm")


class Fcifspeed(Enum):
    """
    Fcifspeed

    Represents the speed of a fibre channel port.

    Following are the meanings of the enumerated values\:

      auto      (1) \- Negotiate to determine the speed 

                      automatically.

      oneG      (2) \- 1Gbit 

      twoG      (3) \- 2Gbit

      fourG     (4) \- 4Gbit 

      autoMaxTwoG (5)  \- Negotiate to determine the 

                         speed automatically upto a 

                         maximum of 2Gbit.

      eightG    (6) \- 8Gbit

      autoMaxFourG (7) \- Negotiate to determine the

                         speed automatically upto a

                         maximum of 4Gbit.          

      tenG      (8) \- 10GBit.

      autoMaxEightG (9) \- Negotiate to determine the

                         speed automatically upto a

                         maximum of 8Gbit.

      sixteenG  (10) \- 16GBit.

      autoMaxSixteenG (11) \- Negotiate to determine the

                         speed automatically upto a

                         maximum of 16Gbit.

    .. data:: auto = 1

    .. data:: oneG = 2

    .. data:: twoG = 3

    .. data:: fourG = 4

    .. data:: autoMaxTwoG = 5

    .. data:: eightG = 6

    .. data:: autoMaxFourG = 7

    .. data:: tenG = 8

    .. data:: autoMaxEightG = 9

    .. data:: sixteenG = 10

    .. data:: autoMaxSixteenG = 11

    """

    auto = Enum.YLeaf(1, "auto")

    oneG = Enum.YLeaf(2, "oneG")

    twoG = Enum.YLeaf(3, "twoG")

    fourG = Enum.YLeaf(4, "fourG")

    autoMaxTwoG = Enum.YLeaf(5, "autoMaxTwoG")

    eightG = Enum.YLeaf(6, "eightG")

    autoMaxFourG = Enum.YLeaf(7, "autoMaxFourG")

    tenG = Enum.YLeaf(8, "tenG")

    autoMaxEightG = Enum.YLeaf(9, "autoMaxEightG")

    sixteenG = Enum.YLeaf(10, "sixteenG")

    autoMaxSixteenG = Enum.YLeaf(11, "autoMaxSixteenG")


class Fcportmoduletypes(Enum):
    """
    Fcportmoduletypes

    Represents module type of the port connector. This

    object refers to the hardware implementation of the port.

    The enums are defined as per FC\-GS\-4 standard.

    unknown             (1) \- unknown

    other               (2) \- other

    gbic                (3) \- gbic (gigabit interface card)

    embedded            (4) \- gbic is part of the line card 

                              and is unremovable

    glm                 (5) \- if its a gigabit link module 

                              (GLM). A GLM has a different 

                              form factor than GBIC. GLM is 

                              not supported by our switch.

    gbicWithSerialID    (6) \- If GBIC serial id can be read

    gbicWithoutSerialID (7) \- If GBIC serial id cannot be read

    sfpWithSerialID     (8) \- If small form factor (SFP) 

                              pluggable GBICs serial id can 

                              be read

    sfpWithoutSerialID  (9) \- If small form factor (SFP) 

                              pluggable GBICs serial id 

                              cannot be read

    The following enums are module types for 10 gigabit small 

    form factor pluggable sfp port connectors.

    xfp                (10) \- xfp 

    x2Short            (11) \- x2 short 

    x2Medium           (12) \- x2 medium

    x2Tall             (13) \- x2 tall

    xpakShort          (14) \- xpak short

    xpakMedium         (15) \- xpak medium

    xpakTall           (16) \- xpak tall

    xenpak             (17) \- xenpak

    sfpDwdm            (18) \- DWDM SFP type

    qsfp               (19) \- Quad small form\-factor (QSFP) 

                                                      pluggable type

    x2Dwdm             (20) \- x2 DWDM

    .

    .. data:: unknown = 1

    .. data:: other = 2

    .. data:: gbic = 3

    .. data:: embedded = 4

    .. data:: glm = 5

    .. data:: gbicWithSerialID = 6

    .. data:: gbicWithoutSerialID = 7

    .. data:: sfpWithSerialID = 8

    .. data:: sfpWithoutSerialID = 9

    .. data:: xfp = 10

    .. data:: x2Short = 11

    .. data:: x2Medium = 12

    .. data:: x2Tall = 13

    .. data:: xpakShort = 14

    .. data:: xpakMedium = 15

    .. data:: xpakTall = 16

    .. data:: xenpak = 17

    .. data:: sfpDwdm = 18

    .. data:: qsfp = 19

    .. data:: x2Dwdm = 20

    """

    unknown = Enum.YLeaf(1, "unknown")

    other = Enum.YLeaf(2, "other")

    gbic = Enum.YLeaf(3, "gbic")

    embedded = Enum.YLeaf(4, "embedded")

    glm = Enum.YLeaf(5, "glm")

    gbicWithSerialID = Enum.YLeaf(6, "gbicWithSerialID")

    gbicWithoutSerialID = Enum.YLeaf(7, "gbicWithoutSerialID")

    sfpWithSerialID = Enum.YLeaf(8, "sfpWithSerialID")

    sfpWithoutSerialID = Enum.YLeaf(9, "sfpWithoutSerialID")

    xfp = Enum.YLeaf(10, "xfp")

    x2Short = Enum.YLeaf(11, "x2Short")

    x2Medium = Enum.YLeaf(12, "x2Medium")

    x2Tall = Enum.YLeaf(13, "x2Tall")

    xpakShort = Enum.YLeaf(14, "xpakShort")

    xpakMedium = Enum.YLeaf(15, "xpakMedium")

    xpakTall = Enum.YLeaf(16, "xpakTall")

    xenpak = Enum.YLeaf(17, "xenpak")

    sfpDwdm = Enum.YLeaf(18, "sfpDwdm")

    qsfp = Enum.YLeaf(19, "qsfp")

    x2Dwdm = Enum.YLeaf(20, "x2Dwdm")


class Fcporttxtypes(Enum):
    """
    Fcporttxtypes

    Represents port transciever technology types.

    unknown (1) \- unknown

    longWaveLaser (2) \- 1550nm laser

    shortWaveLaser (3) \- 850nm laser

    longWaveLaserCostReduced (4) \- 1310nm laser

    electrical (5) \- electrical 

    tenGigBaseSr (6)  \- 10GBASE\-SR 850nm laser

    tenGigBaseLr (7)  \- 10GBASE\-LR 1310nm laser

    tenGigBaseEr (8)  \- 10GBASE\-ER 1550nm laser

    tenGigBaseLx4 (9) \- 10GBASE\-LX4 WWDM 1300nm laser

    tenGigBaseSw (10)  \- 850nm laser

    tenGigBaseLw (11) \- 1310nm laser

    tenGigBaseEw (12) \- 1550nm laser

    .

    .. data:: unknown = 1

    .. data:: longWaveLaser = 2

    .. data:: shortWaveLaser = 3

    .. data:: longWaveLaserCostReduced = 4

    .. data:: electrical = 5

    .. data:: tenGigBaseSr = 6

    .. data:: tenGigBaseLr = 7

    .. data:: tenGigBaseEr = 8

    .. data:: tenGigBaseLx4 = 9

    .. data:: tenGigBaseSw = 10

    .. data:: tenGigBaseLw = 11

    .. data:: tenGigBaseEw = 12

    """

    unknown = Enum.YLeaf(1, "unknown")

    longWaveLaser = Enum.YLeaf(2, "longWaveLaser")

    shortWaveLaser = Enum.YLeaf(3, "shortWaveLaser")

    longWaveLaserCostReduced = Enum.YLeaf(4, "longWaveLaserCostReduced")

    electrical = Enum.YLeaf(5, "electrical")

    tenGigBaseSr = Enum.YLeaf(6, "tenGigBaseSr")

    tenGigBaseLr = Enum.YLeaf(7, "tenGigBaseLr")

    tenGigBaseEr = Enum.YLeaf(8, "tenGigBaseEr")

    tenGigBaseLx4 = Enum.YLeaf(9, "tenGigBaseLx4")

    tenGigBaseSw = Enum.YLeaf(10, "tenGigBaseSw")

    tenGigBaseLw = Enum.YLeaf(11, "tenGigBaseLw")

    tenGigBaseEw = Enum.YLeaf(12, "tenGigBaseEw")


class Fcporttypes(Enum):
    """
    Fcporttypes

    Represents fibre channel port types\:

    auto (1)   \- Mode is determined by port initialization 

                scheme.

    fPort (2)  \- Fibre channel fabric port. 

    flPort (3) \- Fibre channel arbitrated loop port.

    ePort (4)  \- Fabric Expansion port.

    bPort (5)  \- Bridging port.

    fxPort (6) \- This port can only be f\_port or fl\_port.

    sdPort (7) \- SPAN destination port. SD\_ports transmit 

                traffic copied from one or more source ports

                for monitoring purposes.        

    tlPort (8) \- Translation loop port.

    nPort (9)   \- Fibre channel N port.

    nlPort (10) \- Fibre channel NL port.

    nxPort (11) \- This port can only be n\_port or nl\_port.

      \-\- read only port types.

    tePort (12) \- Trunking e\_port.

                 Note\: A port which is administratively set

                 to 'ePort', will operationally have type

                 'tePort' if fcIfOperTrunkMode has the value

                 'trunk'.

    fvPort (13) \- Virtual Port.

    portOperDown (14) \- port operationally down

                        If a port is operationally down, the

                        port mode is unknown. In such cases

                        the operational port mode is shown 

                        as 'portOperDown'. 

    stPort (15) \- SPAN Tunnel destination port.

    npPort (16) \- N Proxy port mode applicable only to N\-port

                  Virtualizer (NPV)

    tfPort (17) \- Trunking fibre channel fabric port.

    tnpPort (18) \- Trunking N Proxy port mode applicable only

                  to N\-port Virtualizer (NPV).

    .. data:: auto = 1

    .. data:: fPort = 2

    .. data:: flPort = 3

    .. data:: ePort = 4

    .. data:: bPort = 5

    .. data:: fxPort = 6

    .. data:: sdPort = 7

    .. data:: tlPort = 8

    .. data:: nPort = 9

    .. data:: nlPort = 10

    .. data:: nxPort = 11

    .. data:: tePort = 12

    .. data:: fvPort = 13

    .. data:: portOperDown = 14

    .. data:: stPort = 15

    .. data:: npPort = 16

    .. data:: tfPort = 17

    .. data:: tnpPort = 18

    """

    auto = Enum.YLeaf(1, "auto")

    fPort = Enum.YLeaf(2, "fPort")

    flPort = Enum.YLeaf(3, "flPort")

    ePort = Enum.YLeaf(4, "ePort")

    bPort = Enum.YLeaf(5, "bPort")

    fxPort = Enum.YLeaf(6, "fxPort")

    sdPort = Enum.YLeaf(7, "sdPort")

    tlPort = Enum.YLeaf(8, "tlPort")

    nPort = Enum.YLeaf(9, "nPort")

    nlPort = Enum.YLeaf(10, "nlPort")

    nxPort = Enum.YLeaf(11, "nxPort")

    tePort = Enum.YLeaf(12, "tePort")

    fvPort = Enum.YLeaf(13, "fvPort")

    portOperDown = Enum.YLeaf(14, "portOperDown")

    stPort = Enum.YLeaf(15, "stPort")

    npPort = Enum.YLeaf(16, "npPort")

    tfPort = Enum.YLeaf(17, "tfPort")

    tnpPort = Enum.YLeaf(18, "tnpPort")


class Interfaceopermode(Enum):
    """
    Interfaceopermode

    Represents the operational mode of an interface

    auto (1) \- Mode is determined by port initialization

               scheme.

    fPort (2) \- Fibre channel fabric port.

    flPort (3) \- Fibre channel arbitrated loop port.

    ePort (4)  \- Fabric Expansion port.

    bPort (5)  \- Bridging port.

    fxPort (6) \- This port can only be f\_port or fl\_port.

    sdPort (7) \- SPAN destination port. SD\_ports transmit

                 traffic copied from one or more source

                 ports for monitoring purposes.

    tlPort (8) \- Translation loop port.

    nPort (9)   \- Fibre channel N port.

    nlPort (10) \- Fibre channel NL port.

    nxPort (11) \- This port can only be n\_port or nl\_port.

    \-\- read only port types.

    tePort (12) \- Trunking e\_port.

              Note\: A port which is administratively set

              to 'ePort', will operationally have type

              'tePort' if fcIfOperTrunkMode has the value

              'trunk'.

    fvPort (13) \- Virtual Port.

    portOperDown (14) \- port operationally down

                      If a port is operationally down, the

                      port mode is unknown. In such cases

                      the operational port mode is shown

                      as 'portOperDown'.

    stPort (15) \- SPAN Tunnel destination port.

    mgmtPort(16) \- Mgmt Port.

    ipsPort(17) \- Ethernet Port.

    evPort(18) \- FCIP tunnels on Ethernet ports.

    npPort (19) \- N Proxy port mode applicable only 

                  to N\-port Virtualizer (NPV).

    tfPort (20) \- Trunking fibre channel fabric port.

    tnpPort (21) \- Trunking N Proxy port mode applicable only

                          to N\-port Virtualizer (NPV).

    .. data:: auto = 1

    .. data:: fPort = 2

    .. data:: flPort = 3

    .. data:: ePort = 4

    .. data:: bPort = 5

    .. data:: fxPort = 6

    .. data:: sdPort = 7

    .. data:: tlPort = 8

    .. data:: nPort = 9

    .. data:: nlPort = 10

    .. data:: nxPort = 11

    .. data:: tePort = 12

    .. data:: fvPort = 13

    .. data:: portOperDown = 14

    .. data:: stPort = 15

    .. data:: mgmtPort = 16

    .. data:: ipsPort = 17

    .. data:: evPort = 18

    .. data:: npPort = 19

    .. data:: tfPort = 20

    .. data:: tnpPort = 21

    """

    auto = Enum.YLeaf(1, "auto")

    fPort = Enum.YLeaf(2, "fPort")

    flPort = Enum.YLeaf(3, "flPort")

    ePort = Enum.YLeaf(4, "ePort")

    bPort = Enum.YLeaf(5, "bPort")

    fxPort = Enum.YLeaf(6, "fxPort")

    sdPort = Enum.YLeaf(7, "sdPort")

    tlPort = Enum.YLeaf(8, "tlPort")

    nPort = Enum.YLeaf(9, "nPort")

    nlPort = Enum.YLeaf(10, "nlPort")

    nxPort = Enum.YLeaf(11, "nxPort")

    tePort = Enum.YLeaf(12, "tePort")

    fvPort = Enum.YLeaf(13, "fvPort")

    portOperDown = Enum.YLeaf(14, "portOperDown")

    stPort = Enum.YLeaf(15, "stPort")

    mgmtPort = Enum.YLeaf(16, "mgmtPort")

    ipsPort = Enum.YLeaf(17, "ipsPort")

    evPort = Enum.YLeaf(18, "evPort")

    npPort = Enum.YLeaf(19, "npPort")

    tfPort = Enum.YLeaf(20, "tfPort")

    tnpPort = Enum.YLeaf(21, "tnpPort")


class Fcclassofservices(Bits):
    """
    Fcclassofservices

    Represents the class of service capability of an
    NxPort or FxPort.
    Keys are:- class6 , class2 , classF , class1 , class5 , class4 , class3

    """

    def __init__(self):
        super(Fcclassofservices, self).__init__()


