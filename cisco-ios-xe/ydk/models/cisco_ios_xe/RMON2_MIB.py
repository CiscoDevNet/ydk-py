""" RMON2_MIB 

The MIB module for managing remote monitoring
device implementations. This MIB module
augments the original RMON MIB as specified in
RFC 1757.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class RMON2MIB(Entity):
    """
    
    
    .. attribute:: addressmap
    
    	
    	**type**\:   :py:class:`Addressmap <ydk.models.cisco_ios_xe.RMON2_MIB.RMON2MIB.Addressmap>`
    
    .. attribute:: addressmapcontroltable
    
    	A table to control the collection of network layer address to physical address to interface mappings.  Note that this is not like the typical RMON controlTable and dataTable in which each entry creates its own data table.  Each entry in this table enables the discovery of addresses on a new interface and the placement of address mappings into the central addressMapTable.  Implementations are encouraged to add an entry per monitored interface upon initialization so that a default collection of address mappings is available
    	**type**\:   :py:class:`Addressmapcontroltable <ydk.models.cisco_ios_xe.RMON2_MIB.RMON2MIB.Addressmapcontroltable>`
    
    .. attribute:: addressmaptable
    
    	A table of network layer address to physical address to interface mappings.  The probe will add entries to this table based on the source MAC and network addresses seen in packets without MAC\-level errors. The probe will populate this table for all protocols in the protocol directory table whose value of protocolDirAddressMapConfig is equal to supportedOn(3), and will delete any entries whose protocolDirEntry is deleted or has a protocolDirAddressMapConfig value of supportedOff(2)
    	**type**\:   :py:class:`Addressmaptable <ydk.models.cisco_ios_xe.RMON2_MIB.RMON2MIB.Addressmaptable>`
    
    .. attribute:: alhosttable
    
    	A collection of statistics for a particular protocol from a particular network address that has been discovered on an interface of this device.  The probe will populate this table for all protocols in the protocol directory table whose value of protocolDirHostConfig is equal to supportedOn(3), and will delete any entries whose protocolDirEntry is deleted or has a protocolDirHostConfig value of supportedOff(2).  The probe will add to this table all addresses seen as the source or destination address in all packets with no MAC errors, and will increment octet and packet counts in the table for all packets with no MAC errors.  Further, entries will only be added to this table if their address exists in the nlHostTable and will be deleted from this table if their address is deleted from the nlHostTable
    	**type**\:   :py:class:`Alhosttable <ydk.models.cisco_ios_xe.RMON2_MIB.RMON2MIB.Alhosttable>`
    
    .. attribute:: almatrixdstable
    
    	A list of application traffic matrix entries which collect statistics for conversations of a particular protocol between two network\-level addresses.  This table is indexed first by the destination address and then by the source address to make it convenient to collect all statistics to a particular address.  The probe will populate this table for all protocols in the protocol directory table whose value of protocolDirMatrixConfig is equal to supportedOn(3), and will delete any entries whose protocolDirEntry is deleted or has a protocolDirMatrixConfig value of supportedOff(2).  The probe will add to this table all pairs of addresses for all protocols seen in all packets with no MAC errors, and will increment octet and packet counts in the table for all packets with no MAC errors.  Further, entries will only be added to this table if their address pair exists in the nlMatrixDSTable and will be deleted from this table if the address pair is deleted from the nlMatrixDSTable
    	**type**\:   :py:class:`Almatrixdstable <ydk.models.cisco_ios_xe.RMON2_MIB.RMON2MIB.Almatrixdstable>`
    
    .. attribute:: almatrixsdtable
    
    	A list of application traffic matrix entries which collect      statistics for conversations of a particular protocol between two network\-level addresses.  This table is indexed first by the source address and then by the destination address to make it convenient to collect all statistics from a particular address.  The probe will populate this table for all protocols in the protocol directory table whose value of protocolDirMatrixConfig is equal to supportedOn(3), and will delete any entries whose protocolDirEntry is deleted or has a protocolDirMatrixConfig value of supportedOff(2).  The probe will add to this table all pairs of addresses for all protocols seen in all packets with no MAC errors, and will increment octet and packet counts in the table for all packets with no MAC errors.  Further, entries will only be added to this table if their address pair exists in the nlMatrixSDTable and will be deleted from this table if the address pair is deleted from the nlMatrixSDTable
    	**type**\:   :py:class:`Almatrixsdtable <ydk.models.cisco_ios_xe.RMON2_MIB.RMON2MIB.Almatrixsdtable>`
    
    .. attribute:: almatrixtopncontroltable
    
    	A set of parameters that control the creation of a report of the top N matrix entries according to a selected metric
    	**type**\:   :py:class:`Almatrixtopncontroltable <ydk.models.cisco_ios_xe.RMON2_MIB.RMON2MIB.Almatrixtopncontroltable>`
    
    .. attribute:: almatrixtopntable
    
    	A set of statistics for those application layer matrix entries that have counted the highest number of octets or packets
    	**type**\:   :py:class:`Almatrixtopntable <ydk.models.cisco_ios_xe.RMON2_MIB.RMON2MIB.Almatrixtopntable>`
    
    .. attribute:: hlhostcontroltable
    
    	A list of higher layer (i.e. non\-MAC) host table control entries.  These entries will enable the collection of the network and application level host tables indexed by network addresses. Both the network and application level host tables are controlled by this table is so that they will both be created and deleted at the same time, further increasing the ease with which they can be implemented as a single datastore (note that if an implementation stores application layer host records in memory, it can derive network layer host records from them).  Entries in the nlHostTable will be created on behalf of each entry in this table. Additionally, if this probe implements the alHostTable, entries in the alHostTable will be created on behalf of each entry in this table.  Implementations are encouraged to add an entry per monitored interface upon initialization so that a default collection of host statistics is available
    	**type**\:   :py:class:`Hlhostcontroltable <ydk.models.cisco_ios_xe.RMON2_MIB.RMON2MIB.Hlhostcontroltable>`
    
    .. attribute:: hlmatrixcontroltable
    
    	A list of higher layer (i.e. non\-MAC) matrix control entries.  These entries will enable the collection of the network and application level matrix tables containing conversation statistics indexed by pairs of network addresses. Both the network and application level matrix tables are controlled by this table is so that they will both be created and deleted at the same time, further increasing the ease with which they can be implemented as a single datastore (note that if an implementation stores application layer matrix records in memory, it can derive network layer matrix records from them).  Entries in the nlMatrixSDTable and nlMatrixDSTable will be created on behalf of each entry in this table.  Additionally, if this probe implements the alMatrix tables, entries in the alMatrix tables will be created on behalf of each entry in this table
    	**type**\:   :py:class:`Hlmatrixcontroltable <ydk.models.cisco_ios_xe.RMON2_MIB.RMON2MIB.Hlmatrixcontroltable>`
    
    .. attribute:: netconfigtable
    
    	A table of netConfigEntries
    	**type**\:   :py:class:`Netconfigtable <ydk.models.cisco_ios_xe.RMON2_MIB.RMON2MIB.Netconfigtable>`
    
    .. attribute:: nlhosttable
    
    	A collection of statistics for a particular network layer address that has been discovered on an interface of this device.  The probe will populate this table for all network layer protocols in the protocol directory table whose value of protocolDirHostConfig is equal to supportedOn(3), and will delete any entries whose protocolDirEntry is deleted or has a protocolDirHostConfig value of supportedOff(2).  The probe will add to this table all addresses seen as the source or destination address in all packets with no MAC errors, and will increment octet and packet counts in the table for all packets with no MAC errors
    	**type**\:   :py:class:`Nlhosttable <ydk.models.cisco_ios_xe.RMON2_MIB.RMON2MIB.Nlhosttable>`
    
    .. attribute:: nlmatrixdstable
    
    	A list of traffic matrix entries which collect statistics for conversations between two network\-level addresses.  This table is indexed first by the destination address and then by the source address to make it convenient to collect all conversations to a particular address.  The probe will populate this table for all network layer protocols in the protocol directory table whose value of protocolDirMatrixConfig is equal to supportedOn(3), and will delete any entries whose protocolDirEntry is deleted or has a protocolDirMatrixConfig value of supportedOff(2).  The probe will add to this table all pairs of addresses seen in all packets with no MAC errors, and will increment      octet and packet counts in the table for all packets with no MAC errors.  Further, this table will only contain entries that have a corresponding entry in the nlMatrixSDTable with the same source address and destination address
    	**type**\:   :py:class:`Nlmatrixdstable <ydk.models.cisco_ios_xe.RMON2_MIB.RMON2MIB.Nlmatrixdstable>`
    
    .. attribute:: nlmatrixsdtable
    
    	A list of traffic matrix entries which collect statistics for conversations between two network\-level addresses.  This table is indexed first by the source address and then by the destination address to make it convenient to collect all conversations from a particular address.  The probe will populate this table for all network layer protocols in the protocol directory table whose value of protocolDirMatrixConfig is equal to supportedOn(3), and will delete any entries whose protocolDirEntry is deleted or has a protocolDirMatrixConfig value of supportedOff(2).      The probe will add to this table all pairs of addresses seen in all packets with no MAC errors, and will increment octet and packet counts in the table for all packets with no MAC errors.  Further, this table will only contain entries that have a corresponding entry in the nlMatrixDSTable with the same source address and destination address
    	**type**\:   :py:class:`Nlmatrixsdtable <ydk.models.cisco_ios_xe.RMON2_MIB.RMON2MIB.Nlmatrixsdtable>`
    
    .. attribute:: nlmatrixtopncontroltable
    
    	A set of parameters that control the creation of a report of the top N matrix entries according to a selected metric
    	**type**\:   :py:class:`Nlmatrixtopncontroltable <ydk.models.cisco_ios_xe.RMON2_MIB.RMON2MIB.Nlmatrixtopncontroltable>`
    
    .. attribute:: nlmatrixtopntable
    
    	A set of statistics for those network layer matrix entries that have counted the highest number of octets or packets
    	**type**\:   :py:class:`Nlmatrixtopntable <ydk.models.cisco_ios_xe.RMON2_MIB.RMON2MIB.Nlmatrixtopntable>`
    
    .. attribute:: probeconfig
    
    	
    	**type**\:   :py:class:`Probeconfig <ydk.models.cisco_ios_xe.RMON2_MIB.RMON2MIB.Probeconfig>`
    
    .. attribute:: protocoldir
    
    	
    	**type**\:   :py:class:`Protocoldir <ydk.models.cisco_ios_xe.RMON2_MIB.RMON2MIB.Protocoldir>`
    
    .. attribute:: protocoldirtable
    
    	This table lists the protocols that this agent has the capability to decode and count.  There is one entry in this table for each such protocol.  These protocols represent different network layer, transport layer, and higher\-layer protocols.  The agent should boot up with this table preconfigured with those protocols that it knows about and wishes to monitor.  Implementations are strongly encouraged to support protocols higher than the network layer (at least for the protocol distribution group), even for implementations that don't support the application layer groups
    	**type**\:   :py:class:`Protocoldirtable <ydk.models.cisco_ios_xe.RMON2_MIB.RMON2MIB.Protocoldirtable>`
    
    .. attribute:: protocoldistcontroltable
    
    	Controls the setup of protocol type distribution statistics tables.  Implementations are encouraged to add an entry per monitored interface upon initialization so that a default collection of protocol statistics is available.  Rationale\: This table controls collection of very basic statistics for any or all of the protocols detected on a given interface. An NMS can use this table to quickly determine bandwidth allocation utilized by different protocols.  A media\-specific statistics collection could also be configured (e.g. etherStats, trPStats) to easily obtain total frame, octet, and droppedEvents for the same interface
    	**type**\:   :py:class:`Protocoldistcontroltable <ydk.models.cisco_ios_xe.RMON2_MIB.RMON2MIB.Protocoldistcontroltable>`
    
    .. attribute:: protocoldiststatstable
    
    	An entry is made in this table for every protocol in the      protocolDirTable which has been seen in at least one packet. Counters are updated in this table for every protocol type that is encountered when parsing a packet, but no counters are updated for packets with MAC\-layer errors.  Note that if a protocolDirEntry is deleted, all associated entries in this table are removed
    	**type**\:   :py:class:`Protocoldiststatstable <ydk.models.cisco_ios_xe.RMON2_MIB.RMON2MIB.Protocoldiststatstable>`
    
    .. attribute:: serialconfigtable
    
    	A table of serial interface configuration entries.  This data will be stored in non\-volatile memory and preserved across probe resets or power loss
    	**type**\:   :py:class:`Serialconfigtable <ydk.models.cisco_ios_xe.RMON2_MIB.RMON2MIB.Serialconfigtable>`
    
    .. attribute:: serialconnectiontable
    
    	A list of serialConnectionEntries
    	**type**\:   :py:class:`Serialconnectiontable <ydk.models.cisco_ios_xe.RMON2_MIB.RMON2MIB.Serialconnectiontable>`
    
    .. attribute:: trapdesttable
    
    	A list of trap destination entries
    	**type**\:   :py:class:`Trapdesttable <ydk.models.cisco_ios_xe.RMON2_MIB.RMON2MIB.Trapdesttable>`
    
    .. attribute:: usrhistorycontroltable
    
    	A list of data\-collection configuration entries
    	**type**\:   :py:class:`Usrhistorycontroltable <ydk.models.cisco_ios_xe.RMON2_MIB.RMON2MIB.Usrhistorycontroltable>`
    
    .. attribute:: usrhistoryobjecttable
    
    	A list of data\-collection configuration entries
    	**type**\:   :py:class:`Usrhistoryobjecttable <ydk.models.cisco_ios_xe.RMON2_MIB.RMON2MIB.Usrhistoryobjecttable>`
    
    .. attribute:: usrhistorytable
    
    	A list of user defined history entries
    	**type**\:   :py:class:`Usrhistorytable <ydk.models.cisco_ios_xe.RMON2_MIB.RMON2MIB.Usrhistorytable>`
    
    

    """

    _prefix = 'RMON2-MIB'
    _revision = '1996-05-27'

    def __init__(self):
        super(RMON2MIB, self).__init__()
        self._top_entity = None

        self.yang_name = "RMON2-MIB"
        self.yang_parent_name = "RMON2-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"addressMap" : ("addressmap", RMON2MIB.Addressmap), "addressMapControlTable" : ("addressmapcontroltable", RMON2MIB.Addressmapcontroltable), "addressMapTable" : ("addressmaptable", RMON2MIB.Addressmaptable), "alHostTable" : ("alhosttable", RMON2MIB.Alhosttable), "alMatrixDSTable" : ("almatrixdstable", RMON2MIB.Almatrixdstable), "alMatrixSDTable" : ("almatrixsdtable", RMON2MIB.Almatrixsdtable), "alMatrixTopNControlTable" : ("almatrixtopncontroltable", RMON2MIB.Almatrixtopncontroltable), "alMatrixTopNTable" : ("almatrixtopntable", RMON2MIB.Almatrixtopntable), "hlHostControlTable" : ("hlhostcontroltable", RMON2MIB.Hlhostcontroltable), "hlMatrixControlTable" : ("hlmatrixcontroltable", RMON2MIB.Hlmatrixcontroltable), "netConfigTable" : ("netconfigtable", RMON2MIB.Netconfigtable), "nlHostTable" : ("nlhosttable", RMON2MIB.Nlhosttable), "nlMatrixDSTable" : ("nlmatrixdstable", RMON2MIB.Nlmatrixdstable), "nlMatrixSDTable" : ("nlmatrixsdtable", RMON2MIB.Nlmatrixsdtable), "nlMatrixTopNControlTable" : ("nlmatrixtopncontroltable", RMON2MIB.Nlmatrixtopncontroltable), "nlMatrixTopNTable" : ("nlmatrixtopntable", RMON2MIB.Nlmatrixtopntable), "probeConfig" : ("probeconfig", RMON2MIB.Probeconfig), "protocolDir" : ("protocoldir", RMON2MIB.Protocoldir), "protocolDirTable" : ("protocoldirtable", RMON2MIB.Protocoldirtable), "protocolDistControlTable" : ("protocoldistcontroltable", RMON2MIB.Protocoldistcontroltable), "protocolDistStatsTable" : ("protocoldiststatstable", RMON2MIB.Protocoldiststatstable), "serialConfigTable" : ("serialconfigtable", RMON2MIB.Serialconfigtable), "serialConnectionTable" : ("serialconnectiontable", RMON2MIB.Serialconnectiontable), "trapDestTable" : ("trapdesttable", RMON2MIB.Trapdesttable), "usrHistoryControlTable" : ("usrhistorycontroltable", RMON2MIB.Usrhistorycontroltable), "usrHistoryObjectTable" : ("usrhistoryobjecttable", RMON2MIB.Usrhistoryobjecttable), "usrHistoryTable" : ("usrhistorytable", RMON2MIB.Usrhistorytable)}
        self._child_list_classes = {}

        self.addressmap = RMON2MIB.Addressmap()
        self.addressmap.parent = self
        self._children_name_map["addressmap"] = "addressMap"
        self._children_yang_names.add("addressMap")

        self.addressmapcontroltable = RMON2MIB.Addressmapcontroltable()
        self.addressmapcontroltable.parent = self
        self._children_name_map["addressmapcontroltable"] = "addressMapControlTable"
        self._children_yang_names.add("addressMapControlTable")

        self.addressmaptable = RMON2MIB.Addressmaptable()
        self.addressmaptable.parent = self
        self._children_name_map["addressmaptable"] = "addressMapTable"
        self._children_yang_names.add("addressMapTable")

        self.alhosttable = RMON2MIB.Alhosttable()
        self.alhosttable.parent = self
        self._children_name_map["alhosttable"] = "alHostTable"
        self._children_yang_names.add("alHostTable")

        self.almatrixdstable = RMON2MIB.Almatrixdstable()
        self.almatrixdstable.parent = self
        self._children_name_map["almatrixdstable"] = "alMatrixDSTable"
        self._children_yang_names.add("alMatrixDSTable")

        self.almatrixsdtable = RMON2MIB.Almatrixsdtable()
        self.almatrixsdtable.parent = self
        self._children_name_map["almatrixsdtable"] = "alMatrixSDTable"
        self._children_yang_names.add("alMatrixSDTable")

        self.almatrixtopncontroltable = RMON2MIB.Almatrixtopncontroltable()
        self.almatrixtopncontroltable.parent = self
        self._children_name_map["almatrixtopncontroltable"] = "alMatrixTopNControlTable"
        self._children_yang_names.add("alMatrixTopNControlTable")

        self.almatrixtopntable = RMON2MIB.Almatrixtopntable()
        self.almatrixtopntable.parent = self
        self._children_name_map["almatrixtopntable"] = "alMatrixTopNTable"
        self._children_yang_names.add("alMatrixTopNTable")

        self.hlhostcontroltable = RMON2MIB.Hlhostcontroltable()
        self.hlhostcontroltable.parent = self
        self._children_name_map["hlhostcontroltable"] = "hlHostControlTable"
        self._children_yang_names.add("hlHostControlTable")

        self.hlmatrixcontroltable = RMON2MIB.Hlmatrixcontroltable()
        self.hlmatrixcontroltable.parent = self
        self._children_name_map["hlmatrixcontroltable"] = "hlMatrixControlTable"
        self._children_yang_names.add("hlMatrixControlTable")

        self.netconfigtable = RMON2MIB.Netconfigtable()
        self.netconfigtable.parent = self
        self._children_name_map["netconfigtable"] = "netConfigTable"
        self._children_yang_names.add("netConfigTable")

        self.nlhosttable = RMON2MIB.Nlhosttable()
        self.nlhosttable.parent = self
        self._children_name_map["nlhosttable"] = "nlHostTable"
        self._children_yang_names.add("nlHostTable")

        self.nlmatrixdstable = RMON2MIB.Nlmatrixdstable()
        self.nlmatrixdstable.parent = self
        self._children_name_map["nlmatrixdstable"] = "nlMatrixDSTable"
        self._children_yang_names.add("nlMatrixDSTable")

        self.nlmatrixsdtable = RMON2MIB.Nlmatrixsdtable()
        self.nlmatrixsdtable.parent = self
        self._children_name_map["nlmatrixsdtable"] = "nlMatrixSDTable"
        self._children_yang_names.add("nlMatrixSDTable")

        self.nlmatrixtopncontroltable = RMON2MIB.Nlmatrixtopncontroltable()
        self.nlmatrixtopncontroltable.parent = self
        self._children_name_map["nlmatrixtopncontroltable"] = "nlMatrixTopNControlTable"
        self._children_yang_names.add("nlMatrixTopNControlTable")

        self.nlmatrixtopntable = RMON2MIB.Nlmatrixtopntable()
        self.nlmatrixtopntable.parent = self
        self._children_name_map["nlmatrixtopntable"] = "nlMatrixTopNTable"
        self._children_yang_names.add("nlMatrixTopNTable")

        self.probeconfig = RMON2MIB.Probeconfig()
        self.probeconfig.parent = self
        self._children_name_map["probeconfig"] = "probeConfig"
        self._children_yang_names.add("probeConfig")

        self.protocoldir = RMON2MIB.Protocoldir()
        self.protocoldir.parent = self
        self._children_name_map["protocoldir"] = "protocolDir"
        self._children_yang_names.add("protocolDir")

        self.protocoldirtable = RMON2MIB.Protocoldirtable()
        self.protocoldirtable.parent = self
        self._children_name_map["protocoldirtable"] = "protocolDirTable"
        self._children_yang_names.add("protocolDirTable")

        self.protocoldistcontroltable = RMON2MIB.Protocoldistcontroltable()
        self.protocoldistcontroltable.parent = self
        self._children_name_map["protocoldistcontroltable"] = "protocolDistControlTable"
        self._children_yang_names.add("protocolDistControlTable")

        self.protocoldiststatstable = RMON2MIB.Protocoldiststatstable()
        self.protocoldiststatstable.parent = self
        self._children_name_map["protocoldiststatstable"] = "protocolDistStatsTable"
        self._children_yang_names.add("protocolDistStatsTable")

        self.serialconfigtable = RMON2MIB.Serialconfigtable()
        self.serialconfigtable.parent = self
        self._children_name_map["serialconfigtable"] = "serialConfigTable"
        self._children_yang_names.add("serialConfigTable")

        self.serialconnectiontable = RMON2MIB.Serialconnectiontable()
        self.serialconnectiontable.parent = self
        self._children_name_map["serialconnectiontable"] = "serialConnectionTable"
        self._children_yang_names.add("serialConnectionTable")

        self.trapdesttable = RMON2MIB.Trapdesttable()
        self.trapdesttable.parent = self
        self._children_name_map["trapdesttable"] = "trapDestTable"
        self._children_yang_names.add("trapDestTable")

        self.usrhistorycontroltable = RMON2MIB.Usrhistorycontroltable()
        self.usrhistorycontroltable.parent = self
        self._children_name_map["usrhistorycontroltable"] = "usrHistoryControlTable"
        self._children_yang_names.add("usrHistoryControlTable")

        self.usrhistoryobjecttable = RMON2MIB.Usrhistoryobjecttable()
        self.usrhistoryobjecttable.parent = self
        self._children_name_map["usrhistoryobjecttable"] = "usrHistoryObjectTable"
        self._children_yang_names.add("usrHistoryObjectTable")

        self.usrhistorytable = RMON2MIB.Usrhistorytable()
        self.usrhistorytable.parent = self
        self._children_name_map["usrhistorytable"] = "usrHistoryTable"
        self._children_yang_names.add("usrHistoryTable")
        self._segment_path = lambda: "RMON2-MIB:RMON2-MIB"


    class Addressmap(Entity):
        """
        
        
        .. attribute:: addressmapdeletes
        
        	The number of times an address mapping entry has been deleted from the addressMapTable (for any reason).  If an entry is deleted, then inserted, and then deleted, this counter will be incremented by 2.  Note that the table size can be determined by subtracting addressMapDeletes from addressMapInserts
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: addressmapinserts
        
        	The number of times an address mapping entry has been inserted into the addressMapTable.  If an entry is inserted, then deleted, and then inserted, this counter will be incremented by 2.  Note that the table size can be determined by subtracting addressMapDeletes from addressMapInserts
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: addressmapmaxdesiredentries
        
        	The maximum number of entries that are desired in the addressMapTable. The probe will not create more than this number of entries in the table, but may choose to create fewer entries in this table for any reason including the lack of resources.  If this object is set to a value less than the current number of entries, enough entries are chosen in an implementation\-dependent manner and deleted so that the number of entries in the table equals the value of this object.  If this value is set to \-1, the probe may create any number of entries in this table.  This object may be used to control how resources are allocated on the probe for the various RMON functions
        	**type**\:  int
        
        	**range:** \-1..2147483647
        
        

        """

        _prefix = 'RMON2-MIB'
        _revision = '1996-05-27'

        def __init__(self):
            super(RMON2MIB.Addressmap, self).__init__()

            self.yang_name = "addressMap"
            self.yang_parent_name = "RMON2-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.addressmapdeletes = YLeaf(YType.uint32, "addressMapDeletes")

            self.addressmapinserts = YLeaf(YType.uint32, "addressMapInserts")

            self.addressmapmaxdesiredentries = YLeaf(YType.int32, "addressMapMaxDesiredEntries")
            self._segment_path = lambda: "addressMap"
            self._absolute_path = lambda: "RMON2-MIB:RMON2-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(RMON2MIB.Addressmap, ['addressmapdeletes', 'addressmapinserts', 'addressmapmaxdesiredentries'], name, value)


    class Addressmapcontroltable(Entity):
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
        	**type**\: list of    :py:class:`Addressmapcontrolentry <ydk.models.cisco_ios_xe.RMON2_MIB.RMON2MIB.Addressmapcontroltable.Addressmapcontrolentry>`
        
        

        """

        _prefix = 'RMON2-MIB'
        _revision = '1996-05-27'

        def __init__(self):
            super(RMON2MIB.Addressmapcontroltable, self).__init__()

            self.yang_name = "addressMapControlTable"
            self.yang_parent_name = "RMON2-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"addressMapControlEntry" : ("addressmapcontrolentry", RMON2MIB.Addressmapcontroltable.Addressmapcontrolentry)}

            self.addressmapcontrolentry = YList(self)
            self._segment_path = lambda: "addressMapControlTable"
            self._absolute_path = lambda: "RMON2-MIB:RMON2-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(RMON2MIB.Addressmapcontroltable, [], name, value)


        class Addressmapcontrolentry(Entity):
            """
            A conceptual row in the addressMapControlTable.
            
            
            
            
            
            An example of the indexing of this entry is
            addressMapControlDroppedFrames.1
            
            .. attribute:: addressmapcontrolindex  <key>
            
            	A unique index for this entry in the addressMapControlTable
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: addressmapcontroldatasource
            
            	The source of data for this addressMapControlEntry
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: addressmapcontroldroppedframes
            
            	The total number of frames which were received by the probe and therefore not accounted for in the \*StatsDropEvents, but for which the probe chose not to count for this entry for whatever reason.  Most often, this event occurs when the probe is out of some resources and decides to shed load from this collection.  This count does not include packets that were not counted because they had MAC\-layer errors.  Note that, unlike the dropEvents counter, this number is the exact number of frames dropped
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: addressmapcontrolowner
            
            	The entity that configured this entry and is therefore using the resources assigned to it
            	**type**\:  str
            
            	**length:** 0..127
            
            .. attribute:: addressmapcontrolstatus
            
            	The status of this addressMap control entry.  An entry may not exist in the active state unless all objects in the entry have an appropriate value.  If this object is not equal to active(1), all associated entries in the addressMapTable shall be deleted
            	**type**\:   :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            

            """

            _prefix = 'RMON2-MIB'
            _revision = '1996-05-27'

            def __init__(self):
                super(RMON2MIB.Addressmapcontroltable.Addressmapcontrolentry, self).__init__()

                self.yang_name = "addressMapControlEntry"
                self.yang_parent_name = "addressMapControlTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.addressmapcontrolindex = YLeaf(YType.int32, "addressMapControlIndex")

                self.addressmapcontroldatasource = YLeaf(YType.str, "addressMapControlDataSource")

                self.addressmapcontroldroppedframes = YLeaf(YType.uint32, "addressMapControlDroppedFrames")

                self.addressmapcontrolowner = YLeaf(YType.str, "addressMapControlOwner")

                self.addressmapcontrolstatus = YLeaf(YType.enumeration, "addressMapControlStatus")
                self._segment_path = lambda: "addressMapControlEntry" + "[addressMapControlIndex='" + self.addressmapcontrolindex.get() + "']"
                self._absolute_path = lambda: "RMON2-MIB:RMON2-MIB/addressMapControlTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(RMON2MIB.Addressmapcontroltable.Addressmapcontrolentry, ['addressmapcontrolindex', 'addressmapcontroldatasource', 'addressmapcontroldroppedframes', 'addressmapcontrolowner', 'addressmapcontrolstatus'], name, value)


    class Addressmaptable(Entity):
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
        	**type**\: list of    :py:class:`Addressmapentry <ydk.models.cisco_ios_xe.RMON2_MIB.RMON2MIB.Addressmaptable.Addressmapentry>`
        
        

        """

        _prefix = 'RMON2-MIB'
        _revision = '1996-05-27'

        def __init__(self):
            super(RMON2MIB.Addressmaptable, self).__init__()

            self.yang_name = "addressMapTable"
            self.yang_parent_name = "RMON2-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"addressMapEntry" : ("addressmapentry", RMON2MIB.Addressmaptable.Addressmapentry)}

            self.addressmapentry = YList(self)
            self._segment_path = lambda: "addressMapTable"
            self._absolute_path = lambda: "RMON2-MIB:RMON2-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(RMON2MIB.Addressmaptable, [], name, value)


        class Addressmapentry(Entity):
            """
            A conceptual row in the addressMapTable.
            The protocolDirLocalIndex in the index identifies the network
            layer protocol of the addressMapNetworkAddress.
            
            
            
            
            
            An example of the indexing of this entry is
            addressMapSource.783495.18.4.128.2.6.6.11.1.3.6.1.2.1.2.2.1.1.1
            
            .. attribute:: addressmaptimemark  <key>
            
            	A TimeFilter for this entry.  See the TimeFilter textual convention to see how this works
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: protocoldirlocalindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`protocoldirlocalindex <ydk.models.cisco_ios_xe.RMON2_MIB.RMON2MIB.Protocoldirtable.Protocoldirentry>`
            
            .. attribute:: addressmapnetworkaddress  <key>
            
            	The network address for this relation.  This is represented as an octet string with specific semantics and length as identified by the protocolDirLocalIndex component of the index.  For example, if the protocolDirLocalIndex indicates an encapsulation of ip, this object is encoded as a length octet of 4, followed by the 4 octets of the ip address, in network byte order
            	**type**\:  str
            
            .. attribute:: addressmapsource  <key>
            
            	The interface or port on which the associated network address was most recently seen.      If this address mapping was discovered on an interface, this object shall identify the instance of the ifIndex object, defined in [3,5], for the desired interface. For example, if an entry were to receive data from interface #1, this object would be set to ifIndex.1.  If this address mapping was discovered on a port, this object shall identify the instance of the rptrGroupPortIndex object, defined in [RFC1516], for the desired port. For example, if an entry were to receive data from group #1, port #1, this object would be set to rptrGroupPortIndex.1.1.  Note that while the dataSource associated with this entry may only point to index objects, this object may at times point to repeater port objects. This situation occurs when the dataSource points to an interface which is a locally attached repeater and the agent has additional information about the source port of traffic seen on that repeater
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: addressmaplastchange
            
            	The value of sysUpTime at the time this entry was last created or the values of the physical address changed.  This can be used to help detect duplicate address problems, in which case this object will be updated frequently
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: addressmapphysicaladdress
            
            	The last source physical address on which the associated network address was seen.  If the protocol of the associated network address was encapsulated inside of a network\-level or higher protocol, this will be the address of the next\-lower protocol with the addressRecognitionCapable bit enabled and will be formatted as specified for that protocol
            	**type**\:  str
            
            

            """

            _prefix = 'RMON2-MIB'
            _revision = '1996-05-27'

            def __init__(self):
                super(RMON2MIB.Addressmaptable.Addressmapentry, self).__init__()

                self.yang_name = "addressMapEntry"
                self.yang_parent_name = "addressMapTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.addressmaptimemark = YLeaf(YType.uint32, "addressMapTimeMark")

                self.protocoldirlocalindex = YLeaf(YType.str, "protocolDirLocalIndex")

                self.addressmapnetworkaddress = YLeaf(YType.str, "addressMapNetworkAddress")

                self.addressmapsource = YLeaf(YType.str, "addressMapSource")

                self.addressmaplastchange = YLeaf(YType.uint32, "addressMapLastChange")

                self.addressmapphysicaladdress = YLeaf(YType.str, "addressMapPhysicalAddress")
                self._segment_path = lambda: "addressMapEntry" + "[addressMapTimeMark='" + self.addressmaptimemark.get() + "']" + "[protocolDirLocalIndex='" + self.protocoldirlocalindex.get() + "']" + "[addressMapNetworkAddress='" + self.addressmapnetworkaddress.get() + "']" + "[addressMapSource='" + self.addressmapsource.get() + "']"
                self._absolute_path = lambda: "RMON2-MIB:RMON2-MIB/addressMapTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(RMON2MIB.Addressmaptable.Addressmapentry, ['addressmaptimemark', 'protocoldirlocalindex', 'addressmapnetworkaddress', 'addressmapsource', 'addressmaplastchange', 'addressmapphysicaladdress'], name, value)


    class Alhosttable(Entity):
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
        	**type**\: list of    :py:class:`Alhostentry <ydk.models.cisco_ios_xe.RMON2_MIB.RMON2MIB.Alhosttable.Alhostentry>`
        
        

        """

        _prefix = 'RMON2-MIB'
        _revision = '1996-05-27'

        def __init__(self):
            super(RMON2MIB.Alhosttable, self).__init__()

            self.yang_name = "alHostTable"
            self.yang_parent_name = "RMON2-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"alHostEntry" : ("alhostentry", RMON2MIB.Alhosttable.Alhostentry)}

            self.alhostentry = YList(self)
            self._segment_path = lambda: "alHostTable"
            self._absolute_path = lambda: "RMON2-MIB:RMON2-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(RMON2MIB.Alhosttable, [], name, value)


        class Alhostentry(Entity):
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
            
            .. attribute:: hlhostcontrolindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..65535
            
            	**refers to**\:  :py:class:`hlhostcontrolindex <ydk.models.cisco_ios_xe.RMON2_MIB.RMON2MIB.Hlhostcontroltable.Hlhostcontrolentry>`
            
            .. attribute:: alhosttimemark  <key>
            
            	A TimeFilter for this entry.  See the TimeFilter textual convention to see how this works
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: protocoldirlocalindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`protocoldirlocalindex <ydk.models.cisco_ios_xe.RMON2_MIB.RMON2MIB.Protocoldirtable.Protocoldirentry>`
            
            .. attribute:: nlhostaddress  <key>
            
            	
            	**type**\:  str
            
            	**refers to**\:  :py:class:`nlhostaddress <ydk.models.cisco_ios_xe.RMON2_MIB.RMON2MIB.Nlhosttable.Nlhostentry>`
            
            .. attribute:: protocoldirlocalindex_2  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`protocoldirlocalindex <ydk.models.cisco_ios_xe.RMON2_MIB.RMON2MIB.Protocoldirtable.Protocoldirentry>`
            
            .. attribute:: alhostcreatetime
            
            	The value of sysUpTime when this entry was last activated. This can be used by the management station to ensure that the entry has not been deleted and recreated between polls
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: alhostinoctets
            
            	The number of octets transmitted to this address of this protocol type since it was added to the alHostTable (excluding framing bits but including      FCS octets), excluding those octets in packets that contained errors.  Note this doesn't count just those octets in the particular protocol frames, but includes the entire packet that contained the protocol
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: alhostinpkts
            
            	The number of packets of this protocol type without errors transmitted to this address since it was added to the alHostTable.  Note that this is the number of link\-layer packets, so if a single network\-layer packet is fragmented into several link\-layer frames, this counter is incremented several times
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: alhostoutoctets
            
            	The number of octets transmitted by this address of this protocol type since it was added to the alHostTable (excluding framing bits but including FCS octets), excluding those octets in packets that contained errors.  Note this doesn't count just those octets in the particular protocol frames, but includes the entire packet that contained the protocol
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: alhostoutpkts
            
            	The number of packets of this protocol type without errors transmitted by this address since it was added to the alHostTable.  Note that this is the number of link\-layer packets, so if a single network\-layer packet is fragmented into several link\-layer frames, this counter is incremented several times
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'RMON2-MIB'
            _revision = '1996-05-27'

            def __init__(self):
                super(RMON2MIB.Alhosttable.Alhostentry, self).__init__()

                self.yang_name = "alHostEntry"
                self.yang_parent_name = "alHostTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.hlhostcontrolindex = YLeaf(YType.str, "hlHostControlIndex")

                self.alhosttimemark = YLeaf(YType.uint32, "alHostTimeMark")

                self.protocoldirlocalindex = YLeaf(YType.str, "protocolDirLocalIndex")

                self.nlhostaddress = YLeaf(YType.str, "nlHostAddress")

                self.protocoldirlocalindex_2 = YLeaf(YType.str, "protocolDirLocalIndex_2")

                self.alhostcreatetime = YLeaf(YType.uint32, "alHostCreateTime")

                self.alhostinoctets = YLeaf(YType.uint32, "alHostInOctets")

                self.alhostinpkts = YLeaf(YType.uint32, "alHostInPkts")

                self.alhostoutoctets = YLeaf(YType.uint32, "alHostOutOctets")

                self.alhostoutpkts = YLeaf(YType.uint32, "alHostOutPkts")
                self._segment_path = lambda: "alHostEntry" + "[hlHostControlIndex='" + self.hlhostcontrolindex.get() + "']" + "[alHostTimeMark='" + self.alhosttimemark.get() + "']" + "[protocolDirLocalIndex='" + self.protocoldirlocalindex.get() + "']" + "[nlHostAddress='" + self.nlhostaddress.get() + "']" + "[protocolDirLocalIndex_2='" + self.protocoldirlocalindex_2.get() + "']"
                self._absolute_path = lambda: "RMON2-MIB:RMON2-MIB/alHostTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(RMON2MIB.Alhosttable.Alhostentry, ['hlhostcontrolindex', 'alhosttimemark', 'protocoldirlocalindex', 'nlhostaddress', 'protocoldirlocalindex_2', 'alhostcreatetime', 'alhostinoctets', 'alhostinpkts', 'alhostoutoctets', 'alhostoutpkts'], name, value)


    class Almatrixdstable(Entity):
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
        	**type**\: list of    :py:class:`Almatrixdsentry <ydk.models.cisco_ios_xe.RMON2_MIB.RMON2MIB.Almatrixdstable.Almatrixdsentry>`
        
        

        """

        _prefix = 'RMON2-MIB'
        _revision = '1996-05-27'

        def __init__(self):
            super(RMON2MIB.Almatrixdstable, self).__init__()

            self.yang_name = "alMatrixDSTable"
            self.yang_parent_name = "RMON2-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"alMatrixDSEntry" : ("almatrixdsentry", RMON2MIB.Almatrixdstable.Almatrixdsentry)}

            self.almatrixdsentry = YList(self)
            self._segment_path = lambda: "alMatrixDSTable"
            self._absolute_path = lambda: "RMON2-MIB:RMON2-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(RMON2MIB.Almatrixdstable, [], name, value)


        class Almatrixdsentry(Entity):
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
            
            .. attribute:: hlmatrixcontrolindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..65535
            
            	**refers to**\:  :py:class:`hlmatrixcontrolindex <ydk.models.cisco_ios_xe.RMON2_MIB.RMON2MIB.Hlmatrixcontroltable.Hlmatrixcontrolentry>`
            
            .. attribute:: almatrixdstimemark  <key>
            
            	A TimeFilter for this entry.  See the TimeFilter textual convention to see how this works
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: protocoldirlocalindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`protocoldirlocalindex <ydk.models.cisco_ios_xe.RMON2_MIB.RMON2MIB.Protocoldirtable.Protocoldirentry>`
            
            .. attribute:: nlmatrixdsdestaddress  <key>
            
            	
            	**type**\:  str
            
            	**refers to**\:  :py:class:`nlmatrixdsdestaddress <ydk.models.cisco_ios_xe.RMON2_MIB.RMON2MIB.Nlmatrixdstable.Nlmatrixdsentry>`
            
            .. attribute:: nlmatrixdssourceaddress  <key>
            
            	
            	**type**\:  str
            
            	**refers to**\:  :py:class:`nlmatrixdssourceaddress <ydk.models.cisco_ios_xe.RMON2_MIB.RMON2MIB.Nlmatrixdstable.Nlmatrixdsentry>`
            
            .. attribute:: protocoldirlocalindex_2  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`protocoldirlocalindex <ydk.models.cisco_ios_xe.RMON2_MIB.RMON2MIB.Protocoldirtable.Protocoldirentry>`
            
            .. attribute:: almatrixdscreatetime
            
            	The value of sysUpTime when this entry was last activated. This can be used by the management station to ensure that the entry has not been deleted and recreated between polls
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: almatrixdsoctets
            
            	The number of octets in packets of this protocol type transmitted from the source address to the destination address since this entry was added to the alMatrixDSTable (excluding framing bits but including FCS octets), excluding those octets in packets that contained errors.  Note this doesn't count just those octets in the particular protocol frames, but includes the entire packet that contained the protocol
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: almatrixdspkts
            
            	The number of packets of this protocol type without errors transmitted from the source address to the destination address since this entry was added to the alMatrixDSTable.  Note that this is the number of link\-layer packets, so if a single network\-layer packet is fragmented into several link\-layer frames, this counter is incremented several times
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'RMON2-MIB'
            _revision = '1996-05-27'

            def __init__(self):
                super(RMON2MIB.Almatrixdstable.Almatrixdsentry, self).__init__()

                self.yang_name = "alMatrixDSEntry"
                self.yang_parent_name = "alMatrixDSTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.hlmatrixcontrolindex = YLeaf(YType.str, "hlMatrixControlIndex")

                self.almatrixdstimemark = YLeaf(YType.uint32, "alMatrixDSTimeMark")

                self.protocoldirlocalindex = YLeaf(YType.str, "protocolDirLocalIndex")

                self.nlmatrixdsdestaddress = YLeaf(YType.str, "nlMatrixDSDestAddress")

                self.nlmatrixdssourceaddress = YLeaf(YType.str, "nlMatrixDSSourceAddress")

                self.protocoldirlocalindex_2 = YLeaf(YType.str, "protocolDirLocalIndex_2")

                self.almatrixdscreatetime = YLeaf(YType.uint32, "alMatrixDSCreateTime")

                self.almatrixdsoctets = YLeaf(YType.uint32, "alMatrixDSOctets")

                self.almatrixdspkts = YLeaf(YType.uint32, "alMatrixDSPkts")
                self._segment_path = lambda: "alMatrixDSEntry" + "[hlMatrixControlIndex='" + self.hlmatrixcontrolindex.get() + "']" + "[alMatrixDSTimeMark='" + self.almatrixdstimemark.get() + "']" + "[protocolDirLocalIndex='" + self.protocoldirlocalindex.get() + "']" + "[nlMatrixDSDestAddress='" + self.nlmatrixdsdestaddress.get() + "']" + "[nlMatrixDSSourceAddress='" + self.nlmatrixdssourceaddress.get() + "']" + "[protocolDirLocalIndex_2='" + self.protocoldirlocalindex_2.get() + "']"
                self._absolute_path = lambda: "RMON2-MIB:RMON2-MIB/alMatrixDSTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(RMON2MIB.Almatrixdstable.Almatrixdsentry, ['hlmatrixcontrolindex', 'almatrixdstimemark', 'protocoldirlocalindex', 'nlmatrixdsdestaddress', 'nlmatrixdssourceaddress', 'protocoldirlocalindex_2', 'almatrixdscreatetime', 'almatrixdsoctets', 'almatrixdspkts'], name, value)


    class Almatrixsdtable(Entity):
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
        	**type**\: list of    :py:class:`Almatrixsdentry <ydk.models.cisco_ios_xe.RMON2_MIB.RMON2MIB.Almatrixsdtable.Almatrixsdentry>`
        
        

        """

        _prefix = 'RMON2-MIB'
        _revision = '1996-05-27'

        def __init__(self):
            super(RMON2MIB.Almatrixsdtable, self).__init__()

            self.yang_name = "alMatrixSDTable"
            self.yang_parent_name = "RMON2-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"alMatrixSDEntry" : ("almatrixsdentry", RMON2MIB.Almatrixsdtable.Almatrixsdentry)}

            self.almatrixsdentry = YList(self)
            self._segment_path = lambda: "alMatrixSDTable"
            self._absolute_path = lambda: "RMON2-MIB:RMON2-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(RMON2MIB.Almatrixsdtable, [], name, value)


        class Almatrixsdentry(Entity):
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
            
            .. attribute:: hlmatrixcontrolindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..65535
            
            	**refers to**\:  :py:class:`hlmatrixcontrolindex <ydk.models.cisco_ios_xe.RMON2_MIB.RMON2MIB.Hlmatrixcontroltable.Hlmatrixcontrolentry>`
            
            .. attribute:: almatrixsdtimemark  <key>
            
            	A TimeFilter for this entry.  See the TimeFilter textual convention to see how this works
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: protocoldirlocalindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`protocoldirlocalindex <ydk.models.cisco_ios_xe.RMON2_MIB.RMON2MIB.Protocoldirtable.Protocoldirentry>`
            
            .. attribute:: nlmatrixsdsourceaddress  <key>
            
            	
            	**type**\:  str
            
            	**refers to**\:  :py:class:`nlmatrixsdsourceaddress <ydk.models.cisco_ios_xe.RMON2_MIB.RMON2MIB.Nlmatrixsdtable.Nlmatrixsdentry>`
            
            .. attribute:: nlmatrixsddestaddress  <key>
            
            	
            	**type**\:  str
            
            	**refers to**\:  :py:class:`nlmatrixsddestaddress <ydk.models.cisco_ios_xe.RMON2_MIB.RMON2MIB.Nlmatrixsdtable.Nlmatrixsdentry>`
            
            .. attribute:: protocoldirlocalindex_2  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`protocoldirlocalindex <ydk.models.cisco_ios_xe.RMON2_MIB.RMON2MIB.Protocoldirtable.Protocoldirentry>`
            
            .. attribute:: almatrixsdcreatetime
            
            	The value of sysUpTime when this entry was last activated. This can be used by the management station to ensure that the entry has not been deleted and recreated between polls
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: almatrixsdoctets
            
            	The number of octets in packets of this protocol type transmitted from the source address to the destination address since this entry was added to the alMatrixSDTable (excluding framing bits but including FCS octets), excluding those octets in packets that contained errors.  Note this doesn't count just those octets in the particular protocol frames, but includes the entire packet that contained the protocol
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: almatrixsdpkts
            
            	The number of packets of this protocol type without errors transmitted from the source address to the destination address since this entry was added to the alMatrixSDTable.  Note that this is the number of link\-layer packets, so if a single network\-layer packet is fragmented into several link\-layer frames, this counter is incremented several times
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'RMON2-MIB'
            _revision = '1996-05-27'

            def __init__(self):
                super(RMON2MIB.Almatrixsdtable.Almatrixsdentry, self).__init__()

                self.yang_name = "alMatrixSDEntry"
                self.yang_parent_name = "alMatrixSDTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.hlmatrixcontrolindex = YLeaf(YType.str, "hlMatrixControlIndex")

                self.almatrixsdtimemark = YLeaf(YType.uint32, "alMatrixSDTimeMark")

                self.protocoldirlocalindex = YLeaf(YType.str, "protocolDirLocalIndex")

                self.nlmatrixsdsourceaddress = YLeaf(YType.str, "nlMatrixSDSourceAddress")

                self.nlmatrixsddestaddress = YLeaf(YType.str, "nlMatrixSDDestAddress")

                self.protocoldirlocalindex_2 = YLeaf(YType.str, "protocolDirLocalIndex_2")

                self.almatrixsdcreatetime = YLeaf(YType.uint32, "alMatrixSDCreateTime")

                self.almatrixsdoctets = YLeaf(YType.uint32, "alMatrixSDOctets")

                self.almatrixsdpkts = YLeaf(YType.uint32, "alMatrixSDPkts")
                self._segment_path = lambda: "alMatrixSDEntry" + "[hlMatrixControlIndex='" + self.hlmatrixcontrolindex.get() + "']" + "[alMatrixSDTimeMark='" + self.almatrixsdtimemark.get() + "']" + "[protocolDirLocalIndex='" + self.protocoldirlocalindex.get() + "']" + "[nlMatrixSDSourceAddress='" + self.nlmatrixsdsourceaddress.get() + "']" + "[nlMatrixSDDestAddress='" + self.nlmatrixsddestaddress.get() + "']" + "[protocolDirLocalIndex_2='" + self.protocoldirlocalindex_2.get() + "']"
                self._absolute_path = lambda: "RMON2-MIB:RMON2-MIB/alMatrixSDTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(RMON2MIB.Almatrixsdtable.Almatrixsdentry, ['hlmatrixcontrolindex', 'almatrixsdtimemark', 'protocoldirlocalindex', 'nlmatrixsdsourceaddress', 'nlmatrixsddestaddress', 'protocoldirlocalindex_2', 'almatrixsdcreatetime', 'almatrixsdoctets', 'almatrixsdpkts'], name, value)


    class Almatrixtopncontroltable(Entity):
        """
        A set of parameters that control the creation of a
        report of the top N matrix entries according to
        a selected metric.
        
        .. attribute:: almatrixtopncontrolentry
        
        	A conceptual row in the alMatrixTopNControlTable.  An example of the indexing of this table is alMatrixTopNControlDuration.3
        	**type**\: list of    :py:class:`Almatrixtopncontrolentry <ydk.models.cisco_ios_xe.RMON2_MIB.RMON2MIB.Almatrixtopncontroltable.Almatrixtopncontrolentry>`
        
        

        """

        _prefix = 'RMON2-MIB'
        _revision = '1996-05-27'

        def __init__(self):
            super(RMON2MIB.Almatrixtopncontroltable, self).__init__()

            self.yang_name = "alMatrixTopNControlTable"
            self.yang_parent_name = "RMON2-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"alMatrixTopNControlEntry" : ("almatrixtopncontrolentry", RMON2MIB.Almatrixtopncontroltable.Almatrixtopncontrolentry)}

            self.almatrixtopncontrolentry = YList(self)
            self._segment_path = lambda: "alMatrixTopNControlTable"
            self._absolute_path = lambda: "RMON2-MIB:RMON2-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(RMON2MIB.Almatrixtopncontroltable, [], name, value)


        class Almatrixtopncontrolentry(Entity):
            """
            A conceptual row in the alMatrixTopNControlTable.
            
            An example of the indexing of this table is
            alMatrixTopNControlDuration.3
            
            .. attribute:: almatrixtopncontrolindex  <key>
            
            	An index that uniquely identifies an entry in the alMatrixTopNControlTable.  Each such entry defines one top N report prepared for one interface
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: almatrixtopncontrolduration
            
            	The number of seconds that this report has collected during the last sampling interval.  When the associated alMatrixTopNControlTimeRemaining object is set, this object shall be set by the probe to the same value and shall not be modified until the next time the alMatrixTopNControlTimeRemaining is set.  This value shall be zero if no reports have been requested for this alMatrixTopNControlEntry
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: almatrixtopncontrolgeneratedreports
            
            	The number of reports that have been generated by this entry
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: almatrixtopncontrolgrantedsize
            
            	The maximum number of matrix entries in this report.  When the associated alMatrixTopNControlRequestedSize object is created or modified, the probe should set this      object as closely to the requested value as is possible for the particular implementation and available resources. The probe must not lower this value except as a result of a set to the associated alMatrixTopNControlRequestedSize object.  If the value of alMatrixTopNControlRateBase is equal to alMatrixTopNTerminalsPkts or alMatrixTopNAllPkts, when the next topN report is generated, matrix entries with the highest value of alMatrixTopNPktRate shall be placed in this table in decreasing order of this rate until there is no more room or until there are no more matrix entries.  If the value of alMatrixTopNControlRateBase is equal to alMatrixTopNTerminalsOctets or alMatrixTopNAllOctets, when the next topN report is generated, matrix entries with the highest value of alMatrixTopNOctetRate shall be placed in this table in decreasing order of this rate until there is no more room or until there are no more matrix entries.  It is an implementation\-specific matter how entries with the same value of alMatrixTopNPktRate or alMatrixTopNOctetRate are sorted.  It is also an implementation\-specific matter as to whether or not zero\-valued entries are available
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: almatrixtopncontrolmatrixindex
            
            	The alMatrix[SD/DS] table for which a top N report will be prepared on behalf of this entry.  The alMatrix[SD/DS] table is identified by the value of the hlMatrixControlIndex for that table \- that value is used here to identify the particular table.  This object may not be modified if the associated alMatrixTopNControlStatus object is equal to active(1)
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: almatrixtopncontrolowner
            
            	The entity that configured this entry and is therefore using the resources assigned to it
            	**type**\:  str
            
            	**length:** 0..127
            
            .. attribute:: almatrixtopncontrolratebase
            
            	The variable for each alMatrix[SD/DS] entry that the      alMatrixTopNEntries are sorted by, as well as the selector of the view of the matrix table that will be used.  The values alMatrixTopNTerminalsPkts and alMatrixTopNTerminalsOctets cause collection only from protocols that have no child protocols that are counted.  The values alMatrixTopNAllPkts and alMatrixTopNAllOctets cause collection from all alMatrix entries.  This object may not be modified if the associated alMatrixTopNControlStatus object is equal to active(1)
            	**type**\:   :py:class:`Almatrixtopncontrolratebase <ydk.models.cisco_ios_xe.RMON2_MIB.RMON2MIB.Almatrixtopncontroltable.Almatrixtopncontrolentry.Almatrixtopncontrolratebase>`
            
            .. attribute:: almatrixtopncontrolrequestedsize
            
            	The maximum number of matrix entries requested for this report.  When this object is created or modified, the probe should set alMatrixTopNControlGrantedSize as closely to this object as is possible for the particular probe implementation and available resources
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: almatrixtopncontrolstarttime
            
            	The value of sysUpTime when this top N report was last started.  In other words, this is the time that the associated alMatrixTopNControlTimeRemaining object was modified to start the requested report or the time the report was last automatically (re)started.  This object may be used by the management station to determine if a report was missed or not
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: almatrixtopncontrolstatus
            
            	The status of this alMatrixTopNControlEntry.  An entry may not exist in the active state unless all objects in the entry have an appropriate value.  If this object is not equal to active(1), all associated entries in the alMatrixTopNTable shall be deleted by the agent
            	**type**\:   :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            .. attribute:: almatrixtopncontroltimeremaining
            
            	The number of seconds left in the report currently being collected.  When this object is modified by the management station, a new collection is started, possibly aborting a currently running report.  The new value is used as the requested duration of this report, and is immediately loaded into the associated alMatrixTopNControlDuration object. When the report finishes, the probe will automatically start another collection with the same initial value of alMatrixTopNControlTimeRemaining.  Thus the management station may simply read the resulting reports repeatedly, checking the startTime and duration each time to ensure that a report was not missed or that the report parameters were not changed.  While the value of this object is non\-zero, it decrements by one per second until it reaches zero.  At the time that this object decrements to zero, the report is made accessible in the alMatrixTopNTable, overwriting any report that may be there.  When this object is modified by the management station, any associated entries in the alMatrixTopNTable shall be deleted.  (Note that this is a different algorithm than the one used in the hostTopNTable)
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            

            """

            _prefix = 'RMON2-MIB'
            _revision = '1996-05-27'

            def __init__(self):
                super(RMON2MIB.Almatrixtopncontroltable.Almatrixtopncontrolentry, self).__init__()

                self.yang_name = "alMatrixTopNControlEntry"
                self.yang_parent_name = "alMatrixTopNControlTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.almatrixtopncontrolindex = YLeaf(YType.int32, "alMatrixTopNControlIndex")

                self.almatrixtopncontrolduration = YLeaf(YType.int32, "alMatrixTopNControlDuration")

                self.almatrixtopncontrolgeneratedreports = YLeaf(YType.uint32, "alMatrixTopNControlGeneratedReports")

                self.almatrixtopncontrolgrantedsize = YLeaf(YType.int32, "alMatrixTopNControlGrantedSize")

                self.almatrixtopncontrolmatrixindex = YLeaf(YType.int32, "alMatrixTopNControlMatrixIndex")

                self.almatrixtopncontrolowner = YLeaf(YType.str, "alMatrixTopNControlOwner")

                self.almatrixtopncontrolratebase = YLeaf(YType.enumeration, "alMatrixTopNControlRateBase")

                self.almatrixtopncontrolrequestedsize = YLeaf(YType.int32, "alMatrixTopNControlRequestedSize")

                self.almatrixtopncontrolstarttime = YLeaf(YType.uint32, "alMatrixTopNControlStartTime")

                self.almatrixtopncontrolstatus = YLeaf(YType.enumeration, "alMatrixTopNControlStatus")

                self.almatrixtopncontroltimeremaining = YLeaf(YType.int32, "alMatrixTopNControlTimeRemaining")
                self._segment_path = lambda: "alMatrixTopNControlEntry" + "[alMatrixTopNControlIndex='" + self.almatrixtopncontrolindex.get() + "']"
                self._absolute_path = lambda: "RMON2-MIB:RMON2-MIB/alMatrixTopNControlTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(RMON2MIB.Almatrixtopncontroltable.Almatrixtopncontrolentry, ['almatrixtopncontrolindex', 'almatrixtopncontrolduration', 'almatrixtopncontrolgeneratedreports', 'almatrixtopncontrolgrantedsize', 'almatrixtopncontrolmatrixindex', 'almatrixtopncontrolowner', 'almatrixtopncontrolratebase', 'almatrixtopncontrolrequestedsize', 'almatrixtopncontrolstarttime', 'almatrixtopncontrolstatus', 'almatrixtopncontroltimeremaining'], name, value)

            class Almatrixtopncontrolratebase(Enum):
                """
                Almatrixtopncontrolratebase

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

                .. data:: alMatrixTopNTerminalsPkts = 1

                .. data:: alMatrixTopNTerminalsOctets = 2

                .. data:: alMatrixTopNAllPkts = 3

                .. data:: alMatrixTopNAllOctets = 4

                """

                alMatrixTopNTerminalsPkts = Enum.YLeaf(1, "alMatrixTopNTerminalsPkts")

                alMatrixTopNTerminalsOctets = Enum.YLeaf(2, "alMatrixTopNTerminalsOctets")

                alMatrixTopNAllPkts = Enum.YLeaf(3, "alMatrixTopNAllPkts")

                alMatrixTopNAllOctets = Enum.YLeaf(4, "alMatrixTopNAllOctets")



    class Almatrixtopntable(Entity):
        """
        A set of statistics for those application layer matrix
        entries that have counted the highest number of octets or
        packets.
        
        .. attribute:: almatrixtopnentry
        
        	A conceptual row in the alMatrixTopNTable.  The alMatrixTopNControlIndex value in the index identifies the alMatrixTopNControlEntry on whose behalf this entry was created.  An example of the indexing of this table is alMatrixTopNPktRate.3.10
        	**type**\: list of    :py:class:`Almatrixtopnentry <ydk.models.cisco_ios_xe.RMON2_MIB.RMON2MIB.Almatrixtopntable.Almatrixtopnentry>`
        
        

        """

        _prefix = 'RMON2-MIB'
        _revision = '1996-05-27'

        def __init__(self):
            super(RMON2MIB.Almatrixtopntable, self).__init__()

            self.yang_name = "alMatrixTopNTable"
            self.yang_parent_name = "RMON2-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"alMatrixTopNEntry" : ("almatrixtopnentry", RMON2MIB.Almatrixtopntable.Almatrixtopnentry)}

            self.almatrixtopnentry = YList(self)
            self._segment_path = lambda: "alMatrixTopNTable"
            self._absolute_path = lambda: "RMON2-MIB:RMON2-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(RMON2MIB.Almatrixtopntable, [], name, value)


        class Almatrixtopnentry(Entity):
            """
            A conceptual row in the alMatrixTopNTable.
            
            The alMatrixTopNControlIndex value in the index identifies
            the alMatrixTopNControlEntry on whose behalf this entry was
            created.
            
            An example of the indexing of this table is
            alMatrixTopNPktRate.3.10
            
            .. attribute:: almatrixtopncontrolindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..65535
            
            	**refers to**\:  :py:class:`almatrixtopncontrolindex <ydk.models.cisco_ios_xe.RMON2_MIB.RMON2MIB.Almatrixtopncontroltable.Almatrixtopncontrolentry>`
            
            .. attribute:: almatrixtopnindex  <key>
            
            	An index that uniquely identifies an entry in the alMatrixTopNTable among those in the same report. This index is between 1 and N, where N is the number of entries in this report.  If the value of alMatrixTopNControlRateBase is equal to alMatrixTopNTerminalsPkts or alMatrixTopNAllPkts, increasing values of alMatrixTopNIndex shall be assigned to entries with decreasing values of alMatrixTopNPktRate until index N is assigned or there are no more alMatrixTopNEntries.  If the value of alMatrixTopNControlRateBase is equal to alMatrixTopNTerminalsOctets or alMatrixTopNAllOctets, increasing values of alMatrixTopNIndex shall be assigned to entries with decreasing values of alMatrixTopNOctetRate until index N is assigned or there are no more alMatrixTopNEntries
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: almatrixtopnappprotocoldirlocalindex
            
            	The type of the protocol counted by this matrix entry
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: almatrixtopndestaddress
            
            	The network layer address of the destination host in this conversation.  This is represented as an octet string with specific semantics and length as identified by the associated alMatrixTopNProtocolDirLocalIndex.  For example, if the alMatrixTopNProtocolDirLocalIndex indicates an encapsulation of ip, this object is encoded as a length octet of 4, followed by the 4 octets of the ip address, in network byte order
            	**type**\:  str
            
            .. attribute:: almatrixtopnoctetrate
            
            	The number of octets seen of this protocol from the source host to the destination host during this sampling interval, counted using the rules for counting the alMatrixSDOctets object.  If the value of alMatrixTopNControlRateBase is alMatrixTopNTerminalsOctets or alMatrixTopNAllOctets, this variable will be used to sort this report
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: almatrixtopnpktrate
            
            	The number of packets seen of this protocol from the source host to the destination host during this sampling interval, counted using the rules for counting the alMatrixSDPkts object.  If the value of alMatrixTopNControlRateBase is alMatrixTopNTerminalsPkts or alMatrixTopNAllPkts, this variable will be used to sort this report
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: almatrixtopnprotocoldirlocalindex
            
            	The protocolDirLocalIndex of the network layer protocol of this entry's network address
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: almatrixtopnreverseoctetrate
            
            	The number of octets seen of this protocol from the destination host to the source host during this sampling interval, counted using the rules for counting the alMatrixDSOctets object  (note that the corresponding alMatrixSDOctets object selected is the one whose source address is equal to alMatrixTopNDestAddress and whose destination address is equal to alMatrixTopNSourceAddress.)  Note that if the value of alMatrixTopNControlRateBase is equal      to alMatrixTopNTerminalsOctets or alMatrixTopNAllOctets, the sort of topN entries is based entirely on alMatrixTopNOctetRate, and not on the value of this object
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: almatrixtopnreversepktrate
            
            	The number of packets seen of this protocol from the destination host to the source host during this sampling interval, counted using the rules for counting the alMatrixDSPkts object  (note that the corresponding alMatrixSDPkts object selected is the one whose source address is equal to alMatrixTopNDestAddress and whose destination address is equal to alMatrixTopNSourceAddress.)  Note that if the value of alMatrixTopNControlRateBase is equal to alMatrixTopNTerminalsPkts or alMatrixTopNAllPkts, the sort of topN entries is based entirely on alMatrixTopNPktRate, and not on the value of this object
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: almatrixtopnsourceaddress
            
            	The network layer address of the source host in this conversation. This is represented as an octet string with specific semantics and length as identified      by the associated alMatrixTopNProtocolDirLocalIndex.  For example, if the alMatrixTopNProtocolDirLocalIndex indicates an encapsulation of ip, this object is encoded as a length octet of 4, followed by the 4 octets of the ip address, in network byte order
            	**type**\:  str
            
            

            """

            _prefix = 'RMON2-MIB'
            _revision = '1996-05-27'

            def __init__(self):
                super(RMON2MIB.Almatrixtopntable.Almatrixtopnentry, self).__init__()

                self.yang_name = "alMatrixTopNEntry"
                self.yang_parent_name = "alMatrixTopNTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.almatrixtopncontrolindex = YLeaf(YType.str, "alMatrixTopNControlIndex")

                self.almatrixtopnindex = YLeaf(YType.int32, "alMatrixTopNIndex")

                self.almatrixtopnappprotocoldirlocalindex = YLeaf(YType.int32, "alMatrixTopNAppProtocolDirLocalIndex")

                self.almatrixtopndestaddress = YLeaf(YType.str, "alMatrixTopNDestAddress")

                self.almatrixtopnoctetrate = YLeaf(YType.uint32, "alMatrixTopNOctetRate")

                self.almatrixtopnpktrate = YLeaf(YType.uint32, "alMatrixTopNPktRate")

                self.almatrixtopnprotocoldirlocalindex = YLeaf(YType.int32, "alMatrixTopNProtocolDirLocalIndex")

                self.almatrixtopnreverseoctetrate = YLeaf(YType.uint32, "alMatrixTopNReverseOctetRate")

                self.almatrixtopnreversepktrate = YLeaf(YType.uint32, "alMatrixTopNReversePktRate")

                self.almatrixtopnsourceaddress = YLeaf(YType.str, "alMatrixTopNSourceAddress")
                self._segment_path = lambda: "alMatrixTopNEntry" + "[alMatrixTopNControlIndex='" + self.almatrixtopncontrolindex.get() + "']" + "[alMatrixTopNIndex='" + self.almatrixtopnindex.get() + "']"
                self._absolute_path = lambda: "RMON2-MIB:RMON2-MIB/alMatrixTopNTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(RMON2MIB.Almatrixtopntable.Almatrixtopnentry, ['almatrixtopncontrolindex', 'almatrixtopnindex', 'almatrixtopnappprotocoldirlocalindex', 'almatrixtopndestaddress', 'almatrixtopnoctetrate', 'almatrixtopnpktrate', 'almatrixtopnprotocoldirlocalindex', 'almatrixtopnreverseoctetrate', 'almatrixtopnreversepktrate', 'almatrixtopnsourceaddress'], name, value)


    class Hlhostcontroltable(Entity):
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
        	**type**\: list of    :py:class:`Hlhostcontrolentry <ydk.models.cisco_ios_xe.RMON2_MIB.RMON2MIB.Hlhostcontroltable.Hlhostcontrolentry>`
        
        

        """

        _prefix = 'RMON2-MIB'
        _revision = '1996-05-27'

        def __init__(self):
            super(RMON2MIB.Hlhostcontroltable, self).__init__()

            self.yang_name = "hlHostControlTable"
            self.yang_parent_name = "RMON2-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"hlHostControlEntry" : ("hlhostcontrolentry", RMON2MIB.Hlhostcontroltable.Hlhostcontrolentry)}

            self.hlhostcontrolentry = YList(self)
            self._segment_path = lambda: "hlHostControlTable"
            self._absolute_path = lambda: "RMON2-MIB:RMON2-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(RMON2MIB.Hlhostcontroltable, [], name, value)


        class Hlhostcontrolentry(Entity):
            """
            A conceptual row in the hlHostControlTable.
            
            An example of the indexing of this entry is
            hlHostControlNlDroppedFrames.1
            
            .. attribute:: hlhostcontrolindex  <key>
            
            	An index that uniquely identifies an entry in the hlHostControlTable.  Each such entry defines a function that discovers hosts on a particular interface and places statistics about them in the nlHostTable, and optionally in the alHostTable, on behalf of this hlHostControlEntry
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: hlhostcontrolaldeletes
            
            	The number of times an alHost entry has been deleted from the alHost table (for any reason).  If an entry is deleted, then inserted, and then deleted, this counter will be incremented by 2.  To allow for efficient implementation strategies, agents may delay updating this object for short periods of time.  For example, an implementation strategy may allow internal data structures to differ from those visible via SNMP for short periods of time.  This counter may reflect the internal data structures for those short periods of time.  Note that the table size can be determined by subtracting hlHostControlAlDeletes from hlHostControlAlInserts
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: hlhostcontrolaldroppedframes
            
            	The total number of frames which were received by the probe and therefore not accounted for in the \*StatsDropEvents, but for which the probe chose not to count for the associated alHost entries for whatever reason.  Most often, this event occurs when the probe is out of some resources and decides to shed load from this collection.  This count does not include packets that were not counted because they had MAC\-layer errors.       Note that if the alHostTable is not implemented or is inactive because no protocols are enabled in the protocol directory, this value should be 0.  Note that, unlike the dropEvents counter, this number is the exact number of frames dropped
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: hlhostcontrolalinserts
            
            	The number of times an alHost entry has been inserted into the alHost table.  If an entry is inserted, then deleted, and then inserted, this counter will be incremented by 2.  To allow for efficient implementation strategies, agents may delay updating this object for short periods of time.  For example, an implementation strategy may allow internal data structures to differ from those visible via SNMP for short periods of time.  This counter may reflect the internal data structures for those short periods of time.  Note that the table size can be determined by subtracting hlHostControlAlDeletes from hlHostControlAlInserts
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: hlhostcontrolalmaxdesiredentries
            
            	The maximum number of entries that are desired in the alHost table on behalf of this control entry. The probe will not create more than this number of associated entries in the table, but may choose to create fewer entries in this table for any reason including the lack of resources.  If this object is set to a value less than the current number of entries, enough entries are chosen in an implementation\-dependent manner and deleted so that the number of entries in the table equals the value of this object.  If this value is set to \-1, the probe may create any number of entries in this table.  If the associated hlHostControlStatus object is equal to `active', this object may not be modified.  This object may be used to control how resources are allocated on the probe for the various RMON functions
            	**type**\:  int
            
            	**range:** \-1..2147483647
            
            .. attribute:: hlhostcontroldatasource
            
            	The source of data for the associated host tables.  The statistics in this group reflect all packets on the local network segment attached to the identified interface.  This object may not be modified if the associated hlHostControlStatus object is equal to active(1)
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: hlhostcontrolnldeletes
            
            	The number of times an nlHost entry has been deleted from the nlHost table (for any reason).  If an entry is deleted, then inserted, and then deleted, this counter will be incremented by 2.  To allow for efficient implementation strategies, agents may delay updating this object for short periods of time.  For example, an implementation strategy may allow internal      data structures to differ from those visible via SNMP for short periods of time.  This counter may reflect the internal data structures for those short periods of time.  Note that the table size can be determined by subtracting hlHostControlNlDeletes from hlHostControlNlInserts
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: hlhostcontrolnldroppedframes
            
            	The total number of frames which were received by the probe and therefore not accounted for in the \*StatsDropEvents, but for which the probe chose not to count for the associated      nlHost entries for whatever reason.  Most often, this event occurs when the probe is out of some resources and decides to shed load from this collection.  This count does not include packets that were not counted because they had MAC\-layer errors.  Note that if the nlHostTable is inactive because no protocols are enabled in the protocol directory, this value should be 0.  Note that, unlike the dropEvents counter, this number is the exact number of frames dropped
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: hlhostcontrolnlinserts
            
            	The number of times an nlHost entry has been inserted into the nlHost table.  If an entry is inserted, then deleted, and then inserted, this counter will be incremented by 2.  To allow for efficient implementation strategies, agents may delay updating this object for short periods of time.  For example, an implementation strategy may allow internal data structures to differ from those visible via SNMP for short periods of time.  This counter may reflect the internal data structures for those short periods of time.  Note that the table size can be determined by subtracting hlHostControlNlDeletes from hlHostControlNlInserts
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: hlhostcontrolnlmaxdesiredentries
            
            	The maximum number of entries that are desired in the nlHostTable on behalf of this control entry. The probe will not create more than this number of associated entries in the table, but may choose to create fewer entries in this table for any reason including the lack of resources.  If this object is set to a value less than the current number of entries, enough entries are chosen in an implementation\-dependent manner and deleted so that the number of entries in the table equals the value of this object.  If this value is set to \-1, the probe may create any number of entries in this table.  If the associated hlHostControlStatus object is equal to `active', this object may not be modified.  This object may be used to control how resources are allocated on the probe for the various RMON functions
            	**type**\:  int
            
            	**range:** \-1..2147483647
            
            .. attribute:: hlhostcontrolowner
            
            	The entity that configured this entry and is therefore using the resources assigned to it
            	**type**\:  str
            
            	**length:** 0..127
            
            .. attribute:: hlhostcontrolstatus
            
            	The status of this hlHostControlEntry.  An entry may not exist in the active state unless all objects in the entry have an appropriate value.  If this object is not equal to active(1), all associated entries in the nlHostTable and alHostTable shall be deleted
            	**type**\:   :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            

            """

            _prefix = 'RMON2-MIB'
            _revision = '1996-05-27'

            def __init__(self):
                super(RMON2MIB.Hlhostcontroltable.Hlhostcontrolentry, self).__init__()

                self.yang_name = "hlHostControlEntry"
                self.yang_parent_name = "hlHostControlTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.hlhostcontrolindex = YLeaf(YType.int32, "hlHostControlIndex")

                self.hlhostcontrolaldeletes = YLeaf(YType.uint32, "hlHostControlAlDeletes")

                self.hlhostcontrolaldroppedframes = YLeaf(YType.uint32, "hlHostControlAlDroppedFrames")

                self.hlhostcontrolalinserts = YLeaf(YType.uint32, "hlHostControlAlInserts")

                self.hlhostcontrolalmaxdesiredentries = YLeaf(YType.int32, "hlHostControlAlMaxDesiredEntries")

                self.hlhostcontroldatasource = YLeaf(YType.str, "hlHostControlDataSource")

                self.hlhostcontrolnldeletes = YLeaf(YType.uint32, "hlHostControlNlDeletes")

                self.hlhostcontrolnldroppedframes = YLeaf(YType.uint32, "hlHostControlNlDroppedFrames")

                self.hlhostcontrolnlinserts = YLeaf(YType.uint32, "hlHostControlNlInserts")

                self.hlhostcontrolnlmaxdesiredentries = YLeaf(YType.int32, "hlHostControlNlMaxDesiredEntries")

                self.hlhostcontrolowner = YLeaf(YType.str, "hlHostControlOwner")

                self.hlhostcontrolstatus = YLeaf(YType.enumeration, "hlHostControlStatus")
                self._segment_path = lambda: "hlHostControlEntry" + "[hlHostControlIndex='" + self.hlhostcontrolindex.get() + "']"
                self._absolute_path = lambda: "RMON2-MIB:RMON2-MIB/hlHostControlTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(RMON2MIB.Hlhostcontroltable.Hlhostcontrolentry, ['hlhostcontrolindex', 'hlhostcontrolaldeletes', 'hlhostcontrolaldroppedframes', 'hlhostcontrolalinserts', 'hlhostcontrolalmaxdesiredentries', 'hlhostcontroldatasource', 'hlhostcontrolnldeletes', 'hlhostcontrolnldroppedframes', 'hlhostcontrolnlinserts', 'hlhostcontrolnlmaxdesiredentries', 'hlhostcontrolowner', 'hlhostcontrolstatus'], name, value)


    class Hlmatrixcontroltable(Entity):
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
        	**type**\: list of    :py:class:`Hlmatrixcontrolentry <ydk.models.cisco_ios_xe.RMON2_MIB.RMON2MIB.Hlmatrixcontroltable.Hlmatrixcontrolentry>`
        
        

        """

        _prefix = 'RMON2-MIB'
        _revision = '1996-05-27'

        def __init__(self):
            super(RMON2MIB.Hlmatrixcontroltable, self).__init__()

            self.yang_name = "hlMatrixControlTable"
            self.yang_parent_name = "RMON2-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"hlMatrixControlEntry" : ("hlmatrixcontrolentry", RMON2MIB.Hlmatrixcontroltable.Hlmatrixcontrolentry)}

            self.hlmatrixcontrolentry = YList(self)
            self._segment_path = lambda: "hlMatrixControlTable"
            self._absolute_path = lambda: "RMON2-MIB:RMON2-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(RMON2MIB.Hlmatrixcontroltable, [], name, value)


        class Hlmatrixcontrolentry(Entity):
            """
            A conceptual row in the hlMatrixControlTable.
            
            An example of indexing of this entry is
            hlMatrixControlNlDroppedFrames.1
            
            .. attribute:: hlmatrixcontrolindex  <key>
            
            	An index that uniquely identifies an entry in the hlMatrixControlTable.  Each such entry defines a function that discovers conversations on a particular interface and places statistics about them in the nlMatrixSDTable and the nlMatrixDSTable, and optionally the alMatrixSDTable and alMatrixDSTable, on behalf of this hlMatrixControlEntry
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: hlmatrixcontrolaldeletes
            
            	The number of times an alMatrix entry has been deleted from the alMatrix tables.  If an entry is deleted, then inserted, and then deleted, this counter will be incremented by 2.  The deletion of a conversation from both the alMatrixSDTable and alMatrixDSTable shall be counted as two deletions (even though every deletion from one table must be accompanied by a deletion from the other).  To allow for efficient implementation strategies, agents may delay updating this object for short periods of time.  For example, an implementation strategy may allow internal data structures to differ from those visible via SNMP for short periods of time.  This counter may reflect the internal data structures for those short periods of time.  Note that the table size can be determined by subtracting hlMatrixControlAlDeletes from hlMatrixControlAlInserts
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: hlmatrixcontrolaldroppedframes
            
            	The total number of frames which were received by the probe and therefore not accounted for in the \*StatsDropEvents, but for which the probe chose not to count for this entry for whatever reason.  Most often, this event occurs when the probe is out of some resources and decides to shed load from this collection.  This count does not include packets that were not counted because they had MAC\-layer errors.  Note that if the alMatrixTables are not implemented or are inactive because no protocols are enabled in the protocol directory, this value should be 0.  Note that, unlike the dropEvents counter, this number is the exact number of frames dropped
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: hlmatrixcontrolalinserts
            
            	The number of times an alMatrix entry has been inserted into the alMatrix tables.  If an entry is inserted, then deleted, and then inserted, this counter will be incremented by 2.  The addition of a conversation into both the alMatrixSDTable and alMatrixDSTable shall be counted as two insertions (even though every addition into one table must be accompanied by an insertion into the other).  To allow for efficient implementation strategies, agents may delay updating this object for short periods of time.  For example, an implementation strategy may allow internal data structures to differ from those visible via SNMP for short periods of time.  This counter may reflect the internal      data structures for those short periods of time.  Note that the table size can be determined by subtracting hlMatrixControlAlDeletes from hlMatrixControlAlInserts
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: hlmatrixcontrolalmaxdesiredentries
            
            	The maximum number of entries that are desired in the alMatrix tables on behalf of this control entry. The probe will not create more than this number of associated entries in the table, but may choose to create fewer entries in this table for any reason including the lack of resources.  If this object is set to a value less than the current number of entries, enough entries are chosen in an implementation\-dependent manner and deleted so that the number of entries in the table equals the value of this object.  If this value is set to \-1, the probe may create any number of entries in this table.  If the associated      hlMatrixControlStatus object is equal to `active', this object may not be modified.  This object may be used to control how resources are allocated on the probe for the various RMON functions
            	**type**\:  int
            
            	**range:** \-1..2147483647
            
            .. attribute:: hlmatrixcontroldatasource
            
            	The source of the data for the associated matrix tables.  The statistics in this group reflect all packets on the local network segment attached to the      identified interface.  This object may not be modified if the associated hlMatrixControlStatus object is equal to active(1)
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: hlmatrixcontrolnldeletes
            
            	The number of times an nlMatrix entry has been deleted from the nlMatrix tables (for any reason).  If an entry is deleted, then inserted, and then deleted, this counter will be incremented by 2.  The deletion of a conversation from both the nlMatrixSDTable and nlMatrixDSTable shall be counted as two deletions (even though every deletion from one table must be accompanied by a deletion from the other).  To allow for efficient implementation strategies, agents may delay updating this object for short periods of time.  For example, an implementation strategy may allow internal data structures to differ from those visible via SNMP for short periods of time.  This counter may reflect the internal data structures for those short periods of time.  Note that the table size can be determined by subtracting hlMatrixControlNlDeletes from hlMatrixControlNlInserts
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: hlmatrixcontrolnldroppedframes
            
            	The total number of frames which were received by the probe and therefore not accounted for in the \*StatsDropEvents, but for which the probe chose not to count for this entry for whatever reason.  Most often, this event occurs when the probe is out of some resources and decides to shed load from this collection.  This count does not include packets that were not counted because they had MAC\-layer errors.  Note that if the nlMatrixTables are inactive because no protocols are enabled in the protocol directory, this value should be 0.  Note that, unlike the dropEvents counter, this number is the exact number of frames dropped
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: hlmatrixcontrolnlinserts
            
            	The number of times an nlMatrix entry has been inserted into the nlMatrix tables.  If an entry is inserted, then deleted, and then inserted, this counter will be incremented by 2.  The addition of a conversation into both the nlMatrixSDTable and nlMatrixDSTable shall be counted as two insertions (even though every addition into one table must be accompanied by an insertion into the other).  To allow for efficient implementation strategies, agents may delay updating this object for short periods of time.  For example, an implementation strategy may allow internal data structures to differ from those visible via SNMP for short periods of time.  This counter may reflect the internal data structures for those short periods of time.      Note that the sum of then nlMatrixSDTable and nlMatrixDSTable sizes can be determined by subtracting hlMatrixControlNlDeletes from hlMatrixControlNlInserts
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: hlmatrixcontrolnlmaxdesiredentries
            
            	The maximum number of entries that are desired in the nlMatrix tables on behalf of this control entry. The probe will not create more than this number of associated entries in the table, but may choose to create fewer entries in this table for any reason including the lack of resources.  If this object is set to a value less than the current number of entries, enough entries are chosen in an implementation\-dependent manner and deleted so that the number of entries in the table equals the value of this object.  If this value is set to \-1, the probe may create any number of entries in this table.  If the associated      hlMatrixControlStatus object is equal to `active', this object may not be modified.  This object may be used to control how resources are allocated on the probe for the various RMON functions
            	**type**\:  int
            
            	**range:** \-1..2147483647
            
            .. attribute:: hlmatrixcontrolowner
            
            	The entity that configured this entry and is therefore using the resources assigned to it
            	**type**\:  str
            
            	**length:** 0..127
            
            .. attribute:: hlmatrixcontrolstatus
            
            	The status of this hlMatrixControlEntry.  An entry may not exist in the active state unless all objects in the entry have an appropriate value.  If this object is not equal to active(1), all associated entries in the nlMatrixSDTable, nlMatrixDSTable, alMatrixSDTable, and the alMatrixDSTable shall be deleted by the agent
            	**type**\:   :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            

            """

            _prefix = 'RMON2-MIB'
            _revision = '1996-05-27'

            def __init__(self):
                super(RMON2MIB.Hlmatrixcontroltable.Hlmatrixcontrolentry, self).__init__()

                self.yang_name = "hlMatrixControlEntry"
                self.yang_parent_name = "hlMatrixControlTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.hlmatrixcontrolindex = YLeaf(YType.int32, "hlMatrixControlIndex")

                self.hlmatrixcontrolaldeletes = YLeaf(YType.uint32, "hlMatrixControlAlDeletes")

                self.hlmatrixcontrolaldroppedframes = YLeaf(YType.uint32, "hlMatrixControlAlDroppedFrames")

                self.hlmatrixcontrolalinserts = YLeaf(YType.uint32, "hlMatrixControlAlInserts")

                self.hlmatrixcontrolalmaxdesiredentries = YLeaf(YType.int32, "hlMatrixControlAlMaxDesiredEntries")

                self.hlmatrixcontroldatasource = YLeaf(YType.str, "hlMatrixControlDataSource")

                self.hlmatrixcontrolnldeletes = YLeaf(YType.uint32, "hlMatrixControlNlDeletes")

                self.hlmatrixcontrolnldroppedframes = YLeaf(YType.uint32, "hlMatrixControlNlDroppedFrames")

                self.hlmatrixcontrolnlinserts = YLeaf(YType.uint32, "hlMatrixControlNlInserts")

                self.hlmatrixcontrolnlmaxdesiredentries = YLeaf(YType.int32, "hlMatrixControlNlMaxDesiredEntries")

                self.hlmatrixcontrolowner = YLeaf(YType.str, "hlMatrixControlOwner")

                self.hlmatrixcontrolstatus = YLeaf(YType.enumeration, "hlMatrixControlStatus")
                self._segment_path = lambda: "hlMatrixControlEntry" + "[hlMatrixControlIndex='" + self.hlmatrixcontrolindex.get() + "']"
                self._absolute_path = lambda: "RMON2-MIB:RMON2-MIB/hlMatrixControlTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(RMON2MIB.Hlmatrixcontroltable.Hlmatrixcontrolentry, ['hlmatrixcontrolindex', 'hlmatrixcontrolaldeletes', 'hlmatrixcontrolaldroppedframes', 'hlmatrixcontrolalinserts', 'hlmatrixcontrolalmaxdesiredentries', 'hlmatrixcontroldatasource', 'hlmatrixcontrolnldeletes', 'hlmatrixcontrolnldroppedframes', 'hlmatrixcontrolnlinserts', 'hlmatrixcontrolnlmaxdesiredentries', 'hlmatrixcontrolowner', 'hlmatrixcontrolstatus'], name, value)


    class Netconfigtable(Entity):
        """
        A table of netConfigEntries.
        
        .. attribute:: netconfigentry
        
        	A set of configuration parameters for a particular network interface on this device. If the device has no network interface, this table is empty.  The index is composed of the ifIndex assigned to the corresponding interface
        	**type**\: list of    :py:class:`Netconfigentry <ydk.models.cisco_ios_xe.RMON2_MIB.RMON2MIB.Netconfigtable.Netconfigentry>`
        
        

        """

        _prefix = 'RMON2-MIB'
        _revision = '1996-05-27'

        def __init__(self):
            super(RMON2MIB.Netconfigtable, self).__init__()

            self.yang_name = "netConfigTable"
            self.yang_parent_name = "RMON2-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"netConfigEntry" : ("netconfigentry", RMON2MIB.Netconfigtable.Netconfigentry)}

            self.netconfigentry = YList(self)
            self._segment_path = lambda: "netConfigTable"
            self._absolute_path = lambda: "RMON2-MIB:RMON2-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(RMON2MIB.Netconfigtable, [], name, value)


        class Netconfigentry(Entity):
            """
            A set of configuration parameters for a particular
            network interface on this device. If the device has no network
            interface, this table is empty.
            
            The index is composed of the ifIndex assigned to the
            corresponding interface.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.RFC1213_MIB.RFC1213MIB.Iftable.Ifentry>`
            
            .. attribute:: netconfigipaddress
            
            	The IP address of this Net interface.  The default value for this object is 0.0.0.0.  If either the netConfigIPAddress or netConfigSubnetMask are 0.0.0.0, then when the device boots, it may use BOOTP to try to figure out what these values should be. If BOOTP fails, before the device can talk on the network, this value must be configured (e.g., through a terminal attached to the device). If BOOTP is      used, care should be taken to not send BOOTP broadcasts too frequently and to eventually send very infrequently if no replies are received
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: netconfigstatus
            
            	The status of this netConfigEntry.  An entry may not exist in the active state unless all objects in the entry have an appropriate value
            	**type**\:   :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            .. attribute:: netconfigsubnetmask
            
            	The subnet mask of this Net interface.  The default value for this object is 0.0.0.0.  If either the netConfigIPAddress or netConfigSubnetMask are 0.0.0.0, then when the device boots, it may use BOOTP to try to figure out what these values should be. If BOOTP fails, before the device can talk on the network, this value must be configured (e.g., through a terminal attached to the device). If BOOTP is used, care should be taken to not send BOOTP broadcasts too frequently and to eventually send very infrequently if no replies are received
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            

            """

            _prefix = 'RMON2-MIB'
            _revision = '1996-05-27'

            def __init__(self):
                super(RMON2MIB.Netconfigtable.Netconfigentry, self).__init__()

                self.yang_name = "netConfigEntry"
                self.yang_parent_name = "netConfigTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.netconfigipaddress = YLeaf(YType.str, "netConfigIPAddress")

                self.netconfigstatus = YLeaf(YType.enumeration, "netConfigStatus")

                self.netconfigsubnetmask = YLeaf(YType.str, "netConfigSubnetMask")
                self._segment_path = lambda: "netConfigEntry" + "[ifIndex='" + self.ifindex.get() + "']"
                self._absolute_path = lambda: "RMON2-MIB:RMON2-MIB/netConfigTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(RMON2MIB.Netconfigtable.Netconfigentry, ['ifindex', 'netconfigipaddress', 'netconfigstatus', 'netconfigsubnetmask'], name, value)


    class Nlhosttable(Entity):
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
        	**type**\: list of    :py:class:`Nlhostentry <ydk.models.cisco_ios_xe.RMON2_MIB.RMON2MIB.Nlhosttable.Nlhostentry>`
        
        

        """

        _prefix = 'RMON2-MIB'
        _revision = '1996-05-27'

        def __init__(self):
            super(RMON2MIB.Nlhosttable, self).__init__()

            self.yang_name = "nlHostTable"
            self.yang_parent_name = "RMON2-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"nlHostEntry" : ("nlhostentry", RMON2MIB.Nlhosttable.Nlhostentry)}

            self.nlhostentry = YList(self)
            self._segment_path = lambda: "nlHostTable"
            self._absolute_path = lambda: "RMON2-MIB:RMON2-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(RMON2MIB.Nlhosttable, [], name, value)


        class Nlhostentry(Entity):
            """
            A conceptual row in the nlHostTable.
            
            The hlHostControlIndex value in the index identifies the
            hlHostControlEntry on whose behalf this entry was created.
            The protocolDirLocalIndex value in the index identifies the
            network layer protocol of the nlHostAddress.
            
            An example of the indexing of this entry is
            nlHostOutPkts.1.783495.18.4.128.2.6.6.
            
            .. attribute:: hlhostcontrolindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..65535
            
            	**refers to**\:  :py:class:`hlhostcontrolindex <ydk.models.cisco_ios_xe.RMON2_MIB.RMON2MIB.Hlhostcontroltable.Hlhostcontrolentry>`
            
            .. attribute:: nlhosttimemark  <key>
            
            	A TimeFilter for this entry.  See the TimeFilter textual convention to see how this works
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: protocoldirlocalindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`protocoldirlocalindex <ydk.models.cisco_ios_xe.RMON2_MIB.RMON2MIB.Protocoldirtable.Protocoldirentry>`
            
            .. attribute:: nlhostaddress  <key>
            
            	The network address for this nlHostEntry.  This is represented as an octet string with specific semantics and length as identified by the protocolDirLocalIndex component of the index.  For example, if the protocolDirLocalIndex indicates an encapsulation of ip, this object is encoded as a length octet of 4, followed by the 4 octets of the ip address, in network byte order
            	**type**\:  str
            
            .. attribute:: nlhostcreatetime
            
            	The value of sysUpTime when this entry was last activated. This can be used by the management station to ensure that the entry has not been deleted and recreated between polls
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nlhostinoctets
            
            	The number of octets transmitted to this address since it was added to the nlHostTable (excluding framing bits but including FCS octets), excluding those octets in packets that contained errors.  Note this doesn't count just those octets in the particular protocol frames, but includes the entire packet that contained the protocol
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nlhostinpkts
            
            	The number of packets without errors transmitted to this address since it was added to the nlHostTable.  Note that this is the number of link\-layer packets, so if a single network\-layer packet is fragmented into several link\-layer frames, this counter is incremented several times
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nlhostoutmacnonunicastpkts
            
            	The number of packets without errors transmitted by this address that were directed to any MAC broadcast addresses or to any MAC multicast addresses since this host was added to the nlHostTable. Note that this is the number of link\-layer packets, so if a single network\-layer packet is fragmented into several link\-layer frames, this counter is incremented several times
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nlhostoutoctets
            
            	The number of octets transmitted by this address since it was added to the nlHostTable (excluding framing bits but including FCS octets), excluding those octets in packets that contained errors.  Note this doesn't count just those octets in the particular protocol frames, but includes the entire packet that contained the protocol
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nlhostoutpkts
            
            	The number of packets without errors transmitted by      this address since it was added to the nlHostTable.  Note that this is the number of link\-layer packets, so if a single network\-layer packet is fragmented into several link\-layer frames, this counter is incremented several times
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'RMON2-MIB'
            _revision = '1996-05-27'

            def __init__(self):
                super(RMON2MIB.Nlhosttable.Nlhostentry, self).__init__()

                self.yang_name = "nlHostEntry"
                self.yang_parent_name = "nlHostTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.hlhostcontrolindex = YLeaf(YType.str, "hlHostControlIndex")

                self.nlhosttimemark = YLeaf(YType.uint32, "nlHostTimeMark")

                self.protocoldirlocalindex = YLeaf(YType.str, "protocolDirLocalIndex")

                self.nlhostaddress = YLeaf(YType.str, "nlHostAddress")

                self.nlhostcreatetime = YLeaf(YType.uint32, "nlHostCreateTime")

                self.nlhostinoctets = YLeaf(YType.uint32, "nlHostInOctets")

                self.nlhostinpkts = YLeaf(YType.uint32, "nlHostInPkts")

                self.nlhostoutmacnonunicastpkts = YLeaf(YType.uint32, "nlHostOutMacNonUnicastPkts")

                self.nlhostoutoctets = YLeaf(YType.uint32, "nlHostOutOctets")

                self.nlhostoutpkts = YLeaf(YType.uint32, "nlHostOutPkts")
                self._segment_path = lambda: "nlHostEntry" + "[hlHostControlIndex='" + self.hlhostcontrolindex.get() + "']" + "[nlHostTimeMark='" + self.nlhosttimemark.get() + "']" + "[protocolDirLocalIndex='" + self.protocoldirlocalindex.get() + "']" + "[nlHostAddress='" + self.nlhostaddress.get() + "']"
                self._absolute_path = lambda: "RMON2-MIB:RMON2-MIB/nlHostTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(RMON2MIB.Nlhosttable.Nlhostentry, ['hlhostcontrolindex', 'nlhosttimemark', 'protocoldirlocalindex', 'nlhostaddress', 'nlhostcreatetime', 'nlhostinoctets', 'nlhostinpkts', 'nlhostoutmacnonunicastpkts', 'nlhostoutoctets', 'nlhostoutpkts'], name, value)


    class Nlmatrixdstable(Entity):
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
        	**type**\: list of    :py:class:`Nlmatrixdsentry <ydk.models.cisco_ios_xe.RMON2_MIB.RMON2MIB.Nlmatrixdstable.Nlmatrixdsentry>`
        
        

        """

        _prefix = 'RMON2-MIB'
        _revision = '1996-05-27'

        def __init__(self):
            super(RMON2MIB.Nlmatrixdstable, self).__init__()

            self.yang_name = "nlMatrixDSTable"
            self.yang_parent_name = "RMON2-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"nlMatrixDSEntry" : ("nlmatrixdsentry", RMON2MIB.Nlmatrixdstable.Nlmatrixdsentry)}

            self.nlmatrixdsentry = YList(self)
            self._segment_path = lambda: "nlMatrixDSTable"
            self._absolute_path = lambda: "RMON2-MIB:RMON2-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(RMON2MIB.Nlmatrixdstable, [], name, value)


        class Nlmatrixdsentry(Entity):
            """
            A conceptual row in the nlMatrixDSTable.
            
            The hlMatrixControlIndex value in the index identifies the
            hlMatrixControlEntry on whose behalf this entry was created.
            The protocolDirLocalIndex value in the index identifies the
            network layer protocol of the nlMatrixDSSourceAddress and
            nlMatrixDSDestAddress.
            
            An example of the indexing of this table is
            nlMatrixDSPkts.1.783495.18.4.128.2.6.7.4.128.2.6.6
            
            .. attribute:: hlmatrixcontrolindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..65535
            
            	**refers to**\:  :py:class:`hlmatrixcontrolindex <ydk.models.cisco_ios_xe.RMON2_MIB.RMON2MIB.Hlmatrixcontroltable.Hlmatrixcontrolentry>`
            
            .. attribute:: nlmatrixdstimemark  <key>
            
            	A TimeFilter for this entry.  See the TimeFilter textual convention to see how this works
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: protocoldirlocalindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`protocoldirlocalindex <ydk.models.cisco_ios_xe.RMON2_MIB.RMON2MIB.Protocoldirtable.Protocoldirentry>`
            
            .. attribute:: nlmatrixdsdestaddress  <key>
            
            	The network destination address for this nlMatrixDSEntry.  This is represented as an octet string with specific semantics and length as identified by the protocolDirLocalIndex component of the index.  For example, if the protocolDirLocalIndex indicates an encapsulation of ip, this object is encoded as a length octet of 4, followed by the 4 octets of the ip address, in network byte order
            	**type**\:  str
            
            .. attribute:: nlmatrixdssourceaddress  <key>
            
            	The network source address for this nlMatrixDSEntry.  This is represented as an octet string with specific semantics and length as identified by the protocolDirLocalIndex component of the index.  For example, if the protocolDirLocalIndex indicates an encapsulation of ip, this object is encoded as a length octet of 4, followed by the 4 octets of the ip address, in network byte order
            	**type**\:  str
            
            .. attribute:: nlmatrixdscreatetime
            
            	The value of sysUpTime when this entry was last activated. This can be used by the management station to ensure that the entry has not been deleted and recreated between polls
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nlmatrixdsoctets
            
            	The number of octets transmitted from the source address to the destination address since this entry was added to the nlMatrixDSTable (excluding framing bits but including FCS octets), excluding those octets in packets that contained errors.  Note this doesn't count just those octets in the particular protocol frames, but includes the entire packet that contained the protocol
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nlmatrixdspkts
            
            	The number of packets without errors transmitted from the source address to the destination address since this entry was added to the nlMatrixDSTable.  Note that this is the number of link\-layer packets, so if a single network\-layer packet is fragmented into several link\-layer frames, this counter is incremented several times
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'RMON2-MIB'
            _revision = '1996-05-27'

            def __init__(self):
                super(RMON2MIB.Nlmatrixdstable.Nlmatrixdsentry, self).__init__()

                self.yang_name = "nlMatrixDSEntry"
                self.yang_parent_name = "nlMatrixDSTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.hlmatrixcontrolindex = YLeaf(YType.str, "hlMatrixControlIndex")

                self.nlmatrixdstimemark = YLeaf(YType.uint32, "nlMatrixDSTimeMark")

                self.protocoldirlocalindex = YLeaf(YType.str, "protocolDirLocalIndex")

                self.nlmatrixdsdestaddress = YLeaf(YType.str, "nlMatrixDSDestAddress")

                self.nlmatrixdssourceaddress = YLeaf(YType.str, "nlMatrixDSSourceAddress")

                self.nlmatrixdscreatetime = YLeaf(YType.uint32, "nlMatrixDSCreateTime")

                self.nlmatrixdsoctets = YLeaf(YType.uint32, "nlMatrixDSOctets")

                self.nlmatrixdspkts = YLeaf(YType.uint32, "nlMatrixDSPkts")
                self._segment_path = lambda: "nlMatrixDSEntry" + "[hlMatrixControlIndex='" + self.hlmatrixcontrolindex.get() + "']" + "[nlMatrixDSTimeMark='" + self.nlmatrixdstimemark.get() + "']" + "[protocolDirLocalIndex='" + self.protocoldirlocalindex.get() + "']" + "[nlMatrixDSDestAddress='" + self.nlmatrixdsdestaddress.get() + "']" + "[nlMatrixDSSourceAddress='" + self.nlmatrixdssourceaddress.get() + "']"
                self._absolute_path = lambda: "RMON2-MIB:RMON2-MIB/nlMatrixDSTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(RMON2MIB.Nlmatrixdstable.Nlmatrixdsentry, ['hlmatrixcontrolindex', 'nlmatrixdstimemark', 'protocoldirlocalindex', 'nlmatrixdsdestaddress', 'nlmatrixdssourceaddress', 'nlmatrixdscreatetime', 'nlmatrixdsoctets', 'nlmatrixdspkts'], name, value)


    class Nlmatrixsdtable(Entity):
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
        	**type**\: list of    :py:class:`Nlmatrixsdentry <ydk.models.cisco_ios_xe.RMON2_MIB.RMON2MIB.Nlmatrixsdtable.Nlmatrixsdentry>`
        
        

        """

        _prefix = 'RMON2-MIB'
        _revision = '1996-05-27'

        def __init__(self):
            super(RMON2MIB.Nlmatrixsdtable, self).__init__()

            self.yang_name = "nlMatrixSDTable"
            self.yang_parent_name = "RMON2-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"nlMatrixSDEntry" : ("nlmatrixsdentry", RMON2MIB.Nlmatrixsdtable.Nlmatrixsdentry)}

            self.nlmatrixsdentry = YList(self)
            self._segment_path = lambda: "nlMatrixSDTable"
            self._absolute_path = lambda: "RMON2-MIB:RMON2-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(RMON2MIB.Nlmatrixsdtable, [], name, value)


        class Nlmatrixsdentry(Entity):
            """
            A conceptual row in the nlMatrixSDTable.
            
            The hlMatrixControlIndex value in the index identifies the
            hlMatrixControlEntry on whose behalf this entry was created.
            The protocolDirLocalIndex value in the index identifies the
            network layer protocol of the nlMatrixSDSourceAddress and
            nlMatrixSDDestAddress.
            
            An example of the indexing of this table is
            nlMatrixSDPkts.1.783495.18.4.128.2.6.6.4.128.2.6.7
            
            .. attribute:: hlmatrixcontrolindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..65535
            
            	**refers to**\:  :py:class:`hlmatrixcontrolindex <ydk.models.cisco_ios_xe.RMON2_MIB.RMON2MIB.Hlmatrixcontroltable.Hlmatrixcontrolentry>`
            
            .. attribute:: nlmatrixsdtimemark  <key>
            
            	A TimeFilter for this entry.  See the TimeFilter textual convention to see how this works
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: protocoldirlocalindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`protocoldirlocalindex <ydk.models.cisco_ios_xe.RMON2_MIB.RMON2MIB.Protocoldirtable.Protocoldirentry>`
            
            .. attribute:: nlmatrixsdsourceaddress  <key>
            
            	The network source address for this nlMatrixSDEntry.  This is represented as an octet string with specific semantics and length as identified by the protocolDirLocalIndex component of the index.  For example, if the protocolDirLocalIndex indicates an encapsulation of ip, this object is encoded as a length octet of 4, followed by the 4 octets of the ip address, in network byte order
            	**type**\:  str
            
            .. attribute:: nlmatrixsddestaddress  <key>
            
            	The network destination address for this nlMatrixSDEntry.  This is represented as an octet string with specific semantics and length as identified by the protocolDirLocalIndex component of the index.  For example, if the protocolDirLocalIndex indicates an encapsulation of ip, this object is encoded as a length octet of 4, followed by the 4 octets of the ip address, in network byte order
            	**type**\:  str
            
            .. attribute:: nlmatrixsdcreatetime
            
            	The value of sysUpTime when this entry was last activated. This can be used by the management station to ensure that the entry has not been deleted and recreated between polls
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nlmatrixsdoctets
            
            	The number of octets transmitted from the source address to the destination address since this entry was added to the nlMatrixSDTable (excluding framing bits but including FCS octets), excluding those octets in packets that contained errors.  Note this doesn't count just those octets in the particular protocol frames, but includes the entire packet that contained the protocol
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nlmatrixsdpkts
            
            	The number of packets without errors transmitted from the source address to the destination address since this entry was added to the nlMatrixSDTable.  Note that this is the number of link\-layer packets, so if a single network\-layer packet is fragmented into several link\-layer frames, this counter is incremented several times
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'RMON2-MIB'
            _revision = '1996-05-27'

            def __init__(self):
                super(RMON2MIB.Nlmatrixsdtable.Nlmatrixsdentry, self).__init__()

                self.yang_name = "nlMatrixSDEntry"
                self.yang_parent_name = "nlMatrixSDTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.hlmatrixcontrolindex = YLeaf(YType.str, "hlMatrixControlIndex")

                self.nlmatrixsdtimemark = YLeaf(YType.uint32, "nlMatrixSDTimeMark")

                self.protocoldirlocalindex = YLeaf(YType.str, "protocolDirLocalIndex")

                self.nlmatrixsdsourceaddress = YLeaf(YType.str, "nlMatrixSDSourceAddress")

                self.nlmatrixsddestaddress = YLeaf(YType.str, "nlMatrixSDDestAddress")

                self.nlmatrixsdcreatetime = YLeaf(YType.uint32, "nlMatrixSDCreateTime")

                self.nlmatrixsdoctets = YLeaf(YType.uint32, "nlMatrixSDOctets")

                self.nlmatrixsdpkts = YLeaf(YType.uint32, "nlMatrixSDPkts")
                self._segment_path = lambda: "nlMatrixSDEntry" + "[hlMatrixControlIndex='" + self.hlmatrixcontrolindex.get() + "']" + "[nlMatrixSDTimeMark='" + self.nlmatrixsdtimemark.get() + "']" + "[protocolDirLocalIndex='" + self.protocoldirlocalindex.get() + "']" + "[nlMatrixSDSourceAddress='" + self.nlmatrixsdsourceaddress.get() + "']" + "[nlMatrixSDDestAddress='" + self.nlmatrixsddestaddress.get() + "']"
                self._absolute_path = lambda: "RMON2-MIB:RMON2-MIB/nlMatrixSDTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(RMON2MIB.Nlmatrixsdtable.Nlmatrixsdentry, ['hlmatrixcontrolindex', 'nlmatrixsdtimemark', 'protocoldirlocalindex', 'nlmatrixsdsourceaddress', 'nlmatrixsddestaddress', 'nlmatrixsdcreatetime', 'nlmatrixsdoctets', 'nlmatrixsdpkts'], name, value)


    class Nlmatrixtopncontroltable(Entity):
        """
        A set of parameters that control the creation of a
        report of the top N matrix entries according to
        a selected metric.
        
        .. attribute:: nlmatrixtopncontrolentry
        
        	A conceptual row in the nlMatrixTopNControlTable.  An example of the indexing of this table is nlMatrixTopNControlDuration.3
        	**type**\: list of    :py:class:`Nlmatrixtopncontrolentry <ydk.models.cisco_ios_xe.RMON2_MIB.RMON2MIB.Nlmatrixtopncontroltable.Nlmatrixtopncontrolentry>`
        
        

        """

        _prefix = 'RMON2-MIB'
        _revision = '1996-05-27'

        def __init__(self):
            super(RMON2MIB.Nlmatrixtopncontroltable, self).__init__()

            self.yang_name = "nlMatrixTopNControlTable"
            self.yang_parent_name = "RMON2-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"nlMatrixTopNControlEntry" : ("nlmatrixtopncontrolentry", RMON2MIB.Nlmatrixtopncontroltable.Nlmatrixtopncontrolentry)}

            self.nlmatrixtopncontrolentry = YList(self)
            self._segment_path = lambda: "nlMatrixTopNControlTable"
            self._absolute_path = lambda: "RMON2-MIB:RMON2-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(RMON2MIB.Nlmatrixtopncontroltable, [], name, value)


        class Nlmatrixtopncontrolentry(Entity):
            """
            A conceptual row in the nlMatrixTopNControlTable.
            
            An example of the indexing of this table is
            nlMatrixTopNControlDuration.3
            
            .. attribute:: nlmatrixtopncontrolindex  <key>
            
            	An index that uniquely identifies an entry in the nlMatrixTopNControlTable.  Each such entry defines one top N report prepared for one interface
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: nlmatrixtopncontrolduration
            
            	The number of seconds that this report has collected during the last sampling interval.  When the associated nlMatrixTopNControlTimeRemaining object is set, this object shall be set by the probe to the same value and shall not be modified until the next time the nlMatrixTopNControlTimeRemaining is set. This value shall be zero if no reports have been requested for this nlMatrixTopNControlEntry
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: nlmatrixtopncontrolgeneratedreports
            
            	The number of reports that have been generated by this entry
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nlmatrixtopncontrolgrantedsize
            
            	The maximum number of matrix entries in this report.  When the associated nlMatrixTopNControlRequestedSize object is created or modified, the probe should set this object as closely to the requested value as is possible for the particular implementation and available resources. The probe must not lower this value except as a result of a set to the associated nlMatrixTopNControlRequestedSize object.  If the value of nlMatrixTopNControlRateBase is equal to nlMatrixTopNPkts, when the next topN report is generated, matrix entries with the highest value of nlMatrixTopNPktRate shall be placed in this table in decreasing order of this rate until there is no more room or until there are no more      matrix entries.  If the value of nlMatrixTopNControlRateBase is equal to nlMatrixTopNOctets, when the next topN report is generated, matrix entries with the highest value of nlMatrixTopNOctetRate shall be placed in this table in decreasing order of this rate until there is no more room or until there are no more matrix entries.  It is an implementation\-specific matter how entries with the same value of nlMatrixTopNPktRate or nlMatrixTopNOctetRate are sorted.  It is also an implementation\-specific matter as to whether or not zero\-valued entries are available
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: nlmatrixtopncontrolmatrixindex
            
            	The nlMatrix[SD/DS] table for which a top N report will be prepared on behalf of this entry.  The nlMatrix[SD/DS] table is identified by the value of the hlMatrixControlIndex for that table \- that value is used here to identify the particular table.  This object may not be modified if the associated nlMatrixTopNControlStatus object is equal to active(1)
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: nlmatrixtopncontrolowner
            
            	The entity that configured this entry and is therefore using the resources assigned to it
            	**type**\:  str
            
            	**length:** 0..127
            
            .. attribute:: nlmatrixtopncontrolratebase
            
            	The variable for each nlMatrix[SD/DS] entry that the nlMatrixTopNEntries are sorted by.      This object may not be modified if the associated nlMatrixTopNControlStatus object is equal to active(1)
            	**type**\:   :py:class:`Nlmatrixtopncontrolratebase <ydk.models.cisco_ios_xe.RMON2_MIB.RMON2MIB.Nlmatrixtopncontroltable.Nlmatrixtopncontrolentry.Nlmatrixtopncontrolratebase>`
            
            .. attribute:: nlmatrixtopncontrolrequestedsize
            
            	The maximum number of matrix entries requested for this report.  When this object is created or modified, the probe should set nlMatrixTopNControlGrantedSize as closely to this object as is possible for the particular probe implementation and available resources
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: nlmatrixtopncontrolstarttime
            
            	The value of sysUpTime when this top N report was last started.  In other words, this is the time that the associated nlMatrixTopNControlTimeRemaining object was modified to start the requested report or the time the report was last automatically (re)started.  This object may be used by the management station to determine if a report was missed or not
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nlmatrixtopncontrolstatus
            
            	The status of this nlMatrixTopNControlEntry.  An entry may not exist in the active state unless all objects in the entry have an appropriate value.      If this object is not equal to active(1), all associated entries in the nlMatrixTopNTable shall be deleted by the agent
            	**type**\:   :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            .. attribute:: nlmatrixtopncontroltimeremaining
            
            	The number of seconds left in the report currently being collected.  When this object is modified by the management station, a new collection is started, possibly aborting a currently running report.  The new value is used as the requested duration of this report, and is immediately loaded into the associated nlMatrixTopNControlDuration object. When the report finishes, the probe will automatically start another collection with the same initial value of nlMatrixTopNControlTimeRemaining.  Thus the management station may simply read the resulting reports repeatedly, checking the startTime and duration each time to ensure that a report was not missed or that the report parameters were not changed.  While the value of this object is non\-zero, it decrements by one per second until it reaches zero.  At the time that this object decrements to zero, the report is made accessible in the nlMatrixTopNTable, overwriting any report that may be there.  When this object is modified by the management station, any associated entries in the nlMatrixTopNTable shall be deleted.  (Note that this is a different algorithm than the one used in the hostTopNTable)
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            

            """

            _prefix = 'RMON2-MIB'
            _revision = '1996-05-27'

            def __init__(self):
                super(RMON2MIB.Nlmatrixtopncontroltable.Nlmatrixtopncontrolentry, self).__init__()

                self.yang_name = "nlMatrixTopNControlEntry"
                self.yang_parent_name = "nlMatrixTopNControlTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.nlmatrixtopncontrolindex = YLeaf(YType.int32, "nlMatrixTopNControlIndex")

                self.nlmatrixtopncontrolduration = YLeaf(YType.int32, "nlMatrixTopNControlDuration")

                self.nlmatrixtopncontrolgeneratedreports = YLeaf(YType.uint32, "nlMatrixTopNControlGeneratedReports")

                self.nlmatrixtopncontrolgrantedsize = YLeaf(YType.int32, "nlMatrixTopNControlGrantedSize")

                self.nlmatrixtopncontrolmatrixindex = YLeaf(YType.int32, "nlMatrixTopNControlMatrixIndex")

                self.nlmatrixtopncontrolowner = YLeaf(YType.str, "nlMatrixTopNControlOwner")

                self.nlmatrixtopncontrolratebase = YLeaf(YType.enumeration, "nlMatrixTopNControlRateBase")

                self.nlmatrixtopncontrolrequestedsize = YLeaf(YType.int32, "nlMatrixTopNControlRequestedSize")

                self.nlmatrixtopncontrolstarttime = YLeaf(YType.uint32, "nlMatrixTopNControlStartTime")

                self.nlmatrixtopncontrolstatus = YLeaf(YType.enumeration, "nlMatrixTopNControlStatus")

                self.nlmatrixtopncontroltimeremaining = YLeaf(YType.int32, "nlMatrixTopNControlTimeRemaining")
                self._segment_path = lambda: "nlMatrixTopNControlEntry" + "[nlMatrixTopNControlIndex='" + self.nlmatrixtopncontrolindex.get() + "']"
                self._absolute_path = lambda: "RMON2-MIB:RMON2-MIB/nlMatrixTopNControlTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(RMON2MIB.Nlmatrixtopncontroltable.Nlmatrixtopncontrolentry, ['nlmatrixtopncontrolindex', 'nlmatrixtopncontrolduration', 'nlmatrixtopncontrolgeneratedreports', 'nlmatrixtopncontrolgrantedsize', 'nlmatrixtopncontrolmatrixindex', 'nlmatrixtopncontrolowner', 'nlmatrixtopncontrolratebase', 'nlmatrixtopncontrolrequestedsize', 'nlmatrixtopncontrolstarttime', 'nlmatrixtopncontrolstatus', 'nlmatrixtopncontroltimeremaining'], name, value)

            class Nlmatrixtopncontrolratebase(Enum):
                """
                Nlmatrixtopncontrolratebase

                The variable for each nlMatrix[SD/DS] entry that the

                nlMatrixTopNEntries are sorted by.

                This object may not be modified if the associated

                nlMatrixTopNControlStatus object is equal to active(1).

                .. data:: nlMatrixTopNPkts = 1

                .. data:: nlMatrixTopNOctets = 2

                """

                nlMatrixTopNPkts = Enum.YLeaf(1, "nlMatrixTopNPkts")

                nlMatrixTopNOctets = Enum.YLeaf(2, "nlMatrixTopNOctets")



    class Nlmatrixtopntable(Entity):
        """
        A set of statistics for those network layer matrix entries
        that have counted the highest number of octets or packets.
        
        .. attribute:: nlmatrixtopnentry
        
        	A conceptual row in the nlMatrixTopNTable.  The nlMatrixTopNControlIndex value in the index identifies the nlMatrixTopNControlEntry on whose behalf this entry was created.  An example of the indexing of this table is nlMatrixTopNPktRate.3.10
        	**type**\: list of    :py:class:`Nlmatrixtopnentry <ydk.models.cisco_ios_xe.RMON2_MIB.RMON2MIB.Nlmatrixtopntable.Nlmatrixtopnentry>`
        
        

        """

        _prefix = 'RMON2-MIB'
        _revision = '1996-05-27'

        def __init__(self):
            super(RMON2MIB.Nlmatrixtopntable, self).__init__()

            self.yang_name = "nlMatrixTopNTable"
            self.yang_parent_name = "RMON2-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"nlMatrixTopNEntry" : ("nlmatrixtopnentry", RMON2MIB.Nlmatrixtopntable.Nlmatrixtopnentry)}

            self.nlmatrixtopnentry = YList(self)
            self._segment_path = lambda: "nlMatrixTopNTable"
            self._absolute_path = lambda: "RMON2-MIB:RMON2-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(RMON2MIB.Nlmatrixtopntable, [], name, value)


        class Nlmatrixtopnentry(Entity):
            """
            A conceptual row in the nlMatrixTopNTable.
            
            The nlMatrixTopNControlIndex value in the index identifies the
            nlMatrixTopNControlEntry on whose behalf this entry was
            created.
            
            An example of the indexing of this table is
            nlMatrixTopNPktRate.3.10
            
            .. attribute:: nlmatrixtopncontrolindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..65535
            
            	**refers to**\:  :py:class:`nlmatrixtopncontrolindex <ydk.models.cisco_ios_xe.RMON2_MIB.RMON2MIB.Nlmatrixtopncontroltable.Nlmatrixtopncontrolentry>`
            
            .. attribute:: nlmatrixtopnindex  <key>
            
            	An index that uniquely identifies an entry in the nlMatrixTopNTable among those in the same report.      This index is between 1 and N, where N is the number of entries in this report.  If the value of nlMatrixTopNControlRateBase is equal to nlMatrixTopNPkts, increasing values of nlMatrixTopNIndex shall be assigned to entries with decreasing values of nlMatrixTopNPktRate until index N is assigned or there are no more nlMatrixTopNEntries.  If the value of nlMatrixTopNControlRateBase is equal to nlMatrixTopNOctets, increasing values of nlMatrixTopNIndex shall be assigned to entries with decreasing values of nlMatrixTopNOctetRate until index N is assigned or there are no more nlMatrixTopNEntries
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: nlmatrixtopndestaddress
            
            	The network layer address of the destination host in this conversation.  This is represented as an octet string with specific semantics and length as identified by the associated nlMatrixTopNProtocolDirLocalIndex.  For example, if the nlMatrixTopNProtocolDirLocalIndex indicates an encapsulation of ip, this object is encoded as a length octet of 4, followed by the 4 octets of the ip address, in network byte order
            	**type**\:  str
            
            .. attribute:: nlmatrixtopnoctetrate
            
            	The number of octets seen from the source host to the destination host during this sampling interval, counted using the rules for counting the nlMatrixSDOctets object.  If the value of nlMatrixTopNControlRateBase is nlMatrixTopNOctets, this variable will be used to sort this report
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nlmatrixtopnpktrate
            
            	The number of packets seen from the source host to the destination host during this sampling interval, counted using the rules for counting the nlMatrixSDPkts object. If the value of nlMatrixTopNControlRateBase is nlMatrixTopNPkts, this variable will be used to sort this report
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nlmatrixtopnprotocoldirlocalindex
            
            	The protocolDirLocalIndex of the network layer protocol of this entry's network address
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: nlmatrixtopnreverseoctetrate
            
            	The number of octets seen from the destination host to the source host during this sampling interval, counted using the rules for counting the nlMatrixDSOctets object (note that the corresponding nlMatrixSDOctets object selected is the one whose source address is equal to nlMatrixTopNDestAddress and whose destination address is equal to nlMatrixTopNSourceAddress.)  Note that if the value of nlMatrixTopNControlRateBase is equal to nlMatrixTopNOctets, the sort of topN entries is based entirely on nlMatrixTopNOctetRate, and not on the value of this object
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nlmatrixtopnreversepktrate
            
            	The number of packets seen from the destination host to the source host during this sampling interval, counted using the rules for counting the nlMatrixSDPkts object (note that the corresponding nlMatrixSDPkts object selected is the one whose source address is equal to nlMatrixTopNDestAddress and whose destination address is equal to nlMatrixTopNSourceAddress.)  Note that if the value of nlMatrixTopNControlRateBase is equal to nlMatrixTopNPkts, the sort of topN entries is based entirely on nlMatrixTopNPktRate, and not on the value of this object
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nlmatrixtopnsourceaddress
            
            	The network layer address of the source host in this conversation.  This is represented as an octet string with specific semantics and length as identified by the associated nlMatrixTopNProtocolDirLocalIndex.  For example, if the protocolDirLocalIndex indicates an encapsulation of ip, this object is encoded as a length octet of 4, followed by the 4 octets of the ip address, in network byte order
            	**type**\:  str
            
            

            """

            _prefix = 'RMON2-MIB'
            _revision = '1996-05-27'

            def __init__(self):
                super(RMON2MIB.Nlmatrixtopntable.Nlmatrixtopnentry, self).__init__()

                self.yang_name = "nlMatrixTopNEntry"
                self.yang_parent_name = "nlMatrixTopNTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.nlmatrixtopncontrolindex = YLeaf(YType.str, "nlMatrixTopNControlIndex")

                self.nlmatrixtopnindex = YLeaf(YType.int32, "nlMatrixTopNIndex")

                self.nlmatrixtopndestaddress = YLeaf(YType.str, "nlMatrixTopNDestAddress")

                self.nlmatrixtopnoctetrate = YLeaf(YType.uint32, "nlMatrixTopNOctetRate")

                self.nlmatrixtopnpktrate = YLeaf(YType.uint32, "nlMatrixTopNPktRate")

                self.nlmatrixtopnprotocoldirlocalindex = YLeaf(YType.int32, "nlMatrixTopNProtocolDirLocalIndex")

                self.nlmatrixtopnreverseoctetrate = YLeaf(YType.uint32, "nlMatrixTopNReverseOctetRate")

                self.nlmatrixtopnreversepktrate = YLeaf(YType.uint32, "nlMatrixTopNReversePktRate")

                self.nlmatrixtopnsourceaddress = YLeaf(YType.str, "nlMatrixTopNSourceAddress")
                self._segment_path = lambda: "nlMatrixTopNEntry" + "[nlMatrixTopNControlIndex='" + self.nlmatrixtopncontrolindex.get() + "']" + "[nlMatrixTopNIndex='" + self.nlmatrixtopnindex.get() + "']"
                self._absolute_path = lambda: "RMON2-MIB:RMON2-MIB/nlMatrixTopNTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(RMON2MIB.Nlmatrixtopntable.Nlmatrixtopnentry, ['nlmatrixtopncontrolindex', 'nlmatrixtopnindex', 'nlmatrixtopndestaddress', 'nlmatrixtopnoctetrate', 'nlmatrixtopnpktrate', 'nlmatrixtopnprotocoldirlocalindex', 'nlmatrixtopnreverseoctetrate', 'nlmatrixtopnreversepktrate', 'nlmatrixtopnsourceaddress'], name, value)


    class Probeconfig(Entity):
        """
        
        
        .. attribute:: netdefaultgateway
        
        	The IP Address of the default gateway.  If this value is undefined or unknown, it shall have the value 0.0.0.0
        	**type**\:  str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        .. attribute:: probecapabilities
        
        	An indication of the RMON MIB groups supported on at least one interface by this probe
        	**type**\:  str
        
        	**length:** 1
        
        .. attribute:: probedatetime
        
        	Probe's current date and time.  field  octets  contents                  range \-\-\-\-\-  \-\-\-\-\-\-  \-\-\-\-\-\-\-\-                  \-\-\-\-\-   1      1\-2   year                      0..65536   2       3    month                     1..12   3       4    day                       1..31   4       5    hour                      0..23   5       6    minutes                   0..59   6       7    seconds                   0..60                 (use 60 for leap\-second)   7       8    deci\-seconds              0..9   8       9    direction from UTC        '+' / '\-'   9      10    hours from UTC            0..11  10      11    minutes from UTC          0..59  For example, Tuesday May 26, 1992 at 1\:30\:15 PM EDT would be displayed as\:              1992\-5\-26,13\:30\:15.0,\-4\:0  Note that if only local time is known, then timezone information (fields 8\-10) is not present, and if no time information is known, the null string is returned
        	**type**\:  str
        
        	**length:** 0 \| 8 \| 11
        
        .. attribute:: probedownloadaction
        
        	When this object is set to downloadToRAM(2) or downloadToPROM(3), the device will discontinue its normal operation and begin download of the image specified by probeDownloadFile from the server specified by probeDownloadTFTPServer using the TFTP protocol.  If downloadToRAM(2) is specified, the new image is copied to RAM only (the old image remains unaltered in the flash EPROM).  If downloadToPROM(3) is specified the new image is written to the flash EPROM memory after its checksum has been verified to be correct. When the download process is completed, the device will      warm boot to restart the newly loaded application. When the device is not downloading, this object will have a value of notDownloading(1)
        	**type**\:   :py:class:`Probedownloadaction <ydk.models.cisco_ios_xe.RMON2_MIB.RMON2MIB.Probeconfig.Probedownloadaction>`
        
        .. attribute:: probedownloadfile
        
        	The file name to be downloaded from the TFTP server when a download is next requested via this MIB.  This value is set to the zero length string when no file name has been specified
        	**type**\:  str
        
        	**length:** 0..127
        
        .. attribute:: probedownloadstatus
        
        	The status of the last download procedure, if any.  This object will have a value of downloadStatusUnknown(2) if no download process has been performed
        	**type**\:   :py:class:`Probedownloadstatus <ydk.models.cisco_ios_xe.RMON2_MIB.RMON2MIB.Probeconfig.Probedownloadstatus>`
        
        .. attribute:: probedownloadtftpserver
        
        	The IP address of the TFTP server that contains the boot image to load when a download is next requested via this MIB. This value is set to `0.0.0.0' when no IP address has been specified
        	**type**\:  str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        .. attribute:: probehardwarerev
        
        	The hardware revision of this device.  This string will have a zero length if the revision is unknown
        	**type**\:  str
        
        	**length:** 0..31
        
        .. attribute:: proberesetcontrol
        
        	Setting this object to warmBoot(2) causes the device to restart the application software with current configuration parameters saved in non\-volatile memory.  Setting this object to coldBoot(3) causes the device to reinitialize configuration parameters in non\-volatile memory to default values and restart the application software.  When the device is running normally, this variable has a value of running(1)
        	**type**\:   :py:class:`Proberesetcontrol <ydk.models.cisco_ios_xe.RMON2_MIB.RMON2MIB.Probeconfig.Proberesetcontrol>`
        
        .. attribute:: probesoftwarerev
        
        	The software revision of this device.  This string will have a zero length if the revision is unknown
        	**type**\:  str
        
        	**length:** 0..31
        
        

        """

        _prefix = 'RMON2-MIB'
        _revision = '1996-05-27'

        def __init__(self):
            super(RMON2MIB.Probeconfig, self).__init__()

            self.yang_name = "probeConfig"
            self.yang_parent_name = "RMON2-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.netdefaultgateway = YLeaf(YType.str, "netDefaultGateway")

            self.probecapabilities = YLeaf(YType.str, "probeCapabilities")

            self.probedatetime = YLeaf(YType.str, "probeDateTime")

            self.probedownloadaction = YLeaf(YType.enumeration, "probeDownloadAction")

            self.probedownloadfile = YLeaf(YType.str, "probeDownloadFile")

            self.probedownloadstatus = YLeaf(YType.enumeration, "probeDownloadStatus")

            self.probedownloadtftpserver = YLeaf(YType.str, "probeDownloadTFTPServer")

            self.probehardwarerev = YLeaf(YType.str, "probeHardwareRev")

            self.proberesetcontrol = YLeaf(YType.enumeration, "probeResetControl")

            self.probesoftwarerev = YLeaf(YType.str, "probeSoftwareRev")
            self._segment_path = lambda: "probeConfig"
            self._absolute_path = lambda: "RMON2-MIB:RMON2-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(RMON2MIB.Probeconfig, ['netdefaultgateway', 'probecapabilities', 'probedatetime', 'probedownloadaction', 'probedownloadfile', 'probedownloadstatus', 'probedownloadtftpserver', 'probehardwarerev', 'proberesetcontrol', 'probesoftwarerev'], name, value)

        class Probedownloadaction(Enum):
            """
            Probedownloadaction

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

            .. data:: notDownloading = 1

            .. data:: downloadToPROM = 2

            .. data:: downloadToRAM = 3

            """

            notDownloading = Enum.YLeaf(1, "notDownloading")

            downloadToPROM = Enum.YLeaf(2, "downloadToPROM")

            downloadToRAM = Enum.YLeaf(3, "downloadToRAM")


        class Probedownloadstatus(Enum):
            """
            Probedownloadstatus

            The status of the last download procedure, if any.  This

            object will have a value of downloadStatusUnknown(2) if no

            download process has been performed.

            .. data:: downloadSuccess = 1

            .. data:: downloadStatusUnknown = 2

            .. data:: downloadGeneralError = 3

            .. data:: downloadNoResponseFromServer = 4

            .. data:: downloadChecksumError = 5

            .. data:: downloadIncompatibleImage = 6

            .. data:: downloadTftpFileNotFound = 7

            .. data:: downloadTftpAccessViolation = 8

            """

            downloadSuccess = Enum.YLeaf(1, "downloadSuccess")

            downloadStatusUnknown = Enum.YLeaf(2, "downloadStatusUnknown")

            downloadGeneralError = Enum.YLeaf(3, "downloadGeneralError")

            downloadNoResponseFromServer = Enum.YLeaf(4, "downloadNoResponseFromServer")

            downloadChecksumError = Enum.YLeaf(5, "downloadChecksumError")

            downloadIncompatibleImage = Enum.YLeaf(6, "downloadIncompatibleImage")

            downloadTftpFileNotFound = Enum.YLeaf(7, "downloadTftpFileNotFound")

            downloadTftpAccessViolation = Enum.YLeaf(8, "downloadTftpAccessViolation")


        class Proberesetcontrol(Enum):
            """
            Proberesetcontrol

            Setting this object to warmBoot(2) causes the device to

            restart the application software with current configuration

            parameters saved in non\-volatile memory.  Setting this

            object to coldBoot(3) causes the device to reinitialize

            configuration parameters in non\-volatile memory to default

            values and restart the application software.  When the device

            is running normally, this variable has a value of

            running(1).

            .. data:: running = 1

            .. data:: warmBoot = 2

            .. data:: coldBoot = 3

            """

            running = Enum.YLeaf(1, "running")

            warmBoot = Enum.YLeaf(2, "warmBoot")

            coldBoot = Enum.YLeaf(3, "coldBoot")



    class Protocoldir(Entity):
        """
        
        
        .. attribute:: protocoldirlastchange
        
        	The value of sysUpTime at the time the protocol directory was last modified, either through insertions or deletions, or through modifications of either the protocolDirAddressMapConfig, protocolDirHostConfig, or protocolDirMatrixConfig
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'RMON2-MIB'
        _revision = '1996-05-27'

        def __init__(self):
            super(RMON2MIB.Protocoldir, self).__init__()

            self.yang_name = "protocolDir"
            self.yang_parent_name = "RMON2-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.protocoldirlastchange = YLeaf(YType.uint32, "protocolDirLastChange")
            self._segment_path = lambda: "protocolDir"
            self._absolute_path = lambda: "RMON2-MIB:RMON2-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(RMON2MIB.Protocoldir, ['protocoldirlastchange'], name, value)


    class Protocoldirtable(Entity):
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
        	**type**\: list of    :py:class:`Protocoldirentry <ydk.models.cisco_ios_xe.RMON2_MIB.RMON2MIB.Protocoldirtable.Protocoldirentry>`
        
        

        """

        _prefix = 'RMON2-MIB'
        _revision = '1996-05-27'

        def __init__(self):
            super(RMON2MIB.Protocoldirtable, self).__init__()

            self.yang_name = "protocolDirTable"
            self.yang_parent_name = "RMON2-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"protocolDirEntry" : ("protocoldirentry", RMON2MIB.Protocoldirtable.Protocoldirentry)}

            self.protocoldirentry = YList(self)
            self._segment_path = lambda: "protocolDirTable"
            self._absolute_path = lambda: "RMON2-MIB:RMON2-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(RMON2MIB.Protocoldirtable, [], name, value)


        class Protocoldirentry(Entity):
            """
            A conceptual row in the protocolDirTable.
            
            An example of the indexing of this entry is
            protocolDirLocalIndex.8.0.0.0.1.0.0.8.0.2.0.0, which is the
            encoding of a length of 8, followed by 8 subids encoding the
            protocolDirID of 1.2048, followed by a length of 2 and the
            2 subids encoding zero\-valued parameters.
            
            .. attribute:: protocoldirid  <key>
            
            	A unique identifier for a particular protocol.  Standard identifiers will be defined in a manner such that they can often be used as specifications for new protocols \- i.e. a tree\-structured assignment mechanism that matches the protocol encapsulation `tree' and which has algorithmic assignment mechanisms for certain subtrees. See RFC XXX for more details.  Despite the algorithmic mechanism, the probe will only place entries in here for those protocols it chooses to collect.  In other words, it need not populate this table with all of the possible ethernet protocol types, nor need it create them on the fly when it sees them.  Whether or not it does these things is a matter of product definition (cost/benefit, usability), and is up to the designer of the product.  If an entry is written to this table with a protocolDirID that the agent doesn't understand, either directly or algorithmically, the SET request will be rejected with an inconsistentName or badValue (for SNMPv1) error
            	**type**\:  str
            
            .. attribute:: protocoldirparameters  <key>
            
            	A set of parameters for the associated protocolDirID. See the associated RMON2 Protocol Identifiers document for a description of the possible parameters. There will be one octet in this string for each sub\-identifier in the protocolDirID, and the parameters will appear here in the same order as the associated sub\-identifiers appear in the protocolDirID.  Every node in the protocolDirID tree has a different, optional set of parameters defined (that is, the definition of parameters for a node is optional).  The proper parameter value for each node is included in this string.  Note that the inclusion of a parameter value in this string for each node is not optional \- what is optional is that a node may have no parameters defined, in which case the parameter field for that node will be zero
            	**type**\:  str
            
            .. attribute:: protocoldiraddressmapconfig
            
            	This object describes and configures the probe's support for address mapping for this protocol.  When the probe creates entries in this table for all protocols that it understands, it will set the entry to notSupported(1) if it doesn't have the capability to perform address mapping for the protocol or if this protocol is not a network\-layer protocol.  When an entry is created in this table by a management operation as part of the limited extensibility feature, the probe must set this value to notSupported(1), because limited extensibility of the protocolDirTable does not extend to interpreting addresses of the extended protocols.  If the value of this object is notSupported(1), the probe will not perform address mapping for this protocol and shall not allow this object to be changed to any other value. If the value of this object is supportedOn(3), the probe supports address mapping for this protocol and is configured to perform address mapping for this protocol for all addressMappingControlEntries and all interfaces. If the value of this object is supportedOff(2), the probe supports address mapping for this protocol but is configured to not perform address mapping for this protocol for any addressMappingControlEntries and all interfaces. Whenever this value changes from supportedOn(3) to supportedOff(2), the probe shall delete all related entries in the addressMappingTable
            	**type**\:   :py:class:`Protocoldiraddressmapconfig <ydk.models.cisco_ios_xe.RMON2_MIB.RMON2MIB.Protocoldirtable.Protocoldirentry.Protocoldiraddressmapconfig>`
            
            .. attribute:: protocoldirdescr
            
            	A textual description of the protocol encapsulation. A probe may choose to describe only a subset of the entire encapsulation (e.g. only the highest layer).  This object is intended for human consumption only.  This object may not be modified if the associated protocolDirStatus object is equal to active(1)
            	**type**\:  str
            
            	**length:** 1..64
            
            .. attribute:: protocoldirhostconfig
            
            	This object describes and configures the probe's support for the network layer and application layer host tables for this protocol.  When the probe creates entries in this table for all protocols that it understands, it will set the entry to notSupported(1) if it doesn't have the capability to track the nlHostTable for this protocol or if the alHostTable is implemented but doesn't have the capability to track this protocol.  Note that if the alHostTable is implemented, the probe may only support a protocol if it is supported in both the nlHostTable and the alHostTable.      If the associated protocolDirType object has the addressRecognitionCapable bit set, then this is a network layer protocol for which the probe recognizes addresses, and thus the probe will populate the nlHostTable and alHostTable with addresses it discovers for this protocol.  If the value of this object is notSupported(1), the probe will not track the nlHostTable or alHostTable for this protocol and shall not allow this object to be changed to any other value. If the value of this object is supportedOn(3), the probe supports tracking of the nlHostTable and alHostTable for this protocol and is configured to track both tables for this protocol for all control entries and all interfaces. If the value of this object is supportedOff(2), the probe supports tracking of the nlHostTable and alHostTable for this protocol but is configured to not track these tables for any control entries or interfaces. Whenever this value changes from supportedOn(3) to supportedOff(2), the probe shall delete all related entries in the nlHostTable and alHostTable.  Note that since each alHostEntry references 2 protocol directory entries, one for the network address and one for the type of the highest protocol recognized, that an entry will only be created in that table if this value is supportedOn(3) for both protocols
            	**type**\:   :py:class:`Protocoldirhostconfig <ydk.models.cisco_ios_xe.RMON2_MIB.RMON2MIB.Protocoldirtable.Protocoldirentry.Protocoldirhostconfig>`
            
            .. attribute:: protocoldirlocalindex
            
            	The locally arbitrary, but unique identifier associated with this protocolDir entry.  The value for each supported protocol must remain constant at least from one re\-initialization of the entity's network management system to the next re\-initialization, except that if a protocol is deleted and re\-created, it must be re\-created with a new value that has not been used since the last re\-initialization.  The specific value is meaningful only within a given SNMP entity. A protocolDirLocalIndex must not be re\-used until the next agent\-restart in the event the protocol directory entry is deleted
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: protocoldirmatrixconfig
            
            	This object describes and configures the probe's support for the network layer and application layer matrix tables for this protocol.  When the probe creates entries in this table for all protocols that it understands, it will set the entry to notSupported(1) if it doesn't have the capability to track the nlMatrixTables for this protocol or if the alMatrixTables are implemented but don't have the capability to track this protocol.  Note that if the alMatrix tables are implemented, the probe may only support a protocol if it is supported in the the both of the nlMatrixTables and both of the alMatrixTables.      If the associated protocolDirType object has the addressRecognitionCapable bit set, then this is a network layer protocol for which the probe recognizes addresses, and thus the probe will populate both of the nlMatrixTables and both of the alMatrixTables with addresses it discovers for this protocol.  If the value of this object is notSupported(1), the probe will not track either of the nlMatrixTables or the alMatrixTables for this protocol and shall not allow this object to be changed to any other value. If the value of this object is supportedOn(3), the probe supports tracking of both of the nlMatrixTables and (if implemented) both of the alMatrixTables for this protocol and is configured to track these tables for this protocol for all control entries and all interfaces. If the value of this object is supportedOff(2), the probe supports tracking of both of the nlMatrixTables and (if implemented) both of the alMatrixTables for this protocol but is configured to not track these tables for this protocol for any control entries or interfaces. Whenever this value changes from supportedOn(3) to supportedOff(2), the probe shall delete all related entries in the nlMatrixTables and the alMatrixTables.  Note that since each alMatrixEntry references 2 protocol directory entries, one for the network address and one for the type of the highest protocol recognized, that an entry will only be created in that table if this value is supportedOn(3) for both protocols
            	**type**\:   :py:class:`Protocoldirmatrixconfig <ydk.models.cisco_ios_xe.RMON2_MIB.RMON2MIB.Protocoldirtable.Protocoldirentry.Protocoldirmatrixconfig>`
            
            .. attribute:: protocoldirowner
            
            	The entity that configured this entry and is therefore using the resources assigned to it
            	**type**\:  str
            
            	**length:** 0..127
            
            .. attribute:: protocoldirstatus
            
            	The status of this protocol directory entry.  An entry may not exist in the active state unless all      objects in the entry have an appropriate value.  If this object is not equal to active(1), all associated entries in the nlHostTable, nlMatrixSDTable, nlMatrixDSTable, alHostTable, alMatrixSDTable, and alMatrixDSTable shall be deleted
            	**type**\:   :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            .. attribute:: protocoldirtype
            
            	This object describes 2 attributes of this protocol directory entry.  The presence or absence of the `extensible' bit describes whether or not this protocol directory entry can be extended      by the user by creating protocol directory entries which are children of this protocol.  An example of an entry that will often allow extensibility is `ip.udp'.  The probe may automatically populate some children of this node such as `ip.udp.snmp' and `ip.udp.dns'. A probe administrator or user may also populate additional children via remote SNMP requests that create entries in this table.  When a child node is added for a protocol for which the probe has no built in support, extending a parent node (for which the probe does have built in support), that child node is not extendible.  This is termed `limited extensibility'.  When a child node is added through this extensibility mechanism, the values of protocolDirLocalIndex and protocolDirType shall be assigned by the agent.  The other objects in the entry will be assigned by the manager who is creating the new entry.  This object also describes whether or not this agent can recognize addresses for this protocol, should it be a network level protocol.  That is, while a probe may be able to recognize packets of a particular network layer protocol and count them, it takes additional logic to be able to recognize the addresses in this protocol and to populate network layer or application layer tables with the addresses in this protocol.  If this bit is set, the agent will recognize network layer addresses for this protoocl and populate the network and application layer host and matrix tables with these protocols.  Note that when an entry is created, the agent will supply values for the bits that match the capabilities of the agent with respect to this protocol.  Note that since row creations usually exercise the limited extensibility feature, these bits will usually be set to zero
            	**type**\:  str
            
            	**length:** 1
            
            

            """

            _prefix = 'RMON2-MIB'
            _revision = '1996-05-27'

            def __init__(self):
                super(RMON2MIB.Protocoldirtable.Protocoldirentry, self).__init__()

                self.yang_name = "protocolDirEntry"
                self.yang_parent_name = "protocolDirTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.protocoldirid = YLeaf(YType.str, "protocolDirID")

                self.protocoldirparameters = YLeaf(YType.str, "protocolDirParameters")

                self.protocoldiraddressmapconfig = YLeaf(YType.enumeration, "protocolDirAddressMapConfig")

                self.protocoldirdescr = YLeaf(YType.str, "protocolDirDescr")

                self.protocoldirhostconfig = YLeaf(YType.enumeration, "protocolDirHostConfig")

                self.protocoldirlocalindex = YLeaf(YType.int32, "protocolDirLocalIndex")

                self.protocoldirmatrixconfig = YLeaf(YType.enumeration, "protocolDirMatrixConfig")

                self.protocoldirowner = YLeaf(YType.str, "protocolDirOwner")

                self.protocoldirstatus = YLeaf(YType.enumeration, "protocolDirStatus")

                self.protocoldirtype = YLeaf(YType.str, "protocolDirType")
                self._segment_path = lambda: "protocolDirEntry" + "[protocolDirID='" + self.protocoldirid.get() + "']" + "[protocolDirParameters='" + self.protocoldirparameters.get() + "']"
                self._absolute_path = lambda: "RMON2-MIB:RMON2-MIB/protocolDirTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(RMON2MIB.Protocoldirtable.Protocoldirentry, ['protocoldirid', 'protocoldirparameters', 'protocoldiraddressmapconfig', 'protocoldirdescr', 'protocoldirhostconfig', 'protocoldirlocalindex', 'protocoldirmatrixconfig', 'protocoldirowner', 'protocoldirstatus', 'protocoldirtype'], name, value)

            class Protocoldiraddressmapconfig(Enum):
                """
                Protocoldiraddressmapconfig

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

                .. data:: notSupported = 1

                .. data:: supportedOff = 2

                .. data:: supportedOn = 3

                """

                notSupported = Enum.YLeaf(1, "notSupported")

                supportedOff = Enum.YLeaf(2, "supportedOff")

                supportedOn = Enum.YLeaf(3, "supportedOn")


            class Protocoldirhostconfig(Enum):
                """
                Protocoldirhostconfig

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

                .. data:: notSupported = 1

                .. data:: supportedOff = 2

                .. data:: supportedOn = 3

                """

                notSupported = Enum.YLeaf(1, "notSupported")

                supportedOff = Enum.YLeaf(2, "supportedOff")

                supportedOn = Enum.YLeaf(3, "supportedOn")


            class Protocoldirmatrixconfig(Enum):
                """
                Protocoldirmatrixconfig

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

                .. data:: notSupported = 1

                .. data:: supportedOff = 2

                .. data:: supportedOn = 3

                """

                notSupported = Enum.YLeaf(1, "notSupported")

                supportedOff = Enum.YLeaf(2, "supportedOff")

                supportedOn = Enum.YLeaf(3, "supportedOn")



    class Protocoldistcontroltable(Entity):
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
        	**type**\: list of    :py:class:`Protocoldistcontrolentry <ydk.models.cisco_ios_xe.RMON2_MIB.RMON2MIB.Protocoldistcontroltable.Protocoldistcontrolentry>`
        
        

        """

        _prefix = 'RMON2-MIB'
        _revision = '1996-05-27'

        def __init__(self):
            super(RMON2MIB.Protocoldistcontroltable, self).__init__()

            self.yang_name = "protocolDistControlTable"
            self.yang_parent_name = "RMON2-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"protocolDistControlEntry" : ("protocoldistcontrolentry", RMON2MIB.Protocoldistcontroltable.Protocoldistcontrolentry)}

            self.protocoldistcontrolentry = YList(self)
            self._segment_path = lambda: "protocolDistControlTable"
            self._absolute_path = lambda: "RMON2-MIB:RMON2-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(RMON2MIB.Protocoldistcontroltable, [], name, value)


        class Protocoldistcontrolentry(Entity):
            """
            A conceptual row in the protocolDistControlTable.
            
            An example of the indexing of this entry is
            
            
            
            
            
            protocolDistControlDroppedFrames.7
            
            .. attribute:: protocoldistcontrolindex  <key>
            
            	A unique index for this protocolDistControlEntry
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: protocoldistcontrolcreatetime
            
            	The value of sysUpTime when this control entry was last activated. This can be used by the management station to ensure that the table has not been deleted and recreated between polls
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: protocoldistcontroldatasource
            
            	The source of data for the this protocol distribution.  The statistics in this group reflect all packets on the local network segment attached to the identified interface.  This object may not be modified if the associated protocolDistControlStatus object is equal to active(1)
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: protocoldistcontroldroppedframes
            
            	The total number of frames which were received by the probe and therefore not accounted for in the \*StatsDropEvents, but for which the probe chose not to count for this entry for whatever reason.  Most often, this event occurs when the probe is out of some resources and decides to shed load from this collection.       This count does not include packets that were not counted because they had MAC\-layer errors.  Note that, unlike the dropEvents counter, this number is the exact number of frames dropped
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: protocoldistcontrolowner
            
            	The entity that configured this entry and is therefore using the resources assigned to it
            	**type**\:  str
            
            	**length:** 0..127
            
            .. attribute:: protocoldistcontrolstatus
            
            	The status of this row.  An entry may not exist in the active state unless all objects in the entry have an appropriate value.  If this object is not equal to active(1), all associated entries in the protocolDistStatsTable shall be deleted
            	**type**\:   :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            

            """

            _prefix = 'RMON2-MIB'
            _revision = '1996-05-27'

            def __init__(self):
                super(RMON2MIB.Protocoldistcontroltable.Protocoldistcontrolentry, self).__init__()

                self.yang_name = "protocolDistControlEntry"
                self.yang_parent_name = "protocolDistControlTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.protocoldistcontrolindex = YLeaf(YType.int32, "protocolDistControlIndex")

                self.protocoldistcontrolcreatetime = YLeaf(YType.uint32, "protocolDistControlCreateTime")

                self.protocoldistcontroldatasource = YLeaf(YType.str, "protocolDistControlDataSource")

                self.protocoldistcontroldroppedframes = YLeaf(YType.uint32, "protocolDistControlDroppedFrames")

                self.protocoldistcontrolowner = YLeaf(YType.str, "protocolDistControlOwner")

                self.protocoldistcontrolstatus = YLeaf(YType.enumeration, "protocolDistControlStatus")
                self._segment_path = lambda: "protocolDistControlEntry" + "[protocolDistControlIndex='" + self.protocoldistcontrolindex.get() + "']"
                self._absolute_path = lambda: "RMON2-MIB:RMON2-MIB/protocolDistControlTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(RMON2MIB.Protocoldistcontroltable.Protocoldistcontrolentry, ['protocoldistcontrolindex', 'protocoldistcontrolcreatetime', 'protocoldistcontroldatasource', 'protocoldistcontroldroppedframes', 'protocoldistcontrolowner', 'protocoldistcontrolstatus'], name, value)


    class Protocoldiststatstable(Entity):
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
        	**type**\: list of    :py:class:`Protocoldiststatsentry <ydk.models.cisco_ios_xe.RMON2_MIB.RMON2MIB.Protocoldiststatstable.Protocoldiststatsentry>`
        
        

        """

        _prefix = 'RMON2-MIB'
        _revision = '1996-05-27'

        def __init__(self):
            super(RMON2MIB.Protocoldiststatstable, self).__init__()

            self.yang_name = "protocolDistStatsTable"
            self.yang_parent_name = "RMON2-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"protocolDistStatsEntry" : ("protocoldiststatsentry", RMON2MIB.Protocoldiststatstable.Protocoldiststatsentry)}

            self.protocoldiststatsentry = YList(self)
            self._segment_path = lambda: "protocolDistStatsTable"
            self._absolute_path = lambda: "RMON2-MIB:RMON2-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(RMON2MIB.Protocoldiststatstable, [], name, value)


        class Protocoldiststatsentry(Entity):
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
            
            .. attribute:: protocoldistcontrolindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..65535
            
            	**refers to**\:  :py:class:`protocoldistcontrolindex <ydk.models.cisco_ios_xe.RMON2_MIB.RMON2MIB.Protocoldistcontroltable.Protocoldistcontrolentry>`
            
            .. attribute:: protocoldirlocalindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`protocoldirlocalindex <ydk.models.cisco_ios_xe.RMON2_MIB.RMON2MIB.Protocoldirtable.Protocoldirentry>`
            
            .. attribute:: protocoldiststatsoctets
            
            	The number of octets in packets received of this protocol type since it was added to the protocolDistStatsTable (excluding framing bits but including FCS octets), except for those octets in packets that contained errors.  Note this doesn't count just those octets in the particular protocol frames, but includes the entire packet that contained the protocol
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: protocoldiststatspkts
            
            	The number of packets without errors received of this protocol type.  Note that this is the number of link\-layer packets, so if a single network\-layer packet is fragmented into several link\-layer frames, this counter is incremented several times
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'RMON2-MIB'
            _revision = '1996-05-27'

            def __init__(self):
                super(RMON2MIB.Protocoldiststatstable.Protocoldiststatsentry, self).__init__()

                self.yang_name = "protocolDistStatsEntry"
                self.yang_parent_name = "protocolDistStatsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.protocoldistcontrolindex = YLeaf(YType.str, "protocolDistControlIndex")

                self.protocoldirlocalindex = YLeaf(YType.str, "protocolDirLocalIndex")

                self.protocoldiststatsoctets = YLeaf(YType.uint32, "protocolDistStatsOctets")

                self.protocoldiststatspkts = YLeaf(YType.uint32, "protocolDistStatsPkts")
                self._segment_path = lambda: "protocolDistStatsEntry" + "[protocolDistControlIndex='" + self.protocoldistcontrolindex.get() + "']" + "[protocolDirLocalIndex='" + self.protocoldirlocalindex.get() + "']"
                self._absolute_path = lambda: "RMON2-MIB:RMON2-MIB/protocolDistStatsTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(RMON2MIB.Protocoldiststatstable.Protocoldiststatsentry, ['protocoldistcontrolindex', 'protocoldirlocalindex', 'protocoldiststatsoctets', 'protocoldiststatspkts'], name, value)


    class Serialconfigtable(Entity):
        """
        A table of serial interface configuration entries.  This data
        will be stored in non\-volatile memory and preserved across
        probe resets or power loss.
        
        .. attribute:: serialconfigentry
        
        	A set of configuration parameters for a particular serial interface on this device. If the device has no serial interfaces, this table is empty.  The index is composed of the ifIndex assigned to this serial line interface
        	**type**\: list of    :py:class:`Serialconfigentry <ydk.models.cisco_ios_xe.RMON2_MIB.RMON2MIB.Serialconfigtable.Serialconfigentry>`
        
        

        """

        _prefix = 'RMON2-MIB'
        _revision = '1996-05-27'

        def __init__(self):
            super(RMON2MIB.Serialconfigtable, self).__init__()

            self.yang_name = "serialConfigTable"
            self.yang_parent_name = "RMON2-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"serialConfigEntry" : ("serialconfigentry", RMON2MIB.Serialconfigtable.Serialconfigentry)}

            self.serialconfigentry = YList(self)
            self._segment_path = lambda: "serialConfigTable"
            self._absolute_path = lambda: "RMON2-MIB:RMON2-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(RMON2MIB.Serialconfigtable, [], name, value)


        class Serialconfigentry(Entity):
            """
            A set of configuration parameters for a particular
            serial interface on this device. If the device has no serial
            interfaces, this table is empty.
            
            The index is composed of the ifIndex assigned to this serial
            line interface.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.RFC1213_MIB.RFC1213MIB.Iftable.Ifentry>`
            
            .. attribute:: serialdialouttimeout
            
            	This timeout value is used when the probe initiates the serial connection with the intention of contacting a management station. This variable represents the number of seconds of inactivity allowed before terminating the connection on this serial interface
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: serialmode
            
            	The type of incoming connection to expect on this serial interface
            	**type**\:   :py:class:`Serialmode <ydk.models.cisco_ios_xe.RMON2_MIB.RMON2MIB.Serialconfigtable.Serialconfigentry.Serialmode>`
            
            .. attribute:: serialmodemconnectresp
            
            	An ASCII string containing substrings that describe the expected modem connection response code and associated bps rate.  The substrings are delimited by the first character in the string, for example\:    /CONNECT/300/CONNECT 1200/1200/CONNECT 2400/2400/    CONNECT 4800/4800/CONNECT 9600/9600 will be interpreted as\:     response code    bps rate     CONNECT            300     CONNECT 1200      1200          CONNECT 2400      2400     CONNECT 4800      4800     CONNECT 9600      9600 The agent will use the information in this string to adjust the bps rate of this serial interface once a modem connection is established.  A value that is appropriate for a wide variety of modems is\: '/CONNECT/300/CONNECT 1200/1200/CONNECT 2400/2400/  CONNECT 4800/4800/CONNECT 9600/9600/CONNECT 14400/14400/ CONNECT 19200/19200/CONNECT 38400/38400/'
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: serialmodemhangupstring
            
            	A control string which specifies how to disconnect a modem connection on this serial interface.  This object is only meaningful if the associated serialMode has the value of modem(2). A control string that is appropriate for a wide variety of modems is\: '^d2^s+++^d2^sATH0^M^d2'
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: serialmodeminitstring
            
            	A control string which controls how a modem attached to this serial interface should be initialized.  The initialization is performed once during startup and again after each connection is terminated if the associated serialMode has the value of modem(2).  A control string that is appropriate for a wide variety of modems is\: '^s^MATE0Q0V1X4 S0=1 S2=43^M'
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: serialmodemnoconnectresp
            
            	An ASCII string containing response codes that may be generated by a modem to report the reason why a connection attempt has failed.  The response codes are delimited by the first character in the string, for example\:    /NO CARRIER/BUSY/NO DIALTONE/NO ANSWER/ERROR/ If one of these response codes is received via this serial interface while attempting to make a modem connection, the agent will issue the hang up command as specified by serialModemHangUpString.  A value that is appropriate for a wide variety of modems is\: '/NO CARRIER/BUSY/NO DIALTONE/NO ANSWER/ERROR/'
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: serialprotocol
            
            	The type of data link encapsulation to be used on this serial interface
            	**type**\:   :py:class:`Serialprotocol <ydk.models.cisco_ios_xe.RMON2_MIB.RMON2MIB.Serialconfigtable.Serialconfigentry.Serialprotocol>`
            
            .. attribute:: serialstatus
            
            	The status of this serialConfigEntry.  An entry may not exist in the active state unless all objects in the entry have an appropriate value
            	**type**\:   :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            .. attribute:: serialtimeout
            
            	This timeout value is used when the Management Station has initiated the conversation over the serial link. This variable represents the number of seconds of inactivity allowed before terminating the connection on this serial interface. Use the      serialDialoutTimeout in the case where the probe has initiated the connection for the purpose of sending a trap
            	**type**\:  int
            
            	**range:** 1..65535
            
            

            """

            _prefix = 'RMON2-MIB'
            _revision = '1996-05-27'

            def __init__(self):
                super(RMON2MIB.Serialconfigtable.Serialconfigentry, self).__init__()

                self.yang_name = "serialConfigEntry"
                self.yang_parent_name = "serialConfigTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.serialdialouttimeout = YLeaf(YType.int32, "serialDialoutTimeout")

                self.serialmode = YLeaf(YType.enumeration, "serialMode")

                self.serialmodemconnectresp = YLeaf(YType.str, "serialModemConnectResp")

                self.serialmodemhangupstring = YLeaf(YType.str, "serialModemHangUpString")

                self.serialmodeminitstring = YLeaf(YType.str, "serialModemInitString")

                self.serialmodemnoconnectresp = YLeaf(YType.str, "serialModemNoConnectResp")

                self.serialprotocol = YLeaf(YType.enumeration, "serialProtocol")

                self.serialstatus = YLeaf(YType.enumeration, "serialStatus")

                self.serialtimeout = YLeaf(YType.int32, "serialTimeout")
                self._segment_path = lambda: "serialConfigEntry" + "[ifIndex='" + self.ifindex.get() + "']"
                self._absolute_path = lambda: "RMON2-MIB:RMON2-MIB/serialConfigTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(RMON2MIB.Serialconfigtable.Serialconfigentry, ['ifindex', 'serialdialouttimeout', 'serialmode', 'serialmodemconnectresp', 'serialmodemhangupstring', 'serialmodeminitstring', 'serialmodemnoconnectresp', 'serialprotocol', 'serialstatus', 'serialtimeout'], name, value)

            class Serialmode(Enum):
                """
                Serialmode

                The type of incoming connection to expect on this serial

                interface.

                .. data:: direct = 1

                .. data:: modem = 2

                """

                direct = Enum.YLeaf(1, "direct")

                modem = Enum.YLeaf(2, "modem")


            class Serialprotocol(Enum):
                """
                Serialprotocol

                The type of data link encapsulation to be used on this

                serial interface.

                .. data:: other = 1

                .. data:: slip = 2

                .. data:: ppp = 3

                """

                other = Enum.YLeaf(1, "other")

                slip = Enum.YLeaf(2, "slip")

                ppp = Enum.YLeaf(3, "ppp")



    class Serialconnectiontable(Entity):
        """
        A list of serialConnectionEntries.
        
        .. attribute:: serialconnectionentry
        
        	Configuration for a SLIP link over a serial line
        	**type**\: list of    :py:class:`Serialconnectionentry <ydk.models.cisco_ios_xe.RMON2_MIB.RMON2MIB.Serialconnectiontable.Serialconnectionentry>`
        
        

        """

        _prefix = 'RMON2-MIB'
        _revision = '1996-05-27'

        def __init__(self):
            super(RMON2MIB.Serialconnectiontable, self).__init__()

            self.yang_name = "serialConnectionTable"
            self.yang_parent_name = "RMON2-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"serialConnectionEntry" : ("serialconnectionentry", RMON2MIB.Serialconnectiontable.Serialconnectionentry)}

            self.serialconnectionentry = YList(self)
            self._segment_path = lambda: "serialConnectionTable"
            self._absolute_path = lambda: "RMON2-MIB:RMON2-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(RMON2MIB.Serialconnectiontable, [], name, value)


        class Serialconnectionentry(Entity):
            """
            Configuration for a SLIP link over a serial line.
            
            .. attribute:: serialconnectindex  <key>
            
            	A value that uniquely identifies this serialConnection entry
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: serialconnectdestipaddress
            
            	The IP Address that can be reached at the other end of this serial connection. This object may not be modified if the associated serialConnectStatus object is equal to active(1)
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: serialconnectdialstring
            
            	A control string which specifies how to dial the phone number in order to establish a modem connection.  The string should include dialing prefix and suffix.  For example\: ``^s^MATD9,888\-1234^M'' will instruct the Probe to send a carriage return followed by the dialing prefix ``ATD'', the phone number ``9,888\-1234'', and a carriage return as the dialing suffix. This object may not be modified if the associated serialConnectStatus object is equal to active(1)
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: serialconnectowner
            
            	The entity that configured this entry and is therefore using the resources assigned to it
            	**type**\:  str
            
            	**length:** 0..127
            
            .. attribute:: serialconnectstatus
            
            	The status of this serialConnectionEntry.  If the manager attempts to set this object to active(1) when the serialConnectType is set to modem(2) or modem\-switch(4) and the serialConnectDialString is a zero\-length string or cannot be correctly parsed as a ConnectString, the set request will be rejected with badValue(3).  If the manager attempts to set this object to active(1) when the serialConnectType is set to switch(3) or modem\-switch(4) and the serialConnectSwitchConnectSeq, the serialConnectSwitchDisconnectSeq, or the serialConnectSwitchResetSeq are zero\-length strings or cannot be correctly parsed as ConnectStrings, the set request will be rejected with badValue(3).  An entry may not exist in the active state unless all objects in the entry have an appropriate value
            	**type**\:   :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            .. attribute:: serialconnectswitchconnectseq
            
            	A control string which specifies how to establish a data switch connection. This object may not be modified if the associated serialConnectStatus object is equal to active(1)
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: serialconnectswitchdisconnectseq
            
            	A control string which specifies how to terminate a data switch connection. This object may not be modified if the associated      serialConnectStatus object is equal to active(1)
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: serialconnectswitchresetseq
            
            	A control string which specifies how to reset a data switch in the event of a timeout. This object may not be modified if the associated serialConnectStatus object is equal to active(1)
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: serialconnecttype
            
            	The type of outgoing connection to make.  If this object has the value direct(1), then a direct serial connection is assumed.  If this object has the value modem(2), then serialConnectDialString will be used to make a modem connection.  If this object has the value switch(3),      then serialConnectSwitchConnectSeq will be used to establish the connection over a serial data switch, and serialConnectSwitchDisconnectSeq will be used to terminate the connection.  If this object has the value modem\-switch(4), then a modem connection will be made first followed by the switch connection.  This object may not be modified if the associated serialConnectStatus object is equal to active(1)
            	**type**\:   :py:class:`Serialconnecttype <ydk.models.cisco_ios_xe.RMON2_MIB.RMON2MIB.Serialconnectiontable.Serialconnectionentry.Serialconnecttype>`
            
            

            """

            _prefix = 'RMON2-MIB'
            _revision = '1996-05-27'

            def __init__(self):
                super(RMON2MIB.Serialconnectiontable.Serialconnectionentry, self).__init__()

                self.yang_name = "serialConnectionEntry"
                self.yang_parent_name = "serialConnectionTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.serialconnectindex = YLeaf(YType.int32, "serialConnectIndex")

                self.serialconnectdestipaddress = YLeaf(YType.str, "serialConnectDestIpAddress")

                self.serialconnectdialstring = YLeaf(YType.str, "serialConnectDialString")

                self.serialconnectowner = YLeaf(YType.str, "serialConnectOwner")

                self.serialconnectstatus = YLeaf(YType.enumeration, "serialConnectStatus")

                self.serialconnectswitchconnectseq = YLeaf(YType.str, "serialConnectSwitchConnectSeq")

                self.serialconnectswitchdisconnectseq = YLeaf(YType.str, "serialConnectSwitchDisconnectSeq")

                self.serialconnectswitchresetseq = YLeaf(YType.str, "serialConnectSwitchResetSeq")

                self.serialconnecttype = YLeaf(YType.enumeration, "serialConnectType")
                self._segment_path = lambda: "serialConnectionEntry" + "[serialConnectIndex='" + self.serialconnectindex.get() + "']"
                self._absolute_path = lambda: "RMON2-MIB:RMON2-MIB/serialConnectionTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(RMON2MIB.Serialconnectiontable.Serialconnectionentry, ['serialconnectindex', 'serialconnectdestipaddress', 'serialconnectdialstring', 'serialconnectowner', 'serialconnectstatus', 'serialconnectswitchconnectseq', 'serialconnectswitchdisconnectseq', 'serialconnectswitchresetseq', 'serialconnecttype'], name, value)

            class Serialconnecttype(Enum):
                """
                Serialconnecttype

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

                .. data:: direct = 1

                .. data:: modem = 2

                .. data:: switch = 3

                .. data:: modemSwitch = 4

                """

                direct = Enum.YLeaf(1, "direct")

                modem = Enum.YLeaf(2, "modem")

                switch = Enum.YLeaf(3, "switch")

                modemSwitch = Enum.YLeaf(4, "modemSwitch")



    class Trapdesttable(Entity):
        """
        A list of trap destination entries.
        
        .. attribute:: trapdestentry
        
        	This entry includes a destination IP address to which to send traps for this community
        	**type**\: list of    :py:class:`Trapdestentry <ydk.models.cisco_ios_xe.RMON2_MIB.RMON2MIB.Trapdesttable.Trapdestentry>`
        
        

        """

        _prefix = 'RMON2-MIB'
        _revision = '1996-05-27'

        def __init__(self):
            super(RMON2MIB.Trapdesttable, self).__init__()

            self.yang_name = "trapDestTable"
            self.yang_parent_name = "RMON2-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"trapDestEntry" : ("trapdestentry", RMON2MIB.Trapdesttable.Trapdestentry)}

            self.trapdestentry = YList(self)
            self._segment_path = lambda: "trapDestTable"
            self._absolute_path = lambda: "RMON2-MIB:RMON2-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(RMON2MIB.Trapdesttable, [], name, value)


        class Trapdestentry(Entity):
            """
            This entry includes a destination IP address to which to send
            traps for this community.
            
            .. attribute:: trapdestindex  <key>
            
            	A value that uniquely identifies this trapDestEntry
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: trapdestaddress
            
            	The address to send traps on behalf of this entry.  If the associated trapDestProtocol object is equal to ip(1), the encoding of this object is the same as the snmpUDPAddress textual convention in [RFC1906]\:   \-\- for a SnmpUDPAddress of length 6\:   \-\-   \-\- octets   contents        encoding   \-\-  1\-4     IP\-address      network\-byte order   \-\-  5\-6     UDP\-port        network\-byte order  If the associated trapDestProtocol object is equal to ipx(2), the encoding of this object is the same as the snmpIPXAddress textual convention in [RFC1906]\:   \-\- for a SnmpIPXAddress of length 12\:   \-\-   \-\- octets   contents            encoding   \-\-  1\-4     network\-number      network\-byte order   \-\-  5\-10    physical\-address    network\-byte order   \-\- 11\-12    socket\-number       network\-byte order  This object may not be modified if the associated      trapDestStatus object is equal to active(1)
            	**type**\:  str
            
            .. attribute:: trapdestcommunity
            
            	A community to which this destination address belongs. This entry is associated with any eventEntries in the RMON      MIB whose value of eventCommunity is equal to the value of this object.  Every time an associated event entry sends a trap due to an event, that trap will be sent to each address in the trapDestTable with a trapDestCommunity equal to eventCommunity.  This object may not be modified if the associated trapDestStatus object is equal to active(1)
            	**type**\:  str
            
            	**length:** 0..127
            
            .. attribute:: trapdestowner
            
            	The entity that configured this entry and is therefore using the resources assigned to it
            	**type**\:  str
            
            	**length:** 0..127
            
            .. attribute:: trapdestprotocol
            
            	The protocol with which to send this trap
            	**type**\:   :py:class:`Trapdestprotocol <ydk.models.cisco_ios_xe.RMON2_MIB.RMON2MIB.Trapdesttable.Trapdestentry.Trapdestprotocol>`
            
            .. attribute:: trapdeststatus
            
            	The status of this trap destination entry.  An entry may not exist in the active state unless all objects in the entry have an appropriate value
            	**type**\:   :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            

            """

            _prefix = 'RMON2-MIB'
            _revision = '1996-05-27'

            def __init__(self):
                super(RMON2MIB.Trapdesttable.Trapdestentry, self).__init__()

                self.yang_name = "trapDestEntry"
                self.yang_parent_name = "trapDestTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.trapdestindex = YLeaf(YType.int32, "trapDestIndex")

                self.trapdestaddress = YLeaf(YType.str, "trapDestAddress")

                self.trapdestcommunity = YLeaf(YType.str, "trapDestCommunity")

                self.trapdestowner = YLeaf(YType.str, "trapDestOwner")

                self.trapdestprotocol = YLeaf(YType.enumeration, "trapDestProtocol")

                self.trapdeststatus = YLeaf(YType.enumeration, "trapDestStatus")
                self._segment_path = lambda: "trapDestEntry" + "[trapDestIndex='" + self.trapdestindex.get() + "']"
                self._absolute_path = lambda: "RMON2-MIB:RMON2-MIB/trapDestTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(RMON2MIB.Trapdesttable.Trapdestentry, ['trapdestindex', 'trapdestaddress', 'trapdestcommunity', 'trapdestowner', 'trapdestprotocol', 'trapdeststatus'], name, value)

            class Trapdestprotocol(Enum):
                """
                Trapdestprotocol

                The protocol with which to send this trap.

                .. data:: ip = 1

                .. data:: ipx = 2

                """

                ip = Enum.YLeaf(1, "ip")

                ipx = Enum.YLeaf(2, "ipx")



    class Usrhistorycontroltable(Entity):
        """
        A list of data\-collection configuration entries.
        
        .. attribute:: usrhistorycontrolentry
        
        	A list of parameters that set up a group of user\-defined MIB objects to be sampled periodically (called a bucket\-group).  For example, an instance of usrHistoryControlInterval might be named usrHistoryControlInterval.1
        	**type**\: list of    :py:class:`Usrhistorycontrolentry <ydk.models.cisco_ios_xe.RMON2_MIB.RMON2MIB.Usrhistorycontroltable.Usrhistorycontrolentry>`
        
        

        """

        _prefix = 'RMON2-MIB'
        _revision = '1996-05-27'

        def __init__(self):
            super(RMON2MIB.Usrhistorycontroltable, self).__init__()

            self.yang_name = "usrHistoryControlTable"
            self.yang_parent_name = "RMON2-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"usrHistoryControlEntry" : ("usrhistorycontrolentry", RMON2MIB.Usrhistorycontroltable.Usrhistorycontrolentry)}

            self.usrhistorycontrolentry = YList(self)
            self._segment_path = lambda: "usrHistoryControlTable"
            self._absolute_path = lambda: "RMON2-MIB:RMON2-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(RMON2MIB.Usrhistorycontroltable, [], name, value)


        class Usrhistorycontrolentry(Entity):
            """
            A list of parameters that set up a group of user\-defined
            MIB objects to be sampled periodically (called a
            bucket\-group).
            
            For example, an instance of usrHistoryControlInterval
            might be named usrHistoryControlInterval.1
            
            .. attribute:: usrhistorycontrolindex  <key>
            
            	An index that uniquely identifies an entry in the usrHistoryControlTable.  Each such entry defines a set of samples at a particular interval for a specified set of MIB instances available from the managed system
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: usrhistorycontrolbucketsgranted
            
            	The number of discrete sampling intervals over which data shall be saved in the part of the usrHistoryTable associated with this usrHistoryControlEntry.  When the associated usrHistoryControlBucketsRequested      object is created or modified, the probe should set this object as closely to the requested value as is possible for the particular  probe implementation and available resources.  The probe must not lower this value except as a result of a modification to the associated usrHistoryControlBucketsRequested object.  The associated usrHistoryControlBucketsRequested object should be set before or at the same time as this object to allow the probe to accurately estimate the resources required for this usrHistoryControlEntry.  There will be times when the actual number of buckets associated with this entry is less than the value of this object.  In this case, at the end of each sampling interval, a new bucket will be added to the usrHistoryTable.  When the number of buckets reaches the value of this object and a new bucket is to be added to the usrHistoryTable, the oldest bucket associated with this usrHistoryControlEntry shall be deleted by the agent so that the new bucket can be added.  When the value of this object changes to a value less than the current value, entries are deleted from the usrHistoryTable associated with this usrHistoryControlEntry. Enough of the oldest of these entries shall be deleted by the agent so that their number remains less than or equal to the new value of this object.  When the value of this object changes to a value greater than the current value, the number of associated usrHistory entries may be allowed to grow
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: usrhistorycontrolbucketsrequested
            
            	The requested number of discrete time intervals over which data is to be saved in the part of the usrHistoryTable associated with this usrHistoryControlEntry.  When this object is created or modified, the probe should set usrHistoryControlBucketsGranted as closely to this object as is possible for the particular probe implementation and available resources
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: usrhistorycontrolinterval
            
            	The interval in seconds over which the data is sampled for each bucket in the part of the usrHistory table associated with this usrHistoryControlEntry.  Because the counters in a bucket may overflow at their maximum value with no indication, a prudent manager will take into account the possibility of overflow in any of      the associated counters. It is important to consider the minimum time in which any counter could overflow on a particular media type and set the usrHistoryControlInterval object to a value less than this interval.  This object may not be modified if the associated usrHistoryControlStatus object is equal to active(1)
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: usrhistorycontrolobjects
            
            	The number of MIB objects to be collected in the portion of usrHistoryTable associated with this usrHistoryControlEntry.  This object may not be modified if the associated instance of usrHistoryControlStatus is equal to active(1)
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: usrhistorycontrolowner
            
            	The entity that configured this entry and is therefore using the resources assigned to it
            	**type**\:  str
            
            	**length:** 0..127
            
            .. attribute:: usrhistorycontrolstatus
            
            	The status of this variable history control entry.  An entry may not exist in the active state unless all objects in the entry have an appropriate value.  If this object is not equal to active(1), all associated entries in the usrHistoryTable shall be deleted
            	**type**\:   :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            

            """

            _prefix = 'RMON2-MIB'
            _revision = '1996-05-27'

            def __init__(self):
                super(RMON2MIB.Usrhistorycontroltable.Usrhistorycontrolentry, self).__init__()

                self.yang_name = "usrHistoryControlEntry"
                self.yang_parent_name = "usrHistoryControlTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.usrhistorycontrolindex = YLeaf(YType.int32, "usrHistoryControlIndex")

                self.usrhistorycontrolbucketsgranted = YLeaf(YType.int32, "usrHistoryControlBucketsGranted")

                self.usrhistorycontrolbucketsrequested = YLeaf(YType.int32, "usrHistoryControlBucketsRequested")

                self.usrhistorycontrolinterval = YLeaf(YType.int32, "usrHistoryControlInterval")

                self.usrhistorycontrolobjects = YLeaf(YType.int32, "usrHistoryControlObjects")

                self.usrhistorycontrolowner = YLeaf(YType.str, "usrHistoryControlOwner")

                self.usrhistorycontrolstatus = YLeaf(YType.enumeration, "usrHistoryControlStatus")
                self._segment_path = lambda: "usrHistoryControlEntry" + "[usrHistoryControlIndex='" + self.usrhistorycontrolindex.get() + "']"
                self._absolute_path = lambda: "RMON2-MIB:RMON2-MIB/usrHistoryControlTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(RMON2MIB.Usrhistorycontroltable.Usrhistorycontrolentry, ['usrhistorycontrolindex', 'usrhistorycontrolbucketsgranted', 'usrhistorycontrolbucketsrequested', 'usrhistorycontrolinterval', 'usrhistorycontrolobjects', 'usrhistorycontrolowner', 'usrhistorycontrolstatus'], name, value)


    class Usrhistoryobjecttable(Entity):
        """
        A list of data\-collection configuration entries.
        
        .. attribute:: usrhistoryobjectentry
        
        	A list of MIB instances to be sampled periodically.  Entries in this table are created when an associated usrHistoryControlObjects object is created.  The usrHistoryControlIndex value in the index is that of the associated usrHistoryControlEntry.  For example, an instance of usrHistoryObjectVariable might be usrHistoryObjectVariable.1.3
        	**type**\: list of    :py:class:`Usrhistoryobjectentry <ydk.models.cisco_ios_xe.RMON2_MIB.RMON2MIB.Usrhistoryobjecttable.Usrhistoryobjectentry>`
        
        

        """

        _prefix = 'RMON2-MIB'
        _revision = '1996-05-27'

        def __init__(self):
            super(RMON2MIB.Usrhistoryobjecttable, self).__init__()

            self.yang_name = "usrHistoryObjectTable"
            self.yang_parent_name = "RMON2-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"usrHistoryObjectEntry" : ("usrhistoryobjectentry", RMON2MIB.Usrhistoryobjecttable.Usrhistoryobjectentry)}

            self.usrhistoryobjectentry = YList(self)
            self._segment_path = lambda: "usrHistoryObjectTable"
            self._absolute_path = lambda: "RMON2-MIB:RMON2-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(RMON2MIB.Usrhistoryobjecttable, [], name, value)


        class Usrhistoryobjectentry(Entity):
            """
            A list of MIB instances to be sampled periodically.
            
            Entries in this table are created when an associated
            usrHistoryControlObjects object is created.
            
            The usrHistoryControlIndex value in the index is
            that of the associated usrHistoryControlEntry.
            
            For example, an instance of usrHistoryObjectVariable might be
            usrHistoryObjectVariable.1.3
            
            .. attribute:: usrhistorycontrolindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..65535
            
            	**refers to**\:  :py:class:`usrhistorycontrolindex <ydk.models.cisco_ios_xe.RMON2_MIB.RMON2MIB.Usrhistorycontroltable.Usrhistorycontrolentry>`
            
            .. attribute:: usrhistoryobjectindex  <key>
            
            	An index used to uniquely identify an entry in the usrHistoryObject table.  Each such entry defines a MIB instance to be collected periodically
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: usrhistoryobjectsampletype
            
            	The method of sampling the selected variable for storage in the usrHistoryTable.  If the value of this object is absoluteValue(1), the value of the selected variable will be copied directly into the history bucket.  If the value of this object is deltaValue(2), the value of the selected variable at the last sample will be subtracted from the current value, and the difference will be stored in the history bucket. If the associated usrHistoryObjectVariable instance could not be obtained at the previous sample interval, then a delta sample is not possible, and the value of the associated usrHistoryValStatus object for this interval will be valueNotAvailable(1).  This object may not be modified if the associated usrHistoryControlStatus object is equal to active(1)
            	**type**\:   :py:class:`Usrhistoryobjectsampletype <ydk.models.cisco_ios_xe.RMON2_MIB.RMON2MIB.Usrhistoryobjecttable.Usrhistoryobjectentry.Usrhistoryobjectsampletype>`
            
            .. attribute:: usrhistoryobjectvariable
            
            	The object identifier of the particular variable to be sampled.  Only variables that resolve to an ASN.1 primitive type of Integer32 (Integer32, Counter, Gauge, or TimeTicks) may be sampled.  Because SNMP access control is articulated entirely in terms of the contents of MIB views, no access control mechanism exists that can restrict the value of this object to identify only those objects that exist in a particular MIB view. Because there is thus no acceptable means of restricting the read access that could be obtained through the user history      mechanism, the probe must only grant write access to this object in those views that have read access to all objects on the probe.  During a set operation, if the supplied variable name is not available in the selected MIB view, a badValue error must be returned.  This object may not be modified if the associated usrHistoryControlStatus object is equal to active(1)
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            

            """

            _prefix = 'RMON2-MIB'
            _revision = '1996-05-27'

            def __init__(self):
                super(RMON2MIB.Usrhistoryobjecttable.Usrhistoryobjectentry, self).__init__()

                self.yang_name = "usrHistoryObjectEntry"
                self.yang_parent_name = "usrHistoryObjectTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.usrhistorycontrolindex = YLeaf(YType.str, "usrHistoryControlIndex")

                self.usrhistoryobjectindex = YLeaf(YType.int32, "usrHistoryObjectIndex")

                self.usrhistoryobjectsampletype = YLeaf(YType.enumeration, "usrHistoryObjectSampleType")

                self.usrhistoryobjectvariable = YLeaf(YType.str, "usrHistoryObjectVariable")
                self._segment_path = lambda: "usrHistoryObjectEntry" + "[usrHistoryControlIndex='" + self.usrhistorycontrolindex.get() + "']" + "[usrHistoryObjectIndex='" + self.usrhistoryobjectindex.get() + "']"
                self._absolute_path = lambda: "RMON2-MIB:RMON2-MIB/usrHistoryObjectTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(RMON2MIB.Usrhistoryobjecttable.Usrhistoryobjectentry, ['usrhistorycontrolindex', 'usrhistoryobjectindex', 'usrhistoryobjectsampletype', 'usrhistoryobjectvariable'], name, value)

            class Usrhistoryobjectsampletype(Enum):
                """
                Usrhistoryobjectsampletype

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

                .. data:: absoluteValue = 1

                .. data:: deltaValue = 2

                """

                absoluteValue = Enum.YLeaf(1, "absoluteValue")

                deltaValue = Enum.YLeaf(2, "deltaValue")



    class Usrhistorytable(Entity):
        """
        A list of user defined history entries.
        
        .. attribute:: usrhistoryentry
        
        	A historical sample of user\-defined variables.  This sample is associated with the usrHistoryControlEntry which set up the parameters for a regular collection of these samples.  The usrHistoryControlIndex value in the index identifies the usrHistoryControlEntry on whose behalf this entry was created.  The usrHistoryObjectIndex value in the index identifies the usrHistoryObjectEntry on whose behalf this entry was created.  For example, an instance of usrHistoryAbsValue, which represents the 14th sample of a variable collected as specified by usrHistoryControlEntry.1 and usrHistoryObjectEntry.1.5, would be named usrHistoryAbsValue.1.14.5
        	**type**\: list of    :py:class:`Usrhistoryentry <ydk.models.cisco_ios_xe.RMON2_MIB.RMON2MIB.Usrhistorytable.Usrhistoryentry>`
        
        

        """

        _prefix = 'RMON2-MIB'
        _revision = '1996-05-27'

        def __init__(self):
            super(RMON2MIB.Usrhistorytable, self).__init__()

            self.yang_name = "usrHistoryTable"
            self.yang_parent_name = "RMON2-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"usrHistoryEntry" : ("usrhistoryentry", RMON2MIB.Usrhistorytable.Usrhistoryentry)}

            self.usrhistoryentry = YList(self)
            self._segment_path = lambda: "usrHistoryTable"
            self._absolute_path = lambda: "RMON2-MIB:RMON2-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(RMON2MIB.Usrhistorytable, [], name, value)


        class Usrhistoryentry(Entity):
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
            
            .. attribute:: usrhistorycontrolindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..65535
            
            	**refers to**\:  :py:class:`usrhistorycontrolindex <ydk.models.cisco_ios_xe.RMON2_MIB.RMON2MIB.Usrhistorycontroltable.Usrhistorycontrolentry>`
            
            .. attribute:: usrhistorysampleindex  <key>
            
            	An index that uniquely identifies the particular sample this entry represents among all samples associated with the same usrHistoryControlEntry. This index starts at 1 and increases by one as each new sample is taken
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: usrhistoryobjectindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..65535
            
            	**refers to**\:  :py:class:`usrhistoryobjectindex <ydk.models.cisco_ios_xe.RMON2_MIB.RMON2MIB.Usrhistoryobjecttable.Usrhistoryobjectentry>`
            
            .. attribute:: usrhistoryabsvalue
            
            	The absolute value (i.e. unsigned value) of the user\-specified statistic during the last sampling period. The value during the current sampling period is not made available until the period is completed.  To obtain the true value for this sampling interval, the associated instance of usrHistoryValStatus must be checked, and usrHistoryAbsValue adjusted as necessary.  If the MIB instance could not be accessed during the sampling interval, then this object will have a value of zero and the associated instance of usrHistoryValStatus will be set to 'valueNotAvailable(1)'
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: usrhistoryintervalend
            
            	The value of sysUpTime at the end of the interval over which this sample was measured
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: usrhistoryintervalstart
            
            	The value of sysUpTime at the start of the interval over which this sample was measured.  If the probe keeps track of the time of day, it should start the first sample of the history at a time such that when the next hour of the day begins, a sample is started at that instant.  Note that following this rule may require the probe to delay collecting the first sample of the history, as each sample must be of the same interval. Also note that the sample which is currently being collected is not accessible in this table until the end of its interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: usrhistoryvalstatus
            
            	This object indicates the validity and sign of the data in the associated instance of usrHistoryAbsValue.  If the MIB instance could not be accessed during the sampling interval, then 'valueNotAvailable(1)' will be returned.  If the sample is valid and actual value of the sample is greater than or equal to zero then 'valuePositive(2)' is returned.  If the sample is valid and the actual value of the sample is less than zero, 'valueNegative(3)' will be returned. The associated instance of usrHistoryAbsValue should be multiplied by \-1 to obtain the true sample value
            	**type**\:   :py:class:`Usrhistoryvalstatus <ydk.models.cisco_ios_xe.RMON2_MIB.RMON2MIB.Usrhistorytable.Usrhistoryentry.Usrhistoryvalstatus>`
            
            

            """

            _prefix = 'RMON2-MIB'
            _revision = '1996-05-27'

            def __init__(self):
                super(RMON2MIB.Usrhistorytable.Usrhistoryentry, self).__init__()

                self.yang_name = "usrHistoryEntry"
                self.yang_parent_name = "usrHistoryTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.usrhistorycontrolindex = YLeaf(YType.str, "usrHistoryControlIndex")

                self.usrhistorysampleindex = YLeaf(YType.int32, "usrHistorySampleIndex")

                self.usrhistoryobjectindex = YLeaf(YType.str, "usrHistoryObjectIndex")

                self.usrhistoryabsvalue = YLeaf(YType.uint32, "usrHistoryAbsValue")

                self.usrhistoryintervalend = YLeaf(YType.uint32, "usrHistoryIntervalEnd")

                self.usrhistoryintervalstart = YLeaf(YType.uint32, "usrHistoryIntervalStart")

                self.usrhistoryvalstatus = YLeaf(YType.enumeration, "usrHistoryValStatus")
                self._segment_path = lambda: "usrHistoryEntry" + "[usrHistoryControlIndex='" + self.usrhistorycontrolindex.get() + "']" + "[usrHistorySampleIndex='" + self.usrhistorysampleindex.get() + "']" + "[usrHistoryObjectIndex='" + self.usrhistoryobjectindex.get() + "']"
                self._absolute_path = lambda: "RMON2-MIB:RMON2-MIB/usrHistoryTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(RMON2MIB.Usrhistorytable.Usrhistoryentry, ['usrhistorycontrolindex', 'usrhistorysampleindex', 'usrhistoryobjectindex', 'usrhistoryabsvalue', 'usrhistoryintervalend', 'usrhistoryintervalstart', 'usrhistoryvalstatus'], name, value)

            class Usrhistoryvalstatus(Enum):
                """
                Usrhistoryvalstatus

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

                .. data:: valueNotAvailable = 1

                .. data:: valuePositive = 2

                .. data:: valueNegative = 3

                """

                valueNotAvailable = Enum.YLeaf(1, "valueNotAvailable")

                valuePositive = Enum.YLeaf(2, "valuePositive")

                valueNegative = Enum.YLeaf(3, "valueNegative")


    def clone_ptr(self):
        self._top_entity = RMON2MIB()
        return self._top_entity

