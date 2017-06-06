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

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class CiscoContextMappingMib(object):
    """
    
    
    .. attribute:: ccontextmappingbridgedomaintable
    
    	This table contains information on which cContextMappingVacmContextName is mapped to which bridge domain.  A Bridge Domain is one of the means by which it is possible  to define an Ethernet broadcast domain on a bridging device.  A network can have multiple broadcast domains configured. This table helps the network management personnel to find  out the  details of various broadcast domains configured  in the network.  An entry need to exist in cContextMappingTable, to create  an entry in this table
    	**type**\:   :py:class:`Ccontextmappingbridgedomaintable <ydk.models.cisco_ios_xe.CISCO_CONTEXT_MAPPING_MIB.CiscoContextMappingMib.Ccontextmappingbridgedomaintable>`
    
    .. attribute:: ccontextmappingbridgeinstancetable
    
    	This table contains information on mapping between cContextMappingVacmContextName and bridge instance.  Bridge instance is an instance of a physical or logical  bridge which has unique bridge\-id.  If an entry is deleted from cContextMappingTable, the corresponding entry in this table will also get deleted.  If an entry needs to be created in this table, the corresponding entry must exist in cContextMappingTable
    	**type**\:   :py:class:`Ccontextmappingbridgeinstancetable <ydk.models.cisco_ios_xe.CISCO_CONTEXT_MAPPING_MIB.CiscoContextMappingMib.Ccontextmappingbridgeinstancetable>`
    
    .. attribute:: ccontextmappinglicensegrouptable
    
    	This table contains information on which cContextMappingVacmContextName is mapped to which License Group. Group level licensing is used where each Technology Package is enabled via a License
    	**type**\:   :py:class:`Ccontextmappinglicensegrouptable <ydk.models.cisco_ios_xe.CISCO_CONTEXT_MAPPING_MIB.CiscoContextMappingMib.Ccontextmappinglicensegrouptable>`
    
    .. attribute:: ccontextmappingtable
    
    	This table contains information on which cContextMappingVacmContextName is mapped to which VRF, topology, and routing protocol instance.  This table is indexed by SNMP VACM context.  Configuring a row in this table for an SNMP context does not require that the context be already defined, i.e., a row can be created in this table for a context before the corresponding row is created in RFC 3415's vacmContextTable.  To create a row in this table, a manager must set cContextMappingRowStatus to either 'createAndGo' or 'createAndWait'.  To delete a row in this table, a manager must set cContextMappingRowStatus to 'destroy'
    	**type**\:   :py:class:`Ccontextmappingtable <ydk.models.cisco_ios_xe.CISCO_CONTEXT_MAPPING_MIB.CiscoContextMappingMib.Ccontextmappingtable>`
    
    

    """

    _prefix = 'CISCO-CONTEXT-MAPPING-MIB'
    _revision = '2008-11-22'

    def __init__(self):
        self.ccontextmappingbridgedomaintable = CiscoContextMappingMib.Ccontextmappingbridgedomaintable()
        self.ccontextmappingbridgedomaintable.parent = self
        self.ccontextmappingbridgeinstancetable = CiscoContextMappingMib.Ccontextmappingbridgeinstancetable()
        self.ccontextmappingbridgeinstancetable.parent = self
        self.ccontextmappinglicensegrouptable = CiscoContextMappingMib.Ccontextmappinglicensegrouptable()
        self.ccontextmappinglicensegrouptable.parent = self
        self.ccontextmappingtable = CiscoContextMappingMib.Ccontextmappingtable()
        self.ccontextmappingtable.parent = self


    class Ccontextmappingtable(object):
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
        	**type**\: list of    :py:class:`Ccontextmappingentry <ydk.models.cisco_ios_xe.CISCO_CONTEXT_MAPPING_MIB.CiscoContextMappingMib.Ccontextmappingtable.Ccontextmappingentry>`
        
        

        """

        _prefix = 'CISCO-CONTEXT-MAPPING-MIB'
        _revision = '2008-11-22'

        def __init__(self):
            self.parent = None
            self.ccontextmappingentry = YList()
            self.ccontextmappingentry.parent = self
            self.ccontextmappingentry.name = 'ccontextmappingentry'


        class Ccontextmappingentry(object):
            """
            Information relating to a single mapping of
            cContextMappingVacmContextName to the corresponding VRF,
            the corresponding topology, and the corresponding routing
            protocol instance.
            
            .. attribute:: ccontextmappingvacmcontextname  <key>
            
            	The vacmContextName given to the SNMP context.  This is a human readable name identifying a particular SNMP VACM context at a particular SNMP entity. The empty contextName (zero length) represents the default context
            	**type**\:  str
            
            	**length:** 0..32
            
            .. attribute:: ccontextmappingprotoinstname
            
            	The value of an instance of this object identifies the name given to the protocol instance to which the SNMP context is mapped to.  This is typically a human\-readable string. This is the same ASCII string used in the router's console interface to refer to this protocol instance.  When the value of this object is the zero length string it indicates that the SNMP context is independent of any protocol instance
            	**type**\:  str
            
            	**length:** 0..32
            
            .. attribute:: ccontextmappingrowstatus
            
            	This object facilitates the creation, modification, or deletion of a conceptual row in this table
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            .. attribute:: ccontextmappingstoragetype
            
            	The storage type for this conceptual row.  Conceptual rows having the value 'permanent' need not allow write\-access to any columnar objects in the row
            	**type**\:   :py:class:`StoragetypeEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.StoragetypeEnum>`
            
            .. attribute:: ccontextmappingtopologyname
            
            	The value of an instance of this object identifies the name given to the topology to which the SNMP context is mapped to.  This is typically a human\-readable string. This is the same ASCII string used in the router's console interface to refer to this topology.  When the value of this object is the zero length string it indicates that the SNMP context is independent of any topology
            	**type**\:  str
            
            	**length:** 0..32
            
            .. attribute:: ccontextmappingvrfname
            
            	The value of an instance of this object identifies the name given to the VRF to which the SNMP context is mapped to.  This is typically a human\-readable string. This is the same ASCII string used in the router's console interface to refer to this VRF.  When the value of this object is the zero length string it indicates that the SNMP context is independent of any VRF
            	**type**\:  str
            
            	**length:** 0..32
            
            

            """

            _prefix = 'CISCO-CONTEXT-MAPPING-MIB'
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
                    raise YPYModelError('Key property ccontextmappingvacmcontextname is None')

                return '/CISCO-CONTEXT-MAPPING-MIB:CISCO-CONTEXT-MAPPING-MIB/CISCO-CONTEXT-MAPPING-MIB:cContextMappingTable/CISCO-CONTEXT-MAPPING-MIB:cContextMappingEntry[CISCO-CONTEXT-MAPPING-MIB:cContextMappingVacmContextName = ' + str(self.ccontextmappingvacmcontextname) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
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

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_CONTEXT_MAPPING_MIB as meta
                return meta._meta_table['CiscoContextMappingMib.Ccontextmappingtable.Ccontextmappingentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-CONTEXT-MAPPING-MIB:CISCO-CONTEXT-MAPPING-MIB/CISCO-CONTEXT-MAPPING-MIB:cContextMappingTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.ccontextmappingentry is not None:
                for child_ref in self.ccontextmappingentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_CONTEXT_MAPPING_MIB as meta
            return meta._meta_table['CiscoContextMappingMib.Ccontextmappingtable']['meta_info']


    class Ccontextmappingbridgedomaintable(object):
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
        	**type**\: list of    :py:class:`Ccontextmappingbridgedomainentry <ydk.models.cisco_ios_xe.CISCO_CONTEXT_MAPPING_MIB.CiscoContextMappingMib.Ccontextmappingbridgedomaintable.Ccontextmappingbridgedomainentry>`
        
        

        """

        _prefix = 'CISCO-CONTEXT-MAPPING-MIB'
        _revision = '2008-11-22'

        def __init__(self):
            self.parent = None
            self.ccontextmappingbridgedomainentry = YList()
            self.ccontextmappingbridgedomainentry.parent = self
            self.ccontextmappingbridgedomainentry.name = 'ccontextmappingbridgedomainentry'


        class Ccontextmappingbridgedomainentry(object):
            """
            Information relating to a single mapping of
            cContextMappingVacmContextName to the 
            corresponding bridge domain.
            
            To create a row in this table, a manager must set
            cContextMappingBridgeDomainRowStatus to either 
            'createAndGo' or 'createAndWait'.
            
            To delete a row in this table, a manager must set
            cContextMappingBridgeDomainRowStatus to 'destroy'.
            
            .. attribute:: ccontextmappingvacmcontextname  <key>
            
            	
            	**type**\:  str
            
            	**length:** 0..32
            
            	**refers to**\:  :py:class:`ccontextmappingvacmcontextname <ydk.models.cisco_ios_xe.CISCO_CONTEXT_MAPPING_MIB.CiscoContextMappingMib.Ccontextmappingtable.Ccontextmappingentry>`
            
            .. attribute:: ccontextmappingbridgedomainidentifier
            
            	The value of an instance of this object identifies the bridge domain to which the SNMP context is  mapped to
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: ccontextmappingbridgedomainrowstatus
            
            	This object facilitates the creation, modification, or deletion of a conceptual row in this table
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            .. attribute:: ccontextmappingbridgedomainstoragetype
            
            	The storage type for this conceptual row.  Conceptual rows having the value 'permanent' need not allow write\-access to any columnar objects in the row
            	**type**\:   :py:class:`StoragetypeEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.StoragetypeEnum>`
            
            

            """

            _prefix = 'CISCO-CONTEXT-MAPPING-MIB'
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
                    raise YPYModelError('Key property ccontextmappingvacmcontextname is None')

                return '/CISCO-CONTEXT-MAPPING-MIB:CISCO-CONTEXT-MAPPING-MIB/CISCO-CONTEXT-MAPPING-MIB:cContextMappingBridgeDomainTable/CISCO-CONTEXT-MAPPING-MIB:cContextMappingBridgeDomainEntry[CISCO-CONTEXT-MAPPING-MIB:cContextMappingVacmContextName = ' + str(self.ccontextmappingvacmcontextname) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ccontextmappingvacmcontextname is not None:
                    return True

                if self.ccontextmappingbridgedomainidentifier is not None:
                    return True

                if self.ccontextmappingbridgedomainrowstatus is not None:
                    return True

                if self.ccontextmappingbridgedomainstoragetype is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_CONTEXT_MAPPING_MIB as meta
                return meta._meta_table['CiscoContextMappingMib.Ccontextmappingbridgedomaintable.Ccontextmappingbridgedomainentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-CONTEXT-MAPPING-MIB:CISCO-CONTEXT-MAPPING-MIB/CISCO-CONTEXT-MAPPING-MIB:cContextMappingBridgeDomainTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.ccontextmappingbridgedomainentry is not None:
                for child_ref in self.ccontextmappingbridgedomainentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_CONTEXT_MAPPING_MIB as meta
            return meta._meta_table['CiscoContextMappingMib.Ccontextmappingbridgedomaintable']['meta_info']


    class Ccontextmappingbridgeinstancetable(object):
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
        	**type**\: list of    :py:class:`Ccontextmappingbridgeinstanceentry <ydk.models.cisco_ios_xe.CISCO_CONTEXT_MAPPING_MIB.CiscoContextMappingMib.Ccontextmappingbridgeinstancetable.Ccontextmappingbridgeinstanceentry>`
        
        

        """

        _prefix = 'CISCO-CONTEXT-MAPPING-MIB'
        _revision = '2008-11-22'

        def __init__(self):
            self.parent = None
            self.ccontextmappingbridgeinstanceentry = YList()
            self.ccontextmappingbridgeinstanceentry.parent = self
            self.ccontextmappingbridgeinstanceentry.name = 'ccontextmappingbridgeinstanceentry'


        class Ccontextmappingbridgeinstanceentry(object):
            """
            Information relating to a single mapping of
            cContextMappingVacmContextName to the 
            corresponding bridge instance.
            
            To create a row in this table, a manager must set
            cContextMappingBridgeInstRowStatus to either 
            'createAndGo' or 'createAndWait'.
            
            To delete a row in this table, a manager must set
            cContextMappingBridgeInstRowStatus to 'destroy'.
            
            .. attribute:: ccontextmappingvacmcontextname  <key>
            
            	
            	**type**\:  str
            
            	**length:** 0..32
            
            	**refers to**\:  :py:class:`ccontextmappingvacmcontextname <ydk.models.cisco_ios_xe.CISCO_CONTEXT_MAPPING_MIB.CiscoContextMappingMib.Ccontextmappingtable.Ccontextmappingentry>`
            
            .. attribute:: ccontextmappingbridgeinstname
            
            	The object identifies the name given to bridge instance to which the SNMP context is mapped to.  Value of this object cannot be changed when the  RowStatus object in the same row is 'active'.  This is typically a human\-readable string. This is the same ASCII string used in the router's console interface to refer to this bridge instance.  When the value of this object is a zero length string, it indicates that the SNMP context is independent of any bridge instances
            	**type**\:  str
            
            .. attribute:: ccontextmappingbridgeinstrowstatus
            
            	This object facilitates the creation, modification, or deletion of a conceptual row in this table
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            .. attribute:: ccontextmappingbridgeinststoragetype
            
            	The storage type for this conceptual row.  Value of this object cannot be changed when the  RowStatus object in the same row is 'active'.  Conceptual rows having the value 'permanent' need not allow write\-access to any columnar objects in the row
            	**type**\:   :py:class:`StoragetypeEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.StoragetypeEnum>`
            
            

            """

            _prefix = 'CISCO-CONTEXT-MAPPING-MIB'
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
                    raise YPYModelError('Key property ccontextmappingvacmcontextname is None')

                return '/CISCO-CONTEXT-MAPPING-MIB:CISCO-CONTEXT-MAPPING-MIB/CISCO-CONTEXT-MAPPING-MIB:cContextMappingBridgeInstanceTable/CISCO-CONTEXT-MAPPING-MIB:cContextMappingBridgeInstanceEntry[CISCO-CONTEXT-MAPPING-MIB:cContextMappingVacmContextName = ' + str(self.ccontextmappingvacmcontextname) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ccontextmappingvacmcontextname is not None:
                    return True

                if self.ccontextmappingbridgeinstname is not None:
                    return True

                if self.ccontextmappingbridgeinstrowstatus is not None:
                    return True

                if self.ccontextmappingbridgeinststoragetype is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_CONTEXT_MAPPING_MIB as meta
                return meta._meta_table['CiscoContextMappingMib.Ccontextmappingbridgeinstancetable.Ccontextmappingbridgeinstanceentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-CONTEXT-MAPPING-MIB:CISCO-CONTEXT-MAPPING-MIB/CISCO-CONTEXT-MAPPING-MIB:cContextMappingBridgeInstanceTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.ccontextmappingbridgeinstanceentry is not None:
                for child_ref in self.ccontextmappingbridgeinstanceentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_CONTEXT_MAPPING_MIB as meta
            return meta._meta_table['CiscoContextMappingMib.Ccontextmappingbridgeinstancetable']['meta_info']


    class Ccontextmappinglicensegrouptable(object):
        """
        This table contains information on which
        cContextMappingVacmContextName is mapped to
        which License Group.
        Group level licensing is used where each
        Technology Package is enabled via a License.
        
        .. attribute:: ccontextmappinglicensegroupentry
        
        	Information relating to a single mapping of CContextMappingVacmContextName to the corresponding License Group
        	**type**\: list of    :py:class:`Ccontextmappinglicensegroupentry <ydk.models.cisco_ios_xe.CISCO_CONTEXT_MAPPING_MIB.CiscoContextMappingMib.Ccontextmappinglicensegrouptable.Ccontextmappinglicensegroupentry>`
        
        

        """

        _prefix = 'CISCO-CONTEXT-MAPPING-MIB'
        _revision = '2008-11-22'

        def __init__(self):
            self.parent = None
            self.ccontextmappinglicensegroupentry = YList()
            self.ccontextmappinglicensegroupentry.parent = self
            self.ccontextmappinglicensegroupentry.name = 'ccontextmappinglicensegroupentry'


        class Ccontextmappinglicensegroupentry(object):
            """
            Information relating to a single mapping of
            CContextMappingVacmContextName to the
            corresponding License Group.
            
            .. attribute:: ccontextmappingvacmcontextname  <key>
            
            	
            	**type**\:  str
            
            	**length:** 0..32
            
            	**refers to**\:  :py:class:`ccontextmappingvacmcontextname <ydk.models.cisco_ios_xe.CISCO_CONTEXT_MAPPING_MIB.CiscoContextMappingMib.Ccontextmappingtable.Ccontextmappingentry>`
            
            .. attribute:: ccontextmappinglicensegroupname
            
            	The value of an instance of this object identifies the name given to the Group to which the SNMP context is mapped.  Feature sets from all groups will be combined to form  universal image. User can configure multiple groups as needed.  For example\: In Next generation ISRs will use the universal image package level licensing model for its licensing need. Each group has the feature set needed for that specific technology. Feature sets from different groups are combined to  form universal image and each feature set for a group  can be enabled using a valid license key. There will  be a base level ipbase package in which the router  boots with out any license key.  The following are the different Technology Groups. 1.crypto 2.data 3.ip 4.legacy 5.novpn\-security 6.security 7.uc
            	**type**\:  str
            
            	**length:** 0..32
            
            .. attribute:: ccontextmappinglicensegrouprowstatus
            
            	This object facilitates the creation, modification, or deletion of a conceptual row in this table
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            .. attribute:: ccontextmappinglicensegroupstoragetype
            
            	The storage type for this conceptual row.  Conceptual rows having the value 'permanent' need not allow write\-access to any columnar objects in the row
            	**type**\:   :py:class:`StoragetypeEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.StoragetypeEnum>`
            
            

            """

            _prefix = 'CISCO-CONTEXT-MAPPING-MIB'
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
                    raise YPYModelError('Key property ccontextmappingvacmcontextname is None')

                return '/CISCO-CONTEXT-MAPPING-MIB:CISCO-CONTEXT-MAPPING-MIB/CISCO-CONTEXT-MAPPING-MIB:cContextMappingLicenseGroupTable/CISCO-CONTEXT-MAPPING-MIB:cContextMappingLicenseGroupEntry[CISCO-CONTEXT-MAPPING-MIB:cContextMappingVacmContextName = ' + str(self.ccontextmappingvacmcontextname) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ccontextmappingvacmcontextname is not None:
                    return True

                if self.ccontextmappinglicensegroupname is not None:
                    return True

                if self.ccontextmappinglicensegrouprowstatus is not None:
                    return True

                if self.ccontextmappinglicensegroupstoragetype is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_CONTEXT_MAPPING_MIB as meta
                return meta._meta_table['CiscoContextMappingMib.Ccontextmappinglicensegrouptable.Ccontextmappinglicensegroupentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-CONTEXT-MAPPING-MIB:CISCO-CONTEXT-MAPPING-MIB/CISCO-CONTEXT-MAPPING-MIB:cContextMappingLicenseGroupTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.ccontextmappinglicensegroupentry is not None:
                for child_ref in self.ccontextmappinglicensegroupentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_CONTEXT_MAPPING_MIB as meta
            return meta._meta_table['CiscoContextMappingMib.Ccontextmappinglicensegrouptable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-CONTEXT-MAPPING-MIB:CISCO-CONTEXT-MAPPING-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.ccontextmappingbridgedomaintable is not None and self.ccontextmappingbridgedomaintable._has_data():
            return True

        if self.ccontextmappingbridgeinstancetable is not None and self.ccontextmappingbridgeinstancetable._has_data():
            return True

        if self.ccontextmappinglicensegrouptable is not None and self.ccontextmappinglicensegrouptable._has_data():
            return True

        if self.ccontextmappingtable is not None and self.ccontextmappingtable._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_CONTEXT_MAPPING_MIB as meta
        return meta._meta_table['CiscoContextMappingMib']['meta_info']


