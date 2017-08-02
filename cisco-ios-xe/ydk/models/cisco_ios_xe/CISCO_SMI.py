""" CISCO_SMI 

The Structure of Management Information for the
Cisco enterprise.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Ciscounknownrptrgroup(Identity):
    """
    The identity of an unknown repeater port group.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        super(Ciscounknownrptrgroup, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:ciscoUnknownRptrGroup")


class Ciscotdomainudpipv4(Identity):
    """
    The UDP over IPv4 transport domain.  The corresponding
    transport address is of type CiscoTAddressIPv4.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        super(Ciscotdomainudpipv4, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:ciscoTDomainUdpIpv4")


class Ciscotdomainsctpipv6(Identity):
    """
    The SCTP over IPv6 transport domain.  The corresponding
    transport address is of type CiscoTAddressIPv6 for global IPv6
    addresses and CiscoTAddressIPv6s for scoped IPv6 addresses.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        super(Ciscotdomainsctpipv6, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:ciscoTDomainSctpIpv6")


class Ciscotdomainipx(Identity):
    """
    The IPX transport domain.  The corresponding transport
    address is of type CiscoTAddressIPX.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        super(Ciscotdomainipx, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:ciscoTDomainIpx")


class Ciscochipsetsaint2(Identity):
    """
    The identity of the Rev 2 SAINT ethernet chipset
    manufactured for cisco by LSI Logic.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        super(Ciscochipsetsaint2, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:ciscoChipSetSaint2")


class Newport(Identity):
    """
    subtree reserved for use by the former Newport Systems
    Solutions, now a portion of the Access Business Unit.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        super(Newport, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:newport")


class Ciscotdomainlocal(Identity):
    """
    The Posix Local IPC transport domain. The corresponding
    transport address is of type CiscoTAddressLocal.  The Posix
    Local IPC transport domain incorporates the well known UNIX
    domain sockets.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        super(Ciscotdomainlocal, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:ciscoTDomainLocal")


class Ciscopibtomib(Identity):
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
        super(Ciscopibtomib, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:ciscoPibToMib")


class Lightstream(Identity):
    """
    subtree reserved for use by Lightstream
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        super(Lightstream, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:lightstream")


class Ciscochipsetsaint3(Identity):
    """
    The identity of the Rev 3 SAINT ethernet chipset
    manufactured for cisco by Plessey.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        super(Ciscochipsetsaint3, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:ciscoChipSetSaint3")


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


class Ciscoproxy(Identity):
    """
    ciscoProxy OBJECT IDENTIFIERS are used to uniquely name
    party mib records created to proxy for SNMPv1.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        super(Ciscoproxy, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:ciscoProxy")


class Ciscotdomainclns(Identity):
    """
    The CLNS transport domain.  The corresponding transport
    address is of type CiscoTAddressOSI.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        super(Ciscotdomainclns, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:ciscoTDomainClns")


class Ciscotdomainudpipv6(Identity):
    """
    The UDP over IPv6 transport domain.  The corresponding
    transport address is of type CiscoTAddressIPv6 for global IPv6
    addresses and CiscoTAddressIPv6s for scoped IPv6 addresses.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        super(Ciscotdomainudpipv6, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:ciscoTDomainUdpIpv6")


class Ciscowsx5020Rptrgroup(Identity):
    """
    The authoritative identity of the wsx5020 repeater
    port group.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        super(Ciscowsx5020Rptrgroup, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:ciscoWsx5020RptrGroup")


class Otherenterprises(Identity):
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
        super(Otherenterprises, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:otherEnterprises")


class Ciscotdomainsctpipv4(Identity):
    """
    The SCTP over IPv4 transport domain.  The corresponding
    transport address is of type CiscoTAddressIPv4.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        super(Ciscotdomainsctpipv4, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:ciscoTDomainSctpIpv4")


class Ciscocibmmigroup(Identity):
    """
    ciscoCibMmiGroup is the root of the Cisco\-assigned OID
    subtree for assignment to MIB modules describing managed
    objects supporting the Modem Management Interface (MMI),
    the interface that facilitates CPE automatic configuration.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        super(Ciscocibmmigroup, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:ciscoCibMmiGroup")


class Ciscopolicy(Identity):
    """
    ciscoPolicy is the root of the Cisco\-assigned OID
    subtree for use with Policy Management.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        super(Ciscopolicy, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:ciscoPolicy")


class Pakmon(Identity):
    """
    reserved for pakmon
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        super(Pakmon, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:pakmon")


class Ciscoagentcapability(Identity):
    """
    ciscoAgentCapability provides a root object identifier
    from which AGENT\-CAPABILITIES values may be assigned.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        super(Ciscoagentcapability, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:ciscoAgentCapability")


class Ciscopki(Identity):
    """
    ciscoPKI is the root of cisco\-assigned OID subtree for PKI
    Certificate Policies and Certificate Extensions.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        super(Ciscopki, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:ciscoPKI")


class Cisco2505Rptrgroup(Identity):
    """
    The authoritative identity of the Cisco 2505 repeater
    port group.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        super(Cisco2505Rptrgroup, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:cisco2505RptrGroup")


class Ciscoproducts(Identity):
    """
    ciscoProducts is the root OBJECT IDENTIFIER from
    which sysObjectID values are assigned.  Actual
    values are defined in CISCO\-PRODUCTS\-MIB.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        super(Ciscoproducts, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:ciscoProducts")


class Ciscoadmin(Identity):
    """
    ciscoAdmin is reserved for administratively assigned
    OBJECT IDENTIFIERS, i.e. those not associated with MIB
    objects
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        super(Ciscoadmin, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:ciscoAdmin")


class Ciscotdomainddp(Identity):
    """
    The DDP transport domain.  The corresponding transport
    address is of type CiscoTAddressNBP.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        super(Ciscotdomainddp, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:ciscoTDomainDdp")


class Ciscotdomaintcpipv6(Identity):
    """
    The TCP over IPv6 transport domain.  The corresponding
    transport address is of type CiscoTAddressIPv6 for global IPv6
    addresses and CiscoTAddressIPv6s for scoped IPv6 addresses.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        super(Ciscotdomaintcpipv6, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:ciscoTDomainTcpIpv6")


class Ciscosmb(Identity):
    """
    ciscoSMB provides root Object Identifier for Management
    Information Base for products of Cisco built for Small and 
    Medium Business market.The MIB numbers under this root are 
    managed and controlled by ciscosmb\_mib@cisco.com
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        super(Ciscosmb, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:ciscoSMB")


class Ciscodomains(Identity):
    """
    ciscoDomains provides a root object identifier from which
    different transport mapping values may be assigned.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        super(Ciscodomains, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:ciscoDomains")


class Ciscochipsetsaint1(Identity):
    """
    The identity of the Rev 1 SAINT ethernet chipset
    manufactured for cisco by LSI Logic.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        super(Ciscochipsetsaint1, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:ciscoChipSetSaint1")


class Ciscoconfig(Identity):
    """
    ciscoConfig is the main subtree for configuration mibs.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        super(Ciscoconfig, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:ciscoConfig")


class Ciscotdomaincons(Identity):
    """
    The CONS transport domain.  The corresponding transport
    address is of type CiscoTAddressOSI.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        super(Ciscotdomaincons, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:ciscoTDomainCons")


class Ciscocibprovgroup(Identity):
    """
    ciscoCibStoreGroup is the root of the Cisco\-assigned OID
    subtree for assignment to MIB modules describing managed
    objects contributing to the Configuration Information Base
    (CIB).
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        super(Ciscocibprovgroup, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:ciscoCibProvGroup")


class Ciscocib(Identity):
    """
    ciscoCIB is the root of the Cisco\-assigned OID subtree for
    assignment to MIB modules describing managed objects that
    part of the CPE automatic configuration framework.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        super(Ciscocib, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:ciscoCIB")


class Ciscopib(Identity):
    """
    ciscoPIB is the root of the Cisco\-assigned OID
    subtree for assignment to PIB (Policy Information
    Base) modules.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        super(Ciscopib, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:ciscoPIB")


class Workgroup(Identity):
    """
    subtree reserved for use by the Workgroup Business Unit
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        super(Workgroup, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:workgroup")


class Ciscoexperiment(Identity):
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
        super(Ciscoexperiment, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:ciscoExperiment")


class Ciscochipsets(Identity):
    """
    Numerous media\-specific MIBS have an object, defined as
    an OBJECT IDENTIFIER, which is the identity of the chipset
    realizing the interface.  Cisco\-specific chipsets have their 
    OBJECT IDENTIFIERS assigned under this subtree.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        super(Ciscochipsets, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:ciscoChipSets")


class Local(Identity):
    """
    Subtree beneath which pre\-10.2 MIBS were built.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        super(Local, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:local")


class Ciscomgmt(Identity):
    """
    ciscoMgmt is the main subtree for new mib development.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        super(Ciscomgmt, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:ciscoMgmt")


class Temporary(Identity):
    """
    Subtree beneath which pre\-10.2 experiments were
    placed.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        super(Temporary, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:temporary")


class Cisco2507Rptrgroup(Identity):
    """
    The authoritative identity of the Cisco 2507 repeater
    port group.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        super(Cisco2507Rptrgroup, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:cisco2507RptrGroup")


class Cisco2516Rptrgroup(Identity):
    """
    The authoritative identity of the Cisco 2516 repeater
    port group.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        super(Cisco2516Rptrgroup, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:cisco2516RptrGroup")


class Ciscotdomaintcpipv4(Identity):
    """
    The TCP over IPv4 transport domain.  The corresponding
    transport address is of type CiscoTAddressIPv4.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        super(Ciscotdomaintcpipv4, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:ciscoTDomainTcpIpv4")


class Ciscochipsetsaint4(Identity):
    """
    The identity of the Rev 4 SAINT ethernet chipset
    manufactured for cisco by Mitsubishi.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        super(Ciscochipsetsaint4, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:ciscoChipSetSaint4")


class Ciscorptrgroupobjectid(Identity):
    """
    ciscoRptrGroupObjectID OBJECT IDENTIFIERS are used to
    uniquely identify groups of repeater ports for use by the
    SNMP\-REPEATER\-MIB (RFC 1516) rptrGroupObjectID object.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        super(Ciscorptrgroupobjectid, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:ciscoRptrGroupObjectID")


class Ciscosb(Identity):
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
        super(Ciscosb, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:ciscoSB")


class Ciscomodules(Identity):
    """
    ciscoModules provides a root object identifier
    from which MODULE\-IDENTITY values may be assigned.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        super(Ciscomodules, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:ciscoModules")


class Ciscopartnerproducts(Identity):
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
        super(Ciscopartnerproducts, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:ciscoPartnerProducts")


class Ciscopolicyauto(Identity):
    """
    ciscoPolicyAuto is the root of the Cisco\-assigned
    OID subtree for OIDs which are automatically assigned
    for use in Policy Management.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        super(Ciscopolicyauto, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SMI", "CISCO-SMI", "CISCO-SMI:ciscoPolicyAuto")


