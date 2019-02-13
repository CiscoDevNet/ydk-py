""" CISCO_NBAR_PROTOCOL_DISCOVERY_MIB 

Cisco NBAR Protocol Discovery MIB 

NBAR \- Network Based Application Recognition is
an intelligent classification engine that recognizes 
applications that are static (which use fixed TCP or
UDP port numbers), and stateful (which dynamically 
assign TCP or UDP port numbers). 

Protocol Discovery \- uses NBAR to show you the mix 
of applications currently running on the network. 
Key statistics are associated with each protocol. 
These statistics can be used to define traffic 
classes and QoS policies.

Functionality\:
1. To enable/disable Protocol Discovery per interface.
2. Display the protocols/applications which NBAR
   currently recognizes.
3. To display various Protocol Discovery statistics.
4. A configurable top N table which lists
   protocols using user defined criteria.
5. To configure notifications (traps) based 
   on configurable statistic thresholds.
6. To maintain a history table of all notification 
   events.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CiscoPdDataType(Enum):
    """
    CiscoPdDataType (Enum Class)

    These are the data types which NBAR

    can measure a particular protocol by.

    bitRateIn(1)      \- incoming bitrate.

    bitRateOut(2)     \- outgoing bitrate.

    bitRateSum(3)     \- sum of incoming and 

                        outgoing bitrate.

    byteCountIn(4)    \- incoming bytecount.

    byteCountOut(5)   \- outgoing bytecount.

    byteCountSum(6)   \- sum of incoming and 

                        outgoing bytecount.

    packetCountIn(7)  \- incoming packetcount.

    packetCountOut(8) \- outgoing packetcount.

    packetCountSum(9) \- sum of incoming and 

                        outgoing packetcount.

    UNITS\:

    bitrate     \- unit is kilo bits per second

    bytecount   \- unit is bytes

    packetcount \- unit is packets

    .. data:: bitRateIn = 1

    .. data:: bitRateOut = 2

    .. data:: bitRateSum = 3

    .. data:: byteCountIn = 4

    .. data:: byteCountOut = 5

    .. data:: byteCountSum = 6

    .. data:: packetCountIn = 7

    .. data:: packetCountOut = 8

    .. data:: packetCountSum = 9

    """

    bitRateIn = Enum.YLeaf(1, "bitRateIn")

    bitRateOut = Enum.YLeaf(2, "bitRateOut")

    bitRateSum = Enum.YLeaf(3, "bitRateSum")

    byteCountIn = Enum.YLeaf(4, "byteCountIn")

    byteCountOut = Enum.YLeaf(5, "byteCountOut")

    byteCountSum = Enum.YLeaf(6, "byteCountSum")

    packetCountIn = Enum.YLeaf(7, "packetCountIn")

    packetCountOut = Enum.YLeaf(8, "packetCountOut")

    packetCountSum = Enum.YLeaf(9, "packetCountSum")



class CISCONBARPROTOCOLDISCOVERYMIB(Entity):
    """
    
    
    .. attribute:: cnpdnotificationsconfig
    
    	
    	**type**\:  :py:class:`CnpdNotificationsConfig <ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB.CISCONBARPROTOCOLDISCOVERYMIB.CnpdNotificationsConfig>`
    
    	**config**\: False
    
    .. attribute:: cnpdstatustable
    
    	The cnpdStatusTable is used to enable and disable Protocol Discovery on an interface
    	**type**\:  :py:class:`CnpdStatusTable <ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB.CISCONBARPROTOCOLDISCOVERYMIB.CnpdStatusTable>`
    
    	**config**\: False
    
    .. attribute:: cnpdallstatstable
    
    	The cnpdAllStatsTable contains all the statistics available for all the protocols/applications currently recognized by NBAR Protocol Discovery for a particular  interface.  In the event of an overflow, the 32 bit counters are not  valid. There is no overflow support
    	**type**\:  :py:class:`CnpdAllStatsTable <ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB.CISCONBARPROTOCOLDISCOVERYMIB.CnpdAllStatsTable>`
    
    	**config**\: False
    
    .. attribute:: cnpdtopnconfigtable
    
    	The cnpdTopNConfigTable is used to configure cnpdTopNStatsTable's
    	**type**\:  :py:class:`CnpdTopNConfigTable <ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB.CISCONBARPROTOCOLDISCOVERYMIB.CnpdTopNConfigTable>`
    
    	**config**\: False
    
    .. attribute:: cnpdtopnstatstable
    
    	A cnpdTopNStatsTable describes an ordered list of protocols
    	**type**\:  :py:class:`CnpdTopNStatsTable <ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB.CISCONBARPROTOCOLDISCOVERYMIB.CnpdTopNStatsTable>`
    
    	**config**\: False
    
    .. attribute:: cnpdthresholdconfigtable
    
    	The cnpdThresholdConfigTable allows the management station to create thresholds for the purpose of sending notifications if breached, and creating a history of breached thresholds
    	**type**\:  :py:class:`CnpdThresholdConfigTable <ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB.CISCONBARPROTOCOLDISCOVERYMIB.CnpdThresholdConfigTable>`
    
    	**config**\: False
    
    .. attribute:: cnpdthresholdhistorytable
    
    	The Threshold History table. Notifications are unreliable so this table provides a history of the last 5000 threshold breached events. A notification can be traced back to its cnpdThresholdHistoryEntry
    	**type**\:  :py:class:`CnpdThresholdHistoryTable <ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB.CISCONBARPROTOCOLDISCOVERYMIB.CnpdThresholdHistoryTable>`
    
    	**config**\: False
    
    .. attribute:: cnpdsupportedprotocolstable
    
    	The Supported Protocols table lists all the  protocols and applications which NBAR is currently capable of recognizing
    	**type**\:  :py:class:`CnpdSupportedProtocolsTable <ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB.CISCONBARPROTOCOLDISCOVERYMIB.CnpdSupportedProtocolsTable>`
    
    	**config**\: False
    
    

    """

    _prefix = 'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB'
    _revision = '2002-08-16'

    def __init__(self):
        super(CISCONBARPROTOCOLDISCOVERYMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-NBAR-PROTOCOL-DISCOVERY-MIB"
        self.yang_parent_name = "CISCO-NBAR-PROTOCOL-DISCOVERY-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("cnpdNotificationsConfig", ("cnpdnotificationsconfig", CISCONBARPROTOCOLDISCOVERYMIB.CnpdNotificationsConfig)), ("cnpdStatusTable", ("cnpdstatustable", CISCONBARPROTOCOLDISCOVERYMIB.CnpdStatusTable)), ("cnpdAllStatsTable", ("cnpdallstatstable", CISCONBARPROTOCOLDISCOVERYMIB.CnpdAllStatsTable)), ("cnpdTopNConfigTable", ("cnpdtopnconfigtable", CISCONBARPROTOCOLDISCOVERYMIB.CnpdTopNConfigTable)), ("cnpdTopNStatsTable", ("cnpdtopnstatstable", CISCONBARPROTOCOLDISCOVERYMIB.CnpdTopNStatsTable)), ("cnpdThresholdConfigTable", ("cnpdthresholdconfigtable", CISCONBARPROTOCOLDISCOVERYMIB.CnpdThresholdConfigTable)), ("cnpdThresholdHistoryTable", ("cnpdthresholdhistorytable", CISCONBARPROTOCOLDISCOVERYMIB.CnpdThresholdHistoryTable)), ("cnpdSupportedProtocolsTable", ("cnpdsupportedprotocolstable", CISCONBARPROTOCOLDISCOVERYMIB.CnpdSupportedProtocolsTable))])
        self._leafs = OrderedDict()

        self.cnpdnotificationsconfig = CISCONBARPROTOCOLDISCOVERYMIB.CnpdNotificationsConfig()
        self.cnpdnotificationsconfig.parent = self
        self._children_name_map["cnpdnotificationsconfig"] = "cnpdNotificationsConfig"

        self.cnpdstatustable = CISCONBARPROTOCOLDISCOVERYMIB.CnpdStatusTable()
        self.cnpdstatustable.parent = self
        self._children_name_map["cnpdstatustable"] = "cnpdStatusTable"

        self.cnpdallstatstable = CISCONBARPROTOCOLDISCOVERYMIB.CnpdAllStatsTable()
        self.cnpdallstatstable.parent = self
        self._children_name_map["cnpdallstatstable"] = "cnpdAllStatsTable"

        self.cnpdtopnconfigtable = CISCONBARPROTOCOLDISCOVERYMIB.CnpdTopNConfigTable()
        self.cnpdtopnconfigtable.parent = self
        self._children_name_map["cnpdtopnconfigtable"] = "cnpdTopNConfigTable"

        self.cnpdtopnstatstable = CISCONBARPROTOCOLDISCOVERYMIB.CnpdTopNStatsTable()
        self.cnpdtopnstatstable.parent = self
        self._children_name_map["cnpdtopnstatstable"] = "cnpdTopNStatsTable"

        self.cnpdthresholdconfigtable = CISCONBARPROTOCOLDISCOVERYMIB.CnpdThresholdConfigTable()
        self.cnpdthresholdconfigtable.parent = self
        self._children_name_map["cnpdthresholdconfigtable"] = "cnpdThresholdConfigTable"

        self.cnpdthresholdhistorytable = CISCONBARPROTOCOLDISCOVERYMIB.CnpdThresholdHistoryTable()
        self.cnpdthresholdhistorytable.parent = self
        self._children_name_map["cnpdthresholdhistorytable"] = "cnpdThresholdHistoryTable"

        self.cnpdsupportedprotocolstable = CISCONBARPROTOCOLDISCOVERYMIB.CnpdSupportedProtocolsTable()
        self.cnpdsupportedprotocolstable.parent = self
        self._children_name_map["cnpdsupportedprotocolstable"] = "cnpdSupportedProtocolsTable"
        self._segment_path = lambda: "CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:CISCO-NBAR-PROTOCOL-DISCOVERY-MIB"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(CISCONBARPROTOCOLDISCOVERYMIB, [], name, value)


    class CnpdNotificationsConfig(Entity):
        """
        
        
        .. attribute:: cnpdnotificationsenable
        
        	This object is used to enable or disable  Notifications on a global basis.   If set to 'true' \- Notifications are enabled. If set to 'false' \- Notifications are disabled
        	**type**\: bool
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB'
        _revision = '2002-08-16'

        def __init__(self):
            super(CISCONBARPROTOCOLDISCOVERYMIB.CnpdNotificationsConfig, self).__init__()

            self.yang_name = "cnpdNotificationsConfig"
            self.yang_parent_name = "CISCO-NBAR-PROTOCOL-DISCOVERY-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('cnpdnotificationsenable', (YLeaf(YType.boolean, 'cnpdNotificationsEnable'), ['bool'])),
            ])
            self.cnpdnotificationsenable = None
            self._segment_path = lambda: "cnpdNotificationsConfig"
            self._absolute_path = lambda: "CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:CISCO-NBAR-PROTOCOL-DISCOVERY-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCONBARPROTOCOLDISCOVERYMIB.CnpdNotificationsConfig, ['cnpdnotificationsenable'], name, value)



    class CnpdStatusTable(Entity):
        """
        The cnpdStatusTable is used to enable and
        disable Protocol Discovery on an interface.
        
        .. attribute:: cnpdstatusentry
        
        	An entry in the cnpdStatusTable contains objects for enabling or disabling Protocol Discovery on a per interface basis
        	**type**\: list of  		 :py:class:`CnpdStatusEntry <ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB.CISCONBARPROTOCOLDISCOVERYMIB.CnpdStatusTable.CnpdStatusEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB'
        _revision = '2002-08-16'

        def __init__(self):
            super(CISCONBARPROTOCOLDISCOVERYMIB.CnpdStatusTable, self).__init__()

            self.yang_name = "cnpdStatusTable"
            self.yang_parent_name = "CISCO-NBAR-PROTOCOL-DISCOVERY-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cnpdStatusEntry", ("cnpdstatusentry", CISCONBARPROTOCOLDISCOVERYMIB.CnpdStatusTable.CnpdStatusEntry))])
            self._leafs = OrderedDict()

            self.cnpdstatusentry = YList(self)
            self._segment_path = lambda: "cnpdStatusTable"
            self._absolute_path = lambda: "CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:CISCO-NBAR-PROTOCOL-DISCOVERY-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCONBARPROTOCOLDISCOVERYMIB.CnpdStatusTable, [], name, value)


        class CnpdStatusEntry(Entity):
            """
            An entry in the cnpdStatusTable contains objects
            for enabling or disabling Protocol Discovery on a
            per interface basis.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            	**config**\: False
            
            .. attribute:: cnpdstatuspdenable
            
            	This object is used to enable or disable  Protocol Discovery on an interface.   If set to 'true' \- Protocol Discovery is  enabled on this Interface.  If set to 'false' \- Protocol Discovery is  disabled on this Interface
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: cnpdstatuslastupdatetime
            
            	The value of sysUpTime at the time Protocol  Discovery was last enabled  on an interface. If the interface does not have Protocol Discovery enabled this value is zero
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB'
            _revision = '2002-08-16'

            def __init__(self):
                super(CISCONBARPROTOCOLDISCOVERYMIB.CnpdStatusTable.CnpdStatusEntry, self).__init__()

                self.yang_name = "cnpdStatusEntry"
                self.yang_parent_name = "cnpdStatusTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('cnpdstatuspdenable', (YLeaf(YType.boolean, 'cnpdStatusPdEnable'), ['bool'])),
                    ('cnpdstatuslastupdatetime', (YLeaf(YType.uint32, 'cnpdStatusLastUpdateTime'), ['int'])),
                ])
                self.ifindex = None
                self.cnpdstatuspdenable = None
                self.cnpdstatuslastupdatetime = None
                self._segment_path = lambda: "cnpdStatusEntry" + "[ifIndex='" + str(self.ifindex) + "']"
                self._absolute_path = lambda: "CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:CISCO-NBAR-PROTOCOL-DISCOVERY-MIB/cnpdStatusTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCONBARPROTOCOLDISCOVERYMIB.CnpdStatusTable.CnpdStatusEntry, ['ifindex', 'cnpdstatuspdenable', 'cnpdstatuslastupdatetime'], name, value)




    class CnpdAllStatsTable(Entity):
        """
        The cnpdAllStatsTable contains all the statistics
        available for all the protocols/applications currently
        recognized by NBAR Protocol Discovery for a particular 
        interface.
        
        In the event of an overflow, the 32 bit counters are not 
        valid. There is no overflow support.
        
        .. attribute:: cnpdallstatsentry
        
        	An entry in the cnpdAllStatsTable table. This entry  contains the statistics collected on all the protocols  which NBAR classifies for a particular interface
        	**type**\: list of  		 :py:class:`CnpdAllStatsEntry <ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB.CISCONBARPROTOCOLDISCOVERYMIB.CnpdAllStatsTable.CnpdAllStatsEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB'
        _revision = '2002-08-16'

        def __init__(self):
            super(CISCONBARPROTOCOLDISCOVERYMIB.CnpdAllStatsTable, self).__init__()

            self.yang_name = "cnpdAllStatsTable"
            self.yang_parent_name = "CISCO-NBAR-PROTOCOL-DISCOVERY-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cnpdAllStatsEntry", ("cnpdallstatsentry", CISCONBARPROTOCOLDISCOVERYMIB.CnpdAllStatsTable.CnpdAllStatsEntry))])
            self._leafs = OrderedDict()

            self.cnpdallstatsentry = YList(self)
            self._segment_path = lambda: "cnpdAllStatsTable"
            self._absolute_path = lambda: "CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:CISCO-NBAR-PROTOCOL-DISCOVERY-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCONBARPROTOCOLDISCOVERYMIB.CnpdAllStatsTable, [], name, value)


        class CnpdAllStatsEntry(Entity):
            """
            An entry in the cnpdAllStatsTable table. This entry 
            contains the statistics collected on all the protocols 
            which NBAR classifies for a particular interface.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            	**config**\: False
            
            .. attribute:: cnpdallstatsprotocolsindex  (key)
            
            	An object which represents a unique  identifier for a protocol or application  which NBAR currently recognizes.  This object is an index into the  SupportedProtocolsTable where details of the protocol can be found
            	**type**\: int
            
            	**range:** 1..1024
            
            	**config**\: False
            
            .. attribute:: cnpdallstatsprotocolname
            
            	Name of the application or protocol, a  unique textual string, assigned in the cnpdSupportedProtocolsTable
            	**type**\: str
            
            	**length:** 1..255
            
            	**config**\: False
            
            .. attribute:: cnpdallstatsinpkts
            
            	The packet count of inbound packets as  determined by Protocol Discovery
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: packets
            
            .. attribute:: cnpdallstatsoutpkts
            
            	The packet count of outbound packets as  determined by Protocol Discovery
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: packets
            
            .. attribute:: cnpdallstatsinbytes
            
            	The byte count of inbound octets as  determined by Protocol Discovery
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: bytes
            
            .. attribute:: cnpdallstatsoutbytes
            
            	The byte count of outbound octets as determined by Protocol Discovery
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: bytes
            
            .. attribute:: cnpdallstatshcinpkts
            
            	The packet count of inbound packets as  determined by Protocol Discovery. This is the 64\-bit (High Capacity) version of cnpdAllStatsInPkts
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            	**units**\: packets
            
            .. attribute:: cnpdallstatshcoutpkts
            
            	The packet count of outbound packets as  determined by Protocol Discovery. This is the 64\-bit (High Capacity) version of cnpdAllStatsOutPkts
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            	**units**\: packets
            
            .. attribute:: cnpdallstatshcinbytes
            
            	The byte count of inbound octets as  determined by Protocol Discovery. This is the 64\-bit (High Capacity) version of cnpdAllStatsInBytes
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            	**units**\: bytes
            
            .. attribute:: cnpdallstatshcoutbytes
            
            	The byte count of outbound octets as  determined by Protocol Discovery. This is the 64\-bit (High Capacity) version of cnpdAllStatsOutBytes
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            	**units**\: bytes
            
            .. attribute:: cnpdallstatsinbitrate
            
            	The inbound bit rate as determined  by Protocol Discovery
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**config**\: False
            
            	**units**\: kilo bits per second
            
            .. attribute:: cnpdallstatsoutbitrate
            
            	The outbound bit rate as determined  by Protocol Discovery
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**config**\: False
            
            	**units**\: kilo bits per second
            
            

            """

            _prefix = 'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB'
            _revision = '2002-08-16'

            def __init__(self):
                super(CISCONBARPROTOCOLDISCOVERYMIB.CnpdAllStatsTable.CnpdAllStatsEntry, self).__init__()

                self.yang_name = "cnpdAllStatsEntry"
                self.yang_parent_name = "cnpdAllStatsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex','cnpdallstatsprotocolsindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('cnpdallstatsprotocolsindex', (YLeaf(YType.uint32, 'cnpdAllStatsProtocolsIndex'), ['int'])),
                    ('cnpdallstatsprotocolname', (YLeaf(YType.str, 'cnpdAllStatsProtocolName'), ['str'])),
                    ('cnpdallstatsinpkts', (YLeaf(YType.uint32, 'cnpdAllStatsInPkts'), ['int'])),
                    ('cnpdallstatsoutpkts', (YLeaf(YType.uint32, 'cnpdAllStatsOutPkts'), ['int'])),
                    ('cnpdallstatsinbytes', (YLeaf(YType.uint32, 'cnpdAllStatsInBytes'), ['int'])),
                    ('cnpdallstatsoutbytes', (YLeaf(YType.uint32, 'cnpdAllStatsOutBytes'), ['int'])),
                    ('cnpdallstatshcinpkts', (YLeaf(YType.uint64, 'cnpdAllStatsHCInPkts'), ['int'])),
                    ('cnpdallstatshcoutpkts', (YLeaf(YType.uint64, 'cnpdAllStatsHCOutPkts'), ['int'])),
                    ('cnpdallstatshcinbytes', (YLeaf(YType.uint64, 'cnpdAllStatsHCInBytes'), ['int'])),
                    ('cnpdallstatshcoutbytes', (YLeaf(YType.uint64, 'cnpdAllStatsHCOutBytes'), ['int'])),
                    ('cnpdallstatsinbitrate', (YLeaf(YType.uint32, 'cnpdAllStatsInBitRate'), ['int'])),
                    ('cnpdallstatsoutbitrate', (YLeaf(YType.uint32, 'cnpdAllStatsOutBitRate'), ['int'])),
                ])
                self.ifindex = None
                self.cnpdallstatsprotocolsindex = None
                self.cnpdallstatsprotocolname = None
                self.cnpdallstatsinpkts = None
                self.cnpdallstatsoutpkts = None
                self.cnpdallstatsinbytes = None
                self.cnpdallstatsoutbytes = None
                self.cnpdallstatshcinpkts = None
                self.cnpdallstatshcoutpkts = None
                self.cnpdallstatshcinbytes = None
                self.cnpdallstatshcoutbytes = None
                self.cnpdallstatsinbitrate = None
                self.cnpdallstatsoutbitrate = None
                self._segment_path = lambda: "cnpdAllStatsEntry" + "[ifIndex='" + str(self.ifindex) + "']" + "[cnpdAllStatsProtocolsIndex='" + str(self.cnpdallstatsprotocolsindex) + "']"
                self._absolute_path = lambda: "CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:CISCO-NBAR-PROTOCOL-DISCOVERY-MIB/cnpdAllStatsTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCONBARPROTOCOLDISCOVERYMIB.CnpdAllStatsTable.CnpdAllStatsEntry, ['ifindex', 'cnpdallstatsprotocolsindex', 'cnpdallstatsprotocolname', 'cnpdallstatsinpkts', 'cnpdallstatsoutpkts', 'cnpdallstatsinbytes', 'cnpdallstatsoutbytes', 'cnpdallstatshcinpkts', 'cnpdallstatshcoutpkts', 'cnpdallstatshcinbytes', 'cnpdallstatshcoutbytes', 'cnpdallstatsinbitrate', 'cnpdallstatsoutbitrate'], name, value)




    class CnpdTopNConfigTable(Entity):
        """
        The cnpdTopNConfigTable is used to configure
        cnpdTopNStatsTable's.
        
        .. attribute:: cnpdtopnconfigentry
        
        	This entry provides the objects to configure and thus initiate the generation of a cnpdTopNStatsTable.
        	**type**\: list of  		 :py:class:`CnpdTopNConfigEntry <ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB.CISCONBARPROTOCOLDISCOVERYMIB.CnpdTopNConfigTable.CnpdTopNConfigEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB'
        _revision = '2002-08-16'

        def __init__(self):
            super(CISCONBARPROTOCOLDISCOVERYMIB.CnpdTopNConfigTable, self).__init__()

            self.yang_name = "cnpdTopNConfigTable"
            self.yang_parent_name = "CISCO-NBAR-PROTOCOL-DISCOVERY-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cnpdTopNConfigEntry", ("cnpdtopnconfigentry", CISCONBARPROTOCOLDISCOVERYMIB.CnpdTopNConfigTable.CnpdTopNConfigEntry))])
            self._leafs = OrderedDict()

            self.cnpdtopnconfigentry = YList(self)
            self._segment_path = lambda: "cnpdTopNConfigTable"
            self._absolute_path = lambda: "CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:CISCO-NBAR-PROTOCOL-DISCOVERY-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCONBARPROTOCOLDISCOVERYMIB.CnpdTopNConfigTable, [], name, value)


        class CnpdTopNConfigEntry(Entity):
            """
            This entry provides the objects to configure and thus
            initiate the generation of a cnpdTopNStatsTable..
            
            .. attribute:: cnpdtopnconfigindex  (key)
            
            	A monotonically increasing integer which uniquely identifies a cnpdTopNConfigEntry  in the cnpdTopNConfigTable
            	**type**\: int
            
            	**range:** 1..50
            
            	**config**\: False
            
            .. attribute:: cnpdtopnconfigifindex
            
            	This object allows the management station to select the interface, which Protocol Discovery is running on, to be used to create this  cnpdTopNConfigEntry
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**config**\: False
            
            .. attribute:: cnpdtopnconfigstatsselect
            
            	This object allows the management station to select the statistic used to base the order of the top\-n table on.  For example\: a cnpdTopNConfigStatsSelect of bitRateSum means order this table based on each applications/protocols combined in and out bitrate
            	**type**\:  :py:class:`CiscoPdDataType <ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB.CiscoPdDataType>`
            
            	**config**\: False
            
            .. attribute:: cnpdtopnconfigsampletime
            
            	If the cnpdTopNConfigStatsSelect is bitRateIn, bitRateOut or bitRateSum, then this value is the interval in seconds that  the bitrate is sampled.  This has no effect if the cnpdTopNConfigStatsSelect is byte or packet based.  When this object is modified by the management  station, a new sample period is started regardless of whether the original cnpdTopNConfigSampleTime was finished
            	**type**\: int
            
            	**range:** 1..2048
            
            	**config**\: False
            
            	**units**\: seconds
            
            .. attribute:: cnpdtopnconfigrequestedsize
            
            	The requested size of the associated  cnpdTopNStatsTable entry.  For example a cnpdTopNConfigRequestedSize of 20 indicates the management station wants to create an associated  cnpdTopNStatsTable  entry of 20 protocol/application's
            	**type**\: int
            
            	**range:** 1..500
            
            	**config**\: False
            
            .. attribute:: cnpdtopnconfiggrantedsize
            
            	The actual size of the associated 	 cnpdTopNStatsTable entry.  The reason this may differ from  cnpdTopNConfigRequestedSize is because a  management station may request a number of  protocols that is greater than the number of  protocols actually found by Protocol Discovery
            	**type**\: int
            
            	**range:** 1..500
            
            	**config**\: False
            
            .. attribute:: cnpdtopnconfigtime
            
            	The value of sysUpTime when the associated cnpdTopNStatsTable entry was created
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cnpdtopnconfigstatus
            
            	This object is used to create or delete  the row entry in cnpdTopNConfigTable.  When creating a row entry the management station is required to specify a value for cnpdTopNConfigIfIndex only.  'notReady' means that a row exists but  either it has no valid IfIndex or it has  not been set to createAndGo or active.  'active' means that a createAndGo or active  has been issued, AND a valid ifIndex exists.  Therefore if a row is 'active' it means a  TopNStats entry has been generated.  If you set an 'active' row to createAndWait  it will get the status 'notReady'.   If you set any row to 'notReady' \- it will go  to the 'notReadystate'.  If you set any row to 'notInService' \- it will  go to the 'notInService' state and the corresponding  TopNStatsEntry will be deleted.  The same TopNConfig entry can be re\-used without  changes by setting it to 'active'. The corresponding  TopStatsTable entry will be regenerated. This can  be used by the NMS to poll a particular TopNConfig  Entry.  Changes to an existing TopNConfig entry can be made by setting the status to 'createAndWait' and changing the necessary objects. Setting it to 'createAndGo' or 'active' will cause the corresponding TopNStats entry to be regenerated
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB'
            _revision = '2002-08-16'

            def __init__(self):
                super(CISCONBARPROTOCOLDISCOVERYMIB.CnpdTopNConfigTable.CnpdTopNConfigEntry, self).__init__()

                self.yang_name = "cnpdTopNConfigEntry"
                self.yang_parent_name = "cnpdTopNConfigTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cnpdtopnconfigindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cnpdtopnconfigindex', (YLeaf(YType.uint32, 'cnpdTopNConfigIndex'), ['int'])),
                    ('cnpdtopnconfigifindex', (YLeaf(YType.int32, 'cnpdTopNConfigIfIndex'), ['int'])),
                    ('cnpdtopnconfigstatsselect', (YLeaf(YType.enumeration, 'cnpdTopNConfigStatsSelect'), [('ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB', 'CiscoPdDataType', '')])),
                    ('cnpdtopnconfigsampletime', (YLeaf(YType.uint32, 'cnpdTopNConfigSampleTime'), ['int'])),
                    ('cnpdtopnconfigrequestedsize', (YLeaf(YType.uint32, 'cnpdTopNConfigRequestedSize'), ['int'])),
                    ('cnpdtopnconfiggrantedsize', (YLeaf(YType.uint32, 'cnpdTopNConfigGrantedSize'), ['int'])),
                    ('cnpdtopnconfigtime', (YLeaf(YType.uint32, 'cnpdTopNConfigTime'), ['int'])),
                    ('cnpdtopnconfigstatus', (YLeaf(YType.enumeration, 'cnpdTopNConfigStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.cnpdtopnconfigindex = None
                self.cnpdtopnconfigifindex = None
                self.cnpdtopnconfigstatsselect = None
                self.cnpdtopnconfigsampletime = None
                self.cnpdtopnconfigrequestedsize = None
                self.cnpdtopnconfiggrantedsize = None
                self.cnpdtopnconfigtime = None
                self.cnpdtopnconfigstatus = None
                self._segment_path = lambda: "cnpdTopNConfigEntry" + "[cnpdTopNConfigIndex='" + str(self.cnpdtopnconfigindex) + "']"
                self._absolute_path = lambda: "CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:CISCO-NBAR-PROTOCOL-DISCOVERY-MIB/cnpdTopNConfigTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCONBARPROTOCOLDISCOVERYMIB.CnpdTopNConfigTable.CnpdTopNConfigEntry, ['cnpdtopnconfigindex', 'cnpdtopnconfigifindex', 'cnpdtopnconfigstatsselect', 'cnpdtopnconfigsampletime', 'cnpdtopnconfigrequestedsize', 'cnpdtopnconfiggrantedsize', 'cnpdtopnconfigtime', 'cnpdtopnconfigstatus'], name, value)




    class CnpdTopNStatsTable(Entity):
        """
        A cnpdTopNStatsTable describes an ordered
        list of protocols.
        
        .. attribute:: cnpdtopnstatsentry
        
        	This entry is used to store a set of objects which  describe a cnpdTopNStatsTable. A cnpdTopNStatsTable  is a number of protocols and statistics sorted  according to the criteria in the associated cnpdTopNConfigEntry.  Therefore a cnpdTopNStatsTable can differ in content  and size according to what was configured in the associated cnpdTopNConfigTableEntry
        	**type**\: list of  		 :py:class:`CnpdTopNStatsEntry <ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB.CISCONBARPROTOCOLDISCOVERYMIB.CnpdTopNStatsTable.CnpdTopNStatsEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB'
        _revision = '2002-08-16'

        def __init__(self):
            super(CISCONBARPROTOCOLDISCOVERYMIB.CnpdTopNStatsTable, self).__init__()

            self.yang_name = "cnpdTopNStatsTable"
            self.yang_parent_name = "CISCO-NBAR-PROTOCOL-DISCOVERY-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cnpdTopNStatsEntry", ("cnpdtopnstatsentry", CISCONBARPROTOCOLDISCOVERYMIB.CnpdTopNStatsTable.CnpdTopNStatsEntry))])
            self._leafs = OrderedDict()

            self.cnpdtopnstatsentry = YList(self)
            self._segment_path = lambda: "cnpdTopNStatsTable"
            self._absolute_path = lambda: "CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:CISCO-NBAR-PROTOCOL-DISCOVERY-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCONBARPROTOCOLDISCOVERYMIB.CnpdTopNStatsTable, [], name, value)


        class CnpdTopNStatsEntry(Entity):
            """
            This entry is used to store a set of objects which 
            describe a cnpdTopNStatsTable. A cnpdTopNStatsTable 
            is a number of protocols and statistics sorted 
            according to the criteria in the associated
            cnpdTopNConfigEntry.
            
            Therefore a cnpdTopNStatsTable can differ in content 
            and size according to what was configured in the associated
            cnpdTopNConfigTableEntry.
            
            .. attribute:: cnpdtopnconfigindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..50
            
            	**refers to**\:  :py:class:`cnpdtopnconfigindex <ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB.CISCONBARPROTOCOLDISCOVERYMIB.CnpdTopNConfigTable.CnpdTopNConfigEntry>`
            
            	**config**\: False
            
            .. attribute:: cnpdtopnstatsindex  (key)
            
            	A monotonically increasing integer which  uniquely identifies a cnpdTopNStatsEntry  in the cnpdTopNStatsTable
            	**type**\: int
            
            	**range:** 1..500
            
            	**config**\: False
            
            .. attribute:: cnpdtopnstatsprotocolname
            
            	Name of the application or protocol,  a unique textual string, assigned in the cnpdSupportedProtocolsTable
            	**type**\: str
            
            	**length:** 1..255
            
            	**config**\: False
            
            .. attribute:: cnpdtopnstatsrate
            
            	The amount of change in the selected statistic during this sampling interval. The selected statistic is the cnpdTopNConfigStatsSelect from the associated cnpdTopNConfigStatsEntry
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cnpdtopnstatshcrate
            
            	The amount of change in the selected statistic during this sampling interval. The selected statistic is the cnpdTopNConfigStatsSelect from the associated cnpdTopNConfigStatsEntry.	  This is the 64\-bit (High Capacity) version of  cnpdTopNStatsRate
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB'
            _revision = '2002-08-16'

            def __init__(self):
                super(CISCONBARPROTOCOLDISCOVERYMIB.CnpdTopNStatsTable.CnpdTopNStatsEntry, self).__init__()

                self.yang_name = "cnpdTopNStatsEntry"
                self.yang_parent_name = "cnpdTopNStatsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cnpdtopnconfigindex','cnpdtopnstatsindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cnpdtopnconfigindex', (YLeaf(YType.str, 'cnpdTopNConfigIndex'), ['int'])),
                    ('cnpdtopnstatsindex', (YLeaf(YType.uint32, 'cnpdTopNStatsIndex'), ['int'])),
                    ('cnpdtopnstatsprotocolname', (YLeaf(YType.str, 'cnpdTopNStatsProtocolName'), ['str'])),
                    ('cnpdtopnstatsrate', (YLeaf(YType.uint32, 'cnpdTopNStatsRate'), ['int'])),
                    ('cnpdtopnstatshcrate', (YLeaf(YType.uint64, 'cnpdTopNStatsHCRate'), ['int'])),
                ])
                self.cnpdtopnconfigindex = None
                self.cnpdtopnstatsindex = None
                self.cnpdtopnstatsprotocolname = None
                self.cnpdtopnstatsrate = None
                self.cnpdtopnstatshcrate = None
                self._segment_path = lambda: "cnpdTopNStatsEntry" + "[cnpdTopNConfigIndex='" + str(self.cnpdtopnconfigindex) + "']" + "[cnpdTopNStatsIndex='" + str(self.cnpdtopnstatsindex) + "']"
                self._absolute_path = lambda: "CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:CISCO-NBAR-PROTOCOL-DISCOVERY-MIB/cnpdTopNStatsTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCONBARPROTOCOLDISCOVERYMIB.CnpdTopNStatsTable.CnpdTopNStatsEntry, ['cnpdtopnconfigindex', 'cnpdtopnstatsindex', 'cnpdtopnstatsprotocolname', 'cnpdtopnstatsrate', 'cnpdtopnstatshcrate'], name, value)




    class CnpdThresholdConfigTable(Entity):
        """
        The cnpdThresholdConfigTable allows the management
        station to create thresholds for the purpose of
        sending notifications if breached, and creating a
        history of breached thresholds.
        
        .. attribute:: cnpdthresholdconfigentry
        
        	This entry contains configuration information to  set thresholds for the purpose of notifications.  The management station is allowed to set thresholds on individual statistics for individual protocols on an interface. If the threshold is breached by the protocol statistic, a new event is written to the cnpdThresholdHistoryTable, which in turn will  generate a Notification Event.  This function has a hysteresis mechanism to limit the generation of events. This mechanism generates one event as a threshold is crossed in the appropriate direction. No more events are generated for that threshold until the opposite threshold is crossed. This stops repeated Notification events being generated each time the value is sampled, when the value is above the threshold. Instead one notification is sent when the threshold is breached and one notification when the statistic drops below the threshold value again
        	**type**\: list of  		 :py:class:`CnpdThresholdConfigEntry <ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB.CISCONBARPROTOCOLDISCOVERYMIB.CnpdThresholdConfigTable.CnpdThresholdConfigEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB'
        _revision = '2002-08-16'

        def __init__(self):
            super(CISCONBARPROTOCOLDISCOVERYMIB.CnpdThresholdConfigTable, self).__init__()

            self.yang_name = "cnpdThresholdConfigTable"
            self.yang_parent_name = "CISCO-NBAR-PROTOCOL-DISCOVERY-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cnpdThresholdConfigEntry", ("cnpdthresholdconfigentry", CISCONBARPROTOCOLDISCOVERYMIB.CnpdThresholdConfigTable.CnpdThresholdConfigEntry))])
            self._leafs = OrderedDict()

            self.cnpdthresholdconfigentry = YList(self)
            self._segment_path = lambda: "cnpdThresholdConfigTable"
            self._absolute_path = lambda: "CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:CISCO-NBAR-PROTOCOL-DISCOVERY-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCONBARPROTOCOLDISCOVERYMIB.CnpdThresholdConfigTable, [], name, value)


        class CnpdThresholdConfigEntry(Entity):
            """
            This entry contains configuration information to 
            set thresholds for the purpose of notifications.
            
            The management station is allowed to set thresholds
            on individual statistics for individual protocols
            on an interface. If the threshold is breached by
            the protocol statistic, a new event is written to
            the cnpdThresholdHistoryTable, which in turn will 
            generate a Notification Event.
            
            This function has a hysteresis mechanism to limit
            the generation of events. This mechanism generates
            one event as a threshold is crossed in the
            appropriate direction. No more events are generated
            for that threshold until the opposite threshold is
            crossed. This stops repeated Notification events
            being generated each time the value is sampled,
            when the value is above the threshold. Instead one
            notification is sent when the threshold is breached
            and one notification when the statistic drops below
            the threshold value again.
            
            .. attribute:: cnpdthresholdconfigindex  (key)
            
            	A monotonically increasing integer which  uniquely identifies an entry in the  cnpdThresholdConfigTable
            	**type**\: int
            
            	**range:** 1..100
            
            	**config**\: False
            
            .. attribute:: cnpdthresholdconfigifindex
            
            	This object allows the management station to  select the interface, which Protocol Discovery is  running on, to be used to create this  cnpdThresholdConfigTable entry
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**config**\: False
            
            .. attribute:: cnpdthresholdconfiginterval
            
            	The interval in seconds over which the data is sampled and compared with cnpdThresholdConfigRising and cnpdThresholdConfigFalling thresholds
            	**type**\: int
            
            	**range:** 1..2048
            
            	**config**\: False
            
            	**units**\: seconds
            
            .. attribute:: cnpdthresholdconfigsampletype
            
            	The method of sampling the selected statistic and calculating the value to be compared against  cnpdThresholdConfigRising or  cnpdThresholdConfigFalling thresholds.  		 If the value of this object is absoluteValue(1),  the value at the end of the sampling interval  cnpdThresholdConfigInterval, will be compared  with the cnpdThresholdConfigRising and  cnpdThresholdConfigFalling thresholds.   In this mode, when cnpdThresholdConfigStatsSelect is byte or packet based, a maximum of two  cnpdThresholdHistory entries will be created per application, as these byte and packet counts  monotonically increase from zero. 		 If the value of this object is deltaValue(2),  the difference between the samples at the  beginning and end of the cnpdThresholdConfigInterval  will be compared with the cnpdThresholdConfigRising  and cnpdThresholdConfigFalling thresholds. 		 Because the difference in the previous and current samples are compared over the sample period cnpdThresholdConfigInterval, this mode provides  more granularity to the thresholds because the NMS  is now provided with the gradient or change in the  cnpdThresholdConfigStatsSelect.  Note that even though the sample value is monotonically increasing for byte and packet counts,  cnpdThresholdConfigSampleType set to deltaValue, can  generate falling cnpdThresholdHistory entries, because the gradient can be lower than the  cnpdThresholdConfigFalling value
            	**type**\:  :py:class:`CnpdThresholdConfigSampleType <ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB.CISCONBARPROTOCOLDISCOVERYMIB.CnpdThresholdConfigTable.CnpdThresholdConfigEntry.CnpdThresholdConfigSampleType>`
            
            	**config**\: False
            
            .. attribute:: cnpdthresholdconfigprotocol
            
            	The application or protocol which the management station wishes to configure a threshold on.  This object is an index into the  SupportedProtocolsTable where details of the protocol can be found.  If cnpdThresholdConfigProtocolAny is set to TRUE this value will be ignored. If it is set to FALSE, then cnpdThresholdConfigProtocol will be the only protocol that is checked to see if it has breached the threshold
            	**type**\: int
            
            	**range:** 1..1024
            
            	**config**\: False
            
            .. attribute:: cnpdthresholdconfigprotocolany
            
            	If set to 'true' \- this threshold is configured to check for any protocol which meets the threshold criteria. This means that multiple protocols can generate ThresholdHistoryTable entries. Each protocol is subject to the hysterisis mechanism.  If set to 'false' \- this threshold is configured to check for the protocol which meets the threshold criteria referred to by cnpdThresholdConfigProtocol
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: cnpdthresholdconfigstatsselect
            
            	This object allows the management station to select the statistic used to base the threshold on.  For example a cnpdThresholdConfigStatsSelect of bitRateSum means cnpdThresholdConfigRising and cnpdThresholdConfigFalling are values based on the combined value of in and out bitrates
            	**type**\:  :py:class:`CiscoPdDataType <ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB.CiscoPdDataType>`
            
            	**config**\: False
            
            .. attribute:: cnpdthresholdconfigstartup
            
            	This controls the type of notification that is  sent when this threshold entry is first enabled.   Because there is no previous sampling history, choosing one of these options determines the type of notification generated \- Rising or Falling.  If the first sample after this entry is enabled  is greater than or equal to cnpdThresholdConfigRising and this object is equal to rising(1) or risingOrFalling(3),  then a single rising notification will be generated.   If the first sample after this entry is enabled is less than or equal to cnpdThresholdConfigFalling and this object is equal to falling(2) or  risingOrFalling(3), then a single falling notification  will be generated
            	**type**\:  :py:class:`CnpdThresholdConfigStartup <ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB.CISCONBARPROTOCOLDISCOVERYMIB.CnpdThresholdConfigTable.CnpdThresholdConfigEntry.CnpdThresholdConfigStartup>`
            
            	**config**\: False
            
            .. attribute:: cnpdthresholdconfigrising
            
            	This is the threshold object which the managment station sets to determine if it gets breached. It  indicates the statistic being sampled was rising.  When the current sample is greater than or  equal to this object, and the value at the last  sampling interval was less than this object (in  other words the value is rising), an entry in the  cnpdThresholdHistoryTable will be created.  After a rising event is generated, another such  event will not be generated until the sampled value falls below this threshold and reaches the cnpdThresholdConfigFalling value.  This ensures that samples which are taken after a cnpdThresholdConfigRising threshold event has been created, do not create further thresholds and therefore notifications, until the  cnpdThresholdConfigFalling threshold has been met.  Thus a very short cnpdThresholdConfigInterval can be chosen without risk of multiple notifications for the same threshold breach condition
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**config**\: False
            
            .. attribute:: cnpdthresholdconfigfalling
            
            	This is the threshold object which the management  station sets to determine if it gets breached. It  indicates the statistic being sampled was falling.   When current sample is less than or equal  to this object, and the value at the last sampling interval was greater than this object (in other  words the value is falling), an entry in the  cnpdThresholdHistoryTable will be created.  		 After a falling event is generated, another  such event will not be generated until the sampled  value rises above this object and reaches the cnpdThresholdConfigRising value
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**config**\: False
            
            .. attribute:: cnpdthresholdconfigstatus
            
            	This object is used to create or delete  the row entry in cnpdThresholdConfigTable.   When creating a row entry the management station  is required to specify a value for  cnpdThresholdConfigIfIndex, cnpdThresholdConfigRising  and cnpdThresholdConfigFalling.  'active' means that a createAndGo or active has  been issued, AND a valid ifIndex exists. And therefore  if a row is 'active' it means a ThresholdHistory entry  may have been generated if the value was breached.  If you set an 'active' row to 'createAndWait' \- it will  in fact get the status 'notReady'.   Likewise if you set any row to 'notInService' or 'notReady'  it will go to the 'notReady' state
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB'
            _revision = '2002-08-16'

            def __init__(self):
                super(CISCONBARPROTOCOLDISCOVERYMIB.CnpdThresholdConfigTable.CnpdThresholdConfigEntry, self).__init__()

                self.yang_name = "cnpdThresholdConfigEntry"
                self.yang_parent_name = "cnpdThresholdConfigTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cnpdthresholdconfigindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cnpdthresholdconfigindex', (YLeaf(YType.uint32, 'cnpdThresholdConfigIndex'), ['int'])),
                    ('cnpdthresholdconfigifindex', (YLeaf(YType.int32, 'cnpdThresholdConfigIfIndex'), ['int'])),
                    ('cnpdthresholdconfiginterval', (YLeaf(YType.uint32, 'cnpdThresholdConfigInterval'), ['int'])),
                    ('cnpdthresholdconfigsampletype', (YLeaf(YType.enumeration, 'cnpdThresholdConfigSampleType'), [('ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB', 'CISCONBARPROTOCOLDISCOVERYMIB', 'CnpdThresholdConfigTable.CnpdThresholdConfigEntry.CnpdThresholdConfigSampleType')])),
                    ('cnpdthresholdconfigprotocol', (YLeaf(YType.uint32, 'cnpdThresholdConfigProtocol'), ['int'])),
                    ('cnpdthresholdconfigprotocolany', (YLeaf(YType.boolean, 'cnpdThresholdConfigProtocolAny'), ['bool'])),
                    ('cnpdthresholdconfigstatsselect', (YLeaf(YType.enumeration, 'cnpdThresholdConfigStatsSelect'), [('ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB', 'CiscoPdDataType', '')])),
                    ('cnpdthresholdconfigstartup', (YLeaf(YType.enumeration, 'cnpdThresholdConfigStartup'), [('ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB', 'CISCONBARPROTOCOLDISCOVERYMIB', 'CnpdThresholdConfigTable.CnpdThresholdConfigEntry.CnpdThresholdConfigStartup')])),
                    ('cnpdthresholdconfigrising', (YLeaf(YType.uint32, 'cnpdThresholdConfigRising'), ['int'])),
                    ('cnpdthresholdconfigfalling', (YLeaf(YType.uint32, 'cnpdThresholdConfigFalling'), ['int'])),
                    ('cnpdthresholdconfigstatus', (YLeaf(YType.enumeration, 'cnpdThresholdConfigStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.cnpdthresholdconfigindex = None
                self.cnpdthresholdconfigifindex = None
                self.cnpdthresholdconfiginterval = None
                self.cnpdthresholdconfigsampletype = None
                self.cnpdthresholdconfigprotocol = None
                self.cnpdthresholdconfigprotocolany = None
                self.cnpdthresholdconfigstatsselect = None
                self.cnpdthresholdconfigstartup = None
                self.cnpdthresholdconfigrising = None
                self.cnpdthresholdconfigfalling = None
                self.cnpdthresholdconfigstatus = None
                self._segment_path = lambda: "cnpdThresholdConfigEntry" + "[cnpdThresholdConfigIndex='" + str(self.cnpdthresholdconfigindex) + "']"
                self._absolute_path = lambda: "CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:CISCO-NBAR-PROTOCOL-DISCOVERY-MIB/cnpdThresholdConfigTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCONBARPROTOCOLDISCOVERYMIB.CnpdThresholdConfigTable.CnpdThresholdConfigEntry, ['cnpdthresholdconfigindex', 'cnpdthresholdconfigifindex', 'cnpdthresholdconfiginterval', 'cnpdthresholdconfigsampletype', 'cnpdthresholdconfigprotocol', 'cnpdthresholdconfigprotocolany', 'cnpdthresholdconfigstatsselect', 'cnpdthresholdconfigstartup', 'cnpdthresholdconfigrising', 'cnpdthresholdconfigfalling', 'cnpdthresholdconfigstatus'], name, value)

            class CnpdThresholdConfigSampleType(Enum):
                """
                CnpdThresholdConfigSampleType (Enum Class)

                The method of sampling the selected statistic and

                calculating the value to be compared against 

                cnpdThresholdConfigRising or 

                cnpdThresholdConfigFalling thresholds. 

                If the value of this object is absoluteValue(1), 

                the value at the end of the sampling interval 

                cnpdThresholdConfigInterval, will be compared 

                with the cnpdThresholdConfigRising and 

                cnpdThresholdConfigFalling thresholds. 

                In this mode, when cnpdThresholdConfigStatsSelect is

                byte or packet based, a maximum of two 

                cnpdThresholdHistory entries will be created per

                application, as these byte and packet counts 

                monotonically increase from zero.

                If the value of this object is deltaValue(2), 

                the difference between the samples at the 

                beginning and end of the cnpdThresholdConfigInterval 

                will be compared with the cnpdThresholdConfigRising 

                and cnpdThresholdConfigFalling thresholds.

                Because the difference in the previous and current

                samples are compared over the sample period

                cnpdThresholdConfigInterval, this mode provides 

                more granularity to the thresholds because the NMS 

                is now provided with the gradient or change in the 

                cnpdThresholdConfigStatsSelect.

                Note that even though the sample value is monotonically

                increasing for byte and packet counts, 

                cnpdThresholdConfigSampleType set to deltaValue, can 

                generate falling cnpdThresholdHistory entries, because

                the gradient can be lower than the 

                cnpdThresholdConfigFalling value.

                .. data:: absoluteValue = 1

                .. data:: deltaValue = 2

                """

                absoluteValue = Enum.YLeaf(1, "absoluteValue")

                deltaValue = Enum.YLeaf(2, "deltaValue")


            class CnpdThresholdConfigStartup(Enum):
                """
                CnpdThresholdConfigStartup (Enum Class)

                This controls the type of notification that is 

                sent when this threshold entry is first enabled. 

                Because there is no previous sampling history,

                choosing one of these options determines the type

                of notification generated \- Rising or Falling.

                If the first sample after this entry is enabled 

                is greater than or equal to cnpdThresholdConfigRising and

                this object is equal to rising(1) or risingOrFalling(3), 

                then a single rising notification will be generated. 

                If the first sample after this entry is enabled

                is less than or equal to cnpdThresholdConfigFalling

                and this object is equal to falling(2) or 

                risingOrFalling(3), then a single falling notification 

                will be generated.

                .. data:: rising = 1

                .. data:: falling = 2

                .. data:: risingOrFalling = 3

                """

                rising = Enum.YLeaf(1, "rising")

                falling = Enum.YLeaf(2, "falling")

                risingOrFalling = Enum.YLeaf(3, "risingOrFalling")





    class CnpdThresholdHistoryTable(Entity):
        """
        The Threshold History table. Notifications
        are unreliable so this table provides a
        history of the last 5000 threshold breached
        events. A notification can be traced back to
        its cnpdThresholdHistoryEntry.
        
        .. attribute:: cnpdthresholdhistoryentry
        
        	This entry is created each time a threshold  is breached.   Thus there is not necessarily a one to one  relationship to cnpdThresholdConfigTable  as not every Threshold configured will  be breached
        	**type**\: list of  		 :py:class:`CnpdThresholdHistoryEntry <ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB.CISCONBARPROTOCOLDISCOVERYMIB.CnpdThresholdHistoryTable.CnpdThresholdHistoryEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB'
        _revision = '2002-08-16'

        def __init__(self):
            super(CISCONBARPROTOCOLDISCOVERYMIB.CnpdThresholdHistoryTable, self).__init__()

            self.yang_name = "cnpdThresholdHistoryTable"
            self.yang_parent_name = "CISCO-NBAR-PROTOCOL-DISCOVERY-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cnpdThresholdHistoryEntry", ("cnpdthresholdhistoryentry", CISCONBARPROTOCOLDISCOVERYMIB.CnpdThresholdHistoryTable.CnpdThresholdHistoryEntry))])
            self._leafs = OrderedDict()

            self.cnpdthresholdhistoryentry = YList(self)
            self._segment_path = lambda: "cnpdThresholdHistoryTable"
            self._absolute_path = lambda: "CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:CISCO-NBAR-PROTOCOL-DISCOVERY-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCONBARPROTOCOLDISCOVERYMIB.CnpdThresholdHistoryTable, [], name, value)


        class CnpdThresholdHistoryEntry(Entity):
            """
            This entry is created each time a threshold 
            is breached. 
            
            Thus there is not necessarily a one to one 
            relationship to cnpdThresholdConfigTable 
            as not every Threshold configured will 
            be breached.
            
            .. attribute:: cnpdthresholdhistoryindex  (key)
            
            	A monotonically increasing integer which uniquely identifies this  cnpdThresholdHistoryEntry in the  cnpdThresholdHistory table
            	**type**\: int
            
            	**range:** 1..1000
            
            	**config**\: False
            
            .. attribute:: cnpdthresholdhistoryconfigindex
            
            	The cnpdThresholdConfigTable entry  which generated this entry. Using this  object the management station can backtrack  to the appropriate cnpdThresholdConfigEntry
            	**type**\: int
            
            	**range:** 1..1000
            
            	**config**\: False
            
            .. attribute:: cnpdthresholdhistoryvalue
            
            	The actual value of the statistic when  the sampling was made
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**config**\: False
            
            .. attribute:: cnpdthresholdhistorytype
            
            	Describes whether this is an event caused by a rising or falling threshold breach
            	**type**\:  :py:class:`CnpdThresholdHistoryType <ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB.CISCONBARPROTOCOLDISCOVERYMIB.CnpdThresholdHistoryTable.CnpdThresholdHistoryEntry.CnpdThresholdHistoryType>`
            
            	**config**\: False
            
            .. attribute:: cnpdthresholdhistorytime
            
            	The value of sysUpTime of the running  configuration when the event occurred
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cnpdthresholdhistoryprotocol
            
            	The application or protocol which the management station configured a threshold on.  This object is an index into the  SupportedProtocolsTable where details of the protocol can be found
            	**type**\: int
            
            	**range:** 1..1024
            
            	**config**\: False
            
            .. attribute:: cnpdthresholdhistorystatsselect
            
            	This is the statistic used to base the threshold on
            	**type**\:  :py:class:`CiscoPdDataType <ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB.CiscoPdDataType>`
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB'
            _revision = '2002-08-16'

            def __init__(self):
                super(CISCONBARPROTOCOLDISCOVERYMIB.CnpdThresholdHistoryTable.CnpdThresholdHistoryEntry, self).__init__()

                self.yang_name = "cnpdThresholdHistoryEntry"
                self.yang_parent_name = "cnpdThresholdHistoryTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cnpdthresholdhistoryindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cnpdthresholdhistoryindex', (YLeaf(YType.uint32, 'cnpdThresholdHistoryIndex'), ['int'])),
                    ('cnpdthresholdhistoryconfigindex', (YLeaf(YType.uint32, 'cnpdThresholdHistoryConfigIndex'), ['int'])),
                    ('cnpdthresholdhistoryvalue', (YLeaf(YType.uint32, 'cnpdThresholdHistoryValue'), ['int'])),
                    ('cnpdthresholdhistorytype', (YLeaf(YType.enumeration, 'cnpdThresholdHistoryType'), [('ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB', 'CISCONBARPROTOCOLDISCOVERYMIB', 'CnpdThresholdHistoryTable.CnpdThresholdHistoryEntry.CnpdThresholdHistoryType')])),
                    ('cnpdthresholdhistorytime', (YLeaf(YType.uint32, 'cnpdThresholdHistoryTime'), ['int'])),
                    ('cnpdthresholdhistoryprotocol', (YLeaf(YType.uint32, 'cnpdThresholdHistoryProtocol'), ['int'])),
                    ('cnpdthresholdhistorystatsselect', (YLeaf(YType.enumeration, 'cnpdThresholdHistoryStatsSelect'), [('ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB', 'CiscoPdDataType', '')])),
                ])
                self.cnpdthresholdhistoryindex = None
                self.cnpdthresholdhistoryconfigindex = None
                self.cnpdthresholdhistoryvalue = None
                self.cnpdthresholdhistorytype = None
                self.cnpdthresholdhistorytime = None
                self.cnpdthresholdhistoryprotocol = None
                self.cnpdthresholdhistorystatsselect = None
                self._segment_path = lambda: "cnpdThresholdHistoryEntry" + "[cnpdThresholdHistoryIndex='" + str(self.cnpdthresholdhistoryindex) + "']"
                self._absolute_path = lambda: "CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:CISCO-NBAR-PROTOCOL-DISCOVERY-MIB/cnpdThresholdHistoryTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCONBARPROTOCOLDISCOVERYMIB.CnpdThresholdHistoryTable.CnpdThresholdHistoryEntry, ['cnpdthresholdhistoryindex', 'cnpdthresholdhistoryconfigindex', 'cnpdthresholdhistoryvalue', 'cnpdthresholdhistorytype', 'cnpdthresholdhistorytime', 'cnpdthresholdhistoryprotocol', 'cnpdthresholdhistorystatsselect'], name, value)

            class CnpdThresholdHistoryType(Enum):
                """
                CnpdThresholdHistoryType (Enum Class)

                Describes whether this is an

                event caused by a rising

                or falling threshold breach.

                .. data:: risingBreach = 1

                .. data:: fallingBreach = 2

                """

                risingBreach = Enum.YLeaf(1, "risingBreach")

                fallingBreach = Enum.YLeaf(2, "fallingBreach")





    class CnpdSupportedProtocolsTable(Entity):
        """
        The Supported Protocols table lists all the 
        protocols and applications which NBAR is currently
        capable of recognizing.
        
        .. attribute:: cnpdsupportedprotocolsentry
        
        	A entry in the Supported Protocols table reflecting key information about a protocol
        	**type**\: list of  		 :py:class:`CnpdSupportedProtocolsEntry <ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB.CISCONBARPROTOCOLDISCOVERYMIB.CnpdSupportedProtocolsTable.CnpdSupportedProtocolsEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB'
        _revision = '2002-08-16'

        def __init__(self):
            super(CISCONBARPROTOCOLDISCOVERYMIB.CnpdSupportedProtocolsTable, self).__init__()

            self.yang_name = "cnpdSupportedProtocolsTable"
            self.yang_parent_name = "CISCO-NBAR-PROTOCOL-DISCOVERY-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cnpdSupportedProtocolsEntry", ("cnpdsupportedprotocolsentry", CISCONBARPROTOCOLDISCOVERYMIB.CnpdSupportedProtocolsTable.CnpdSupportedProtocolsEntry))])
            self._leafs = OrderedDict()

            self.cnpdsupportedprotocolsentry = YList(self)
            self._segment_path = lambda: "cnpdSupportedProtocolsTable"
            self._absolute_path = lambda: "CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:CISCO-NBAR-PROTOCOL-DISCOVERY-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCONBARPROTOCOLDISCOVERYMIB.CnpdSupportedProtocolsTable, [], name, value)


        class CnpdSupportedProtocolsEntry(Entity):
            """
            A entry in the Supported Protocols table reflecting
            key information about a protocol.
            
            .. attribute:: cnpdsupportedprotocolsindex  (key)
            
            	A unique identifier of a row in this table.  Thus it also represents a unique identifier for a protocol or application which NBAR currently recognizes
            	**type**\: int
            
            	**range:** 1..1024
            
            	**config**\: False
            
            .. attribute:: cnpdsupportedprotocolsname
            
            	This object reflects the valid string of a protocol or application which NBAR currently recognizes
            	**type**\: str
            
            	**length:** 1..255
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB'
            _revision = '2002-08-16'

            def __init__(self):
                super(CISCONBARPROTOCOLDISCOVERYMIB.CnpdSupportedProtocolsTable.CnpdSupportedProtocolsEntry, self).__init__()

                self.yang_name = "cnpdSupportedProtocolsEntry"
                self.yang_parent_name = "cnpdSupportedProtocolsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cnpdsupportedprotocolsindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cnpdsupportedprotocolsindex', (YLeaf(YType.uint32, 'cnpdSupportedProtocolsIndex'), ['int'])),
                    ('cnpdsupportedprotocolsname', (YLeaf(YType.str, 'cnpdSupportedProtocolsName'), ['str'])),
                ])
                self.cnpdsupportedprotocolsindex = None
                self.cnpdsupportedprotocolsname = None
                self._segment_path = lambda: "cnpdSupportedProtocolsEntry" + "[cnpdSupportedProtocolsIndex='" + str(self.cnpdsupportedprotocolsindex) + "']"
                self._absolute_path = lambda: "CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:CISCO-NBAR-PROTOCOL-DISCOVERY-MIB/cnpdSupportedProtocolsTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCONBARPROTOCOLDISCOVERYMIB.CnpdSupportedProtocolsTable.CnpdSupportedProtocolsEntry, ['cnpdsupportedprotocolsindex', 'cnpdsupportedprotocolsname'], name, value)



    def clone_ptr(self):
        self._top_entity = CISCONBARPROTOCOLDISCOVERYMIB()
        return self._top_entity



