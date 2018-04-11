""" CISCO_VLAN_IFTABLE_RELATIONSHIP_MIB 

Cisco VLAN ifTable Relationship MIB lists VLAN\-id and ifIndex
information for routed VLAN interfaces.  

A routed VLAN interface is the router interface or sub\-interface 
to which the router's IP address on the VLAN is attached.  
For example, an ISL, SDE, or 802.1Q encapsulated
subinterface, or Switched Virtual Interface (SVI).

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CISCOVLANIFTABLERELATIONSHIPMIB(Entity):
    """
    
    
    .. attribute:: cvivlaninterfaceindextable
    
    	The cviVlanInterfaceIndexTable provides a way to translate a VLAN\-id in to an ifIndex, so that  the routed VLAN interface's routing configuration  can be obtained from interface entry in ipRouteTable.  Note that some routers can have interfaces to multiple VLAN management domains, and therefore can have multiple  routed VLAN interfaces which connect to different VLANs  having the same VLAN\-id.  Thus, it is possible to have  multiple rows in this table for the same VLAN\-id.  The cviVlanInterfaceIndexTable also provides a way to find the VLAN\-id from an ifTable VLAN's ifIndex
    	**type**\:  :py:class:`Cvivlaninterfaceindextable <ydk.models.cisco_ios_xe.CISCO_VLAN_IFTABLE_RELATIONSHIP_MIB.CISCOVLANIFTABLERELATIONSHIPMIB.Cvivlaninterfaceindextable>`
    
    

    """

    _prefix = 'CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB'
    _revision = '2013-07-15'

    def __init__(self):
        super(CISCOVLANIFTABLERELATIONSHIPMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB"
        self.yang_parent_name = "CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("cviVlanInterfaceIndexTable", ("cvivlaninterfaceindextable", CISCOVLANIFTABLERELATIONSHIPMIB.Cvivlaninterfaceindextable))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.cvivlaninterfaceindextable = CISCOVLANIFTABLERELATIONSHIPMIB.Cvivlaninterfaceindextable()
        self.cvivlaninterfaceindextable.parent = self
        self._children_name_map["cvivlaninterfaceindextable"] = "cviVlanInterfaceIndexTable"
        self._children_yang_names.add("cviVlanInterfaceIndexTable")
        self._segment_path = lambda: "CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB:CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB"


    class Cvivlaninterfaceindextable(Entity):
        """
        The cviVlanInterfaceIndexTable provides a way to
        translate a VLAN\-id in to an ifIndex, so that 
        the routed VLAN interface's routing configuration 
        can be obtained from interface entry in ipRouteTable.
        
        Note that some routers can have interfaces to multiple
        VLAN management domains, and therefore can have multiple 
        routed VLAN interfaces which connect to different VLANs 
        having the same VLAN\-id.  Thus, it is possible to have 
        multiple rows in this table for the same VLAN\-id.
        
        The cviVlanInterfaceIndexTable also provides a way
        to find the VLAN\-id from an ifTable VLAN's ifIndex.
        
        .. attribute:: cvivlaninterfaceindexentry
        
        	Each entry represents a routed VLAN interface, its corresponding physical port if any, and the ifTable entry for the routed VLAN interface.  Entries are created by the agent when the routed VLAN interface is created.  Operational status of routing does not affect the entries listed here.  For routing configuration please refer to ipRouteTable.  Entries are deleted by the agent when the routed VLAN interface is removed from the system configuration
        	**type**\: list of  		 :py:class:`Cvivlaninterfaceindexentry <ydk.models.cisco_ios_xe.CISCO_VLAN_IFTABLE_RELATIONSHIP_MIB.CISCOVLANIFTABLERELATIONSHIPMIB.Cvivlaninterfaceindextable.Cvivlaninterfaceindexentry>`
        
        

        """

        _prefix = 'CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB'
        _revision = '2013-07-15'

        def __init__(self):
            super(CISCOVLANIFTABLERELATIONSHIPMIB.Cvivlaninterfaceindextable, self).__init__()

            self.yang_name = "cviVlanInterfaceIndexTable"
            self.yang_parent_name = "CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cviVlanInterfaceIndexEntry", ("cvivlaninterfaceindexentry", CISCOVLANIFTABLERELATIONSHIPMIB.Cvivlaninterfaceindextable.Cvivlaninterfaceindexentry))])
            self._leafs = OrderedDict()

            self.cvivlaninterfaceindexentry = YList(self)
            self._segment_path = lambda: "cviVlanInterfaceIndexTable"
            self._absolute_path = lambda: "CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB:CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOVLANIFTABLERELATIONSHIPMIB.Cvivlaninterfaceindextable, [], name, value)


        class Cvivlaninterfaceindexentry(Entity):
            """
            Each entry represents a routed VLAN interface, its
            corresponding physical port if any, and the ifTable entry
            for the routed VLAN interface.
            
            Entries are created by the agent when the routed VLAN interface
            is created.  Operational status of routing does not affect
            the entries listed here.  For routing configuration please refer
            to ipRouteTable.
            
            Entries are deleted by the agent when the routed VLAN interface
            is removed from the system configuration.
            
            .. attribute:: cvivlanid  (key)
            
            	The VLAN\-id number of the routed VLAN interface
            	**type**\: int
            
            	**range:** 0..4095
            
            .. attribute:: cviphysicalifindex  (key)
            
            	For subinterfaces, this object is the ifIndex of the physical interface for the subinterface.  For Switch Virtual Interfaces (SVIs), this object is zero
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: cviroutedvlanifindex
            
            	The index for the ifTable entry associated with this routed VLAN interface
            	**type**\: int
            
            	**range:** 1..2147483647
            
            

            """

            _prefix = 'CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB'
            _revision = '2013-07-15'

            def __init__(self):
                super(CISCOVLANIFTABLERELATIONSHIPMIB.Cvivlaninterfaceindextable.Cvivlaninterfaceindexentry, self).__init__()

                self.yang_name = "cviVlanInterfaceIndexEntry"
                self.yang_parent_name = "cviVlanInterfaceIndexTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cvivlanid','cviphysicalifindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cvivlanid', YLeaf(YType.int32, 'cviVlanId')),
                    ('cviphysicalifindex', YLeaf(YType.int32, 'cviPhysicalIfIndex')),
                    ('cviroutedvlanifindex', YLeaf(YType.int32, 'cviRoutedVlanIfIndex')),
                ])
                self.cvivlanid = None
                self.cviphysicalifindex = None
                self.cviroutedvlanifindex = None
                self._segment_path = lambda: "cviVlanInterfaceIndexEntry" + "[cviVlanId='" + str(self.cvivlanid) + "']" + "[cviPhysicalIfIndex='" + str(self.cviphysicalifindex) + "']"
                self._absolute_path = lambda: "CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB:CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB/cviVlanInterfaceIndexTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOVLANIFTABLERELATIONSHIPMIB.Cvivlaninterfaceindextable.Cvivlaninterfaceindexentry, ['cvivlanid', 'cviphysicalifindex', 'cviroutedvlanifindex'], name, value)

    def clone_ptr(self):
        self._top_entity = CISCOVLANIFTABLERELATIONSHIPMIB()
        return self._top_entity

