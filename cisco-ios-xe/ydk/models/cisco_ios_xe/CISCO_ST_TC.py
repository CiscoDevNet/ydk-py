""" CISCO_ST_TC 

This module defines textual conventions used in
Storage Area Network technology specific mibs.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class FcaddresstypeEnum(Enum):
    """
    FcaddresstypeEnum

    Denotes if a Fibre Channel Address is

    a World Wide Name (WWN) or a Fibre

    Channel Address ID (FCID).

    wwn(1) \- address is WWN.

    fcid(2) \- address is FCID.

    .. data:: wwn = 1

    .. data:: fcid = 2

    """

    wwn = 1

    fcid = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_ST_TC as meta
        return meta._meta_table['FcaddresstypeEnum']


class FcifservicestatetypeEnum(Enum):
    """
    FcifservicestatetypeEnum

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

    inService = 1

    outOfService = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_ST_TC as meta
        return meta._meta_table['FcifservicestatetypeEnum']


class FcifsfpdiagleveltypeEnum(Enum):
    """
    FcifsfpdiagleveltypeEnum

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

    unknown = 1

    normal = 2

    lowWarning = 3

    lowAlarm = 4

    highWarning = 5

    highAlarm = 6


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_ST_TC as meta
        return meta._meta_table['FcifsfpdiagleveltypeEnum']


class FcifspeedEnum(Enum):
    """
    FcifspeedEnum

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

    auto = 1

    oneG = 2

    twoG = 3

    fourG = 4

    autoMaxTwoG = 5

    eightG = 6

    autoMaxFourG = 7

    tenG = 8

    autoMaxEightG = 9

    sixteenG = 10

    autoMaxSixteenG = 11


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_ST_TC as meta
        return meta._meta_table['FcifspeedEnum']


class FcportmoduletypesEnum(Enum):
    """
    FcportmoduletypesEnum

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

    unknown = 1

    other = 2

    gbic = 3

    embedded = 4

    glm = 5

    gbicWithSerialID = 6

    gbicWithoutSerialID = 7

    sfpWithSerialID = 8

    sfpWithoutSerialID = 9

    xfp = 10

    x2Short = 11

    x2Medium = 12

    x2Tall = 13

    xpakShort = 14

    xpakMedium = 15

    xpakTall = 16

    xenpak = 17

    sfpDwdm = 18

    qsfp = 19

    x2Dwdm = 20


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_ST_TC as meta
        return meta._meta_table['FcportmoduletypesEnum']


class FcporttxtypesEnum(Enum):
    """
    FcporttxtypesEnum

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

    unknown = 1

    longWaveLaser = 2

    shortWaveLaser = 3

    longWaveLaserCostReduced = 4

    electrical = 5

    tenGigBaseSr = 6

    tenGigBaseLr = 7

    tenGigBaseEr = 8

    tenGigBaseLx4 = 9

    tenGigBaseSw = 10

    tenGigBaseLw = 11

    tenGigBaseEw = 12


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_ST_TC as meta
        return meta._meta_table['FcporttxtypesEnum']


class FcporttypesEnum(Enum):
    """
    FcporttypesEnum

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

    auto = 1

    fPort = 2

    flPort = 3

    ePort = 4

    bPort = 5

    fxPort = 6

    sdPort = 7

    tlPort = 8

    nPort = 9

    nlPort = 10

    nxPort = 11

    tePort = 12

    fvPort = 13

    portOperDown = 14

    stPort = 15

    npPort = 16

    tfPort = 17

    tnpPort = 18


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_ST_TC as meta
        return meta._meta_table['FcporttypesEnum']


class InterfaceopermodeEnum(Enum):
    """
    InterfaceopermodeEnum

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

    auto = 1

    fPort = 2

    flPort = 3

    ePort = 4

    bPort = 5

    fxPort = 6

    sdPort = 7

    tlPort = 8

    nPort = 9

    nlPort = 10

    nxPort = 11

    tePort = 12

    fvPort = 13

    portOperDown = 14

    stPort = 15

    mgmtPort = 16

    ipsPort = 17

    evPort = 18

    npPort = 19

    tfPort = 20

    tnpPort = 21


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_ST_TC as meta
        return meta._meta_table['InterfaceopermodeEnum']


class Fcclassofservices(FixedBitsDict):
    """
    Fcclassofservices

    Represents the class of service capability of an
    NxPort or FxPort.
    Keys are:- class6 , class3 , class2 , classF , class1 , class5 , class4

    """

    def __init__(self):
        self._dictionary = { 
            'class6':False,
            'class3':False,
            'class2':False,
            'classF':False,
            'class1':False,
            'class5':False,
            'class4':False,
        }
        self._pos_map = { 
            'class6':6,
            'class3':3,
            'class2':2,
            'classF':0,
            'class1':1,
            'class5':5,
            'class4':4,
        }


