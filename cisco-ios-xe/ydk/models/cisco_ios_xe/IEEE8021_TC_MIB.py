""" IEEE8021_TC_MIB 

Textual conventions used throughout the various IEEE 802.1 MIB
modules.

Unless otherwise indicated, the references in this MIB
module are to IEEE 802.1Q\-2005 as amended by IEEE 802.1ad,
IEEE 802.1ak, IEEE 802.1ag and IEEE 802.1ah.

Copyright (C) IEEE.
This version of this MIB module is part of IEEE802.1Q;
see the draft itself for full legal notices.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class Ieee8021BridgeporttypeEnum(Enum):
    """
    Ieee8021BridgeporttypeEnum

    A port type.  The possible port types are\:

    customerVlanPort(2) \- Indicates a port is a C\-tag

        aware port of an enterprise VLAN aware bridge.

    providerNetworkPort(3) \- Indicates a port is an S\-tag

        aware port of a Provider Bridge or Backbone Edge

        Bridge used for connections within a PBN or PBBN.

    customerNetworkPort(4) \- Indicates a port is an S\-tag

        aware port of a Provider Bridge or Backbone Edge

        Bridge used for connections to the exterior of a

        PBN or PBBN.

    customerEdgePort(5) \- Indicates a port is a C\-tag

        aware port of a Provider Bridge used for connections

        to the exterior of a PBN or PBBN.

    customerBackbonePort(6) \- Indicates a port is a I\-tag

        aware port of a Backbone Edge Bridge's B\-component.

    virtualInstancePort(7) \- Indicates a port is a virtual

        S\-tag aware port within a Backbone Edge Bridge's

        I\-component which is responsible for handling

        S\-tagged traffic for a specific backbone service

        instance.

    dBridgePort(8) \- Indicates a port is a VLAN\-unaware

        member of an 802.1D bridge.

    .. data:: none = 1

    .. data:: customerVlanPort = 2

    .. data:: providerNetworkPort = 3

    .. data:: customerNetworkPort = 4

    .. data:: customerEdgePort = 5

    .. data:: customerBackbonePort = 6

    .. data:: virtualInstancePort = 7

    .. data:: dBridgePort = 8

    """

    none = 1

    customerVlanPort = 2

    providerNetworkPort = 3

    customerNetworkPort = 4

    customerEdgePort = 5

    customerBackbonePort = 6

    virtualInstancePort = 7

    dBridgePort = 8


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _IEEE8021_TC_MIB as meta
        return meta._meta_table['Ieee8021BridgeporttypeEnum']


class Ieee8021PortacceptableframetypesEnum(Enum):
    """
    Ieee8021PortacceptableframetypesEnum

    Acceptable frame types on a port.

    .. data:: admitAll = 1

    .. data:: admitUntaggedAndPriority = 2

    .. data:: admitTagged = 3

    """

    admitAll = 1

    admitUntaggedAndPriority = 2

    admitTagged = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _IEEE8021_TC_MIB as meta
        return meta._meta_table['Ieee8021PortacceptableframetypesEnum']


class Ieee8021PrioritycodepointEnum(Enum):
    """
    Ieee8021PrioritycodepointEnum

    Bridge ports may encode or decode the PCP value of the 

    frames that traverse the port. This textual convention 

    names the possible encoding and decoding schemes that

    the port may use.  The priority and drop\_eligible

    parameters are encoded in the Priority Code Point (PCP)

    field of the VLAN tag using the Priority Code Point

    Encoding Table for the Port, and they are decoded from

    the PCP using the Priority Code Point Decoding Table.

    .. data:: codePoint8p0d = 1

    .. data:: codePoint7p1d = 2

    .. data:: codePoint6p2d = 3

    .. data:: codePoint5p3d = 4

    """

    codePoint8p0d = 1

    codePoint7p1d = 2

    codePoint6p2d = 3

    codePoint5p3d = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _IEEE8021_TC_MIB as meta
        return meta._meta_table['Ieee8021PrioritycodepointEnum']


class Ieee8021ServiceselectortypeEnum(Enum):
    """
    Ieee8021ServiceselectortypeEnum

    A value that represents a type (and thereby the format)

    of a IEEE8021ServiceSelectorValue.  The value can be one of

    the following\:

    ieeeReserved(0)   Reserved for definition by IEEE 802.1

                      recommend to not use zero unless

                      absolutely needed.

    vlanId(1)         12\-Bit identifier as described in IEEE802.1Q.

    isid(2)           20\-Bit identifier as described in IEEE802.1ah.

    ieeeReserved(xx)  Reserved for definition by IEEE 802.1

                      xx values can be [3..7].

    To support future extensions, the IEEE8021ServiceSelectorType

    textual convention SHOULD NOT be sub\-typed in object type

    definitions.  It MAY be sub\-typed in compliance statements in

    order to require only a subset of these address types for a

    compliant implementation.

    Implementations MUST ensure that IEEE8021ServiceSelectorType

    objects and any dependent objects (e.g.,

    IEEE8021ServiceSelectorValue objects) are consistent.  An

    inconsistentValue error MUST be generated if an attempt to

    change an IEEE8021ServiceSelectorType object would, for

    example, lead to an undefined IEEE8021ServiceSelectorValue value.

    .. data:: vlanId = 1

    .. data:: isid = 2

    """

    vlanId = 1

    isid = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _IEEE8021_TC_MIB as meta
        return meta._meta_table['Ieee8021ServiceselectortypeEnum']


class Ieee8021Pbbingressegress(FixedBitsDict):
    """
    Ieee8021Pbbingressegress

    A 2 bit selector which determines if frames on this VIP may
    ingress to the PBBN but not egress the PBBN, egress to the
    PBBN but not ingress the PBBN, or both ingress and egress
    the PBBN.
    Keys are:- egress , ingress

    """

    def __init__(self):
        self._dictionary = { 
            'egress':False,
            'ingress':False,
        }
        self._pos_map = { 
            'egress':1,
            'ingress':0,
        }


