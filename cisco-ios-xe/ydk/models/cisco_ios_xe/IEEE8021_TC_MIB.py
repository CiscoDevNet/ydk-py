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
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Ieee8021Bridgeporttype(Enum):
    """
    Ieee8021Bridgeporttype

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

    none = Enum.YLeaf(1, "none")

    customerVlanPort = Enum.YLeaf(2, "customerVlanPort")

    providerNetworkPort = Enum.YLeaf(3, "providerNetworkPort")

    customerNetworkPort = Enum.YLeaf(4, "customerNetworkPort")

    customerEdgePort = Enum.YLeaf(5, "customerEdgePort")

    customerBackbonePort = Enum.YLeaf(6, "customerBackbonePort")

    virtualInstancePort = Enum.YLeaf(7, "virtualInstancePort")

    dBridgePort = Enum.YLeaf(8, "dBridgePort")


class Ieee8021Portacceptableframetypes(Enum):
    """
    Ieee8021Portacceptableframetypes

    Acceptable frame types on a port.

    .. data:: admitAll = 1

    .. data:: admitUntaggedAndPriority = 2

    .. data:: admitTagged = 3

    """

    admitAll = Enum.YLeaf(1, "admitAll")

    admitUntaggedAndPriority = Enum.YLeaf(2, "admitUntaggedAndPriority")

    admitTagged = Enum.YLeaf(3, "admitTagged")


class Ieee8021Prioritycodepoint(Enum):
    """
    Ieee8021Prioritycodepoint

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

    codePoint8p0d = Enum.YLeaf(1, "codePoint8p0d")

    codePoint7p1d = Enum.YLeaf(2, "codePoint7p1d")

    codePoint6p2d = Enum.YLeaf(3, "codePoint6p2d")

    codePoint5p3d = Enum.YLeaf(4, "codePoint5p3d")


class Ieee8021Serviceselectortype(Enum):
    """
    Ieee8021Serviceselectortype

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

    vlanId = Enum.YLeaf(1, "vlanId")

    isid = Enum.YLeaf(2, "isid")


class Ieee8021Pbbingressegress(Bits):
    """
    Ieee8021Pbbingressegress

    A 2 bit selector which determines if frames on this VIP may
    ingress to the PBBN but not egress the PBBN, egress to the
    PBBN but not ingress the PBBN, or both ingress and egress
    the PBBN.
    Keys are:- egress , ingress

    """

    def __init__(self):
        super(Ieee8021Pbbingressegress, self).__init__()


