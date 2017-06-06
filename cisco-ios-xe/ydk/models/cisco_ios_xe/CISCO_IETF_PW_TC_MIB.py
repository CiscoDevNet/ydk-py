""" CISCO_IETF_PW_TC_MIB 

This MIB Module provides Textual Conventions 
and OBJECT\-IDENTITY Objects to be used PW services.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class CpwoperstatusEnum(Enum):
    """
    CpwoperstatusEnum

    Indicate the operational status of the PW VC. 

    \- up\:             Ready to pass packets.  

    \- down\:           If PW signaling has not yet finished, or 

                      indications available at the service  

                      level indicate that the VC is not  

                      passing packets. 

    \- testing\:        If AdminStatus at the VC level is set to  

                      test. 

    \- dormant\:        The VC is not available because of the 

                      required resources are occupied VC with  

                      higher priority VCs . 

    \- notPresent\:     Some component is missing to accomplish  

                      the set up of the VC. 

    \- lowerLayerDown\: The underlying PSN or outer tunnel is not 

                      in OperStatus 'up'.  

    .. data:: up = 1

    .. data:: down = 2

    .. data:: testing = 3

    .. data:: unknown = 4

    .. data:: dormant = 5

    .. data:: notPresent = 6

    .. data:: lowerLayerDown = 7

    """

    up = 1

    down = 2

    testing = 3

    unknown = 4

    dormant = 5

    notPresent = 6

    lowerLayerDown = 7


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_PW_TC_MIB as meta
        return meta._meta_table['CpwoperstatusEnum']


class CpwvctypeEnum(Enum):
    """
    CpwvctypeEnum

    Indicate the VC type (i.e. the carried service). 

    Note\: the exact set of VC types is yet to be worked  

    out by the WG. 

    .. data:: other = 0

    .. data:: frameRelay = 1

    .. data:: atmAal5Vcc = 2

    .. data:: atmTransparent = 3

    .. data:: ethernetVLAN = 4

    .. data:: ethernet = 5

    .. data:: hdlc = 6

    .. data:: ppp = 7

    .. data:: cep = 8

    .. data:: atmVccCell = 9

    .. data:: atmVpcCell = 10

    .. data:: ethernetVPLS = 11

    .. data:: e1Satop = 12

    .. data:: t1Satop = 13

    .. data:: e3Satop = 14

    .. data:: t3Satop = 15

    .. data:: basicCesPsn = 16

    .. data:: basicTdmIp = 17

    .. data:: tdmCasCesPsn = 18

    .. data:: tdmCasTdmIp = 19

    """

    other = 0

    frameRelay = 1

    atmAal5Vcc = 2

    atmTransparent = 3

    ethernetVLAN = 4

    ethernet = 5

    hdlc = 6

    ppp = 7

    cep = 8

    atmVccCell = 9

    atmVpcCell = 10

    ethernetVPLS = 11

    e1Satop = 12

    t1Satop = 13

    e3Satop = 14

    t3Satop = 15

    basicCesPsn = 16

    basicTdmIp = 17

    tdmCasCesPsn = 18

    tdmCasTdmIp = 19


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_PW_TC_MIB as meta
        return meta._meta_table['CpwvctypeEnum']



