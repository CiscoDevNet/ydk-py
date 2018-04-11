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
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CISCOCONTEXTMAPPINGMIB(Entity):
    """
    
    
    .. attribute:: ccontextmappingtable
    
    	This table contains information on which cContextMappingVacmContextName is mapped to which VRF, topology, and routing protocol instance.  This table is indexed by SNMP VACM context.  Configuring a row in this table for an SNMP context does not require that the context be already defined, i.e., a row can be created in this table for a context before the corresponding row is created in RFC 3415's vacmContextTable.  To create a row in this table, a manager must set cContextMappingRowStatus to either 'createAndGo' or 'createAndWait'.  To delete a row in this table, a manager must set cContextMappingRowStatus to 'destroy'
    	**type**\:  :py:class:`Ccontextmappingtable <ydk.models.cisco_ios_xe.CISCO_CONTEXT_MAPPING_MIB.CISCOCONTEXTMAPPINGMIB.Ccontextmappingtable>`
    
    .. attribute:: ccontextmappingbridgedomaintable
    
    	This table contains information on which cContextMappingVacmContextName is mapped to which bridge domain.  A Bridge Domain is one of the means by which it is possible  to define an Ethernet broadcast domain on a bridging device.  A network can have multiple broadcast domains configured. This table helps the network management personnel to find  out the  details of various broadcast domains configured  in the network.  An entry need to exist in cContextMappingTable, to create  an entry in this table
    	**type**\:  :py:class:`Ccontextmappingbridgedomaintable <ydk.models.cisco_ios_xe.CISCO_CONTEXT_MAPPING_MIB.CISCOCONTEXTMAPPINGMIB.Ccontextmappingbridgedomaintable>`
    
    .. attribute:: ccontextmappingbridgeinstancetable
    
    	This table contains information on mapping between cContextMappingVacmContextName and bridge instance.  Bridge instance is an instance of a physical or logical  bridge which has unique bridge\-id.  If an entry is deleted from cContextMappingTable, the corresponding entry in this table will also get deleted.  If an entry needs to be created in this table, the corresponding entry must exist in cContextMappingTable
    	**type**\:  :py:class:`Ccontextmappingbridgeinstancetable <ydk.models.cisco_ios_xe.CISCO_CONTEXT_MAPPING_MIB.CISCOCONTEXTMAPPINGMIB.Ccontextmappingbridgeinstancetable>`
    
    .. attribute:: ccontextmappinglicensegrouptable
    
    	This table contains information on which cContextMappingVacmContextName is mapped to which License Group. Group level licensing is used where each Technology Package is enabled via a License
    	**type**\:  :py:class:`Ccontextmappinglicensegrouptable <ydk.models.cisco_ios_xe.CISCO_CONTEXT_MAPPING_MIB.CISCOCONTEXTMAPPINGMIB.Ccontextmappinglicensegrouptable>`
    
    

    """

    _prefix = 'CISCO-CONTEXT-MAPPING-MIB'
    _revision = '2008-11-22'

    def __init__(self):
        super(CISCOCONTEXTMAPPINGMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-CONTEXT-MAPPING-MIB"
        self.yang_parent_name = "CISCO-CONTEXT-MAPPING-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("cContextMappingTable", ("ccontextmappingtable", CISCOCONTEXTMAPPINGMIB.Ccontextmappingtable)), ("cContextMappingBridgeDomainTable", ("ccontextmappingbridgedomaintable", CISCOCONTEXTMAPPINGMIB.Ccontextmappingbridgedomaintable)), ("cContextMappingBridgeInstanceTable", ("ccontextmappingbridgeinstancetable", CISCOCONTEXTMAPPINGMIB.Ccontextmappingbridgeinstancetable)), ("cContextMappingLicenseGroupTable", ("ccontextmappinglicensegrouptable", CISCOCONTEXTMAPPINGMIB.Ccontextmappinglicensegrouptable))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.ccontextmappingtable = CISCOCONTEXTMAPPINGMIB.Ccontextmappingtable()
        self.ccontextmappingtable.parent = self
        self._children_name_map["ccontextmappingtable"] = "cContextMappingTable"
        self._children_yang_names.add("cContextMappingTable")

        self.ccontextmappingbridgedomaintable = CISCOCONTEXTMAPPINGMIB.Ccontextmappingbridgedomaintable()
        self.ccontextmappingbridgedomaintable.parent = self
        self._children_name_map["ccontextmappingbridgedomaintable"] = "cContextMappingBridgeDomainTable"
        self._children_yang_names.add("cContextMappingBridgeDomainTable")

        self.ccontextmappingbridgeinstancetable = CISCOCONTEXTMAPPINGMIB.Ccontextmappingbridgeinstancetable()
        self.ccontextmappingbridgeinstancetable.parent = self
        self._children_name_map["ccontextmappingbridgeinstancetable"] = "cContextMappingBridgeInstanceTable"
        self._children_yang_names.add("cContextMappingBridgeInstanceTable")

        self.ccontextmappinglicensegrouptable = CISCOCONTEXTMAPPINGMIB.Ccontextmappinglicensegrouptable()
        self.ccontextmappinglicensegrouptable.parent = self
        self._children_name_map["ccontextmappinglicensegrouptable"] = "cContextMappingLicenseGroupTable"
        self._children_yang_names.add("cContextMappingLicenseGroupTable")
        self._segment_path = lambda: "CISCO-CONTEXT-MAPPING-MIB:CISCO-CONTEXT-MAPPING-MIB"


    class Ccontextmappingtable(Entity):
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
        	**type**\: list of  		 :py:class:`Ccontextmappingentry <ydk.models.cisco_ios_xe.CISCO_CONTEXT_MAPPING_MIB.CISCOCONTEXTMAPPINGMIB.Ccontextmappingtable.Ccontextmappingentry>`
        
        

        """

        _prefix = 'CISCO-CONTEXT-MAPPING-MIB'
        _revision = '2008-11-22'

        def __init__(self):
            super(CISCOCONTEXTMAPPINGMIB.Ccontextmappingtable, self).__init__()

            self.yang_name = "cContextMappingTable"
            self.yang_parent_name = "CISCO-CONTEXT-MAPPING-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cContextMappingEntry", ("ccontextmappingentry", CISCOCONTEXTMAPPINGMIB.Ccontextmappingtable.Ccontextmappingentry))])
            self._leafs = OrderedDict()

            self.ccontextmappingentry = YList(self)
            self._segment_path = lambda: "cContextMappingTable"
            self._absolute_path = lambda: "CISCO-CONTEXT-MAPPING-MIB:CISCO-CONTEXT-MAPPING-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOCONTEXTMAPPINGMIB.Ccontextmappingtable, [], name, value)


        class Ccontextmappingentry(Entity):
            """
            Information relating to a single mapping of
            cContextMappingVacmContextName to the corresponding VRF,
            the corresponding topology, and the corresponding routing
            protocol instance.
            
            .. attribute:: ccontextmappingvacmcontextname  (key)
            
            	The vacmContextName given to the SNMP context.  This is a human readable name identifying a particular SNMP VACM context at a particular SNMP entity. The empty contextName (zero length) represents the default context
            	**type**\: str
            
            	**length:** 0..32
            
            .. attribute:: ccontextmappingvrfname
            
            	The value of an instance of this object identifies the name given to the VRF to which the SNMP context is mapped to.  This is typically a human\-readable string. This is the same ASCII string used in the router's console interface to refer to this VRF.  When the value of this object is the zero length string it indicates that the SNMP context is independent of any VRF
            	**type**\: str
            
            	**length:** 0..32
            
            .. attribute:: ccontextmappingtopologyname
            
            	The value of an instance of this object identifies the name given to the topology to which the SNMP context is mapped to.  This is typically a human\-readable string. This is the same ASCII string used in the router's console interface to refer to this topology.  When the value of this object is the zero length string it indicates that the SNMP context is independent of any topology
            	**type**\: str
            
            	**length:** 0..32
            
            .. attribute:: ccontextmappingprotoinstname
            
            	The value of an instance of this object identifies the name given to the protocol instance to which the SNMP context is mapped to.  This is typically a human\-readable string. This is the same ASCII string used in the router's console interface to refer to this protocol instance.  When the value of this object is the zero length string it indicates that the SNMP context is independent of any protocol instance
            	**type**\: str
            
            	**length:** 0..32
            
            .. attribute:: ccontextmappingstoragetype
            
            	The storage type for this conceptual row.  Conceptual rows having the value 'permanent' need not allow write\-access to any columnar objects in the row
            	**type**\:  :py:class:`StorageType <ydk.models.cisco_ios_xe.SNMPv2_TC.StorageType>`
            
            .. attribute:: ccontextmappingrowstatus
            
            	This object facilitates the creation, modification, or deletion of a conceptual row in this table
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            

            """

            _prefix = 'CISCO-CONTEXT-MAPPING-MIB'
            _revision = '2008-11-22'

            def __init__(self):
                super(CISCOCONTEXTMAPPINGMIB.Ccontextmappingtable.Ccontextmappingentry, self).__init__()

                self.yang_name = "cContextMappingEntry"
                self.yang_parent_name = "cContextMappingTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ccontextmappingvacmcontextname']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ccontextmappingvacmcontextname', YLeaf(YType.str, 'cContextMappingVacmContextName')),
                    ('ccontextmappingvrfname', YLeaf(YType.str, 'cContextMappingVrfName')),
                    ('ccontextmappingtopologyname', YLeaf(YType.str, 'cContextMappingTopologyName')),
                    ('ccontextmappingprotoinstname', YLeaf(YType.str, 'cContextMappingProtoInstName')),
                    ('ccontextmappingstoragetype', YLeaf(YType.enumeration, 'cContextMappingStorageType')),
                    ('ccontextmappingrowstatus', YLeaf(YType.enumeration, 'cContextMappingRowStatus')),
                ])
                self.ccontextmappingvacmcontextname = None
                self.ccontextmappingvrfname = None
                self.ccontextmappingtopologyname = None
                self.ccontextmappingprotoinstname = None
                self.ccontextmappingstoragetype = None
                self.ccontextmappingrowstatus = None
                self._segment_path = lambda: "cContextMappingEntry" + "[cContextMappingVacmContextName='" + str(self.ccontextmappingvacmcontextname) + "']"
                self._absolute_path = lambda: "CISCO-CONTEXT-MAPPING-MIB:CISCO-CONTEXT-MAPPING-MIB/cContextMappingTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOCONTEXTMAPPINGMIB.Ccontextmappingtable.Ccontextmappingentry, ['ccontextmappingvacmcontextname', 'ccontextmappingvrfname', 'ccontextmappingtopologyname', 'ccontextmappingprotoinstname', 'ccontextmappingstoragetype', 'ccontextmappingrowstatus'], name, value)


    class Ccontextmappingbridgedomaintable(Entity):
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
        	**type**\: list of  		 :py:class:`Ccontextmappingbridgedomainentry <ydk.models.cisco_ios_xe.CISCO_CONTEXT_MAPPING_MIB.CISCOCONTEXTMAPPINGMIB.Ccontextmappingbridgedomaintable.Ccontextmappingbridgedomainentry>`
        
        

        """

        _prefix = 'CISCO-CONTEXT-MAPPING-MIB'
        _revision = '2008-11-22'

        def __init__(self):
            super(CISCOCONTEXTMAPPINGMIB.Ccontextmappingbridgedomaintable, self).__init__()

            self.yang_name = "cContextMappingBridgeDomainTable"
            self.yang_parent_name = "CISCO-CONTEXT-MAPPING-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cContextMappingBridgeDomainEntry", ("ccontextmappingbridgedomainentry", CISCOCONTEXTMAPPINGMIB.Ccontextmappingbridgedomaintable.Ccontextmappingbridgedomainentry))])
            self._leafs = OrderedDict()

            self.ccontextmappingbridgedomainentry = YList(self)
            self._segment_path = lambda: "cContextMappingBridgeDomainTable"
            self._absolute_path = lambda: "CISCO-CONTEXT-MAPPING-MIB:CISCO-CONTEXT-MAPPING-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOCONTEXTMAPPINGMIB.Ccontextmappingbridgedomaintable, [], name, value)


        class Ccontextmappingbridgedomainentry(Entity):
            """
            Information relating to a single mapping of
            cContextMappingVacmContextName to the 
            corresponding bridge domain.
            
            To create a row in this table, a manager must set
            cContextMappingBridgeDomainRowStatus to either 
            'createAndGo' or 'createAndWait'.
            
            To delete a row in this table, a manager must set
            cContextMappingBridgeDomainRowStatus to 'destroy'.
            
            .. attribute:: ccontextmappingvacmcontextname  (key)
            
            	
            	**type**\: str
            
            	**length:** 0..32
            
            	**refers to**\:  :py:class:`ccontextmappingvacmcontextname <ydk.models.cisco_ios_xe.CISCO_CONTEXT_MAPPING_MIB.CISCOCONTEXTMAPPINGMIB.Ccontextmappingtable.Ccontextmappingentry>`
            
            .. attribute:: ccontextmappingbridgedomainidentifier
            
            	The value of an instance of this object identifies the bridge domain to which the SNMP context is  mapped to
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: ccontextmappingbridgedomainstoragetype
            
            	The storage type for this conceptual row.  Conceptual rows having the value 'permanent' need not allow write\-access to any columnar objects in the row
            	**type**\:  :py:class:`StorageType <ydk.models.cisco_ios_xe.SNMPv2_TC.StorageType>`
            
            .. attribute:: ccontextmappingbridgedomainrowstatus
            
            	This object facilitates the creation, modification, or deletion of a conceptual row in this table
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            

            """

            _prefix = 'CISCO-CONTEXT-MAPPING-MIB'
            _revision = '2008-11-22'

            def __init__(self):
                super(CISCOCONTEXTMAPPINGMIB.Ccontextmappingbridgedomaintable.Ccontextmappingbridgedomainentry, self).__init__()

                self.yang_name = "cContextMappingBridgeDomainEntry"
                self.yang_parent_name = "cContextMappingBridgeDomainTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ccontextmappingvacmcontextname']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ccontextmappingvacmcontextname', YLeaf(YType.str, 'cContextMappingVacmContextName')),
                    ('ccontextmappingbridgedomainidentifier', YLeaf(YType.uint32, 'cContextMappingBridgeDomainIdentifier')),
                    ('ccontextmappingbridgedomainstoragetype', YLeaf(YType.enumeration, 'cContextMappingBridgeDomainStorageType')),
                    ('ccontextmappingbridgedomainrowstatus', YLeaf(YType.enumeration, 'cContextMappingBridgeDomainRowStatus')),
                ])
                self.ccontextmappingvacmcontextname = None
                self.ccontextmappingbridgedomainidentifier = None
                self.ccontextmappingbridgedomainstoragetype = None
                self.ccontextmappingbridgedomainrowstatus = None
                self._segment_path = lambda: "cContextMappingBridgeDomainEntry" + "[cContextMappingVacmContextName='" + str(self.ccontextmappingvacmcontextname) + "']"
                self._absolute_path = lambda: "CISCO-CONTEXT-MAPPING-MIB:CISCO-CONTEXT-MAPPING-MIB/cContextMappingBridgeDomainTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOCONTEXTMAPPINGMIB.Ccontextmappingbridgedomaintable.Ccontextmappingbridgedomainentry, ['ccontextmappingvacmcontextname', 'ccontextmappingbridgedomainidentifier', 'ccontextmappingbridgedomainstoragetype', 'ccontextmappingbridgedomainrowstatus'], name, value)


    class Ccontextmappingbridgeinstancetable(Entity):
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
        	**type**\: list of  		 :py:class:`Ccontextmappingbridgeinstanceentry <ydk.models.cisco_ios_xe.CISCO_CONTEXT_MAPPING_MIB.CISCOCONTEXTMAPPINGMIB.Ccontextmappingbridgeinstancetable.Ccontextmappingbridgeinstanceentry>`
        
        

        """

        _prefix = 'CISCO-CONTEXT-MAPPING-MIB'
        _revision = '2008-11-22'

        def __init__(self):
            super(CISCOCONTEXTMAPPINGMIB.Ccontextmappingbridgeinstancetable, self).__init__()

            self.yang_name = "cContextMappingBridgeInstanceTable"
            self.yang_parent_name = "CISCO-CONTEXT-MAPPING-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cContextMappingBridgeInstanceEntry", ("ccontextmappingbridgeinstanceentry", CISCOCONTEXTMAPPINGMIB.Ccontextmappingbridgeinstancetable.Ccontextmappingbridgeinstanceentry))])
            self._leafs = OrderedDict()

            self.ccontextmappingbridgeinstanceentry = YList(self)
            self._segment_path = lambda: "cContextMappingBridgeInstanceTable"
            self._absolute_path = lambda: "CISCO-CONTEXT-MAPPING-MIB:CISCO-CONTEXT-MAPPING-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOCONTEXTMAPPINGMIB.Ccontextmappingbridgeinstancetable, [], name, value)


        class Ccontextmappingbridgeinstanceentry(Entity):
            """
            Information relating to a single mapping of
            cContextMappingVacmContextName to the 
            corresponding bridge instance.
            
            To create a row in this table, a manager must set
            cContextMappingBridgeInstRowStatus to either 
            'createAndGo' or 'createAndWait'.
            
            To delete a row in this table, a manager must set
            cContextMappingBridgeInstRowStatus to 'destroy'.
            
            .. attribute:: ccontextmappingvacmcontextname  (key)
            
            	
            	**type**\: str
            
            	**length:** 0..32
            
            	**refers to**\:  :py:class:`ccontextmappingvacmcontextname <ydk.models.cisco_ios_xe.CISCO_CONTEXT_MAPPING_MIB.CISCOCONTEXTMAPPINGMIB.Ccontextmappingtable.Ccontextmappingentry>`
            
            .. attribute:: ccontextmappingbridgeinstname
            
            	The object identifies the name given to bridge instance to which the SNMP context is mapped to.  Value of this object cannot be changed when the  RowStatus object in the same row is 'active'.  This is typically a human\-readable string. This is the same ASCII string used in the router's console interface to refer to this bridge instance.  When the value of this object is a zero length string, it indicates that the SNMP context is independent of any bridge instances
            	**type**\: str
            
            .. attribute:: ccontextmappingbridgeinststoragetype
            
            	The storage type for this conceptual row.  Value of this object cannot be changed when the  RowStatus object in the same row is 'active'.  Conceptual rows having the value 'permanent' need not allow write\-access to any columnar objects in the row
            	**type**\:  :py:class:`StorageType <ydk.models.cisco_ios_xe.SNMPv2_TC.StorageType>`
            
            .. attribute:: ccontextmappingbridgeinstrowstatus
            
            	This object facilitates the creation, modification, or deletion of a conceptual row in this table
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            

            """

            _prefix = 'CISCO-CONTEXT-MAPPING-MIB'
            _revision = '2008-11-22'

            def __init__(self):
                super(CISCOCONTEXTMAPPINGMIB.Ccontextmappingbridgeinstancetable.Ccontextmappingbridgeinstanceentry, self).__init__()

                self.yang_name = "cContextMappingBridgeInstanceEntry"
                self.yang_parent_name = "cContextMappingBridgeInstanceTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ccontextmappingvacmcontextname']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ccontextmappingvacmcontextname', YLeaf(YType.str, 'cContextMappingVacmContextName')),
                    ('ccontextmappingbridgeinstname', YLeaf(YType.str, 'cContextMappingBridgeInstName')),
                    ('ccontextmappingbridgeinststoragetype', YLeaf(YType.enumeration, 'cContextMappingBridgeInstStorageType')),
                    ('ccontextmappingbridgeinstrowstatus', YLeaf(YType.enumeration, 'cContextMappingBridgeInstRowStatus')),
                ])
                self.ccontextmappingvacmcontextname = None
                self.ccontextmappingbridgeinstname = None
                self.ccontextmappingbridgeinststoragetype = None
                self.ccontextmappingbridgeinstrowstatus = None
                self._segment_path = lambda: "cContextMappingBridgeInstanceEntry" + "[cContextMappingVacmContextName='" + str(self.ccontextmappingvacmcontextname) + "']"
                self._absolute_path = lambda: "CISCO-CONTEXT-MAPPING-MIB:CISCO-CONTEXT-MAPPING-MIB/cContextMappingBridgeInstanceTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOCONTEXTMAPPINGMIB.Ccontextmappingbridgeinstancetable.Ccontextmappingbridgeinstanceentry, ['ccontextmappingvacmcontextname', 'ccontextmappingbridgeinstname', 'ccontextmappingbridgeinststoragetype', 'ccontextmappingbridgeinstrowstatus'], name, value)


    class Ccontextmappinglicensegrouptable(Entity):
        """
        This table contains information on which
        cContextMappingVacmContextName is mapped to
        which License Group.
        Group level licensing is used where each
        Technology Package is enabled via a License.
        
        .. attribute:: ccontextmappinglicensegroupentry
        
        	Information relating to a single mapping of CContextMappingVacmContextName to the corresponding License Group
        	**type**\: list of  		 :py:class:`Ccontextmappinglicensegroupentry <ydk.models.cisco_ios_xe.CISCO_CONTEXT_MAPPING_MIB.CISCOCONTEXTMAPPINGMIB.Ccontextmappinglicensegrouptable.Ccontextmappinglicensegroupentry>`
        
        

        """

        _prefix = 'CISCO-CONTEXT-MAPPING-MIB'
        _revision = '2008-11-22'

        def __init__(self):
            super(CISCOCONTEXTMAPPINGMIB.Ccontextmappinglicensegrouptable, self).__init__()

            self.yang_name = "cContextMappingLicenseGroupTable"
            self.yang_parent_name = "CISCO-CONTEXT-MAPPING-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cContextMappingLicenseGroupEntry", ("ccontextmappinglicensegroupentry", CISCOCONTEXTMAPPINGMIB.Ccontextmappinglicensegrouptable.Ccontextmappinglicensegroupentry))])
            self._leafs = OrderedDict()

            self.ccontextmappinglicensegroupentry = YList(self)
            self._segment_path = lambda: "cContextMappingLicenseGroupTable"
            self._absolute_path = lambda: "CISCO-CONTEXT-MAPPING-MIB:CISCO-CONTEXT-MAPPING-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOCONTEXTMAPPINGMIB.Ccontextmappinglicensegrouptable, [], name, value)


        class Ccontextmappinglicensegroupentry(Entity):
            """
            Information relating to a single mapping of
            CContextMappingVacmContextName to the
            corresponding License Group.
            
            .. attribute:: ccontextmappingvacmcontextname  (key)
            
            	
            	**type**\: str
            
            	**length:** 0..32
            
            	**refers to**\:  :py:class:`ccontextmappingvacmcontextname <ydk.models.cisco_ios_xe.CISCO_CONTEXT_MAPPING_MIB.CISCOCONTEXTMAPPINGMIB.Ccontextmappingtable.Ccontextmappingentry>`
            
            .. attribute:: ccontextmappinglicensegroupname
            
            	The value of an instance of this object identifies the name given to the Group to which the SNMP context is mapped.  Feature sets from all groups will be combined to form  universal image. User can configure multiple groups as needed.  For example\: In Next generation ISRs will use the universal image package level licensing model for its licensing need. Each group has the feature set needed for that specific technology. Feature sets from different groups are combined to  form universal image and each feature set for a group  can be enabled using a valid license key. There will  be a base level ipbase package in which the router  boots with out any license key.  The following are the different Technology Groups. 1.crypto 2.data 3.ip 4.legacy 5.novpn\-security 6.security 7.uc
            	**type**\: str
            
            	**length:** 0..32
            
            .. attribute:: ccontextmappinglicensegroupstoragetype
            
            	The storage type for this conceptual row.  Conceptual rows having the value 'permanent' need not allow write\-access to any columnar objects in the row
            	**type**\:  :py:class:`StorageType <ydk.models.cisco_ios_xe.SNMPv2_TC.StorageType>`
            
            .. attribute:: ccontextmappinglicensegrouprowstatus
            
            	This object facilitates the creation, modification, or deletion of a conceptual row in this table
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            

            """

            _prefix = 'CISCO-CONTEXT-MAPPING-MIB'
            _revision = '2008-11-22'

            def __init__(self):
                super(CISCOCONTEXTMAPPINGMIB.Ccontextmappinglicensegrouptable.Ccontextmappinglicensegroupentry, self).__init__()

                self.yang_name = "cContextMappingLicenseGroupEntry"
                self.yang_parent_name = "cContextMappingLicenseGroupTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ccontextmappingvacmcontextname']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ccontextmappingvacmcontextname', YLeaf(YType.str, 'cContextMappingVacmContextName')),
                    ('ccontextmappinglicensegroupname', YLeaf(YType.str, 'cContextMappingLicenseGroupName')),
                    ('ccontextmappinglicensegroupstoragetype', YLeaf(YType.enumeration, 'cContextMappingLicenseGroupStorageType')),
                    ('ccontextmappinglicensegrouprowstatus', YLeaf(YType.enumeration, 'cContextMappingLicenseGroupRowStatus')),
                ])
                self.ccontextmappingvacmcontextname = None
                self.ccontextmappinglicensegroupname = None
                self.ccontextmappinglicensegroupstoragetype = None
                self.ccontextmappinglicensegrouprowstatus = None
                self._segment_path = lambda: "cContextMappingLicenseGroupEntry" + "[cContextMappingVacmContextName='" + str(self.ccontextmappingvacmcontextname) + "']"
                self._absolute_path = lambda: "CISCO-CONTEXT-MAPPING-MIB:CISCO-CONTEXT-MAPPING-MIB/cContextMappingLicenseGroupTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOCONTEXTMAPPINGMIB.Ccontextmappinglicensegrouptable.Ccontextmappinglicensegroupentry, ['ccontextmappingvacmcontextname', 'ccontextmappinglicensegroupname', 'ccontextmappinglicensegroupstoragetype', 'ccontextmappinglicensegrouprowstatus'], name, value)

    def clone_ptr(self):
        self._top_entity = CISCOCONTEXTMAPPINGMIB()
        return self._top_entity

