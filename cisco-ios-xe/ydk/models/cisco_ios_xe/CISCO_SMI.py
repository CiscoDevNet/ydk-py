""" CISCO_SMI 

The Structure of Management Information for the
Cisco enterprise.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CiscoChipSetSaint2(Identity):
    """
    The identity of the Rev 2 SAINT ethernet chipset
    manufactured for cisco by LSI Logic.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        super(CiscoChipSetSaint2, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:ciscoChipSetSaint2")


class CiscoTDomainClns(Identity):
    """
    The CLNS transport domain.  The corresponding transport
    address is of type CiscoTAddressOSI.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        super(CiscoTDomainClns, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:ciscoTDomainClns")


class CiscoProxy(Identity):
    """
    ciscoProxy OBJECT IDENTIFIERS are used to uniquely name
    party mib records created to proxy for SNMPv1.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        super(CiscoProxy, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:ciscoProxy")


class CiscoTDomainCons(Identity):
    """
    The CONS transport domain.  The corresponding transport
    address is of type CiscoTAddressOSI.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        super(CiscoTDomainCons, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:ciscoTDomainCons")


class CiscoPolicyAuto(Identity):
    """
    ciscoPolicyAuto is the root of the Cisco\-assigned
    OID subtree for OIDs which are automatically assigned
    for use in Policy Management.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        super(CiscoPolicyAuto, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:ciscoPolicyAuto")


class CiscoTDomainTcpIpv6(Identity):
    """
    The TCP over IPv6 transport domain.  The corresponding
    transport address is of type CiscoTAddressIPv6 for global IPv6
    addresses and CiscoTAddressIPv6s for scoped IPv6 addresses.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        super(CiscoTDomainTcpIpv6, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:ciscoTDomainTcpIpv6")


class Cisco2505RptrGroup(Identity):
    """
    The authoritative identity of the Cisco 2505 repeater
    port group.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        super(Cisco2505RptrGroup, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:cisco2505RptrGroup")


class CiscoTDomainUdpIpv6(Identity):
    """
    The UDP over IPv6 transport domain.  The corresponding
    transport address is of type CiscoTAddressIPv6 for global IPv6
    addresses and CiscoTAddressIPv6s for scoped IPv6 addresses.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        super(CiscoTDomainUdpIpv6, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:ciscoTDomainUdpIpv6")


class CiscoTDomainUdpIpv4(Identity):
    """
    The UDP over IPv4 transport domain.  The corresponding
    transport address is of type CiscoTAddressIPv4.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        super(CiscoTDomainUdpIpv4, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:ciscoTDomainUdpIpv4")


class CiscoPIB(Identity):
    """
    ciscoPIB is the root of the Cisco\-assigned OID
    subtree for assignment to PIB (Policy Information
    Base) modules.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        super(CiscoPIB, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:ciscoPIB")


class CiscoExperiment(Identity):
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

    def __init__(self):
        super(CiscoExperiment, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:ciscoExperiment")


class CiscoMgmt(Identity):
    """
    ciscoMgmt is the main subtree for new mib development.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        super(CiscoMgmt, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:ciscoMgmt")


class CiscoCibProvGroup(Identity):
    """
    ciscoCibStoreGroup is the root of the Cisco\-assigned OID
    subtree for assignment to MIB modules describing managed
    objects contributing to the Configuration Information Base
    (CIB).
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        super(CiscoCibProvGroup, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:ciscoCibProvGroup")


class CiscoRptrGroupObjectID(Identity):
    """
    ciscoRptrGroupObjectID OBJECT IDENTIFIERS are used to
    uniquely identify groups of repeater ports for use by the
    SNMP\-REPEATER\-MIB (RFC 1516) rptrGroupObjectID object.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        super(CiscoRptrGroupObjectID, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:ciscoRptrGroupObjectID")


class CiscoDomains(Identity):
    """
    ciscoDomains provides a root object identifier from which
    different transport mapping values may be assigned.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        super(CiscoDomains, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:ciscoDomains")


class CiscoPibToMib(Identity):
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

    def __init__(self):
        super(CiscoPibToMib, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:ciscoPibToMib")


class CiscoTDomainIpx(Identity):
    """
    The IPX transport domain.  The corresponding transport
    address is of type CiscoTAddressIPX.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        super(CiscoTDomainIpx, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:ciscoTDomainIpx")


class CiscoTDomainSctpIpv4(Identity):
    """
    The SCTP over IPv4 transport domain.  The corresponding
    transport address is of type CiscoTAddressIPv4.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        super(CiscoTDomainSctpIpv4, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:ciscoTDomainSctpIpv4")


class CiscoUnknownRptrGroup(Identity):
    """
    The identity of an unknown repeater port group.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        super(CiscoUnknownRptrGroup, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:ciscoUnknownRptrGroup")


class CiscoModules(Identity):
    """
    ciscoModules provides a root object identifier
    from which MODULE\-IDENTITY values may be assigned.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        super(CiscoModules, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:ciscoModules")


class Lightstream(Identity):
    """
    subtree reserved for use by Lightstream
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        super(Lightstream, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:lightstream")


class CiscoAdmin(Identity):
    """
    ciscoAdmin is reserved for administratively assigned
    OBJECT IDENTIFIERS, i.e. those not associated with MIB
    objects
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        super(CiscoAdmin, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:ciscoAdmin")


class CiscoTDomainLocal(Identity):
    """
    The Posix Local IPC transport domain. The corresponding
    transport address is of type CiscoTAddressLocal.  The Posix
    Local IPC transport domain incorporates the well known UNIX
    domain sockets.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        super(CiscoTDomainLocal, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:ciscoTDomainLocal")


class CiscoTDomainDdp(Identity):
    """
    The DDP transport domain.  The corresponding transport
    address is of type CiscoTAddressNBP.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        super(CiscoTDomainDdp, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:ciscoTDomainDdp")


class Cisco2507RptrGroup(Identity):
    """
    The authoritative identity of the Cisco 2507 repeater
    port group.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        super(Cisco2507RptrGroup, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:cisco2507RptrGroup")


class CiscoChipSetSaint3(Identity):
    """
    The identity of the Rev 3 SAINT ethernet chipset
    manufactured for cisco by Plessey.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        super(CiscoChipSetSaint3, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:ciscoChipSetSaint3")


class CiscoChipSetSaint1(Identity):
    """
    The identity of the Rev 1 SAINT ethernet chipset
    manufactured for cisco by LSI Logic.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        super(CiscoChipSetSaint1, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:ciscoChipSetSaint1")


class Temporary(Identity):
    """
    Subtree beneath which pre\-10.2 experiments were
    placed.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        super(Temporary, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:temporary")


class Workgroup(Identity):
    """
    subtree reserved for use by the Workgroup Business Unit
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        super(Workgroup, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:workgroup")


class CiscoChipSetSaint4(Identity):
    """
    The identity of the Rev 4 SAINT ethernet chipset
    manufactured for cisco by Mitsubishi.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        super(CiscoChipSetSaint4, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:ciscoChipSetSaint4")


class Ciscoworks(Identity):
    """
    ciscoworks provides a root object identifier beneath
    which mibs applicable to the CiscoWorks family of network
    management products are defined.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        super(Ciscoworks, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:ciscoworks")


class Pakmon(Identity):
    """
    reserved for pakmon
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        super(Pakmon, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:pakmon")


class CiscoWsx5020RptrGroup(Identity):
    """
    The authoritative identity of the wsx5020 repeater
    port group.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        super(CiscoWsx5020RptrGroup, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:ciscoWsx5020RptrGroup")


class CiscoAgentCapability(Identity):
    """
    ciscoAgentCapability provides a root object identifier
    from which AGENT\-CAPABILITIES values may be assigned.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        super(CiscoAgentCapability, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:ciscoAgentCapability")


class CiscoPartnerProducts(Identity):
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

    def __init__(self):
        super(CiscoPartnerProducts, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:ciscoPartnerProducts")


class CiscoCibMmiGroup(Identity):
    """
    ciscoCibMmiGroup is the root of the Cisco\-assigned OID
    subtree for assignment to MIB modules describing managed
    objects supporting the Modem Management Interface (MMI),
    the interface that facilitates CPE automatic configuration.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        super(CiscoCibMmiGroup, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:ciscoCibMmiGroup")


class CiscoProducts(Identity):
    """
    ciscoProducts is the root OBJECT IDENTIFIER from
    which sysObjectID values are assigned.  Actual
    values are defined in CISCO\-PRODUCTS\-MIB.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        super(CiscoProducts, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:ciscoProducts")


class CiscoPKI(Identity):
    """
    ciscoPKI is the root of cisco\-assigned OID subtree for PKI
    Certificate Policies and Certificate Extensions.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        super(CiscoPKI, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:ciscoPKI")


class Cisco2516RptrGroup(Identity):
    """
    The authoritative identity of the Cisco 2516 repeater
    port group.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        super(Cisco2516RptrGroup, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:cisco2516RptrGroup")


class CiscoConfig(Identity):
    """
    ciscoConfig is the main subtree for configuration mibs.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        super(CiscoConfig, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:ciscoConfig")


class CiscoChipSets(Identity):
    """
    Numerous media\-specific MIBS have an object, defined as
    an OBJECT IDENTIFIER, which is the identity of the chipset
    realizing the interface.  Cisco\-specific chipsets have their 
    OBJECT IDENTIFIERS assigned under this subtree.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        super(CiscoChipSets, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:ciscoChipSets")


class OtherEnterprises(Identity):
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

    def __init__(self):
        super(OtherEnterprises, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:otherEnterprises")


class CiscoCIB(Identity):
    """
    ciscoCIB is the root of the Cisco\-assigned OID subtree for
    assignment to MIB modules describing managed objects that
    part of the CPE automatic configuration framework.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        super(CiscoCIB, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:ciscoCIB")


class Local(Identity):
    """
    Subtree beneath which pre\-10.2 MIBS were built.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        super(Local, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:local")


class CiscoPolicy(Identity):
    """
    ciscoPolicy is the root of the Cisco\-assigned OID
    subtree for use with Policy Management.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        super(CiscoPolicy, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:ciscoPolicy")


class CiscoTDomainSctpIpv6(Identity):
    """
    The SCTP over IPv6 transport domain.  The corresponding
    transport address is of type CiscoTAddressIPv6 for global IPv6
    addresses and CiscoTAddressIPv6s for scoped IPv6 addresses.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        super(CiscoTDomainSctpIpv6, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:ciscoTDomainSctpIpv6")


class Newport(Identity):
    """
    subtree reserved for use by the former Newport Systems
    Solutions, now a portion of the Access Business Unit.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        super(Newport, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:newport")


class CiscoSB(Identity):
    """
    ciscoSB provides root Object Identifier for Management
    Information Base for products of Cisco Small Business.
    This includes products rebranded from linksys aquisition.
    MIB numbers under this root are managed and controlled
    by ciscosb\_mib@cisco.com.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        super(CiscoSB, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:ciscoSB")


class CiscoTDomainTcpIpv4(Identity):
    """
    The TCP over IPv4 transport domain.  The corresponding
    transport address is of type CiscoTAddressIPv4.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        super(CiscoTDomainTcpIpv4, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:ciscoTDomainTcpIpv4")


class CiscoSMB(Identity):
    """
    ciscoSMB provides root Object Identifier for Management
    Information Base for products of Cisco built for Small and 
    Medium Business market.The MIB numbers under this root are 
    managed and controlled by ciscosmb\_mib@cisco.com
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        super(CiscoSMB, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:ciscoSMB")


