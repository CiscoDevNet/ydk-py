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

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError




class CISCOVLANIFTABLERELATIONSHIPMIB(object):
    """
    
    
    .. attribute:: cvivlaninterfaceindextable
    
    	The cviVlanInterfaceIndexTable provides a way to translate a VLAN\-id in to an ifIndex, so that  the routed VLAN interface's routing configuration  can be obtained from interface entry in ipRouteTable.  Note that some routers can have interfaces to multiple VLAN management domains, and therefore can have multiple  routed VLAN interfaces which connect to different VLANs  having the same VLAN\-id.  Thus, it is possible to have  multiple rows in this table for the same VLAN\-id.  The cviVlanInterfaceIndexTable also provides a way to find the VLAN\-id from an ifTable VLAN's ifIndex
    	**type**\: :py:class:`CviVlanInterfaceIndexTable <ydk.models.vlan.CISCO_VLAN_IFTABLE_RELATIONSHIP_MIB.CISCOVLANIFTABLERELATIONSHIPMIB.CviVlanInterfaceIndexTable>`
    
    

    """

    _prefix = 'cisco-vlan'
    _revision = '2013-07-15'

    def __init__(self):
        self.cvivlaninterfaceindextable = CISCOVLANIFTABLERELATIONSHIPMIB.CviVlanInterfaceIndexTable()
        self.cvivlaninterfaceindextable.parent = self


    class CviVlanInterfaceIndexTable(object):
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
        	**type**\: list of :py:class:`CviVlanInterfaceIndexEntry <ydk.models.vlan.CISCO_VLAN_IFTABLE_RELATIONSHIP_MIB.CISCOVLANIFTABLERELATIONSHIPMIB.CviVlanInterfaceIndexTable.CviVlanInterfaceIndexEntry>`
        
        

        """

        _prefix = 'cisco-vlan'
        _revision = '2013-07-15'

        def __init__(self):
            self.parent = None
            self.cvivlaninterfaceindexentry = YList()
            self.cvivlaninterfaceindexentry.parent = self
            self.cvivlaninterfaceindexentry.name = 'cvivlaninterfaceindexentry'


        class CviVlanInterfaceIndexEntry(object):
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
            
            .. attribute:: cviphysicalifindex
            
            	For subinterfaces, this object is the ifIndex of the physical interface for the subinterface.  For Switch Virtual Interfaces (SVIs), this object is zero
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: cvivlanid
            
            	The VLAN\-id number of the routed VLAN interface
            	**type**\: int
            
            	**range:** 0..4095
            
            .. attribute:: cviroutedvlanifindex
            
            	The index for the ifTable entry associated with this routed VLAN interface
            	**type**\: int
            
            	**range:** 1..2147483647
            
            

            """

            _prefix = 'cisco-vlan'
            _revision = '2013-07-15'

            def __init__(self):
                self.parent = None
                self.cviphysicalifindex = None
                self.cvivlanid = None
                self.cviroutedvlanifindex = None

            @property
            def _common_path(self):
                if self.cviphysicalifindex is None:
                    raise YPYDataValidationError('Key property cviphysicalifindex is None')
                if self.cvivlanid is None:
                    raise YPYDataValidationError('Key property cvivlanid is None')

                return '/CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB:CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB/CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB:cviVlanInterfaceIndexTable/CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB:cviVlanInterfaceIndexEntry[CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB:cviPhysicalIfIndex = ' + str(self.cviphysicalifindex) + '][CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB:cviVlanId = ' + str(self.cvivlanid) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cviphysicalifindex is not None:
                    return True

                if self.cvivlanid is not None:
                    return True

                if self.cviroutedvlanifindex is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.vlan._meta import _CISCO_VLAN_IFTABLE_RELATIONSHIP_MIB as meta
                return meta._meta_table['CISCOVLANIFTABLERELATIONSHIPMIB.CviVlanInterfaceIndexTable.CviVlanInterfaceIndexEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB:CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB/CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB:cviVlanInterfaceIndexTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cvivlaninterfaceindexentry is not None:
                for child_ref in self.cvivlaninterfaceindexentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.vlan._meta import _CISCO_VLAN_IFTABLE_RELATIONSHIP_MIB as meta
            return meta._meta_table['CISCOVLANIFTABLERELATIONSHIPMIB.CviVlanInterfaceIndexTable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB:CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.cvivlaninterfaceindextable is not None and self.cvivlaninterfaceindextable._has_data():
            return True

        if self.cvivlaninterfaceindextable is not None and self.cvivlaninterfaceindextable.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.vlan._meta import _CISCO_VLAN_IFTABLE_RELATIONSHIP_MIB as meta
        return meta._meta_table['CISCOVLANIFTABLERELATIONSHIPMIB']['meta_info']


