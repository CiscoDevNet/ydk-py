""" CISCO_SMI 

The Structure of Management Information for the
Cisco enterprise.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError


from ydk.models.ietf.ietf_yang_smiv2 import ObjectIdentity_Identity


class Cisco2505RptrGroup_Identity(ObjectIdentity_Identity):
    """
    The authoritative identity of the Cisco 2505 repeater
    port group.
    
    

    """

    _prefix = 'cisco-smi'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentity_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.smi._meta import _CISCO_SMI as meta
        return meta._meta_table['Cisco2505RptrGroup_Identity']['meta_info']


class Cisco2507RptrGroup_Identity(ObjectIdentity_Identity):
    """
    The authoritative identity of the Cisco 2507 repeater
    port group.
    
    

    """

    _prefix = 'cisco-smi'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentity_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.smi._meta import _CISCO_SMI as meta
        return meta._meta_table['Cisco2507RptrGroup_Identity']['meta_info']


class Cisco2516RptrGroup_Identity(ObjectIdentity_Identity):
    """
    The authoritative identity of the Cisco 2516 repeater
    port group.
    
    

    """

    _prefix = 'cisco-smi'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentity_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.smi._meta import _CISCO_SMI as meta
        return meta._meta_table['Cisco2516RptrGroup_Identity']['meta_info']


class CiscoAdmin_Identity(ObjectIdentity_Identity):
    """
    ciscoAdmin is reserved for administratively assigned
    OBJECT IDENTIFIERS, i.e. those not associated with MIB
    objects
    
    

    """

    _prefix = 'cisco-smi'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentity_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.smi._meta import _CISCO_SMI as meta
        return meta._meta_table['CiscoAdmin_Identity']['meta_info']


class CiscoAgentCapability_Identity(ObjectIdentity_Identity):
    """
    ciscoAgentCapability provides a root object identifier
    from which AGENT\-CAPABILITIES values may be assigned.
    
    

    """

    _prefix = 'cisco-smi'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentity_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.smi._meta import _CISCO_SMI as meta
        return meta._meta_table['CiscoAgentCapability_Identity']['meta_info']


class CiscoCIB_Identity(ObjectIdentity_Identity):
    """
    ciscoCIB is the root of the Cisco\-assigned OID subtree for
    assignment to MIB modules describing managed objects that
    part of the CPE automatic configuration framework.
    
    

    """

    _prefix = 'cisco-smi'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentity_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.smi._meta import _CISCO_SMI as meta
        return meta._meta_table['CiscoCIB_Identity']['meta_info']


class CiscoChipSetSaint1_Identity(ObjectIdentity_Identity):
    """
    The identity of the Rev 1 SAINT ethernet chipset
    manufactured for cisco by LSI Logic.
    
    

    """

    _prefix = 'cisco-smi'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentity_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.smi._meta import _CISCO_SMI as meta
        return meta._meta_table['CiscoChipSetSaint1_Identity']['meta_info']


class CiscoChipSetSaint2_Identity(ObjectIdentity_Identity):
    """
    The identity of the Rev 2 SAINT ethernet chipset
    manufactured for cisco by LSI Logic.
    
    

    """

    _prefix = 'cisco-smi'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentity_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.smi._meta import _CISCO_SMI as meta
        return meta._meta_table['CiscoChipSetSaint2_Identity']['meta_info']


class CiscoChipSetSaint3_Identity(ObjectIdentity_Identity):
    """
    The identity of the Rev 3 SAINT ethernet chipset
    manufactured for cisco by Plessey.
    
    

    """

    _prefix = 'cisco-smi'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentity_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.smi._meta import _CISCO_SMI as meta
        return meta._meta_table['CiscoChipSetSaint3_Identity']['meta_info']


class CiscoChipSetSaint4_Identity(ObjectIdentity_Identity):
    """
    The identity of the Rev 4 SAINT ethernet chipset
    manufactured for cisco by Mitsubishi.
    
    

    """

    _prefix = 'cisco-smi'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentity_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.smi._meta import _CISCO_SMI as meta
        return meta._meta_table['CiscoChipSetSaint4_Identity']['meta_info']


class CiscoChipSets_Identity(ObjectIdentity_Identity):
    """
    Numerous media\-specific MIBS have an object, defined as
    an OBJECT IDENTIFIER, which is the identity of the chipset
    realizing the interface.  Cisco\-specific chipsets have their 
    OBJECT IDENTIFIERS assigned under this subtree.
    
    

    """

    _prefix = 'cisco-smi'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentity_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.smi._meta import _CISCO_SMI as meta
        return meta._meta_table['CiscoChipSets_Identity']['meta_info']


class CiscoCibMmiGroup_Identity(ObjectIdentity_Identity):
    """
    ciscoCibMmiGroup is the root of the Cisco\-assigned OID
    subtree for assignment to MIB modules describing managed
    objects supporting the Modem Management Interface (MMI),
    the interface that facilitates CPE automatic configuration.
    
    

    """

    _prefix = 'cisco-smi'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentity_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.smi._meta import _CISCO_SMI as meta
        return meta._meta_table['CiscoCibMmiGroup_Identity']['meta_info']


class CiscoCibProvGroup_Identity(ObjectIdentity_Identity):
    """
    ciscoCibStoreGroup is the root of the Cisco\-assigned OID
    subtree for assignment to MIB modules describing managed
    objects contributing to the Configuration Information Base
    (CIB).
    
    

    """

    _prefix = 'cisco-smi'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentity_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.smi._meta import _CISCO_SMI as meta
        return meta._meta_table['CiscoCibProvGroup_Identity']['meta_info']


class CiscoConfig_Identity(ObjectIdentity_Identity):
    """
    ciscoConfig is the main subtree for configuration mibs.
    
    

    """

    _prefix = 'cisco-smi'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentity_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.smi._meta import _CISCO_SMI as meta
        return meta._meta_table['CiscoConfig_Identity']['meta_info']


class CiscoDomains_Identity(ObjectIdentity_Identity):
    """
    ciscoDomains provides a root object identifier from which
    different transport mapping values may be assigned.
    
    

    """

    _prefix = 'cisco-smi'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentity_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.smi._meta import _CISCO_SMI as meta
        return meta._meta_table['CiscoDomains_Identity']['meta_info']


class CiscoExperiment_Identity(ObjectIdentity_Identity):
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

    _prefix = 'cisco-smi'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentity_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.smi._meta import _CISCO_SMI as meta
        return meta._meta_table['CiscoExperiment_Identity']['meta_info']


class CiscoMgmt_Identity(ObjectIdentity_Identity):
    """
    ciscoMgmt is the main subtree for new mib development.
    
    

    """

    _prefix = 'cisco-smi'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentity_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.smi._meta import _CISCO_SMI as meta
        return meta._meta_table['CiscoMgmt_Identity']['meta_info']


class CiscoModules_Identity(ObjectIdentity_Identity):
    """
    ciscoModules provides a root object identifier
    from which MODULE\-IDENTITY values may be assigned.
    
    

    """

    _prefix = 'cisco-smi'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentity_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.smi._meta import _CISCO_SMI as meta
        return meta._meta_table['CiscoModules_Identity']['meta_info']


class CiscoPIB_Identity(ObjectIdentity_Identity):
    """
    ciscoPIB is the root of the Cisco\-assigned OID
    subtree for assignment to PIB (Policy Information
    Base) modules.
    
    

    """

    _prefix = 'cisco-smi'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentity_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.smi._meta import _CISCO_SMI as meta
        return meta._meta_table['CiscoPIB_Identity']['meta_info']


class CiscoPKI_Identity(ObjectIdentity_Identity):
    """
    ciscoPKI is the root of cisco\-assigned OID subtree for PKI
    Certificate Policies and Certificate Extensions.
    
    

    """

    _prefix = 'cisco-smi'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentity_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.smi._meta import _CISCO_SMI as meta
        return meta._meta_table['CiscoPKI_Identity']['meta_info']


class CiscoPartnerProducts_Identity(ObjectIdentity_Identity):
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

    _prefix = 'cisco-smi'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentity_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.smi._meta import _CISCO_SMI as meta
        return meta._meta_table['CiscoPartnerProducts_Identity']['meta_info']


class CiscoPibToMib_Identity(ObjectIdentity_Identity):
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

    _prefix = 'cisco-smi'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentity_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.smi._meta import _CISCO_SMI as meta
        return meta._meta_table['CiscoPibToMib_Identity']['meta_info']


class CiscoPolicyAuto_Identity(ObjectIdentity_Identity):
    """
    ciscoPolicyAuto is the root of the Cisco\-assigned
    OID subtree for OIDs which are automatically assigned
    for use in Policy Management.
    
    

    """

    _prefix = 'cisco-smi'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentity_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.smi._meta import _CISCO_SMI as meta
        return meta._meta_table['CiscoPolicyAuto_Identity']['meta_info']


class CiscoPolicy_Identity(ObjectIdentity_Identity):
    """
    ciscoPolicy is the root of the Cisco\-assigned OID
    subtree for use with Policy Management.
    
    

    """

    _prefix = 'cisco-smi'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentity_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.smi._meta import _CISCO_SMI as meta
        return meta._meta_table['CiscoPolicy_Identity']['meta_info']


class CiscoProducts_Identity(ObjectIdentity_Identity):
    """
    ciscoProducts is the root OBJECT IDENTIFIER from
    which sysObjectID values are assigned.  Actual
    values are defined in CISCO\-PRODUCTS\-MIB.
    
    

    """

    _prefix = 'cisco-smi'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentity_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.smi._meta import _CISCO_SMI as meta
        return meta._meta_table['CiscoProducts_Identity']['meta_info']


class CiscoProxy_Identity(ObjectIdentity_Identity):
    """
    ciscoProxy OBJECT IDENTIFIERS are used to uniquely name
    party mib records created to proxy for SNMPv1.
    
    

    """

    _prefix = 'cisco-smi'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentity_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.smi._meta import _CISCO_SMI as meta
        return meta._meta_table['CiscoProxy_Identity']['meta_info']


class CiscoRptrGroupObjectID_Identity(ObjectIdentity_Identity):
    """
    ciscoRptrGroupObjectID OBJECT IDENTIFIERS are used to
    uniquely identify groups of repeater ports for use by the
    SNMP\-REPEATER\-MIB (RFC 1516) rptrGroupObjectID object.
    
    

    """

    _prefix = 'cisco-smi'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentity_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.smi._meta import _CISCO_SMI as meta
        return meta._meta_table['CiscoRptrGroupObjectID_Identity']['meta_info']


class CiscoSB_Identity(ObjectIdentity_Identity):
    """
    ciscoSB provides root Object Identifier for Management
    Information Base for products of Cisco Small Business.
    This includes products rebranded from linksys aquisition.
    MIB numbers under this root are managed and controlled
    by ciscosb\_mib@cisco.com.
    
    

    """

    _prefix = 'cisco-smi'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentity_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.smi._meta import _CISCO_SMI as meta
        return meta._meta_table['CiscoSB_Identity']['meta_info']


class CiscoSMB_Identity(ObjectIdentity_Identity):
    """
    ciscoSMB provides root Object Identifier for Management
    Information Base for products of Cisco built for Small and 
    Medium Business market.The MIB numbers under this root are 
    managed and controlled by ciscosmb\_mib@cisco.com
    
    

    """

    _prefix = 'cisco-smi'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentity_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.smi._meta import _CISCO_SMI as meta
        return meta._meta_table['CiscoSMB_Identity']['meta_info']


class CiscoTDomainClns_Identity(ObjectIdentity_Identity):
    """
    The CLNS transport domain.  The corresponding transport
    address is of type CiscoTAddressOSI.
    
    

    """

    _prefix = 'cisco-smi'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentity_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.smi._meta import _CISCO_SMI as meta
        return meta._meta_table['CiscoTDomainClns_Identity']['meta_info']


class CiscoTDomainCons_Identity(ObjectIdentity_Identity):
    """
    The CONS transport domain.  The corresponding transport
    address is of type CiscoTAddressOSI.
    
    

    """

    _prefix = 'cisco-smi'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentity_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.smi._meta import _CISCO_SMI as meta
        return meta._meta_table['CiscoTDomainCons_Identity']['meta_info']


class CiscoTDomainDdp_Identity(ObjectIdentity_Identity):
    """
    The DDP transport domain.  The corresponding transport
    address is of type CiscoTAddressNBP.
    
    

    """

    _prefix = 'cisco-smi'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentity_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.smi._meta import _CISCO_SMI as meta
        return meta._meta_table['CiscoTDomainDdp_Identity']['meta_info']


class CiscoTDomainIpx_Identity(ObjectIdentity_Identity):
    """
    The IPX transport domain.  The corresponding transport
    address is of type CiscoTAddressIPX.
    
    

    """

    _prefix = 'cisco-smi'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentity_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.smi._meta import _CISCO_SMI as meta
        return meta._meta_table['CiscoTDomainIpx_Identity']['meta_info']


class CiscoTDomainLocal_Identity(ObjectIdentity_Identity):
    """
    The Posix Local IPC transport domain. The corresponding
    transport address is of type CiscoTAddressLocal.  The Posix
    Local IPC transport domain incorporates the well known UNIX
    domain sockets.
    
    

    """

    _prefix = 'cisco-smi'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentity_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.smi._meta import _CISCO_SMI as meta
        return meta._meta_table['CiscoTDomainLocal_Identity']['meta_info']


class CiscoTDomainSctpIpv4_Identity(ObjectIdentity_Identity):
    """
    The SCTP over IPv4 transport domain.  The corresponding
    transport address is of type CiscoTAddressIPv4.
    
    

    """

    _prefix = 'cisco-smi'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentity_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.smi._meta import _CISCO_SMI as meta
        return meta._meta_table['CiscoTDomainSctpIpv4_Identity']['meta_info']


class CiscoTDomainSctpIpv6_Identity(ObjectIdentity_Identity):
    """
    The SCTP over IPv6 transport domain.  The corresponding
    transport address is of type CiscoTAddressIPv6 for global IPv6
    addresses and CiscoTAddressIPv6s for scoped IPv6 addresses.
    
    

    """

    _prefix = 'cisco-smi'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentity_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.smi._meta import _CISCO_SMI as meta
        return meta._meta_table['CiscoTDomainSctpIpv6_Identity']['meta_info']


class CiscoTDomainTcpIpv4_Identity(ObjectIdentity_Identity):
    """
    The TCP over IPv4 transport domain.  The corresponding
    transport address is of type CiscoTAddressIPv4.
    
    

    """

    _prefix = 'cisco-smi'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentity_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.smi._meta import _CISCO_SMI as meta
        return meta._meta_table['CiscoTDomainTcpIpv4_Identity']['meta_info']


class CiscoTDomainTcpIpv6_Identity(ObjectIdentity_Identity):
    """
    The TCP over IPv6 transport domain.  The corresponding
    transport address is of type CiscoTAddressIPv6 for global IPv6
    addresses and CiscoTAddressIPv6s for scoped IPv6 addresses.
    
    

    """

    _prefix = 'cisco-smi'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentity_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.smi._meta import _CISCO_SMI as meta
        return meta._meta_table['CiscoTDomainTcpIpv6_Identity']['meta_info']


class CiscoTDomainUdpIpv4_Identity(ObjectIdentity_Identity):
    """
    The UDP over IPv4 transport domain.  The corresponding
    transport address is of type CiscoTAddressIPv4.
    
    

    """

    _prefix = 'cisco-smi'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentity_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.smi._meta import _CISCO_SMI as meta
        return meta._meta_table['CiscoTDomainUdpIpv4_Identity']['meta_info']


class CiscoTDomainUdpIpv6_Identity(ObjectIdentity_Identity):
    """
    The UDP over IPv6 transport domain.  The corresponding
    transport address is of type CiscoTAddressIPv6 for global IPv6
    addresses and CiscoTAddressIPv6s for scoped IPv6 addresses.
    
    

    """

    _prefix = 'cisco-smi'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentity_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.smi._meta import _CISCO_SMI as meta
        return meta._meta_table['CiscoTDomainUdpIpv6_Identity']['meta_info']


class CiscoUnknownRptrGroup_Identity(ObjectIdentity_Identity):
    """
    The identity of an unknown repeater port group.
    
    

    """

    _prefix = 'cisco-smi'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentity_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.smi._meta import _CISCO_SMI as meta
        return meta._meta_table['CiscoUnknownRptrGroup_Identity']['meta_info']


class CiscoWsx5020RptrGroup_Identity(ObjectIdentity_Identity):
    """
    The authoritative identity of the wsx5020 repeater
    port group.
    
    

    """

    _prefix = 'cisco-smi'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentity_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.smi._meta import _CISCO_SMI as meta
        return meta._meta_table['CiscoWsx5020RptrGroup_Identity']['meta_info']


class Ciscoworks_Identity(ObjectIdentity_Identity):
    """
    ciscoworks provides a root object identifier beneath
    which mibs applicable to the CiscoWorks family of network
    management products are defined.
    
    

    """

    _prefix = 'cisco-smi'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentity_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.smi._meta import _CISCO_SMI as meta
        return meta._meta_table['Ciscoworks_Identity']['meta_info']


class Lightstream_Identity(ObjectIdentity_Identity):
    """
    subtree reserved for use by Lightstream
    
    

    """

    _prefix = 'cisco-smi'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentity_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.smi._meta import _CISCO_SMI as meta
        return meta._meta_table['Lightstream_Identity']['meta_info']


class Local_Identity(ObjectIdentity_Identity):
    """
    Subtree beneath which pre\-10.2 MIBS were built.
    
    

    """

    _prefix = 'cisco-smi'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentity_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.smi._meta import _CISCO_SMI as meta
        return meta._meta_table['Local_Identity']['meta_info']


class Newport_Identity(ObjectIdentity_Identity):
    """
    subtree reserved for use by the former Newport Systems
    Solutions, now a portion of the Access Business Unit.
    
    

    """

    _prefix = 'cisco-smi'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentity_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.smi._meta import _CISCO_SMI as meta
        return meta._meta_table['Newport_Identity']['meta_info']


class OtherEnterprises_Identity(ObjectIdentity_Identity):
    """
    otherEnterprises provides a root object identifier
    from which mibs produced by other companies may be
    placed.  mibs produced by other enterprises are
    typicially implemented with the object identifiers
    as defined in the mib, but if the mib is deemed to
    be uncontrolled, we may reroot the mib at this
    subtree in order to have a controlled version.
    
    

    """

    _prefix = 'cisco-smi'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentity_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.smi._meta import _CISCO_SMI as meta
        return meta._meta_table['OtherEnterprises_Identity']['meta_info']


class Pakmon_Identity(ObjectIdentity_Identity):
    """
    reserved for pakmon
    
    

    """

    _prefix = 'cisco-smi'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentity_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.smi._meta import _CISCO_SMI as meta
        return meta._meta_table['Pakmon_Identity']['meta_info']


class Temporary_Identity(ObjectIdentity_Identity):
    """
    Subtree beneath which pre\-10.2 experiments were
    placed.
    
    

    """

    _prefix = 'cisco-smi'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentity_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.smi._meta import _CISCO_SMI as meta
        return meta._meta_table['Temporary_Identity']['meta_info']


class Workgroup_Identity(ObjectIdentity_Identity):
    """
    subtree reserved for use by the Workgroup Business Unit
    
    

    """

    _prefix = 'cisco-smi'
    _revision = '2012-08-29'

    def __init__(self):
        ObjectIdentity_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.smi._meta import _CISCO_SMI as meta
        return meta._meta_table['Workgroup_Identity']['meta_info']


