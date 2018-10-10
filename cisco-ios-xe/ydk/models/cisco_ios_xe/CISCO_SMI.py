""" CISCO_SMI 

The Structure of Management Information for the
Cisco enterprise.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error

from ydk.models.ietf.ietf_yang_smiv2 import ObjectIdentity



class CiscoChipSetSaint2(ObjectIdentity):
    """
    The identity of the Rev 2 SAINT ethernet chipset
    manufactured for cisco by LSI Logic.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", pref="CISCO-SMI", tag="CISCO-SMI:ciscoChipSetSaint2"):
        super(CiscoChipSetSaint2, self).__init__(ns, pref, tag)


class CiscoTDomainClns(ObjectIdentity):
    """
    The CLNS transport domain.  The corresponding transport
    address is of type CiscoTAddressOSI.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", pref="CISCO-SMI", tag="CISCO-SMI:ciscoTDomainClns"):
        super(CiscoTDomainClns, self).__init__(ns, pref, tag)


class CiscoProxy(ObjectIdentity):
    """
    ciscoProxy OBJECT IDENTIFIERS are used to uniquely name
    party mib records created to proxy for SNMPv1.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", pref="CISCO-SMI", tag="CISCO-SMI:ciscoProxy"):
        super(CiscoProxy, self).__init__(ns, pref, tag)


class CiscoTDomainCons(ObjectIdentity):
    """
    The CONS transport domain.  The corresponding transport
    address is of type CiscoTAddressOSI.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", pref="CISCO-SMI", tag="CISCO-SMI:ciscoTDomainCons"):
        super(CiscoTDomainCons, self).__init__(ns, pref, tag)


class CiscoPolicyAuto(ObjectIdentity):
    """
    ciscoPolicyAuto is the root of the Cisco\-assigned
    OID subtree for OIDs which are automatically assigned
    for use in Policy Management.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", pref="CISCO-SMI", tag="CISCO-SMI:ciscoPolicyAuto"):
        super(CiscoPolicyAuto, self).__init__(ns, pref, tag)


class CiscoTDomainTcpIpv6(ObjectIdentity):
    """
    The TCP over IPv6 transport domain.  The corresponding
    transport address is of type CiscoTAddressIPv6 for global IPv6
    addresses and CiscoTAddressIPv6s for scoped IPv6 addresses.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", pref="CISCO-SMI", tag="CISCO-SMI:ciscoTDomainTcpIpv6"):
        super(CiscoTDomainTcpIpv6, self).__init__(ns, pref, tag)


class Cisco2505RptrGroup(ObjectIdentity):
    """
    The authoritative identity of the Cisco 2505 repeater
    port group.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", pref="CISCO-SMI", tag="CISCO-SMI:cisco2505RptrGroup"):
        super(Cisco2505RptrGroup, self).__init__(ns, pref, tag)


class CiscoTDomainUdpIpv6(ObjectIdentity):
    """
    The UDP over IPv6 transport domain.  The corresponding
    transport address is of type CiscoTAddressIPv6 for global IPv6
    addresses and CiscoTAddressIPv6s for scoped IPv6 addresses.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", pref="CISCO-SMI", tag="CISCO-SMI:ciscoTDomainUdpIpv6"):
        super(CiscoTDomainUdpIpv6, self).__init__(ns, pref, tag)


class CiscoTDomainUdpIpv4(ObjectIdentity):
    """
    The UDP over IPv4 transport domain.  The corresponding
    transport address is of type CiscoTAddressIPv4.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", pref="CISCO-SMI", tag="CISCO-SMI:ciscoTDomainUdpIpv4"):
        super(CiscoTDomainUdpIpv4, self).__init__(ns, pref, tag)


class CiscoPIB(ObjectIdentity):
    """
    ciscoPIB is the root of the Cisco\-assigned OID
    subtree for assignment to PIB (Policy Information
    Base) modules.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", pref="CISCO-SMI", tag="CISCO-SMI:ciscoPIB"):
        super(CiscoPIB, self).__init__(ns, pref, tag)


class CiscoExperiment(ObjectIdentity):
    """
    ciscoExperiment provides a root object identifier
    from which experimental mibs may be temporarily
    based.  mibs are typicially based here if they
    fall in one of two categories
    1) are IETF work\-in\-process mibs which have not
    been assigned a permanent object identifier by
    the IANA.
    2) are cisco work\-in\-process which has not been
    assigned a permanent object identifier by the
    cisco assigned number authority, typicially because
    the mib is not ready for deployment.
    
    NOTE WELL\:  support for mibs in the ciscoExperiment
    subtree will be deleted when a permanent object
    identifier assignment is made.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", pref="CISCO-SMI", tag="CISCO-SMI:ciscoExperiment"):
        super(CiscoExperiment, self).__init__(ns, pref, tag)


