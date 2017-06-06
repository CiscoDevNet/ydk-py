""" CISCO_SMI 

The Structure of Management Information for the
Cisco enterprise.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError


from ydk.models.ietf.ietf_yang_smiv2 import ObjectIdentityIdentity


class CiscocibmmigroupIdentity(ObjectIdentityIdentity):
    """
    ciscoCibMmiGroup is the root of the Cisco\-assigned OID
    subtree for assignment to MIB modules describing managed
    objects supporting the Modem Management Interface (MMI),
    the interface that facilitates CPE automatic configuration.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_SMI as meta
        return meta._meta_table['CiscocibmmigroupIdentity']['meta_info']


class CiscoconfigIdentity(ObjectIdentityIdentity):
    """
    ciscoConfig is the main subtree for configuration mibs.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_SMI as meta
        return meta._meta_table['CiscoconfigIdentity']['meta_info']


class TemporaryIdentity(ObjectIdentityIdentity):
    """
    Subtree beneath which pre\-10.2 experiments were
    placed.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_SMI as meta
        return meta._meta_table['TemporaryIdentity']['meta_info']


class CiscoproductsIdentity(ObjectIdentityIdentity):
    """
    ciscoProducts is the root OBJECT IDENTIFIER from
    which sysObjectID values are assigned.  Actual
    values are defined in CISCO\-PRODUCTS\-MIB.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_SMI as meta
        return meta._meta_table['CiscoproductsIdentity']['meta_info']


class Ciscotdomaintcpipv6Identity(ObjectIdentityIdentity):
    """
    The TCP over IPv6 transport domain.  The corresponding
    transport address is of type CiscoTAddressIPv6 for global IPv6
    addresses and CiscoTAddressIPv6s for scoped IPv6 addresses.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_SMI as meta
        return meta._meta_table['Ciscotdomaintcpipv6Identity']['meta_info']


class CiscotdomainddpIdentity(ObjectIdentityIdentity):
    """
    The DDP transport domain.  The corresponding transport
    address is of type CiscoTAddressNBP.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_SMI as meta
        return meta._meta_table['CiscotdomainddpIdentity']['meta_info']


class Ciscochipsetsaint4Identity(ObjectIdentityIdentity):
    """
    The identity of the Rev 4 SAINT ethernet chipset
    manufactured for cisco by Mitsubishi.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_SMI as meta
        return meta._meta_table['Ciscochipsetsaint4Identity']['meta_info']


class Ciscotdomainsctpipv6Identity(ObjectIdentityIdentity):
    """
    The SCTP over IPv6 transport domain.  The corresponding
    transport address is of type CiscoTAddressIPv6 for global IPv6
    addresses and CiscoTAddressIPv6s for scoped IPv6 addresses.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_SMI as meta
        return meta._meta_table['Ciscotdomainsctpipv6Identity']['meta_info']


class CiscomodulesIdentity(ObjectIdentityIdentity):
    """
    ciscoModules provides a root object identifier
    from which MODULE\-IDENTITY values may be assigned.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_SMI as meta
        return meta._meta_table['CiscomodulesIdentity']['meta_info']


class CiscopartnerproductsIdentity(ObjectIdentityIdentity):
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
        ObjectIdentityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_SMI as meta
        return meta._meta_table['CiscopartnerproductsIdentity']['meta_info']


class CiscomgmtIdentity(ObjectIdentityIdentity):
    """
    ciscoMgmt is the main subtree for new mib development.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_SMI as meta
        return meta._meta_table['CiscomgmtIdentity']['meta_info']


class LightstreamIdentity(ObjectIdentityIdentity):
    """
    subtree reserved for use by Lightstream
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_SMI as meta
        return meta._meta_table['LightstreamIdentity']['meta_info']


class CiscopkiIdentity(ObjectIdentityIdentity):
    """
    ciscoPKI is the root of cisco\-assigned OID subtree for PKI
    Certificate Policies and Certificate Extensions.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_SMI as meta
        return meta._meta_table['CiscopkiIdentity']['meta_info']


class CiscochipsetsIdentity(ObjectIdentityIdentity):
    """
    Numerous media\-specific MIBS have an object, defined as
    an OBJECT IDENTIFIER, which is the identity of the chipset
    realizing the interface.  Cisco\-specific chipsets have their 
    OBJECT IDENTIFIERS assigned under this subtree.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_SMI as meta
        return meta._meta_table['CiscochipsetsIdentity']['meta_info']


class CiscounknownrptrgroupIdentity(ObjectIdentityIdentity):
    """
    The identity of an unknown repeater port group.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_SMI as meta
        return meta._meta_table['CiscounknownrptrgroupIdentity']['meta_info']


class CiscoworksIdentity(ObjectIdentityIdentity):
    """
    ciscoworks provides a root object identifier beneath
    which mibs applicable to the CiscoWorks family of network
    management products are defined.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_SMI as meta
        return meta._meta_table['CiscoworksIdentity']['meta_info']


