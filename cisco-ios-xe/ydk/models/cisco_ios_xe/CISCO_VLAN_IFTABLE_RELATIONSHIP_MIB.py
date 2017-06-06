""" CISCO_VLAN_IFTABLE_RELATIONSHIP_MIB 

Cisco VLAN ifTable Relationship MIB lists VLAN\-id and ifIndex
information for routed VLAN interfaces.  

A routed VLAN interface is the router interface or sub\-interface 
to which the router's IP address on the VLAN is attached.  
For example, an ISL, SDE, or 802.1Q encapsulated
subinterface, or Switched Virtual Interface (SVI).

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class CiscoVlanIftableRelationshipMib(object):
    """
    
    
    .. attribute:: cvivlaninterfaceindextable
    
    	The cviVlanInterfaceIndexTable provides a way to translate a VLAN\-id in to an ifIndex, so that  the routed VLAN interface's routing configuration  can be obtained from interface entry in ipRouteTable.  Note that some routers can have interfaces to multiple VLAN management domains, and therefore can have multiple  routed VLAN interfaces which connect to different VLANs  having the same VLAN\-id.  Thus, it is possible to have  multiple rows in this table for the same VLAN\-id.  The cviVlanInterfaceIndexTable also provides a way to find the VLAN\-id from an ifTable VLAN's ifIndex
    	**type**\:   :py:class:`Cvivlaninterfaceindextable <ydk.models.cisco_ios_xe.CISCO_VLAN_IFTABLE_RELATIONSHIP_MIB.CiscoVlanIftableRelationshipMib.Cvivlaninterfaceindextable>`
    
    

    """

    _prefix = 'CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB'
    _revision = '2013-07-15'

    def __init__(self):
        self.cvivlaninterfaceindextable = CiscoVlanIftableRelationshipMib.Cvivlaninterfaceindextable()
        self.cvivlaninterfaceindextable.parent = self


    class Cvivlaninterfaceindextable(object):
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
        	**type**\: list of    :py:class:`Cvivlaninterfaceindexentry <ydk.models.cisco_ios_xe.CISCO_VLAN_IFTABLE_RELATIONSHIP_MIB.CiscoVlanIftableRelationshipMib.Cvivlaninterfaceindextable.Cvivlaninterfaceindexentry>`
        
        

        """

        _prefix = 'CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB'
        _revision = '2013-07-15'

        def __init__(self):
            self.parent = None
            self.cvivlaninterfaceindexentry = YList()
            self.cvivlaninterfaceindexentry.parent = self
            self.cvivlaninterfaceindexentry.name = 'cvivlaninterfaceindexentry'


        class Cvivlaninterfaceindexentry(object):
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
            
            .. attribute:: cvivlanid  <key>
            
            	The VLAN\-id number of the routed VLAN interface
            	**type**\:  int
            
            	**range:** 0..4095
            
            .. attribute:: cviphysicalifindex  <key>
            
            	For subinterfaces, this object is the ifIndex of the physical interface for the subinterface.  For Switch Virtual Interfaces (SVIs), this object is zero
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: cviroutedvlanifindex
            
            	The index for the ifTable entry associated with this routed VLAN interface
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            

            """

            _prefix = 'CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB'
            _revision = '2013-07-15'

            def __init__(self):
                self.parent = None
                self.cvivlanid = None
                self.cviphysicalifindex = None
                self.cviroutedvlanifindex = None

            @property
            def _common_path(self):
                if self.cvivlanid is None:
                    raise YPYModelError('Key property cvivlanid is None')
                if self.cviphysicalifindex is None:
                    raise YPYModelError('Key property cviphysicalifindex is None')

                return '/CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB:CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB/CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB:cviVlanInterfaceIndexTable/CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB:cviVlanInterfaceIndexEntry[CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB:cviVlanId = ' + str(self.cvivlanid) + '][CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB:cviPhysicalIfIndex = ' + str(self.cviphysicalifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.cvivlanid is not None:
                    return True

                if self.cviphysicalifindex is not None:
                    return True

                if self.cviroutedvlanifindex is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_VLAN_IFTABLE_RELATIONSHIP_MIB as meta
                return meta._meta_table['CiscoVlanIftableRelationshipMib.Cvivlaninterfaceindextable.Cvivlaninterfaceindexentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB:CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB/CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB:cviVlanInterfaceIndexTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cvivlaninterfaceindexentry is not None:
                for child_ref in self.cvivlaninterfaceindexentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_VLAN_IFTABLE_RELATIONSHIP_MIB as meta
            return meta._meta_table['CiscoVlanIftableRelationshipMib.Cvivlaninterfaceindextable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB:CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.cvivlaninterfaceindextable is not None and self.cvivlaninterfaceindextable._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_VLAN_IFTABLE_RELATIONSHIP_MIB as meta
        return meta._meta_table['CiscoVlanIftableRelationshipMib']['meta_info']