class CiscoMgmt(ObjectIdentity):
    """
    ciscoMgmt is the main subtree for new mib development.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", pref="CISCO-SMI", tag="CISCO-SMI:ciscoMgmt"):
        super(CiscoMgmt, self).__init__(ns, pref, tag)


class CiscoCibProvGroup(ObjectIdentity):
    """
    ciscoCibStoreGroup is the root of the Cisco\-assigned OID
    subtree for assignment to MIB modules describing managed
    objects contributing to the Configuration Information Base
    (CIB).
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", pref="CISCO-SMI", tag="CISCO-SMI:ciscoCibProvGroup"):
        super(CiscoCibProvGroup, self).__init__(ns, pref, tag)


class CiscoRptrGroupObjectID(ObjectIdentity):
    """
    ciscoRptrGroupObjectID OBJECT IDENTIFIERS are used to
    uniquely identify groups of repeater ports for use by the
    SNMP\-REPEATER\-MIB (RFC 1516) rptrGroupObjectID object.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", pref="CISCO-SMI", tag="CISCO-SMI:ciscoRptrGroupObjectID"):
        super(CiscoRptrGroupObjectID, self).__init__(ns, pref, tag)


class CiscoDomains(ObjectIdentity):
    """
    ciscoDomains provides a root object identifier from which
    different transport mapping values may be assigned.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", pref="CISCO-SMI", tag="CISCO-SMI:ciscoDomains"):
        super(CiscoDomains, self).__init__(ns, pref, tag)


class CiscoPibToMib(ObjectIdentity):
    """
    ciscoPibToMib is the root of the Cisco\-assigned
    OID subtree for MIBs which are algorithmically
    generated/translated from Cisco PIBs with OIDs
    assigned under the ciscoPIB subtree.
    These generated MIBs allow management
    entities (other the current Policy Server) to
    read the downloaded policy.  By convention, for PIB
    'ciscoPIB.x', the generated MIB shall have the
    name 'ciscoPibToMib.x'.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", pref="CISCO-SMI", tag="CISCO-SMI:ciscoPibToMib"):
        super(CiscoPibToMib, self).__init__(ns, pref, tag)


class CiscoTDomainIpx(ObjectIdentity):
    """
    The IPX transport domain.  The corresponding transport
    address is of type CiscoTAddressIPX.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", pref="CISCO-SMI", tag="CISCO-SMI:ciscoTDomainIpx"):
        super(CiscoTDomainIpx, self).__init__(ns, pref, tag)


class CiscoTDomainSctpIpv4(ObjectIdentity):
    """
    The SCTP over IPv4 transport domain.  The corresponding
    transport address is of type CiscoTAddressIPv4.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", pref="CISCO-SMI", tag="CISCO-SMI:ciscoTDomainSctpIpv4"):
        super(CiscoTDomainSctpIpv4, self).__init__(ns, pref, tag)


class CiscoUnknownRptrGroup(ObjectIdentity):
    """
    The identity of an unknown repeater port group.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", pref="CISCO-SMI", tag="CISCO-SMI:ciscoUnknownRptrGroup"):
        super(CiscoUnknownRptrGroup, self).__init__(ns, pref, tag)


class CiscoModules(ObjectIdentity):
    """
    ciscoModules provides a root object identifier
    from which MODULE\-IDENTITY values may be assigned.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", pref="CISCO-SMI", tag="CISCO-SMI:ciscoModules"):
        super(CiscoModules, self).__init__(ns, pref, tag)


class Lightstream(ObjectIdentity):
    """
    subtree reserved for use by Lightstream
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", pref="CISCO-SMI", tag="CISCO-SMI:lightstream"):
        super(Lightstream, self).__init__(ns, pref, tag)


class CiscoAdmin(ObjectIdentity):
    """
    ciscoAdmin is reserved for administratively assigned
    OBJECT IDENTIFIERS, i.e. those not associated with MIB
    objects
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", pref="CISCO-SMI", tag="CISCO-SMI:ciscoAdmin"):
        super(CiscoAdmin, self).__init__(ns, pref, tag)


class CiscoTDomainLocal(ObjectIdentity):
    """
    The Posix Local IPC transport domain. The corresponding
    transport address is of type CiscoTAddressLocal.  The Posix
    Local IPC transport domain incorporates the well known UNIX
    domain sockets.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", pref="CISCO-SMI", tag="CISCO-SMI:ciscoTDomainLocal"):
        super(CiscoTDomainLocal, self).__init__(ns, pref, tag)