class CiscoexperimentIdentity(ObjectIdentityIdentity):
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
        ObjectIdentityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_SMI as meta
        return meta._meta_table['CiscoexperimentIdentity']['meta_info']


class NewportIdentity(ObjectIdentityIdentity):
    """
    subtree reserved for use by the former Newport Systems
    Solutions, now a portion of the Access Business Unit.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_SMI as meta
        return meta._meta_table['NewportIdentity']['meta_info']


class Cisco2516RptrgroupIdentity(ObjectIdentityIdentity):
    """
    The authoritative identity of the Cisco 2516 repeater
    port group.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_SMI as meta
        return meta._meta_table['Cisco2516RptrgroupIdentity']['meta_info']


class Ciscotdomainudpipv6Identity(ObjectIdentityIdentity):
    """
    The UDP over IPv6 transport domain.  The corresponding
    transport address is of type CiscoTAddressIPv6 for global IPv6
    addresses and CiscoTAddressIPv6s for scoped IPv6 addresses.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_SMI as meta
        return meta._meta_table['Ciscotdomainudpipv6Identity']['meta_info']


class OtherenterprisesIdentity(ObjectIdentityIdentity):
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
        ObjectIdentityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_SMI as meta
        return meta._meta_table['OtherenterprisesIdentity']['meta_info']


class CiscopibIdentity(ObjectIdentityIdentity):
    """
    ciscoPIB is the root of the Cisco\-assigned OID
    subtree for assignment to PIB (Policy Information
    Base) modules.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_SMI as meta
        return meta._meta_table['CiscopibIdentity']['meta_info']


class CiscotdomainlocalIdentity(ObjectIdentityIdentity):
    """
    The Posix Local IPC transport domain. The corresponding
    transport address is of type CiscoTAddressLocal.  The Posix
    Local IPC transport domain incorporates the well known UNIX
    domain sockets.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_SMI as meta
        return meta._meta_table['CiscotdomainlocalIdentity']['meta_info']


class LocalIdentity(ObjectIdentityIdentity):
    """
    Subtree beneath which pre\-10.2 MIBS were built.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_SMI as meta
        return meta._meta_table['LocalIdentity']['meta_info']


class Cisco2507RptrgroupIdentity(ObjectIdentityIdentity):
    """
    The authoritative identity of the Cisco 2507 repeater
    port group.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_SMI as meta
        return meta._meta_table['Cisco2507RptrgroupIdentity']['meta_info']


class CiscotdomainclnsIdentity(ObjectIdentityIdentity):
    """
    The CLNS transport domain.  The corresponding transport
    address is of type CiscoTAddressOSI.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_SMI as meta
        return meta._meta_table['CiscotdomainclnsIdentity']['meta_info']


class Ciscochipsetsaint2Identity(ObjectIdentityIdentity):
    """
    The identity of the Rev 2 SAINT ethernet chipset
    manufactured for cisco by LSI Logic.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_SMI as meta
        return meta._meta_table['Ciscochipsetsaint2Identity']['meta_info']


class Ciscotdomainsctpipv4Identity(ObjectIdentityIdentity):
    """
    The SCTP over IPv4 transport domain.  The corresponding
    transport address is of type CiscoTAddressIPv4.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_SMI as meta
        return meta._meta_table['Ciscotdomainsctpipv4Identity']['meta_info']


class CiscosmbIdentity(ObjectIdentityIdentity):
    """
    ciscoSMB provides root Object Identifier for Management
    Information Base for products of Cisco built for Small and 
    Medium Business market.The MIB numbers under this root are 
    managed and controlled by ciscosmb\_mib@cisco.com
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_SMI as meta
        return meta._meta_table['CiscosmbIdentity']['meta_info']


class CiscosbIdentity(ObjectIdentityIdentity):
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
        ObjectIdentityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_SMI as meta
        return meta._meta_table['CiscosbIdentity']['meta_info']


class PakmonIdentity(ObjectIdentityIdentity):
    """
    reserved for pakmon
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_SMI as meta
        return meta._meta_table['PakmonIdentity']['meta_info']


class CiscoagentcapabilityIdentity(ObjectIdentityIdentity):
    """
    ciscoAgentCapability provides a root object identifier
    from which AGENT\-CAPABILITIES values may be assigned.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_SMI as meta
        return meta._meta_table['CiscoagentcapabilityIdentity']['meta_info']


class Cisco2505RptrgroupIdentity(ObjectIdentityIdentity):
    """
    The authoritative identity of the Cisco 2505 repeater
    port group.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_SMI as meta
        return meta._meta_table['Cisco2505RptrgroupIdentity']['meta_info']


