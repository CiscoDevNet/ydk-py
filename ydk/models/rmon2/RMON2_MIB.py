""" RMON2_MIB 

The MIB module for managing remote monitoring
device implementations. This MIB module
augments the original RMON MIB as specified in
RFC 1757.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError


from ydk.models.snmpv2.SNMPv2_TC import RowStatus_Enum


class RMON2MIB(object):
    """
    
    
    .. attribute:: addressmap
    
    	
    	**type**\: :py:class:`AddressMap <ydk.models.rmon2.RMON2_MIB.RMON2MIB.AddressMap>`
    
    .. attribute:: addressmapcontroltable
    
    	A table to control the collection of network layer address to physical address to interface mappings.  Note that this is not like the typical RMON controlTable and dataTable in which each entry creates its own data table.  Each entry in this table enables the discovery of addresses on a new interface and the placement of address mappings into the central addressMapTable.  Implementations are encouraged to add an entry per monitored interface upon initialization so that a default collection of address mappings is available
    	**type**\: :py:class:`AddressMapControlTable <ydk.models.rmon2.RMON2_MIB.RMON2MIB.AddressMapControlTable>`
    
    .. attribute:: addressmaptable
    
    	A table of network layer address to physical address to interface mappings.  The probe will add entries to this table based on the source MAC and network addresses seen in packets without MAC\-level errors. The probe will populate this table for all protocols in the protocol directory table whose value of protocolDirAddressMapConfig is equal to supportedOn(3), and will delete any entries whose protocolDirEntry is deleted or has a protocolDirAddressMapConfig value of supportedOff(2)
    	**type**\: :py:class:`AddressMapTable <ydk.models.rmon2.RMON2_MIB.RMON2MIB.AddressMapTable>`
    
    .. attribute:: alhosttable
    
    	A collection of statistics for a particular protocol from a particular network address that has been discovered on an interface of this device.  The probe will populate this table for all protocols in the protocol directory table whose value of protocolDirHostConfig is equal to supportedOn(3), and will delete any entries whose protocolDirEntry is deleted or has a protocolDirHostConfig value of supportedOff(2).  The probe will add to this table all addresses seen as the source or destination address in all packets with no MAC errors, and will increment octet and packet counts in the table for all packets with no MAC errors.  Further, entries will only be added to this table if their address exists in the nlHostTable and will be deleted from this table if their address is deleted from the nlHostTable
    	**type**\: :py:class:`AlHostTable <ydk.models.rmon2.RMON2_MIB.RMON2MIB.AlHostTable>`
    
    .. attribute:: almatrixdstable
    
    	A list of application traffic matrix entries which collect statistics for conversations of a particular protocol between two network\-level addresses.  This table is indexed first by the destination address and then by the source address to make it convenient to collect all statistics to a particular address.  The probe will populate this table for all protocols in the protocol directory table whose value of protocolDirMatrixConfig is equal to supportedOn(3), and will delete any entries whose protocolDirEntry is deleted or has a protocolDirMatrixConfig value of supportedOff(2).  The probe will add to this table all pairs of addresses for all protocols seen in all packets with no MAC errors, and will increment octet and packet counts in the table for all packets with no MAC errors.  Further, entries will only be added to this table if their address pair exists in the nlMatrixDSTable and will be deleted from this table if the address pair is deleted from the nlMatrixDSTable
    	**type**\: :py:class:`AlMatrixDSTable <ydk.models.rmon2.RMON2_MIB.RMON2MIB.AlMatrixDSTable>`
    
    .. attribute:: almatrixsdtable
    
    	A list of application traffic matrix entries which collect      statistics for conversations of a particular protocol between two network\-level addresses.  This table is indexed first by the source address and then by the destination address to make it convenient to collect all statistics from a particular address.  The probe will populate this table for all protocols in the protocol directory table whose value of protocolDirMatrixConfig is equal to supportedOn(3), and will delete any entries whose protocolDirEntry is deleted or has a protocolDirMatrixConfig value of supportedOff(2).  The probe will add to this table all pairs of addresses for all protocols seen in all packets with no MAC errors, and will increment octet and packet counts in the table for all packets with no MAC errors.  Further, entries will only be added to this table if their address pair exists in the nlMatrixSDTable and will be deleted from this table if the address pair is deleted from the nlMatrixSDTable
    	**type**\: :py:class:`AlMatrixSDTable <ydk.models.rmon2.RMON2_MIB.RMON2MIB.AlMatrixSDTable>`
    
    .. attribute:: almatrixtopncontroltable
    
    	A set of parameters that control the creation of a report of the top N matrix entries according to a selected metric
    	**type**\: :py:class:`AlMatrixTopNControlTable <ydk.models.rmon2.RMON2_MIB.RMON2MIB.AlMatrixTopNControlTable>`
    
    .. attribute:: almatrixtopntable
    
    	A set of statistics for those application layer matrix entries that have counted the highest number of octets or packets
    	**type**\: :py:class:`AlMatrixTopNTable <ydk.models.rmon2.RMON2_MIB.RMON2MIB.AlMatrixTopNTable>`
    
    .. attribute:: hlhostcontroltable
    
    	A list of higher layer (i.e. non\-MAC) host table control entries.  These entries will enable the collection of the network and application level host tables indexed by network addresses. Both the network and application level host tables are controlled by this table is so that they will both be created and deleted at the same time, further increasing the ease with which they can be implemented as a single datastore (note that if an implementation stores application layer host records in memory, it can derive network layer host records from them).  Entries in the nlHostTable will be created on behalf of each entry in this table. Additionally, if this probe implements the alHostTable, entries in the alHostTable will be created on behalf of each entry in this table.  Implementations are encouraged to add an entry per monitored interface upon initialization so that a default collection of host statistics is available
    	**type**\: :py:class:`HlHostControlTable <ydk.models.rmon2.RMON2_MIB.RMON2MIB.HlHostControlTable>`
    
    .. attribute:: hlmatrixcontroltable
    
    	A list of higher layer (i.e. non\-MAC) matrix control entries.  These entries will enable the collection of the network and application level matrix tables containing conversation statistics indexed by pairs of network addresses. Both the network and application level matrix tables are controlled by this table is so that they will both be created and deleted at the same time, further increasing the ease with which they can be implemented as a single datastore (note that if an implementation stores application layer matrix records in memory, it can derive network layer matrix records from them).  Entries in the nlMatrixSDTable and nlMatrixDSTable will be created on behalf of each entry in this table.  Additionally, if this probe implements the alMatrix tables, entries in the alMatrix tables will be created on behalf of each entry in this table
    	**type**\: :py:class:`HlMatrixControlTable <ydk.models.rmon2.RMON2_MIB.RMON2MIB.HlMatrixControlTable>`
    
    .. attribute:: netconfigtable
    
    	A table of netConfigEntries
    	**type**\: :py:class:`NetConfigTable <ydk.models.rmon2.RMON2_MIB.RMON2MIB.NetConfigTable>`
    
    .. attribute:: nlhosttable
    
    	A collection of statistics for a particular network layer address that has been discovered on an interface of this device.  The probe will populate this table for all network layer protocols in the protocol directory table whose value of protocolDirHostConfig is equal to supportedOn(3), and will delete any entries whose protocolDirEntry is deleted or has a protocolDirHostConfig value of supportedOff(2).  The probe will add to this table all addresses seen as the source or destination address in all packets with no MAC errors, and will increment octet and packet counts in the table for all packets with no MAC errors
    	**type**\: :py:class:`NlHostTable <ydk.models.rmon2.RMON2_MIB.RMON2MIB.NlHostTable>`
    
    .. attribute:: nlmatrixdstable
    
    	A list of traffic matrix entries which collect statistics for conversations between two network\-level addresses.  This table is indexed first by the destination address and then by the source address to make it convenient to collect all conversations to a particular address.  The probe will populate this table for all network layer protocols in the protocol directory table whose value of protocolDirMatrixConfig is equal to supportedOn(3), and will delete any entries whose protocolDirEntry is deleted or has a protocolDirMatrixConfig value of supportedOff(2).  The probe will add to this table all pairs of addresses seen in all packets with no MAC errors, and will increment      octet and packet counts in the table for all packets with no MAC errors.  Further, this table will only contain entries that have a corresponding entry in the nlMatrixSDTable with the same source address and destination address
    	**type**\: :py:class:`NlMatrixDSTable <ydk.models.rmon2.RMON2_MIB.RMON2MIB.NlMatrixDSTable>`
    
    .. attribute:: nlmatrixsdtable
    
    	A list of traffic matrix entries which collect statistics for conversations between two network\-level addresses.  This table is indexed first by the source address and then by the destination address to make it convenient to collect all conversations from a particular address.  The probe will populate this table for all network layer protocols in the protocol directory table whose value of protocolDirMatrixConfig is equal to supportedOn(3), and will delete any entries whose protocolDirEntry is deleted or has a protocolDirMatrixConfig value of supportedOff(2).      The probe will add to this table all pairs of addresses seen in all packets with no MAC errors, and will increment octet and packet counts in the table for all packets with no MAC errors.  Further, this table will only contain entries that have a corresponding entry in the nlMatrixDSTable with the same source address and destination address
    	**type**\: :py:class:`NlMatrixSDTable <ydk.models.rmon2.RMON2_MIB.RMON2MIB.NlMatrixSDTable>`
    
    .. attribute:: nlmatrixtopncontroltable
    
    	A set of parameters that control the creation of a report of the top N matrix entries according to a selected metric
    	**type**\: :py:class:`NlMatrixTopNControlTable <ydk.models.rmon2.RMON2_MIB.RMON2MIB.NlMatrixTopNControlTable>`
    
    .. attribute:: nlmatrixtopntable
    
    	A set of statistics for those network layer matrix entries that have counted the highest number of octets or packets
    	**type**\: :py:class:`NlMatrixTopNTable <ydk.models.rmon2.RMON2_MIB.RMON2MIB.NlMatrixTopNTable>`
    
    .. attribute:: probeconfig
    
    	
    	**type**\: :py:class:`ProbeConfig <ydk.models.rmon2.RMON2_MIB.RMON2MIB.ProbeConfig>`
    
    .. attribute:: protocoldir
    
    	
    	**type**\: :py:class:`ProtocolDir <ydk.models.rmon2.RMON2_MIB.RMON2MIB.ProtocolDir>`
    
    .. attribute:: protocoldirtable
    
    	This table lists the protocols that this agent has the capability to decode and count.  There is one entry in this table for each such protocol.  These protocols represent different network layer, transport layer, and higher\-layer protocols.  The agent should boot up with this table preconfigured with those protocols that it knows about and wishes to monitor.  Implementations are strongly encouraged to support protocols higher than the network layer (at least for the protocol distribution group), even for implementations that don't support the application layer groups
    	**type**\: :py:class:`ProtocolDirTable <ydk.models.rmon2.RMON2_MIB.RMON2MIB.ProtocolDirTable>`
    
    .. attribute:: protocoldistcontroltable
    
    	Controls the setup of protocol type distribution statistics tables.  Implementations are encouraged to add an entry per monitored interface upon initialization so that a default collection of protocol statistics is available.  Rationale\: This table controls collection of very basic statistics for any or all of the protocols detected on a given interface. An NMS can use this table to quickly determine bandwidth allocation utilized by different protocols.  A media\-specific statistics collection could also be configured (e.g. etherStats, trPStats) to easily obtain total frame, octet, and droppedEvents for the same interface
    	**type**\: :py:class:`ProtocolDistControlTable <ydk.models.rmon2.RMON2_MIB.RMON2MIB.ProtocolDistControlTable>`
    
    .. attribute:: protocoldiststatstable
    
    	An entry is made in this table for every protocol in the      protocolDirTable which has been seen in at least one packet. Counters are updated in this table for every protocol type that is encountered when parsing a packet, but no counters are updated for packets with MAC\-layer errors.  Note that if a protocolDirEntry is deleted, all associated entries in this table are removed
    	**type**\: :py:class:`ProtocolDistStatsTable <ydk.models.rmon2.RMON2_MIB.RMON2MIB.ProtocolDistStatsTable>`
    
    .. attribute:: serialconfigtable
    
    	A table of serial interface configuration entries.  This data will be stored in non\-volatile memory and preserved across probe resets or power loss
    	**type**\: :py:class:`SerialConfigTable <ydk.models.rmon2.RMON2_MIB.RMON2MIB.SerialConfigTable>`
    
    .. attribute:: serialconnectiontable
    
    	A list of serialConnectionEntries
    	**type**\: :py:class:`SerialConnectionTable <ydk.models.rmon2.RMON2_MIB.RMON2MIB.SerialConnectionTable>`
    
    .. attribute:: trapdesttable
    
    	A list of trap destination entries
    	**type**\: :py:class:`TrapDestTable <ydk.models.rmon2.RMON2_MIB.RMON2MIB.TrapDestTable>`
    
    .. attribute:: usrhistorycontroltable
    
    	A list of data\-collection configuration entries
    	**type**\: :py:class:`UsrHistoryControlTable <ydk.models.rmon2.RMON2_MIB.RMON2MIB.UsrHistoryControlTable>`
    
    .. attribute:: usrhistoryobjecttable
    
    	A list of data\-collection configuration entries
    	**type**\: :py:class:`UsrHistoryObjectTable <ydk.models.rmon2.RMON2_MIB.RMON2MIB.UsrHistoryObjectTable>`
    
    .. attribute:: usrhistorytable
    
    	A list of user defined history entries
    	**type**\: :py:class:`UsrHistoryTable <ydk.models.rmon2.RMON2_MIB.RMON2MIB.UsrHistoryTable>`
    
    

    """

    _prefix = 'rmon2-mib'
    _revision = '1996-05-27'

    def __init__(self):
        self.addressmap = RMON2MIB.AddressMap()
        self.addressmap.parent = self
        self.addressmapcontroltable = RMON2MIB.AddressMapControlTable()
        self.addressmapcontroltable.parent = self
        self.addressmaptable = RMON2MIB.AddressMapTable()
        self.addressmaptable.parent = self
        self.alhosttable = RMON2MIB.AlHostTable()
        self.alhosttable.parent = self
        self.almatrixdstable = RMON2MIB.AlMatrixDSTable()
        self.almatrixdstable.parent = self
        self.almatrixsdtable = RMON2MIB.AlMatrixSDTable()
        self.almatrixsdtable.parent = self
        self.almatrixtopncontroltable = RMON2MIB.AlMatrixTopNControlTable()
        self.almatrixtopncontroltable.parent = self
        self.almatrixtopntable = RMON2MIB.AlMatrixTopNTable()
        self.almatrixtopntable.parent = self
        self.hlhostcontroltable = RMON2MIB.HlHostControlTable()
        self.hlhostcontroltable.parent = self
        self.hlmatrixcontroltable = RMON2MIB.HlMatrixControlTable()
        self.hlmatrixcontroltable.parent = self
        self.netconfigtable = RMON2MIB.NetConfigTable()
        self.netconfigtable.parent = self
        self.nlhosttable = RMON2MIB.NlHostTable()
        self.nlhosttable.parent = self
        self.nlmatrixdstable = RMON2MIB.NlMatrixDSTable()
        self.nlmatrixdstable.parent = self
        self.nlmatrixsdtable = RMON2MIB.NlMatrixSDTable()
        self.nlmatrixsdtable.parent = self
        self.nlmatrixtopncontroltable = RMON2MIB.NlMatrixTopNControlTable()
        self.nlmatrixtopncontroltable.parent = self
        self.nlmatrixtopntable = RMON2MIB.NlMatrixTopNTable()
        self.nlmatrixtopntable.parent = self
        self.probeconfig = RMON2MIB.ProbeConfig()
        self.probeconfig.parent = self
        self.protocoldir = RMON2MIB.ProtocolDir()
        self.protocoldir.parent = self
        self.protocoldirtable = RMON2MIB.ProtocolDirTable()
        self.protocoldirtable.parent = self
        self.protocoldistcontroltable = RMON2MIB.ProtocolDistControlTable()
        self.protocoldistcontroltable.parent = self
        self.protocoldiststatstable = RMON2MIB.ProtocolDistStatsTable()
        self.protocoldiststatstable.parent = self
        self.serialconfigtable = RMON2MIB.SerialConfigTable()
        self.serialconfigtable.parent = self
        self.serialconnectiontable = RMON2MIB.SerialConnectionTable()
        self.serialconnectiontable.parent = self
        self.trapdesttable = RMON2MIB.TrapDestTable()
        self.trapdesttable.parent = self
        self.usrhistorycontroltable = RMON2MIB.UsrHistoryControlTable()
        self.usrhistorycontroltable.parent = self
        self.usrhistoryobjecttable = RMON2MIB.UsrHistoryObjectTable()
        self.usrhistoryobjecttable.parent = self
        self.usrhistorytable = RMON2MIB.UsrHistoryTable()
        self.usrhistorytable.parent = self


    class AddressMap(object):
        """
        
        
        .. attribute:: addressmapdeletes
        
        	The number of times an address mapping entry has been deleted from the addressMapTable (for any reason).  If an entry is deleted, then inserted, and then deleted, this counter will be incremented by 2.  Note that the table size can be determined by subtracting addressMapDeletes from addressMapInserts
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: addressmapinserts
        
        	The number of times an address mapping entry has been inserted into the addressMapTable.  If an entry is inserted, then deleted, and then inserted, this counter will be incremented by 2.  Note that the table size can be determined by subtracting addressMapDeletes from addressMapInserts
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: addressmapmaxdesiredentries
        
        	The maximum number of entries that are desired in the addressMapTable. The probe will not create more than this number of entries in the table, but may choose to create fewer entries in this table for any reason including the lack of resources.  If this object is set to a value less than the current number of entries, enough entries are chosen in an implementation\-dependent manner and deleted so that the number of entries in the table equals the value of this object.  If this value is set to \-1, the probe may create any number of entries in this table.  This object may be used to control how resources are allocated on the probe for the various RMON functions
        	**type**\: int
        
        	**range:** \-1..2147483647
        
        

        """

        _prefix = 'rmon2-mib'
        _revision = '1996-05-27'

        def __init__(self):
            self.parent = None
            self.addressmapdeletes = None
            self.addressmapinserts = None
            self.addressmapmaxdesiredentries = None

        @property
        def _common_path(self):

            return '/RMON2-MIB:RMON2-MIB/RMON2-MIB:addressMap'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.addressmapdeletes is not None:
                return True

            if self.addressmapinserts is not None:
                return True

            if self.addressmapmaxdesiredentries is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.rmon2._meta import _RMON2_MIB as meta
            return meta._meta_table['RMON2MIB.AddressMap']['meta_info']


    class AddressMapControlTable(object):
        """
        A table to control the collection of network layer address to
        physical address to interface mappings.
        
        Note that this is not like the typical RMON
        controlTable and dataTable in which each entry creates
        its own data table.  Each entry in this table enables the
        discovery of addresses on a new interface and the placement
        of address mappings into the central addressMapTable.
        
        Implementations are encouraged to add an entry per monitored
        interface upon initialization so that a default collection
        of address mappings is available.
        
        .. attribute:: addressmapcontrolentry
        
        	A conceptual row in the addressMapControlTable.      An example of the indexing of this entry is addressMapControlDroppedFrames.1
        	**type**\: list of :py:class:`AddressMapControlEntry <ydk.models.rmon2.RMON2_MIB.RMON2MIB.AddressMapControlTable.AddressMapControlEntry>`
        
        

        """

        _prefix = 'rmon2-mib'
        _revision = '1996-05-27'

        def __init__(self):
            self.parent = None
            self.addressmapcontrolentry = YList()
            self.addressmapcontrolentry.parent = self
            self.addressmapcontrolentry.name = 'addressmapcontrolentry'


        class AddressMapControlEntry(object):
            """
            A conceptual row in the addressMapControlTable.
            
            
            
            
            
            An example of the indexing of this entry is
            addressMapControlDroppedFrames.1
            
            .. attribute:: addressmapcontrolindex
            
            	A unique index for this entry in the addressMapControlTable
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: addressmapcontroldatasource
            
            	The source of data for this addressMapControlEntry
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: addressmapcontroldroppedframes
            
            	The total number of frames which were received by the probe and therefore not accounted for in the \*StatsDropEvents, but for which the probe chose not to count for this entry for whatever reason.  Most often, this event occurs when the probe is out of some resources and decides to shed load from this collection.  This count does not include packets that were not counted because they had MAC\-layer errors.  Note that, unlike the dropEvents counter, this number is the exact number of frames dropped
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: addressmapcontrolowner
            
            	The entity that configured this entry and is therefore using the resources assigned to it
            	**type**\: str
            
            	**range:** 0..127
            
            .. attribute:: addressmapcontrolstatus
            
            	The status of this addressMap control entry.  An entry may not exist in the active state unless all objects in the entry have an appropriate value.  If this object is not equal to active(1), all associated entries in the addressMapTable shall be deleted
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            

            """

            _prefix = 'rmon2-mib'
            _revision = '1996-05-27'

            def __init__(self):
                self.parent = None
                self.addressmapcontrolindex = None
                self.addressmapcontroldatasource = None
                self.addressmapcontroldroppedframes = None
                self.addressmapcontrolowner = None
                self.addressmapcontrolstatus = None

            @property
            def _common_path(self):
                if self.addressmapcontrolindex is None:
                    raise YPYDataValidationError('Key property addressmapcontrolindex is None')

                return '/RMON2-MIB:RMON2-MIB/RMON2-MIB:addressMapControlTable/RMON2-MIB:addressMapControlEntry[RMON2-MIB:addressMapControlIndex = ' + str(self.addressmapcontrolindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.addressmapcontrolindex is not None:
                    return True

                if self.addressmapcontroldatasource is not None:
                    return True

                if self.addressmapcontroldroppedframes is not None:
                    return True

                if self.addressmapcontrolowner is not None:
                    return True

                if self.addressmapcontrolstatus is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.rmon2._meta import _RMON2_MIB as meta
                return meta._meta_table['RMON2MIB.AddressMapControlTable.AddressMapControlEntry']['meta_info']

        @property
        def _common_path(self):

            return '/RMON2-MIB:RMON2-MIB/RMON2-MIB:addressMapControlTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.addressmapcontrolentry is not None:
                for child_ref in self.addressmapcontrolentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.rmon2._meta import _RMON2_MIB as meta
            return meta._meta_table['RMON2MIB.AddressMapControlTable']['meta_info']


    class AddressMapTable(object):
        """
        A table of network layer address to physical address to
        interface mappings.
        
        The probe will add entries to this table based on the source
        MAC and network addresses seen in packets without MAC\-level
        errors. The probe will populate this table for all protocols
        in the protocol directory table whose value of
        protocolDirAddressMapConfig is equal to supportedOn(3), and
        will delete any entries whose protocolDirEntry is deleted or
        has a protocolDirAddressMapConfig value of supportedOff(2).
        
        .. attribute:: addressmapentry
        
        	A conceptual row in the addressMapTable. The protocolDirLocalIndex in the index identifies the network layer protocol of the addressMapNetworkAddress.      An example of the indexing of this entry is addressMapSource.783495.18.4.128.2.6.6.11.1.3.6.1.2.1.2.2.1.1.1
        	**type**\: list of :py:class:`AddressMapEntry <ydk.models.rmon2.RMON2_MIB.RMON2MIB.AddressMapTable.AddressMapEntry>`
        
        

        """

        _prefix = 'rmon2-mib'
        _revision = '1996-05-27'

        def __init__(self):
            self.parent = None
            self.addressmapentry = YList()
            self.addressmapentry.parent = self
            self.addressmapentry.name = 'addressmapentry'


        class AddressMapEntry(object):
            """
            A conceptual row in the addressMapTable.
            The protocolDirLocalIndex in the index identifies the network
            layer protocol of the addressMapNetworkAddress.
            
            
            
            
            
            An example of the indexing of this entry is
            addressMapSource.783495.18.4.128.2.6.6.11.1.3.6.1.2.1.2.2.1.1.1
            
            .. attribute:: addressmapnetworkaddress
            
            	The network address for this relation.  This is represented as an octet string with specific semantics and length as identified by the protocolDirLocalIndex component of the index.  For example, if the protocolDirLocalIndex indicates an encapsulation of ip, this object is encoded as a length octet of 4, followed by the 4 octets of the ip address, in network byte order
            	**type**\: str
            
            .. attribute:: addressmapsource
            
            	The interface or port on which the associated network address was most recently seen.      If this address mapping was discovered on an interface, this object shall identify the instance of the ifIndex object, defined in [3,5], for the desired interface. For example, if an entry were to receive data from interface #1, this object would be set to ifIndex.1.  If this address mapping was discovered on a port, this object shall identify the instance of the rptrGroupPortIndex object, defined in [RFC1516], for the desired port. For example, if an entry were to receive data from group #1, port #1, this object would be set to rptrGroupPortIndex.1.1.  Note that while the dataSource associated with this entry may only point to index objects, this object may at times point to repeater port objects. This situation occurs when the dataSource points to an interface which is a locally attached repeater and the agent has additional information about the source port of traffic seen on that repeater
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: addressmaptimemark
            
            	A TimeFilter for this entry.  See the TimeFilter textual convention to see how this works
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: protocoldirlocalindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: addressmaplastchange
            
            	The value of sysUpTime at the time this entry was last created or the values of the physical address changed.  This can be used to help detect duplicate address problems, in which case this object will be updated frequently
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: addressmapphysicaladdress
            
            	The last source physical address on which the associated network address was seen.  If the protocol of the associated network address was encapsulated inside of a network\-level or higher protocol, this will be the address of the next\-lower protocol with the addressRecognitionCapable bit enabled and will be formatted as specified for that protocol
            	**type**\: str
            
            

            """

            _prefix = 'rmon2-mib'
            _revision = '1996-05-27'

            def __init__(self):
                self.parent = None
                self.addressmapnetworkaddress = None
                self.addressmapsource = None
                self.addressmaptimemark = None
                self.protocoldirlocalindex = None
                self.addressmaplastchange = None
                self.addressmapphysicaladdress = None

            @property
            def _common_path(self):
                if self.addressmapnetworkaddress is None:
                    raise YPYDataValidationError('Key property addressmapnetworkaddress is None')
                if self.addressmapsource is None:
                    raise YPYDataValidationError('Key property addressmapsource is None')
                if self.addressmaptimemark is None:
                    raise YPYDataValidationError('Key property addressmaptimemark is None')
                if self.protocoldirlocalindex is None:
                    raise YPYDataValidationError('Key property protocoldirlocalindex is None')

                return '/RMON2-MIB:RMON2-MIB/RMON2-MIB:addressMapTable/RMON2-MIB:addressMapEntry[RMON2-MIB:addressMapNetworkAddress = ' + str(self.addressmapnetworkaddress) + '][RMON2-MIB:addressMapSource = ' + str(self.addressmapsource) + '][RMON2-MIB:addressMapTimeMark = ' + str(self.addressmaptimemark) + '][RMON2-MIB:protocolDirLocalIndex = ' + str(self.protocoldirlocalindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.addressmapnetworkaddress is not None:
                    return True

                if self.addressmapsource is not None:
                    return True

                if self.addressmaptimemark is not None:
                    return True

                if self.protocoldirlocalindex is not None:
                    return True

                if self.addressmaplastchange is not None:
                    return True

                if self.addressmapphysicaladdress is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.rmon2._meta import _RMON2_MIB as meta
                return meta._meta_table['RMON2MIB.AddressMapTable.AddressMapEntry']['meta_info']

        @property
        def _common_path(self):

            return '/RMON2-MIB:RMON2-MIB/RMON2-MIB:addressMapTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.addressmapentry is not None:
                for child_ref in self.addressmapentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.rmon2._meta import _RMON2_MIB as meta
            return meta._meta_table['RMON2MIB.AddressMapTable']['meta_info']


    class AlHostTable(object):
        """
        A collection of statistics for a particular protocol from a
        particular network address that has been discovered on an
        interface of this device.
        
        The probe will populate this table for all protocols in the
        protocol directory table whose value of
        protocolDirHostConfig is equal to supportedOn(3), and
        will delete any entries whose protocolDirEntry is deleted or
        has a protocolDirHostConfig value of supportedOff(2).
        
        The probe will add to this table all addresses
        seen as the source or destination address in all packets with
        no MAC errors, and will increment octet and packet counts in
        the table for all packets with no MAC errors.  Further,
        entries will only be added to this table if their address
        exists in the nlHostTable and will be deleted from this table
        if their address is deleted from the nlHostTable.
        
        .. attribute:: alhostentry
        
        	A conceptual row in the alHostTable.  The hlHostControlIndex value in the index identifies the hlHostControlEntry on whose behalf this entry was created. The first protocolDirLocalIndex value in the index identifies the network layer protocol of the address. The nlHostAddress value in the index identifies the network layer address of this entry. The second protocolDirLocalIndex value in the index identifies the protocol that is counted by this entry.  An example of the indexing in this entry is alHostOutPkts.1.783495.18.4.128.2.6.6.34
        	**type**\: list of :py:class:`AlHostEntry <ydk.models.rmon2.RMON2_MIB.RMON2MIB.AlHostTable.AlHostEntry>`
        
        

        """

        _prefix = 'rmon2-mib'
        _revision = '1996-05-27'

        def __init__(self):
            self.parent = None
            self.alhostentry = YList()
            self.alhostentry.parent = self
            self.alhostentry.name = 'alhostentry'


        class AlHostEntry(object):
            """
            A conceptual row in the alHostTable.
            
            The hlHostControlIndex value in the index identifies the
            hlHostControlEntry on whose behalf this entry was created.
            The first protocolDirLocalIndex value in the index identifies
            the network layer protocol of the address.
            The nlHostAddress value in the index identifies the network
            layer address of this entry.
            The second protocolDirLocalIndex value in the index identifies
            the protocol that is counted by this entry.
            
            An example of the indexing in this entry is
            alHostOutPkts.1.783495.18.4.128.2.6.6.34
            
            .. attribute:: alhosttimemark
            
            	A TimeFilter for this entry.  See the TimeFilter textual convention to see how this works
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: hlhostcontrolindex
            
            	
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: nlhostaddress
            
            	
            	**type**\: str
            
            .. attribute:: protocoldirlocalindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: protocoldirlocalindex_2
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: alhostcreatetime
            
            	The value of sysUpTime when this entry was last activated. This can be used by the management station to ensure that the entry has not been deleted and recreated between polls
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: alhostinoctets
            
            	The number of octets transmitted to this address of this protocol type since it was added to the alHostTable (excluding framing bits but including      FCS octets), excluding those octets in packets that contained errors.  Note this doesn't count just those octets in the particular protocol frames, but includes the entire packet that contained the protocol
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: alhostinpkts
            
            	The number of packets of this protocol type without errors transmitted to this address since it was added to the alHostTable.  Note that this is the number of link\-layer packets, so if a single network\-layer packet is fragmented into several link\-layer frames, this counter is incremented several times
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: alhostoutoctets
            
            	The number of octets transmitted by this address of this protocol type since it was added to the alHostTable (excluding framing bits but including FCS octets), excluding those octets in packets that contained errors.  Note this doesn't count just those octets in the particular protocol frames, but includes the entire packet that contained the protocol
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: alhostoutpkts
            
            	The number of packets of this protocol type without errors transmitted by this address since it was added to the alHostTable.  Note that this is the number of link\-layer packets, so if a single network\-layer packet is fragmented into several link\-layer frames, this counter is incremented several times
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'rmon2-mib'
            _revision = '1996-05-27'

            def __init__(self):
                self.parent = None
                self.alhosttimemark = None
                self.hlhostcontrolindex = None
                self.nlhostaddress = None
                self.protocoldirlocalindex = None
                self.protocoldirlocalindex_2 = None
                self.alhostcreatetime = None
                self.alhostinoctets = None
                self.alhostinpkts = None
                self.alhostoutoctets = None
                self.alhostoutpkts = None

            @property
            def _common_path(self):
                if self.alhosttimemark is None:
                    raise YPYDataValidationError('Key property alhosttimemark is None')
                if self.hlhostcontrolindex is None:
                    raise YPYDataValidationError('Key property hlhostcontrolindex is None')
                if self.nlhostaddress is None:
                    raise YPYDataValidationError('Key property nlhostaddress is None')
                if self.protocoldirlocalindex is None:
                    raise YPYDataValidationError('Key property protocoldirlocalindex is None')
                if self.protocoldirlocalindex_2 is None:
                    raise YPYDataValidationError('Key property protocoldirlocalindex_2 is None')

                return '/RMON2-MIB:RMON2-MIB/RMON2-MIB:alHostTable/RMON2-MIB:alHostEntry[RMON2-MIB:alHostTimeMark = ' + str(self.alhosttimemark) + '][RMON2-MIB:hlHostControlIndex = ' + str(self.hlhostcontrolindex) + '][RMON2-MIB:nlHostAddress = ' + str(self.nlhostaddress) + '][RMON2-MIB:protocolDirLocalIndex = ' + str(self.protocoldirlocalindex) + '][RMON2-MIB:protocolDirLocalIndex_2 = ' + str(self.protocoldirlocalindex_2) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.alhosttimemark is not None:
                    return True

                if self.hlhostcontrolindex is not None:
                    return True

                if self.nlhostaddress is not None:
                    return True

                if self.protocoldirlocalindex is not None:
                    return True

                if self.protocoldirlocalindex_2 is not None:
                    return True

                if self.alhostcreatetime is not None:
                    return True

                if self.alhostinoctets is not None:
                    return True

                if self.alhostinpkts is not None:
                    return True

                if self.alhostoutoctets is not None:
                    return True

                if self.alhostoutpkts is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.rmon2._meta import _RMON2_MIB as meta
                return meta._meta_table['RMON2MIB.AlHostTable.AlHostEntry']['meta_info']

        @property
        def _common_path(self):

            return '/RMON2-MIB:RMON2-MIB/RMON2-MIB:alHostTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.alhostentry is not None:
                for child_ref in self.alhostentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.rmon2._meta import _RMON2_MIB as meta
            return meta._meta_table['RMON2MIB.AlHostTable']['meta_info']


    class AlMatrixDSTable(object):
        """
        A list of application traffic matrix entries which collect
        statistics for conversations of a particular protocol between
        two network\-level addresses.  This table is indexed first by
        the destination address and then by the source address to make
        it convenient to collect all statistics to a particular
        address.
        
        The probe will populate this table for all protocols in the
        protocol directory table whose value of
        protocolDirMatrixConfig is equal to supportedOn(3), and
        will delete any entries whose protocolDirEntry is deleted or
        has a protocolDirMatrixConfig value of supportedOff(2).
        
        The probe will add to this table all pairs of addresses for
        all protocols seen in all packets with no MAC errors, and will
        increment octet and packet counts in the table for all packets
        with no MAC errors.  Further, entries will only be added to
        this table if their address pair exists in the nlMatrixDSTable
        and will be deleted from this table if the address pair is
        deleted from the nlMatrixDSTable.
        
        .. attribute:: almatrixdsentry
        
        	A conceptual row in the alMatrixDSTable.  The hlMatrixControlIndex value in the index identifies the hlMatrixControlEntry on whose behalf this entry was created. The first protocolDirLocalIndex value in the index identifies the network layer protocol of the alMatrixDSSourceAddress and alMatrixDSDestAddress.      The nlMatrixDSDestAddress value in the index identifies the network layer address of the destination host in this conversation. The nlMatrixDSSourceAddress value in the index identifies the network layer address of the source host in this conversation. The second protocolDirLocalIndex value in the index identifies the protocol that is counted by this entry.  An example of the indexing of this entry is alMatrixDSPkts.1.783495.18.4.128.2.6.7.4.128.2.6.6.34
        	**type**\: list of :py:class:`AlMatrixDSEntry <ydk.models.rmon2.RMON2_MIB.RMON2MIB.AlMatrixDSTable.AlMatrixDSEntry>`
        
        

        """

        _prefix = 'rmon2-mib'
        _revision = '1996-05-27'

        def __init__(self):
            self.parent = None
            self.almatrixdsentry = YList()
            self.almatrixdsentry.parent = self
            self.almatrixdsentry.name = 'almatrixdsentry'


        class AlMatrixDSEntry(object):
            """
            A conceptual row in the alMatrixDSTable.
            
            The hlMatrixControlIndex value in the index identifies the
            hlMatrixControlEntry on whose behalf this entry was created.
            The first protocolDirLocalIndex value in the index identifies
            the network layer protocol of the alMatrixDSSourceAddress and
            alMatrixDSDestAddress.
            
            
            
            
            
            The nlMatrixDSDestAddress value in the index identifies the
            network layer address of the destination host in this
            conversation.
            The nlMatrixDSSourceAddress value in the index identifies the
            network layer address of the source host in this conversation.
            The second protocolDirLocalIndex value in the index identifies
            the protocol that is counted by this entry.
            
            An example of the indexing of this entry is
            alMatrixDSPkts.1.783495.18.4.128.2.6.7.4.128.2.6.6.34
            
            .. attribute:: almatrixdstimemark
            
            	A TimeFilter for this entry.  See the TimeFilter textual convention to see how this works
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: hlmatrixcontrolindex
            
            	
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: nlmatrixdsdestaddress
            
            	
            	**type**\: str
            
            .. attribute:: nlmatrixdssourceaddress
            
            	
            	**type**\: str
            
            .. attribute:: protocoldirlocalindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: protocoldirlocalindex_2
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: almatrixdscreatetime
            
            	The value of sysUpTime when this entry was last activated. This can be used by the management station to ensure that the entry has not been deleted and recreated between polls
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: almatrixdsoctets
            
            	The number of octets in packets of this protocol type transmitted from the source address to the destination address since this entry was added to the alMatrixDSTable (excluding framing bits but including FCS octets), excluding those octets in packets that contained errors.  Note this doesn't count just those octets in the particular protocol frames, but includes the entire packet that contained the protocol
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: almatrixdspkts
            
            	The number of packets of this protocol type without errors transmitted from the source address to the destination address since this entry was added to the alMatrixDSTable.  Note that this is the number of link\-layer packets, so if a single network\-layer packet is fragmented into several link\-layer frames, this counter is incremented several times
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'rmon2-mib'
            _revision = '1996-05-27'

            def __init__(self):
                self.parent = None
                self.almatrixdstimemark = None
                self.hlmatrixcontrolindex = None
                self.nlmatrixdsdestaddress = None
                self.nlmatrixdssourceaddress = None
                self.protocoldirlocalindex = None
                self.protocoldirlocalindex_2 = None
                self.almatrixdscreatetime = None
                self.almatrixdsoctets = None
                self.almatrixdspkts = None

            @property
            def _common_path(self):
                if self.almatrixdstimemark is None:
                    raise YPYDataValidationError('Key property almatrixdstimemark is None')
                if self.hlmatrixcontrolindex is None:
                    raise YPYDataValidationError('Key property hlmatrixcontrolindex is None')
                if self.nlmatrixdsdestaddress is None:
                    raise YPYDataValidationError('Key property nlmatrixdsdestaddress is None')
                if self.nlmatrixdssourceaddress is None:
                    raise YPYDataValidationError('Key property nlmatrixdssourceaddress is None')
                if self.protocoldirlocalindex is None:
                    raise YPYDataValidationError('Key property protocoldirlocalindex is None')
                if self.protocoldirlocalindex_2 is None:
                    raise YPYDataValidationError('Key property protocoldirlocalindex_2 is None')

                return '/RMON2-MIB:RMON2-MIB/RMON2-MIB:alMatrixDSTable/RMON2-MIB:alMatrixDSEntry[RMON2-MIB:alMatrixDSTimeMark = ' + str(self.almatrixdstimemark) + '][RMON2-MIB:hlMatrixControlIndex = ' + str(self.hlmatrixcontrolindex) + '][RMON2-MIB:nlMatrixDSDestAddress = ' + str(self.nlmatrixdsdestaddress) + '][RMON2-MIB:nlMatrixDSSourceAddress = ' + str(self.nlmatrixdssourceaddress) + '][RMON2-MIB:protocolDirLocalIndex = ' + str(self.protocoldirlocalindex) + '][RMON2-MIB:protocolDirLocalIndex_2 = ' + str(self.protocoldirlocalindex_2) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.almatrixdstimemark is not None:
                    return True

                if self.hlmatrixcontrolindex is not None:
                    return True

                if self.nlmatrixdsdestaddress is not None:
                    return True

                if self.nlmatrixdssourceaddress is not None:
                    return True

                if self.protocoldirlocalindex is not None:
                    return True

                if self.protocoldirlocalindex_2 is not None:
                    return True

                if self.almatrixdscreatetime is not None:
                    return True

                if self.almatrixdsoctets is not None:
                    return True

                if self.almatrixdspkts is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.rmon2._meta import _RMON2_MIB as meta
                return meta._meta_table['RMON2MIB.AlMatrixDSTable.AlMatrixDSEntry']['meta_info']

        @property
        def _common_path(self):

            return '/RMON2-MIB:RMON2-MIB/RMON2-MIB:alMatrixDSTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.almatrixdsentry is not None:
                for child_ref in self.almatrixdsentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.rmon2._meta import _RMON2_MIB as meta
            return meta._meta_table['RMON2MIB.AlMatrixDSTable']['meta_info']


    class AlMatrixSDTable(object):
        """
        A list of application traffic matrix entries which collect
        
        
        
        
        
        statistics for conversations of a particular protocol between
        two network\-level addresses.  This table is indexed first by
        the source address and then by the destination address to make
        it convenient to collect all statistics from a particular
        address.
        
        The probe will populate this table for all protocols in the
        protocol directory table whose value of
        protocolDirMatrixConfig is equal to supportedOn(3), and
        will delete any entries whose protocolDirEntry is deleted or
        has a protocolDirMatrixConfig value of supportedOff(2).
        
        The probe will add to this table all pairs of addresses for
        all protocols seen in all packets with no MAC errors, and will
        increment octet and packet counts in the table for all packets
        with no MAC errors.  Further, entries will only be added to
        this table if their address pair exists in the nlMatrixSDTable
        and will be deleted from this table if the address pair is
        deleted from the nlMatrixSDTable.
        
        .. attribute:: almatrixsdentry
        
        	A conceptual row in the alMatrixSDTable.  The hlMatrixControlIndex value in the index identifies the hlMatrixControlEntry on whose behalf this entry was created. The first protocolDirLocalIndex value in the index identifies the network layer protocol of the nlMatrixSDSourceAddress and nlMatrixSDDestAddress. The nlMatrixSDSourceAddress value in the index identifies the network layer address of the source host in this conversation. The nlMatrixSDDestAddress value in the index identifies the network layer address of the destination host in this conversation. The second protocolDirLocalIndex value in the index identifies the protocol that is counted by this entry.  An example of the indexing of this entry is alMatrixSDPkts.1.783495.18.4.128.2.6.6.4.128.2.6.7.34
        	**type**\: list of :py:class:`AlMatrixSDEntry <ydk.models.rmon2.RMON2_MIB.RMON2MIB.AlMatrixSDTable.AlMatrixSDEntry>`
        
        

        """

        _prefix = 'rmon2-mib'
        _revision = '1996-05-27'

        def __init__(self):
            self.parent = None
            self.almatrixsdentry = YList()
            self.almatrixsdentry.parent = self
            self.almatrixsdentry.name = 'almatrixsdentry'


        class AlMatrixSDEntry(object):
            """
            A conceptual row in the alMatrixSDTable.
            
            The hlMatrixControlIndex value in the index identifies the
            hlMatrixControlEntry on whose behalf this entry was created.
            The first protocolDirLocalIndex value in the index identifies
            the network layer protocol of the nlMatrixSDSourceAddress and
            nlMatrixSDDestAddress.
            The nlMatrixSDSourceAddress value in the index identifies the
            network layer address of the source host in this conversation.
            The nlMatrixSDDestAddress value in the index identifies the
            network layer address of the destination host in this
            conversation.
            The second protocolDirLocalIndex value in the index identifies
            the protocol that is counted by this entry.
            
            An example of the indexing of this entry is
            alMatrixSDPkts.1.783495.18.4.128.2.6.6.4.128.2.6.7.34
            
            .. attribute:: almatrixsdtimemark
            
            	A TimeFilter for this entry.  See the TimeFilter textual convention to see how this works
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: hlmatrixcontrolindex
            
            	
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: nlmatrixsddestaddress
            
            	
            	**type**\: str
            
            .. attribute:: nlmatrixsdsourceaddress
            
            	
            	**type**\: str
            
            .. attribute:: protocoldirlocalindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: protocoldirlocalindex_2
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: almatrixsdcreatetime
            
            	The value of sysUpTime when this entry was last activated. This can be used by the management station to ensure that the entry has not been deleted and recreated between polls
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: almatrixsdoctets
            
            	The number of octets in packets of this protocol type transmitted from the source address to the destination address since this entry was added to the alMatrixSDTable (excluding framing bits but including FCS octets), excluding those octets in packets that contained errors.  Note this doesn't count just those octets in the particular protocol frames, but includes the entire packet that contained the protocol
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: almatrixsdpkts
            
            	The number of packets of this protocol type without errors transmitted from the source address to the destination address since this entry was added to the alMatrixSDTable.  Note that this is the number of link\-layer packets, so if a single network\-layer packet is fragmented into several link\-layer frames, this counter is incremented several times
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'rmon2-mib'
            _revision = '1996-05-27'

            def __init__(self):
                self.parent = None
                self.almatrixsdtimemark = None
                self.hlmatrixcontrolindex = None
                self.nlmatrixsddestaddress = None
                self.nlmatrixsdsourceaddress = None
                self.protocoldirlocalindex = None
                self.protocoldirlocalindex_2 = None
                self.almatrixsdcreatetime = None
                self.almatrixsdoctets = None
                self.almatrixsdpkts = None

            @property
            def _common_path(self):
                if self.almatrixsdtimemark is None:
                    raise YPYDataValidationError('Key property almatrixsdtimemark is None')
                if self.hlmatrixcontrolindex is None:
                    raise YPYDataValidationError('Key property hlmatrixcontrolindex is None')
                if self.nlmatrixsddestaddress is None:
                    raise YPYDataValidationError('Key property nlmatrixsddestaddress is None')
                if self.nlmatrixsdsourceaddress is None:
                    raise YPYDataValidationError('Key property nlmatrixsdsourceaddress is None')
                if self.protocoldirlocalindex is None:
                    raise YPYDataValidationError('Key property protocoldirlocalindex is None')
                if self.protocoldirlocalindex_2 is None:
                    raise YPYDataValidationError('Key property protocoldirlocalindex_2 is None')

                return '/RMON2-MIB:RMON2-MIB/RMON2-MIB:alMatrixSDTable/RMON2-MIB:alMatrixSDEntry[RMON2-MIB:alMatrixSDTimeMark = ' + str(self.almatrixsdtimemark) + '][RMON2-MIB:hlMatrixControlIndex = ' + str(self.hlmatrixcontrolindex) + '][RMON2-MIB:nlMatrixSDDestAddress = ' + str(self.nlmatrixsddestaddress) + '][RMON2-MIB:nlMatrixSDSourceAddress = ' + str(self.nlmatrixsdsourceaddress) + '][RMON2-MIB:protocolDirLocalIndex = ' + str(self.protocoldirlocalindex) + '][RMON2-MIB:protocolDirLocalIndex_2 = ' + str(self.protocoldirlocalindex_2) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.almatrixsdtimemark is not None:
                    return True

                if self.hlmatrixcontrolindex is not None:
                    return True

                if self.nlmatrixsddestaddress is not None:
                    return True

                if self.nlmatrixsdsourceaddress is not None:
                    return True

                if self.protocoldirlocalindex is not None:
                    return True

                if self.protocoldirlocalindex_2 is not None:
                    return True

                if self.almatrixsdcreatetime is not None:
                    return True

                if self.almatrixsdoctets is not None:
                    return True

                if self.almatrixsdpkts is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.rmon2._meta import _RMON2_MIB as meta
                return meta._meta_table['RMON2MIB.AlMatrixSDTable.AlMatrixSDEntry']['meta_info']

        @property
        def _common_path(self):

            return '/RMON2-MIB:RMON2-MIB/RMON2-MIB:alMatrixSDTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.almatrixsdentry is not None:
                for child_ref in self.almatrixsdentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.rmon2._meta import _RMON2_MIB as meta
            return meta._meta_table['RMON2MIB.AlMatrixSDTable']['meta_info']


    class AlMatrixTopNControlTable(object):
        """
        A set of parameters that control the creation of a
        report of the top N matrix entries according to
        a selected metric.
        
        .. attribute:: almatrixtopncontrolentry
        
        	A conceptual row in the alMatrixTopNControlTable.  An example of the indexing of this table is alMatrixTopNControlDuration.3
        	**type**\: list of :py:class:`AlMatrixTopNControlEntry <ydk.models.rmon2.RMON2_MIB.RMON2MIB.AlMatrixTopNControlTable.AlMatrixTopNControlEntry>`
        
        

        """

        _prefix = 'rmon2-mib'
        _revision = '1996-05-27'

        def __init__(self):
            self.parent = None
            self.almatrixtopncontrolentry = YList()
            self.almatrixtopncontrolentry.parent = self
            self.almatrixtopncontrolentry.name = 'almatrixtopncontrolentry'


        class AlMatrixTopNControlEntry(object):
            """
            A conceptual row in the alMatrixTopNControlTable.
            
            An example of the indexing of this table is
            alMatrixTopNControlDuration.3
            
            .. attribute:: almatrixtopncontrolindex
            
            	An index that uniquely identifies an entry in the alMatrixTopNControlTable.  Each such entry defines one top N report prepared for one interface
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: almatrixtopncontrolduration
            
            	The number of seconds that this report has collected during the last sampling interval.  When the associated alMatrixTopNControlTimeRemaining object is set, this object shall be set by the probe to the same value and shall not be modified until the next time the alMatrixTopNControlTimeRemaining is set.  This value shall be zero if no reports have been requested for this alMatrixTopNControlEntry
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: almatrixtopncontrolgeneratedreports
            
            	The number of reports that have been generated by this entry
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: almatrixtopncontrolgrantedsize
            
            	The maximum number of matrix entries in this report.  When the associated alMatrixTopNControlRequestedSize object is created or modified, the probe should set this      object as closely to the requested value as is possible for the particular implementation and available resources. The probe must not lower this value except as a result of a set to the associated alMatrixTopNControlRequestedSize object.  If the value of alMatrixTopNControlRateBase is equal to alMatrixTopNTerminalsPkts or alMatrixTopNAllPkts, when the next topN report is generated, matrix entries with the highest value of alMatrixTopNPktRate shall be placed in this table in decreasing order of this rate until there is no more room or until there are no more matrix entries.  If the value of alMatrixTopNControlRateBase is equal to alMatrixTopNTerminalsOctets or alMatrixTopNAllOctets, when the next topN report is generated, matrix entries with the highest value of alMatrixTopNOctetRate shall be placed in this table in decreasing order of this rate until there is no more room or until there are no more matrix entries.  It is an implementation\-specific matter how entries with the same value of alMatrixTopNPktRate or alMatrixTopNOctetRate are sorted.  It is also an implementation\-specific matter as to whether or not zero\-valued entries are available
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: almatrixtopncontrolmatrixindex
            
            	The alMatrix[SD/DS] table for which a top N report will be prepared on behalf of this entry.  The alMatrix[SD/DS] table is identified by the value of the hlMatrixControlIndex for that table \- that value is used here to identify the particular table.  This object may not be modified if the associated alMatrixTopNControlStatus object is equal to active(1)
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: almatrixtopncontrolowner
            
            	The entity that configured this entry and is therefore using the resources assigned to it
            	**type**\: str
            
            	**range:** 0..127
            
            .. attribute:: almatrixtopncontrolratebase
            
            	The variable for each alMatrix[SD/DS] entry that the      alMatrixTopNEntries are sorted by, as well as the selector of the view of the matrix table that will be used.  The values alMatrixTopNTerminalsPkts and alMatrixTopNTerminalsOctets cause collection only from protocols that have no child protocols that are counted.  The values alMatrixTopNAllPkts and alMatrixTopNAllOctets cause collection from all alMatrix entries.  This object may not be modified if the associated alMatrixTopNControlStatus object is equal to active(1)
            	**type**\: :py:class:`AlMatrixTopNControlRateBase_Enum <ydk.models.rmon2.RMON2_MIB.RMON2MIB.AlMatrixTopNControlTable.AlMatrixTopNControlEntry.AlMatrixTopNControlRateBase_Enum>`
            
            .. attribute:: almatrixtopncontrolrequestedsize
            
            	The maximum number of matrix entries requested for this report.  When this object is created or modified, the probe should set alMatrixTopNControlGrantedSize as closely to this object as is possible for the particular probe implementation and available resources
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: almatrixtopncontrolstarttime
            
            	The value of sysUpTime when this top N report was last started.  In other words, this is the time that the associated alMatrixTopNControlTimeRemaining object was modified to start the requested report or the time the report was last automatically (re)started.  This object may be used by the management station to determine if a report was missed or not
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: almatrixtopncontrolstatus
            
            	The status of this alMatrixTopNControlEntry.  An entry may not exist in the active state unless all objects in the entry have an appropriate value.  If this object is not equal to active(1), all associated entries in the alMatrixTopNTable shall be deleted by the agent
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            .. attribute:: almatrixtopncontroltimeremaining
            
            	The number of seconds left in the report currently being collected.  When this object is modified by the management station, a new collection is started, possibly aborting a currently running report.  The new value is used as the requested duration of this report, and is immediately loaded into the associated alMatrixTopNControlDuration object. When the report finishes, the probe will automatically start another collection with the same initial value of alMatrixTopNControlTimeRemaining.  Thus the management station may simply read the resulting reports repeatedly, checking the startTime and duration each time to ensure that a report was not missed or that the report parameters were not changed.  While the value of this object is non\-zero, it decrements by one per second until it reaches zero.  At the time that this object decrements to zero, the report is made accessible in the alMatrixTopNTable, overwriting any report that may be there.  When this object is modified by the management station, any associated entries in the alMatrixTopNTable shall be deleted.  (Note that this is a different algorithm than the one used in the hostTopNTable)
            	**type**\: int
            
            	**range:** 0..2147483647
            
            

            """

            _prefix = 'rmon2-mib'
            _revision = '1996-05-27'

            def __init__(self):
                self.parent = None
                self.almatrixtopncontrolindex = None
                self.almatrixtopncontrolduration = None
                self.almatrixtopncontrolgeneratedreports = None
                self.almatrixtopncontrolgrantedsize = None
                self.almatrixtopncontrolmatrixindex = None
                self.almatrixtopncontrolowner = None
                self.almatrixtopncontrolratebase = None
                self.almatrixtopncontrolrequestedsize = None
                self.almatrixtopncontrolstarttime = None
                self.almatrixtopncontrolstatus = None
                self.almatrixtopncontroltimeremaining = None

            class AlMatrixTopNControlRateBase_Enum(Enum):
                """
                AlMatrixTopNControlRateBase_Enum

                The variable for each alMatrix[SD/DS] entry that the
                
                
                
                
                
                alMatrixTopNEntries are sorted by, as well as the
                selector of the view of the matrix table that will be
                used.
                
                The values alMatrixTopNTerminalsPkts and
                alMatrixTopNTerminalsOctets cause collection only from
                protocols that have no child protocols that are counted.  The
                values alMatrixTopNAllPkts and alMatrixTopNAllOctets cause
                collection from all alMatrix entries.
                
                This object may not be modified if the associated
                alMatrixTopNControlStatus object is equal to active(1).

                """

                ALMATRIXTOPNTERMINALSPKTS = 1

                ALMATRIXTOPNTERMINALSOCTETS = 2

                ALMATRIXTOPNALLPKTS = 3

                ALMATRIXTOPNALLOCTETS = 4


                @staticmethod
                def _meta_info():
                    from ydk.models.rmon2._meta import _RMON2_MIB as meta
                    return meta._meta_table['RMON2MIB.AlMatrixTopNControlTable.AlMatrixTopNControlEntry.AlMatrixTopNControlRateBase_Enum']


            @property
            def _common_path(self):
                if self.almatrixtopncontrolindex is None:
                    raise YPYDataValidationError('Key property almatrixtopncontrolindex is None')

                return '/RMON2-MIB:RMON2-MIB/RMON2-MIB:alMatrixTopNControlTable/RMON2-MIB:alMatrixTopNControlEntry[RMON2-MIB:alMatrixTopNControlIndex = ' + str(self.almatrixtopncontrolindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.almatrixtopncontrolindex is not None:
                    return True

                if self.almatrixtopncontrolduration is not None:
                    return True

                if self.almatrixtopncontrolgeneratedreports is not None:
                    return True

                if self.almatrixtopncontrolgrantedsize is not None:
                    return True

                if self.almatrixtopncontrolmatrixindex is not None:
                    return True

                if self.almatrixtopncontrolowner is not None:
                    return True

                if self.almatrixtopncontrolratebase is not None:
                    return True

                if self.almatrixtopncontrolrequestedsize is not None:
                    return True

                if self.almatrixtopncontrolstarttime is not None:
                    return True

                if self.almatrixtopncontrolstatus is not None:
                    return True

                if self.almatrixtopncontroltimeremaining is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.rmon2._meta import _RMON2_MIB as meta
                return meta._meta_table['RMON2MIB.AlMatrixTopNControlTable.AlMatrixTopNControlEntry']['meta_info']

        @property
        def _common_path(self):

            return '/RMON2-MIB:RMON2-MIB/RMON2-MIB:alMatrixTopNControlTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.almatrixtopncontrolentry is not None:
                for child_ref in self.almatrixtopncontrolentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.rmon2._meta import _RMON2_MIB as meta
            return meta._meta_table['RMON2MIB.AlMatrixTopNControlTable']['meta_info']


    class AlMatrixTopNTable(object):
        """
        A set of statistics for those application layer matrix
        entries that have counted the highest number of octets or
        packets.
        
        .. attribute:: almatrixtopnentry
        
        	A conceptual row in the alMatrixTopNTable.  The alMatrixTopNControlIndex value in the index identifies the alMatrixTopNControlEntry on whose behalf this entry was created.  An example of the indexing of this table is alMatrixTopNPktRate.3.10
        	**type**\: list of :py:class:`AlMatrixTopNEntry <ydk.models.rmon2.RMON2_MIB.RMON2MIB.AlMatrixTopNTable.AlMatrixTopNEntry>`
        
        

        """

        _prefix = 'rmon2-mib'
        _revision = '1996-05-27'

        def __init__(self):
            self.parent = None
            self.almatrixtopnentry = YList()
            self.almatrixtopnentry.parent = self
            self.almatrixtopnentry.name = 'almatrixtopnentry'


        class AlMatrixTopNEntry(object):
            """
            A conceptual row in the alMatrixTopNTable.
            
            The alMatrixTopNControlIndex value in the index identifies
            the alMatrixTopNControlEntry on whose behalf this entry was
            created.
            
            An example of the indexing of this table is
            alMatrixTopNPktRate.3.10
            
            .. attribute:: almatrixtopncontrolindex
            
            	
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: almatrixtopnindex
            
            	An index that uniquely identifies an entry in the alMatrixTopNTable among those in the same report. This index is between 1 and N, where N is the number of entries in this report.  If the value of alMatrixTopNControlRateBase is equal to alMatrixTopNTerminalsPkts or alMatrixTopNAllPkts, increasing values of alMatrixTopNIndex shall be assigned to entries with decreasing values of alMatrixTopNPktRate until index N is assigned or there are no more alMatrixTopNEntries.  If the value of alMatrixTopNControlRateBase is equal to alMatrixTopNTerminalsOctets or alMatrixTopNAllOctets, increasing values of alMatrixTopNIndex shall be assigned to entries with decreasing values of alMatrixTopNOctetRate until index N is assigned or there are no more alMatrixTopNEntries
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: almatrixtopnappprotocoldirlocalindex
            
            	The type of the protocol counted by this matrix entry
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: almatrixtopndestaddress
            
            	The network layer address of the destination host in this conversation.  This is represented as an octet string with specific semantics and length as identified by the associated alMatrixTopNProtocolDirLocalIndex.  For example, if the alMatrixTopNProtocolDirLocalIndex indicates an encapsulation of ip, this object is encoded as a length octet of 4, followed by the 4 octets of the ip address, in network byte order
            	**type**\: str
            
            .. attribute:: almatrixtopnoctetrate
            
            	The number of octets seen of this protocol from the source host to the destination host during this sampling interval, counted using the rules for counting the alMatrixSDOctets object.  If the value of alMatrixTopNControlRateBase is alMatrixTopNTerminalsOctets or alMatrixTopNAllOctets, this variable will be used to sort this report
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: almatrixtopnpktrate
            
            	The number of packets seen of this protocol from the source host to the destination host during this sampling interval, counted using the rules for counting the alMatrixSDPkts object.  If the value of alMatrixTopNControlRateBase is alMatrixTopNTerminalsPkts or alMatrixTopNAllPkts, this variable will be used to sort this report
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: almatrixtopnprotocoldirlocalindex
            
            	The protocolDirLocalIndex of the network layer protocol of this entry's network address
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: almatrixtopnreverseoctetrate
            
            	The number of octets seen of this protocol from the destination host to the source host during this sampling interval, counted using the rules for counting the alMatrixDSOctets object  (note that the corresponding alMatrixSDOctets object selected is the one whose source address is equal to alMatrixTopNDestAddress and whose destination address is equal to alMatrixTopNSourceAddress.)  Note that if the value of alMatrixTopNControlRateBase is equal      to alMatrixTopNTerminalsOctets or alMatrixTopNAllOctets, the sort of topN entries is based entirely on alMatrixTopNOctetRate, and not on the value of this object
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: almatrixtopnreversepktrate
            
            	The number of packets seen of this protocol from the destination host to the source host during this sampling interval, counted using the rules for counting the alMatrixDSPkts object  (note that the corresponding alMatrixSDPkts object selected is the one whose source address is equal to alMatrixTopNDestAddress and whose destination address is equal to alMatrixTopNSourceAddress.)  Note that if the value of alMatrixTopNControlRateBase is equal to alMatrixTopNTerminalsPkts or alMatrixTopNAllPkts, the sort of topN entries is based entirely on alMatrixTopNPktRate, and not on the value of this object
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: almatrixtopnsourceaddress
            
            	The network layer address of the source host in this conversation. This is represented as an octet string with specific semantics and length as identified      by the associated alMatrixTopNProtocolDirLocalIndex.  For example, if the alMatrixTopNProtocolDirLocalIndex indicates an encapsulation of ip, this object is encoded as a length octet of 4, followed by the 4 octets of the ip address, in network byte order
            	**type**\: str
            
            

            """

            _prefix = 'rmon2-mib'
            _revision = '1996-05-27'

            def __init__(self):
                self.parent = None
                self.almatrixtopncontrolindex = None
                self.almatrixtopnindex = None
                self.almatrixtopnappprotocoldirlocalindex = None
                self.almatrixtopndestaddress = None
                self.almatrixtopnoctetrate = None
                self.almatrixtopnpktrate = None
                self.almatrixtopnprotocoldirlocalindex = None
                self.almatrixtopnreverseoctetrate = None
                self.almatrixtopnreversepktrate = None
                self.almatrixtopnsourceaddress = None

            @property
            def _common_path(self):
                if self.almatrixtopncontrolindex is None:
                    raise YPYDataValidationError('Key property almatrixtopncontrolindex is None')
                if self.almatrixtopnindex is None:
                    raise YPYDataValidationError('Key property almatrixtopnindex is None')

                return '/RMON2-MIB:RMON2-MIB/RMON2-MIB:alMatrixTopNTable/RMON2-MIB:alMatrixTopNEntry[RMON2-MIB:alMatrixTopNControlIndex = ' + str(self.almatrixtopncontrolindex) + '][RMON2-MIB:alMatrixTopNIndex = ' + str(self.almatrixtopnindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.almatrixtopncontrolindex is not None:
                    return True

                if self.almatrixtopnindex is not None:
                    return True

                if self.almatrixtopnappprotocoldirlocalindex is not None:
                    return True

                if self.almatrixtopndestaddress is not None:
                    return True

                if self.almatrixtopnoctetrate is not None:
                    return True

                if self.almatrixtopnpktrate is not None:
                    return True

                if self.almatrixtopnprotocoldirlocalindex is not None:
                    return True

                if self.almatrixtopnreverseoctetrate is not None:
                    return True

                if self.almatrixtopnreversepktrate is not None:
                    return True

                if self.almatrixtopnsourceaddress is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.rmon2._meta import _RMON2_MIB as meta
                return meta._meta_table['RMON2MIB.AlMatrixTopNTable.AlMatrixTopNEntry']['meta_info']

        @property
        def _common_path(self):

            return '/RMON2-MIB:RMON2-MIB/RMON2-MIB:alMatrixTopNTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.almatrixtopnentry is not None:
                for child_ref in self.almatrixtopnentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.rmon2._meta import _RMON2_MIB as meta
            return meta._meta_table['RMON2MIB.AlMatrixTopNTable']['meta_info']


    class HlHostControlTable(object):
        """
        A list of higher layer (i.e. non\-MAC) host table control entries.
        
        These entries will enable the collection of the network and
        application level host tables indexed by network addresses.
        Both the network and application level host tables are
        controlled by this table is so that they will both be created
        and deleted at the same time, further increasing the ease with
        which they can be implemented as a single datastore (note that
        if an implementation stores application layer host records in
        memory, it can derive network layer host records from them).
        
        Entries in the nlHostTable will be created on behalf of each
        entry in this table. Additionally, if this probe implements
        the alHostTable, entries in the alHostTable will be created on
        behalf of each entry in this table.
        
        Implementations are encouraged to add an entry per monitored
        interface upon initialization so that a default collection
        of host statistics is available.
        
        .. attribute:: hlhostcontrolentry
        
        	A conceptual row in the hlHostControlTable.  An example of the indexing of this entry is hlHostControlNlDroppedFrames.1
        	**type**\: list of :py:class:`HlHostControlEntry <ydk.models.rmon2.RMON2_MIB.RMON2MIB.HlHostControlTable.HlHostControlEntry>`
        
        

        """

        _prefix = 'rmon2-mib'
        _revision = '1996-05-27'

        def __init__(self):
            self.parent = None
            self.hlhostcontrolentry = YList()
            self.hlhostcontrolentry.parent = self
            self.hlhostcontrolentry.name = 'hlhostcontrolentry'


        class HlHostControlEntry(object):
            """
            A conceptual row in the hlHostControlTable.
            
            An example of the indexing of this entry is
            hlHostControlNlDroppedFrames.1
            
            .. attribute:: hlhostcontrolindex
            
            	An index that uniquely identifies an entry in the hlHostControlTable.  Each such entry defines a function that discovers hosts on a particular interface and places statistics about them in the nlHostTable, and optionally in the alHostTable, on behalf of this hlHostControlEntry
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: hlhostcontrolaldeletes
            
            	The number of times an alHost entry has been deleted from the alHost table (for any reason).  If an entry is deleted, then inserted, and then deleted, this counter will be incremented by 2.  To allow for efficient implementation strategies, agents may delay updating this object for short periods of time.  For example, an implementation strategy may allow internal data structures to differ from those visible via SNMP for short periods of time.  This counter may reflect the internal data structures for those short periods of time.  Note that the table size can be determined by subtracting hlHostControlAlDeletes from hlHostControlAlInserts
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: hlhostcontrolaldroppedframes
            
            	The total number of frames which were received by the probe and therefore not accounted for in the \*StatsDropEvents, but for which the probe chose not to count for the associated alHost entries for whatever reason.  Most often, this event occurs when the probe is out of some resources and decides to shed load from this collection.  This count does not include packets that were not counted because they had MAC\-layer errors.       Note that if the alHostTable is not implemented or is inactive because no protocols are enabled in the protocol directory, this value should be 0.  Note that, unlike the dropEvents counter, this number is the exact number of frames dropped
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: hlhostcontrolalinserts
            
            	The number of times an alHost entry has been inserted into the alHost table.  If an entry is inserted, then deleted, and then inserted, this counter will be incremented by 2.  To allow for efficient implementation strategies, agents may delay updating this object for short periods of time.  For example, an implementation strategy may allow internal data structures to differ from those visible via SNMP for short periods of time.  This counter may reflect the internal data structures for those short periods of time.  Note that the table size can be determined by subtracting hlHostControlAlDeletes from hlHostControlAlInserts
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: hlhostcontrolalmaxdesiredentries
            
            	The maximum number of entries that are desired in the alHost table on behalf of this control entry. The probe will not create more than this number of associated entries in the table, but may choose to create fewer entries in this table for any reason including the lack of resources.  If this object is set to a value less than the current number of entries, enough entries are chosen in an implementation\-dependent manner and deleted so that the number of entries in the table equals the value of this object.  If this value is set to \-1, the probe may create any number of entries in this table.  If the associated hlHostControlStatus object is equal to `active', this object may not be modified.  This object may be used to control how resources are allocated on the probe for the various RMON functions
            	**type**\: int
            
            	**range:** \-1..2147483647
            
            .. attribute:: hlhostcontroldatasource
            
            	The source of data for the associated host tables.  The statistics in this group reflect all packets on the local network segment attached to the identified interface.  This object may not be modified if the associated hlHostControlStatus object is equal to active(1)
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: hlhostcontrolnldeletes
            
            	The number of times an nlHost entry has been deleted from the nlHost table (for any reason).  If an entry is deleted, then inserted, and then deleted, this counter will be incremented by 2.  To allow for efficient implementation strategies, agents may delay updating this object for short periods of time.  For example, an implementation strategy may allow internal      data structures to differ from those visible via SNMP for short periods of time.  This counter may reflect the internal data structures for those short periods of time.  Note that the table size can be determined by subtracting hlHostControlNlDeletes from hlHostControlNlInserts
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: hlhostcontrolnldroppedframes
            
            	The total number of frames which were received by the probe and therefore not accounted for in the \*StatsDropEvents, but for which the probe chose not to count for the associated      nlHost entries for whatever reason.  Most often, this event occurs when the probe is out of some resources and decides to shed load from this collection.  This count does not include packets that were not counted because they had MAC\-layer errors.  Note that if the nlHostTable is inactive because no protocols are enabled in the protocol directory, this value should be 0.  Note that, unlike the dropEvents counter, this number is the exact number of frames dropped
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: hlhostcontrolnlinserts
            
            	The number of times an nlHost entry has been inserted into the nlHost table.  If an entry is inserted, then deleted, and then inserted, this counter will be incremented by 2.  To allow for efficient implementation strategies, agents may delay updating this object for short periods of time.  For example, an implementation strategy may allow internal data structures to differ from those visible via SNMP for short periods of time.  This counter may reflect the internal data structures for those short periods of time.  Note that the table size can be determined by subtracting hlHostControlNlDeletes from hlHostControlNlInserts
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: hlhostcontrolnlmaxdesiredentries
            
            	The maximum number of entries that are desired in the nlHostTable on behalf of this control entry. The probe will not create more than this number of associated entries in the table, but may choose to create fewer entries in this table for any reason including the lack of resources.  If this object is set to a value less than the current number of entries, enough entries are chosen in an implementation\-dependent manner and deleted so that the number of entries in the table equals the value of this object.  If this value is set to \-1, the probe may create any number of entries in this table.  If the associated hlHostControlStatus object is equal to `active', this object may not be modified.  This object may be used to control how resources are allocated on the probe for the various RMON functions
            	**type**\: int
            
            	**range:** \-1..2147483647
            
            .. attribute:: hlhostcontrolowner
            
            	The entity that configured this entry and is therefore using the resources assigned to it
            	**type**\: str
            
            	**range:** 0..127
            
            .. attribute:: hlhostcontrolstatus
            
            	The status of this hlHostControlEntry.  An entry may not exist in the active state unless all objects in the entry have an appropriate value.  If this object is not equal to active(1), all associated entries in the nlHostTable and alHostTable shall be deleted
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            

            """

            _prefix = 'rmon2-mib'
            _revision = '1996-05-27'

            def __init__(self):
                self.parent = None
                self.hlhostcontrolindex = None
                self.hlhostcontrolaldeletes = None
                self.hlhostcontrolaldroppedframes = None
                self.hlhostcontrolalinserts = None
                self.hlhostcontrolalmaxdesiredentries = None
                self.hlhostcontroldatasource = None
                self.hlhostcontrolnldeletes = None
                self.hlhostcontrolnldroppedframes = None
                self.hlhostcontrolnlinserts = None
                self.hlhostcontrolnlmaxdesiredentries = None
                self.hlhostcontrolowner = None
                self.hlhostcontrolstatus = None

            @property
            def _common_path(self):
                if self.hlhostcontrolindex is None:
                    raise YPYDataValidationError('Key property hlhostcontrolindex is None')

                return '/RMON2-MIB:RMON2-MIB/RMON2-MIB:hlHostControlTable/RMON2-MIB:hlHostControlEntry[RMON2-MIB:hlHostControlIndex = ' + str(self.hlhostcontrolindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.hlhostcontrolindex is not None:
                    return True

                if self.hlhostcontrolaldeletes is not None:
                    return True

                if self.hlhostcontrolaldroppedframes is not None:
                    return True

                if self.hlhostcontrolalinserts is not None:
                    return True

                if self.hlhostcontrolalmaxdesiredentries is not None:
                    return True

                if self.hlhostcontroldatasource is not None:
                    return True

                if self.hlhostcontrolnldeletes is not None:
                    return True

                if self.hlhostcontrolnldroppedframes is not None:
                    return True

                if self.hlhostcontrolnlinserts is not None:
                    return True

                if self.hlhostcontrolnlmaxdesiredentries is not None:
                    return True

                if self.hlhostcontrolowner is not None:
                    return True

                if self.hlhostcontrolstatus is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.rmon2._meta import _RMON2_MIB as meta
                return meta._meta_table['RMON2MIB.HlHostControlTable.HlHostControlEntry']['meta_info']

        @property
        def _common_path(self):

            return '/RMON2-MIB:RMON2-MIB/RMON2-MIB:hlHostControlTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.hlhostcontrolentry is not None:
                for child_ref in self.hlhostcontrolentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.rmon2._meta import _RMON2_MIB as meta
            return meta._meta_table['RMON2MIB.HlHostControlTable']['meta_info']


    class HlMatrixControlTable(object):
        """
        A list of higher layer (i.e. non\-MAC) matrix control entries.
        
        These entries will enable the collection of the network and
        application level matrix tables containing conversation
        statistics indexed by pairs of network addresses.
        Both the network and application level matrix tables are
        controlled by this table is so that they will both be created
        and deleted at the same time, further increasing the ease with
        which they can be implemented as a single datastore (note that
        if an implementation stores application layer matrix records
        in memory, it can derive network layer matrix records from
        them).
        
        Entries in the nlMatrixSDTable and nlMatrixDSTable will be
        created on behalf of each entry in this table.  Additionally,
        if this probe implements the alMatrix tables, entries in the
        alMatrix tables will be created on behalf of each entry in
        this table.
        
        .. attribute:: hlmatrixcontrolentry
        
        	A conceptual row in the hlMatrixControlTable.  An example of indexing of this entry is hlMatrixControlNlDroppedFrames.1
        	**type**\: list of :py:class:`HlMatrixControlEntry <ydk.models.rmon2.RMON2_MIB.RMON2MIB.HlMatrixControlTable.HlMatrixControlEntry>`
        
        

        """

        _prefix = 'rmon2-mib'
        _revision = '1996-05-27'

        def __init__(self):
            self.parent = None
            self.hlmatrixcontrolentry = YList()
            self.hlmatrixcontrolentry.parent = self
            self.hlmatrixcontrolentry.name = 'hlmatrixcontrolentry'


        class HlMatrixControlEntry(object):
            """
            A conceptual row in the hlMatrixControlTable.
            
            An example of indexing of this entry is
            hlMatrixControlNlDroppedFrames.1
            
            .. attribute:: hlmatrixcontrolindex
            
            	An index that uniquely identifies an entry in the hlMatrixControlTable.  Each such entry defines a function that discovers conversations on a particular interface and places statistics about them in the nlMatrixSDTable and the nlMatrixDSTable, and optionally the alMatrixSDTable and alMatrixDSTable, on behalf of this hlMatrixControlEntry
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: hlmatrixcontrolaldeletes
            
            	The number of times an alMatrix entry has been deleted from the alMatrix tables.  If an entry is deleted, then inserted, and then deleted, this counter will be incremented by 2.  The deletion of a conversation from both the alMatrixSDTable and alMatrixDSTable shall be counted as two deletions (even though every deletion from one table must be accompanied by a deletion from the other).  To allow for efficient implementation strategies, agents may delay updating this object for short periods of time.  For example, an implementation strategy may allow internal data structures to differ from those visible via SNMP for short periods of time.  This counter may reflect the internal data structures for those short periods of time.  Note that the table size can be determined by subtracting hlMatrixControlAlDeletes from hlMatrixControlAlInserts
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: hlmatrixcontrolaldroppedframes
            
            	The total number of frames which were received by the probe and therefore not accounted for in the \*StatsDropEvents, but for which the probe chose not to count for this entry for whatever reason.  Most often, this event occurs when the probe is out of some resources and decides to shed load from this collection.  This count does not include packets that were not counted because they had MAC\-layer errors.  Note that if the alMatrixTables are not implemented or are inactive because no protocols are enabled in the protocol directory, this value should be 0.  Note that, unlike the dropEvents counter, this number is the exact number of frames dropped
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: hlmatrixcontrolalinserts
            
            	The number of times an alMatrix entry has been inserted into the alMatrix tables.  If an entry is inserted, then deleted, and then inserted, this counter will be incremented by 2.  The addition of a conversation into both the alMatrixSDTable and alMatrixDSTable shall be counted as two insertions (even though every addition into one table must be accompanied by an insertion into the other).  To allow for efficient implementation strategies, agents may delay updating this object for short periods of time.  For example, an implementation strategy may allow internal data structures to differ from those visible via SNMP for short periods of time.  This counter may reflect the internal      data structures for those short periods of time.  Note that the table size can be determined by subtracting hlMatrixControlAlDeletes from hlMatrixControlAlInserts
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: hlmatrixcontrolalmaxdesiredentries
            
            	The maximum number of entries that are desired in the alMatrix tables on behalf of this control entry. The probe will not create more than this number of associated entries in the table, but may choose to create fewer entries in this table for any reason including the lack of resources.  If this object is set to a value less than the current number of entries, enough entries are chosen in an implementation\-dependent manner and deleted so that the number of entries in the table equals the value of this object.  If this value is set to \-1, the probe may create any number of entries in this table.  If the associated      hlMatrixControlStatus object is equal to `active', this object may not be modified.  This object may be used to control how resources are allocated on the probe for the various RMON functions
            	**type**\: int
            
            	**range:** \-1..2147483647
            
            .. attribute:: hlmatrixcontroldatasource
            
            	The source of the data for the associated matrix tables.  The statistics in this group reflect all packets on the local network segment attached to the      identified interface.  This object may not be modified if the associated hlMatrixControlStatus object is equal to active(1)
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: hlmatrixcontrolnldeletes
            
            	The number of times an nlMatrix entry has been deleted from the nlMatrix tables (for any reason).  If an entry is deleted, then inserted, and then deleted, this counter will be incremented by 2.  The deletion of a conversation from both the nlMatrixSDTable and nlMatrixDSTable shall be counted as two deletions (even though every deletion from one table must be accompanied by a deletion from the other).  To allow for efficient implementation strategies, agents may delay updating this object for short periods of time.  For example, an implementation strategy may allow internal data structures to differ from those visible via SNMP for short periods of time.  This counter may reflect the internal data structures for those short periods of time.  Note that the table size can be determined by subtracting hlMatrixControlNlDeletes from hlMatrixControlNlInserts
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: hlmatrixcontrolnldroppedframes
            
            	The total number of frames which were received by the probe and therefore not accounted for in the \*StatsDropEvents, but for which the probe chose not to count for this entry for whatever reason.  Most often, this event occurs when the probe is out of some resources and decides to shed load from this collection.  This count does not include packets that were not counted because they had MAC\-layer errors.  Note that if the nlMatrixTables are inactive because no protocols are enabled in the protocol directory, this value should be 0.  Note that, unlike the dropEvents counter, this number is the exact number of frames dropped
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: hlmatrixcontrolnlinserts
            
            	The number of times an nlMatrix entry has been inserted into the nlMatrix tables.  If an entry is inserted, then deleted, and then inserted, this counter will be incremented by 2.  The addition of a conversation into both the nlMatrixSDTable and nlMatrixDSTable shall be counted as two insertions (even though every addition into one table must be accompanied by an insertion into the other).  To allow for efficient implementation strategies, agents may delay updating this object for short periods of time.  For example, an implementation strategy may allow internal data structures to differ from those visible via SNMP for short periods of time.  This counter may reflect the internal data structures for those short periods of time.      Note that the sum of then nlMatrixSDTable and nlMatrixDSTable sizes can be determined by subtracting hlMatrixControlNlDeletes from hlMatrixControlNlInserts
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: hlmatrixcontrolnlmaxdesiredentries
            
            	The maximum number of entries that are desired in the nlMatrix tables on behalf of this control entry. The probe will not create more than this number of associated entries in the table, but may choose to create fewer entries in this table for any reason including the lack of resources.  If this object is set to a value less than the current number of entries, enough entries are chosen in an implementation\-dependent manner and deleted so that the number of entries in the table equals the value of this object.  If this value is set to \-1, the probe may create any number of entries in this table.  If the associated      hlMatrixControlStatus object is equal to `active', this object may not be modified.  This object may be used to control how resources are allocated on the probe for the various RMON functions
            	**type**\: int
            
            	**range:** \-1..2147483647
            
            .. attribute:: hlmatrixcontrolowner
            
            	The entity that configured this entry and is therefore using the resources assigned to it
            	**type**\: str
            
            	**range:** 0..127
            
            .. attribute:: hlmatrixcontrolstatus
            
            	The status of this hlMatrixControlEntry.  An entry may not exist in the active state unless all objects in the entry have an appropriate value.  If this object is not equal to active(1), all associated entries in the nlMatrixSDTable, nlMatrixDSTable, alMatrixSDTable, and the alMatrixDSTable shall be deleted by the agent
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            

            """

            _prefix = 'rmon2-mib'
            _revision = '1996-05-27'

            def __init__(self):
                self.parent = None
                self.hlmatrixcontrolindex = None
                self.hlmatrixcontrolaldeletes = None
                self.hlmatrixcontrolaldroppedframes = None
                self.hlmatrixcontrolalinserts = None
                self.hlmatrixcontrolalmaxdesiredentries = None
                self.hlmatrixcontroldatasource = None
                self.hlmatrixcontrolnldeletes = None
                self.hlmatrixcontrolnldroppedframes = None
                self.hlmatrixcontrolnlinserts = None
                self.hlmatrixcontrolnlmaxdesiredentries = None
                self.hlmatrixcontrolowner = None
                self.hlmatrixcontrolstatus = None

            @property
            def _common_path(self):
                if self.hlmatrixcontrolindex is None:
                    raise YPYDataValidationError('Key property hlmatrixcontrolindex is None')

                return '/RMON2-MIB:RMON2-MIB/RMON2-MIB:hlMatrixControlTable/RMON2-MIB:hlMatrixControlEntry[RMON2-MIB:hlMatrixControlIndex = ' + str(self.hlmatrixcontrolindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.hlmatrixcontrolindex is not None:
                    return True

                if self.hlmatrixcontrolaldeletes is not None:
                    return True

                if self.hlmatrixcontrolaldroppedframes is not None:
                    return True

                if self.hlmatrixcontrolalinserts is not None:
                    return True

                if self.hlmatrixcontrolalmaxdesiredentries is not None:
                    return True

                if self.hlmatrixcontroldatasource is not None:
                    return True

                if self.hlmatrixcontrolnldeletes is not None:
                    return True

                if self.hlmatrixcontrolnldroppedframes is not None:
                    return True

                if self.hlmatrixcontrolnlinserts is not None:
                    return True

                if self.hlmatrixcontrolnlmaxdesiredentries is not None:
                    return True

                if self.hlmatrixcontrolowner is not None:
                    return True

                if self.hlmatrixcontrolstatus is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.rmon2._meta import _RMON2_MIB as meta
                return meta._meta_table['RMON2MIB.HlMatrixControlTable.HlMatrixControlEntry']['meta_info']

        @property
        def _common_path(self):

            return '/RMON2-MIB:RMON2-MIB/RMON2-MIB:hlMatrixControlTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.hlmatrixcontrolentry is not None:
                for child_ref in self.hlmatrixcontrolentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.rmon2._meta import _RMON2_MIB as meta
            return meta._meta_table['RMON2MIB.HlMatrixControlTable']['meta_info']


    class NetConfigTable(object):
        """
        A table of netConfigEntries.
        
        .. attribute:: netconfigentry
        
        	A set of configuration parameters for a particular network interface on this device. If the device has no network interface, this table is empty.  The index is composed of the ifIndex assigned to the corresponding interface
        	**type**\: list of :py:class:`NetConfigEntry <ydk.models.rmon2.RMON2_MIB.RMON2MIB.NetConfigTable.NetConfigEntry>`
        
        

        """

        _prefix = 'rmon2-mib'
        _revision = '1996-05-27'

        def __init__(self):
            self.parent = None
            self.netconfigentry = YList()
            self.netconfigentry.parent = self
            self.netconfigentry.name = 'netconfigentry'


        class NetConfigEntry(object):
            """
            A set of configuration parameters for a particular
            network interface on this device. If the device has no network
            interface, this table is empty.
            
            The index is composed of the ifIndex assigned to the
            corresponding interface.
            
            .. attribute:: ifindex
            
            	
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: netconfigipaddress
            
            	The IP address of this Net interface.  The default value for this object is 0.0.0.0.  If either the netConfigIPAddress or netConfigSubnetMask are 0.0.0.0, then when the device boots, it may use BOOTP to try to figure out what these values should be. If BOOTP fails, before the device can talk on the network, this value must be configured (e.g., through a terminal attached to the device). If BOOTP is      used, care should be taken to not send BOOTP broadcasts too frequently and to eventually send very infrequently if no replies are received
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: netconfigstatus
            
            	The status of this netConfigEntry.  An entry may not exist in the active state unless all objects in the entry have an appropriate value
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            .. attribute:: netconfigsubnetmask
            
            	The subnet mask of this Net interface.  The default value for this object is 0.0.0.0.  If either the netConfigIPAddress or netConfigSubnetMask are 0.0.0.0, then when the device boots, it may use BOOTP to try to figure out what these values should be. If BOOTP fails, before the device can talk on the network, this value must be configured (e.g., through a terminal attached to the device). If BOOTP is used, care should be taken to not send BOOTP broadcasts too frequently and to eventually send very infrequently if no replies are received
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            

            """

            _prefix = 'rmon2-mib'
            _revision = '1996-05-27'

            def __init__(self):
                self.parent = None
                self.ifindex = None
                self.netconfigipaddress = None
                self.netconfigstatus = None
                self.netconfigsubnetmask = None

            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYDataValidationError('Key property ifindex is None')

                return '/RMON2-MIB:RMON2-MIB/RMON2-MIB:netConfigTable/RMON2-MIB:netConfigEntry[RMON2-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ifindex is not None:
                    return True

                if self.netconfigipaddress is not None:
                    return True

                if self.netconfigstatus is not None:
                    return True

                if self.netconfigsubnetmask is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.rmon2._meta import _RMON2_MIB as meta
                return meta._meta_table['RMON2MIB.NetConfigTable.NetConfigEntry']['meta_info']

        @property
        def _common_path(self):

            return '/RMON2-MIB:RMON2-MIB/RMON2-MIB:netConfigTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.netconfigentry is not None:
                for child_ref in self.netconfigentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.rmon2._meta import _RMON2_MIB as meta
            return meta._meta_table['RMON2MIB.NetConfigTable']['meta_info']


    class NlHostTable(object):
        """
        A collection of statistics for a particular network layer
        address that has been discovered on an interface of this
        device.
        
        The probe will populate this table for all network layer
        protocols in the protocol directory table whose value of
        protocolDirHostConfig is equal to supportedOn(3), and
        will delete any entries whose protocolDirEntry is deleted or
        has a protocolDirHostConfig value of supportedOff(2).
        
        The probe will add to this table all addresses seen
        as the source or destination address in all packets with no
        MAC errors, and will increment octet and packet counts in the
        table for all packets with no MAC errors.
        
        .. attribute:: nlhostentry
        
        	A conceptual row in the nlHostTable.  The hlHostControlIndex value in the index identifies the hlHostControlEntry on whose behalf this entry was created. The protocolDirLocalIndex value in the index identifies the network layer protocol of the nlHostAddress.  An example of the indexing of this entry is nlHostOutPkts.1.783495.18.4.128.2.6.6
        	**type**\: list of :py:class:`NlHostEntry <ydk.models.rmon2.RMON2_MIB.RMON2MIB.NlHostTable.NlHostEntry>`
        
        

        """

        _prefix = 'rmon2-mib'
        _revision = '1996-05-27'

        def __init__(self):
            self.parent = None
            self.nlhostentry = YList()
            self.nlhostentry.parent = self
            self.nlhostentry.name = 'nlhostentry'


        class NlHostEntry(object):
            """
            A conceptual row in the nlHostTable.
            
            The hlHostControlIndex value in the index identifies the
            hlHostControlEntry on whose behalf this entry was created.
            The protocolDirLocalIndex value in the index identifies the
            network layer protocol of the nlHostAddress.
            
            An example of the indexing of this entry is
            nlHostOutPkts.1.783495.18.4.128.2.6.6.
            
            .. attribute:: hlhostcontrolindex
            
            	
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: nlhostaddress
            
            	The network address for this nlHostEntry.  This is represented as an octet string with specific semantics and length as identified by the protocolDirLocalIndex component of the index.  For example, if the protocolDirLocalIndex indicates an encapsulation of ip, this object is encoded as a length octet of 4, followed by the 4 octets of the ip address, in network byte order
            	**type**\: str
            
            .. attribute:: nlhosttimemark
            
            	A TimeFilter for this entry.  See the TimeFilter textual convention to see how this works
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: protocoldirlocalindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: nlhostcreatetime
            
            	The value of sysUpTime when this entry was last activated. This can be used by the management station to ensure that the entry has not been deleted and recreated between polls
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nlhostinoctets
            
            	The number of octets transmitted to this address since it was added to the nlHostTable (excluding framing bits but including FCS octets), excluding those octets in packets that contained errors.  Note this doesn't count just those octets in the particular protocol frames, but includes the entire packet that contained the protocol
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nlhostinpkts
            
            	The number of packets without errors transmitted to this address since it was added to the nlHostTable.  Note that this is the number of link\-layer packets, so if a single network\-layer packet is fragmented into several link\-layer frames, this counter is incremented several times
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nlhostoutmacnonunicastpkts
            
            	The number of packets without errors transmitted by this address that were directed to any MAC broadcast addresses or to any MAC multicast addresses since this host was added to the nlHostTable. Note that this is the number of link\-layer packets, so if a single network\-layer packet is fragmented into several link\-layer frames, this counter is incremented several times
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nlhostoutoctets
            
            	The number of octets transmitted by this address since it was added to the nlHostTable (excluding framing bits but including FCS octets), excluding those octets in packets that contained errors.  Note this doesn't count just those octets in the particular protocol frames, but includes the entire packet that contained the protocol
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nlhostoutpkts
            
            	The number of packets without errors transmitted by      this address since it was added to the nlHostTable.  Note that this is the number of link\-layer packets, so if a single network\-layer packet is fragmented into several link\-layer frames, this counter is incremented several times
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'rmon2-mib'
            _revision = '1996-05-27'

            def __init__(self):
                self.parent = None
                self.hlhostcontrolindex = None
                self.nlhostaddress = None
                self.nlhosttimemark = None
                self.protocoldirlocalindex = None
                self.nlhostcreatetime = None
                self.nlhostinoctets = None
                self.nlhostinpkts = None
                self.nlhostoutmacnonunicastpkts = None
                self.nlhostoutoctets = None
                self.nlhostoutpkts = None

            @property
            def _common_path(self):
                if self.hlhostcontrolindex is None:
                    raise YPYDataValidationError('Key property hlhostcontrolindex is None')
                if self.nlhostaddress is None:
                    raise YPYDataValidationError('Key property nlhostaddress is None')
                if self.nlhosttimemark is None:
                    raise YPYDataValidationError('Key property nlhosttimemark is None')
                if self.protocoldirlocalindex is None:
                    raise YPYDataValidationError('Key property protocoldirlocalindex is None')

                return '/RMON2-MIB:RMON2-MIB/RMON2-MIB:nlHostTable/RMON2-MIB:nlHostEntry[RMON2-MIB:hlHostControlIndex = ' + str(self.hlhostcontrolindex) + '][RMON2-MIB:nlHostAddress = ' + str(self.nlhostaddress) + '][RMON2-MIB:nlHostTimeMark = ' + str(self.nlhosttimemark) + '][RMON2-MIB:protocolDirLocalIndex = ' + str(self.protocoldirlocalindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.hlhostcontrolindex is not None:
                    return True

                if self.nlhostaddress is not None:
                    return True

                if self.nlhosttimemark is not None:
                    return True

                if self.protocoldirlocalindex is not None:
                    return True

                if self.nlhostcreatetime is not None:
                    return True

                if self.nlhostinoctets is not None:
                    return True

                if self.nlhostinpkts is not None:
                    return True

                if self.nlhostoutmacnonunicastpkts is not None:
                    return True

                if self.nlhostoutoctets is not None:
                    return True

                if self.nlhostoutpkts is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.rmon2._meta import _RMON2_MIB as meta
                return meta._meta_table['RMON2MIB.NlHostTable.NlHostEntry']['meta_info']

        @property
        def _common_path(self):

            return '/RMON2-MIB:RMON2-MIB/RMON2-MIB:nlHostTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.nlhostentry is not None:
                for child_ref in self.nlhostentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.rmon2._meta import _RMON2_MIB as meta
            return meta._meta_table['RMON2MIB.NlHostTable']['meta_info']


    class NlMatrixDSTable(object):
        """
        A list of traffic matrix entries which collect statistics for
        conversations between two network\-level addresses.  This table
        is indexed first by the destination address and then by the
        source address to make it convenient to collect all
        conversations to a particular address.
        
        The probe will populate this table for all network layer
        protocols in the protocol directory table whose value of
        protocolDirMatrixConfig is equal to supportedOn(3), and
        will delete any entries whose protocolDirEntry is deleted or
        has a protocolDirMatrixConfig value of supportedOff(2).
        
        The probe will add to this table all pairs of addresses
        seen in all packets with no MAC errors, and will increment
        
        
        
        
        
        octet and packet counts in the table for all packets with no
        MAC errors.
        
        Further, this table will only contain entries that have a
        corresponding entry in the nlMatrixSDTable with the same
        source address and destination address.
        
        .. attribute:: nlmatrixdsentry
        
        	A conceptual row in the nlMatrixDSTable.  The hlMatrixControlIndex value in the index identifies the hlMatrixControlEntry on whose behalf this entry was created. The protocolDirLocalIndex value in the index identifies the network layer protocol of the nlMatrixDSSourceAddress and nlMatrixDSDestAddress.  An example of the indexing of this table is nlMatrixDSPkts.1.783495.18.4.128.2.6.7.4.128.2.6.6
        	**type**\: list of :py:class:`NlMatrixDSEntry <ydk.models.rmon2.RMON2_MIB.RMON2MIB.NlMatrixDSTable.NlMatrixDSEntry>`
        
        

        """

        _prefix = 'rmon2-mib'
        _revision = '1996-05-27'

        def __init__(self):
            self.parent = None
            self.nlmatrixdsentry = YList()
            self.nlmatrixdsentry.parent = self
            self.nlmatrixdsentry.name = 'nlmatrixdsentry'


        class NlMatrixDSEntry(object):
            """
            A conceptual row in the nlMatrixDSTable.
            
            The hlMatrixControlIndex value in the index identifies the
            hlMatrixControlEntry on whose behalf this entry was created.
            The protocolDirLocalIndex value in the index identifies the
            network layer protocol of the nlMatrixDSSourceAddress and
            nlMatrixDSDestAddress.
            
            An example of the indexing of this table is
            nlMatrixDSPkts.1.783495.18.4.128.2.6.7.4.128.2.6.6
            
            .. attribute:: hlmatrixcontrolindex
            
            	
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: nlmatrixdsdestaddress
            
            	The network destination address for this nlMatrixDSEntry.  This is represented as an octet string with specific semantics and length as identified by the protocolDirLocalIndex component of the index.  For example, if the protocolDirLocalIndex indicates an encapsulation of ip, this object is encoded as a length octet of 4, followed by the 4 octets of the ip address, in network byte order
            	**type**\: str
            
            .. attribute:: nlmatrixdssourceaddress
            
            	The network source address for this nlMatrixDSEntry.  This is represented as an octet string with specific semantics and length as identified by the protocolDirLocalIndex component of the index.  For example, if the protocolDirLocalIndex indicates an encapsulation of ip, this object is encoded as a length octet of 4, followed by the 4 octets of the ip address, in network byte order
            	**type**\: str
            
            .. attribute:: nlmatrixdstimemark
            
            	A TimeFilter for this entry.  See the TimeFilter textual convention to see how this works
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: protocoldirlocalindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: nlmatrixdscreatetime
            
            	The value of sysUpTime when this entry was last activated. This can be used by the management station to ensure that the entry has not been deleted and recreated between polls
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nlmatrixdsoctets
            
            	The number of octets transmitted from the source address to the destination address since this entry was added to the nlMatrixDSTable (excluding framing bits but including FCS octets), excluding those octets in packets that contained errors.  Note this doesn't count just those octets in the particular protocol frames, but includes the entire packet that contained the protocol
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nlmatrixdspkts
            
            	The number of packets without errors transmitted from the source address to the destination address since this entry was added to the nlMatrixDSTable.  Note that this is the number of link\-layer packets, so if a single network\-layer packet is fragmented into several link\-layer frames, this counter is incremented several times
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'rmon2-mib'
            _revision = '1996-05-27'

            def __init__(self):
                self.parent = None
                self.hlmatrixcontrolindex = None
                self.nlmatrixdsdestaddress = None
                self.nlmatrixdssourceaddress = None
                self.nlmatrixdstimemark = None
                self.protocoldirlocalindex = None
                self.nlmatrixdscreatetime = None
                self.nlmatrixdsoctets = None
                self.nlmatrixdspkts = None

            @property
            def _common_path(self):
                if self.hlmatrixcontrolindex is None:
                    raise YPYDataValidationError('Key property hlmatrixcontrolindex is None')
                if self.nlmatrixdsdestaddress is None:
                    raise YPYDataValidationError('Key property nlmatrixdsdestaddress is None')
                if self.nlmatrixdssourceaddress is None:
                    raise YPYDataValidationError('Key property nlmatrixdssourceaddress is None')
                if self.nlmatrixdstimemark is None:
                    raise YPYDataValidationError('Key property nlmatrixdstimemark is None')
                if self.protocoldirlocalindex is None:
                    raise YPYDataValidationError('Key property protocoldirlocalindex is None')

                return '/RMON2-MIB:RMON2-MIB/RMON2-MIB:nlMatrixDSTable/RMON2-MIB:nlMatrixDSEntry[RMON2-MIB:hlMatrixControlIndex = ' + str(self.hlmatrixcontrolindex) + '][RMON2-MIB:nlMatrixDSDestAddress = ' + str(self.nlmatrixdsdestaddress) + '][RMON2-MIB:nlMatrixDSSourceAddress = ' + str(self.nlmatrixdssourceaddress) + '][RMON2-MIB:nlMatrixDSTimeMark = ' + str(self.nlmatrixdstimemark) + '][RMON2-MIB:protocolDirLocalIndex = ' + str(self.protocoldirlocalindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.hlmatrixcontrolindex is not None:
                    return True

                if self.nlmatrixdsdestaddress is not None:
                    return True

                if self.nlmatrixdssourceaddress is not None:
                    return True

                if self.nlmatrixdstimemark is not None:
                    return True

                if self.protocoldirlocalindex is not None:
                    return True

                if self.nlmatrixdscreatetime is not None:
                    return True

                if self.nlmatrixdsoctets is not None:
                    return True

                if self.nlmatrixdspkts is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.rmon2._meta import _RMON2_MIB as meta
                return meta._meta_table['RMON2MIB.NlMatrixDSTable.NlMatrixDSEntry']['meta_info']

        @property
        def _common_path(self):

            return '/RMON2-MIB:RMON2-MIB/RMON2-MIB:nlMatrixDSTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.nlmatrixdsentry is not None:
                for child_ref in self.nlmatrixdsentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.rmon2._meta import _RMON2_MIB as meta
            return meta._meta_table['RMON2MIB.NlMatrixDSTable']['meta_info']


    class NlMatrixSDTable(object):
        """
        A list of traffic matrix entries which collect statistics for
        conversations between two network\-level addresses.  This table
        is indexed first by the source address and then by the
        destination address to make it convenient to collect all
        conversations from a particular address.
        
        The probe will populate this table for all network layer
        protocols in the protocol directory table whose value of
        protocolDirMatrixConfig is equal to supportedOn(3), and
        will delete any entries whose protocolDirEntry is deleted or
        has a protocolDirMatrixConfig value of supportedOff(2).
        
        
        
        
        
        The probe will add to this table all pairs of addresses
        seen in all packets with no MAC errors, and will increment
        octet and packet counts in the table for all packets with no
        MAC errors.
        
        Further, this table will only contain entries that have a
        corresponding entry in the nlMatrixDSTable with the same
        source address and destination address.
        
        .. attribute:: nlmatrixsdentry
        
        	A conceptual row in the nlMatrixSDTable.  The hlMatrixControlIndex value in the index identifies the hlMatrixControlEntry on whose behalf this entry was created. The protocolDirLocalIndex value in the index identifies the network layer protocol of the nlMatrixSDSourceAddress and nlMatrixSDDestAddress.  An example of the indexing of this table is nlMatrixSDPkts.1.783495.18.4.128.2.6.6.4.128.2.6.7
        	**type**\: list of :py:class:`NlMatrixSDEntry <ydk.models.rmon2.RMON2_MIB.RMON2MIB.NlMatrixSDTable.NlMatrixSDEntry>`
        
        

        """

        _prefix = 'rmon2-mib'
        _revision = '1996-05-27'

        def __init__(self):
            self.parent = None
            self.nlmatrixsdentry = YList()
            self.nlmatrixsdentry.parent = self
            self.nlmatrixsdentry.name = 'nlmatrixsdentry'


        class NlMatrixSDEntry(object):
            """
            A conceptual row in the nlMatrixSDTable.
            
            The hlMatrixControlIndex value in the index identifies the
            hlMatrixControlEntry on whose behalf this entry was created.
            The protocolDirLocalIndex value in the index identifies the
            network layer protocol of the nlMatrixSDSourceAddress and
            nlMatrixSDDestAddress.
            
            An example of the indexing of this table is
            nlMatrixSDPkts.1.783495.18.4.128.2.6.6.4.128.2.6.7
            
            .. attribute:: hlmatrixcontrolindex
            
            	
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: nlmatrixsddestaddress
            
            	The network destination address for this nlMatrixSDEntry.  This is represented as an octet string with specific semantics and length as identified by the protocolDirLocalIndex component of the index.  For example, if the protocolDirLocalIndex indicates an encapsulation of ip, this object is encoded as a length octet of 4, followed by the 4 octets of the ip address, in network byte order
            	**type**\: str
            
            .. attribute:: nlmatrixsdsourceaddress
            
            	The network source address for this nlMatrixSDEntry.  This is represented as an octet string with specific semantics and length as identified by the protocolDirLocalIndex component of the index.  For example, if the protocolDirLocalIndex indicates an encapsulation of ip, this object is encoded as a length octet of 4, followed by the 4 octets of the ip address, in network byte order
            	**type**\: str
            
            .. attribute:: nlmatrixsdtimemark
            
            	A TimeFilter for this entry.  See the TimeFilter textual convention to see how this works
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: protocoldirlocalindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: nlmatrixsdcreatetime
            
            	The value of sysUpTime when this entry was last activated. This can be used by the management station to ensure that the entry has not been deleted and recreated between polls
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nlmatrixsdoctets
            
            	The number of octets transmitted from the source address to the destination address since this entry was added to the nlMatrixSDTable (excluding framing bits but including FCS octets), excluding those octets in packets that contained errors.  Note this doesn't count just those octets in the particular protocol frames, but includes the entire packet that contained the protocol
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nlmatrixsdpkts
            
            	The number of packets without errors transmitted from the source address to the destination address since this entry was added to the nlMatrixSDTable.  Note that this is the number of link\-layer packets, so if a single network\-layer packet is fragmented into several link\-layer frames, this counter is incremented several times
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'rmon2-mib'
            _revision = '1996-05-27'

            def __init__(self):
                self.parent = None
                self.hlmatrixcontrolindex = None
                self.nlmatrixsddestaddress = None
                self.nlmatrixsdsourceaddress = None
                self.nlmatrixsdtimemark = None
                self.protocoldirlocalindex = None
                self.nlmatrixsdcreatetime = None
                self.nlmatrixsdoctets = None
                self.nlmatrixsdpkts = None

            @property
            def _common_path(self):
                if self.hlmatrixcontrolindex is None:
                    raise YPYDataValidationError('Key property hlmatrixcontrolindex is None')
                if self.nlmatrixsddestaddress is None:
                    raise YPYDataValidationError('Key property nlmatrixsddestaddress is None')
                if self.nlmatrixsdsourceaddress is None:
                    raise YPYDataValidationError('Key property nlmatrixsdsourceaddress is None')
                if self.nlmatrixsdtimemark is None:
                    raise YPYDataValidationError('Key property nlmatrixsdtimemark is None')
                if self.protocoldirlocalindex is None:
                    raise YPYDataValidationError('Key property protocoldirlocalindex is None')

                return '/RMON2-MIB:RMON2-MIB/RMON2-MIB:nlMatrixSDTable/RMON2-MIB:nlMatrixSDEntry[RMON2-MIB:hlMatrixControlIndex = ' + str(self.hlmatrixcontrolindex) + '][RMON2-MIB:nlMatrixSDDestAddress = ' + str(self.nlmatrixsddestaddress) + '][RMON2-MIB:nlMatrixSDSourceAddress = ' + str(self.nlmatrixsdsourceaddress) + '][RMON2-MIB:nlMatrixSDTimeMark = ' + str(self.nlmatrixsdtimemark) + '][RMON2-MIB:protocolDirLocalIndex = ' + str(self.protocoldirlocalindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.hlmatrixcontrolindex is not None:
                    return True

                if self.nlmatrixsddestaddress is not None:
                    return True

                if self.nlmatrixsdsourceaddress is not None:
                    return True

                if self.nlmatrixsdtimemark is not None:
                    return True

                if self.protocoldirlocalindex is not None:
                    return True

                if self.nlmatrixsdcreatetime is not None:
                    return True

                if self.nlmatrixsdoctets is not None:
                    return True

                if self.nlmatrixsdpkts is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.rmon2._meta import _RMON2_MIB as meta
                return meta._meta_table['RMON2MIB.NlMatrixSDTable.NlMatrixSDEntry']['meta_info']

        @property
        def _common_path(self):

            return '/RMON2-MIB:RMON2-MIB/RMON2-MIB:nlMatrixSDTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.nlmatrixsdentry is not None:
                for child_ref in self.nlmatrixsdentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.rmon2._meta import _RMON2_MIB as meta
            return meta._meta_table['RMON2MIB.NlMatrixSDTable']['meta_info']


    class NlMatrixTopNControlTable(object):
        """
        A set of parameters that control the creation of a
        report of the top N matrix entries according to
        a selected metric.
        
        .. attribute:: nlmatrixtopncontrolentry
        
        	A conceptual row in the nlMatrixTopNControlTable.  An example of the indexing of this table is nlMatrixTopNControlDuration.3
        	**type**\: list of :py:class:`NlMatrixTopNControlEntry <ydk.models.rmon2.RMON2_MIB.RMON2MIB.NlMatrixTopNControlTable.NlMatrixTopNControlEntry>`
        
        

        """

        _prefix = 'rmon2-mib'
        _revision = '1996-05-27'

        def __init__(self):
            self.parent = None
            self.nlmatrixtopncontrolentry = YList()
            self.nlmatrixtopncontrolentry.parent = self
            self.nlmatrixtopncontrolentry.name = 'nlmatrixtopncontrolentry'


        class NlMatrixTopNControlEntry(object):
            """
            A conceptual row in the nlMatrixTopNControlTable.
            
            An example of the indexing of this table is
            nlMatrixTopNControlDuration.3
            
            .. attribute:: nlmatrixtopncontrolindex
            
            	An index that uniquely identifies an entry in the nlMatrixTopNControlTable.  Each such entry defines one top N report prepared for one interface
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: nlmatrixtopncontrolduration
            
            	The number of seconds that this report has collected during the last sampling interval.  When the associated nlMatrixTopNControlTimeRemaining object is set, this object shall be set by the probe to the same value and shall not be modified until the next time the nlMatrixTopNControlTimeRemaining is set. This value shall be zero if no reports have been requested for this nlMatrixTopNControlEntry
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: nlmatrixtopncontrolgeneratedreports
            
            	The number of reports that have been generated by this entry
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nlmatrixtopncontrolgrantedsize
            
            	The maximum number of matrix entries in this report.  When the associated nlMatrixTopNControlRequestedSize object is created or modified, the probe should set this object as closely to the requested value as is possible for the particular implementation and available resources. The probe must not lower this value except as a result of a set to the associated nlMatrixTopNControlRequestedSize object.  If the value of nlMatrixTopNControlRateBase is equal to nlMatrixTopNPkts, when the next topN report is generated, matrix entries with the highest value of nlMatrixTopNPktRate shall be placed in this table in decreasing order of this rate until there is no more room or until there are no more      matrix entries.  If the value of nlMatrixTopNControlRateBase is equal to nlMatrixTopNOctets, when the next topN report is generated, matrix entries with the highest value of nlMatrixTopNOctetRate shall be placed in this table in decreasing order of this rate until there is no more room or until there are no more matrix entries.  It is an implementation\-specific matter how entries with the same value of nlMatrixTopNPktRate or nlMatrixTopNOctetRate are sorted.  It is also an implementation\-specific matter as to whether or not zero\-valued entries are available
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: nlmatrixtopncontrolmatrixindex
            
            	The nlMatrix[SD/DS] table for which a top N report will be prepared on behalf of this entry.  The nlMatrix[SD/DS] table is identified by the value of the hlMatrixControlIndex for that table \- that value is used here to identify the particular table.  This object may not be modified if the associated nlMatrixTopNControlStatus object is equal to active(1)
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: nlmatrixtopncontrolowner
            
            	The entity that configured this entry and is therefore using the resources assigned to it
            	**type**\: str
            
            	**range:** 0..127
            
            .. attribute:: nlmatrixtopncontrolratebase
            
            	The variable for each nlMatrix[SD/DS] entry that the nlMatrixTopNEntries are sorted by.      This object may not be modified if the associated nlMatrixTopNControlStatus object is equal to active(1)
            	**type**\: :py:class:`NlMatrixTopNControlRateBase_Enum <ydk.models.rmon2.RMON2_MIB.RMON2MIB.NlMatrixTopNControlTable.NlMatrixTopNControlEntry.NlMatrixTopNControlRateBase_Enum>`
            
            .. attribute:: nlmatrixtopncontrolrequestedsize
            
            	The maximum number of matrix entries requested for this report.  When this object is created or modified, the probe should set nlMatrixTopNControlGrantedSize as closely to this object as is possible for the particular probe implementation and available resources
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: nlmatrixtopncontrolstarttime
            
            	The value of sysUpTime when this top N report was last started.  In other words, this is the time that the associated nlMatrixTopNControlTimeRemaining object was modified to start the requested report or the time the report was last automatically (re)started.  This object may be used by the management station to determine if a report was missed or not
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nlmatrixtopncontrolstatus
            
            	The status of this nlMatrixTopNControlEntry.  An entry may not exist in the active state unless all objects in the entry have an appropriate value.      If this object is not equal to active(1), all associated entries in the nlMatrixTopNTable shall be deleted by the agent
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            .. attribute:: nlmatrixtopncontroltimeremaining
            
            	The number of seconds left in the report currently being collected.  When this object is modified by the management station, a new collection is started, possibly aborting a currently running report.  The new value is used as the requested duration of this report, and is immediately loaded into the associated nlMatrixTopNControlDuration object. When the report finishes, the probe will automatically start another collection with the same initial value of nlMatrixTopNControlTimeRemaining.  Thus the management station may simply read the resulting reports repeatedly, checking the startTime and duration each time to ensure that a report was not missed or that the report parameters were not changed.  While the value of this object is non\-zero, it decrements by one per second until it reaches zero.  At the time that this object decrements to zero, the report is made accessible in the nlMatrixTopNTable, overwriting any report that may be there.  When this object is modified by the management station, any associated entries in the nlMatrixTopNTable shall be deleted.  (Note that this is a different algorithm than the one used in the hostTopNTable)
            	**type**\: int
            
            	**range:** 0..2147483647
            
            

            """

            _prefix = 'rmon2-mib'
            _revision = '1996-05-27'

            def __init__(self):
                self.parent = None
                self.nlmatrixtopncontrolindex = None
                self.nlmatrixtopncontrolduration = None
                self.nlmatrixtopncontrolgeneratedreports = None
                self.nlmatrixtopncontrolgrantedsize = None
                self.nlmatrixtopncontrolmatrixindex = None
                self.nlmatrixtopncontrolowner = None
                self.nlmatrixtopncontrolratebase = None
                self.nlmatrixtopncontrolrequestedsize = None
                self.nlmatrixtopncontrolstarttime = None
                self.nlmatrixtopncontrolstatus = None
                self.nlmatrixtopncontroltimeremaining = None

            class NlMatrixTopNControlRateBase_Enum(Enum):
                """
                NlMatrixTopNControlRateBase_Enum

                The variable for each nlMatrix[SD/DS] entry that the
                nlMatrixTopNEntries are sorted by.
                
                
                
                
                
                This object may not be modified if the associated
                nlMatrixTopNControlStatus object is equal to active(1).

                """

                NLMATRIXTOPNPKTS = 1

                NLMATRIXTOPNOCTETS = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.rmon2._meta import _RMON2_MIB as meta
                    return meta._meta_table['RMON2MIB.NlMatrixTopNControlTable.NlMatrixTopNControlEntry.NlMatrixTopNControlRateBase_Enum']


            @property
            def _common_path(self):
                if self.nlmatrixtopncontrolindex is None:
                    raise YPYDataValidationError('Key property nlmatrixtopncontrolindex is None')

                return '/RMON2-MIB:RMON2-MIB/RMON2-MIB:nlMatrixTopNControlTable/RMON2-MIB:nlMatrixTopNControlEntry[RMON2-MIB:nlMatrixTopNControlIndex = ' + str(self.nlmatrixtopncontrolindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.nlmatrixtopncontrolindex is not None:
                    return True

                if self.nlmatrixtopncontrolduration is not None:
                    return True

                if self.nlmatrixtopncontrolgeneratedreports is not None:
                    return True

                if self.nlmatrixtopncontrolgrantedsize is not None:
                    return True

                if self.nlmatrixtopncontrolmatrixindex is not None:
                    return True

                if self.nlmatrixtopncontrolowner is not None:
                    return True

                if self.nlmatrixtopncontrolratebase is not None:
                    return True

                if self.nlmatrixtopncontrolrequestedsize is not None:
                    return True

                if self.nlmatrixtopncontrolstarttime is not None:
                    return True

                if self.nlmatrixtopncontrolstatus is not None:
                    return True

                if self.nlmatrixtopncontroltimeremaining is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.rmon2._meta import _RMON2_MIB as meta
                return meta._meta_table['RMON2MIB.NlMatrixTopNControlTable.NlMatrixTopNControlEntry']['meta_info']

        @property
        def _common_path(self):

            return '/RMON2-MIB:RMON2-MIB/RMON2-MIB:nlMatrixTopNControlTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.nlmatrixtopncontrolentry is not None:
                for child_ref in self.nlmatrixtopncontrolentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.rmon2._meta import _RMON2_MIB as meta
            return meta._meta_table['RMON2MIB.NlMatrixTopNControlTable']['meta_info']


    class NlMatrixTopNTable(object):
        """
        A set of statistics for those network layer matrix entries
        that have counted the highest number of octets or packets.
        
        .. attribute:: nlmatrixtopnentry
        
        	A conceptual row in the nlMatrixTopNTable.  The nlMatrixTopNControlIndex value in the index identifies the nlMatrixTopNControlEntry on whose behalf this entry was created.  An example of the indexing of this table is nlMatrixTopNPktRate.3.10
        	**type**\: list of :py:class:`NlMatrixTopNEntry <ydk.models.rmon2.RMON2_MIB.RMON2MIB.NlMatrixTopNTable.NlMatrixTopNEntry>`
        
        

        """

        _prefix = 'rmon2-mib'
        _revision = '1996-05-27'

        def __init__(self):
            self.parent = None
            self.nlmatrixtopnentry = YList()
            self.nlmatrixtopnentry.parent = self
            self.nlmatrixtopnentry.name = 'nlmatrixtopnentry'


        class NlMatrixTopNEntry(object):
            """
            A conceptual row in the nlMatrixTopNTable.
            
            The nlMatrixTopNControlIndex value in the index identifies the
            nlMatrixTopNControlEntry on whose behalf this entry was
            created.
            
            An example of the indexing of this table is
            nlMatrixTopNPktRate.3.10
            
            .. attribute:: nlmatrixtopncontrolindex
            
            	
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: nlmatrixtopnindex
            
            	An index that uniquely identifies an entry in the nlMatrixTopNTable among those in the same report.      This index is between 1 and N, where N is the number of entries in this report.  If the value of nlMatrixTopNControlRateBase is equal to nlMatrixTopNPkts, increasing values of nlMatrixTopNIndex shall be assigned to entries with decreasing values of nlMatrixTopNPktRate until index N is assigned or there are no more nlMatrixTopNEntries.  If the value of nlMatrixTopNControlRateBase is equal to nlMatrixTopNOctets, increasing values of nlMatrixTopNIndex shall be assigned to entries with decreasing values of nlMatrixTopNOctetRate until index N is assigned or there are no more nlMatrixTopNEntries
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: nlmatrixtopndestaddress
            
            	The network layer address of the destination host in this conversation.  This is represented as an octet string with specific semantics and length as identified by the associated nlMatrixTopNProtocolDirLocalIndex.  For example, if the nlMatrixTopNProtocolDirLocalIndex indicates an encapsulation of ip, this object is encoded as a length octet of 4, followed by the 4 octets of the ip address, in network byte order
            	**type**\: str
            
            .. attribute:: nlmatrixtopnoctetrate
            
            	The number of octets seen from the source host to the destination host during this sampling interval, counted using the rules for counting the nlMatrixSDOctets object.  If the value of nlMatrixTopNControlRateBase is nlMatrixTopNOctets, this variable will be used to sort this report
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nlmatrixtopnpktrate
            
            	The number of packets seen from the source host to the destination host during this sampling interval, counted using the rules for counting the nlMatrixSDPkts object. If the value of nlMatrixTopNControlRateBase is nlMatrixTopNPkts, this variable will be used to sort this report
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nlmatrixtopnprotocoldirlocalindex
            
            	The protocolDirLocalIndex of the network layer protocol of this entry's network address
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: nlmatrixtopnreverseoctetrate
            
            	The number of octets seen from the destination host to the source host during this sampling interval, counted using the rules for counting the nlMatrixDSOctets object (note that the corresponding nlMatrixSDOctets object selected is the one whose source address is equal to nlMatrixTopNDestAddress and whose destination address is equal to nlMatrixTopNSourceAddress.)  Note that if the value of nlMatrixTopNControlRateBase is equal to nlMatrixTopNOctets, the sort of topN entries is based entirely on nlMatrixTopNOctetRate, and not on the value of this object
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nlmatrixtopnreversepktrate
            
            	The number of packets seen from the destination host to the source host during this sampling interval, counted using the rules for counting the nlMatrixSDPkts object (note that the corresponding nlMatrixSDPkts object selected is the one whose source address is equal to nlMatrixTopNDestAddress and whose destination address is equal to nlMatrixTopNSourceAddress.)  Note that if the value of nlMatrixTopNControlRateBase is equal to nlMatrixTopNPkts, the sort of topN entries is based entirely on nlMatrixTopNPktRate, and not on the value of this object
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nlmatrixtopnsourceaddress
            
            	The network layer address of the source host in this conversation.  This is represented as an octet string with specific semantics and length as identified by the associated nlMatrixTopNProtocolDirLocalIndex.  For example, if the protocolDirLocalIndex indicates an encapsulation of ip, this object is encoded as a length octet of 4, followed by the 4 octets of the ip address, in network byte order
            	**type**\: str
            
            

            """

            _prefix = 'rmon2-mib'
            _revision = '1996-05-27'

            def __init__(self):
                self.parent = None
                self.nlmatrixtopncontrolindex = None
                self.nlmatrixtopnindex = None
                self.nlmatrixtopndestaddress = None
                self.nlmatrixtopnoctetrate = None
                self.nlmatrixtopnpktrate = None
                self.nlmatrixtopnprotocoldirlocalindex = None
                self.nlmatrixtopnreverseoctetrate = None
                self.nlmatrixtopnreversepktrate = None
                self.nlmatrixtopnsourceaddress = None

            @property
            def _common_path(self):
                if self.nlmatrixtopncontrolindex is None:
                    raise YPYDataValidationError('Key property nlmatrixtopncontrolindex is None')
                if self.nlmatrixtopnindex is None:
                    raise YPYDataValidationError('Key property nlmatrixtopnindex is None')

                return '/RMON2-MIB:RMON2-MIB/RMON2-MIB:nlMatrixTopNTable/RMON2-MIB:nlMatrixTopNEntry[RMON2-MIB:nlMatrixTopNControlIndex = ' + str(self.nlmatrixtopncontrolindex) + '][RMON2-MIB:nlMatrixTopNIndex = ' + str(self.nlmatrixtopnindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.nlmatrixtopncontrolindex is not None:
                    return True

                if self.nlmatrixtopnindex is not None:
                    return True

                if self.nlmatrixtopndestaddress is not None:
                    return True

                if self.nlmatrixtopnoctetrate is not None:
                    return True

                if self.nlmatrixtopnpktrate is not None:
                    return True

                if self.nlmatrixtopnprotocoldirlocalindex is not None:
                    return True

                if self.nlmatrixtopnreverseoctetrate is not None:
                    return True

                if self.nlmatrixtopnreversepktrate is not None:
                    return True

                if self.nlmatrixtopnsourceaddress is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.rmon2._meta import _RMON2_MIB as meta
                return meta._meta_table['RMON2MIB.NlMatrixTopNTable.NlMatrixTopNEntry']['meta_info']

        @property
        def _common_path(self):

            return '/RMON2-MIB:RMON2-MIB/RMON2-MIB:nlMatrixTopNTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.nlmatrixtopnentry is not None:
                for child_ref in self.nlmatrixtopnentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.rmon2._meta import _RMON2_MIB as meta
            return meta._meta_table['RMON2MIB.NlMatrixTopNTable']['meta_info']


    class ProbeConfig(object):
        """
        
        
        .. attribute:: netdefaultgateway
        
        	The IP Address of the default gateway.  If this value is undefined or unknown, it shall have the value 0.0.0.0
        	**type**\: str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        .. attribute:: probecapabilities
        
        	An indication of the RMON MIB groups supported on at least one interface by this probe
        	**type**\: str
        
        	**range:** 1
        
        .. attribute:: probedatetime
        
        	Probe's current date and time.  field  octets  contents                  range \-\-\-\-\-  \-\-\-\-\-\-  \-\-\-\-\-\-\-\-                  \-\-\-\-\-   1      1\-2   year                      0..65536   2       3    month                     1..12   3       4    day                       1..31   4       5    hour                      0..23   5       6    minutes                   0..59   6       7    seconds                   0..60                 (use 60 for leap\-second)   7       8    deci\-seconds              0..9   8       9    direction from UTC        '+' / '\-'   9      10    hours from UTC            0..11  10      11    minutes from UTC          0..59  For example, Tuesday May 26, 1992 at 1\:30\:15 PM EDT would be displayed as\:              1992\-5\-26,13\:30\:15.0,\-4\:0  Note that if only local time is known, then timezone information (fields 8\-10) is not present, and if no time information is known, the null string is returned
        	**type**\: str
        
        	**range:** 0 \| 8 \| 11
        
        .. attribute:: probedownloadaction
        
        	When this object is set to downloadToRAM(2) or downloadToPROM(3), the device will discontinue its normal operation and begin download of the image specified by probeDownloadFile from the server specified by probeDownloadTFTPServer using the TFTP protocol.  If downloadToRAM(2) is specified, the new image is copied to RAM only (the old image remains unaltered in the flash EPROM).  If downloadToPROM(3) is specified the new image is written to the flash EPROM memory after its checksum has been verified to be correct. When the download process is completed, the device will      warm boot to restart the newly loaded application. When the device is not downloading, this object will have a value of notDownloading(1)
        	**type**\: :py:class:`ProbeDownloadAction_Enum <ydk.models.rmon2.RMON2_MIB.RMON2MIB.ProbeConfig.ProbeDownloadAction_Enum>`
        
        .. attribute:: probedownloadfile
        
        	The file name to be downloaded from the TFTP server when a download is next requested via this MIB.  This value is set to the zero length string when no file name has been specified
        	**type**\: str
        
        	**range:** 0..127
        
        .. attribute:: probedownloadstatus
        
        	The status of the last download procedure, if any.  This object will have a value of downloadStatusUnknown(2) if no download process has been performed
        	**type**\: :py:class:`ProbeDownloadStatus_Enum <ydk.models.rmon2.RMON2_MIB.RMON2MIB.ProbeConfig.ProbeDownloadStatus_Enum>`
        
        .. attribute:: probedownloadtftpserver
        
        	The IP address of the TFTP server that contains the boot image to load when a download is next requested via this MIB. This value is set to `0.0.0.0' when no IP address has been specified
        	**type**\: str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        .. attribute:: probehardwarerev
        
        	The hardware revision of this device.  This string will have a zero length if the revision is unknown
        	**type**\: str
        
        	**range:** 0..31
        
        .. attribute:: proberesetcontrol
        
        	Setting this object to warmBoot(2) causes the device to restart the application software with current configuration parameters saved in non\-volatile memory.  Setting this object to coldBoot(3) causes the device to reinitialize configuration parameters in non\-volatile memory to default values and restart the application software.  When the device is running normally, this variable has a value of running(1)
        	**type**\: :py:class:`ProbeResetControl_Enum <ydk.models.rmon2.RMON2_MIB.RMON2MIB.ProbeConfig.ProbeResetControl_Enum>`
        
        .. attribute:: probesoftwarerev
        
        	The software revision of this device.  This string will have a zero length if the revision is unknown
        	**type**\: str
        
        	**range:** 0..15
        
        

        """

        _prefix = 'rmon2-mib'
        _revision = '1996-05-27'

        def __init__(self):
            self.parent = None
            self.netdefaultgateway = None
            self.probecapabilities = None
            self.probedatetime = None
            self.probedownloadaction = None
            self.probedownloadfile = None
            self.probedownloadstatus = None
            self.probedownloadtftpserver = None
            self.probehardwarerev = None
            self.proberesetcontrol = None
            self.probesoftwarerev = None

        class ProbeDownloadAction_Enum(Enum):
            """
            ProbeDownloadAction_Enum

            When this object is set to downloadToRAM(2) or
            downloadToPROM(3), the device will discontinue its
            normal operation and begin download of the image specified
            by probeDownloadFile from the server specified by
            probeDownloadTFTPServer using the TFTP protocol.  If
            downloadToRAM(2) is specified, the new image is copied
            to RAM only (the old image remains unaltered in the flash
            EPROM).  If downloadToPROM(3) is specified
            the new image is written to the flash EPROM
            memory after its checksum has been verified to be correct.
            When the download process is completed, the device will
            
            
            
            
            
            warm boot to restart the newly loaded application.
            When the device is not downloading, this object will have
            a value of notDownloading(1).

            """

            NOTDOWNLOADING = 1

            DOWNLOADTOPROM = 2

            DOWNLOADTORAM = 3


            @staticmethod
            def _meta_info():
                from ydk.models.rmon2._meta import _RMON2_MIB as meta
                return meta._meta_table['RMON2MIB.ProbeConfig.ProbeDownloadAction_Enum']


        class ProbeDownloadStatus_Enum(Enum):
            """
            ProbeDownloadStatus_Enum

            The status of the last download procedure, if any.  This
            object will have a value of downloadStatusUnknown(2) if no
            download process has been performed.

            """

            DOWNLOADSUCCESS = 1

            DOWNLOADSTATUSUNKNOWN = 2

            DOWNLOADGENERALERROR = 3

            DOWNLOADNORESPONSEFROMSERVER = 4

            DOWNLOADCHECKSUMERROR = 5

            DOWNLOADINCOMPATIBLEIMAGE = 6

            DOWNLOADTFTPFILENOTFOUND = 7

            DOWNLOADTFTPACCESSVIOLATION = 8


            @staticmethod
            def _meta_info():
                from ydk.models.rmon2._meta import _RMON2_MIB as meta
                return meta._meta_table['RMON2MIB.ProbeConfig.ProbeDownloadStatus_Enum']


        class ProbeResetControl_Enum(Enum):
            """
            ProbeResetControl_Enum

            Setting this object to warmBoot(2) causes the device to
            restart the application software with current configuration
            parameters saved in non\-volatile memory.  Setting this
            object to coldBoot(3) causes the device to reinitialize
            configuration parameters in non\-volatile memory to default
            values and restart the application software.  When the device
            is running normally, this variable has a value of
            running(1).

            """

            RUNNING = 1

            WARMBOOT = 2

            COLDBOOT = 3


            @staticmethod
            def _meta_info():
                from ydk.models.rmon2._meta import _RMON2_MIB as meta
                return meta._meta_table['RMON2MIB.ProbeConfig.ProbeResetControl_Enum']


        @property
        def _common_path(self):

            return '/RMON2-MIB:RMON2-MIB/RMON2-MIB:probeConfig'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.netdefaultgateway is not None:
                return True

            if self.probecapabilities is not None:
                return True

            if self.probedatetime is not None:
                return True

            if self.probedownloadaction is not None:
                return True

            if self.probedownloadfile is not None:
                return True

            if self.probedownloadstatus is not None:
                return True

            if self.probedownloadtftpserver is not None:
                return True

            if self.probehardwarerev is not None:
                return True

            if self.proberesetcontrol is not None:
                return True

            if self.probesoftwarerev is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.rmon2._meta import _RMON2_MIB as meta
            return meta._meta_table['RMON2MIB.ProbeConfig']['meta_info']


    class ProtocolDir(object):
        """
        
        
        .. attribute:: protocoldirlastchange
        
        	The value of sysUpTime at the time the protocol directory was last modified, either through insertions or deletions, or through modifications of either the protocolDirAddressMapConfig, protocolDirHostConfig, or protocolDirMatrixConfig
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'rmon2-mib'
        _revision = '1996-05-27'

        def __init__(self):
            self.parent = None
            self.protocoldirlastchange = None

        @property
        def _common_path(self):

            return '/RMON2-MIB:RMON2-MIB/RMON2-MIB:protocolDir'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.protocoldirlastchange is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.rmon2._meta import _RMON2_MIB as meta
            return meta._meta_table['RMON2MIB.ProtocolDir']['meta_info']


    class ProtocolDirTable(object):
        """
        This table lists the protocols that this agent has the
        capability to decode and count.  There is one entry in this
        table for each such protocol.  These protocols represent
        different network layer, transport layer, and higher\-layer
        protocols.  The agent should boot up with this table
        preconfigured with those protocols that it knows about and
        wishes to monitor.  Implementations are strongly encouraged to
        support protocols higher than the network layer (at least for
        the protocol distribution group), even for implementations
        that don't support the application layer groups.
        
        .. attribute:: protocoldirentry
        
        	A conceptual row in the protocolDirTable.  An example of the indexing of this entry is protocolDirLocalIndex.8.0.0.0.1.0.0.8.0.2.0.0, which is the encoding of a length of 8, followed by 8 subids encoding the protocolDirID of 1.2048, followed by a length of 2 and the 2 subids encoding zero\-valued parameters
        	**type**\: list of :py:class:`ProtocolDirEntry <ydk.models.rmon2.RMON2_MIB.RMON2MIB.ProtocolDirTable.ProtocolDirEntry>`
        
        

        """

        _prefix = 'rmon2-mib'
        _revision = '1996-05-27'

        def __init__(self):
            self.parent = None
            self.protocoldirentry = YList()
            self.protocoldirentry.parent = self
            self.protocoldirentry.name = 'protocoldirentry'


        class ProtocolDirEntry(object):
            """
            A conceptual row in the protocolDirTable.
            
            An example of the indexing of this entry is
            protocolDirLocalIndex.8.0.0.0.1.0.0.8.0.2.0.0, which is the
            encoding of a length of 8, followed by 8 subids encoding the
            protocolDirID of 1.2048, followed by a length of 2 and the
            2 subids encoding zero\-valued parameters.
            
            .. attribute:: protocoldirid
            
            	A unique identifier for a particular protocol.  Standard identifiers will be defined in a manner such that they can often be used as specifications for new protocols \- i.e. a tree\-structured assignment mechanism that matches the protocol encapsulation `tree' and which has algorithmic assignment mechanisms for certain subtrees. See RFC XXX for more details.  Despite the algorithmic mechanism, the probe will only place entries in here for those protocols it chooses to collect.  In other words, it need not populate this table with all of the possible ethernet protocol types, nor need it create them on the fly when it sees them.  Whether or not it does these things is a matter of product definition (cost/benefit, usability), and is up to the designer of the product.  If an entry is written to this table with a protocolDirID that the agent doesn't understand, either directly or algorithmically, the SET request will be rejected with an inconsistentName or badValue (for SNMPv1) error
            	**type**\: str
            
            .. attribute:: protocoldirparameters
            
            	A set of parameters for the associated protocolDirID. See the associated RMON2 Protocol Identifiers document for a description of the possible parameters. There will be one octet in this string for each sub\-identifier in the protocolDirID, and the parameters will appear here in the same order as the associated sub\-identifiers appear in the protocolDirID.  Every node in the protocolDirID tree has a different, optional set of parameters defined (that is, the definition of parameters for a node is optional).  The proper parameter value for each node is included in this string.  Note that the inclusion of a parameter value in this string for each node is not optional \- what is optional is that a node may have no parameters defined, in which case the parameter field for that node will be zero
            	**type**\: str
            
            .. attribute:: protocoldiraddressmapconfig
            
            	This object describes and configures the probe's support for address mapping for this protocol.  When the probe creates entries in this table for all protocols that it understands, it will set the entry to notSupported(1) if it doesn't have the capability to perform address mapping for the protocol or if this protocol is not a network\-layer protocol.  When an entry is created in this table by a management operation as part of the limited extensibility feature, the probe must set this value to notSupported(1), because limited extensibility of the protocolDirTable does not extend to interpreting addresses of the extended protocols.  If the value of this object is notSupported(1), the probe will not perform address mapping for this protocol and shall not allow this object to be changed to any other value. If the value of this object is supportedOn(3), the probe supports address mapping for this protocol and is configured to perform address mapping for this protocol for all addressMappingControlEntries and all interfaces. If the value of this object is supportedOff(2), the probe supports address mapping for this protocol but is configured to not perform address mapping for this protocol for any addressMappingControlEntries and all interfaces. Whenever this value changes from supportedOn(3) to supportedOff(2), the probe shall delete all related entries in the addressMappingTable
            	**type**\: :py:class:`ProtocolDirAddressMapConfig_Enum <ydk.models.rmon2.RMON2_MIB.RMON2MIB.ProtocolDirTable.ProtocolDirEntry.ProtocolDirAddressMapConfig_Enum>`
            
            .. attribute:: protocoldirdescr
            
            	A textual description of the protocol encapsulation. A probe may choose to describe only a subset of the entire encapsulation (e.g. only the highest layer).  This object is intended for human consumption only.  This object may not be modified if the associated protocolDirStatus object is equal to active(1)
            	**type**\: str
            
            	**range:** 1..64
            
            .. attribute:: protocoldirhostconfig
            
            	This object describes and configures the probe's support for the network layer and application layer host tables for this protocol.  When the probe creates entries in this table for all protocols that it understands, it will set the entry to notSupported(1) if it doesn't have the capability to track the nlHostTable for this protocol or if the alHostTable is implemented but doesn't have the capability to track this protocol.  Note that if the alHostTable is implemented, the probe may only support a protocol if it is supported in both the nlHostTable and the alHostTable.      If the associated protocolDirType object has the addressRecognitionCapable bit set, then this is a network layer protocol for which the probe recognizes addresses, and thus the probe will populate the nlHostTable and alHostTable with addresses it discovers for this protocol.  If the value of this object is notSupported(1), the probe will not track the nlHostTable or alHostTable for this protocol and shall not allow this object to be changed to any other value. If the value of this object is supportedOn(3), the probe supports tracking of the nlHostTable and alHostTable for this protocol and is configured to track both tables for this protocol for all control entries and all interfaces. If the value of this object is supportedOff(2), the probe supports tracking of the nlHostTable and alHostTable for this protocol but is configured to not track these tables for any control entries or interfaces. Whenever this value changes from supportedOn(3) to supportedOff(2), the probe shall delete all related entries in the nlHostTable and alHostTable.  Note that since each alHostEntry references 2 protocol directory entries, one for the network address and one for the type of the highest protocol recognized, that an entry will only be created in that table if this value is supportedOn(3) for both protocols
            	**type**\: :py:class:`ProtocolDirHostConfig_Enum <ydk.models.rmon2.RMON2_MIB.RMON2MIB.ProtocolDirTable.ProtocolDirEntry.ProtocolDirHostConfig_Enum>`
            
            .. attribute:: protocoldirlocalindex
            
            	The locally arbitrary, but unique identifier associated with this protocolDir entry.  The value for each supported protocol must remain constant at least from one re\-initialization of the entity's network management system to the next re\-initialization, except that if a protocol is deleted and re\-created, it must be re\-created with a new value that has not been used since the last re\-initialization.  The specific value is meaningful only within a given SNMP entity. A protocolDirLocalIndex must not be re\-used until the next agent\-restart in the event the protocol directory entry is deleted
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: protocoldirmatrixconfig
            
            	This object describes and configures the probe's support for the network layer and application layer matrix tables for this protocol.  When the probe creates entries in this table for all protocols that it understands, it will set the entry to notSupported(1) if it doesn't have the capability to track the nlMatrixTables for this protocol or if the alMatrixTables are implemented but don't have the capability to track this protocol.  Note that if the alMatrix tables are implemented, the probe may only support a protocol if it is supported in the the both of the nlMatrixTables and both of the alMatrixTables.      If the associated protocolDirType object has the addressRecognitionCapable bit set, then this is a network layer protocol for which the probe recognizes addresses, and thus the probe will populate both of the nlMatrixTables and both of the alMatrixTables with addresses it discovers for this protocol.  If the value of this object is notSupported(1), the probe will not track either of the nlMatrixTables or the alMatrixTables for this protocol and shall not allow this object to be changed to any other value. If the value of this object is supportedOn(3), the probe supports tracking of both of the nlMatrixTables and (if implemented) both of the alMatrixTables for this protocol and is configured to track these tables for this protocol for all control entries and all interfaces. If the value of this object is supportedOff(2), the probe supports tracking of both of the nlMatrixTables and (if implemented) both of the alMatrixTables for this protocol but is configured to not track these tables for this protocol for any control entries or interfaces. Whenever this value changes from supportedOn(3) to supportedOff(2), the probe shall delete all related entries in the nlMatrixTables and the alMatrixTables.  Note that since each alMatrixEntry references 2 protocol directory entries, one for the network address and one for the type of the highest protocol recognized, that an entry will only be created in that table if this value is supportedOn(3) for both protocols
            	**type**\: :py:class:`ProtocolDirMatrixConfig_Enum <ydk.models.rmon2.RMON2_MIB.RMON2MIB.ProtocolDirTable.ProtocolDirEntry.ProtocolDirMatrixConfig_Enum>`
            
            .. attribute:: protocoldirowner
            
            	The entity that configured this entry and is therefore using the resources assigned to it
            	**type**\: str
            
            	**range:** 0..127
            
            .. attribute:: protocoldirstatus
            
            	The status of this protocol directory entry.  An entry may not exist in the active state unless all      objects in the entry have an appropriate value.  If this object is not equal to active(1), all associated entries in the nlHostTable, nlMatrixSDTable, nlMatrixDSTable, alHostTable, alMatrixSDTable, and alMatrixDSTable shall be deleted
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            .. attribute:: protocoldirtype
            
            	This object describes 2 attributes of this protocol directory entry.  The presence or absence of the `extensible' bit describes whether or not this protocol directory entry can be extended      by the user by creating protocol directory entries which are children of this protocol.  An example of an entry that will often allow extensibility is `ip.udp'.  The probe may automatically populate some children of this node such as `ip.udp.snmp' and `ip.udp.dns'. A probe administrator or user may also populate additional children via remote SNMP requests that create entries in this table.  When a child node is added for a protocol for which the probe has no built in support, extending a parent node (for which the probe does have built in support), that child node is not extendible.  This is termed `limited extensibility'.  When a child node is added through this extensibility mechanism, the values of protocolDirLocalIndex and protocolDirType shall be assigned by the agent.  The other objects in the entry will be assigned by the manager who is creating the new entry.  This object also describes whether or not this agent can recognize addresses for this protocol, should it be a network level protocol.  That is, while a probe may be able to recognize packets of a particular network layer protocol and count them, it takes additional logic to be able to recognize the addresses in this protocol and to populate network layer or application layer tables with the addresses in this protocol.  If this bit is set, the agent will recognize network layer addresses for this protoocl and populate the network and application layer host and matrix tables with these protocols.  Note that when an entry is created, the agent will supply values for the bits that match the capabilities of the agent with respect to this protocol.  Note that since row creations usually exercise the limited extensibility feature, these bits will usually be set to zero
            	**type**\: str
            
            	**range:** 1
            
            

            """

            _prefix = 'rmon2-mib'
            _revision = '1996-05-27'

            def __init__(self):
                self.parent = None
                self.protocoldirid = None
                self.protocoldirparameters = None
                self.protocoldiraddressmapconfig = None
                self.protocoldirdescr = None
                self.protocoldirhostconfig = None
                self.protocoldirlocalindex = None
                self.protocoldirmatrixconfig = None
                self.protocoldirowner = None
                self.protocoldirstatus = None
                self.protocoldirtype = None

            class ProtocolDirAddressMapConfig_Enum(Enum):
                """
                ProtocolDirAddressMapConfig_Enum

                This object describes and configures the probe's support for
                address mapping for this protocol.  When the probe creates
                entries in this table for all protocols that it understands,
                it will set the entry to notSupported(1) if it doesn't have
                the capability to perform address mapping for the protocol or
                if this protocol is not a network\-layer protocol.  When
                an entry is created in this table by a management operation as
                part of the limited extensibility feature, the probe must set
                this value to notSupported(1), because limited extensibility
                of the protocolDirTable does not extend to interpreting
                addresses of the extended protocols.
                
                If the value of this object is notSupported(1), the probe
                will not perform address mapping for this protocol and
                shall not allow this object to be changed to any other value.
                If the value of this object is supportedOn(3), the probe
                supports address mapping for this protocol and is configured
                to perform address mapping for this protocol for all
                addressMappingControlEntries and all interfaces.
                If the value of this object is supportedOff(2), the probe
                supports address mapping for this protocol but is configured
                to not perform address mapping for this protocol for any
                addressMappingControlEntries and all interfaces.
                Whenever this value changes from supportedOn(3) to
                supportedOff(2), the probe shall delete all related entries in
                the addressMappingTable.

                """

                NOTSUPPORTED = 1

                SUPPORTEDOFF = 2

                SUPPORTEDON = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.rmon2._meta import _RMON2_MIB as meta
                    return meta._meta_table['RMON2MIB.ProtocolDirTable.ProtocolDirEntry.ProtocolDirAddressMapConfig_Enum']


            class ProtocolDirHostConfig_Enum(Enum):
                """
                ProtocolDirHostConfig_Enum

                This object describes and configures the probe's support for
                the network layer and application layer host tables for this
                protocol.  When the probe creates entries in this table for
                all protocols that it understands, it will set the entry to
                notSupported(1) if it doesn't have the capability to track the
                nlHostTable for this protocol or if the alHostTable is
                implemented but doesn't have the capability to track this
                protocol.  Note that if the alHostTable is implemented, the
                probe may only support a protocol if it is supported in both
                the nlHostTable and the alHostTable.
                
                
                
                
                
                If the associated protocolDirType object has the
                addressRecognitionCapable bit set, then this is a network
                layer protocol for which the probe recognizes addresses, and
                thus the probe will populate the nlHostTable and alHostTable
                with addresses it discovers for this protocol.
                
                If the value of this object is notSupported(1), the probe
                will not track the nlHostTable or alHostTable for this
                protocol and shall not allow this object to be changed to any
                other value. If the value of this object is supportedOn(3),
                the probe supports tracking of the nlHostTable and alHostTable
                for this protocol and is configured to track both tables
                for this protocol for all control entries and all interfaces.
                If the value of this object is supportedOff(2), the probe
                supports tracking of the nlHostTable and alHostTable for this
                protocol but is configured to not track these tables
                for any control entries or interfaces.
                Whenever this value changes from supportedOn(3) to
                supportedOff(2), the probe shall delete all related entries in
                the nlHostTable and alHostTable.
                
                Note that since each alHostEntry references 2 protocol
                directory entries, one for the network address and one for the
                type of the highest protocol recognized, that an entry will
                only be created in that table if this value is supportedOn(3)
                for both protocols.

                """

                NOTSUPPORTED = 1

                SUPPORTEDOFF = 2

                SUPPORTEDON = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.rmon2._meta import _RMON2_MIB as meta
                    return meta._meta_table['RMON2MIB.ProtocolDirTable.ProtocolDirEntry.ProtocolDirHostConfig_Enum']


            class ProtocolDirMatrixConfig_Enum(Enum):
                """
                ProtocolDirMatrixConfig_Enum

                This object describes and configures the probe's support for
                the network layer and application layer matrix tables for this
                protocol.  When the probe creates entries in this table for
                all protocols that it understands, it will set the entry to
                notSupported(1) if it doesn't have the capability to track the
                nlMatrixTables for this protocol or if the alMatrixTables are
                implemented but don't have the capability to track this
                protocol.  Note that if the alMatrix tables are implemented,
                the probe may only support a protocol if it is supported in
                the the both of the nlMatrixTables and both of the
                alMatrixTables.
                
                
                
                
                
                If the associated protocolDirType object has the
                addressRecognitionCapable bit set, then this is a network
                layer protocol for which the probe recognizes addresses, and
                thus the probe will populate both of the nlMatrixTables and
                both of the alMatrixTables with addresses it discovers for
                this protocol.
                
                If the value of this object is notSupported(1), the probe
                will not track either of the nlMatrixTables or the
                alMatrixTables for this protocol and shall not allow this
                object to be changed to any other value. If the value of this
                object is supportedOn(3), the probe supports tracking of both
                of the nlMatrixTables and (if implemented) both of the
                alMatrixTables for this protocol and is configured to track
                these tables for this protocol for all control entries and all
                interfaces. If the value of this object is supportedOff(2),
                the probe supports tracking of both of the nlMatrixTables and
                (if implemented) both of the alMatrixTables for this protocol
                but is configured to not track these tables for this
                protocol for any control entries or interfaces.
                Whenever this value changes from supportedOn(3) to
                supportedOff(2), the probe shall delete all related entries in
                the nlMatrixTables and the alMatrixTables.
                
                Note that since each alMatrixEntry references 2 protocol
                directory entries, one for the network address and one for the
                type of the highest protocol recognized, that an entry will
                only be created in that table if this value is supportedOn(3)
                for both protocols.

                """

                NOTSUPPORTED = 1

                SUPPORTEDOFF = 2

                SUPPORTEDON = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.rmon2._meta import _RMON2_MIB as meta
                    return meta._meta_table['RMON2MIB.ProtocolDirTable.ProtocolDirEntry.ProtocolDirMatrixConfig_Enum']


            @property
            def _common_path(self):
                if self.protocoldirid is None:
                    raise YPYDataValidationError('Key property protocoldirid is None')
                if self.protocoldirparameters is None:
                    raise YPYDataValidationError('Key property protocoldirparameters is None')

                return '/RMON2-MIB:RMON2-MIB/RMON2-MIB:protocolDirTable/RMON2-MIB:protocolDirEntry[RMON2-MIB:protocolDirID = ' + str(self.protocoldirid) + '][RMON2-MIB:protocolDirParameters = ' + str(self.protocoldirparameters) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.protocoldirid is not None:
                    return True

                if self.protocoldirparameters is not None:
                    return True

                if self.protocoldiraddressmapconfig is not None:
                    return True

                if self.protocoldirdescr is not None:
                    return True

                if self.protocoldirhostconfig is not None:
                    return True

                if self.protocoldirlocalindex is not None:
                    return True

                if self.protocoldirmatrixconfig is not None:
                    return True

                if self.protocoldirowner is not None:
                    return True

                if self.protocoldirstatus is not None:
                    return True

                if self.protocoldirtype is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.rmon2._meta import _RMON2_MIB as meta
                return meta._meta_table['RMON2MIB.ProtocolDirTable.ProtocolDirEntry']['meta_info']

        @property
        def _common_path(self):

            return '/RMON2-MIB:RMON2-MIB/RMON2-MIB:protocolDirTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.protocoldirentry is not None:
                for child_ref in self.protocoldirentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.rmon2._meta import _RMON2_MIB as meta
            return meta._meta_table['RMON2MIB.ProtocolDirTable']['meta_info']


    class ProtocolDistControlTable(object):
        """
        Controls the setup of protocol type distribution statistics
        tables.
        
        Implementations are encouraged to add an entry per monitored
        interface upon initialization so that a default collection
        of protocol statistics is available.
        
        Rationale\:
        This table controls collection of very basic statistics
        for any or all of the protocols detected on a given interface.
        An NMS can use this table to quickly determine bandwidth
        allocation utilized by different protocols.
        
        A media\-specific statistics collection could also
        be configured (e.g. etherStats, trPStats) to easily obtain
        total frame, octet, and droppedEvents for the same
        interface.
        
        .. attribute:: protocoldistcontrolentry
        
        	A conceptual row in the protocolDistControlTable.  An example of the indexing of this entry is      protocolDistControlDroppedFrames.7
        	**type**\: list of :py:class:`ProtocolDistControlEntry <ydk.models.rmon2.RMON2_MIB.RMON2MIB.ProtocolDistControlTable.ProtocolDistControlEntry>`
        
        

        """

        _prefix = 'rmon2-mib'
        _revision = '1996-05-27'

        def __init__(self):
            self.parent = None
            self.protocoldistcontrolentry = YList()
            self.protocoldistcontrolentry.parent = self
            self.protocoldistcontrolentry.name = 'protocoldistcontrolentry'


        class ProtocolDistControlEntry(object):
            """
            A conceptual row in the protocolDistControlTable.
            
            An example of the indexing of this entry is
            
            
            
            
            
            protocolDistControlDroppedFrames.7
            
            .. attribute:: protocoldistcontrolindex
            
            	A unique index for this protocolDistControlEntry
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: protocoldistcontrolcreatetime
            
            	The value of sysUpTime when this control entry was last activated. This can be used by the management station to ensure that the table has not been deleted and recreated between polls
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: protocoldistcontroldatasource
            
            	The source of data for the this protocol distribution.  The statistics in this group reflect all packets on the local network segment attached to the identified interface.  This object may not be modified if the associated protocolDistControlStatus object is equal to active(1)
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: protocoldistcontroldroppedframes
            
            	The total number of frames which were received by the probe and therefore not accounted for in the \*StatsDropEvents, but for which the probe chose not to count for this entry for whatever reason.  Most often, this event occurs when the probe is out of some resources and decides to shed load from this collection.       This count does not include packets that were not counted because they had MAC\-layer errors.  Note that, unlike the dropEvents counter, this number is the exact number of frames dropped
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: protocoldistcontrolowner
            
            	The entity that configured this entry and is therefore using the resources assigned to it
            	**type**\: str
            
            	**range:** 0..127
            
            .. attribute:: protocoldistcontrolstatus
            
            	The status of this row.  An entry may not exist in the active state unless all objects in the entry have an appropriate value.  If this object is not equal to active(1), all associated entries in the protocolDistStatsTable shall be deleted
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            

            """

            _prefix = 'rmon2-mib'
            _revision = '1996-05-27'

            def __init__(self):
                self.parent = None
                self.protocoldistcontrolindex = None
                self.protocoldistcontrolcreatetime = None
                self.protocoldistcontroldatasource = None
                self.protocoldistcontroldroppedframes = None
                self.protocoldistcontrolowner = None
                self.protocoldistcontrolstatus = None

            @property
            def _common_path(self):
                if self.protocoldistcontrolindex is None:
                    raise YPYDataValidationError('Key property protocoldistcontrolindex is None')

                return '/RMON2-MIB:RMON2-MIB/RMON2-MIB:protocolDistControlTable/RMON2-MIB:protocolDistControlEntry[RMON2-MIB:protocolDistControlIndex = ' + str(self.protocoldistcontrolindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.protocoldistcontrolindex is not None:
                    return True

                if self.protocoldistcontrolcreatetime is not None:
                    return True

                if self.protocoldistcontroldatasource is not None:
                    return True

                if self.protocoldistcontroldroppedframes is not None:
                    return True

                if self.protocoldistcontrolowner is not None:
                    return True

                if self.protocoldistcontrolstatus is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.rmon2._meta import _RMON2_MIB as meta
                return meta._meta_table['RMON2MIB.ProtocolDistControlTable.ProtocolDistControlEntry']['meta_info']

        @property
        def _common_path(self):

            return '/RMON2-MIB:RMON2-MIB/RMON2-MIB:protocolDistControlTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.protocoldistcontrolentry is not None:
                for child_ref in self.protocoldistcontrolentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.rmon2._meta import _RMON2_MIB as meta
            return meta._meta_table['RMON2MIB.ProtocolDistControlTable']['meta_info']


    class ProtocolDistStatsTable(object):
        """
        An entry is made in this table for every protocol in the
        
        
        
        
        
        protocolDirTable which has been seen in at least one packet.
        Counters are updated in this table for every protocol type
        that is encountered when parsing a packet, but no counters are
        updated for packets with MAC\-layer errors.
        
        Note that if a protocolDirEntry is deleted, all associated
        entries in this table are removed.
        
        .. attribute:: protocoldiststatsentry
        
        	A conceptual row in the protocolDistStatsTable.  The index is composed of the protocolDistControlIndex of the associated protocolDistControlEntry followed by the protocolDirLocalIndex of the associated protocol that this entry represents.  In other words, the index identifies the protocol distribution an entry is a part of as well as the particular protocol that it represents.  An example of the indexing of this entry is protocolDistStatsPkts.1.18
        	**type**\: list of :py:class:`ProtocolDistStatsEntry <ydk.models.rmon2.RMON2_MIB.RMON2MIB.ProtocolDistStatsTable.ProtocolDistStatsEntry>`
        
        

        """

        _prefix = 'rmon2-mib'
        _revision = '1996-05-27'

        def __init__(self):
            self.parent = None
            self.protocoldiststatsentry = YList()
            self.protocoldiststatsentry.parent = self
            self.protocoldiststatsentry.name = 'protocoldiststatsentry'


        class ProtocolDistStatsEntry(object):
            """
            A conceptual row in the protocolDistStatsTable.
            
            The index is composed of the protocolDistControlIndex of the
            associated protocolDistControlEntry followed by the
            protocolDirLocalIndex of the associated protocol that this
            entry represents.  In other words, the index identifies the
            protocol distribution an entry is a part of as well as the
            particular protocol that it represents.
            
            An example of the indexing of this entry is
            protocolDistStatsPkts.1.18
            
            .. attribute:: protocoldirlocalindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: protocoldistcontrolindex
            
            	
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: protocoldiststatsoctets
            
            	The number of octets in packets received of this protocol type since it was added to the protocolDistStatsTable (excluding framing bits but including FCS octets), except for those octets in packets that contained errors.  Note this doesn't count just those octets in the particular protocol frames, but includes the entire packet that contained the protocol
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: protocoldiststatspkts
            
            	The number of packets without errors received of this protocol type.  Note that this is the number of link\-layer packets, so if a single network\-layer packet is fragmented into several link\-layer frames, this counter is incremented several times
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'rmon2-mib'
            _revision = '1996-05-27'

            def __init__(self):
                self.parent = None
                self.protocoldirlocalindex = None
                self.protocoldistcontrolindex = None
                self.protocoldiststatsoctets = None
                self.protocoldiststatspkts = None

            @property
            def _common_path(self):
                if self.protocoldirlocalindex is None:
                    raise YPYDataValidationError('Key property protocoldirlocalindex is None')
                if self.protocoldistcontrolindex is None:
                    raise YPYDataValidationError('Key property protocoldistcontrolindex is None')

                return '/RMON2-MIB:RMON2-MIB/RMON2-MIB:protocolDistStatsTable/RMON2-MIB:protocolDistStatsEntry[RMON2-MIB:protocolDirLocalIndex = ' + str(self.protocoldirlocalindex) + '][RMON2-MIB:protocolDistControlIndex = ' + str(self.protocoldistcontrolindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.protocoldirlocalindex is not None:
                    return True

                if self.protocoldistcontrolindex is not None:
                    return True

                if self.protocoldiststatsoctets is not None:
                    return True

                if self.protocoldiststatspkts is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.rmon2._meta import _RMON2_MIB as meta
                return meta._meta_table['RMON2MIB.ProtocolDistStatsTable.ProtocolDistStatsEntry']['meta_info']

        @property
        def _common_path(self):

            return '/RMON2-MIB:RMON2-MIB/RMON2-MIB:protocolDistStatsTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.protocoldiststatsentry is not None:
                for child_ref in self.protocoldiststatsentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.rmon2._meta import _RMON2_MIB as meta
            return meta._meta_table['RMON2MIB.ProtocolDistStatsTable']['meta_info']


    class SerialConfigTable(object):
        """
        A table of serial interface configuration entries.  This data
        will be stored in non\-volatile memory and preserved across
        probe resets or power loss.
        
        .. attribute:: serialconfigentry
        
        	A set of configuration parameters for a particular serial interface on this device. If the device has no serial interfaces, this table is empty.  The index is composed of the ifIndex assigned to this serial line interface
        	**type**\: list of :py:class:`SerialConfigEntry <ydk.models.rmon2.RMON2_MIB.RMON2MIB.SerialConfigTable.SerialConfigEntry>`
        
        

        """

        _prefix = 'rmon2-mib'
        _revision = '1996-05-27'

        def __init__(self):
            self.parent = None
            self.serialconfigentry = YList()
            self.serialconfigentry.parent = self
            self.serialconfigentry.name = 'serialconfigentry'


        class SerialConfigEntry(object):
            """
            A set of configuration parameters for a particular
            serial interface on this device. If the device has no serial
            interfaces, this table is empty.
            
            The index is composed of the ifIndex assigned to this serial
            line interface.
            
            .. attribute:: ifindex
            
            	
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: serialdialouttimeout
            
            	This timeout value is used when the probe initiates the serial connection with the intention of contacting a management station. This variable represents the number of seconds of inactivity allowed before terminating the connection on this serial interface
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: serialmode
            
            	The type of incoming connection to expect on this serial interface
            	**type**\: :py:class:`SerialMode_Enum <ydk.models.rmon2.RMON2_MIB.RMON2MIB.SerialConfigTable.SerialConfigEntry.SerialMode_Enum>`
            
            .. attribute:: serialmodemconnectresp
            
            	An ASCII string containing substrings that describe the expected modem connection response code and associated bps rate.  The substrings are delimited by the first character in the string, for example\:    /CONNECT/300/CONNECT 1200/1200/CONNECT 2400/2400/    CONNECT 4800/4800/CONNECT 9600/9600 will be interpreted as\:     response code    bps rate     CONNECT            300     CONNECT 1200      1200          CONNECT 2400      2400     CONNECT 4800      4800     CONNECT 9600      9600 The agent will use the information in this string to adjust the bps rate of this serial interface once a modem connection is established.  A value that is appropriate for a wide variety of modems is\: '/CONNECT/300/CONNECT 1200/1200/CONNECT 2400/2400/  CONNECT 4800/4800/CONNECT 9600/9600/CONNECT 14400/14400/ CONNECT 19200/19200/CONNECT 38400/38400/'
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: serialmodemhangupstring
            
            	A control string which specifies how to disconnect a modem connection on this serial interface.  This object is only meaningful if the associated serialMode has the value of modem(2). A control string that is appropriate for a wide variety of modems is\: '^d2^s+++^d2^sATH0^M^d2'
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: serialmodeminitstring
            
            	A control string which controls how a modem attached to this serial interface should be initialized.  The initialization is performed once during startup and again after each connection is terminated if the associated serialMode has the value of modem(2).  A control string that is appropriate for a wide variety of modems is\: '^s^MATE0Q0V1X4 S0=1 S2=43^M'
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: serialmodemnoconnectresp
            
            	An ASCII string containing response codes that may be generated by a modem to report the reason why a connection attempt has failed.  The response codes are delimited by the first character in the string, for example\:    /NO CARRIER/BUSY/NO DIALTONE/NO ANSWER/ERROR/ If one of these response codes is received via this serial interface while attempting to make a modem connection, the agent will issue the hang up command as specified by serialModemHangUpString.  A value that is appropriate for a wide variety of modems is\: '/NO CARRIER/BUSY/NO DIALTONE/NO ANSWER/ERROR/'
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: serialprotocol
            
            	The type of data link encapsulation to be used on this serial interface
            	**type**\: :py:class:`SerialProtocol_Enum <ydk.models.rmon2.RMON2_MIB.RMON2MIB.SerialConfigTable.SerialConfigEntry.SerialProtocol_Enum>`
            
            .. attribute:: serialstatus
            
            	The status of this serialConfigEntry.  An entry may not exist in the active state unless all objects in the entry have an appropriate value
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            .. attribute:: serialtimeout
            
            	This timeout value is used when the Management Station has initiated the conversation over the serial link. This variable represents the number of seconds of inactivity allowed before terminating the connection on this serial interface. Use the      serialDialoutTimeout in the case where the probe has initiated the connection for the purpose of sending a trap
            	**type**\: int
            
            	**range:** 1..65535
            
            

            """

            _prefix = 'rmon2-mib'
            _revision = '1996-05-27'

            def __init__(self):
                self.parent = None
                self.ifindex = None
                self.serialdialouttimeout = None
                self.serialmode = None
                self.serialmodemconnectresp = None
                self.serialmodemhangupstring = None
                self.serialmodeminitstring = None
                self.serialmodemnoconnectresp = None
                self.serialprotocol = None
                self.serialstatus = None
                self.serialtimeout = None

            class SerialMode_Enum(Enum):
                """
                SerialMode_Enum

                The type of incoming connection to expect on this serial
                interface.

                """

                DIRECT = 1

                MODEM = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.rmon2._meta import _RMON2_MIB as meta
                    return meta._meta_table['RMON2MIB.SerialConfigTable.SerialConfigEntry.SerialMode_Enum']


            class SerialProtocol_Enum(Enum):
                """
                SerialProtocol_Enum

                The type of data link encapsulation to be used on this
                serial interface.

                """

                OTHER = 1

                SLIP = 2

                PPP = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.rmon2._meta import _RMON2_MIB as meta
                    return meta._meta_table['RMON2MIB.SerialConfigTable.SerialConfigEntry.SerialProtocol_Enum']


            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYDataValidationError('Key property ifindex is None')

                return '/RMON2-MIB:RMON2-MIB/RMON2-MIB:serialConfigTable/RMON2-MIB:serialConfigEntry[RMON2-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ifindex is not None:
                    return True

                if self.serialdialouttimeout is not None:
                    return True

                if self.serialmode is not None:
                    return True

                if self.serialmodemconnectresp is not None:
                    return True

                if self.serialmodemhangupstring is not None:
                    return True

                if self.serialmodeminitstring is not None:
                    return True

                if self.serialmodemnoconnectresp is not None:
                    return True

                if self.serialprotocol is not None:
                    return True

                if self.serialstatus is not None:
                    return True

                if self.serialtimeout is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.rmon2._meta import _RMON2_MIB as meta
                return meta._meta_table['RMON2MIB.SerialConfigTable.SerialConfigEntry']['meta_info']

        @property
        def _common_path(self):

            return '/RMON2-MIB:RMON2-MIB/RMON2-MIB:serialConfigTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.serialconfigentry is not None:
                for child_ref in self.serialconfigentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.rmon2._meta import _RMON2_MIB as meta
            return meta._meta_table['RMON2MIB.SerialConfigTable']['meta_info']


    class SerialConnectionTable(object):
        """
        A list of serialConnectionEntries.
        
        .. attribute:: serialconnectionentry
        
        	Configuration for a SLIP link over a serial line
        	**type**\: list of :py:class:`SerialConnectionEntry <ydk.models.rmon2.RMON2_MIB.RMON2MIB.SerialConnectionTable.SerialConnectionEntry>`
        
        

        """

        _prefix = 'rmon2-mib'
        _revision = '1996-05-27'

        def __init__(self):
            self.parent = None
            self.serialconnectionentry = YList()
            self.serialconnectionentry.parent = self
            self.serialconnectionentry.name = 'serialconnectionentry'


        class SerialConnectionEntry(object):
            """
            Configuration for a SLIP link over a serial line.
            
            .. attribute:: serialconnectindex
            
            	A value that uniquely identifies this serialConnection entry
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: serialconnectdestipaddress
            
            	The IP Address that can be reached at the other end of this serial connection. This object may not be modified if the associated serialConnectStatus object is equal to active(1)
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: serialconnectdialstring
            
            	A control string which specifies how to dial the phone number in order to establish a modem connection.  The string should include dialing prefix and suffix.  For example\: ``^s^MATD9,888\-1234^M'' will instruct the Probe to send a carriage return followed by the dialing prefix ``ATD'', the phone number ``9,888\-1234'', and a carriage return as the dialing suffix. This object may not be modified if the associated serialConnectStatus object is equal to active(1)
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: serialconnectowner
            
            	The entity that configured this entry and is therefore using the resources assigned to it
            	**type**\: str
            
            	**range:** 0..127
            
            .. attribute:: serialconnectstatus
            
            	The status of this serialConnectionEntry.  If the manager attempts to set this object to active(1) when the serialConnectType is set to modem(2) or modem\-switch(4) and the serialConnectDialString is a zero\-length string or cannot be correctly parsed as a ConnectString, the set request will be rejected with badValue(3).  If the manager attempts to set this object to active(1) when the serialConnectType is set to switch(3) or modem\-switch(4) and the serialConnectSwitchConnectSeq, the serialConnectSwitchDisconnectSeq, or the serialConnectSwitchResetSeq are zero\-length strings or cannot be correctly parsed as ConnectStrings, the set request will be rejected with badValue(3).  An entry may not exist in the active state unless all objects in the entry have an appropriate value
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            .. attribute:: serialconnectswitchconnectseq
            
            	A control string which specifies how to establish a data switch connection. This object may not be modified if the associated serialConnectStatus object is equal to active(1)
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: serialconnectswitchdisconnectseq
            
            	A control string which specifies how to terminate a data switch connection. This object may not be modified if the associated      serialConnectStatus object is equal to active(1)
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: serialconnectswitchresetseq
            
            	A control string which specifies how to reset a data switch in the event of a timeout. This object may not be modified if the associated serialConnectStatus object is equal to active(1)
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: serialconnecttype
            
            	The type of outgoing connection to make.  If this object has the value direct(1), then a direct serial connection is assumed.  If this object has the value modem(2), then serialConnectDialString will be used to make a modem connection.  If this object has the value switch(3),      then serialConnectSwitchConnectSeq will be used to establish the connection over a serial data switch, and serialConnectSwitchDisconnectSeq will be used to terminate the connection.  If this object has the value modem\-switch(4), then a modem connection will be made first followed by the switch connection.  This object may not be modified if the associated serialConnectStatus object is equal to active(1)
            	**type**\: :py:class:`SerialConnectType_Enum <ydk.models.rmon2.RMON2_MIB.RMON2MIB.SerialConnectionTable.SerialConnectionEntry.SerialConnectType_Enum>`
            
            

            """

            _prefix = 'rmon2-mib'
            _revision = '1996-05-27'

            def __init__(self):
                self.parent = None
                self.serialconnectindex = None
                self.serialconnectdestipaddress = None
                self.serialconnectdialstring = None
                self.serialconnectowner = None
                self.serialconnectstatus = None
                self.serialconnectswitchconnectseq = None
                self.serialconnectswitchdisconnectseq = None
                self.serialconnectswitchresetseq = None
                self.serialconnecttype = None

            class SerialConnectType_Enum(Enum):
                """
                SerialConnectType_Enum

                The type of outgoing connection to make.  If this object
                has the value direct(1), then a direct serial connection
                is assumed.  If this object has the value modem(2),
                then serialConnectDialString will be used to make a modem
                connection.  If this object has the value switch(3),
                
                
                
                
                
                then serialConnectSwitchConnectSeq will be used to establish
                the connection over a serial data switch, and
                serialConnectSwitchDisconnectSeq will be used to terminate
                the connection.  If this object has the value
                modem\-switch(4), then a modem connection will be made first
                followed by the switch connection.
                
                This object may not be modified if the associated
                serialConnectStatus object is equal to active(1).

                """

                DIRECT = 1

                MODEM = 2

                SWITCH = 3

                MODEMSWITCH = 4


                @staticmethod
                def _meta_info():
                    from ydk.models.rmon2._meta import _RMON2_MIB as meta
                    return meta._meta_table['RMON2MIB.SerialConnectionTable.SerialConnectionEntry.SerialConnectType_Enum']


            @property
            def _common_path(self):
                if self.serialconnectindex is None:
                    raise YPYDataValidationError('Key property serialconnectindex is None')

                return '/RMON2-MIB:RMON2-MIB/RMON2-MIB:serialConnectionTable/RMON2-MIB:serialConnectionEntry[RMON2-MIB:serialConnectIndex = ' + str(self.serialconnectindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.serialconnectindex is not None:
                    return True

                if self.serialconnectdestipaddress is not None:
                    return True

                if self.serialconnectdialstring is not None:
                    return True

                if self.serialconnectowner is not None:
                    return True

                if self.serialconnectstatus is not None:
                    return True

                if self.serialconnectswitchconnectseq is not None:
                    return True

                if self.serialconnectswitchdisconnectseq is not None:
                    return True

                if self.serialconnectswitchresetseq is not None:
                    return True

                if self.serialconnecttype is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.rmon2._meta import _RMON2_MIB as meta
                return meta._meta_table['RMON2MIB.SerialConnectionTable.SerialConnectionEntry']['meta_info']

        @property
        def _common_path(self):

            return '/RMON2-MIB:RMON2-MIB/RMON2-MIB:serialConnectionTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.serialconnectionentry is not None:
                for child_ref in self.serialconnectionentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.rmon2._meta import _RMON2_MIB as meta
            return meta._meta_table['RMON2MIB.SerialConnectionTable']['meta_info']


    class TrapDestTable(object):
        """
        A list of trap destination entries.
        
        .. attribute:: trapdestentry
        
        	This entry includes a destination IP address to which to send traps for this community
        	**type**\: list of :py:class:`TrapDestEntry <ydk.models.rmon2.RMON2_MIB.RMON2MIB.TrapDestTable.TrapDestEntry>`
        
        

        """

        _prefix = 'rmon2-mib'
        _revision = '1996-05-27'

        def __init__(self):
            self.parent = None
            self.trapdestentry = YList()
            self.trapdestentry.parent = self
            self.trapdestentry.name = 'trapdestentry'


        class TrapDestEntry(object):
            """
            This entry includes a destination IP address to which to send
            traps for this community.
            
            .. attribute:: trapdestindex
            
            	A value that uniquely identifies this trapDestEntry
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: trapdestaddress
            
            	The address to send traps on behalf of this entry.  If the associated trapDestProtocol object is equal to ip(1), the encoding of this object is the same as the snmpUDPAddress textual convention in [RFC1906]\:   \-\- for a SnmpUDPAddress of length 6\:   \-\-   \-\- octets   contents        encoding   \-\-  1\-4     IP\-address      network\-byte order   \-\-  5\-6     UDP\-port        network\-byte order  If the associated trapDestProtocol object is equal to ipx(2), the encoding of this object is the same as the snmpIPXAddress textual convention in [RFC1906]\:   \-\- for a SnmpIPXAddress of length 12\:   \-\-   \-\- octets   contents            encoding   \-\-  1\-4     network\-number      network\-byte order   \-\-  5\-10    physical\-address    network\-byte order   \-\- 11\-12    socket\-number       network\-byte order  This object may not be modified if the associated      trapDestStatus object is equal to active(1)
            	**type**\: str
            
            .. attribute:: trapdestcommunity
            
            	A community to which this destination address belongs. This entry is associated with any eventEntries in the RMON      MIB whose value of eventCommunity is equal to the value of this object.  Every time an associated event entry sends a trap due to an event, that trap will be sent to each address in the trapDestTable with a trapDestCommunity equal to eventCommunity.  This object may not be modified if the associated trapDestStatus object is equal to active(1)
            	**type**\: str
            
            	**range:** 0..127
            
            .. attribute:: trapdestowner
            
            	The entity that configured this entry and is therefore using the resources assigned to it
            	**type**\: str
            
            	**range:** 0..127
            
            .. attribute:: trapdestprotocol
            
            	The protocol with which to send this trap
            	**type**\: :py:class:`TrapDestProtocol_Enum <ydk.models.rmon2.RMON2_MIB.RMON2MIB.TrapDestTable.TrapDestEntry.TrapDestProtocol_Enum>`
            
            .. attribute:: trapdeststatus
            
            	The status of this trap destination entry.  An entry may not exist in the active state unless all objects in the entry have an appropriate value
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            

            """

            _prefix = 'rmon2-mib'
            _revision = '1996-05-27'

            def __init__(self):
                self.parent = None
                self.trapdestindex = None
                self.trapdestaddress = None
                self.trapdestcommunity = None
                self.trapdestowner = None
                self.trapdestprotocol = None
                self.trapdeststatus = None

            class TrapDestProtocol_Enum(Enum):
                """
                TrapDestProtocol_Enum

                The protocol with which to send this trap.

                """

                IP = 1

                IPX = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.rmon2._meta import _RMON2_MIB as meta
                    return meta._meta_table['RMON2MIB.TrapDestTable.TrapDestEntry.TrapDestProtocol_Enum']


            @property
            def _common_path(self):
                if self.trapdestindex is None:
                    raise YPYDataValidationError('Key property trapdestindex is None')

                return '/RMON2-MIB:RMON2-MIB/RMON2-MIB:trapDestTable/RMON2-MIB:trapDestEntry[RMON2-MIB:trapDestIndex = ' + str(self.trapdestindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.trapdestindex is not None:
                    return True

                if self.trapdestaddress is not None:
                    return True

                if self.trapdestcommunity is not None:
                    return True

                if self.trapdestowner is not None:
                    return True

                if self.trapdestprotocol is not None:
                    return True

                if self.trapdeststatus is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.rmon2._meta import _RMON2_MIB as meta
                return meta._meta_table['RMON2MIB.TrapDestTable.TrapDestEntry']['meta_info']

        @property
        def _common_path(self):

            return '/RMON2-MIB:RMON2-MIB/RMON2-MIB:trapDestTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.trapdestentry is not None:
                for child_ref in self.trapdestentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.rmon2._meta import _RMON2_MIB as meta
            return meta._meta_table['RMON2MIB.TrapDestTable']['meta_info']


    class UsrHistoryControlTable(object):
        """
        A list of data\-collection configuration entries.
        
        .. attribute:: usrhistorycontrolentry
        
        	A list of parameters that set up a group of user\-defined MIB objects to be sampled periodically (called a bucket\-group).  For example, an instance of usrHistoryControlInterval might be named usrHistoryControlInterval.1
        	**type**\: list of :py:class:`UsrHistoryControlEntry <ydk.models.rmon2.RMON2_MIB.RMON2MIB.UsrHistoryControlTable.UsrHistoryControlEntry>`
        
        

        """

        _prefix = 'rmon2-mib'
        _revision = '1996-05-27'

        def __init__(self):
            self.parent = None
            self.usrhistorycontrolentry = YList()
            self.usrhistorycontrolentry.parent = self
            self.usrhistorycontrolentry.name = 'usrhistorycontrolentry'


        class UsrHistoryControlEntry(object):
            """
            A list of parameters that set up a group of user\-defined
            MIB objects to be sampled periodically (called a
            bucket\-group).
            
            For example, an instance of usrHistoryControlInterval
            might be named usrHistoryControlInterval.1
            
            .. attribute:: usrhistorycontrolindex
            
            	An index that uniquely identifies an entry in the usrHistoryControlTable.  Each such entry defines a set of samples at a particular interval for a specified set of MIB instances available from the managed system
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: usrhistorycontrolbucketsgranted
            
            	The number of discrete sampling intervals over which data shall be saved in the part of the usrHistoryTable associated with this usrHistoryControlEntry.  When the associated usrHistoryControlBucketsRequested      object is created or modified, the probe should set this object as closely to the requested value as is possible for the particular  probe implementation and available resources.  The probe must not lower this value except as a result of a modification to the associated usrHistoryControlBucketsRequested object.  The associated usrHistoryControlBucketsRequested object should be set before or at the same time as this object to allow the probe to accurately estimate the resources required for this usrHistoryControlEntry.  There will be times when the actual number of buckets associated with this entry is less than the value of this object.  In this case, at the end of each sampling interval, a new bucket will be added to the usrHistoryTable.  When the number of buckets reaches the value of this object and a new bucket is to be added to the usrHistoryTable, the oldest bucket associated with this usrHistoryControlEntry shall be deleted by the agent so that the new bucket can be added.  When the value of this object changes to a value less than the current value, entries are deleted from the usrHistoryTable associated with this usrHistoryControlEntry. Enough of the oldest of these entries shall be deleted by the agent so that their number remains less than or equal to the new value of this object.  When the value of this object changes to a value greater than the current value, the number of associated usrHistory entries may be allowed to grow
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: usrhistorycontrolbucketsrequested
            
            	The requested number of discrete time intervals over which data is to be saved in the part of the usrHistoryTable associated with this usrHistoryControlEntry.  When this object is created or modified, the probe should set usrHistoryControlBucketsGranted as closely to this object as is possible for the particular probe implementation and available resources
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: usrhistorycontrolinterval
            
            	The interval in seconds over which the data is sampled for each bucket in the part of the usrHistory table associated with this usrHistoryControlEntry.  Because the counters in a bucket may overflow at their maximum value with no indication, a prudent manager will take into account the possibility of overflow in any of      the associated counters. It is important to consider the minimum time in which any counter could overflow on a particular media type and set the usrHistoryControlInterval object to a value less than this interval.  This object may not be modified if the associated usrHistoryControlStatus object is equal to active(1)
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: usrhistorycontrolobjects
            
            	The number of MIB objects to be collected in the portion of usrHistoryTable associated with this usrHistoryControlEntry.  This object may not be modified if the associated instance of usrHistoryControlStatus is equal to active(1)
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: usrhistorycontrolowner
            
            	The entity that configured this entry and is therefore using the resources assigned to it
            	**type**\: str
            
            	**range:** 0..127
            
            .. attribute:: usrhistorycontrolstatus
            
            	The status of this variable history control entry.  An entry may not exist in the active state unless all objects in the entry have an appropriate value.  If this object is not equal to active(1), all associated entries in the usrHistoryTable shall be deleted
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            

            """

            _prefix = 'rmon2-mib'
            _revision = '1996-05-27'

            def __init__(self):
                self.parent = None
                self.usrhistorycontrolindex = None
                self.usrhistorycontrolbucketsgranted = None
                self.usrhistorycontrolbucketsrequested = None
                self.usrhistorycontrolinterval = None
                self.usrhistorycontrolobjects = None
                self.usrhistorycontrolowner = None
                self.usrhistorycontrolstatus = None

            @property
            def _common_path(self):
                if self.usrhistorycontrolindex is None:
                    raise YPYDataValidationError('Key property usrhistorycontrolindex is None')

                return '/RMON2-MIB:RMON2-MIB/RMON2-MIB:usrHistoryControlTable/RMON2-MIB:usrHistoryControlEntry[RMON2-MIB:usrHistoryControlIndex = ' + str(self.usrhistorycontrolindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.usrhistorycontrolindex is not None:
                    return True

                if self.usrhistorycontrolbucketsgranted is not None:
                    return True

                if self.usrhistorycontrolbucketsrequested is not None:
                    return True

                if self.usrhistorycontrolinterval is not None:
                    return True

                if self.usrhistorycontrolobjects is not None:
                    return True

                if self.usrhistorycontrolowner is not None:
                    return True

                if self.usrhistorycontrolstatus is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.rmon2._meta import _RMON2_MIB as meta
                return meta._meta_table['RMON2MIB.UsrHistoryControlTable.UsrHistoryControlEntry']['meta_info']

        @property
        def _common_path(self):

            return '/RMON2-MIB:RMON2-MIB/RMON2-MIB:usrHistoryControlTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.usrhistorycontrolentry is not None:
                for child_ref in self.usrhistorycontrolentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.rmon2._meta import _RMON2_MIB as meta
            return meta._meta_table['RMON2MIB.UsrHistoryControlTable']['meta_info']


    class UsrHistoryObjectTable(object):
        """
        A list of data\-collection configuration entries.
        
        .. attribute:: usrhistoryobjectentry
        
        	A list of MIB instances to be sampled periodically.  Entries in this table are created when an associated usrHistoryControlObjects object is created.  The usrHistoryControlIndex value in the index is that of the associated usrHistoryControlEntry.  For example, an instance of usrHistoryObjectVariable might be usrHistoryObjectVariable.1.3
        	**type**\: list of :py:class:`UsrHistoryObjectEntry <ydk.models.rmon2.RMON2_MIB.RMON2MIB.UsrHistoryObjectTable.UsrHistoryObjectEntry>`
        
        

        """

        _prefix = 'rmon2-mib'
        _revision = '1996-05-27'

        def __init__(self):
            self.parent = None
            self.usrhistoryobjectentry = YList()
            self.usrhistoryobjectentry.parent = self
            self.usrhistoryobjectentry.name = 'usrhistoryobjectentry'


        class UsrHistoryObjectEntry(object):
            """
            A list of MIB instances to be sampled periodically.
            
            Entries in this table are created when an associated
            usrHistoryControlObjects object is created.
            
            The usrHistoryControlIndex value in the index is
            that of the associated usrHistoryControlEntry.
            
            For example, an instance of usrHistoryObjectVariable might be
            usrHistoryObjectVariable.1.3
            
            .. attribute:: usrhistorycontrolindex
            
            	
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: usrhistoryobjectindex
            
            	An index used to uniquely identify an entry in the usrHistoryObject table.  Each such entry defines a MIB instance to be collected periodically
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: usrhistoryobjectsampletype
            
            	The method of sampling the selected variable for storage in the usrHistoryTable.  If the value of this object is absoluteValue(1), the value of the selected variable will be copied directly into the history bucket.  If the value of this object is deltaValue(2), the value of the selected variable at the last sample will be subtracted from the current value, and the difference will be stored in the history bucket. If the associated usrHistoryObjectVariable instance could not be obtained at the previous sample interval, then a delta sample is not possible, and the value of the associated usrHistoryValStatus object for this interval will be valueNotAvailable(1).  This object may not be modified if the associated usrHistoryControlStatus object is equal to active(1)
            	**type**\: :py:class:`UsrHistoryObjectSampleType_Enum <ydk.models.rmon2.RMON2_MIB.RMON2MIB.UsrHistoryObjectTable.UsrHistoryObjectEntry.UsrHistoryObjectSampleType_Enum>`
            
            .. attribute:: usrhistoryobjectvariable
            
            	The object identifier of the particular variable to be sampled.  Only variables that resolve to an ASN.1 primitive type of Integer32 (Integer32, Counter, Gauge, or TimeTicks) may be sampled.  Because SNMP access control is articulated entirely in terms of the contents of MIB views, no access control mechanism exists that can restrict the value of this object to identify only those objects that exist in a particular MIB view. Because there is thus no acceptable means of restricting the read access that could be obtained through the user history      mechanism, the probe must only grant write access to this object in those views that have read access to all objects on the probe.  During a set operation, if the supplied variable name is not available in the selected MIB view, a badValue error must be returned.  This object may not be modified if the associated usrHistoryControlStatus object is equal to active(1)
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            

            """

            _prefix = 'rmon2-mib'
            _revision = '1996-05-27'

            def __init__(self):
                self.parent = None
                self.usrhistorycontrolindex = None
                self.usrhistoryobjectindex = None
                self.usrhistoryobjectsampletype = None
                self.usrhistoryobjectvariable = None

            class UsrHistoryObjectSampleType_Enum(Enum):
                """
                UsrHistoryObjectSampleType_Enum

                The method of sampling the selected variable for storage in
                the usrHistoryTable.
                
                If the value of this object is absoluteValue(1), the value of
                the selected variable will be copied directly into the history
                bucket.
                
                If the value of this object is deltaValue(2), the value of the
                selected variable at the last sample will be subtracted from
                the current value, and the difference will be stored in the
                history bucket. If the associated usrHistoryObjectVariable
                instance could not be obtained at the previous sample
                interval, then a delta sample is not possible, and the value
                of the associated usrHistoryValStatus object for this interval
                will be valueNotAvailable(1).
                
                This object may not be modified if the associated
                usrHistoryControlStatus object is equal to active(1).

                """

                ABSOLUTEVALUE = 1

                DELTAVALUE = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.rmon2._meta import _RMON2_MIB as meta
                    return meta._meta_table['RMON2MIB.UsrHistoryObjectTable.UsrHistoryObjectEntry.UsrHistoryObjectSampleType_Enum']


            @property
            def _common_path(self):
                if self.usrhistorycontrolindex is None:
                    raise YPYDataValidationError('Key property usrhistorycontrolindex is None')
                if self.usrhistoryobjectindex is None:
                    raise YPYDataValidationError('Key property usrhistoryobjectindex is None')

                return '/RMON2-MIB:RMON2-MIB/RMON2-MIB:usrHistoryObjectTable/RMON2-MIB:usrHistoryObjectEntry[RMON2-MIB:usrHistoryControlIndex = ' + str(self.usrhistorycontrolindex) + '][RMON2-MIB:usrHistoryObjectIndex = ' + str(self.usrhistoryobjectindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.usrhistorycontrolindex is not None:
                    return True

                if self.usrhistoryobjectindex is not None:
                    return True

                if self.usrhistoryobjectsampletype is not None:
                    return True

                if self.usrhistoryobjectvariable is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.rmon2._meta import _RMON2_MIB as meta
                return meta._meta_table['RMON2MIB.UsrHistoryObjectTable.UsrHistoryObjectEntry']['meta_info']

        @property
        def _common_path(self):

            return '/RMON2-MIB:RMON2-MIB/RMON2-MIB:usrHistoryObjectTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.usrhistoryobjectentry is not None:
                for child_ref in self.usrhistoryobjectentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.rmon2._meta import _RMON2_MIB as meta
            return meta._meta_table['RMON2MIB.UsrHistoryObjectTable']['meta_info']


    class UsrHistoryTable(object):
        """
        A list of user defined history entries.
        
        .. attribute:: usrhistoryentry
        
        	A historical sample of user\-defined variables.  This sample is associated with the usrHistoryControlEntry which set up the parameters for a regular collection of these samples.  The usrHistoryControlIndex value in the index identifies the usrHistoryControlEntry on whose behalf this entry was created.  The usrHistoryObjectIndex value in the index identifies the usrHistoryObjectEntry on whose behalf this entry was created.  For example, an instance of usrHistoryAbsValue, which represents the 14th sample of a variable collected as specified by usrHistoryControlEntry.1 and usrHistoryObjectEntry.1.5, would be named usrHistoryAbsValue.1.14.5
        	**type**\: list of :py:class:`UsrHistoryEntry <ydk.models.rmon2.RMON2_MIB.RMON2MIB.UsrHistoryTable.UsrHistoryEntry>`
        
        

        """

        _prefix = 'rmon2-mib'
        _revision = '1996-05-27'

        def __init__(self):
            self.parent = None
            self.usrhistoryentry = YList()
            self.usrhistoryentry.parent = self
            self.usrhistoryentry.name = 'usrhistoryentry'


        class UsrHistoryEntry(object):
            """
            A historical sample of user\-defined variables.  This sample
            is associated with the usrHistoryControlEntry which set up the
            parameters for a regular collection of these samples.
            
            The usrHistoryControlIndex value in the index identifies the
            usrHistoryControlEntry on whose behalf this entry was created.
            
            The usrHistoryObjectIndex value in the index identifies the
            usrHistoryObjectEntry on whose behalf this entry was created.
            
            For example, an instance of usrHistoryAbsValue, which represents
            the 14th sample of a variable collected as specified by
            usrHistoryControlEntry.1 and usrHistoryObjectEntry.1.5,
            would be named usrHistoryAbsValue.1.14.5
            
            .. attribute:: usrhistorycontrolindex
            
            	
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: usrhistoryobjectindex
            
            	
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: usrhistorysampleindex
            
            	An index that uniquely identifies the particular sample this entry represents among all samples associated with the same usrHistoryControlEntry. This index starts at 1 and increases by one as each new sample is taken
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: usrhistoryabsvalue
            
            	The absolute value (i.e. unsigned value) of the user\-specified statistic during the last sampling period. The value during the current sampling period is not made available until the period is completed.  To obtain the true value for this sampling interval, the associated instance of usrHistoryValStatus must be checked, and usrHistoryAbsValue adjusted as necessary.  If the MIB instance could not be accessed during the sampling interval, then this object will have a value of zero and the associated instance of usrHistoryValStatus will be set to 'valueNotAvailable(1)'
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: usrhistoryintervalend
            
            	The value of sysUpTime at the end of the interval over which this sample was measured
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: usrhistoryintervalstart
            
            	The value of sysUpTime at the start of the interval over which this sample was measured.  If the probe keeps track of the time of day, it should start the first sample of the history at a time such that when the next hour of the day begins, a sample is started at that instant.  Note that following this rule may require the probe to delay collecting the first sample of the history, as each sample must be of the same interval. Also note that the sample which is currently being collected is not accessible in this table until the end of its interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: usrhistoryvalstatus
            
            	This object indicates the validity and sign of the data in the associated instance of usrHistoryAbsValue.  If the MIB instance could not be accessed during the sampling interval, then 'valueNotAvailable(1)' will be returned.  If the sample is valid and actual value of the sample is greater than or equal to zero then 'valuePositive(2)' is returned.  If the sample is valid and the actual value of the sample is less than zero, 'valueNegative(3)' will be returned. The associated instance of usrHistoryAbsValue should be multiplied by \-1 to obtain the true sample value
            	**type**\: :py:class:`UsrHistoryValStatus_Enum <ydk.models.rmon2.RMON2_MIB.RMON2MIB.UsrHistoryTable.UsrHistoryEntry.UsrHistoryValStatus_Enum>`
            
            

            """

            _prefix = 'rmon2-mib'
            _revision = '1996-05-27'

            def __init__(self):
                self.parent = None
                self.usrhistorycontrolindex = None
                self.usrhistoryobjectindex = None
                self.usrhistorysampleindex = None
                self.usrhistoryabsvalue = None
                self.usrhistoryintervalend = None
                self.usrhistoryintervalstart = None
                self.usrhistoryvalstatus = None

            class UsrHistoryValStatus_Enum(Enum):
                """
                UsrHistoryValStatus_Enum

                This object indicates the validity and sign of the data in
                the associated instance of usrHistoryAbsValue.
                
                If the MIB instance could not be accessed during the sampling
                interval, then 'valueNotAvailable(1)' will be returned.
                
                If the sample is valid and actual value of the sample is
                greater than or equal to zero then 'valuePositive(2)' is
                returned.
                
                If the sample is valid and the actual value of the sample is
                less than zero, 'valueNegative(3)' will be returned. The
                associated instance of usrHistoryAbsValue should be multiplied
                by \-1 to obtain the true sample value.

                """

                VALUENOTAVAILABLE = 1

                VALUEPOSITIVE = 2

                VALUENEGATIVE = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.rmon2._meta import _RMON2_MIB as meta
                    return meta._meta_table['RMON2MIB.UsrHistoryTable.UsrHistoryEntry.UsrHistoryValStatus_Enum']


            @property
            def _common_path(self):
                if self.usrhistorycontrolindex is None:
                    raise YPYDataValidationError('Key property usrhistorycontrolindex is None')
                if self.usrhistoryobjectindex is None:
                    raise YPYDataValidationError('Key property usrhistoryobjectindex is None')
                if self.usrhistorysampleindex is None:
                    raise YPYDataValidationError('Key property usrhistorysampleindex is None')

                return '/RMON2-MIB:RMON2-MIB/RMON2-MIB:usrHistoryTable/RMON2-MIB:usrHistoryEntry[RMON2-MIB:usrHistoryControlIndex = ' + str(self.usrhistorycontrolindex) + '][RMON2-MIB:usrHistoryObjectIndex = ' + str(self.usrhistoryobjectindex) + '][RMON2-MIB:usrHistorySampleIndex = ' + str(self.usrhistorysampleindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.usrhistorycontrolindex is not None:
                    return True

                if self.usrhistoryobjectindex is not None:
                    return True

                if self.usrhistorysampleindex is not None:
                    return True

                if self.usrhistoryabsvalue is not None:
                    return True

                if self.usrhistoryintervalend is not None:
                    return True

                if self.usrhistoryintervalstart is not None:
                    return True

                if self.usrhistoryvalstatus is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.rmon2._meta import _RMON2_MIB as meta
                return meta._meta_table['RMON2MIB.UsrHistoryTable.UsrHistoryEntry']['meta_info']

        @property
        def _common_path(self):

            return '/RMON2-MIB:RMON2-MIB/RMON2-MIB:usrHistoryTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.usrhistoryentry is not None:
                for child_ref in self.usrhistoryentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.rmon2._meta import _RMON2_MIB as meta
            return meta._meta_table['RMON2MIB.UsrHistoryTable']['meta_info']

    @property
    def _common_path(self):

        return '/RMON2-MIB:RMON2-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.addressmap is not None and self.addressmap._has_data():
            return True

        if self.addressmap is not None and self.addressmap.is_presence():
            return True

        if self.addressmapcontroltable is not None and self.addressmapcontroltable._has_data():
            return True

        if self.addressmapcontroltable is not None and self.addressmapcontroltable.is_presence():
            return True

        if self.addressmaptable is not None and self.addressmaptable._has_data():
            return True

        if self.addressmaptable is not None and self.addressmaptable.is_presence():
            return True

        if self.alhosttable is not None and self.alhosttable._has_data():
            return True

        if self.alhosttable is not None and self.alhosttable.is_presence():
            return True

        if self.almatrixdstable is not None and self.almatrixdstable._has_data():
            return True

        if self.almatrixdstable is not None and self.almatrixdstable.is_presence():
            return True

        if self.almatrixsdtable is not None and self.almatrixsdtable._has_data():
            return True

        if self.almatrixsdtable is not None and self.almatrixsdtable.is_presence():
            return True

        if self.almatrixtopncontroltable is not None and self.almatrixtopncontroltable._has_data():
            return True

        if self.almatrixtopncontroltable is not None and self.almatrixtopncontroltable.is_presence():
            return True

        if self.almatrixtopntable is not None and self.almatrixtopntable._has_data():
            return True

        if self.almatrixtopntable is not None and self.almatrixtopntable.is_presence():
            return True

        if self.hlhostcontroltable is not None and self.hlhostcontroltable._has_data():
            return True

        if self.hlhostcontroltable is not None and self.hlhostcontroltable.is_presence():
            return True

        if self.hlmatrixcontroltable is not None and self.hlmatrixcontroltable._has_data():
            return True

        if self.hlmatrixcontroltable is not None and self.hlmatrixcontroltable.is_presence():
            return True

        if self.netconfigtable is not None and self.netconfigtable._has_data():
            return True

        if self.netconfigtable is not None and self.netconfigtable.is_presence():
            return True

        if self.nlhosttable is not None and self.nlhosttable._has_data():
            return True

        if self.nlhosttable is not None and self.nlhosttable.is_presence():
            return True

        if self.nlmatrixdstable is not None and self.nlmatrixdstable._has_data():
            return True

        if self.nlmatrixdstable is not None and self.nlmatrixdstable.is_presence():
            return True

        if self.nlmatrixsdtable is not None and self.nlmatrixsdtable._has_data():
            return True

        if self.nlmatrixsdtable is not None and self.nlmatrixsdtable.is_presence():
            return True

        if self.nlmatrixtopncontroltable is not None and self.nlmatrixtopncontroltable._has_data():
            return True

        if self.nlmatrixtopncontroltable is not None and self.nlmatrixtopncontroltable.is_presence():
            return True

        if self.nlmatrixtopntable is not None and self.nlmatrixtopntable._has_data():
            return True

        if self.nlmatrixtopntable is not None and self.nlmatrixtopntable.is_presence():
            return True

        if self.probeconfig is not None and self.probeconfig._has_data():
            return True

        if self.probeconfig is not None and self.probeconfig.is_presence():
            return True

        if self.protocoldir is not None and self.protocoldir._has_data():
            return True

        if self.protocoldir is not None and self.protocoldir.is_presence():
            return True

        if self.protocoldirtable is not None and self.protocoldirtable._has_data():
            return True

        if self.protocoldirtable is not None and self.protocoldirtable.is_presence():
            return True

        if self.protocoldistcontroltable is not None and self.protocoldistcontroltable._has_data():
            return True

        if self.protocoldistcontroltable is not None and self.protocoldistcontroltable.is_presence():
            return True

        if self.protocoldiststatstable is not None and self.protocoldiststatstable._has_data():
            return True

        if self.protocoldiststatstable is not None and self.protocoldiststatstable.is_presence():
            return True

        if self.serialconfigtable is not None and self.serialconfigtable._has_data():
            return True

        if self.serialconfigtable is not None and self.serialconfigtable.is_presence():
            return True

        if self.serialconnectiontable is not None and self.serialconnectiontable._has_data():
            return True

        if self.serialconnectiontable is not None and self.serialconnectiontable.is_presence():
            return True

        if self.trapdesttable is not None and self.trapdesttable._has_data():
            return True

        if self.trapdesttable is not None and self.trapdesttable.is_presence():
            return True

        if self.usrhistorycontroltable is not None and self.usrhistorycontroltable._has_data():
            return True

        if self.usrhistorycontroltable is not None and self.usrhistorycontroltable.is_presence():
            return True

        if self.usrhistoryobjecttable is not None and self.usrhistoryobjecttable._has_data():
            return True

        if self.usrhistoryobjecttable is not None and self.usrhistoryobjecttable.is_presence():
            return True

        if self.usrhistorytable is not None and self.usrhistorytable._has_data():
            return True

        if self.usrhistorytable is not None and self.usrhistorytable.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.rmon2._meta import _RMON2_MIB as meta
        return meta._meta_table['RMON2MIB']['meta_info']


