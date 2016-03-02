""" CISCO_ST_TC 

This module defines textual conventions used in
Storage Area Network technology specific mibs.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class FcAddressType_Enum(Enum):
    """
    FcAddressType_Enum

    Denotes if a Fibre Channel Address is
    a World Wide Name (WWN) or a Fibre
    Channel Address ID (FCID).
    wwn(1) \- address is WWN.
    fcid(2) \- address is FCID.

    """

    WWN = 1

    FCID = 2


    @staticmethod
    def _meta_info():
        from ydk.models.st._meta import _CISCO_ST_TC as meta
        return meta._meta_table['FcAddressType_Enum']


class FcIfServiceStateType_Enum(Enum):
    """
    FcIfServiceStateType_Enum

    Represents the service state of a Fibre Channel
    interface. Following are the meanings of the 
    enumerated values\:
    
    inService    (1) \- interface is in service and is
                  allowed to become operational.
    outOfService (2) \- interface is removed from service 
                  and is not allowed to become 
                  operational.

    """

    INSERVICE = 1

    OUTOFSERVICE = 2


    @staticmethod
    def _meta_info():
        from ydk.models.st._meta import _CISCO_ST_TC as meta
        return meta._meta_table['FcIfServiceStateType_Enum']


class FcIfSfpDiagLevelType_Enum(Enum):
    """
    FcIfSfpDiagLevelType_Enum

    Represents the severity level of the SFP
    diagnostic information of an interface for 
    temperature, voltage, current, optical 
    transmit and receive power.

    """

    UNKNOWN = 1

    NORMAL = 2

    LOWWARNING = 3

    LOWALARM = 4

    HIGHWARNING = 5

    HIGHALARM = 6


    @staticmethod
    def _meta_info():
        from ydk.models.st._meta import _CISCO_ST_TC as meta
        return meta._meta_table['FcIfSfpDiagLevelType_Enum']


class FcIfSpeed_Enum(Enum):
    """
    FcIfSpeed_Enum

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

    """

    AUTO = 1

    ONEG = 2

    TWOG = 3

    FOURG = 4

    AUTOMAXTWOG = 5

    EIGHTG = 6

    AUTOMAXFOURG = 7

    TENG = 8

    AUTOMAXEIGHTG = 9

    SIXTEENG = 10

    AUTOMAXSIXTEENG = 11


    @staticmethod
    def _meta_info():
        from ydk.models.st._meta import _CISCO_ST_TC as meta
        return meta._meta_table['FcIfSpeed_Enum']


class FcPortModuleTypes_Enum(Enum):
    """
    FcPortModuleTypes_Enum

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

    """

    UNKNOWN = 1

    OTHER = 2

    GBIC = 3

    EMBEDDED = 4

    GLM = 5

    GBICWITHSERIALID = 6

    GBICWITHOUTSERIALID = 7

    SFPWITHSERIALID = 8

    SFPWITHOUTSERIALID = 9

    XFP = 10

    X2SHORT = 11

    X2MEDIUM = 12

    X2TALL = 13

    XPAKSHORT = 14

    XPAKMEDIUM = 15

    XPAKTALL = 16

    XENPAK = 17

    SFPDWDM = 18

    QSFP = 19

    X2DWDM = 20


    @staticmethod
    def _meta_info():
        from ydk.models.st._meta import _CISCO_ST_TC as meta
        return meta._meta_table['FcPortModuleTypes_Enum']


class FcPortTxTypes_Enum(Enum):
    """
    FcPortTxTypes_Enum

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

    """

    UNKNOWN = 1

    LONGWAVELASER = 2

    SHORTWAVELASER = 3

    LONGWAVELASERCOSTREDUCED = 4

    ELECTRICAL = 5

    TENGIGBASESR = 6

    TENGIGBASELR = 7

    TENGIGBASEER = 8

    TENGIGBASELX4 = 9

    TENGIGBASESW = 10

    TENGIGBASELW = 11

    TENGIGBASEEW = 12


    @staticmethod
    def _meta_info():
        from ydk.models.st._meta import _CISCO_ST_TC as meta
        return meta._meta_table['FcPortTxTypes_Enum']


class FcPortTypes_Enum(Enum):
    """
    FcPortTypes_Enum

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

    """

    AUTO = 1

    FPORT = 2

    FLPORT = 3

    EPORT = 4

    BPORT = 5

    FXPORT = 6

    SDPORT = 7

    TLPORT = 8

    NPORT = 9

    NLPORT = 10

    NXPORT = 11

    TEPORT = 12

    FVPORT = 13

    PORTOPERDOWN = 14

    STPORT = 15

    NPPORT = 16

    TFPORT = 17

    TNPPORT = 18


    @staticmethod
    def _meta_info():
        from ydk.models.st._meta import _CISCO_ST_TC as meta
        return meta._meta_table['FcPortTypes_Enum']


class InterfaceOperMode_Enum(Enum):
    """
    InterfaceOperMode_Enum

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

    """

    AUTO = 1

    FPORT = 2

    FLPORT = 3

    EPORT = 4

    BPORT = 5

    FXPORT = 6

    SDPORT = 7

    TLPORT = 8

    NPORT = 9

    NLPORT = 10

    NXPORT = 11

    TEPORT = 12

    FVPORT = 13

    PORTOPERDOWN = 14

    STPORT = 15

    MGMTPORT = 16

    IPSPORT = 17

    EVPORT = 18

    NPPORT = 19

    TFPORT = 20

    TNPPORT = 21


    @staticmethod
    def _meta_info():
        from ydk.models.st._meta import _CISCO_ST_TC as meta
        return meta._meta_table['InterfaceOperMode_Enum']


class FcClassOfServices_Bits(FixedBitsDict):
    """
    FcClassOfServices_Bits

    Represents the class of service capability of an
    NxPort or FxPort.
    Keys are:- classF , class6 , class4 , class5 , class2 , class3 , class1

    """

    def __init__(self):
        self._dictionary = { 
            'classF':False,
            'class6':False,
            'class4':False,
            'class5':False,
            'class2':False,
            'class3':False,
            'class1':False,
        }
        self._pos_map = { 
            'classF':0,
            'class6':6,
            'class4':4,
            'class5':5,
            'class2':2,
            'class3':3,
            'class1':1,
        }


