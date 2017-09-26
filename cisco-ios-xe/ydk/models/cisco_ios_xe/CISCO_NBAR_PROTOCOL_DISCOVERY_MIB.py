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
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class CiscoPdDataType(Enum):
    """
    CiscoPdDataType

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
    
    
    .. attribute:: cnpdallstatstable
    
    	The cnpdAllStatsTable contains all the statistics available for all the protocols/applications currently recognized by NBAR Protocol Discovery for a particular  interface.  In the event of an overflow, the 32 bit counters are not  valid. There is no overflow support
    	**type**\:   :py:class:`Cnpdallstatstable <ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB.CISCONBARPROTOCOLDISCOVERYMIB.Cnpdallstatstable>`
    
    .. attribute:: cnpdnotificationsconfig
    
    	
    	**type**\:   :py:class:`Cnpdnotificationsconfig <ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB.CISCONBARPROTOCOLDISCOVERYMIB.Cnpdnotificationsconfig>`
    
    .. attribute:: cnpdstatustable
    
    	The cnpdStatusTable is used to enable and disable Protocol Discovery on an interface
    	**type**\:   :py:class:`Cnpdstatustable <ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB.CISCONBARPROTOCOLDISCOVERYMIB.Cnpdstatustable>`
    
    .. attribute:: cnpdsupportedprotocolstable
    
    	The Supported Protocols table lists all the  protocols and applications which NBAR is currently capable of recognizing
    	**type**\:   :py:class:`Cnpdsupportedprotocolstable <ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB.CISCONBARPROTOCOLDISCOVERYMIB.Cnpdsupportedprotocolstable>`
    
    .. attribute:: cnpdthresholdconfigtable
    
    	The cnpdThresholdConfigTable allows the management station to create thresholds for the purpose of sending notifications if breached, and creating a history of breached thresholds
    	**type**\:   :py:class:`Cnpdthresholdconfigtable <ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB.CISCONBARPROTOCOLDISCOVERYMIB.Cnpdthresholdconfigtable>`
    
    .. attribute:: cnpdthresholdhistorytable
    
    	The Threshold History table. Notifications are unreliable so this table provides a history of the last 5000 threshold breached events. A notification can be traced back to its cnpdThresholdHistoryEntry
    	**type**\:   :py:class:`Cnpdthresholdhistorytable <ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB.CISCONBARPROTOCOLDISCOVERYMIB.Cnpdthresholdhistorytable>`
    
    .. attribute:: cnpdtopnconfigtable
    
    	The cnpdTopNConfigTable is used to configure cnpdTopNStatsTable's
    	**type**\:   :py:class:`Cnpdtopnconfigtable <ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB.CISCONBARPROTOCOLDISCOVERYMIB.Cnpdtopnconfigtable>`
    
    .. attribute:: cnpdtopnstatstable
    
    	A cnpdTopNStatsTable describes an ordered list of protocols
    	**type**\:   :py:class:`Cnpdtopnstatstable <ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB.CISCONBARPROTOCOLDISCOVERYMIB.Cnpdtopnstatstable>`
    
    

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
        self._child_container_classes = {"cnpdAllStatsTable" : ("cnpdallstatstable", CISCONBARPROTOCOLDISCOVERYMIB.Cnpdallstatstable), "cnpdNotificationsConfig" : ("cnpdnotificationsconfig", CISCONBARPROTOCOLDISCOVERYMIB.Cnpdnotificationsconfig), "cnpdStatusTable" : ("cnpdstatustable", CISCONBARPROTOCOLDISCOVERYMIB.Cnpdstatustable), "cnpdSupportedProtocolsTable" : ("cnpdsupportedprotocolstable", CISCONBARPROTOCOLDISCOVERYMIB.Cnpdsupportedprotocolstable), "cnpdThresholdConfigTable" : ("cnpdthresholdconfigtable", CISCONBARPROTOCOLDISCOVERYMIB.Cnpdthresholdconfigtable), "cnpdThresholdHistoryTable" : ("cnpdthresholdhistorytable", CISCONBARPROTOCOLDISCOVERYMIB.Cnpdthresholdhistorytable), "cnpdTopNConfigTable" : ("cnpdtopnconfigtable", CISCONBARPROTOCOLDISCOVERYMIB.Cnpdtopnconfigtable), "cnpdTopNStatsTable" : ("cnpdtopnstatstable", CISCONBARPROTOCOLDISCOVERYMIB.Cnpdtopnstatstable)}
        self._child_list_classes = {}

        self.cnpdallstatstable = CISCONBARPROTOCOLDISCOVERYMIB.Cnpdallstatstable()
        self.cnpdallstatstable.parent = self
        self._children_name_map["cnpdallstatstable"] = "cnpdAllStatsTable"
        self._children_yang_names.add("cnpdAllStatsTable")

        self.cnpdnotificationsconfig = CISCONBARPROTOCOLDISCOVERYMIB.Cnpdnotificationsconfig()
        self.cnpdnotificationsconfig.parent = self
        self._children_name_map["cnpdnotificationsconfig"] = "cnpdNotificationsConfig"
        self._children_yang_names.add("cnpdNotificationsConfig")

        self.cnpdstatustable = CISCONBARPROTOCOLDISCOVERYMIB.Cnpdstatustable()
        self.cnpdstatustable.parent = self
        self._children_name_map["cnpdstatustable"] = "cnpdStatusTable"
        self._children_yang_names.add("cnpdStatusTable")

        self.cnpdsupportedprotocolstable = CISCONBARPROTOCOLDISCOVERYMIB.Cnpdsupportedprotocolstable()
        self.cnpdsupportedprotocolstable.parent = self
        self._children_name_map["cnpdsupportedprotocolstable"] = "cnpdSupportedProtocolsTable"
        self._children_yang_names.add("cnpdSupportedProtocolsTable")

        self.cnpdthresholdconfigtable = CISCONBARPROTOCOLDISCOVERYMIB.Cnpdthresholdconfigtable()
        self.cnpdthresholdconfigtable.parent = self
        self._children_name_map["cnpdthresholdconfigtable"] = "cnpdThresholdConfigTable"
        self._children_yang_names.add("cnpdThresholdConfigTable")

        self.cnpdthresholdhistorytable = CISCONBARPROTOCOLDISCOVERYMIB.Cnpdthresholdhistorytable()
        self.cnpdthresholdhistorytable.parent = self
        self._children_name_map["cnpdthresholdhistorytable"] = "cnpdThresholdHistoryTable"
        self._children_yang_names.add("cnpdThresholdHistoryTable")

        self.cnpdtopnconfigtable = CISCONBARPROTOCOLDISCOVERYMIB.Cnpdtopnconfigtable()
        self.cnpdtopnconfigtable.parent = self
        self._children_name_map["cnpdtopnconfigtable"] = "cnpdTopNConfigTable"
        self._children_yang_names.add("cnpdTopNConfigTable")

        self.cnpdtopnstatstable = CISCONBARPROTOCOLDISCOVERYMIB.Cnpdtopnstatstable()
        self.cnpdtopnstatstable.parent = self
        self._children_name_map["cnpdtopnstatstable"] = "cnpdTopNStatsTable"
        self._children_yang_names.add("cnpdTopNStatsTable")
        self._segment_path = lambda: "CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:CISCO-NBAR-PROTOCOL-DISCOVERY-MIB"


    class Cnpdallstatstable(Entity):
        """
        The cnpdAllStatsTable contains all the statistics
        available for all the protocols/applications currently
        recognized by NBAR Protocol Discovery for a particular 
        interface.
        
        In the event of an overflow, the 32 bit counters are not 
        valid. There is no overflow support.
        
        .. attribute:: cnpdallstatsentry
        
        	An entry in the cnpdAllStatsTable table. This entry  contains the statistics collected on all the protocols  which NBAR classifies for a particular interface
        	**type**\: list of    :py:class:`Cnpdallstatsentry <ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB.CISCONBARPROTOCOLDISCOVERYMIB.Cnpdallstatstable.Cnpdallstatsentry>`
        
        

        """

        _prefix = 'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB'
        _revision = '2002-08-16'

        def __init__(self):
            super(CISCONBARPROTOCOLDISCOVERYMIB.Cnpdallstatstable, self).__init__()

            self.yang_name = "cnpdAllStatsTable"
            self.yang_parent_name = "CISCO-NBAR-PROTOCOL-DISCOVERY-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"cnpdAllStatsEntry" : ("cnpdallstatsentry", CISCONBARPROTOCOLDISCOVERYMIB.Cnpdallstatstable.Cnpdallstatsentry)}

            self.cnpdallstatsentry = YList(self)
            self._segment_path = lambda: "cnpdAllStatsTable"
            self._absolute_path = lambda: "CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:CISCO-NBAR-PROTOCOL-DISCOVERY-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCONBARPROTOCOLDISCOVERYMIB.Cnpdallstatstable, [], name, value)


        class Cnpdallstatsentry(Entity):
            """
            An entry in the cnpdAllStatsTable table. This entry 
            contains the statistics collected on all the protocols 
            which NBAR classifies for a particular interface.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.Iftable.Ifentry>`
            
            .. attribute:: cnpdallstatsprotocolsindex  <key>
            
            	An object which represents a unique  identifier for a protocol or application  which NBAR currently recognizes.  This object is an index into the  SupportedProtocolsTable where details of the protocol can be found
            	**type**\:  int
            
            	**range:** 1..1024
            
            .. attribute:: cnpdallstatshcinbytes
            
            	The byte count of inbound octets as  determined by Protocol Discovery. This is the 64\-bit (High Capacity) version of cnpdAllStatsInBytes
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: bytes
            
            .. attribute:: cnpdallstatshcinpkts
            
            	The packet count of inbound packets as  determined by Protocol Discovery. This is the 64\-bit (High Capacity) version of cnpdAllStatsInPkts
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: packets
            
            .. attribute:: cnpdallstatshcoutbytes
            
            	The byte count of outbound octets as  determined by Protocol Discovery. This is the 64\-bit (High Capacity) version of cnpdAllStatsOutBytes
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: bytes
            
            .. attribute:: cnpdallstatshcoutpkts
            
            	The packet count of outbound packets as  determined by Protocol Discovery. This is the 64\-bit (High Capacity) version of cnpdAllStatsOutPkts
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: packets
            
            .. attribute:: cnpdallstatsinbitrate
            
            	The inbound bit rate as determined  by Protocol Discovery
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            	**units**\: kilo bits per second
            
            .. attribute:: cnpdallstatsinbytes
            
            	The byte count of inbound octets as  determined by Protocol Discovery
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: bytes
            
            .. attribute:: cnpdallstatsinpkts
            
            	The packet count of inbound packets as  determined by Protocol Discovery
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: packets
            
            .. attribute:: cnpdallstatsoutbitrate
            
            	The outbound bit rate as determined  by Protocol Discovery
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            	**units**\: kilo bits per second
            
            .. attribute:: cnpdallstatsoutbytes
            
            	The byte count of outbound octets as determined by Protocol Discovery
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: bytes
            
            .. attribute:: cnpdallstatsoutpkts
            
            	The packet count of outbound packets as  determined by Protocol Discovery
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: packets
            
            .. attribute:: cnpdallstatsprotocolname
            
            	Name of the application or protocol, a  unique textual string, assigned in the cnpdSupportedProtocolsTable
            	**type**\:  str
            
            	**length:** 1..255
            
            

            """

            _prefix = 'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB'
            _revision = '2002-08-16'

            def __init__(self):
                super(CISCONBARPROTOCOLDISCOVERYMIB.Cnpdallstatstable.Cnpdallstatsentry, self).__init__()

                self.yang_name = "cnpdAllStatsEntry"
                self.yang_parent_name = "cnpdAllStatsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.cnpdallstatsprotocolsindex = YLeaf(YType.uint32, "cnpdAllStatsProtocolsIndex")

                self.cnpdallstatshcinbytes = YLeaf(YType.uint64, "cnpdAllStatsHCInBytes")

                self.cnpdallstatshcinpkts = YLeaf(YType.uint64, "cnpdAllStatsHCInPkts")

                self.cnpdallstatshcoutbytes = YLeaf(YType.uint64, "cnpdAllStatsHCOutBytes")

                self.cnpdallstatshcoutpkts = YLeaf(YType.uint64, "cnpdAllStatsHCOutPkts")

                self.cnpdallstatsinbitrate = YLeaf(YType.uint32, "cnpdAllStatsInBitRate")

                self.cnpdallstatsinbytes = YLeaf(YType.uint32, "cnpdAllStatsInBytes")

                self.cnpdallstatsinpkts = YLeaf(YType.uint32, "cnpdAllStatsInPkts")

                self.cnpdallstatsoutbitrate = YLeaf(YType.uint32, "cnpdAllStatsOutBitRate")

                self.cnpdallstatsoutbytes = YLeaf(YType.uint32, "cnpdAllStatsOutBytes")

                self.cnpdallstatsoutpkts = YLeaf(YType.uint32, "cnpdAllStatsOutPkts")

                self.cnpdallstatsprotocolname = YLeaf(YType.str, "cnpdAllStatsProtocolName")
                self._segment_path = lambda: "cnpdAllStatsEntry" + "[ifIndex='" + self.ifindex.get() + "']" + "[cnpdAllStatsProtocolsIndex='" + self.cnpdallstatsprotocolsindex.get() + "']"
                self._absolute_path = lambda: "CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:CISCO-NBAR-PROTOCOL-DISCOVERY-MIB/cnpdAllStatsTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCONBARPROTOCOLDISCOVERYMIB.Cnpdallstatstable.Cnpdallstatsentry, ['ifindex', 'cnpdallstatsprotocolsindex', 'cnpdallstatshcinbytes', 'cnpdallstatshcinpkts', 'cnpdallstatshcoutbytes', 'cnpdallstatshcoutpkts', 'cnpdallstatsinbitrate', 'cnpdallstatsinbytes', 'cnpdallstatsinpkts', 'cnpdallstatsoutbitrate', 'cnpdallstatsoutbytes', 'cnpdallstatsoutpkts', 'cnpdallstatsprotocolname'], name, value)


    class Cnpdnotificationsconfig(Entity):
        """
        
        
        .. attribute:: cnpdnotificationsenable
        
        	This object is used to enable or disable  Notifications on a global basis.   If set to 'true' \- Notifications are enabled. If set to 'false' \- Notifications are disabled
        	**type**\:  bool
        
        

        """

        _prefix = 'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB'
        _revision = '2002-08-16'

        def __init__(self):
            super(CISCONBARPROTOCOLDISCOVERYMIB.Cnpdnotificationsconfig, self).__init__()

            self.yang_name = "cnpdNotificationsConfig"
            self.yang_parent_name = "CISCO-NBAR-PROTOCOL-DISCOVERY-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.cnpdnotificationsenable = YLeaf(YType.boolean, "cnpdNotificationsEnable")
            self._segment_path = lambda: "cnpdNotificationsConfig"
            self._absolute_path = lambda: "CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:CISCO-NBAR-PROTOCOL-DISCOVERY-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCONBARPROTOCOLDISCOVERYMIB.Cnpdnotificationsconfig, ['cnpdnotificationsenable'], name, value)


    class Cnpdstatustable(Entity):
        """
        The cnpdStatusTable is used to enable and
        disable Protocol Discovery on an interface.
        
        .. attribute:: cnpdstatusentry
        
        	An entry in the cnpdStatusTable contains objects for enabling or disabling Protocol Discovery on a per interface basis
        	**type**\: list of    :py:class:`Cnpdstatusentry <ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB.CISCONBARPROTOCOLDISCOVERYMIB.Cnpdstatustable.Cnpdstatusentry>`
        
        

        """

        _prefix = 'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB'
        _revision = '2002-08-16'

        def __init__(self):
            super(CISCONBARPROTOCOLDISCOVERYMIB.Cnpdstatustable, self).__init__()

            self.yang_name = "cnpdStatusTable"
            self.yang_parent_name = "CISCO-NBAR-PROTOCOL-DISCOVERY-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"cnpdStatusEntry" : ("cnpdstatusentry", CISCONBARPROTOCOLDISCOVERYMIB.Cnpdstatustable.Cnpdstatusentry)}

            self.cnpdstatusentry = YList(self)
            self._segment_path = lambda: "cnpdStatusTable"
            self._absolute_path = lambda: "CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:CISCO-NBAR-PROTOCOL-DISCOVERY-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCONBARPROTOCOLDISCOVERYMIB.Cnpdstatustable, [], name, value)


        class Cnpdstatusentry(Entity):
            """
            An entry in the cnpdStatusTable contains objects
            for enabling or disabling Protocol Discovery on a
            per interface basis.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.Iftable.Ifentry>`
            
            .. attribute:: cnpdstatuslastupdatetime
            
            	The value of sysUpTime at the time Protocol  Discovery was last enabled  on an interface. If the interface does not have Protocol Discovery enabled this value is zero
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cnpdstatuspdenable
            
            	This object is used to enable or disable  Protocol Discovery on an interface.   If set to 'true' \- Protocol Discovery is  enabled on this Interface.  If set to 'false' \- Protocol Discovery is  disabled on this Interface
            	**type**\:  bool
            
            

            """

            _prefix = 'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB'
            _revision = '2002-08-16'

            def __init__(self):
                super(CISCONBARPROTOCOLDISCOVERYMIB.Cnpdstatustable.Cnpdstatusentry, self).__init__()

                self.yang_name = "cnpdStatusEntry"
                self.yang_parent_name = "cnpdStatusTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.cnpdstatuslastupdatetime = YLeaf(YType.uint32, "cnpdStatusLastUpdateTime")

                self.cnpdstatuspdenable = YLeaf(YType.boolean, "cnpdStatusPdEnable")
                self._segment_path = lambda: "cnpdStatusEntry" + "[ifIndex='" + self.ifindex.get() + "']"
                self._absolute_path = lambda: "CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:CISCO-NBAR-PROTOCOL-DISCOVERY-MIB/cnpdStatusTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCONBARPROTOCOLDISCOVERYMIB.Cnpdstatustable.Cnpdstatusentry, ['ifindex', 'cnpdstatuslastupdatetime', 'cnpdstatuspdenable'], name, value)


    class Cnpdsupportedprotocolstable(Entity):
        """
        The Supported Protocols table lists all the 
        protocols and applications which NBAR is currently
        capable of recognizing.
        
        .. attribute:: cnpdsupportedprotocolsentry
        
        	A entry in the Supported Protocols table reflecting key information about a protocol
        	**type**\: list of    :py:class:`Cnpdsupportedprotocolsentry <ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB.CISCONBARPROTOCOLDISCOVERYMIB.Cnpdsupportedprotocolstable.Cnpdsupportedprotocolsentry>`
        
        

        """

        _prefix = 'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB'
        _revision = '2002-08-16'

        def __init__(self):
            super(CISCONBARPROTOCOLDISCOVERYMIB.Cnpdsupportedprotocolstable, self).__init__()

            self.yang_name = "cnpdSupportedProtocolsTable"
            self.yang_parent_name = "CISCO-NBAR-PROTOCOL-DISCOVERY-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"cnpdSupportedProtocolsEntry" : ("cnpdsupportedprotocolsentry", CISCONBARPROTOCOLDISCOVERYMIB.Cnpdsupportedprotocolstable.Cnpdsupportedprotocolsentry)}

            self.cnpdsupportedprotocolsentry = YList(self)
            self._segment_path = lambda: "cnpdSupportedProtocolsTable"
            self._absolute_path = lambda: "CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:CISCO-NBAR-PROTOCOL-DISCOVERY-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCONBARPROTOCOLDISCOVERYMIB.Cnpdsupportedprotocolstable, [], name, value)


        class Cnpdsupportedprotocolsentry(Entity):
            """
            A entry in the Supported Protocols table reflecting
            key information about a protocol.
            
            .. attribute:: cnpdsupportedprotocolsindex  <key>
            
            	A unique identifier of a row in this table.  Thus it also represents a unique identifier for a protocol or application which NBAR currently recognizes
            	**type**\:  int
            
            	**range:** 1..1024
            
            .. attribute:: cnpdsupportedprotocolsname
            
            	This object reflects the valid string of a protocol or application which NBAR currently recognizes
            	**type**\:  str
            
            	**length:** 1..255
            
            

            """

            _prefix = 'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB'
            _revision = '2002-08-16'

            def __init__(self):
                super(CISCONBARPROTOCOLDISCOVERYMIB.Cnpdsupportedprotocolstable.Cnpdsupportedprotocolsentry, self).__init__()

                self.yang_name = "cnpdSupportedProtocolsEntry"
                self.yang_parent_name = "cnpdSupportedProtocolsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.cnpdsupportedprotocolsindex = YLeaf(YType.uint32, "cnpdSupportedProtocolsIndex")

                self.cnpdsupportedprotocolsname = YLeaf(YType.str, "cnpdSupportedProtocolsName")
                self._segment_path = lambda: "cnpdSupportedProtocolsEntry" + "[cnpdSupportedProtocolsIndex='" + self.cnpdsupportedprotocolsindex.get() + "']"
                self._absolute_path = lambda: "CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:CISCO-NBAR-PROTOCOL-DISCOVERY-MIB/cnpdSupportedProtocolsTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCONBARPROTOCOLDISCOVERYMIB.Cnpdsupportedprotocolstable.Cnpdsupportedprotocolsentry, ['cnpdsupportedprotocolsindex', 'cnpdsupportedprotocolsname'], name, value)


    class Cnpdthresholdconfigtable(Entity):
        """
        The cnpdThresholdConfigTable allows the management
        station to create thresholds for the purpose of
        sending notifications if breached, and creating a
        history of breached thresholds.
        
        .. attribute:: cnpdthresholdconfigentry
        
        	This entry contains configuration information to  set thresholds for the purpose of notifications.  The management station is allowed to set thresholds on individual statistics for individual protocols on an interface. If the threshold is breached by the protocol statistic, a new event is written to the cnpdThresholdHistoryTable, which in turn will  generate a Notification Event.  This function has a hysteresis mechanism to limit the generation of events. This mechanism generates one event as a threshold is crossed in the appropriate direction. No more events are generated for that threshold until the opposite threshold is crossed. This stops repeated Notification events being generated each time the value is sampled, when the value is above the threshold. Instead one notification is sent when the threshold is breached and one notification when the statistic drops below the threshold value again
        	**type**\: list of    :py:class:`Cnpdthresholdconfigentry <ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB.CISCONBARPROTOCOLDISCOVERYMIB.Cnpdthresholdconfigtable.Cnpdthresholdconfigentry>`
        
        

        """

        _prefix = 'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB'
        _revision = '2002-08-16'

        def __init__(self):
            super(CISCONBARPROTOCOLDISCOVERYMIB.Cnpdthresholdconfigtable, self).__init__()

            self.yang_name = "cnpdThresholdConfigTable"
            self.yang_parent_name = "CISCO-NBAR-PROTOCOL-DISCOVERY-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"cnpdThresholdConfigEntry" : ("cnpdthresholdconfigentry", CISCONBARPROTOCOLDISCOVERYMIB.Cnpdthresholdconfigtable.Cnpdthresholdconfigentry)}

            self.cnpdthresholdconfigentry = YList(self)
            self._segment_path = lambda: "cnpdThresholdConfigTable"
            self._absolute_path = lambda: "CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:CISCO-NBAR-PROTOCOL-DISCOVERY-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCONBARPROTOCOLDISCOVERYMIB.Cnpdthresholdconfigtable, [], name, value)


        class Cnpdthresholdconfigentry(Entity):
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
            
            .. attribute:: cnpdthresholdconfigindex  <key>
            
            	A monotonically increasing integer which  uniquely identifies an entry in the  cnpdThresholdConfigTable
            	**type**\:  int
            
            	**range:** 1..100
            
            .. attribute:: cnpdthresholdconfigfalling
            
            	This is the threshold object which the management  station sets to determine if it gets breached. It  indicates the statistic being sampled was falling.   When current sample is less than or equal  to this object, and the value at the last sampling interval was greater than this object (in other  words the value is falling), an entry in the  cnpdThresholdHistoryTable will be created.  		 After a falling event is generated, another  such event will not be generated until the sampled  value rises above this object and reaches the cnpdThresholdConfigRising value
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: cnpdthresholdconfigifindex
            
            	This object allows the management station to  select the interface, which Protocol Discovery is  running on, to be used to create this  cnpdThresholdConfigTable entry
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: cnpdthresholdconfiginterval
            
            	The interval in seconds over which the data is sampled and compared with cnpdThresholdConfigRising and cnpdThresholdConfigFalling thresholds
            	**type**\:  int
            
            	**range:** 1..2048
            
            	**units**\: seconds
            
            .. attribute:: cnpdthresholdconfigprotocol
            
            	The application or protocol which the management station wishes to configure a threshold on.  This object is an index into the  SupportedProtocolsTable where details of the protocol can be found.  If cnpdThresholdConfigProtocolAny is set to TRUE this value will be ignored. If it is set to FALSE, then cnpdThresholdConfigProtocol will be the only protocol that is checked to see if it has breached the threshold
            	**type**\:  int
            
            	**range:** 1..1024
            
            .. attribute:: cnpdthresholdconfigprotocolany
            
            	If set to 'true' \- this threshold is configured to check for any protocol which meets the threshold criteria. This means that multiple protocols can generate ThresholdHistoryTable entries. Each protocol is subject to the hysterisis mechanism.  If set to 'false' \- this threshold is configured to check for the protocol which meets the threshold criteria referred to by cnpdThresholdConfigProtocol
            	**type**\:  bool
            
            .. attribute:: cnpdthresholdconfigrising
            
            	This is the threshold object which the managment station sets to determine if it gets breached. It  indicates the statistic being sampled was rising.  When the current sample is greater than or  equal to this object, and the value at the last  sampling interval was less than this object (in  other words the value is rising), an entry in the  cnpdThresholdHistoryTable will be created.  After a rising event is generated, another such  event will not be generated until the sampled value falls below this threshold and reaches the cnpdThresholdConfigFalling value.  This ensures that samples which are taken after a cnpdThresholdConfigRising threshold event has been created, do not create further thresholds and therefore notifications, until the  cnpdThresholdConfigFalling threshold has been met.  Thus a very short cnpdThresholdConfigInterval can be chosen without risk of multiple notifications for the same threshold breach condition
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: cnpdthresholdconfigsampletype
            
            	The method of sampling the selected statistic and calculating the value to be compared against  cnpdThresholdConfigRising or  cnpdThresholdConfigFalling thresholds.  		 If the value of this object is absoluteValue(1),  the value at the end of the sampling interval  cnpdThresholdConfigInterval, will be compared  with the cnpdThresholdConfigRising and  cnpdThresholdConfigFalling thresholds.   In this mode, when cnpdThresholdConfigStatsSelect is byte or packet based, a maximum of two  cnpdThresholdHistory entries will be created per application, as these byte and packet counts  monotonically increase from zero. 		 If the value of this object is deltaValue(2),  the difference between the samples at the  beginning and end of the cnpdThresholdConfigInterval  will be compared with the cnpdThresholdConfigRising  and cnpdThresholdConfigFalling thresholds. 		 Because the difference in the previous and current samples are compared over the sample period cnpdThresholdConfigInterval, this mode provides  more granularity to the thresholds because the NMS  is now provided with the gradient or change in the  cnpdThresholdConfigStatsSelect.  Note that even though the sample value is monotonically increasing for byte and packet counts,  cnpdThresholdConfigSampleType set to deltaValue, can  generate falling cnpdThresholdHistory entries, because the gradient can be lower than the  cnpdThresholdConfigFalling value
            	**type**\:   :py:class:`Cnpdthresholdconfigsampletype <ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB.CISCONBARPROTOCOLDISCOVERYMIB.Cnpdthresholdconfigtable.Cnpdthresholdconfigentry.Cnpdthresholdconfigsampletype>`
            
            .. attribute:: cnpdthresholdconfigstartup
            
            	This controls the type of notification that is  sent when this threshold entry is first enabled.   Because there is no previous sampling history, choosing one of these options determines the type of notification generated \- Rising or Falling.  If the first sample after this entry is enabled  is greater than or equal to cnpdThresholdConfigRising and this object is equal to rising(1) or risingOrFalling(3),  then a single rising notification will be generated.   If the first sample after this entry is enabled is less than or equal to cnpdThresholdConfigFalling and this object is equal to falling(2) or  risingOrFalling(3), then a single falling notification  will be generated
            	**type**\:   :py:class:`Cnpdthresholdconfigstartup <ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB.CISCONBARPROTOCOLDISCOVERYMIB.Cnpdthresholdconfigtable.Cnpdthresholdconfigentry.Cnpdthresholdconfigstartup>`
            
            .. attribute:: cnpdthresholdconfigstatsselect
            
            	This object allows the management station to select the statistic used to base the threshold on.  For example a cnpdThresholdConfigStatsSelect of bitRateSum means cnpdThresholdConfigRising and cnpdThresholdConfigFalling are values based on the combined value of in and out bitrates
            	**type**\:   :py:class:`CiscoPdDataType <ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB.CiscoPdDataType>`
            
            .. attribute:: cnpdthresholdconfigstatus
            
            	This object is used to create or delete  the row entry in cnpdThresholdConfigTable.   When creating a row entry the management station  is required to specify a value for  cnpdThresholdConfigIfIndex, cnpdThresholdConfigRising  and cnpdThresholdConfigFalling.  'active' means that a createAndGo or active has  been issued, AND a valid ifIndex exists. And therefore  if a row is 'active' it means a ThresholdHistory entry  may have been generated if the value was breached.  If you set an 'active' row to 'createAndWait' \- it will  in fact get the status 'notReady'.   Likewise if you set any row to 'notInService' or 'notReady'  it will go to the 'notReady' state
            	**type**\:   :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            

            """

            _prefix = 'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB'
            _revision = '2002-08-16'

            def __init__(self):
                super(CISCONBARPROTOCOLDISCOVERYMIB.Cnpdthresholdconfigtable.Cnpdthresholdconfigentry, self).__init__()

                self.yang_name = "cnpdThresholdConfigEntry"
                self.yang_parent_name = "cnpdThresholdConfigTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.cnpdthresholdconfigindex = YLeaf(YType.uint32, "cnpdThresholdConfigIndex")

                self.cnpdthresholdconfigfalling = YLeaf(YType.uint32, "cnpdThresholdConfigFalling")

                self.cnpdthresholdconfigifindex = YLeaf(YType.int32, "cnpdThresholdConfigIfIndex")

                self.cnpdthresholdconfiginterval = YLeaf(YType.uint32, "cnpdThresholdConfigInterval")

                self.cnpdthresholdconfigprotocol = YLeaf(YType.uint32, "cnpdThresholdConfigProtocol")

                self.cnpdthresholdconfigprotocolany = YLeaf(YType.boolean, "cnpdThresholdConfigProtocolAny")

                self.cnpdthresholdconfigrising = YLeaf(YType.uint32, "cnpdThresholdConfigRising")

                self.cnpdthresholdconfigsampletype = YLeaf(YType.enumeration, "cnpdThresholdConfigSampleType")

                self.cnpdthresholdconfigstartup = YLeaf(YType.enumeration, "cnpdThresholdConfigStartup")

                self.cnpdthresholdconfigstatsselect = YLeaf(YType.enumeration, "cnpdThresholdConfigStatsSelect")

                self.cnpdthresholdconfigstatus = YLeaf(YType.enumeration, "cnpdThresholdConfigStatus")
                self._segment_path = lambda: "cnpdThresholdConfigEntry" + "[cnpdThresholdConfigIndex='" + self.cnpdthresholdconfigindex.get() + "']"
                self._absolute_path = lambda: "CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:CISCO-NBAR-PROTOCOL-DISCOVERY-MIB/cnpdThresholdConfigTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCONBARPROTOCOLDISCOVERYMIB.Cnpdthresholdconfigtable.Cnpdthresholdconfigentry, ['cnpdthresholdconfigindex', 'cnpdthresholdconfigfalling', 'cnpdthresholdconfigifindex', 'cnpdthresholdconfiginterval', 'cnpdthresholdconfigprotocol', 'cnpdthresholdconfigprotocolany', 'cnpdthresholdconfigrising', 'cnpdthresholdconfigsampletype', 'cnpdthresholdconfigstartup', 'cnpdthresholdconfigstatsselect', 'cnpdthresholdconfigstatus'], name, value)

            class Cnpdthresholdconfigsampletype(Enum):
                """
                Cnpdthresholdconfigsampletype

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


            class Cnpdthresholdconfigstartup(Enum):
                """
                Cnpdthresholdconfigstartup

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



    class Cnpdthresholdhistorytable(Entity):
        """
        The Threshold History table. Notifications
        are unreliable so this table provides a
        history of the last 5000 threshold breached
        events. A notification can be traced back to
        its cnpdThresholdHistoryEntry.
        
        .. attribute:: cnpdthresholdhistoryentry
        
        	This entry is created each time a threshold  is breached.   Thus there is not necessarily a one to one  relationship to cnpdThresholdConfigTable  as not every Threshold configured will  be breached
        	**type**\: list of    :py:class:`Cnpdthresholdhistoryentry <ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB.CISCONBARPROTOCOLDISCOVERYMIB.Cnpdthresholdhistorytable.Cnpdthresholdhistoryentry>`
        
        

        """

        _prefix = 'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB'
        _revision = '2002-08-16'

        def __init__(self):
            super(CISCONBARPROTOCOLDISCOVERYMIB.Cnpdthresholdhistorytable, self).__init__()

            self.yang_name = "cnpdThresholdHistoryTable"
            self.yang_parent_name = "CISCO-NBAR-PROTOCOL-DISCOVERY-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"cnpdThresholdHistoryEntry" : ("cnpdthresholdhistoryentry", CISCONBARPROTOCOLDISCOVERYMIB.Cnpdthresholdhistorytable.Cnpdthresholdhistoryentry)}

            self.cnpdthresholdhistoryentry = YList(self)
            self._segment_path = lambda: "cnpdThresholdHistoryTable"
            self._absolute_path = lambda: "CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:CISCO-NBAR-PROTOCOL-DISCOVERY-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCONBARPROTOCOLDISCOVERYMIB.Cnpdthresholdhistorytable, [], name, value)


        class Cnpdthresholdhistoryentry(Entity):
            """
            This entry is created each time a threshold 
            is breached. 
            
            Thus there is not necessarily a one to one 
            relationship to cnpdThresholdConfigTable 
            as not every Threshold configured will 
            be breached.
            
            .. attribute:: cnpdthresholdhistoryindex  <key>
            
            	A monotonically increasing integer which uniquely identifies this  cnpdThresholdHistoryEntry in the  cnpdThresholdHistory table
            	**type**\:  int
            
            	**range:** 1..1000
            
            .. attribute:: cnpdthresholdhistoryconfigindex
            
            	The cnpdThresholdConfigTable entry  which generated this entry. Using this  object the management station can backtrack  to the appropriate cnpdThresholdConfigEntry
            	**type**\:  int
            
            	**range:** 1..1000
            
            .. attribute:: cnpdthresholdhistoryprotocol
            
            	The application or protocol which the management station configured a threshold on.  This object is an index into the  SupportedProtocolsTable where details of the protocol can be found
            	**type**\:  int
            
            	**range:** 1..1024
            
            .. attribute:: cnpdthresholdhistorystatsselect
            
            	This is the statistic used to base the threshold on
            	**type**\:   :py:class:`CiscoPdDataType <ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB.CiscoPdDataType>`
            
            .. attribute:: cnpdthresholdhistorytime
            
            	The value of sysUpTime of the running  configuration when the event occurred
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cnpdthresholdhistorytype
            
            	Describes whether this is an event caused by a rising or falling threshold breach
            	**type**\:   :py:class:`Cnpdthresholdhistorytype <ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB.CISCONBARPROTOCOLDISCOVERYMIB.Cnpdthresholdhistorytable.Cnpdthresholdhistoryentry.Cnpdthresholdhistorytype>`
            
            .. attribute:: cnpdthresholdhistoryvalue
            
            	The actual value of the statistic when  the sampling was made
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            

            """

            _prefix = 'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB'
            _revision = '2002-08-16'

            def __init__(self):
                super(CISCONBARPROTOCOLDISCOVERYMIB.Cnpdthresholdhistorytable.Cnpdthresholdhistoryentry, self).__init__()

                self.yang_name = "cnpdThresholdHistoryEntry"
                self.yang_parent_name = "cnpdThresholdHistoryTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.cnpdthresholdhistoryindex = YLeaf(YType.uint32, "cnpdThresholdHistoryIndex")

                self.cnpdthresholdhistoryconfigindex = YLeaf(YType.uint32, "cnpdThresholdHistoryConfigIndex")

                self.cnpdthresholdhistoryprotocol = YLeaf(YType.uint32, "cnpdThresholdHistoryProtocol")

                self.cnpdthresholdhistorystatsselect = YLeaf(YType.enumeration, "cnpdThresholdHistoryStatsSelect")

                self.cnpdthresholdhistorytime = YLeaf(YType.uint32, "cnpdThresholdHistoryTime")

                self.cnpdthresholdhistorytype = YLeaf(YType.enumeration, "cnpdThresholdHistoryType")

                self.cnpdthresholdhistoryvalue = YLeaf(YType.uint32, "cnpdThresholdHistoryValue")
                self._segment_path = lambda: "cnpdThresholdHistoryEntry" + "[cnpdThresholdHistoryIndex='" + self.cnpdthresholdhistoryindex.get() + "']"
                self._absolute_path = lambda: "CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:CISCO-NBAR-PROTOCOL-DISCOVERY-MIB/cnpdThresholdHistoryTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCONBARPROTOCOLDISCOVERYMIB.Cnpdthresholdhistorytable.Cnpdthresholdhistoryentry, ['cnpdthresholdhistoryindex', 'cnpdthresholdhistoryconfigindex', 'cnpdthresholdhistoryprotocol', 'cnpdthresholdhistorystatsselect', 'cnpdthresholdhistorytime', 'cnpdthresholdhistorytype', 'cnpdthresholdhistoryvalue'], name, value)

            class Cnpdthresholdhistorytype(Enum):
                """
                Cnpdthresholdhistorytype

                Describes whether this is an

                event caused by a rising

                or falling threshold breach.

                .. data:: risingBreach = 1

                .. data:: fallingBreach = 2

                """

                risingBreach = Enum.YLeaf(1, "risingBreach")

                fallingBreach = Enum.YLeaf(2, "fallingBreach")



    class Cnpdtopnconfigtable(Entity):
        """
        The cnpdTopNConfigTable is used to configure
        cnpdTopNStatsTable's.
        
        .. attribute:: cnpdtopnconfigentry
        
        	This entry provides the objects to configure and thus initiate the generation of a cnpdTopNStatsTable.
        	**type**\: list of    :py:class:`Cnpdtopnconfigentry <ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB.CISCONBARPROTOCOLDISCOVERYMIB.Cnpdtopnconfigtable.Cnpdtopnconfigentry>`
        
        

        """

        _prefix = 'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB'
        _revision = '2002-08-16'

        def __init__(self):
            super(CISCONBARPROTOCOLDISCOVERYMIB.Cnpdtopnconfigtable, self).__init__()

            self.yang_name = "cnpdTopNConfigTable"
            self.yang_parent_name = "CISCO-NBAR-PROTOCOL-DISCOVERY-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"cnpdTopNConfigEntry" : ("cnpdtopnconfigentry", CISCONBARPROTOCOLDISCOVERYMIB.Cnpdtopnconfigtable.Cnpdtopnconfigentry)}

            self.cnpdtopnconfigentry = YList(self)
            self._segment_path = lambda: "cnpdTopNConfigTable"
            self._absolute_path = lambda: "CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:CISCO-NBAR-PROTOCOL-DISCOVERY-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCONBARPROTOCOLDISCOVERYMIB.Cnpdtopnconfigtable, [], name, value)


        class Cnpdtopnconfigentry(Entity):
            """
            This entry provides the objects to configure and thus
            initiate the generation of a cnpdTopNStatsTable..
            
            .. attribute:: cnpdtopnconfigindex  <key>
            
            	A monotonically increasing integer which uniquely identifies a cnpdTopNConfigEntry  in the cnpdTopNConfigTable
            	**type**\:  int
            
            	**range:** 1..50
            
            .. attribute:: cnpdtopnconfiggrantedsize
            
            	The actual size of the associated 	 cnpdTopNStatsTable entry.  The reason this may differ from  cnpdTopNConfigRequestedSize is because a  management station may request a number of  protocols that is greater than the number of  protocols actually found by Protocol Discovery
            	**type**\:  int
            
            	**range:** 1..500
            
            .. attribute:: cnpdtopnconfigifindex
            
            	This object allows the management station to select the interface, which Protocol Discovery is running on, to be used to create this  cnpdTopNConfigEntry
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: cnpdtopnconfigrequestedsize
            
            	The requested size of the associated  cnpdTopNStatsTable entry.  For example a cnpdTopNConfigRequestedSize of 20 indicates the management station wants to create an associated  cnpdTopNStatsTable  entry of 20 protocol/application's
            	**type**\:  int
            
            	**range:** 1..500
            
            .. attribute:: cnpdtopnconfigsampletime
            
            	If the cnpdTopNConfigStatsSelect is bitRateIn, bitRateOut or bitRateSum, then this value is the interval in seconds that  the bitrate is sampled.  This has no effect if the cnpdTopNConfigStatsSelect is byte or packet based.  When this object is modified by the management  station, a new sample period is started regardless of whether the original cnpdTopNConfigSampleTime was finished
            	**type**\:  int
            
            	**range:** 1..2048
            
            	**units**\: seconds
            
            .. attribute:: cnpdtopnconfigstatsselect
            
            	This object allows the management station to select the statistic used to base the order of the top\-n table on.  For example\: a cnpdTopNConfigStatsSelect of bitRateSum means order this table based on each applications/protocols combined in and out bitrate
            	**type**\:   :py:class:`CiscoPdDataType <ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB.CiscoPdDataType>`
            
            .. attribute:: cnpdtopnconfigstatus
            
            	This object is used to create or delete  the row entry in cnpdTopNConfigTable.  When creating a row entry the management station is required to specify a value for cnpdTopNConfigIfIndex only.  'notReady' means that a row exists but  either it has no valid IfIndex or it has  not been set to createAndGo or active.  'active' means that a createAndGo or active  has been issued, AND a valid ifIndex exists.  Therefore if a row is 'active' it means a  TopNStats entry has been generated.  If you set an 'active' row to createAndWait  it will get the status 'notReady'.   If you set any row to 'notReady' \- it will go  to the 'notReadystate'.  If you set any row to 'notInService' \- it will  go to the 'notInService' state and the corresponding  TopNStatsEntry will be deleted.  The same TopNConfig entry can be re\-used without  changes by setting it to 'active'. The corresponding  TopStatsTable entry will be regenerated. This can  be used by the NMS to poll a particular TopNConfig  Entry.  Changes to an existing TopNConfig entry can be made by setting the status to 'createAndWait' and changing the necessary objects. Setting it to 'createAndGo' or 'active' will cause the corresponding TopNStats entry to be regenerated
            	**type**\:   :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            .. attribute:: cnpdtopnconfigtime
            
            	The value of sysUpTime when the associated cnpdTopNStatsTable entry was created
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB'
            _revision = '2002-08-16'

            def __init__(self):
                super(CISCONBARPROTOCOLDISCOVERYMIB.Cnpdtopnconfigtable.Cnpdtopnconfigentry, self).__init__()

                self.yang_name = "cnpdTopNConfigEntry"
                self.yang_parent_name = "cnpdTopNConfigTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.cnpdtopnconfigindex = YLeaf(YType.uint32, "cnpdTopNConfigIndex")

                self.cnpdtopnconfiggrantedsize = YLeaf(YType.uint32, "cnpdTopNConfigGrantedSize")

                self.cnpdtopnconfigifindex = YLeaf(YType.int32, "cnpdTopNConfigIfIndex")

                self.cnpdtopnconfigrequestedsize = YLeaf(YType.uint32, "cnpdTopNConfigRequestedSize")

                self.cnpdtopnconfigsampletime = YLeaf(YType.uint32, "cnpdTopNConfigSampleTime")

                self.cnpdtopnconfigstatsselect = YLeaf(YType.enumeration, "cnpdTopNConfigStatsSelect")

                self.cnpdtopnconfigstatus = YLeaf(YType.enumeration, "cnpdTopNConfigStatus")

                self.cnpdtopnconfigtime = YLeaf(YType.uint32, "cnpdTopNConfigTime")
                self._segment_path = lambda: "cnpdTopNConfigEntry" + "[cnpdTopNConfigIndex='" + self.cnpdtopnconfigindex.get() + "']"
                self._absolute_path = lambda: "CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:CISCO-NBAR-PROTOCOL-DISCOVERY-MIB/cnpdTopNConfigTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCONBARPROTOCOLDISCOVERYMIB.Cnpdtopnconfigtable.Cnpdtopnconfigentry, ['cnpdtopnconfigindex', 'cnpdtopnconfiggrantedsize', 'cnpdtopnconfigifindex', 'cnpdtopnconfigrequestedsize', 'cnpdtopnconfigsampletime', 'cnpdtopnconfigstatsselect', 'cnpdtopnconfigstatus', 'cnpdtopnconfigtime'], name, value)


    class Cnpdtopnstatstable(Entity):
        """
        A cnpdTopNStatsTable describes an ordered
        list of protocols.
        
        .. attribute:: cnpdtopnstatsentry
        
        	This entry is used to store a set of objects which  describe a cnpdTopNStatsTable. A cnpdTopNStatsTable  is a number of protocols and statistics sorted  according to the criteria in the associated cnpdTopNConfigEntry.  Therefore a cnpdTopNStatsTable can differ in content  and size according to what was configured in the associated cnpdTopNConfigTableEntry
        	**type**\: list of    :py:class:`Cnpdtopnstatsentry <ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB.CISCONBARPROTOCOLDISCOVERYMIB.Cnpdtopnstatstable.Cnpdtopnstatsentry>`
        
        

        """

        _prefix = 'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB'
        _revision = '2002-08-16'

        def __init__(self):
            super(CISCONBARPROTOCOLDISCOVERYMIB.Cnpdtopnstatstable, self).__init__()

            self.yang_name = "cnpdTopNStatsTable"
            self.yang_parent_name = "CISCO-NBAR-PROTOCOL-DISCOVERY-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"cnpdTopNStatsEntry" : ("cnpdtopnstatsentry", CISCONBARPROTOCOLDISCOVERYMIB.Cnpdtopnstatstable.Cnpdtopnstatsentry)}

            self.cnpdtopnstatsentry = YList(self)
            self._segment_path = lambda: "cnpdTopNStatsTable"
            self._absolute_path = lambda: "CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:CISCO-NBAR-PROTOCOL-DISCOVERY-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCONBARPROTOCOLDISCOVERYMIB.Cnpdtopnstatstable, [], name, value)


        class Cnpdtopnstatsentry(Entity):
            """
            This entry is used to store a set of objects which 
            describe a cnpdTopNStatsTable. A cnpdTopNStatsTable 
            is a number of protocols and statistics sorted 
            according to the criteria in the associated
            cnpdTopNConfigEntry.
            
            Therefore a cnpdTopNStatsTable can differ in content 
            and size according to what was configured in the associated
            cnpdTopNConfigTableEntry.
            
            .. attribute:: cnpdtopnconfigindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..50
            
            	**refers to**\:  :py:class:`cnpdtopnconfigindex <ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB.CISCONBARPROTOCOLDISCOVERYMIB.Cnpdtopnconfigtable.Cnpdtopnconfigentry>`
            
            .. attribute:: cnpdtopnstatsindex  <key>
            
            	A monotonically increasing integer which  uniquely identifies a cnpdTopNStatsEntry  in the cnpdTopNStatsTable
            	**type**\:  int
            
            	**range:** 1..500
            
            .. attribute:: cnpdtopnstatshcrate
            
            	The amount of change in the selected statistic during this sampling interval. The selected statistic is the cnpdTopNConfigStatsSelect from the associated cnpdTopNConfigStatsEntry.	  This is the 64\-bit (High Capacity) version of  cnpdTopNStatsRate
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cnpdtopnstatsprotocolname
            
            	Name of the application or protocol,  a unique textual string, assigned in the cnpdSupportedProtocolsTable
            	**type**\:  str
            
            	**length:** 1..255
            
            .. attribute:: cnpdtopnstatsrate
            
            	The amount of change in the selected statistic during this sampling interval. The selected statistic is the cnpdTopNConfigStatsSelect from the associated cnpdTopNConfigStatsEntry
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB'
            _revision = '2002-08-16'

            def __init__(self):
                super(CISCONBARPROTOCOLDISCOVERYMIB.Cnpdtopnstatstable.Cnpdtopnstatsentry, self).__init__()

                self.yang_name = "cnpdTopNStatsEntry"
                self.yang_parent_name = "cnpdTopNStatsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.cnpdtopnconfigindex = YLeaf(YType.str, "cnpdTopNConfigIndex")

                self.cnpdtopnstatsindex = YLeaf(YType.uint32, "cnpdTopNStatsIndex")

                self.cnpdtopnstatshcrate = YLeaf(YType.uint64, "cnpdTopNStatsHCRate")

                self.cnpdtopnstatsprotocolname = YLeaf(YType.str, "cnpdTopNStatsProtocolName")

                self.cnpdtopnstatsrate = YLeaf(YType.uint32, "cnpdTopNStatsRate")
                self._segment_path = lambda: "cnpdTopNStatsEntry" + "[cnpdTopNConfigIndex='" + self.cnpdtopnconfigindex.get() + "']" + "[cnpdTopNStatsIndex='" + self.cnpdtopnstatsindex.get() + "']"
                self._absolute_path = lambda: "CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:CISCO-NBAR-PROTOCOL-DISCOVERY-MIB/cnpdTopNStatsTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCONBARPROTOCOLDISCOVERYMIB.Cnpdtopnstatstable.Cnpdtopnstatsentry, ['cnpdtopnconfigindex', 'cnpdtopnstatsindex', 'cnpdtopnstatshcrate', 'cnpdtopnstatsprotocolname', 'cnpdtopnstatsrate'], name, value)

    def clone_ptr(self):
        self._top_entity = CISCONBARPROTOCOLDISCOVERYMIB()
        return self._top_entity