class CiscoTDomainDdp(ObjectIdentity):
    """
    The DDP transport domain.  The corresponding transport
    address is of type CiscoTAddressNBP.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", pref="CISCO-SMI", tag="CISCO-SMI:ciscoTDomainDdp"):
        super(CiscoTDomainDdp, self).__init__(ns, pref, tag)


class Cisco2507RptrGroup(ObjectIdentity):
    """
    The authoritative identity of the Cisco 2507 repeater
    port group.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", pref="CISCO-SMI", tag="CISCO-SMI:cisco2507RptrGroup"):
        super(Cisco2507RptrGroup, self).__init__(ns, pref, tag)


class CiscoChipSetSaint3(ObjectIdentity):
    """
    The identity of the Rev 3 SAINT ethernet chipset
    manufactured for cisco by Plessey.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", pref="CISCO-SMI", tag="CISCO-SMI:ciscoChipSetSaint3"):
        super(CiscoChipSetSaint3, self).__init__(ns, pref, tag)


class CiscoChipSetSaint1(ObjectIdentity):
    """
    The identity of the Rev 1 SAINT ethernet chipset
    manufactured for cisco by LSI Logic.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", pref="CISCO-SMI", tag="CISCO-SMI:ciscoChipSetSaint1"):
        super(CiscoChipSetSaint1, self).__init__(ns, pref, tag)


class Temporary(ObjectIdentity):
    """
    Subtree beneath which pre\-10.2 experiments were
    placed.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", pref="CISCO-SMI", tag="CISCO-SMI:temporary"):
        super(Temporary, self).__init__(ns, pref, tag)


class Workgroup(ObjectIdentity):
    """
    subtree reserved for use by the Workgroup Business Unit
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", pref="CISCO-SMI", tag="CISCO-SMI:workgroup"):
        super(Workgroup, self).__init__(ns, pref, tag)


class CiscoChipSetSaint4(ObjectIdentity):
    """
    The identity of the Rev 4 SAINT ethernet chipset
    manufactured for cisco by Mitsubishi.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", pref="CISCO-SMI", tag="CISCO-SMI:ciscoChipSetSaint4"):
        super(CiscoChipSetSaint4, self).__init__(ns, pref, tag)


class Ciscoworks(ObjectIdentity):
    """
    ciscoworks provides a root object identifier beneath
    which mibs applicable to the CiscoWorks family of network
    management products are defined.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", pref="CISCO-SMI", tag="CISCO-SMI:ciscoworks"):
        super(Ciscoworks, self).__init__(ns, pref, tag)


class Pakmon(ObjectIdentity):
    """
    reserved for pakmon
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", pref="CISCO-SMI", tag="CISCO-SMI:pakmon"):
        super(Pakmon, self).__init__(ns, pref, tag)


class CiscoWsx5020RptrGroup(ObjectIdentity):
    """
    The authoritative identity of the wsx5020 repeater
    port group.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", pref="CISCO-SMI", tag="CISCO-SMI:ciscoWsx5020RptrGroup"):
        super(CiscoWsx5020RptrGroup, self).__init__(ns, pref, tag)


class CiscoAgentCapability(ObjectIdentity):
    """
    ciscoAgentCapability provides a root object identifier
    from which AGENT\-CAPABILITIES values may be assigned.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", pref="CISCO-SMI", tag="CISCO-SMI:ciscoAgentCapability"):
        super(CiscoAgentCapability, self).__init__(ns, pref, tag)


class CiscoPartnerProducts(ObjectIdentity):
    """
    ciscoPartnerProducts is the root OBJECT IDENTIFIER from
    which partner sysObjectID values may be assigned. Such 
    sysObjectID values are composed of the ciscoPartnerProducts
    prefix, followed by a single identifier that is unique for 
    each partner, followed by the value of sysObjectID of the
    Cisco product from which partner product is derived.  Note
    that the chassisPartner MIB object defines the value of the
    identifier assigned to each partner.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", pref="CISCO-SMI", tag="CISCO-SMI:ciscoPartnerProducts"):
        super(CiscoPartnerProducts, self).__init__(ns, pref, tag)


class CiscoCibMmiGroup(ObjectIdentity):
    """
    ciscoCibMmiGroup is the root of the Cisco\-assigned OID
    subtree for assignment to MIB modules describing managed
    objects supporting the Modem Management Interface (MMI),
    the interface that facilitates CPE automatic configuration.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", pref="CISCO-SMI", tag="CISCO-SMI:ciscoCibMmiGroup"):
        super(CiscoCibMmiGroup, self).__init__(ns, pref, tag)


class CiscoProducts(ObjectIdentity):
    """
    ciscoProducts is the root OBJECT IDENTIFIER from
    which sysObjectID values are assigned.  Actual
    values are defined in CISCO\-PRODUCTS\-MIB.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", pref="CISCO-SMI", tag="CISCO-SMI:ciscoProducts"):
        super(CiscoProducts, self).__init__(ns, pref, tag)


