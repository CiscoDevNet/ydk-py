""" MPLS_TC_STD_MIB 

Copyright (C) The Internet Society (2004). The
initial version of this MIB module was published
in RFC 3811. For full legal notices see the RFC
itself or see\:
http\://www.ietf.org/copyrights/ianamib.html

This MIB module defines TEXTUAL\-CONVENTIONs
for concepts used in Multiprotocol Label
Switching (MPLS) networks.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class MplsLabelDistributionMethod_Enum(Enum):
    """
    MplsLabelDistributionMethod_Enum

    The label distribution method which is also called
    the label advertisement mode [RFC3036].
    Each interface on an LSR is configured to operate
    in either Downstream Unsolicited or Downstream
    on Demand.

    """

    DOWNSTREAMONDEMAND = 1

    DOWNSTREAMUNSOLICITED = 2


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _MPLS_TC_STD_MIB as meta
        return meta._meta_table['MplsLabelDistributionMethod_Enum']


class MplsLdpLabelType_Enum(Enum):
    """
    MplsLdpLabelType_Enum

    The Layer 2 label types which are defined for MPLS
    LDP and/or CR\-LDP are generic(1), atm(2), or
    frameRelay(3).

    """

    GENERIC = 1

    ATM = 2

    FRAMERELAY = 3


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _MPLS_TC_STD_MIB as meta
        return meta._meta_table['MplsLdpLabelType_Enum']


class MplsLspType_Enum(Enum):
    """
    MplsLspType_Enum

    Types of Label Switch Paths (LSPs)
    on a Label Switching Router (LSR) or a
    Label Edge Router (LER) are\:
    
       unknown(1)         \-\- if the LSP is not known
                             to be one of the following.
    
       terminatingLsp(2)  \-\- if the LSP terminates
                             on the LSR/LER, then this
                             is an egressing LSP
                             which ends on the LSR/LER,
    
       originatingLsp(3)  \-\- if the LSP originates
                             from this LSR/LER, then
                             this is an ingressing LSP
                             which is the head\-end of
                             the LSP,
    
    crossConnectingLsp(4) \-\- if the LSP ingresses
                             and egresses on the LSR,
                             then it is
                             cross\-connecting on that
                             LSR.

    """

    UNKNOWN = 1

    TERMINATINGLSP = 2

    ORIGINATINGLSP = 3

    CROSSCONNECTINGLSP = 4


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _MPLS_TC_STD_MIB as meta
        return meta._meta_table['MplsLspType_Enum']


class MplsOwner_Enum(Enum):
    """
    MplsOwner_Enum

    This object indicates the local network
    management subsystem that originally created
    the object(s) in question.  The values of
    this enumeration are defined as follows\:
    
    unknown(1) \- the local network management
    subsystem cannot discern which
    component created the object.
    
    other(2) \- the local network management
    subsystem is able to discern which component
    created the object, but the component is not
    listed within the following choices,
    e.g., command line interface (cli).
    
    snmp(3) \- The Simple Network Management Protocol
    was used to configure this object initially.
    
    ldp(4) \- The Label Distribution Protocol was
    used to configure this object initially.
    
    crldp(5) \- The Constraint\-Based Label Distribution
    Protocol was used to configure this object
    initially.
    
    rsvpTe(6) \- The Resource Reservation Protocol was
    used to configure this object initially.
    
    policyAgent(7) \- A policy agent (perhaps in
    combination with one of the above protocols) was
    used to configure this object initially.
    
    An object created by any of the above choices
    MAY be modified or destroyed by the same or a
    different choice.

    """

    UNKNOWN = 1

    OTHER = 2

    SNMP = 3

    LDP = 4

    CRLDP = 5

    RSVPTE = 6

    POLICYAGENT = 7


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _MPLS_TC_STD_MIB as meta
        return meta._meta_table['MplsOwner_Enum']


class MplsRetentionMode_Enum(Enum):
    """
    MplsRetentionMode_Enum

    The label retention mode which specifies whether
    an LSR maintains a label binding for a FEC
    learned from a neighbor that is not its next hop
    for the FEC.
    
    If the value is conservative(1) then advertised
    label mappings are retained only if they will be
    used to forward packets, i.e., if label came from
    a valid next hop.
    
    If the value is liberal(2) then all advertised
    label mappings are retained whether they are from
    a valid next hop or not.

    """

    CONSERVATIVE = 1

    LIBERAL = 2


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _MPLS_TC_STD_MIB as meta
        return meta._meta_table['MplsRetentionMode_Enum']


class TeHopAddressType_Enum(Enum):
    """
    TeHopAddressType_Enum

    A value that represents a type of address for a
    Traffic Engineered (TE) Tunnel hop.
    
    unknown(0)   An unknown address type.  This value
                 MUST be used if the value of the
                 corresponding TeHopAddress object is a
                 zero\-length string.  It may also be
                 used to indicate a TeHopAddress which
                 is not in one of the formats defined
                 below.
    
    ipv4(1)      An IPv4 network address as defined by
                 the InetAddressIPv4 TEXTUAL\-CONVENTION
                 [RFC3291].
    
    ipv6(2)      A global IPv6 address as defined by
                 the InetAddressIPv6 TEXTUAL\-CONVENTION
                 [RFC3291].
    
    asnumber(3)  An Autonomous System (AS) number as
                 defined by the TeHopAddressAS
                 TEXTUAL\-CONVENTION.
    
    unnum(4)     An unnumbered interface index as
                 defined by the TeHopAddressUnnum
                 TEXTUAL\-CONVENTION.
    
    lspid(5)     An LSP ID for TE Tunnels
                 (RFC3212) as defined by the
                 MplsLSPID TEXTUAL\-CONVENTION.
    
    Each definition of a concrete TeHopAddressType
    value must be accompanied by a definition
    of a TEXTUAL\-CONVENTION for use with that
    TeHopAddress.
    
    To support future extensions, the TeHopAddressType
    TEXTUAL\-CONVENTION SHOULD NOT be sub\-typed in
    object type definitions.  It MAY be sub\-typed in
    compliance statements in order to require only a
    subset of these address types for a compliant
    implementation.
    
    Implementations must ensure that TeHopAddressType
    objects and any dependent objects
    (e.g., TeHopAddress objects) are consistent.
    An inconsistentValue error must be generated
    if an attempt to change a TeHopAddressType
    object would, for example, lead to an
    undefined TeHopAddress value that is
    not defined herein.  In particular,
    TeHopAddressType/TeHopAddress pairs
    must be changed together if the address
    type changes (e.g., from ipv6(2) to ipv4(1)).

    """

    UNKNOWN = 0

    IPV4 = 1

    IPV6 = 2

    ASNUMBER = 3

    UNNUM = 4

    LSPID = 5


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _MPLS_TC_STD_MIB as meta
        return meta._meta_table['TeHopAddressType_Enum']



