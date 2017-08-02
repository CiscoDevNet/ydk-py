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
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CiscoContextMappingMib(Entity):
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
        super(CiscoContextMappingMib, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-CONTEXT-MAPPING-MIB"
        self.yang_parent_name = "CISCO-CONTEXT-MAPPING-MIB"

        self.ccontextmappingbridgedomaintable = CiscoContextMappingMib.Ccontextmappingbridgedomaintable()
        self.ccontextmappingbridgedomaintable.parent = self
        self._children_name_map["ccontextmappingbridgedomaintable"] = "cContextMappingBridgeDomainTable"
        self._children_yang_names.add("cContextMappingBridgeDomainTable")

        self.ccontextmappingbridgeinstancetable = CiscoContextMappingMib.Ccontextmappingbridgeinstancetable()
        self.ccontextmappingbridgeinstancetable.parent = self
        self._children_name_map["ccontextmappingbridgeinstancetable"] = "cContextMappingBridgeInstanceTable"
        self._children_yang_names.add("cContextMappingBridgeInstanceTable")

        self.ccontextmappinglicensegrouptable = CiscoContextMappingMib.Ccontextmappinglicensegrouptable()
        self.ccontextmappinglicensegrouptable.parent = self
        self._children_name_map["ccontextmappinglicensegrouptable"] = "cContextMappingLicenseGroupTable"
        self._children_yang_names.add("cContextMappingLicenseGroupTable")

        self.ccontextmappingtable = CiscoContextMappingMib.Ccontextmappingtable()
        self.ccontextmappingtable.parent = self
        self._children_name_map["ccontextmappingtable"] = "cContextMappingTable"
        self._children_yang_names.add("cContextMappingTable")


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
        	**type**\: list of    :py:class:`Ccontextmappingentry <ydk.models.cisco_ios_xe.CISCO_CONTEXT_MAPPING_MIB.CiscoContextMappingMib.Ccontextmappingtable.Ccontextmappingentry>`
        
        

        """

        _prefix = 'CISCO-CONTEXT-MAPPING-MIB'
        _revision = '2008-11-22'

        def __init__(self):
            super(CiscoContextMappingMib.Ccontextmappingtable, self).__init__()

            self.yang_name = "cContextMappingTable"
            self.yang_parent_name = "CISCO-CONTEXT-MAPPING-MIB"

            self.ccontextmappingentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoContextMappingMib.Ccontextmappingtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoContextMappingMib.Ccontextmappingtable, self).__setattr__(name, value)


        class Ccontextmappingentry(Entity):
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
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: ccontextmappingstoragetype
            
            	The storage type for this conceptual row.  Conceptual rows having the value 'permanent' need not allow write\-access to any columnar objects in the row
            	**type**\:   :py:class:`Storagetype <ydk.models.cisco_ios_xe.SNMPv2_TC.Storagetype>`
            
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
                super(CiscoContextMappingMib.Ccontextmappingtable.Ccontextmappingentry, self).__init__()

                self.yang_name = "cContextMappingEntry"
                self.yang_parent_name = "cContextMappingTable"

                self.ccontextmappingvacmcontextname = YLeaf(YType.str, "cContextMappingVacmContextName")

                self.ccontextmappingprotoinstname = YLeaf(YType.str, "cContextMappingProtoInstName")

                self.ccontextmappingrowstatus = YLeaf(YType.enumeration, "cContextMappingRowStatus")

                self.ccontextmappingstoragetype = YLeaf(YType.enumeration, "cContextMappingStorageType")

                self.ccontextmappingtopologyname = YLeaf(YType.str, "cContextMappingTopologyName")

                self.ccontextmappingvrfname = YLeaf(YType.str, "cContextMappingVrfName")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ccontextmappingvacmcontextname",
                                "ccontextmappingprotoinstname",
                                "ccontextmappingrowstatus",
                                "ccontextmappingstoragetype",
                                "ccontextmappingtopologyname",
                                "ccontextmappingvrfname") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoContextMappingMib.Ccontextmappingtable.Ccontextmappingentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoContextMappingMib.Ccontextmappingtable.Ccontextmappingentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ccontextmappingvacmcontextname.is_set or
                    self.ccontextmappingprotoinstname.is_set or
                    self.ccontextmappingrowstatus.is_set or
                    self.ccontextmappingstoragetype.is_set or
                    self.ccontextmappingtopologyname.is_set or
                    self.ccontextmappingvrfname.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ccontextmappingvacmcontextname.yfilter != YFilter.not_set or
                    self.ccontextmappingprotoinstname.yfilter != YFilter.not_set or
                    self.ccontextmappingrowstatus.yfilter != YFilter.not_set or
                    self.ccontextmappingstoragetype.yfilter != YFilter.not_set or
                    self.ccontextmappingtopologyname.yfilter != YFilter.not_set or
                    self.ccontextmappingvrfname.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cContextMappingEntry" + "[cContextMappingVacmContextName='" + self.ccontextmappingvacmcontextname.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-CONTEXT-MAPPING-MIB:CISCO-CONTEXT-MAPPING-MIB/cContextMappingTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ccontextmappingvacmcontextname.is_set or self.ccontextmappingvacmcontextname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccontextmappingvacmcontextname.get_name_leafdata())
                if (self.ccontextmappingprotoinstname.is_set or self.ccontextmappingprotoinstname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccontextmappingprotoinstname.get_name_leafdata())
                if (self.ccontextmappingrowstatus.is_set or self.ccontextmappingrowstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccontextmappingrowstatus.get_name_leafdata())
                if (self.ccontextmappingstoragetype.is_set or self.ccontextmappingstoragetype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccontextmappingstoragetype.get_name_leafdata())
                if (self.ccontextmappingtopologyname.is_set or self.ccontextmappingtopologyname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccontextmappingtopologyname.get_name_leafdata())
                if (self.ccontextmappingvrfname.is_set or self.ccontextmappingvrfname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccontextmappingvrfname.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cContextMappingVacmContextName" or name == "cContextMappingProtoInstName" or name == "cContextMappingRowStatus" or name == "cContextMappingStorageType" or name == "cContextMappingTopologyName" or name == "cContextMappingVrfName"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cContextMappingVacmContextName"):
                    self.ccontextmappingvacmcontextname = value
                    self.ccontextmappingvacmcontextname.value_namespace = name_space
                    self.ccontextmappingvacmcontextname.value_namespace_prefix = name_space_prefix
                if(value_path == "cContextMappingProtoInstName"):
                    self.ccontextmappingprotoinstname = value
                    self.ccontextmappingprotoinstname.value_namespace = name_space
                    self.ccontextmappingprotoinstname.value_namespace_prefix = name_space_prefix
                if(value_path == "cContextMappingRowStatus"):
                    self.ccontextmappingrowstatus = value
                    self.ccontextmappingrowstatus.value_namespace = name_space
                    self.ccontextmappingrowstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "cContextMappingStorageType"):
                    self.ccontextmappingstoragetype = value
                    self.ccontextmappingstoragetype.value_namespace = name_space
                    self.ccontextmappingstoragetype.value_namespace_prefix = name_space_prefix
                if(value_path == "cContextMappingTopologyName"):
                    self.ccontextmappingtopologyname = value
                    self.ccontextmappingtopologyname.value_namespace = name_space
                    self.ccontextmappingtopologyname.value_namespace_prefix = name_space_prefix
                if(value_path == "cContextMappingVrfName"):
                    self.ccontextmappingvrfname = value
                    self.ccontextmappingvrfname.value_namespace = name_space
                    self.ccontextmappingvrfname.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ccontextmappingentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ccontextmappingentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cContextMappingTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-CONTEXT-MAPPING-MIB:CISCO-CONTEXT-MAPPING-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cContextMappingEntry"):
                for c in self.ccontextmappingentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoContextMappingMib.Ccontextmappingtable.Ccontextmappingentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ccontextmappingentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cContextMappingEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
        	**type**\: list of    :py:class:`Ccontextmappingbridgedomainentry <ydk.models.cisco_ios_xe.CISCO_CONTEXT_MAPPING_MIB.CiscoContextMappingMib.Ccontextmappingbridgedomaintable.Ccontextmappingbridgedomainentry>`
        
        

        """

        _prefix = 'CISCO-CONTEXT-MAPPING-MIB'
        _revision = '2008-11-22'

        def __init__(self):
            super(CiscoContextMappingMib.Ccontextmappingbridgedomaintable, self).__init__()

            self.yang_name = "cContextMappingBridgeDomainTable"
            self.yang_parent_name = "CISCO-CONTEXT-MAPPING-MIB"

            self.ccontextmappingbridgedomainentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoContextMappingMib.Ccontextmappingbridgedomaintable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoContextMappingMib.Ccontextmappingbridgedomaintable, self).__setattr__(name, value)


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
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: ccontextmappingbridgedomainstoragetype
            
            	The storage type for this conceptual row.  Conceptual rows having the value 'permanent' need not allow write\-access to any columnar objects in the row
            	**type**\:   :py:class:`Storagetype <ydk.models.cisco_ios_xe.SNMPv2_TC.Storagetype>`
            
            

            """

            _prefix = 'CISCO-CONTEXT-MAPPING-MIB'
            _revision = '2008-11-22'

            def __init__(self):
                super(CiscoContextMappingMib.Ccontextmappingbridgedomaintable.Ccontextmappingbridgedomainentry, self).__init__()

                self.yang_name = "cContextMappingBridgeDomainEntry"
                self.yang_parent_name = "cContextMappingBridgeDomainTable"

                self.ccontextmappingvacmcontextname = YLeaf(YType.str, "cContextMappingVacmContextName")

                self.ccontextmappingbridgedomainidentifier = YLeaf(YType.uint32, "cContextMappingBridgeDomainIdentifier")

                self.ccontextmappingbridgedomainrowstatus = YLeaf(YType.enumeration, "cContextMappingBridgeDomainRowStatus")

                self.ccontextmappingbridgedomainstoragetype = YLeaf(YType.enumeration, "cContextMappingBridgeDomainStorageType")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ccontextmappingvacmcontextname",
                                "ccontextmappingbridgedomainidentifier",
                                "ccontextmappingbridgedomainrowstatus",
                                "ccontextmappingbridgedomainstoragetype") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoContextMappingMib.Ccontextmappingbridgedomaintable.Ccontextmappingbridgedomainentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoContextMappingMib.Ccontextmappingbridgedomaintable.Ccontextmappingbridgedomainentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ccontextmappingvacmcontextname.is_set or
                    self.ccontextmappingbridgedomainidentifier.is_set or
                    self.ccontextmappingbridgedomainrowstatus.is_set or
                    self.ccontextmappingbridgedomainstoragetype.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ccontextmappingvacmcontextname.yfilter != YFilter.not_set or
                    self.ccontextmappingbridgedomainidentifier.yfilter != YFilter.not_set or
                    self.ccontextmappingbridgedomainrowstatus.yfilter != YFilter.not_set or
                    self.ccontextmappingbridgedomainstoragetype.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cContextMappingBridgeDomainEntry" + "[cContextMappingVacmContextName='" + self.ccontextmappingvacmcontextname.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-CONTEXT-MAPPING-MIB:CISCO-CONTEXT-MAPPING-MIB/cContextMappingBridgeDomainTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ccontextmappingvacmcontextname.is_set or self.ccontextmappingvacmcontextname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccontextmappingvacmcontextname.get_name_leafdata())
                if (self.ccontextmappingbridgedomainidentifier.is_set or self.ccontextmappingbridgedomainidentifier.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccontextmappingbridgedomainidentifier.get_name_leafdata())
                if (self.ccontextmappingbridgedomainrowstatus.is_set or self.ccontextmappingbridgedomainrowstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccontextmappingbridgedomainrowstatus.get_name_leafdata())
                if (self.ccontextmappingbridgedomainstoragetype.is_set or self.ccontextmappingbridgedomainstoragetype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccontextmappingbridgedomainstoragetype.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cContextMappingVacmContextName" or name == "cContextMappingBridgeDomainIdentifier" or name == "cContextMappingBridgeDomainRowStatus" or name == "cContextMappingBridgeDomainStorageType"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cContextMappingVacmContextName"):
                    self.ccontextmappingvacmcontextname = value
                    self.ccontextmappingvacmcontextname.value_namespace = name_space
                    self.ccontextmappingvacmcontextname.value_namespace_prefix = name_space_prefix
                if(value_path == "cContextMappingBridgeDomainIdentifier"):
                    self.ccontextmappingbridgedomainidentifier = value
                    self.ccontextmappingbridgedomainidentifier.value_namespace = name_space
                    self.ccontextmappingbridgedomainidentifier.value_namespace_prefix = name_space_prefix
                if(value_path == "cContextMappingBridgeDomainRowStatus"):
                    self.ccontextmappingbridgedomainrowstatus = value
                    self.ccontextmappingbridgedomainrowstatus.value_namespace = name_space
                    self.ccontextmappingbridgedomainrowstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "cContextMappingBridgeDomainStorageType"):
                    self.ccontextmappingbridgedomainstoragetype = value
                    self.ccontextmappingbridgedomainstoragetype.value_namespace = name_space
                    self.ccontextmappingbridgedomainstoragetype.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ccontextmappingbridgedomainentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ccontextmappingbridgedomainentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cContextMappingBridgeDomainTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-CONTEXT-MAPPING-MIB:CISCO-CONTEXT-MAPPING-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cContextMappingBridgeDomainEntry"):
                for c in self.ccontextmappingbridgedomainentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoContextMappingMib.Ccontextmappingbridgedomaintable.Ccontextmappingbridgedomainentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ccontextmappingbridgedomainentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cContextMappingBridgeDomainEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
        	**type**\: list of    :py:class:`Ccontextmappingbridgeinstanceentry <ydk.models.cisco_ios_xe.CISCO_CONTEXT_MAPPING_MIB.CiscoContextMappingMib.Ccontextmappingbridgeinstancetable.Ccontextmappingbridgeinstanceentry>`
        
        

        """

        _prefix = 'CISCO-CONTEXT-MAPPING-MIB'
        _revision = '2008-11-22'

        def __init__(self):
            super(CiscoContextMappingMib.Ccontextmappingbridgeinstancetable, self).__init__()

            self.yang_name = "cContextMappingBridgeInstanceTable"
            self.yang_parent_name = "CISCO-CONTEXT-MAPPING-MIB"

            self.ccontextmappingbridgeinstanceentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoContextMappingMib.Ccontextmappingbridgeinstancetable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoContextMappingMib.Ccontextmappingbridgeinstancetable, self).__setattr__(name, value)


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
            
            .. attribute:: ccontextmappingvacmcontextname  <key>
            
            	
            	**type**\:  str
            
            	**length:** 0..32
            
            	**refers to**\:  :py:class:`ccontextmappingvacmcontextname <ydk.models.cisco_ios_xe.CISCO_CONTEXT_MAPPING_MIB.CiscoContextMappingMib.Ccontextmappingtable.Ccontextmappingentry>`
            
            .. attribute:: ccontextmappingbridgeinstname
            
            	The object identifies the name given to bridge instance to which the SNMP context is mapped to.  Value of this object cannot be changed when the  RowStatus object in the same row is 'active'.  This is typically a human\-readable string. This is the same ASCII string used in the router's console interface to refer to this bridge instance.  When the value of this object is a zero length string, it indicates that the SNMP context is independent of any bridge instances
            	**type**\:  str
            
            .. attribute:: ccontextmappingbridgeinstrowstatus
            
            	This object facilitates the creation, modification, or deletion of a conceptual row in this table
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: ccontextmappingbridgeinststoragetype
            
            	The storage type for this conceptual row.  Value of this object cannot be changed when the  RowStatus object in the same row is 'active'.  Conceptual rows having the value 'permanent' need not allow write\-access to any columnar objects in the row
            	**type**\:   :py:class:`Storagetype <ydk.models.cisco_ios_xe.SNMPv2_TC.Storagetype>`
            
            

            """

            _prefix = 'CISCO-CONTEXT-MAPPING-MIB'
            _revision = '2008-11-22'

            def __init__(self):
                super(CiscoContextMappingMib.Ccontextmappingbridgeinstancetable.Ccontextmappingbridgeinstanceentry, self).__init__()

                self.yang_name = "cContextMappingBridgeInstanceEntry"
                self.yang_parent_name = "cContextMappingBridgeInstanceTable"

                self.ccontextmappingvacmcontextname = YLeaf(YType.str, "cContextMappingVacmContextName")

                self.ccontextmappingbridgeinstname = YLeaf(YType.str, "cContextMappingBridgeInstName")

                self.ccontextmappingbridgeinstrowstatus = YLeaf(YType.enumeration, "cContextMappingBridgeInstRowStatus")

                self.ccontextmappingbridgeinststoragetype = YLeaf(YType.enumeration, "cContextMappingBridgeInstStorageType")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ccontextmappingvacmcontextname",
                                "ccontextmappingbridgeinstname",
                                "ccontextmappingbridgeinstrowstatus",
                                "ccontextmappingbridgeinststoragetype") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoContextMappingMib.Ccontextmappingbridgeinstancetable.Ccontextmappingbridgeinstanceentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoContextMappingMib.Ccontextmappingbridgeinstancetable.Ccontextmappingbridgeinstanceentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ccontextmappingvacmcontextname.is_set or
                    self.ccontextmappingbridgeinstname.is_set or
                    self.ccontextmappingbridgeinstrowstatus.is_set or
                    self.ccontextmappingbridgeinststoragetype.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ccontextmappingvacmcontextname.yfilter != YFilter.not_set or
                    self.ccontextmappingbridgeinstname.yfilter != YFilter.not_set or
                    self.ccontextmappingbridgeinstrowstatus.yfilter != YFilter.not_set or
                    self.ccontextmappingbridgeinststoragetype.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cContextMappingBridgeInstanceEntry" + "[cContextMappingVacmContextName='" + self.ccontextmappingvacmcontextname.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-CONTEXT-MAPPING-MIB:CISCO-CONTEXT-MAPPING-MIB/cContextMappingBridgeInstanceTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ccontextmappingvacmcontextname.is_set or self.ccontextmappingvacmcontextname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccontextmappingvacmcontextname.get_name_leafdata())
                if (self.ccontextmappingbridgeinstname.is_set or self.ccontextmappingbridgeinstname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccontextmappingbridgeinstname.get_name_leafdata())
                if (self.ccontextmappingbridgeinstrowstatus.is_set or self.ccontextmappingbridgeinstrowstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccontextmappingbridgeinstrowstatus.get_name_leafdata())
                if (self.ccontextmappingbridgeinststoragetype.is_set or self.ccontextmappingbridgeinststoragetype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccontextmappingbridgeinststoragetype.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cContextMappingVacmContextName" or name == "cContextMappingBridgeInstName" or name == "cContextMappingBridgeInstRowStatus" or name == "cContextMappingBridgeInstStorageType"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cContextMappingVacmContextName"):
                    self.ccontextmappingvacmcontextname = value
                    self.ccontextmappingvacmcontextname.value_namespace = name_space
                    self.ccontextmappingvacmcontextname.value_namespace_prefix = name_space_prefix
                if(value_path == "cContextMappingBridgeInstName"):
                    self.ccontextmappingbridgeinstname = value
                    self.ccontextmappingbridgeinstname.value_namespace = name_space
                    self.ccontextmappingbridgeinstname.value_namespace_prefix = name_space_prefix
                if(value_path == "cContextMappingBridgeInstRowStatus"):
                    self.ccontextmappingbridgeinstrowstatus = value
                    self.ccontextmappingbridgeinstrowstatus.value_namespace = name_space
                    self.ccontextmappingbridgeinstrowstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "cContextMappingBridgeInstStorageType"):
                    self.ccontextmappingbridgeinststoragetype = value
                    self.ccontextmappingbridgeinststoragetype.value_namespace = name_space
                    self.ccontextmappingbridgeinststoragetype.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ccontextmappingbridgeinstanceentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ccontextmappingbridgeinstanceentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cContextMappingBridgeInstanceTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-CONTEXT-MAPPING-MIB:CISCO-CONTEXT-MAPPING-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cContextMappingBridgeInstanceEntry"):
                for c in self.ccontextmappingbridgeinstanceentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoContextMappingMib.Ccontextmappingbridgeinstancetable.Ccontextmappingbridgeinstanceentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ccontextmappingbridgeinstanceentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cContextMappingBridgeInstanceEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Ccontextmappinglicensegrouptable(Entity):
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
            super(CiscoContextMappingMib.Ccontextmappinglicensegrouptable, self).__init__()

            self.yang_name = "cContextMappingLicenseGroupTable"
            self.yang_parent_name = "CISCO-CONTEXT-MAPPING-MIB"

            self.ccontextmappinglicensegroupentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoContextMappingMib.Ccontextmappinglicensegrouptable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoContextMappingMib.Ccontextmappinglicensegrouptable, self).__setattr__(name, value)


        class Ccontextmappinglicensegroupentry(Entity):
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
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: ccontextmappinglicensegroupstoragetype
            
            	The storage type for this conceptual row.  Conceptual rows having the value 'permanent' need not allow write\-access to any columnar objects in the row
            	**type**\:   :py:class:`Storagetype <ydk.models.cisco_ios_xe.SNMPv2_TC.Storagetype>`
            
            

            """

            _prefix = 'CISCO-CONTEXT-MAPPING-MIB'
            _revision = '2008-11-22'

            def __init__(self):
                super(CiscoContextMappingMib.Ccontextmappinglicensegrouptable.Ccontextmappinglicensegroupentry, self).__init__()

                self.yang_name = "cContextMappingLicenseGroupEntry"
                self.yang_parent_name = "cContextMappingLicenseGroupTable"

                self.ccontextmappingvacmcontextname = YLeaf(YType.str, "cContextMappingVacmContextName")

                self.ccontextmappinglicensegroupname = YLeaf(YType.str, "cContextMappingLicenseGroupName")

                self.ccontextmappinglicensegrouprowstatus = YLeaf(YType.enumeration, "cContextMappingLicenseGroupRowStatus")

                self.ccontextmappinglicensegroupstoragetype = YLeaf(YType.enumeration, "cContextMappingLicenseGroupStorageType")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ccontextmappingvacmcontextname",
                                "ccontextmappinglicensegroupname",
                                "ccontextmappinglicensegrouprowstatus",
                                "ccontextmappinglicensegroupstoragetype") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoContextMappingMib.Ccontextmappinglicensegrouptable.Ccontextmappinglicensegroupentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoContextMappingMib.Ccontextmappinglicensegrouptable.Ccontextmappinglicensegroupentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ccontextmappingvacmcontextname.is_set or
                    self.ccontextmappinglicensegroupname.is_set or
                    self.ccontextmappinglicensegrouprowstatus.is_set or
                    self.ccontextmappinglicensegroupstoragetype.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ccontextmappingvacmcontextname.yfilter != YFilter.not_set or
                    self.ccontextmappinglicensegroupname.yfilter != YFilter.not_set or
                    self.ccontextmappinglicensegrouprowstatus.yfilter != YFilter.not_set or
                    self.ccontextmappinglicensegroupstoragetype.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cContextMappingLicenseGroupEntry" + "[cContextMappingVacmContextName='" + self.ccontextmappingvacmcontextname.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-CONTEXT-MAPPING-MIB:CISCO-CONTEXT-MAPPING-MIB/cContextMappingLicenseGroupTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ccontextmappingvacmcontextname.is_set or self.ccontextmappingvacmcontextname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccontextmappingvacmcontextname.get_name_leafdata())
                if (self.ccontextmappinglicensegroupname.is_set or self.ccontextmappinglicensegroupname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccontextmappinglicensegroupname.get_name_leafdata())
                if (self.ccontextmappinglicensegrouprowstatus.is_set or self.ccontextmappinglicensegrouprowstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccontextmappinglicensegrouprowstatus.get_name_leafdata())
                if (self.ccontextmappinglicensegroupstoragetype.is_set or self.ccontextmappinglicensegroupstoragetype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccontextmappinglicensegroupstoragetype.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cContextMappingVacmContextName" or name == "cContextMappingLicenseGroupName" or name == "cContextMappingLicenseGroupRowStatus" or name == "cContextMappingLicenseGroupStorageType"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cContextMappingVacmContextName"):
                    self.ccontextmappingvacmcontextname = value
                    self.ccontextmappingvacmcontextname.value_namespace = name_space
                    self.ccontextmappingvacmcontextname.value_namespace_prefix = name_space_prefix
                if(value_path == "cContextMappingLicenseGroupName"):
                    self.ccontextmappinglicensegroupname = value
                    self.ccontextmappinglicensegroupname.value_namespace = name_space
                    self.ccontextmappinglicensegroupname.value_namespace_prefix = name_space_prefix
                if(value_path == "cContextMappingLicenseGroupRowStatus"):
                    self.ccontextmappinglicensegrouprowstatus = value
                    self.ccontextmappinglicensegrouprowstatus.value_namespace = name_space
                    self.ccontextmappinglicensegrouprowstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "cContextMappingLicenseGroupStorageType"):
                    self.ccontextmappinglicensegroupstoragetype = value
                    self.ccontextmappinglicensegroupstoragetype.value_namespace = name_space
                    self.ccontextmappinglicensegroupstoragetype.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ccontextmappinglicensegroupentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ccontextmappinglicensegroupentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cContextMappingLicenseGroupTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-CONTEXT-MAPPING-MIB:CISCO-CONTEXT-MAPPING-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cContextMappingLicenseGroupEntry"):
                for c in self.ccontextmappinglicensegroupentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoContextMappingMib.Ccontextmappinglicensegrouptable.Ccontextmappinglicensegroupentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ccontextmappinglicensegroupentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cContextMappingLicenseGroupEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.ccontextmappingbridgedomaintable is not None and self.ccontextmappingbridgedomaintable.has_data()) or
            (self.ccontextmappingbridgeinstancetable is not None and self.ccontextmappingbridgeinstancetable.has_data()) or
            (self.ccontextmappinglicensegrouptable is not None and self.ccontextmappinglicensegrouptable.has_data()) or
            (self.ccontextmappingtable is not None and self.ccontextmappingtable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.ccontextmappingbridgedomaintable is not None and self.ccontextmappingbridgedomaintable.has_operation()) or
            (self.ccontextmappingbridgeinstancetable is not None and self.ccontextmappingbridgeinstancetable.has_operation()) or
            (self.ccontextmappinglicensegrouptable is not None and self.ccontextmappinglicensegrouptable.has_operation()) or
            (self.ccontextmappingtable is not None and self.ccontextmappingtable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "CISCO-CONTEXT-MAPPING-MIB:CISCO-CONTEXT-MAPPING-MIB" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "cContextMappingBridgeDomainTable"):
            if (self.ccontextmappingbridgedomaintable is None):
                self.ccontextmappingbridgedomaintable = CiscoContextMappingMib.Ccontextmappingbridgedomaintable()
                self.ccontextmappingbridgedomaintable.parent = self
                self._children_name_map["ccontextmappingbridgedomaintable"] = "cContextMappingBridgeDomainTable"
            return self.ccontextmappingbridgedomaintable

        if (child_yang_name == "cContextMappingBridgeInstanceTable"):
            if (self.ccontextmappingbridgeinstancetable is None):
                self.ccontextmappingbridgeinstancetable = CiscoContextMappingMib.Ccontextmappingbridgeinstancetable()
                self.ccontextmappingbridgeinstancetable.parent = self
                self._children_name_map["ccontextmappingbridgeinstancetable"] = "cContextMappingBridgeInstanceTable"
            return self.ccontextmappingbridgeinstancetable

        if (child_yang_name == "cContextMappingLicenseGroupTable"):
            if (self.ccontextmappinglicensegrouptable is None):
                self.ccontextmappinglicensegrouptable = CiscoContextMappingMib.Ccontextmappinglicensegrouptable()
                self.ccontextmappinglicensegrouptable.parent = self
                self._children_name_map["ccontextmappinglicensegrouptable"] = "cContextMappingLicenseGroupTable"
            return self.ccontextmappinglicensegrouptable

        if (child_yang_name == "cContextMappingTable"):
            if (self.ccontextmappingtable is None):
                self.ccontextmappingtable = CiscoContextMappingMib.Ccontextmappingtable()
                self.ccontextmappingtable.parent = self
                self._children_name_map["ccontextmappingtable"] = "cContextMappingTable"
            return self.ccontextmappingtable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "cContextMappingBridgeDomainTable" or name == "cContextMappingBridgeInstanceTable" or name == "cContextMappingLicenseGroupTable" or name == "cContextMappingTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CiscoContextMappingMib()
        return self._top_entity

