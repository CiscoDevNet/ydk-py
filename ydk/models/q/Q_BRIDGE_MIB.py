""" Q_BRIDGE_MIB 

The VLAN Bridge MIB module for managing Virtual Bridged
Local Area Networks, as defined by IEEE 802.1Q\-2003,
including Restricted Vlan Registration defined by
IEEE 802.1u\-2001 and Vlan Classification defined by
IEEE 802.1v\-2001.

Copyright (C) The Internet Society (2006).  This version of
this MIB module is part of RFC 4363; See the RFC itself for
full legal notices.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError


from ydk.models.p.P_BRIDGE_MIB import EnabledStatus_Enum
from ydk.models.snmpv2.SNMPv2_TC import RowStatus_Enum


class QBRIDGEMIB(object):
    """
    
    
    .. attribute:: dot1qbase
    
    	
    	**type**\: :py:class:`Dot1qBase <ydk.models.q.Q_BRIDGE_MIB.QBRIDGEMIB.Dot1qBase>`
    
    .. attribute:: dot1qfdbtable
    
    	A table that contains configuration and control information for each Filtering Database currently operating on this device.  Entries in this table appear automatically when VLANs are assigned FDB IDs in the dot1qVlanCurrentTable
    	**type**\: :py:class:`Dot1qFdbTable <ydk.models.q.Q_BRIDGE_MIB.QBRIDGEMIB.Dot1qFdbTable>`
    
    .. attribute:: dot1qforwardalltable
    
    	A table containing forwarding information for each  VLAN, specifying the set of ports to which forwarding of all multicasts applies, configured statically by management or dynamically by GMRP.  An entry appears in this table for all VLANs that are currently instantiated
    	**type**\: :py:class:`Dot1qForwardAllTable <ydk.models.q.Q_BRIDGE_MIB.QBRIDGEMIB.Dot1qForwardAllTable>`
    
    .. attribute:: dot1qforwardunregisteredtable
    
    	A table containing forwarding information for each VLAN, specifying the set of ports to which forwarding of multicast group\-addressed frames for which no more specific forwarding information applies.  This is configured statically by management and determined dynamically by GMRP.  An entry appears in this table for all VLANs that are currently instantiated
    	**type**\: :py:class:`Dot1qForwardUnregisteredTable <ydk.models.q.Q_BRIDGE_MIB.QBRIDGEMIB.Dot1qForwardUnregisteredTable>`
    
    .. attribute:: dot1qlearningconstraintstable
    
    	A table containing learning constraints for sets of Shared and Independent VLANs
    	**type**\: :py:class:`Dot1qLearningConstraintsTable <ydk.models.q.Q_BRIDGE_MIB.QBRIDGEMIB.Dot1qLearningConstraintsTable>`
    
    .. attribute:: dot1qportvlanhcstatisticstable
    
    	A table containing per\-port, per\-VLAN statistics for traffic on high\-capacity interfaces
    	**type**\: :py:class:`Dot1qPortVlanHCStatisticsTable <ydk.models.q.Q_BRIDGE_MIB.QBRIDGEMIB.Dot1qPortVlanHCStatisticsTable>`
    
    .. attribute:: dot1qportvlanstatisticstable
    
    	A table containing per\-port, per\-VLAN statistics for traffic received.  Separate objects are provided for both the most\-significant and least\-significant bits of statistics counters for ports that are associated with this transparent bridge.  The most\-significant bit objects are only required on high\-capacity interfaces, as defined in the conformance clauses for these objects.  This mechanism is provided as a way to read 64\-bit counters for agents that support only SNMPv1.  Note that the reporting of most\-significant and least\- significant counter bits separately runs the risk of missing an overflow of the lower bits in the interval between sampling. The manager must be aware of this possibility, even within the same varbindlist, when interpreting the results of a request or  asynchronous notification
    	**type**\: :py:class:`Dot1qPortVlanStatisticsTable <ydk.models.q.Q_BRIDGE_MIB.QBRIDGEMIB.Dot1qPortVlanStatisticsTable>`
    
    .. attribute:: dot1qstaticmulticasttable
    
    	A table containing filtering information for Multicast and Broadcast MAC addresses for each VLAN, configured into the device by (local or network) management specifying the set of ports to which frames received from specific ports and containing specific Multicast and Broadcast destination addresses are allowed to be forwarded.  A value of zero in this table (as the port number from which frames with a specific destination address are received) is used to specify all ports for which there is no specific entry in this table for that particular destination address.  Entries are valid for Multicast and Broadcast addresses only
    	**type**\: :py:class:`Dot1qStaticMulticastTable <ydk.models.q.Q_BRIDGE_MIB.QBRIDGEMIB.Dot1qStaticMulticastTable>`
    
    .. attribute:: dot1qstaticunicasttable
    
    	A table containing filtering information for Unicast MAC addresses for each Filtering Database, configured into the device by (local or network) management specifying the set of ports to which frames received from specific ports and containing specific unicast destination addresses are allowed to be forwarded.  A value of zero in this table (as the port number from  which frames with a specific destination address are received) is used to specify all ports for which there is no specific entry in this table for that particular destination address.  Entries are valid for unicast addresses only
    	**type**\: :py:class:`Dot1qStaticUnicastTable <ydk.models.q.Q_BRIDGE_MIB.QBRIDGEMIB.Dot1qStaticUnicastTable>`
    
    .. attribute:: dot1qtpfdbtable
    
    	A table that contains information about unicast entries for which the device has forwarding and/or filtering information.  This information is used by the transparent bridging function in determining how to propagate a received frame
    	**type**\: :py:class:`Dot1qTpFdbTable <ydk.models.q.Q_BRIDGE_MIB.QBRIDGEMIB.Dot1qTpFdbTable>`
    
    .. attribute:: dot1qtpgrouptable
    
    	A table containing filtering information for VLANs configured into the bridge by (local or network) management, or learned dynamically, specifying the set of ports to which frames received on a VLAN for this FDB and containing a specific Group destination address are allowed to be forwarded
    	**type**\: :py:class:`Dot1qTpGroupTable <ydk.models.q.Q_BRIDGE_MIB.QBRIDGEMIB.Dot1qTpGroupTable>`
    
    .. attribute:: dot1qvlan
    
    	
    	**type**\: :py:class:`Dot1qVlan <ydk.models.q.Q_BRIDGE_MIB.QBRIDGEMIB.Dot1qVlan>`
    
    .. attribute:: dot1qvlancurrenttable
    
    	A table containing current configuration information for each VLAN currently configured into the device by (local or network) management, or dynamically created as a result of GVRP requests received
    	**type**\: :py:class:`Dot1qVlanCurrentTable <ydk.models.q.Q_BRIDGE_MIB.QBRIDGEMIB.Dot1qVlanCurrentTable>`
    
    .. attribute:: dot1qvlanstatictable
    
    	A table containing static configuration information for each VLAN configured into the device by (local or network) management.  All entries are permanent and will be restored after the device is reset
    	**type**\: :py:class:`Dot1qVlanStaticTable <ydk.models.q.Q_BRIDGE_MIB.QBRIDGEMIB.Dot1qVlanStaticTable>`
    
    .. attribute:: dot1vprotocolgrouptable
    
    	A table that contains mappings from Protocol Templates to Protocol Group Identifiers used for Port\-and\-Protocol\-based VLAN Classification
    	**type**\: :py:class:`Dot1vProtocolGroupTable <ydk.models.q.Q_BRIDGE_MIB.QBRIDGEMIB.Dot1vProtocolGroupTable>`
    
    .. attribute:: dot1vprotocolporttable
    
    	A table that contains VID sets used for Port\-and\-Protocol\-based VLAN Classification
    	**type**\: :py:class:`Dot1vProtocolPortTable <ydk.models.q.Q_BRIDGE_MIB.QBRIDGEMIB.Dot1vProtocolPortTable>`
    
    

    """

    _prefix = 'q-bridge'
    _revision = '2006-01-09'

    def __init__(self):
        self.dot1qbase = QBRIDGEMIB.Dot1qBase()
        self.dot1qbase.parent = self
        self.dot1qfdbtable = QBRIDGEMIB.Dot1qFdbTable()
        self.dot1qfdbtable.parent = self
        self.dot1qforwardalltable = QBRIDGEMIB.Dot1qForwardAllTable()
        self.dot1qforwardalltable.parent = self
        self.dot1qforwardunregisteredtable = QBRIDGEMIB.Dot1qForwardUnregisteredTable()
        self.dot1qforwardunregisteredtable.parent = self
        self.dot1qlearningconstraintstable = QBRIDGEMIB.Dot1qLearningConstraintsTable()
        self.dot1qlearningconstraintstable.parent = self
        self.dot1qportvlanhcstatisticstable = QBRIDGEMIB.Dot1qPortVlanHCStatisticsTable()
        self.dot1qportvlanhcstatisticstable.parent = self
        self.dot1qportvlanstatisticstable = QBRIDGEMIB.Dot1qPortVlanStatisticsTable()
        self.dot1qportvlanstatisticstable.parent = self
        self.dot1qstaticmulticasttable = QBRIDGEMIB.Dot1qStaticMulticastTable()
        self.dot1qstaticmulticasttable.parent = self
        self.dot1qstaticunicasttable = QBRIDGEMIB.Dot1qStaticUnicastTable()
        self.dot1qstaticunicasttable.parent = self
        self.dot1qtpfdbtable = QBRIDGEMIB.Dot1qTpFdbTable()
        self.dot1qtpfdbtable.parent = self
        self.dot1qtpgrouptable = QBRIDGEMIB.Dot1qTpGroupTable()
        self.dot1qtpgrouptable.parent = self
        self.dot1qvlan = QBRIDGEMIB.Dot1qVlan()
        self.dot1qvlan.parent = self
        self.dot1qvlancurrenttable = QBRIDGEMIB.Dot1qVlanCurrentTable()
        self.dot1qvlancurrenttable.parent = self
        self.dot1qvlanstatictable = QBRIDGEMIB.Dot1qVlanStaticTable()
        self.dot1qvlanstatictable.parent = self
        self.dot1vprotocolgrouptable = QBRIDGEMIB.Dot1vProtocolGroupTable()
        self.dot1vprotocolgrouptable.parent = self
        self.dot1vprotocolporttable = QBRIDGEMIB.Dot1vProtocolPortTable()
        self.dot1vprotocolporttable.parent = self


    class Dot1qBase(object):
        """
        
        
        .. attribute:: dot1qgvrpstatus
        
        	The administrative status requested by management for GVRP.  The value enabled(1) indicates that GVRP should be enabled on this device, on all ports for which it has not been specifically disabled.  When disabled(2), GVRP is disabled on all ports, and all GVRP packets will be forwarded transparently.  This object affects all GVRP Applicant and Registrar state machines.  A transition from disabled(2) to enabled(1) will cause a reset of all GVRP state machines on all ports.  The value of this object MUST be retained across reinitializations of the management system
        	**type**\: :py:class:`EnabledStatus_Enum <ydk.models.p.P_BRIDGE_MIB.EnabledStatus_Enum>`
        
        .. attribute:: dot1qmaxsupportedvlans
        
        	The maximum number of IEEE 802.1Q VLANs that this device supports
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: dot1qmaxvlanid
        
        	The maximum IEEE 802.1Q VLAN\-ID that this device  supports
        	**type**\: int
        
        	**range:** 1..4094
        
        .. attribute:: dot1qnumvlans
        
        	The current number of IEEE 802.1Q VLANs that are configured in this device
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: dot1qvlanversionnumber
        
        	The version number of IEEE 802.1Q that this device supports
        	**type**\: :py:class:`Dot1qVlanVersionNumber_Enum <ydk.models.q.Q_BRIDGE_MIB.QBRIDGEMIB.Dot1qBase.Dot1qVlanVersionNumber_Enum>`
        
        

        """

        _prefix = 'q-bridge'
        _revision = '2006-01-09'

        def __init__(self):
            self.parent = None
            self.dot1qgvrpstatus = None
            self.dot1qmaxsupportedvlans = None
            self.dot1qmaxvlanid = None
            self.dot1qnumvlans = None
            self.dot1qvlanversionnumber = None

        class Dot1qVlanVersionNumber_Enum(Enum):
            """
            Dot1qVlanVersionNumber_Enum

            The version number of IEEE 802.1Q that this device
            supports.

            """

            VERSION1 = 1


            @staticmethod
            def _meta_info():
                from ydk.models.q._meta import _Q_BRIDGE_MIB as meta
                return meta._meta_table['QBRIDGEMIB.Dot1qBase.Dot1qVlanVersionNumber_Enum']


        @property
        def _common_path(self):

            return '/Q-BRIDGE-MIB:Q-BRIDGE-MIB/Q-BRIDGE-MIB:dot1qBase'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.dot1qgvrpstatus is not None:
                return True

            if self.dot1qmaxsupportedvlans is not None:
                return True

            if self.dot1qmaxvlanid is not None:
                return True

            if self.dot1qnumvlans is not None:
                return True

            if self.dot1qvlanversionnumber is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.q._meta import _Q_BRIDGE_MIB as meta
            return meta._meta_table['QBRIDGEMIB.Dot1qBase']['meta_info']


    class Dot1qFdbTable(object):
        """
        A table that contains configuration and control
        information for each Filtering Database currently
        operating on this device.  Entries in this table appear
        automatically when VLANs are assigned FDB IDs in the
        dot1qVlanCurrentTable.
        
        .. attribute:: dot1qfdbentry
        
        	Information about a specific Filtering Database
        	**type**\: list of :py:class:`Dot1qFdbEntry <ydk.models.q.Q_BRIDGE_MIB.QBRIDGEMIB.Dot1qFdbTable.Dot1qFdbEntry>`
        
        

        """

        _prefix = 'q-bridge'
        _revision = '2006-01-09'

        def __init__(self):
            self.parent = None
            self.dot1qfdbentry = YList()
            self.dot1qfdbentry.parent = self
            self.dot1qfdbentry.name = 'dot1qfdbentry'


        class Dot1qFdbEntry(object):
            """
            Information about a specific Filtering Database.
            
            .. attribute:: dot1qfdbid
            
            	The identity of this Filtering Database
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot1qfdbdynamiccount
            
            	The current number of dynamic entries in this Filtering Database
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'q-bridge'
            _revision = '2006-01-09'

            def __init__(self):
                self.parent = None
                self.dot1qfdbid = None
                self.dot1qfdbdynamiccount = None

            @property
            def _common_path(self):
                if self.dot1qfdbid is None:
                    raise YPYDataValidationError('Key property dot1qfdbid is None')

                return '/Q-BRIDGE-MIB:Q-BRIDGE-MIB/Q-BRIDGE-MIB:dot1qFdbTable/Q-BRIDGE-MIB:dot1qFdbEntry[Q-BRIDGE-MIB:dot1qFdbId = ' + str(self.dot1qfdbid) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.dot1qfdbid is not None:
                    return True

                if self.dot1qfdbdynamiccount is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.q._meta import _Q_BRIDGE_MIB as meta
                return meta._meta_table['QBRIDGEMIB.Dot1qFdbTable.Dot1qFdbEntry']['meta_info']

        @property
        def _common_path(self):

            return '/Q-BRIDGE-MIB:Q-BRIDGE-MIB/Q-BRIDGE-MIB:dot1qFdbTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.dot1qfdbentry is not None:
                for child_ref in self.dot1qfdbentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.q._meta import _Q_BRIDGE_MIB as meta
            return meta._meta_table['QBRIDGEMIB.Dot1qFdbTable']['meta_info']


    class Dot1qForwardAllTable(object):
        """
        A table containing forwarding information for each
        
        VLAN, specifying the set of ports to which forwarding of
        all multicasts applies, configured statically by
        management or dynamically by GMRP.  An entry appears in
        this table for all VLANs that are currently
        instantiated.
        
        .. attribute:: dot1qforwardallentry
        
        	Forwarding information for a VLAN, specifying the set of ports to which all multicasts should be forwarded, configured statically by management or dynamically by GMRP
        	**type**\: list of :py:class:`Dot1qForwardAllEntry <ydk.models.q.Q_BRIDGE_MIB.QBRIDGEMIB.Dot1qForwardAllTable.Dot1qForwardAllEntry>`
        
        

        """

        _prefix = 'q-bridge'
        _revision = '2006-01-09'

        def __init__(self):
            self.parent = None
            self.dot1qforwardallentry = YList()
            self.dot1qforwardallentry.parent = self
            self.dot1qforwardallentry.name = 'dot1qforwardallentry'


        class Dot1qForwardAllEntry(object):
            """
            Forwarding information for a VLAN, specifying the set
            of ports to which all multicasts should be forwarded,
            configured statically by management or dynamically by
            GMRP.
            
            .. attribute:: dot1qvlanindex
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot1qforwardallforbiddenports
            
            	The set of ports configured by management in this VLAN for which the Service Requirement attribute Forward All Multicast Groups may not be dynamically registered by GMRP.  This value will be restored after the device is reset.  A port may not be added in this set if it is already a member of the set of ports in dot1qForwardAllStaticPorts.  The default value is a string of zeros of appropriate length.  The value of this object MUST be retained across reinitializations of the management system
            	**type**\: str
            
            .. attribute:: dot1qforwardallports
            
            	The complete set of ports in this VLAN to which all multicast group\-addressed frames are to be forwarded. This includes ports for which this need has been determined dynamically by GMRP, or configured statically by management
            	**type**\: str
            
            .. attribute:: dot1qforwardallstaticports
            
            	The set of ports configured by management in this VLAN to which all multicast group\-addressed frames are to be forwarded.  Ports entered in this list will also appear in the complete set shown by dot1qForwardAllPorts.  This value will be restored after the device is reset.  This only applies to ports that are members of the VLAN, defined by dot1qVlanCurrentEgressPorts.  A port may not be added in this set if it is already a member of the set of ports in dot1qForwardAllForbiddenPorts.  The default value is a string of ones of appropriate length, to indicate the standard behaviour of using basic filtering services, i.e., forward all multicasts to all ports.  The value of this object MUST be retained across reinitializations of the management system
            	**type**\: str
            
            

            """

            _prefix = 'q-bridge'
            _revision = '2006-01-09'

            def __init__(self):
                self.parent = None
                self.dot1qvlanindex = None
                self.dot1qforwardallforbiddenports = None
                self.dot1qforwardallports = None
                self.dot1qforwardallstaticports = None

            @property
            def _common_path(self):
                if self.dot1qvlanindex is None:
                    raise YPYDataValidationError('Key property dot1qvlanindex is None')

                return '/Q-BRIDGE-MIB:Q-BRIDGE-MIB/Q-BRIDGE-MIB:dot1qForwardAllTable/Q-BRIDGE-MIB:dot1qForwardAllEntry[Q-BRIDGE-MIB:dot1qVlanIndex = ' + str(self.dot1qvlanindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.dot1qvlanindex is not None:
                    return True

                if self.dot1qforwardallforbiddenports is not None:
                    return True

                if self.dot1qforwardallports is not None:
                    return True

                if self.dot1qforwardallstaticports is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.q._meta import _Q_BRIDGE_MIB as meta
                return meta._meta_table['QBRIDGEMIB.Dot1qForwardAllTable.Dot1qForwardAllEntry']['meta_info']

        @property
        def _common_path(self):

            return '/Q-BRIDGE-MIB:Q-BRIDGE-MIB/Q-BRIDGE-MIB:dot1qForwardAllTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.dot1qforwardallentry is not None:
                for child_ref in self.dot1qforwardallentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.q._meta import _Q_BRIDGE_MIB as meta
            return meta._meta_table['QBRIDGEMIB.Dot1qForwardAllTable']['meta_info']


    class Dot1qForwardUnregisteredTable(object):
        """
        A table containing forwarding information for each
        VLAN, specifying the set of ports to which forwarding of
        multicast group\-addressed frames for which no
        more specific forwarding information applies.  This is
        configured statically by management and determined
        dynamically by GMRP.  An entry appears in this table for
        all VLANs that are currently instantiated.
        
        .. attribute:: dot1qforwardunregisteredentry
        
        	Forwarding information for a VLAN, specifying the set of ports to which all multicasts for which there is no more specific forwarding information shall be forwarded. This is configured statically by management or dynamically by GMRP
        	**type**\: list of :py:class:`Dot1qForwardUnregisteredEntry <ydk.models.q.Q_BRIDGE_MIB.QBRIDGEMIB.Dot1qForwardUnregisteredTable.Dot1qForwardUnregisteredEntry>`
        
        

        """

        _prefix = 'q-bridge'
        _revision = '2006-01-09'

        def __init__(self):
            self.parent = None
            self.dot1qforwardunregisteredentry = YList()
            self.dot1qforwardunregisteredentry.parent = self
            self.dot1qforwardunregisteredentry.name = 'dot1qforwardunregisteredentry'


        class Dot1qForwardUnregisteredEntry(object):
            """
            Forwarding information for a VLAN, specifying the set
            of ports to which all multicasts for which there is no
            more specific forwarding information shall be forwarded.
            This is configured statically by management or
            dynamically by GMRP.
            
            .. attribute:: dot1qvlanindex
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot1qforwardunregisteredforbiddenports
            
            	The set of ports configured by management in this VLAN for which the Service Requirement attribute Forward Unregistered Multicast Groups may not be dynamically registered by GMRP.  This value will be restored after the device is reset.  A port may not be added in this set if it is already a member of the set of ports in dot1qForwardUnregisteredStaticPorts.  The default value is a string of zeros of appropriate length.  The value of this object MUST be retained across reinitializations of the management system
            	**type**\: str
            
            .. attribute:: dot1qforwardunregisteredports
            
            	The complete set of ports in this VLAN to which multicast group\-addressed frames for which there is no more specific forwarding information will be forwarded. This includes ports for which this need has been determined dynamically by GMRP, or configured statically by management
            	**type**\: str
            
            .. attribute:: dot1qforwardunregisteredstaticports
            
            	The set of ports configured by management, in this VLAN, to which multicast group\-addressed frames for which there is no more specific forwarding information  are to be forwarded.  Ports entered in this list will also appear in the complete set shown by dot1qForwardUnregisteredPorts.  This value will be restored after the device is reset.  A port may not be added in this set if it is already a member of the set of ports in dot1qForwardUnregisteredForbiddenPorts.  The default value is a string of zeros of appropriate length, although this has no effect with the default value of dot1qForwardAllStaticPorts.  The value of this object MUST be retained across reinitializations of the management system
            	**type**\: str
            
            

            """

            _prefix = 'q-bridge'
            _revision = '2006-01-09'

            def __init__(self):
                self.parent = None
                self.dot1qvlanindex = None
                self.dot1qforwardunregisteredforbiddenports = None
                self.dot1qforwardunregisteredports = None
                self.dot1qforwardunregisteredstaticports = None

            @property
            def _common_path(self):
                if self.dot1qvlanindex is None:
                    raise YPYDataValidationError('Key property dot1qvlanindex is None')

                return '/Q-BRIDGE-MIB:Q-BRIDGE-MIB/Q-BRIDGE-MIB:dot1qForwardUnregisteredTable/Q-BRIDGE-MIB:dot1qForwardUnregisteredEntry[Q-BRIDGE-MIB:dot1qVlanIndex = ' + str(self.dot1qvlanindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.dot1qvlanindex is not None:
                    return True

                if self.dot1qforwardunregisteredforbiddenports is not None:
                    return True

                if self.dot1qforwardunregisteredports is not None:
                    return True

                if self.dot1qforwardunregisteredstaticports is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.q._meta import _Q_BRIDGE_MIB as meta
                return meta._meta_table['QBRIDGEMIB.Dot1qForwardUnregisteredTable.Dot1qForwardUnregisteredEntry']['meta_info']

        @property
        def _common_path(self):

            return '/Q-BRIDGE-MIB:Q-BRIDGE-MIB/Q-BRIDGE-MIB:dot1qForwardUnregisteredTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.dot1qforwardunregisteredentry is not None:
                for child_ref in self.dot1qforwardunregisteredentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.q._meta import _Q_BRIDGE_MIB as meta
            return meta._meta_table['QBRIDGEMIB.Dot1qForwardUnregisteredTable']['meta_info']


    class Dot1qLearningConstraintsTable(object):
        """
        A table containing learning constraints for sets of
        Shared and Independent VLANs.
        
        .. attribute:: dot1qlearningconstraintsentry
        
        	A learning constraint defined for a VLAN
        	**type**\: list of :py:class:`Dot1qLearningConstraintsEntry <ydk.models.q.Q_BRIDGE_MIB.QBRIDGEMIB.Dot1qLearningConstraintsTable.Dot1qLearningConstraintsEntry>`
        
        

        """

        _prefix = 'q-bridge'
        _revision = '2006-01-09'

        def __init__(self):
            self.parent = None
            self.dot1qlearningconstraintsentry = YList()
            self.dot1qlearningconstraintsentry.parent = self
            self.dot1qlearningconstraintsentry.name = 'dot1qlearningconstraintsentry'


        class Dot1qLearningConstraintsEntry(object):
            """
            A learning constraint defined for a VLAN.
            
            .. attribute:: dot1qconstraintset
            
            	The identity of the constraint set to which dot1qConstraintVlan belongs.  These values may be chosen by the management station
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: dot1qconstraintvlan
            
            	The index of the row in dot1qVlanCurrentTable for the VLAN constrained by this entry
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot1qconstraintstatus
            
            	The status of this entry
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            .. attribute:: dot1qconstrainttype
            
            	The type of constraint this entry defines. independent(1) \- the VLAN, dot1qConstraintVlan,     uses a filtering database independent from all     other VLANs in the same set, defined by     dot1qConstraintSet. shared(2) \- the VLAN, dot1qConstraintVlan, shares     the same filtering database as all other VLANs     in the same set, defined by dot1qConstraintSet
            	**type**\: :py:class:`Dot1qConstraintType_Enum <ydk.models.q.Q_BRIDGE_MIB.QBRIDGEMIB.Dot1qLearningConstraintsTable.Dot1qLearningConstraintsEntry.Dot1qConstraintType_Enum>`
            
            

            """

            _prefix = 'q-bridge'
            _revision = '2006-01-09'

            def __init__(self):
                self.parent = None
                self.dot1qconstraintset = None
                self.dot1qconstraintvlan = None
                self.dot1qconstraintstatus = None
                self.dot1qconstrainttype = None

            class Dot1qConstraintType_Enum(Enum):
                """
                Dot1qConstraintType_Enum

                The type of constraint this entry defines.
                independent(1) \- the VLAN, dot1qConstraintVlan,
                    uses a filtering database independent from all
                    other VLANs in the same set, defined by
                    dot1qConstraintSet.
                shared(2) \- the VLAN, dot1qConstraintVlan, shares
                    the same filtering database as all other VLANs
                    in the same set, defined by dot1qConstraintSet.

                """

                INDEPENDENT = 1

                SHARED = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.q._meta import _Q_BRIDGE_MIB as meta
                    return meta._meta_table['QBRIDGEMIB.Dot1qLearningConstraintsTable.Dot1qLearningConstraintsEntry.Dot1qConstraintType_Enum']


            @property
            def _common_path(self):
                if self.dot1qconstraintset is None:
                    raise YPYDataValidationError('Key property dot1qconstraintset is None')
                if self.dot1qconstraintvlan is None:
                    raise YPYDataValidationError('Key property dot1qconstraintvlan is None')

                return '/Q-BRIDGE-MIB:Q-BRIDGE-MIB/Q-BRIDGE-MIB:dot1qLearningConstraintsTable/Q-BRIDGE-MIB:dot1qLearningConstraintsEntry[Q-BRIDGE-MIB:dot1qConstraintSet = ' + str(self.dot1qconstraintset) + '][Q-BRIDGE-MIB:dot1qConstraintVlan = ' + str(self.dot1qconstraintvlan) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.dot1qconstraintset is not None:
                    return True

                if self.dot1qconstraintvlan is not None:
                    return True

                if self.dot1qconstraintstatus is not None:
                    return True

                if self.dot1qconstrainttype is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.q._meta import _Q_BRIDGE_MIB as meta
                return meta._meta_table['QBRIDGEMIB.Dot1qLearningConstraintsTable.Dot1qLearningConstraintsEntry']['meta_info']

        @property
        def _common_path(self):

            return '/Q-BRIDGE-MIB:Q-BRIDGE-MIB/Q-BRIDGE-MIB:dot1qLearningConstraintsTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.dot1qlearningconstraintsentry is not None:
                for child_ref in self.dot1qlearningconstraintsentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.q._meta import _Q_BRIDGE_MIB as meta
            return meta._meta_table['QBRIDGEMIB.Dot1qLearningConstraintsTable']['meta_info']


    class Dot1qPortVlanHCStatisticsTable(object):
        """
        A table containing per\-port, per\-VLAN statistics for
        traffic on high\-capacity interfaces.
        
        .. attribute:: dot1qportvlanhcstatisticsentry
        
        	Traffic statistics for a VLAN on a high\-capacity interface
        	**type**\: list of :py:class:`Dot1qPortVlanHCStatisticsEntry <ydk.models.q.Q_BRIDGE_MIB.QBRIDGEMIB.Dot1qPortVlanHCStatisticsTable.Dot1qPortVlanHCStatisticsEntry>`
        
        

        """

        _prefix = 'q-bridge'
        _revision = '2006-01-09'

        def __init__(self):
            self.parent = None
            self.dot1qportvlanhcstatisticsentry = YList()
            self.dot1qportvlanhcstatisticsentry.parent = self
            self.dot1qportvlanhcstatisticsentry.name = 'dot1qportvlanhcstatisticsentry'


        class Dot1qPortVlanHCStatisticsEntry(object):
            """
            Traffic statistics for a VLAN on a high\-capacity
            interface.
            
            .. attribute:: dot1dbaseport
            
            	
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: dot1qvlanindex
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot1qtpvlanporthcindiscards
            
            	The number of valid frames received by this port from its segment that were classified as belonging to this VLAN and that were discarded due to VLAN\-related reasons. Specifically, the IEEE 802.1Q counters for Discard Inbound and Discard on Ingress Filtering
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: dot1qtpvlanporthcinframes
            
            	The number of valid frames received by this port from its segment that were classified as belonging to this VLAN.  Note that a frame received on this port is counted by this object if and only if it is for a  protocol being processed by the local forwarding process for this VLAN.  This object includes received bridge management frames classified as belonging to this VLAN (e.g., GMRP, but not GVRP or STP)
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: dot1qtpvlanporthcoutframes
            
            	The number of valid frames transmitted by this port to its segment from the local forwarding process for this VLAN.  This includes bridge management frames originated by this device that are classified as belonging to this VLAN (e.g., GMRP, but not GVRP or STP)
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            

            """

            _prefix = 'q-bridge'
            _revision = '2006-01-09'

            def __init__(self):
                self.parent = None
                self.dot1dbaseport = None
                self.dot1qvlanindex = None
                self.dot1qtpvlanporthcindiscards = None
                self.dot1qtpvlanporthcinframes = None
                self.dot1qtpvlanporthcoutframes = None

            @property
            def _common_path(self):
                if self.dot1dbaseport is None:
                    raise YPYDataValidationError('Key property dot1dbaseport is None')
                if self.dot1qvlanindex is None:
                    raise YPYDataValidationError('Key property dot1qvlanindex is None')

                return '/Q-BRIDGE-MIB:Q-BRIDGE-MIB/Q-BRIDGE-MIB:dot1qPortVlanHCStatisticsTable/Q-BRIDGE-MIB:dot1qPortVlanHCStatisticsEntry[Q-BRIDGE-MIB:dot1dBasePort = ' + str(self.dot1dbaseport) + '][Q-BRIDGE-MIB:dot1qVlanIndex = ' + str(self.dot1qvlanindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.dot1dbaseport is not None:
                    return True

                if self.dot1qvlanindex is not None:
                    return True

                if self.dot1qtpvlanporthcindiscards is not None:
                    return True

                if self.dot1qtpvlanporthcinframes is not None:
                    return True

                if self.dot1qtpvlanporthcoutframes is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.q._meta import _Q_BRIDGE_MIB as meta
                return meta._meta_table['QBRIDGEMIB.Dot1qPortVlanHCStatisticsTable.Dot1qPortVlanHCStatisticsEntry']['meta_info']

        @property
        def _common_path(self):

            return '/Q-BRIDGE-MIB:Q-BRIDGE-MIB/Q-BRIDGE-MIB:dot1qPortVlanHCStatisticsTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.dot1qportvlanhcstatisticsentry is not None:
                for child_ref in self.dot1qportvlanhcstatisticsentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.q._meta import _Q_BRIDGE_MIB as meta
            return meta._meta_table['QBRIDGEMIB.Dot1qPortVlanHCStatisticsTable']['meta_info']


    class Dot1qPortVlanStatisticsTable(object):
        """
        A table containing per\-port, per\-VLAN statistics for
        traffic received.  Separate objects are provided for both the
        most\-significant and least\-significant bits of statistics
        counters for ports that are associated with this transparent
        bridge.  The most\-significant bit objects are only required on
        high\-capacity interfaces, as defined in the conformance clauses
        for these objects.  This mechanism is provided as a way to read
        64\-bit counters for agents that support only SNMPv1.
        
        Note that the reporting of most\-significant and least\-
        significant counter bits separately runs the risk of missing
        an overflow of the lower bits in the interval between sampling.
        The manager must be aware of this possibility, even within the
        same varbindlist, when interpreting the results of a request or
        
        asynchronous notification.
        
        .. attribute:: dot1qportvlanstatisticsentry
        
        	Traffic statistics for a VLAN on an interface
        	**type**\: list of :py:class:`Dot1qPortVlanStatisticsEntry <ydk.models.q.Q_BRIDGE_MIB.QBRIDGEMIB.Dot1qPortVlanStatisticsTable.Dot1qPortVlanStatisticsEntry>`
        
        

        """

        _prefix = 'q-bridge'
        _revision = '2006-01-09'

        def __init__(self):
            self.parent = None
            self.dot1qportvlanstatisticsentry = YList()
            self.dot1qportvlanstatisticsentry.parent = self
            self.dot1qportvlanstatisticsentry.name = 'dot1qportvlanstatisticsentry'


        class Dot1qPortVlanStatisticsEntry(object):
            """
            Traffic statistics for a VLAN on an interface.
            
            .. attribute:: dot1dbaseport
            
            	
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: dot1qvlanindex
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot1qtpvlanportindiscards
            
            	The number of valid frames received by this port from its segment that were classified as belonging to this VLAN and that were discarded due to VLAN\-related reasons. Specifically, the IEEE 802.1Q counters for Discard Inbound and Discard on Ingress Filtering
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot1qtpvlanportinframes
            
            	The number of valid frames received by this port from its segment that were classified as belonging to this VLAN.  Note that a frame received on this port is counted by this object if and only if it is for a protocol being processed by the local forwarding process for this VLAN.  This object includes received bridge management frames classified as belonging to this VLAN (e.g., GMRP, but not GVRP or STP
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot1qtpvlanportinoverflowdiscards
            
            	The number of times the associated dot1qTpVlanPortInDiscards counter has overflowed
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot1qtpvlanportinoverflowframes
            
            	The number of times the associated dot1qTpVlanPortInFrames counter has overflowed
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot1qtpvlanportoutframes
            
            	The number of valid frames transmitted by this port to its segment from the local forwarding process for this VLAN.  This includes bridge management frames originated by this device that are classified as belonging to this VLAN (e.g., GMRP, but not GVRP or STP)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot1qtpvlanportoutoverflowframes
            
            	The number of times the associated dot1qTpVlanPortOutFrames counter has overflowed
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'q-bridge'
            _revision = '2006-01-09'

            def __init__(self):
                self.parent = None
                self.dot1dbaseport = None
                self.dot1qvlanindex = None
                self.dot1qtpvlanportindiscards = None
                self.dot1qtpvlanportinframes = None
                self.dot1qtpvlanportinoverflowdiscards = None
                self.dot1qtpvlanportinoverflowframes = None
                self.dot1qtpvlanportoutframes = None
                self.dot1qtpvlanportoutoverflowframes = None

            @property
            def _common_path(self):
                if self.dot1dbaseport is None:
                    raise YPYDataValidationError('Key property dot1dbaseport is None')
                if self.dot1qvlanindex is None:
                    raise YPYDataValidationError('Key property dot1qvlanindex is None')

                return '/Q-BRIDGE-MIB:Q-BRIDGE-MIB/Q-BRIDGE-MIB:dot1qPortVlanStatisticsTable/Q-BRIDGE-MIB:dot1qPortVlanStatisticsEntry[Q-BRIDGE-MIB:dot1dBasePort = ' + str(self.dot1dbaseport) + '][Q-BRIDGE-MIB:dot1qVlanIndex = ' + str(self.dot1qvlanindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.dot1dbaseport is not None:
                    return True

                if self.dot1qvlanindex is not None:
                    return True

                if self.dot1qtpvlanportindiscards is not None:
                    return True

                if self.dot1qtpvlanportinframes is not None:
                    return True

                if self.dot1qtpvlanportinoverflowdiscards is not None:
                    return True

                if self.dot1qtpvlanportinoverflowframes is not None:
                    return True

                if self.dot1qtpvlanportoutframes is not None:
                    return True

                if self.dot1qtpvlanportoutoverflowframes is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.q._meta import _Q_BRIDGE_MIB as meta
                return meta._meta_table['QBRIDGEMIB.Dot1qPortVlanStatisticsTable.Dot1qPortVlanStatisticsEntry']['meta_info']

        @property
        def _common_path(self):

            return '/Q-BRIDGE-MIB:Q-BRIDGE-MIB/Q-BRIDGE-MIB:dot1qPortVlanStatisticsTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.dot1qportvlanstatisticsentry is not None:
                for child_ref in self.dot1qportvlanstatisticsentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.q._meta import _Q_BRIDGE_MIB as meta
            return meta._meta_table['QBRIDGEMIB.Dot1qPortVlanStatisticsTable']['meta_info']


    class Dot1qStaticMulticastTable(object):
        """
        A table containing filtering information for Multicast
        and Broadcast MAC addresses for each VLAN, configured
        into the device by (local or network) management
        specifying the set of ports to which frames received
        from specific ports and containing specific Multicast
        and Broadcast destination addresses are allowed to be
        forwarded.  A value of zero in this table (as the port
        number from which frames with a specific destination
        address are received) is used to specify all ports for
        which there is no specific entry in this table for that
        particular destination address.  Entries are valid for
        Multicast and Broadcast addresses only.
        
        .. attribute:: dot1qstaticmulticastentry
        
        	Filtering information configured into the device by (local or network) management specifying the set of ports to which frames received from this specific port  for this VLAN and containing this Multicast or Broadcast destination address are allowed to be forwarded
        	**type**\: list of :py:class:`Dot1qStaticMulticastEntry <ydk.models.q.Q_BRIDGE_MIB.QBRIDGEMIB.Dot1qStaticMulticastTable.Dot1qStaticMulticastEntry>`
        
        

        """

        _prefix = 'q-bridge'
        _revision = '2006-01-09'

        def __init__(self):
            self.parent = None
            self.dot1qstaticmulticastentry = YList()
            self.dot1qstaticmulticastentry.parent = self
            self.dot1qstaticmulticastentry.name = 'dot1qstaticmulticastentry'


        class Dot1qStaticMulticastEntry(object):
            """
            Filtering information configured into the device by
            (local or network) management specifying the set of
            ports to which frames received from this specific port
            
            for this VLAN and containing this Multicast or Broadcast
            destination address are allowed to be forwarded.
            
            .. attribute:: dot1qstaticmulticastaddress
            
            	The destination MAC address in a frame to which this entry's filtering information applies.  This object must take the value of a Multicast or Broadcast address
            	**type**\: str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            .. attribute:: dot1qstaticmulticastreceiveport
            
            	Either the value '0' or the port number of the port from which a frame must be received in order for this entry's filtering information to apply.  A value of zero indicates that this entry applies on all ports of the device for which there is no other applicable entry
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: dot1qvlanindex
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot1qstaticmulticastforbiddenegressports
            
            	The set of ports to which frames received from a specific port and destined for a specific Multicast or Broadcast MAC address must not be forwarded, regardless of any dynamic information, e.g., from GMRP.  A port may not be added in this set if it is already a member of the set of ports in dot1qStaticMulticastStaticEgressPorts. The default value of this object is a string of zeros of appropriate length.  The value of this object MUST be retained across reinitializations of the management system
            	**type**\: str
            
            .. attribute:: dot1qstaticmulticaststaticegressports
            
            	The set of ports to which frames received from a specific port and destined for a specific Multicast or Broadcast MAC address must be forwarded, regardless of any dynamic information, e.g., from GMRP.  A port may not be added in this set if it is already a member of the set of ports in dot1qStaticMulticastForbiddenEgressPorts. The default value of this object is a string of ones of appropriate length.  The value of this object MUST be retained across reinitializations of the management system
            	**type**\: str
            
            .. attribute:: dot1qstaticmulticaststatus
            
            	This object indicates the status of this entry. other(1) \- this entry is currently in use, but     the conditions under which it will remain     so differ from the following values.  invalid(2) \- writing this value to the object     removes the corresponding entry. permanent(3) \- this entry is currently in use     and will remain so after the next reset of     the bridge. deleteOnReset(4) \- this entry is currently in     use and will remain so until the next     reset of the bridge. deleteOnTimeout(5) \- this entry is currently in     use and will remain so until it is aged out.  The value of this object MUST be retained across reinitializations of the management system
            	**type**\: :py:class:`Dot1qStaticMulticastStatus_Enum <ydk.models.q.Q_BRIDGE_MIB.QBRIDGEMIB.Dot1qStaticMulticastTable.Dot1qStaticMulticastEntry.Dot1qStaticMulticastStatus_Enum>`
            
            

            """

            _prefix = 'q-bridge'
            _revision = '2006-01-09'

            def __init__(self):
                self.parent = None
                self.dot1qstaticmulticastaddress = None
                self.dot1qstaticmulticastreceiveport = None
                self.dot1qvlanindex = None
                self.dot1qstaticmulticastforbiddenegressports = None
                self.dot1qstaticmulticaststaticegressports = None
                self.dot1qstaticmulticaststatus = None

            class Dot1qStaticMulticastStatus_Enum(Enum):
                """
                Dot1qStaticMulticastStatus_Enum

                This object indicates the status of this entry.
                other(1) \- this entry is currently in use, but
                    the conditions under which it will remain
                    so differ from the following values.
                
                invalid(2) \- writing this value to the object
                    removes the corresponding entry.
                permanent(3) \- this entry is currently in use
                    and will remain so after the next reset of
                    the bridge.
                deleteOnReset(4) \- this entry is currently in
                    use and will remain so until the next
                    reset of the bridge.
                deleteOnTimeout(5) \- this entry is currently in
                    use and will remain so until it is aged out.
                
                The value of this object MUST be retained across
                reinitializations of the management system.

                """

                OTHER = 1

                INVALID = 2

                PERMANENT = 3

                DELETEONRESET = 4

                DELETEONTIMEOUT = 5


                @staticmethod
                def _meta_info():
                    from ydk.models.q._meta import _Q_BRIDGE_MIB as meta
                    return meta._meta_table['QBRIDGEMIB.Dot1qStaticMulticastTable.Dot1qStaticMulticastEntry.Dot1qStaticMulticastStatus_Enum']


            @property
            def _common_path(self):
                if self.dot1qstaticmulticastaddress is None:
                    raise YPYDataValidationError('Key property dot1qstaticmulticastaddress is None')
                if self.dot1qstaticmulticastreceiveport is None:
                    raise YPYDataValidationError('Key property dot1qstaticmulticastreceiveport is None')
                if self.dot1qvlanindex is None:
                    raise YPYDataValidationError('Key property dot1qvlanindex is None')

                return '/Q-BRIDGE-MIB:Q-BRIDGE-MIB/Q-BRIDGE-MIB:dot1qStaticMulticastTable/Q-BRIDGE-MIB:dot1qStaticMulticastEntry[Q-BRIDGE-MIB:dot1qStaticMulticastAddress = ' + str(self.dot1qstaticmulticastaddress) + '][Q-BRIDGE-MIB:dot1qStaticMulticastReceivePort = ' + str(self.dot1qstaticmulticastreceiveport) + '][Q-BRIDGE-MIB:dot1qVlanIndex = ' + str(self.dot1qvlanindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.dot1qstaticmulticastaddress is not None:
                    return True

                if self.dot1qstaticmulticastreceiveport is not None:
                    return True

                if self.dot1qvlanindex is not None:
                    return True

                if self.dot1qstaticmulticastforbiddenegressports is not None:
                    return True

                if self.dot1qstaticmulticaststaticegressports is not None:
                    return True

                if self.dot1qstaticmulticaststatus is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.q._meta import _Q_BRIDGE_MIB as meta
                return meta._meta_table['QBRIDGEMIB.Dot1qStaticMulticastTable.Dot1qStaticMulticastEntry']['meta_info']

        @property
        def _common_path(self):

            return '/Q-BRIDGE-MIB:Q-BRIDGE-MIB/Q-BRIDGE-MIB:dot1qStaticMulticastTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.dot1qstaticmulticastentry is not None:
                for child_ref in self.dot1qstaticmulticastentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.q._meta import _Q_BRIDGE_MIB as meta
            return meta._meta_table['QBRIDGEMIB.Dot1qStaticMulticastTable']['meta_info']


    class Dot1qStaticUnicastTable(object):
        """
        A table containing filtering information for Unicast
        MAC addresses for each Filtering Database, configured
        into the device by (local or network) management
        specifying the set of ports to which frames received
        from specific ports and containing specific unicast
        destination addresses are allowed to be forwarded.  A
        value of zero in this table (as the port number from
        
        which frames with a specific destination address are
        received) is used to specify all ports for which there
        is no specific entry in this table for that particular
        destination address.  Entries are valid for unicast
        addresses only.
        
        .. attribute:: dot1qstaticunicastentry
        
        	Filtering information configured into the device by (local or network) management specifying the set of ports to which frames received from a specific port and containing a specific unicast destination address are allowed to be forwarded
        	**type**\: list of :py:class:`Dot1qStaticUnicastEntry <ydk.models.q.Q_BRIDGE_MIB.QBRIDGEMIB.Dot1qStaticUnicastTable.Dot1qStaticUnicastEntry>`
        
        

        """

        _prefix = 'q-bridge'
        _revision = '2006-01-09'

        def __init__(self):
            self.parent = None
            self.dot1qstaticunicastentry = YList()
            self.dot1qstaticunicastentry.parent = self
            self.dot1qstaticunicastentry.name = 'dot1qstaticunicastentry'


        class Dot1qStaticUnicastEntry(object):
            """
            Filtering information configured into the device by
            (local or network) management specifying the set of
            ports to which frames received from a specific port and
            containing a specific unicast destination address are
            allowed to be forwarded.
            
            .. attribute:: dot1qfdbid
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot1qstaticunicastaddress
            
            	The destination MAC address in a frame to which this entry's filtering information applies.  This object must take the value of a unicast address
            	**type**\: str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            .. attribute:: dot1qstaticunicastreceiveport
            
            	Either the value '0' or the port number of the port from which a frame must be received in order for this entry's filtering information to apply.  A value of zero indicates that this entry applies on all ports of the device for which there is no other applicable entry
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: dot1qstaticunicastallowedtogoto
            
            	The set of ports for which a frame with a specific unicast address will be flooded in the event that it has not been learned.  It also specifies the set of ports on which a specific unicast address may be dynamically learned.  The dot1qTpFdbTable will have an equivalent entry with a dot1qTpFdbPort value of '0' until this address has been learned, at which point it will be updated with the port the address has been seen on.  This only applies to ports that are members of the VLAN, defined by dot1qVlanCurrentEgressPorts.  The default value of this object is a string of ones of appropriate length.  The value of this object MUST be retained across reinitializations of the management system
            	**type**\: str
            
            .. attribute:: dot1qstaticunicaststatus
            
            	This object indicates the status of this entry. other(1) \- this entry is currently in use, but      the conditions under which it will remain     so differ from the following values. invalid(2) \- writing this value to the object     removes the corresponding entry. permanent(3) \- this entry is currently in use     and will remain so after the next reset of     the bridge. deleteOnReset(4) \- this entry is currently in     use and will remain so until the next     reset of the bridge. deleteOnTimeout(5) \- this entry is currently in     use and will remain so until it is aged out.  The value of this object MUST be retained across reinitializations of the management system
            	**type**\: :py:class:`Dot1qStaticUnicastStatus_Enum <ydk.models.q.Q_BRIDGE_MIB.QBRIDGEMIB.Dot1qStaticUnicastTable.Dot1qStaticUnicastEntry.Dot1qStaticUnicastStatus_Enum>`
            
            

            """

            _prefix = 'q-bridge'
            _revision = '2006-01-09'

            def __init__(self):
                self.parent = None
                self.dot1qfdbid = None
                self.dot1qstaticunicastaddress = None
                self.dot1qstaticunicastreceiveport = None
                self.dot1qstaticunicastallowedtogoto = None
                self.dot1qstaticunicaststatus = None

            class Dot1qStaticUnicastStatus_Enum(Enum):
                """
                Dot1qStaticUnicastStatus_Enum

                This object indicates the status of this entry.
                other(1) \- this entry is currently in use, but
                
                    the conditions under which it will remain
                    so differ from the following values.
                invalid(2) \- writing this value to the object
                    removes the corresponding entry.
                permanent(3) \- this entry is currently in use
                    and will remain so after the next reset of
                    the bridge.
                deleteOnReset(4) \- this entry is currently in
                    use and will remain so until the next
                    reset of the bridge.
                deleteOnTimeout(5) \- this entry is currently in
                    use and will remain so until it is aged out.
                
                The value of this object MUST be retained across
                reinitializations of the management system.

                """

                OTHER = 1

                INVALID = 2

                PERMANENT = 3

                DELETEONRESET = 4

                DELETEONTIMEOUT = 5


                @staticmethod
                def _meta_info():
                    from ydk.models.q._meta import _Q_BRIDGE_MIB as meta
                    return meta._meta_table['QBRIDGEMIB.Dot1qStaticUnicastTable.Dot1qStaticUnicastEntry.Dot1qStaticUnicastStatus_Enum']


            @property
            def _common_path(self):
                if self.dot1qfdbid is None:
                    raise YPYDataValidationError('Key property dot1qfdbid is None')
                if self.dot1qstaticunicastaddress is None:
                    raise YPYDataValidationError('Key property dot1qstaticunicastaddress is None')
                if self.dot1qstaticunicastreceiveport is None:
                    raise YPYDataValidationError('Key property dot1qstaticunicastreceiveport is None')

                return '/Q-BRIDGE-MIB:Q-BRIDGE-MIB/Q-BRIDGE-MIB:dot1qStaticUnicastTable/Q-BRIDGE-MIB:dot1qStaticUnicastEntry[Q-BRIDGE-MIB:dot1qFdbId = ' + str(self.dot1qfdbid) + '][Q-BRIDGE-MIB:dot1qStaticUnicastAddress = ' + str(self.dot1qstaticunicastaddress) + '][Q-BRIDGE-MIB:dot1qStaticUnicastReceivePort = ' + str(self.dot1qstaticunicastreceiveport) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.dot1qfdbid is not None:
                    return True

                if self.dot1qstaticunicastaddress is not None:
                    return True

                if self.dot1qstaticunicastreceiveport is not None:
                    return True

                if self.dot1qstaticunicastallowedtogoto is not None:
                    return True

                if self.dot1qstaticunicaststatus is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.q._meta import _Q_BRIDGE_MIB as meta
                return meta._meta_table['QBRIDGEMIB.Dot1qStaticUnicastTable.Dot1qStaticUnicastEntry']['meta_info']

        @property
        def _common_path(self):

            return '/Q-BRIDGE-MIB:Q-BRIDGE-MIB/Q-BRIDGE-MIB:dot1qStaticUnicastTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.dot1qstaticunicastentry is not None:
                for child_ref in self.dot1qstaticunicastentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.q._meta import _Q_BRIDGE_MIB as meta
            return meta._meta_table['QBRIDGEMIB.Dot1qStaticUnicastTable']['meta_info']


    class Dot1qTpFdbTable(object):
        """
        A table that contains information about unicast entries
        for which the device has forwarding and/or filtering
        information.  This information is used by the
        transparent bridging function in determining how to
        propagate a received frame.
        
        .. attribute:: dot1qtpfdbentry
        
        	Information about a specific unicast MAC address for which the device has some forwarding and/or filtering information
        	**type**\: list of :py:class:`Dot1qTpFdbEntry <ydk.models.q.Q_BRIDGE_MIB.QBRIDGEMIB.Dot1qTpFdbTable.Dot1qTpFdbEntry>`
        
        

        """

        _prefix = 'q-bridge'
        _revision = '2006-01-09'

        def __init__(self):
            self.parent = None
            self.dot1qtpfdbentry = YList()
            self.dot1qtpfdbentry.parent = self
            self.dot1qtpfdbentry.name = 'dot1qtpfdbentry'


        class Dot1qTpFdbEntry(object):
            """
            Information about a specific unicast MAC address for
            which the device has some forwarding and/or filtering
            information.
            
            .. attribute:: dot1qfdbid
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot1qtpfdbaddress
            
            	A unicast MAC address for which the device has forwarding and/or filtering information
            	**type**\: str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            .. attribute:: dot1qtpfdbport
            
            	Either the value '0', or the port number of the port on which a frame having a source address equal to the value of the corresponding instance of dot1qTpFdbAddress has been seen.  A value of '0' indicates that the port number has not been learned but that the device does have some forwarding/filtering information about this address (e.g., in the dot1qStaticUnicastTable). Implementors are encouraged to assign the port value to this object whenever it is learned, even for addresses for which the corresponding value of dot1qTpFdbStatus is not learned(3)
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: dot1qtpfdbstatus
            
            	The status of this entry.  The meanings of the values are\:     other(1) \- none of the following.  This may include         the case where some other MIB object (not the         corresponding instance of dot1qTpFdbPort, nor an         entry in the dot1qStaticUnicastTable) is being         used to determine if and how frames addressed to         the value of the corresponding instance of         dot1qTpFdbAddress are being forwarded.     invalid(2) \- this entry is no longer valid (e.g., it          was learned but has since aged out), but has not         yet been flushed from the table.     learned(3) \- the value of the corresponding instance         of dot1qTpFdbPort was learned and is being used.     self(4) \- the value of the corresponding instance of         dot1qTpFdbAddress represents one of the device's         addresses.  The corresponding instance of         dot1qTpFdbPort indicates which of the device's         ports has this address.     mgmt(5) \- the value of the corresponding instance of         dot1qTpFdbAddress is also the value of an         existing instance of dot1qStaticAddress
            	**type**\: :py:class:`Dot1qTpFdbStatus_Enum <ydk.models.q.Q_BRIDGE_MIB.QBRIDGEMIB.Dot1qTpFdbTable.Dot1qTpFdbEntry.Dot1qTpFdbStatus_Enum>`
            
            

            """

            _prefix = 'q-bridge'
            _revision = '2006-01-09'

            def __init__(self):
                self.parent = None
                self.dot1qfdbid = None
                self.dot1qtpfdbaddress = None
                self.dot1qtpfdbport = None
                self.dot1qtpfdbstatus = None

            class Dot1qTpFdbStatus_Enum(Enum):
                """
                Dot1qTpFdbStatus_Enum

                The status of this entry.  The meanings of the values
                are\:
                    other(1) \- none of the following.  This may include
                        the case where some other MIB object (not the
                        corresponding instance of dot1qTpFdbPort, nor an
                        entry in the dot1qStaticUnicastTable) is being
                        used to determine if and how frames addressed to
                        the value of the corresponding instance of
                        dot1qTpFdbAddress are being forwarded.
                    invalid(2) \- this entry is no longer valid (e.g., it
                
                        was learned but has since aged out), but has not
                        yet been flushed from the table.
                    learned(3) \- the value of the corresponding instance
                        of dot1qTpFdbPort was learned and is being used.
                    self(4) \- the value of the corresponding instance of
                        dot1qTpFdbAddress represents one of the device's
                        addresses.  The corresponding instance of
                        dot1qTpFdbPort indicates which of the device's
                        ports has this address.
                    mgmt(5) \- the value of the corresponding instance of
                        dot1qTpFdbAddress is also the value of an
                        existing instance of dot1qStaticAddress.

                """

                OTHER = 1

                INVALID = 2

                LEARNED = 3

                SELF = 4

                MGMT = 5


                @staticmethod
                def _meta_info():
                    from ydk.models.q._meta import _Q_BRIDGE_MIB as meta
                    return meta._meta_table['QBRIDGEMIB.Dot1qTpFdbTable.Dot1qTpFdbEntry.Dot1qTpFdbStatus_Enum']


            @property
            def _common_path(self):
                if self.dot1qfdbid is None:
                    raise YPYDataValidationError('Key property dot1qfdbid is None')
                if self.dot1qtpfdbaddress is None:
                    raise YPYDataValidationError('Key property dot1qtpfdbaddress is None')

                return '/Q-BRIDGE-MIB:Q-BRIDGE-MIB/Q-BRIDGE-MIB:dot1qTpFdbTable/Q-BRIDGE-MIB:dot1qTpFdbEntry[Q-BRIDGE-MIB:dot1qFdbId = ' + str(self.dot1qfdbid) + '][Q-BRIDGE-MIB:dot1qTpFdbAddress = ' + str(self.dot1qtpfdbaddress) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.dot1qfdbid is not None:
                    return True

                if self.dot1qtpfdbaddress is not None:
                    return True

                if self.dot1qtpfdbport is not None:
                    return True

                if self.dot1qtpfdbstatus is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.q._meta import _Q_BRIDGE_MIB as meta
                return meta._meta_table['QBRIDGEMIB.Dot1qTpFdbTable.Dot1qTpFdbEntry']['meta_info']

        @property
        def _common_path(self):

            return '/Q-BRIDGE-MIB:Q-BRIDGE-MIB/Q-BRIDGE-MIB:dot1qTpFdbTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.dot1qtpfdbentry is not None:
                for child_ref in self.dot1qtpfdbentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.q._meta import _Q_BRIDGE_MIB as meta
            return meta._meta_table['QBRIDGEMIB.Dot1qTpFdbTable']['meta_info']


    class Dot1qTpGroupTable(object):
        """
        A table containing filtering information for VLANs
        configured into the bridge by (local or network)
        management, or learned dynamically, specifying the set of
        ports to which frames received on a VLAN for this FDB
        and containing a specific Group destination address are
        allowed to be forwarded.
        
        .. attribute:: dot1qtpgroupentry
        
        	Filtering information configured into the bridge by management, or learned dynamically, specifying the set of ports to which frames received on a VLAN and containing a specific Group destination address are allowed to be forwarded.  The subset of these ports learned dynamically is also provided
        	**type**\: list of :py:class:`Dot1qTpGroupEntry <ydk.models.q.Q_BRIDGE_MIB.QBRIDGEMIB.Dot1qTpGroupTable.Dot1qTpGroupEntry>`
        
        

        """

        _prefix = 'q-bridge'
        _revision = '2006-01-09'

        def __init__(self):
            self.parent = None
            self.dot1qtpgroupentry = YList()
            self.dot1qtpgroupentry.parent = self
            self.dot1qtpgroupentry.name = 'dot1qtpgroupentry'


        class Dot1qTpGroupEntry(object):
            """
            Filtering information configured into the bridge by
            management, or learned dynamically, specifying the set of
            ports to which frames received on a VLAN and containing
            a specific Group destination address are allowed to be
            forwarded.  The subset of these ports learned dynamically
            is also provided.
            
            .. attribute:: dot1qtpgroupaddress
            
            	The destination Group MAC address in a frame to which this entry's filtering information applies
            	**type**\: str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            .. attribute:: dot1qvlanindex
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot1qtpgroupegressports
            
            	The complete set of ports, in this VLAN, to which frames destined for this Group MAC address are currently being explicitly forwarded.  This does not include ports for which this address is only implicitly forwarded, in the dot1qForwardAllPorts list
            	**type**\: str
            
            .. attribute:: dot1qtpgrouplearnt
            
            	The subset of ports in dot1qTpGroupEgressPorts that were learned by GMRP or some other dynamic mechanism, in this Filtering database
            	**type**\: str
            
            

            """

            _prefix = 'q-bridge'
            _revision = '2006-01-09'

            def __init__(self):
                self.parent = None
                self.dot1qtpgroupaddress = None
                self.dot1qvlanindex = None
                self.dot1qtpgroupegressports = None
                self.dot1qtpgrouplearnt = None

            @property
            def _common_path(self):
                if self.dot1qtpgroupaddress is None:
                    raise YPYDataValidationError('Key property dot1qtpgroupaddress is None')
                if self.dot1qvlanindex is None:
                    raise YPYDataValidationError('Key property dot1qvlanindex is None')

                return '/Q-BRIDGE-MIB:Q-BRIDGE-MIB/Q-BRIDGE-MIB:dot1qTpGroupTable/Q-BRIDGE-MIB:dot1qTpGroupEntry[Q-BRIDGE-MIB:dot1qTpGroupAddress = ' + str(self.dot1qtpgroupaddress) + '][Q-BRIDGE-MIB:dot1qVlanIndex = ' + str(self.dot1qvlanindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.dot1qtpgroupaddress is not None:
                    return True

                if self.dot1qvlanindex is not None:
                    return True

                if self.dot1qtpgroupegressports is not None:
                    return True

                if self.dot1qtpgrouplearnt is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.q._meta import _Q_BRIDGE_MIB as meta
                return meta._meta_table['QBRIDGEMIB.Dot1qTpGroupTable.Dot1qTpGroupEntry']['meta_info']

        @property
        def _common_path(self):

            return '/Q-BRIDGE-MIB:Q-BRIDGE-MIB/Q-BRIDGE-MIB:dot1qTpGroupTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.dot1qtpgroupentry is not None:
                for child_ref in self.dot1qtpgroupentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.q._meta import _Q_BRIDGE_MIB as meta
            return meta._meta_table['QBRIDGEMIB.Dot1qTpGroupTable']['meta_info']


    class Dot1qVlan(object):
        """
        
        
        .. attribute:: dot1qconstraintsetdefault
        
        	The identity of the constraint set to which a VLAN belongs, if there is not an explicit entry for that VLAN in dot1qLearningConstraintsTable.  The value of this object MUST be retained across reinitializations of the management system
        	**type**\: int
        
        	**range:** 0..65535
        
        .. attribute:: dot1qconstrainttypedefault
        
        	The type of constraint set to which a VLAN belongs, if there is not an explicit entry for that VLAN in dot1qLearningConstraintsTable.  The types are as defined for dot1qConstraintType.  The value of this object MUST be retained across  reinitializations of the management system
        	**type**\: :py:class:`Dot1qConstraintTypeDefault_Enum <ydk.models.q.Q_BRIDGE_MIB.QBRIDGEMIB.Dot1qVlan.Dot1qConstraintTypeDefault_Enum>`
        
        .. attribute:: dot1qnextfreelocalvlanindex
        
        	The next available value for dot1qVlanIndex of a local VLAN entry in dot1qVlanStaticTable.  This will report values >=4096 if a new Local VLAN may be created or else the value 0 if this is not possible.  A row creation operation in this table for an entry with a local VlanIndex value may fail if the current value of this object is not used as the index.  Even if the value read is used, there is no guarantee that it will still be the valid index when the create operation is attempted; another manager may have already got in during the intervening time interval. In this case, dot1qNextFreeLocalVlanIndex should be re\-read  and the creation re\-tried with the new value.  This value will automatically change when the current value is used to create a new row
        	**type**\: int
        
        	**range:** 0 \| 4096..2147483647
        
        .. attribute:: dot1qvlannumdeletes
        
        	The number of times a VLAN entry has been deleted from the dot1qVlanCurrentTable (for any reason).  If an entry is deleted, then inserted, and then deleted, this counter will be incremented by 2
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'q-bridge'
        _revision = '2006-01-09'

        def __init__(self):
            self.parent = None
            self.dot1qconstraintsetdefault = None
            self.dot1qconstrainttypedefault = None
            self.dot1qnextfreelocalvlanindex = None
            self.dot1qvlannumdeletes = None

        class Dot1qConstraintTypeDefault_Enum(Enum):
            """
            Dot1qConstraintTypeDefault_Enum

            The type of constraint set to which a VLAN belongs, if
            there is not an explicit entry for that VLAN in
            dot1qLearningConstraintsTable.  The types are as defined
            for dot1qConstraintType.
            
            The value of this object MUST be retained across
            
            reinitializations of the management system.

            """

            INDEPENDENT = 1

            SHARED = 2


            @staticmethod
            def _meta_info():
                from ydk.models.q._meta import _Q_BRIDGE_MIB as meta
                return meta._meta_table['QBRIDGEMIB.Dot1qVlan.Dot1qConstraintTypeDefault_Enum']


        @property
        def _common_path(self):

            return '/Q-BRIDGE-MIB:Q-BRIDGE-MIB/Q-BRIDGE-MIB:dot1qVlan'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.dot1qconstraintsetdefault is not None:
                return True

            if self.dot1qconstrainttypedefault is not None:
                return True

            if self.dot1qnextfreelocalvlanindex is not None:
                return True

            if self.dot1qvlannumdeletes is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.q._meta import _Q_BRIDGE_MIB as meta
            return meta._meta_table['QBRIDGEMIB.Dot1qVlan']['meta_info']


    class Dot1qVlanCurrentTable(object):
        """
        A table containing current configuration information
        for each VLAN currently configured into the device by
        (local or network) management, or dynamically created
        as a result of GVRP requests received.
        
        .. attribute:: dot1qvlancurrententry
        
        	Information for a VLAN configured into the device by  (local or network) management, or dynamically created as a result of GVRP requests received
        	**type**\: list of :py:class:`Dot1qVlanCurrentEntry <ydk.models.q.Q_BRIDGE_MIB.QBRIDGEMIB.Dot1qVlanCurrentTable.Dot1qVlanCurrentEntry>`
        
        

        """

        _prefix = 'q-bridge'
        _revision = '2006-01-09'

        def __init__(self):
            self.parent = None
            self.dot1qvlancurrententry = YList()
            self.dot1qvlancurrententry.parent = self
            self.dot1qvlancurrententry.name = 'dot1qvlancurrententry'


        class Dot1qVlanCurrentEntry(object):
            """
            Information for a VLAN configured into the device by
            
            (local or network) management, or dynamically created
            as a result of GVRP requests received.
            
            .. attribute:: dot1qvlanindex
            
            	The VLAN\-ID or other identifier referring to this VLAN
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot1qvlantimemark
            
            	A TimeFilter for this entry.  See the TimeFilter textual convention to see how this works
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot1qvlancreationtime
            
            	The value of sysUpTime when this VLAN was created
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot1qvlancurrentegressports
            
            	The set of ports that are transmitting traffic for this VLAN as either tagged or untagged frames
            	**type**\: str
            
            .. attribute:: dot1qvlancurrentuntaggedports
            
            	The set of ports that are transmitting traffic for this VLAN as untagged frames
            	**type**\: str
            
            .. attribute:: dot1qvlanfdbid
            
            	The Filtering Database used by this VLAN.  This is one of the dot1qFdbId values in the dot1qFdbTable.  This value is allocated automatically by the device whenever  the VLAN is created\: either dynamically by GVRP, or by management, in dot1qVlanStaticTable.  Allocation of this value follows the learning constraints defined for this VLAN in dot1qLearningConstraintsTable
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot1qvlanstatus
            
            	This object indicates the status of this entry. other(1) \- this entry is currently in use, but the     conditions under which it will remain so differ     from the following values. permanent(2) \- this entry, corresponding to an entry     in dot1qVlanStaticTable, is currently in use and     will remain so after the next reset of the     device.  The port lists for this entry include     ports from the equivalent dot1qVlanStaticTable     entry and ports learned dynamically. dynamicGvrp(3) \- this entry is currently in use      and will remain so until removed by GVRP.  There     is no static entry for this VLAN, and it will be     removed when the last port leaves the VLAN
            	**type**\: :py:class:`Dot1qVlanStatus_Enum <ydk.models.q.Q_BRIDGE_MIB.QBRIDGEMIB.Dot1qVlanCurrentTable.Dot1qVlanCurrentEntry.Dot1qVlanStatus_Enum>`
            
            

            """

            _prefix = 'q-bridge'
            _revision = '2006-01-09'

            def __init__(self):
                self.parent = None
                self.dot1qvlanindex = None
                self.dot1qvlantimemark = None
                self.dot1qvlancreationtime = None
                self.dot1qvlancurrentegressports = None
                self.dot1qvlancurrentuntaggedports = None
                self.dot1qvlanfdbid = None
                self.dot1qvlanstatus = None

            class Dot1qVlanStatus_Enum(Enum):
                """
                Dot1qVlanStatus_Enum

                This object indicates the status of this entry.
                other(1) \- this entry is currently in use, but the
                    conditions under which it will remain so differ
                    from the following values.
                permanent(2) \- this entry, corresponding to an entry
                    in dot1qVlanStaticTable, is currently in use and
                    will remain so after the next reset of the
                    device.  The port lists for this entry include
                    ports from the equivalent dot1qVlanStaticTable
                    entry and ports learned dynamically.
                dynamicGvrp(3) \- this entry is currently in use
                
                    and will remain so until removed by GVRP.  There
                    is no static entry for this VLAN, and it will be
                    removed when the last port leaves the VLAN.

                """

                OTHER = 1

                PERMANENT = 2

                DYNAMICGVRP = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.q._meta import _Q_BRIDGE_MIB as meta
                    return meta._meta_table['QBRIDGEMIB.Dot1qVlanCurrentTable.Dot1qVlanCurrentEntry.Dot1qVlanStatus_Enum']


            @property
            def _common_path(self):
                if self.dot1qvlanindex is None:
                    raise YPYDataValidationError('Key property dot1qvlanindex is None')
                if self.dot1qvlantimemark is None:
                    raise YPYDataValidationError('Key property dot1qvlantimemark is None')

                return '/Q-BRIDGE-MIB:Q-BRIDGE-MIB/Q-BRIDGE-MIB:dot1qVlanCurrentTable/Q-BRIDGE-MIB:dot1qVlanCurrentEntry[Q-BRIDGE-MIB:dot1qVlanIndex = ' + str(self.dot1qvlanindex) + '][Q-BRIDGE-MIB:dot1qVlanTimeMark = ' + str(self.dot1qvlantimemark) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.dot1qvlanindex is not None:
                    return True

                if self.dot1qvlantimemark is not None:
                    return True

                if self.dot1qvlancreationtime is not None:
                    return True

                if self.dot1qvlancurrentegressports is not None:
                    return True

                if self.dot1qvlancurrentuntaggedports is not None:
                    return True

                if self.dot1qvlanfdbid is not None:
                    return True

                if self.dot1qvlanstatus is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.q._meta import _Q_BRIDGE_MIB as meta
                return meta._meta_table['QBRIDGEMIB.Dot1qVlanCurrentTable.Dot1qVlanCurrentEntry']['meta_info']

        @property
        def _common_path(self):

            return '/Q-BRIDGE-MIB:Q-BRIDGE-MIB/Q-BRIDGE-MIB:dot1qVlanCurrentTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.dot1qvlancurrententry is not None:
                for child_ref in self.dot1qvlancurrententry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.q._meta import _Q_BRIDGE_MIB as meta
            return meta._meta_table['QBRIDGEMIB.Dot1qVlanCurrentTable']['meta_info']


    class Dot1qVlanStaticTable(object):
        """
        A table containing static configuration information for
        each VLAN configured into the device by (local or
        network) management.  All entries are permanent and will
        be restored after the device is reset.
        
        .. attribute:: dot1qvlanstaticentry
        
        	Static information for a VLAN configured into the device by (local or network) management
        	**type**\: list of :py:class:`Dot1qVlanStaticEntry <ydk.models.q.Q_BRIDGE_MIB.QBRIDGEMIB.Dot1qVlanStaticTable.Dot1qVlanStaticEntry>`
        
        

        """

        _prefix = 'q-bridge'
        _revision = '2006-01-09'

        def __init__(self):
            self.parent = None
            self.dot1qvlanstaticentry = YList()
            self.dot1qvlanstaticentry.parent = self
            self.dot1qvlanstaticentry.name = 'dot1qvlanstaticentry'


        class Dot1qVlanStaticEntry(object):
            """
            Static information for a VLAN configured into the
            device by (local or network) management.
            
            .. attribute:: dot1qvlanindex
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot1qvlanforbiddenegressports
            
            	The set of ports that are prohibited by management from being included in the egress list for this VLAN. Changes to this object that cause a port to be included or excluded affect the per\-port, per\-VLAN Registrar control for Registration Forbidden for the relevant GVRP state machine on each port.  A port may not be added in this set if it is already a member of the set of ports in dot1qVlanStaticEgressPorts.  The default value of this object is a string of zeros of appropriate length, excluding all ports from the forbidden set
            	**type**\: str
            
            .. attribute:: dot1qvlanstaticegressports
            
            	The set of ports that are permanently assigned to the egress list for this VLAN by management.  Changes to a bit in this object affect the per\-port, per\-VLAN Registrar control for Registration Fixed for the relevant GVRP state machine on each port.  A port may not be added in this set if it is already a member of the set of ports in dot1qVlanForbiddenEgressPorts.  The default value of this object is a string of zeros of appropriate length, indicating not fixed
            	**type**\: str
            
            .. attribute:: dot1qvlanstaticname
            
            	An administratively assigned string, which may be used to identify the VLAN
            	**type**\: str
            
            	**range:** 0..32
            
            .. attribute:: dot1qvlanstaticrowstatus
            
            	This object indicates the status of this entry
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            .. attribute:: dot1qvlanstaticuntaggedports
            
            	The set of ports that should transmit egress packets for this VLAN as untagged.  The default value of this object for the default VLAN (dot1qVlanIndex = 1) is a string of appropriate length including all ports.  There is no specified default for other VLANs.  If a device agent cannot support the set of ports being set, then it will reject the set operation with an error.  For example, a manager might attempt to set more than one VLAN to be untagged on egress where the device does not support this IEEE 802.1Q option
            	**type**\: str
            
            

            """

            _prefix = 'q-bridge'
            _revision = '2006-01-09'

            def __init__(self):
                self.parent = None
                self.dot1qvlanindex = None
                self.dot1qvlanforbiddenegressports = None
                self.dot1qvlanstaticegressports = None
                self.dot1qvlanstaticname = None
                self.dot1qvlanstaticrowstatus = None
                self.dot1qvlanstaticuntaggedports = None

            @property
            def _common_path(self):
                if self.dot1qvlanindex is None:
                    raise YPYDataValidationError('Key property dot1qvlanindex is None')

                return '/Q-BRIDGE-MIB:Q-BRIDGE-MIB/Q-BRIDGE-MIB:dot1qVlanStaticTable/Q-BRIDGE-MIB:dot1qVlanStaticEntry[Q-BRIDGE-MIB:dot1qVlanIndex = ' + str(self.dot1qvlanindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.dot1qvlanindex is not None:
                    return True

                if self.dot1qvlanforbiddenegressports is not None:
                    return True

                if self.dot1qvlanstaticegressports is not None:
                    return True

                if self.dot1qvlanstaticname is not None:
                    return True

                if self.dot1qvlanstaticrowstatus is not None:
                    return True

                if self.dot1qvlanstaticuntaggedports is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.q._meta import _Q_BRIDGE_MIB as meta
                return meta._meta_table['QBRIDGEMIB.Dot1qVlanStaticTable.Dot1qVlanStaticEntry']['meta_info']

        @property
        def _common_path(self):

            return '/Q-BRIDGE-MIB:Q-BRIDGE-MIB/Q-BRIDGE-MIB:dot1qVlanStaticTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.dot1qvlanstaticentry is not None:
                for child_ref in self.dot1qvlanstaticentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.q._meta import _Q_BRIDGE_MIB as meta
            return meta._meta_table['QBRIDGEMIB.Dot1qVlanStaticTable']['meta_info']


    class Dot1vProtocolGroupTable(object):
        """
        A table that contains mappings from Protocol
        Templates to Protocol Group Identifiers used for
        Port\-and\-Protocol\-based VLAN Classification.
        
        .. attribute:: dot1vprotocolgroupentry
        
        	A mapping from a Protocol Template to a Protocol Group Identifier
        	**type**\: list of :py:class:`Dot1vProtocolGroupEntry <ydk.models.q.Q_BRIDGE_MIB.QBRIDGEMIB.Dot1vProtocolGroupTable.Dot1vProtocolGroupEntry>`
        
        

        """

        _prefix = 'q-bridge'
        _revision = '2006-01-09'

        def __init__(self):
            self.parent = None
            self.dot1vprotocolgroupentry = YList()
            self.dot1vprotocolgroupentry.parent = self
            self.dot1vprotocolgroupentry.name = 'dot1vprotocolgroupentry'


        class Dot1vProtocolGroupEntry(object):
            """
            A mapping from a Protocol Template to a Protocol
            Group Identifier.
            
            .. attribute:: dot1vprotocoltemplateframetype
            
            	The data\-link encapsulation format or the 'detagged\_frame\_type' in a Protocol Template
            	**type**\: :py:class:`Dot1vProtocolTemplateFrameType_Enum <ydk.models.q.Q_BRIDGE_MIB.QBRIDGEMIB.Dot1vProtocolGroupTable.Dot1vProtocolGroupEntry.Dot1vProtocolTemplateFrameType_Enum>`
            
            .. attribute:: dot1vprotocoltemplateprotocolvalue
            
            	The identification of the protocol above the data\-link layer in a Protocol Template.  Depending on the frame type, the octet string will have one of the following values\:  For 'ethernet', 'rfc1042' and 'snap8021H',     this is the 16\-bit (2\-octet) IEEE 802.3 Type Field. For 'snapOther',     this is the 40\-bit (5\-octet) PID. For 'llcOther',     this is the 2\-octet IEEE 802.2 Link Service Access     Point (LSAP) pair\: first octet for Destination Service     Access Point (DSAP) and second octet for Source Service     Access Point (SSAP)
            	**type**\: str
            
            	**range:** 2 \| 5
            
            .. attribute:: dot1vprotocolgroupid
            
            	Represents a group of protocols that are associated together when assigning a VID to a frame
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: dot1vprotocolgrouprowstatus
            
            	This object indicates the status of this entry
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            

            """

            _prefix = 'q-bridge'
            _revision = '2006-01-09'

            def __init__(self):
                self.parent = None
                self.dot1vprotocoltemplateframetype = None
                self.dot1vprotocoltemplateprotocolvalue = None
                self.dot1vprotocolgroupid = None
                self.dot1vprotocolgrouprowstatus = None

            class Dot1vProtocolTemplateFrameType_Enum(Enum):
                """
                Dot1vProtocolTemplateFrameType_Enum

                The data\-link encapsulation format or the
                'detagged\_frame\_type' in a Protocol Template.

                """

                ETHERNET = 1

                RFC1042 = 2

                SNAP8021H = 3

                SNAPOTHER = 4

                LLCOTHER = 5


                @staticmethod
                def _meta_info():
                    from ydk.models.q._meta import _Q_BRIDGE_MIB as meta
                    return meta._meta_table['QBRIDGEMIB.Dot1vProtocolGroupTable.Dot1vProtocolGroupEntry.Dot1vProtocolTemplateFrameType_Enum']


            @property
            def _common_path(self):
                if self.dot1vprotocoltemplateframetype is None:
                    raise YPYDataValidationError('Key property dot1vprotocoltemplateframetype is None')
                if self.dot1vprotocoltemplateprotocolvalue is None:
                    raise YPYDataValidationError('Key property dot1vprotocoltemplateprotocolvalue is None')

                return '/Q-BRIDGE-MIB:Q-BRIDGE-MIB/Q-BRIDGE-MIB:dot1vProtocolGroupTable/Q-BRIDGE-MIB:dot1vProtocolGroupEntry[Q-BRIDGE-MIB:dot1vProtocolTemplateFrameType = ' + str(self.dot1vprotocoltemplateframetype) + '][Q-BRIDGE-MIB:dot1vProtocolTemplateProtocolValue = ' + str(self.dot1vprotocoltemplateprotocolvalue) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.dot1vprotocoltemplateframetype is not None:
                    return True

                if self.dot1vprotocoltemplateprotocolvalue is not None:
                    return True

                if self.dot1vprotocolgroupid is not None:
                    return True

                if self.dot1vprotocolgrouprowstatus is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.q._meta import _Q_BRIDGE_MIB as meta
                return meta._meta_table['QBRIDGEMIB.Dot1vProtocolGroupTable.Dot1vProtocolGroupEntry']['meta_info']

        @property
        def _common_path(self):

            return '/Q-BRIDGE-MIB:Q-BRIDGE-MIB/Q-BRIDGE-MIB:dot1vProtocolGroupTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.dot1vprotocolgroupentry is not None:
                for child_ref in self.dot1vprotocolgroupentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.q._meta import _Q_BRIDGE_MIB as meta
            return meta._meta_table['QBRIDGEMIB.Dot1vProtocolGroupTable']['meta_info']


    class Dot1vProtocolPortTable(object):
        """
        A table that contains VID sets used for
        Port\-and\-Protocol\-based VLAN Classification.
        
        .. attribute:: dot1vprotocolportentry
        
        	A VID set for a port
        	**type**\: list of :py:class:`Dot1vProtocolPortEntry <ydk.models.q.Q_BRIDGE_MIB.QBRIDGEMIB.Dot1vProtocolPortTable.Dot1vProtocolPortEntry>`
        
        

        """

        _prefix = 'q-bridge'
        _revision = '2006-01-09'

        def __init__(self):
            self.parent = None
            self.dot1vprotocolportentry = YList()
            self.dot1vprotocolportentry.parent = self
            self.dot1vprotocolportentry.name = 'dot1vprotocolportentry'


        class Dot1vProtocolPortEntry(object):
            """
            A VID set for a port.
            
            .. attribute:: dot1dbaseport
            
            	
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: dot1vprotocolportgroupid
            
            	Designates a group of protocols in the Protocol Group Database
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: dot1vprotocolportgroupvid
            
            	The VID associated with a group of protocols for each port
            	**type**\: int
            
            	**range:** 1..4094
            
            .. attribute:: dot1vprotocolportrowstatus
            
            	This object indicates the status of this entry
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            

            """

            _prefix = 'q-bridge'
            _revision = '2006-01-09'

            def __init__(self):
                self.parent = None
                self.dot1dbaseport = None
                self.dot1vprotocolportgroupid = None
                self.dot1vprotocolportgroupvid = None
                self.dot1vprotocolportrowstatus = None

            @property
            def _common_path(self):
                if self.dot1dbaseport is None:
                    raise YPYDataValidationError('Key property dot1dbaseport is None')
                if self.dot1vprotocolportgroupid is None:
                    raise YPYDataValidationError('Key property dot1vprotocolportgroupid is None')

                return '/Q-BRIDGE-MIB:Q-BRIDGE-MIB/Q-BRIDGE-MIB:dot1vProtocolPortTable/Q-BRIDGE-MIB:dot1vProtocolPortEntry[Q-BRIDGE-MIB:dot1dBasePort = ' + str(self.dot1dbaseport) + '][Q-BRIDGE-MIB:dot1vProtocolPortGroupId = ' + str(self.dot1vprotocolportgroupid) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.dot1dbaseport is not None:
                    return True

                if self.dot1vprotocolportgroupid is not None:
                    return True

                if self.dot1vprotocolportgroupvid is not None:
                    return True

                if self.dot1vprotocolportrowstatus is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.q._meta import _Q_BRIDGE_MIB as meta
                return meta._meta_table['QBRIDGEMIB.Dot1vProtocolPortTable.Dot1vProtocolPortEntry']['meta_info']

        @property
        def _common_path(self):

            return '/Q-BRIDGE-MIB:Q-BRIDGE-MIB/Q-BRIDGE-MIB:dot1vProtocolPortTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.dot1vprotocolportentry is not None:
                for child_ref in self.dot1vprotocolportentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.q._meta import _Q_BRIDGE_MIB as meta
            return meta._meta_table['QBRIDGEMIB.Dot1vProtocolPortTable']['meta_info']

    @property
    def _common_path(self):

        return '/Q-BRIDGE-MIB:Q-BRIDGE-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.dot1qbase is not None and self.dot1qbase._has_data():
            return True

        if self.dot1qbase is not None and self.dot1qbase.is_presence():
            return True

        if self.dot1qfdbtable is not None and self.dot1qfdbtable._has_data():
            return True

        if self.dot1qfdbtable is not None and self.dot1qfdbtable.is_presence():
            return True

        if self.dot1qforwardalltable is not None and self.dot1qforwardalltable._has_data():
            return True

        if self.dot1qforwardalltable is not None and self.dot1qforwardalltable.is_presence():
            return True

        if self.dot1qforwardunregisteredtable is not None and self.dot1qforwardunregisteredtable._has_data():
            return True

        if self.dot1qforwardunregisteredtable is not None and self.dot1qforwardunregisteredtable.is_presence():
            return True

        if self.dot1qlearningconstraintstable is not None and self.dot1qlearningconstraintstable._has_data():
            return True

        if self.dot1qlearningconstraintstable is not None and self.dot1qlearningconstraintstable.is_presence():
            return True

        if self.dot1qportvlanhcstatisticstable is not None and self.dot1qportvlanhcstatisticstable._has_data():
            return True

        if self.dot1qportvlanhcstatisticstable is not None and self.dot1qportvlanhcstatisticstable.is_presence():
            return True

        if self.dot1qportvlanstatisticstable is not None and self.dot1qportvlanstatisticstable._has_data():
            return True

        if self.dot1qportvlanstatisticstable is not None and self.dot1qportvlanstatisticstable.is_presence():
            return True

        if self.dot1qstaticmulticasttable is not None and self.dot1qstaticmulticasttable._has_data():
            return True

        if self.dot1qstaticmulticasttable is not None and self.dot1qstaticmulticasttable.is_presence():
            return True

        if self.dot1qstaticunicasttable is not None and self.dot1qstaticunicasttable._has_data():
            return True

        if self.dot1qstaticunicasttable is not None and self.dot1qstaticunicasttable.is_presence():
            return True

        if self.dot1qtpfdbtable is not None and self.dot1qtpfdbtable._has_data():
            return True

        if self.dot1qtpfdbtable is not None and self.dot1qtpfdbtable.is_presence():
            return True

        if self.dot1qtpgrouptable is not None and self.dot1qtpgrouptable._has_data():
            return True

        if self.dot1qtpgrouptable is not None and self.dot1qtpgrouptable.is_presence():
            return True

        if self.dot1qvlan is not None and self.dot1qvlan._has_data():
            return True

        if self.dot1qvlan is not None and self.dot1qvlan.is_presence():
            return True

        if self.dot1qvlancurrenttable is not None and self.dot1qvlancurrenttable._has_data():
            return True

        if self.dot1qvlancurrenttable is not None and self.dot1qvlancurrenttable.is_presence():
            return True

        if self.dot1qvlanstatictable is not None and self.dot1qvlanstatictable._has_data():
            return True

        if self.dot1qvlanstatictable is not None and self.dot1qvlanstatictable.is_presence():
            return True

        if self.dot1vprotocolgrouptable is not None and self.dot1vprotocolgrouptable._has_data():
            return True

        if self.dot1vprotocolgrouptable is not None and self.dot1vprotocolgrouptable.is_presence():
            return True

        if self.dot1vprotocolporttable is not None and self.dot1vprotocolporttable._has_data():
            return True

        if self.dot1vprotocolporttable is not None and self.dot1vprotocolporttable.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.q._meta import _Q_BRIDGE_MIB as meta
        return meta._meta_table['QBRIDGEMIB']['meta_info']