class CiscoPKI(ObjectIdentity):
    """
    ciscoPKI is the root of cisco\-assigned OID subtree for PKI
    Certificate Policies and Certificate Extensions.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", pref="CISCO-SMI", tag="CISCO-SMI:ciscoPKI"):
        super(CiscoPKI, self).__init__(ns, pref, tag)


class Cisco2516RptrGroup(ObjectIdentity):
    """
    The authoritative identity of the Cisco 2516 repeater
    port group.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", pref="CISCO-SMI", tag="CISCO-SMI:cisco2516RptrGroup"):
        super(Cisco2516RptrGroup, self).__init__(ns, pref, tag)


class CiscoConfig(ObjectIdentity):
    """
    ciscoConfig is the main subtree for configuration mibs.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", pref="CISCO-SMI", tag="CISCO-SMI:ciscoConfig"):
        super(CiscoConfig, self).__init__(ns, pref, tag)


class CiscoChipSets(ObjectIdentity):
    """
    Numerous media\-specific MIBS have an object, defined as
    an OBJECT IDENTIFIER, which is the identity of the chipset
    realizing the interface.  Cisco\-specific chipsets have their 
    OBJECT IDENTIFIERS assigned under this subtree.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", pref="CISCO-SMI", tag="CISCO-SMI:ciscoChipSets"):
        super(CiscoChipSets, self).__init__(ns, pref, tag)


class OtherEnterprises(ObjectIdentity):
    """
    otherEnterprises provides a root object identifier
    from which mibs produced by other companies may be
    placed.  mibs produced by other enterprises are
    typicially implemented with the object identifiers
    as defined in the mib, but if the mib is deemed to
    be uncontrolled, we may reroot the mib at this
    subtree in order to have a controlled version.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", pref="CISCO-SMI", tag="CISCO-SMI:otherEnterprises"):
        super(OtherEnterprises, self).__init__(ns, pref, tag)


class CiscoCIB(ObjectIdentity):
    """
    ciscoCIB is the root of the Cisco\-assigned OID subtree for
    assignment to MIB modules describing managed objects that
    part of the CPE automatic configuration framework.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", pref="CISCO-SMI", tag="CISCO-SMI:ciscoCIB"):
        super(CiscoCIB, self).__init__(ns, pref, tag)


class Local(ObjectIdentity):
    """
    Subtree beneath which pre\-10.2 MIBS were built.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", pref="CISCO-SMI", tag="CISCO-SMI:local"):
        super(Local, self).__init__(ns, pref, tag)


class CiscoPolicy(ObjectIdentity):
    """
    ciscoPolicy is the root of the Cisco\-assigned OID
    subtree for use with Policy Management.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", pref="CISCO-SMI", tag="CISCO-SMI:ciscoPolicy"):
        super(CiscoPolicy, self).__init__(ns, pref, tag)


class CiscoTDomainSctpIpv6(ObjectIdentity):
    """
    The SCTP over IPv6 transport domain.  The corresponding
    transport address is of type CiscoTAddressIPv6 for global IPv6
    addresses and CiscoTAddressIPv6s for scoped IPv6 addresses.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", pref="CISCO-SMI", tag="CISCO-SMI:ciscoTDomainSctpIpv6"):
        super(CiscoTDomainSctpIpv6, self).__init__(ns, pref, tag)


class Newport(ObjectIdentity):
    """
    subtree reserved for use by the former Newport Systems
    Solutions, now a portion of the Access Business Unit.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", pref="CISCO-SMI", tag="CISCO-SMI:newport"):
        super(Newport, self).__init__(ns, pref, tag)


class CiscoSB(ObjectIdentity):
    """
    ciscoSB provides root Object Identifier for Management
    Information Base for products of Cisco Small Business.
    This includes products rebranded from linksys aquisition.
    MIB numbers under this root are managed and controlled
    by ciscosb\_mib@cisco.com.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", pref="CISCO-SMI", tag="CISCO-SMI:ciscoSB"):
        super(CiscoSB, self).__init__(ns, pref, tag)


class CiscoTDomainTcpIpv4(ObjectIdentity):
    """
    The TCP over IPv4 transport domain.  The corresponding
    transport address is of type CiscoTAddressIPv4.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", pref="CISCO-SMI", tag="CISCO-SMI:ciscoTDomainTcpIpv4"):
        super(CiscoTDomainTcpIpv4, self).__init__(ns, pref, tag)


class CiscoSMB(ObjectIdentity):
    """
    ciscoSMB provides root Object Identifier for Management
    Information Base for products of Cisco built for Small and 
    Medium Business market.The MIB numbers under this root are 
    managed and controlled by ciscosmb\_mib@cisco.com
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", pref="CISCO-SMI", tag="CISCO-SMI:ciscoSMB"):
        super(CiscoSMB, self).__init__(ns, pref, tag)


