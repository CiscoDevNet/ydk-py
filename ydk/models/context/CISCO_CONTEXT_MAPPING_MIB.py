""" CISCO_CONTEXT_MAPPING_MIB 

A single SNMP agent sometimes needs to support multiple
instances of the same MIB module, and does so through the
use of multiple SNMP contexts.  This typically occurs because
the technology has evolved to have extra dimension(s), i.e.,
one or more extra data and/or identifier values which are
different in the different contexts, but were not defined in
INDEX clause(s) of the original MIB module.  In such cases,
network management applications need to know the specific
data/identifier values in each context, and this MIB module
provides mapping tables which contain that information.

Within a network there can be multiple Virtual Private
Networks (VPNs) configured using Virtual Routing and
Forwarding Instances (VRFs). Within a VPN there can be
multiple topologies when Multi\-topology Routing (MTR) is
used. Also, Interior Gateway Protocols (IGPs) can have
multiple protocol instances running on the device.
A network can have multiple broadcast domains configured
using Bridge Domain Identifiers.

With MTR routing, VRFs, and Bridge domains, a router now 
needs to support multiple instances of several existing 
MIB modules, and this can be achieved if the router's SNMP 
agent provides access to each instance of the same MIB module 
via a different SNMP context (see Section 3.1.1 of RFC 3411).
For MTR routing, VRFs, and Bridge domains, a different SNMP 
context is needed depending on one or more of the following\: 
the VRF, the topology\-identifier, the routing protocol instance,
and the bridge domain identifier.
In other words, the router's management information can be
accessed through multiple SNMP contexts where each such
context represents a specific VRF, a specific
topology\-identifier, a specific routing protocol instance 
and/or a bridge domain identifier. This MIB module provides 
a mapping of each such SNMP context to the corresponding VRF,
the corresponding topology, the corresponding routing protocol 
instance, and the corresponding bridge domain identifier.
Some SNMP contexts are independent of VRFs, independent of
a topology, independent of a routing protocol instance, or 
independent of a bridge domain and in such a case, the mapping
is to the zero length string.

With the Cisco package licensing strategy, the features 
available in the image are grouped into multiple packages 
and each packages can be managed to operate at different 
feature levels based on the available license. This MIB 
module provides option to associate an SNMP context to a 
feature package group. This will allow manageability of 
license MIB objects specific to a feature package group.

As technology evolves more we may need additional
identifiers to identify the context. Then we would need
to add those additional identifiers into the mapping.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError


from ydk.models.snmpv2.SNMPv2_TC import RowStatus_Enum
from ydk.models.snmpv2.SNMPv2_TC import StorageType_Enum


class CISCOCONTEXTMAPPINGMIB(object):
    """
    
    
    .. attribute:: ccontextmappingbridgedomaintable
    
    	This table contains information on which cContextMappingVacmContextName is mapped to which bridge domain.  A Bridge Domain is one of the means by which it is possible  to define an Ethernet broadcast domain on a bridging device.  A network can have multiple broadcast domains configured. This table helps the network management personnel to find  out the  details of various broadcast domains configured  in the network.  An entry need to exist in cContextMappingTable, to create  an entry in this table
    	**type**\: :py:class:`CContextMappingBridgeDomainTable <ydk.models.context.CISCO_CONTEXT_MAPPING_MIB.CISCOCONTEXTMAPPINGMIB.CContextMappingBridgeDomainTable>`
    
    .. attribute:: ccontextmappingbridgeinstancetable
    
    	This table contains information on mapping between cContextMappingVacmContextName and bridge instance.  Bridge instance is an instance of a physical or logical  bridge which has unique bridge\-id.  If an entry is deleted from cContextMappingTable, the corresponding entry in this table will also get deleted.  If an entry needs to be created in this table, the corresponding entry must exist in cContextMappingTable
    	**type**\: :py:class:`CContextMappingBridgeInstanceTable <ydk.models.context.CISCO_CONTEXT_MAPPING_MIB.CISCOCONTEXTMAPPINGMIB.CContextMappingBridgeInstanceTable>`
    
    .. attribute:: ccontextmappinglicensegrouptable
    
    	This table contains information on which cContextMappingVacmContextName is mapped to which License Group. Group level licensing is used where each Technology Package is enabled via a License
    	**type**\: :py:class:`CContextMappingLicenseGroupTable <ydk.models.context.CISCO_CONTEXT_MAPPING_MIB.CISCOCONTEXTMAPPINGMIB.CContextMappingLicenseGroupTable>`
    
    .. attribute:: ccontextmappingtable
    
    	This table contains information on which cContextMappingVacmContextName is mapped to which VRF, topology, and routing protocol instance.  This table is indexed by SNMP VACM context.  Configuring a row in this table for an SNMP context does not require that the context be already defined, i.e., a row can be created in this table for a context before the corresponding row is created in RFC 3415's vacmContextTable.  To create a row in this table, a manager must set cContextMappingRowStatus to either 'createAndGo' or 'createAndWait'.  To delete a row in this table, a manager must set cContextMappingRowStatus to 'destroy'
    	**type**\: :py:class:`CContextMappingTable <ydk.models.context.CISCO_CONTEXT_MAPPING_MIB.CISCOCONTEXTMAPPINGMIB.CContextMappingTable>`
    
    

    """

    _prefix = 'cisco-context'
    _revision = '2008-11-22'

    def __init__(self):
        self.ccontextmappingbridgedomaintable = CISCOCONTEXTMAPPINGMIB.CContextMappingBridgeDomainTable()
        self.ccontextmappingbridgedomaintable.parent = self
        self.ccontextmappingbridgeinstancetable = CISCOCONTEXTMAPPINGMIB.CContextMappingBridgeInstanceTable()
        self.ccontextmappingbridgeinstancetable.parent = self
        self.ccontextmappinglicensegrouptable = CISCOCONTEXTMAPPINGMIB.CContextMappingLicenseGroupTable()
        self.ccontextmappinglicensegrouptable.parent = self
        self.ccontextmappingtable = CISCOCONTEXTMAPPINGMIB.CContextMappingTable()
        self.ccontextmappingtable.parent = self


    class CContextMappingBridgeDomainTable(object):
        """
        This table contains information on which
        cContextMappingVacmContextName is mapped to
        which bridge domain.
        
        A Bridge Domain is one of the means by which it is possible 
        to define an Ethernet broadcast domain on a bridging device. 
        A network can have multiple broadcast domains configured.
        This table helps the network management personnel to find 
        out the  details of various broadcast domains configured 
        in the network.
        
        An entry need to exist in cContextMappingTable, to create 
        an entry in this table.
        
        .. attribute:: ccontextmappingbridgedomainentry
        
        	Information relating to a single mapping of cContextMappingVacmContextName to the  corresponding bridge domain.  To create a row in this table, a manager must set cContextMappingBridgeDomainRowStatus to either  'createAndGo' or 'createAndWait'.  To delete a row in this table, a manager must set cContextMappingBridgeDomainRowStatus to 'destroy'
        	**type**\: list of :py:class:`CContextMappingBridgeDomainEntry <ydk.models.context.CISCO_CONTEXT_MAPPING_MIB.CISCOCONTEXTMAPPINGMIB.CContextMappingBridgeDomainTable.CContextMappingBridgeDomainEntry>`
        
        

        """

        _prefix = 'cisco-context'
        _revision = '2008-11-22'

        def __init__(self):
            self.parent = None
            self.ccontextmappingbridgedomainentry = YList()
            self.ccontextmappingbridgedomainentry.parent = self
            self.ccontextmappingbridgedomainentry.name = 'ccontextmappingbridgedomainentry'


        class CContextMappingBridgeDomainEntry(object):
            """
            Information relating to a single mapping of
            cContextMappingVacmContextName to the 
            corresponding bridge domain.
            
            To create a row in this table, a manager must set
            cContextMappingBridgeDomainRowStatus to either 
            'createAndGo' or 'createAndWait'.
            
            To delete a row in this table, a manager must set
            cContextMappingBridgeDomainRowStatus to 'destroy'.
            
            .. attribute:: ccontextmappingvacmcontextname
            
            	
            	**type**\: str
            
            	**range:** 0..32
            
            .. attribute:: ccontextmappingbridgedomainidentifier
            
            	The value of an instance of this object identifies the bridge domain to which the SNMP context is  mapped to
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: ccontextmappingbridgedomainrowstatus
            
            	This object facilitates the creation, modification, or deletion of a conceptual row in this table
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            .. attribute:: ccontextmappingbridgedomainstoragetype
            
            	The storage type for this conceptual row.  Conceptual rows having the value 'permanent' need not allow write\-access to any columnar objects in the row
            	**type**\: :py:class:`StorageType_Enum <ydk.models.snmpv2.SNMPv2_TC.StorageType_Enum>`
            
            

            """

            _prefix = 'cisco-context'
            _revision = '2008-11-22'

            def __init__(self):
                self.parent = None
                self.ccontextmappingvacmcontextname = None
                self.ccontextmappingbridgedomainidentifier = None
                self.ccontextmappingbridgedomainrowstatus = None
                self.ccontextmappingbridgedomainstoragetype = None

            @property
            def _common_path(self):
                if self.ccontextmappingvacmcontextname is None:
                    raise YPYDataValidationError('Key property ccontextmappingvacmcontextname is None')

                return '/CISCO-CONTEXT-MAPPING-MIB:CISCO-CONTEXT-MAPPING-MIB/CISCO-CONTEXT-MAPPING-MIB:cContextMappingBridgeDomainTable/CISCO-CONTEXT-MAPPING-MIB:cContextMappingBridgeDomainEntry[CISCO-CONTEXT-MAPPING-MIB:cContextMappingVacmContextName = ' + str(self.ccontextmappingvacmcontextname) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ccontextmappingvacmcontextname is not None:
                    return True

                if self.ccontextmappingbridgedomainidentifier is not None:
                    return True

                if self.ccontextmappingbridgedomainrowstatus is not None:
                    return True

                if self.ccontextmappingbridgedomainstoragetype is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.context._meta import _CISCO_CONTEXT_MAPPING_MIB as meta
                return meta._meta_table['CISCOCONTEXTMAPPINGMIB.CContextMappingBridgeDomainTable.CContextMappingBridgeDomainEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-CONTEXT-MAPPING-MIB:CISCO-CONTEXT-MAPPING-MIB/CISCO-CONTEXT-MAPPING-MIB:cContextMappingBridgeDomainTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ccontextmappingbridgedomainentry is not None:
                for child_ref in self.ccontextmappingbridgedomainentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.context._meta import _CISCO_CONTEXT_MAPPING_MIB as meta
            return meta._meta_table['CISCOCONTEXTMAPPINGMIB.CContextMappingBridgeDomainTable']['meta_info']


    class CContextMappingBridgeInstanceTable(object):
        """
        This table contains information on mapping between
        cContextMappingVacmContextName and bridge instance.
        
        Bridge instance is an instance of a physical or logical 
        bridge which has unique bridge\-id.
        
        If an entry is deleted from cContextMappingTable, the
        corresponding entry in this table will also get deleted.
        
        If an entry needs to be created in this table, the
        corresponding entry must exist in cContextMappingTable.
        
        .. attribute:: ccontextmappingbridgeinstanceentry
        
        	Information relating to a single mapping of cContextMappingVacmContextName to the  corresponding bridge instance.  To create a row in this table, a manager must set cContextMappingBridgeInstRowStatus to either  'createAndGo' or 'createAndWait'.  To delete a row in this table, a manager must set cContextMappingBridgeInstRowStatus to 'destroy'
        	**type**\: list of :py:class:`CContextMappingBridgeInstanceEntry <ydk.models.context.CISCO_CONTEXT_MAPPING_MIB.CISCOCONTEXTMAPPINGMIB.CContextMappingBridgeInstanceTable.CContextMappingBridgeInstanceEntry>`
        
        

        """

        _prefix = 'cisco-context'
        _revision = '2008-11-22'

        def __init__(self):
            self.parent = None
            self.ccontextmappingbridgeinstanceentry = YList()
            self.ccontextmappingbridgeinstanceentry.parent = self
            self.ccontextmappingbridgeinstanceentry.name = 'ccontextmappingbridgeinstanceentry'


        class CContextMappingBridgeInstanceEntry(object):
            """
            Information relating to a single mapping of
            cContextMappingVacmContextName to the 
            corresponding bridge instance.
            
            To create a row in this table, a manager must set
            cContextMappingBridgeInstRowStatus to either 
            'createAndGo' or 'createAndWait'.
            
            To delete a row in this table, a manager must set
            cContextMappingBridgeInstRowStatus to 'destroy'.
            
            .. attribute:: ccontextmappingvacmcontextname
            
            	
            	**type**\: str
            
            	**range:** 0..32
            
            .. attribute:: ccontextmappingbridgeinstname
            
            	The object identifies the name given to bridge instance to which the SNMP context is mapped to.  Value of this object cannot be changed when the  RowStatus object in the same row is 'active'.  This is typically a human\-readable string. This is the same ASCII string used in the router's console interface to refer to this bridge instance.  When the value of this object is a zero length string, it indicates that the SNMP context is independent of any bridge instances
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: ccontextmappingbridgeinstrowstatus
            
            	This object facilitates the creation, modification, or deletion of a conceptual row in this table
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            .. attribute:: ccontextmappingbridgeinststoragetype
            
            	The storage type for this conceptual row.  Value of this object cannot be changed when the  RowStatus object in the same row is 'active'.  Conceptual rows having the value 'permanent' need not allow write\-access to any columnar objects in the row
            	**type**\: :py:class:`StorageType_Enum <ydk.models.snmpv2.SNMPv2_TC.StorageType_Enum>`
            
            

            """

            _prefix = 'cisco-context'
            _revision = '2008-11-22'

            def __init__(self):
                self.parent = None
                self.ccontextmappingvacmcontextname = None
                self.ccontextmappingbridgeinstname = None
                self.ccontextmappingbridgeinstrowstatus = None
                self.ccontextmappingbridgeinststoragetype = None

            @property
            def _common_path(self):
                if self.ccontextmappingvacmcontextname is None:
                    raise YPYDataValidationError('Key property ccontextmappingvacmcontextname is None')

                return '/CISCO-CONTEXT-MAPPING-MIB:CISCO-CONTEXT-MAPPING-MIB/CISCO-CONTEXT-MAPPING-MIB:cContextMappingBridgeInstanceTable/CISCO-CONTEXT-MAPPING-MIB:cContextMappingBridgeInstanceEntry[CISCO-CONTEXT-MAPPING-MIB:cContextMappingVacmContextName = ' + str(self.ccontextmappingvacmcontextname) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ccontextmappingvacmcontextname is not None:
                    return True

                if self.ccontextmappingbridgeinstname is not None:
                    return True

                if self.ccontextmappingbridgeinstrowstatus is not None:
                    return True

                if self.ccontextmappingbridgeinststoragetype is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.context._meta import _CISCO_CONTEXT_MAPPING_MIB as meta
                return meta._meta_table['CISCOCONTEXTMAPPINGMIB.CContextMappingBridgeInstanceTable.CContextMappingBridgeInstanceEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-CONTEXT-MAPPING-MIB:CISCO-CONTEXT-MAPPING-MIB/CISCO-CONTEXT-MAPPING-MIB:cContextMappingBridgeInstanceTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ccontextmappingbridgeinstanceentry is not None:
                for child_ref in self.ccontextmappingbridgeinstanceentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.context._meta import _CISCO_CONTEXT_MAPPING_MIB as meta
            return meta._meta_table['CISCOCONTEXTMAPPINGMIB.CContextMappingBridgeInstanceTable']['meta_info']


    class CContextMappingLicenseGroupTable(object):
        """
        This table contains information on which
        cContextMappingVacmContextName is mapped to
        which License Group.
        Group level licensing is used where each
        Technology Package is enabled via a License.
        
        .. attribute:: ccontextmappinglicensegroupentry
        
        	Information relating to a single mapping of CContextMappingVacmContextName to the corresponding License Group
        	**type**\: list of :py:class:`CContextMappingLicenseGroupEntry <ydk.models.context.CISCO_CONTEXT_MAPPING_MIB.CISCOCONTEXTMAPPINGMIB.CContextMappingLicenseGroupTable.CContextMappingLicenseGroupEntry>`
        
        

        """

        _prefix = 'cisco-context'
        _revision = '2008-11-22'

        def __init__(self):
            self.parent = None
            self.ccontextmappinglicensegroupentry = YList()
            self.ccontextmappinglicensegroupentry.parent = self
            self.ccontextmappinglicensegroupentry.name = 'ccontextmappinglicensegroupentry'


        class CContextMappingLicenseGroupEntry(object):
            """
            Information relating to a single mapping of
            CContextMappingVacmContextName to the
            corresponding License Group.
            
            .. attribute:: ccontextmappingvacmcontextname
            
            	
            	**type**\: str
            
            	**range:** 0..32
            
            .. attribute:: ccontextmappinglicensegroupname
            
            	The value of an instance of this object identifies the name given to the Group to which the SNMP context is mapped.  Feature sets from all groups will be combined to form  universal image. User can configure multiple groups as needed.  For example\: In Next generation ISRs will use the universal image package level licensing model for its licensing need. Each group has the feature set needed for that specific technology. Feature sets from different groups are combined to  form universal image and each feature set for a group  can be enabled using a valid license key. There will  be a base level ipbase package in which the router  boots with out any license key.  The following are the different Technology Groups. 1.crypto 2.data 3.ip 4.legacy 5.novpn\-security 6.security 7.uc
            	**type**\: str
            
            	**range:** 0..32
            
            .. attribute:: ccontextmappinglicensegrouprowstatus
            
            	This object facilitates the creation, modification, or deletion of a conceptual row in this table
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            .. attribute:: ccontextmappinglicensegroupstoragetype
            
            	The storage type for this conceptual row.  Conceptual rows having the value 'permanent' need not allow write\-access to any columnar objects in the row
            	**type**\: :py:class:`StorageType_Enum <ydk.models.snmpv2.SNMPv2_TC.StorageType_Enum>`
            
            

            """

            _prefix = 'cisco-context'
            _revision = '2008-11-22'

            def __init__(self):
                self.parent = None
                self.ccontextmappingvacmcontextname = None
                self.ccontextmappinglicensegroupname = None
                self.ccontextmappinglicensegrouprowstatus = None
                self.ccontextmappinglicensegroupstoragetype = None

            @property
            def _common_path(self):
                if self.ccontextmappingvacmcontextname is None:
                    raise YPYDataValidationError('Key property ccontextmappingvacmcontextname is None')

                return '/CISCO-CONTEXT-MAPPING-MIB:CISCO-CONTEXT-MAPPING-MIB/CISCO-CONTEXT-MAPPING-MIB:cContextMappingLicenseGroupTable/CISCO-CONTEXT-MAPPING-MIB:cContextMappingLicenseGroupEntry[CISCO-CONTEXT-MAPPING-MIB:cContextMappingVacmContextName = ' + str(self.ccontextmappingvacmcontextname) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ccontextmappingvacmcontextname is not None:
                    return True

                if self.ccontextmappinglicensegroupname is not None:
                    return True

                if self.ccontextmappinglicensegrouprowstatus is not None:
                    return True

                if self.ccontextmappinglicensegroupstoragetype is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.context._meta import _CISCO_CONTEXT_MAPPING_MIB as meta
                return meta._meta_table['CISCOCONTEXTMAPPINGMIB.CContextMappingLicenseGroupTable.CContextMappingLicenseGroupEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-CONTEXT-MAPPING-MIB:CISCO-CONTEXT-MAPPING-MIB/CISCO-CONTEXT-MAPPING-MIB:cContextMappingLicenseGroupTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ccontextmappinglicensegroupentry is not None:
                for child_ref in self.ccontextmappinglicensegroupentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.context._meta import _CISCO_CONTEXT_MAPPING_MIB as meta
            return meta._meta_table['CISCOCONTEXTMAPPINGMIB.CContextMappingLicenseGroupTable']['meta_info']


    class CContextMappingTable(object):
        """
        This table contains information on which
        cContextMappingVacmContextName is mapped to
        which VRF, topology, and routing protocol instance.
        
        This table is indexed by SNMP VACM context.
        
        Configuring a row in this table for an SNMP context
        does not require that the context be already defined,
        i.e., a row can be created in this table for a context
        before the corresponding row is created in RFC 3415's
        vacmContextTable.
        
        To create a row in this table, a manager must set
        cContextMappingRowStatus to either 'createAndGo' or
        'createAndWait'.
        
        To delete a row in this table, a manager must set
        cContextMappingRowStatus to 'destroy'.
        
        .. attribute:: ccontextmappingentry
        
        	Information relating to a single mapping of cContextMappingVacmContextName to the corresponding VRF, the corresponding topology, and the corresponding routing protocol instance
        	**type**\: list of :py:class:`CContextMappingEntry <ydk.models.context.CISCO_CONTEXT_MAPPING_MIB.CISCOCONTEXTMAPPINGMIB.CContextMappingTable.CContextMappingEntry>`
        
        

        """

        _prefix = 'cisco-context'
        _revision = '2008-11-22'

        def __init__(self):
            self.parent = None
            self.ccontextmappingentry = YList()
            self.ccontextmappingentry.parent = self
            self.ccontextmappingentry.name = 'ccontextmappingentry'


        class CContextMappingEntry(object):
            """
            Information relating to a single mapping of
            cContextMappingVacmContextName to the corresponding VRF,
            the corresponding topology, and the corresponding routing
            protocol instance.
            
            .. attribute:: ccontextmappingvacmcontextname
            
            	The vacmContextName given to the SNMP context.  This is a human readable name identifying a particular SNMP VACM context at a particular SNMP entity. The empty contextName (zero length) represents the default context
            	**type**\: str
            
            	**range:** 0..32
            
            .. attribute:: ccontextmappingprotoinstname
            
            	The value of an instance of this object identifies the name given to the protocol instance to which the SNMP context is mapped to.  This is typically a human\-readable string. This is the same ASCII string used in the router's console interface to refer to this protocol instance.  When the value of this object is the zero length string it indicates that the SNMP context is independent of any protocol instance
            	**type**\: str
            
            	**range:** 0..32
            
            .. attribute:: ccontextmappingrowstatus
            
            	This object facilitates the creation, modification, or deletion of a conceptual row in this table
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            .. attribute:: ccontextmappingstoragetype
            
            	The storage type for this conceptual row.  Conceptual rows having the value 'permanent' need not allow write\-access to any columnar objects in the row
            	**type**\: :py:class:`StorageType_Enum <ydk.models.snmpv2.SNMPv2_TC.StorageType_Enum>`
            
            .. attribute:: ccontextmappingtopologyname
            
            	The value of an instance of this object identifies the name given to the topology to which the SNMP context is mapped to.  This is typically a human\-readable string. This is the same ASCII string used in the router's console interface to refer to this topology.  When the value of this object is the zero length string it indicates that the SNMP context is independent of any topology
            	**type**\: str
            
            	**range:** 0..32
            
            .. attribute:: ccontextmappingvrfname
            
            	The value of an instance of this object identifies the name given to the VRF to which the SNMP context is mapped to.  This is typically a human\-readable string. This is the same ASCII string used in the router's console interface to refer to this VRF.  When the value of this object is the zero length string it indicates that the SNMP context is independent of any VRF
            	**type**\: str
            
            	**range:** 0..32
            
            

            """

            _prefix = 'cisco-context'
            _revision = '2008-11-22'

            def __init__(self):
                self.parent = None
                self.ccontextmappingvacmcontextname = None
                self.ccontextmappingprotoinstname = None
                self.ccontextmappingrowstatus = None
                self.ccontextmappingstoragetype = None
                self.ccontextmappingtopologyname = None
                self.ccontextmappingvrfname = None

            @property
            def _common_path(self):
                if self.ccontextmappingvacmcontextname is None:
                    raise YPYDataValidationError('Key property ccontextmappingvacmcontextname is None')

                return '/CISCO-CONTEXT-MAPPING-MIB:CISCO-CONTEXT-MAPPING-MIB/CISCO-CONTEXT-MAPPING-MIB:cContextMappingTable/CISCO-CONTEXT-MAPPING-MIB:cContextMappingEntry[CISCO-CONTEXT-MAPPING-MIB:cContextMappingVacmContextName = ' + str(self.ccontextmappingvacmcontextname) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ccontextmappingvacmcontextname is not None:
                    return True

                if self.ccontextmappingprotoinstname is not None:
                    return True

                if self.ccontextmappingrowstatus is not None:
                    return True

                if self.ccontextmappingstoragetype is not None:
                    return True

                if self.ccontextmappingtopologyname is not None:
                    return True

                if self.ccontextmappingvrfname is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.context._meta import _CISCO_CONTEXT_MAPPING_MIB as meta
                return meta._meta_table['CISCOCONTEXTMAPPINGMIB.CContextMappingTable.CContextMappingEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-CONTEXT-MAPPING-MIB:CISCO-CONTEXT-MAPPING-MIB/CISCO-CONTEXT-MAPPING-MIB:cContextMappingTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ccontextmappingentry is not None:
                for child_ref in self.ccontextmappingentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.context._meta import _CISCO_CONTEXT_MAPPING_MIB as meta
            return meta._meta_table['CISCOCONTEXTMAPPINGMIB.CContextMappingTable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-CONTEXT-MAPPING-MIB:CISCO-CONTEXT-MAPPING-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.ccontextmappingbridgedomaintable is not None and self.ccontextmappingbridgedomaintable._has_data():
            return True

        if self.ccontextmappingbridgedomaintable is not None and self.ccontextmappingbridgedomaintable.is_presence():
            return True

        if self.ccontextmappingbridgeinstancetable is not None and self.ccontextmappingbridgeinstancetable._has_data():
            return True

        if self.ccontextmappingbridgeinstancetable is not None and self.ccontextmappingbridgeinstancetable.is_presence():
            return True

        if self.ccontextmappinglicensegrouptable is not None and self.ccontextmappinglicensegrouptable._has_data():
            return True

        if self.ccontextmappinglicensegrouptable is not None and self.ccontextmappinglicensegrouptable.is_presence():
            return True

        if self.ccontextmappingtable is not None and self.ccontextmappingtable._has_data():
            return True

        if self.ccontextmappingtable is not None and self.ccontextmappingtable.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.context._meta import _CISCO_CONTEXT_MAPPING_MIB as meta
        return meta._meta_table['CISCOCONTEXTMAPPINGMIB']['meta_info']


