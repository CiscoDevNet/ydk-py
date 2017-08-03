""" CISCO_IETF_PW_TC_MIB 

This MIB Module provides Textual Conventions 
and OBJECT\-IDENTITY Objects to be used PW services.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Cpwoperstatus(Enum):
    """
    Cpwoperstatus

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

    up = Enum.YLeaf(1, "up")

    down = Enum.YLeaf(2, "down")

    testing = Enum.YLeaf(3, "testing")

    unknown = Enum.YLeaf(4, "unknown")

    dormant = Enum.YLeaf(5, "dormant")

    notPresent = Enum.YLeaf(6, "notPresent")

    lowerLayerDown = Enum.YLeaf(7, "lowerLayerDown")


class Cpwvctype(Enum):
    """
    Cpwvctype

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

    other = Enum.YLeaf(0, "other")

    frameRelay = Enum.YLeaf(1, "frameRelay")

    atmAal5Vcc = Enum.YLeaf(2, "atmAal5Vcc")

    atmTransparent = Enum.YLeaf(3, "atmTransparent")

    ethernetVLAN = Enum.YLeaf(4, "ethernetVLAN")

    ethernet = Enum.YLeaf(5, "ethernet")

    hdlc = Enum.YLeaf(6, "hdlc")

    ppp = Enum.YLeaf(7, "ppp")

    cep = Enum.YLeaf(8, "cep")

    atmVccCell = Enum.YLeaf(9, "atmVccCell")

    atmVpcCell = Enum.YLeaf(10, "atmVpcCell")

    ethernetVPLS = Enum.YLeaf(11, "ethernetVPLS")

    e1Satop = Enum.YLeaf(12, "e1Satop")

    t1Satop = Enum.YLeaf(13, "t1Satop")

    e3Satop = Enum.YLeaf(14, "e3Satop")

    t3Satop = Enum.YLeaf(15, "t3Satop")

    basicCesPsn = Enum.YLeaf(16, "basicCesPsn")

    basicTdmIp = Enum.YLeaf(17, "basicTdmIp")

    tdmCasCesPsn = Enum.YLeaf(18, "tdmCasCesPsn")

    tdmCasTdmIp = Enum.YLeaf(19, "tdmCasTdmIp")