class CiscopolicyIdentity(ObjectIdentityIdentity):
    """
    ciscoPolicy is the root of the Cisco\-assigned OID
    subtree for use with Policy Management.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_SMI as meta
        return meta._meta_table['CiscopolicyIdentity']['meta_info']


class CiscopibtomibIdentity(ObjectIdentityIdentity):
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
        ObjectIdentityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_SMI as meta
        return meta._meta_table['CiscopibtomibIdentity']['meta_info']


class CiscorptrgroupobjectidIdentity(ObjectIdentityIdentity):
    """
    ciscoRptrGroupObjectID OBJECT IDENTIFIERS are used to
    uniquely identify groups of repeater ports for use by the
    SNMP\-REPEATER\-MIB (RFC 1516) rptrGroupObjectID object.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_SMI as meta
        return meta._meta_table['CiscorptrgroupobjectidIdentity']['meta_info']


class CiscocibprovgroupIdentity(ObjectIdentityIdentity):
    """
    ciscoCibStoreGroup is the root of the Cisco\-assigned OID
    subtree for assignment to MIB modules describing managed
    objects contributing to the Configuration Information Base
    (CIB).
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_SMI as meta
        return meta._meta_table['CiscocibprovgroupIdentity']['meta_info']


class Ciscowsx5020RptrgroupIdentity(ObjectIdentityIdentity):
    """
    The authoritative identity of the wsx5020 repeater
    port group.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_SMI as meta
        return meta._meta_table['Ciscowsx5020RptrgroupIdentity']['meta_info']


class CiscoproxyIdentity(ObjectIdentityIdentity):
    """
    ciscoProxy OBJECT IDENTIFIERS are used to uniquely name
    party mib records created to proxy for SNMPv1.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_SMI as meta
        return meta._meta_table['CiscoproxyIdentity']['meta_info']


class CiscodomainsIdentity(ObjectIdentityIdentity):
    """
    ciscoDomains provides a root object identifier from which
    different transport mapping values may be assigned.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_SMI as meta
        return meta._meta_table['CiscodomainsIdentity']['meta_info']


class CiscoadminIdentity(ObjectIdentityIdentity):
    """
    ciscoAdmin is reserved for administratively assigned
    OBJECT IDENTIFIERS, i.e. those not associated with MIB
    objects
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_SMI as meta
        return meta._meta_table['CiscoadminIdentity']['meta_info']


class Ciscochipsetsaint3Identity(ObjectIdentityIdentity):
    """
    The identity of the Rev 3 SAINT ethernet chipset
    manufactured for cisco by Plessey.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_SMI as meta
        return meta._meta_table['Ciscochipsetsaint3Identity']['meta_info']


class CiscotdomainipxIdentity(ObjectIdentityIdentity):
    """
    The IPX transport domain.  The corresponding transport
    address is of type CiscoTAddressIPX.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_SMI as meta
        return meta._meta_table['CiscotdomainipxIdentity']['meta_info']


class CiscocibIdentity(ObjectIdentityIdentity):
    """
    ciscoCIB is the root of the Cisco\-assigned OID subtree for
    assignment to MIB modules describing managed objects that
    part of the CPE automatic configuration framework.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_SMI as meta
        return meta._meta_table['CiscocibIdentity']['meta_info']


class WorkgroupIdentity(ObjectIdentityIdentity):
    """
    subtree reserved for use by the Workgroup Business Unit
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_SMI as meta
        return meta._meta_table['WorkgroupIdentity']['meta_info']


class Ciscotdomaintcpipv4Identity(ObjectIdentityIdentity):
    """
    The TCP over IPv4 transport domain.  The corresponding
    transport address is of type CiscoTAddressIPv4.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_SMI as meta
        return meta._meta_table['Ciscotdomaintcpipv4Identity']['meta_info']


class Ciscotdomainudpipv4Identity(ObjectIdentityIdentity):
    """
    The UDP over IPv4 transport domain.  The corresponding
    transport address is of type CiscoTAddressIPv4.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_SMI as meta
        return meta._meta_table['Ciscotdomainudpipv4Identity']['meta_info']


class Ciscochipsetsaint1Identity(ObjectIdentityIdentity):
    """
    The identity of the Rev 1 SAINT ethernet chipset
    manufactured for cisco by LSI Logic.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_SMI as meta
        return meta._meta_table['Ciscochipsetsaint1Identity']['meta_info']


class CiscopolicyautoIdentity(ObjectIdentityIdentity):
    """
    ciscoPolicyAuto is the root of the Cisco\-assigned
    OID subtree for OIDs which are automatically assigned
    for use in Policy Management.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_SMI as meta
        return meta._meta_table['CiscopolicyautoIdentity']['meta_info']


class CiscotdomainconsIdentity(ObjectIdentityIdentity):
    """
    The CONS transport domain.  The corresponding transport
    address is of type CiscoTAddressOSI.
    
    

    """

    _prefix = 'CISCO-SMI'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_SMI as meta
        return meta._meta_table['CiscotdomainconsIdentity']['meta_info']


