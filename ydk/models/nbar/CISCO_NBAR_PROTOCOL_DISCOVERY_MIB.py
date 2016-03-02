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


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError


from ydk.models.snmpv2.SNMPv2_TC import RowStatus_Enum

class CiscoPdDataType_Enum(Enum):
    """
    CiscoPdDataType_Enum

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

    """

    BITRATEIN = 1

    BITRATEOUT = 2

    BITRATESUM = 3

    BYTECOUNTIN = 4

    BYTECOUNTOUT = 5

    BYTECOUNTSUM = 6

    PACKETCOUNTIN = 7

    PACKETCOUNTOUT = 8

    PACKETCOUNTSUM = 9


    @staticmethod
    def _meta_info():
        from ydk.models.nbar._meta import _CISCO_NBAR_PROTOCOL_DISCOVERY_MIB as meta
        return meta._meta_table['CiscoPdDataType_Enum']



class CISCONBARPROTOCOLDISCOVERYMIB(object):
    """
    
    
    .. attribute:: cnpdallstatstable
    
    	The cnpdAllStatsTable contains all the statistics available for all the protocols/applications currently recognized by NBAR Protocol Discovery for a particular  interface.  In the event of an overflow, the 32 bit counters are not  valid. There is no overflow support
    	**type**\: :py:class:`CnpdAllStatsTable <ydk.models.nbar.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB.CISCONBARPROTOCOLDISCOVERYMIB.CnpdAllStatsTable>`
    
    .. attribute:: cnpdnotificationsconfig
    
    	
    	**type**\: :py:class:`CnpdNotificationsConfig <ydk.models.nbar.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB.CISCONBARPROTOCOLDISCOVERYMIB.CnpdNotificationsConfig>`
    
    .. attribute:: cnpdstatustable
    
    	The cnpdStatusTable is used to enable and disable Protocol Discovery on an interface
    	**type**\: :py:class:`CnpdStatusTable <ydk.models.nbar.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB.CISCONBARPROTOCOLDISCOVERYMIB.CnpdStatusTable>`
    
    .. attribute:: cnpdsupportedprotocolstable
    
    	The Supported Protocols table lists all the  protocols and applications which NBAR is currently capable of recognizing
    	**type**\: :py:class:`CnpdSupportedProtocolsTable <ydk.models.nbar.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB.CISCONBARPROTOCOLDISCOVERYMIB.CnpdSupportedProtocolsTable>`
    
    .. attribute:: cnpdthresholdconfigtable
    
    	The cnpdThresholdConfigTable allows the management station to create thresholds for the purpose of sending notifications if breached, and creating a history of breached thresholds
    	**type**\: :py:class:`CnpdThresholdConfigTable <ydk.models.nbar.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB.CISCONBARPROTOCOLDISCOVERYMIB.CnpdThresholdConfigTable>`
    
    .. attribute:: cnpdthresholdhistorytable
    
    	The Threshold History table. Notifications are unreliable so this table provides a history of the last 5000 threshold breached events. A notification can be traced back to its cnpdThresholdHistoryEntry
    	**type**\: :py:class:`CnpdThresholdHistoryTable <ydk.models.nbar.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB.CISCONBARPROTOCOLDISCOVERYMIB.CnpdThresholdHistoryTable>`
    
    .. attribute:: cnpdtopnconfigtable
    
    	The cnpdTopNConfigTable is used to configure cnpdTopNStatsTable's
    	**type**\: :py:class:`CnpdTopNConfigTable <ydk.models.nbar.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB.CISCONBARPROTOCOLDISCOVERYMIB.CnpdTopNConfigTable>`
    
    .. attribute:: cnpdtopnstatstable
    
    	A cnpdTopNStatsTable describes an ordered list of protocols
    	**type**\: :py:class:`CnpdTopNStatsTable <ydk.models.nbar.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB.CISCONBARPROTOCOLDISCOVERYMIB.CnpdTopNStatsTable>`
    
    

    """

    _prefix = 'cisco-nbar'
    _revision = '2002-08-16'

    def __init__(self):
        self.cnpdallstatstable = CISCONBARPROTOCOLDISCOVERYMIB.CnpdAllStatsTable()
        self.cnpdallstatstable.parent = self
        self.cnpdnotificationsconfig = CISCONBARPROTOCOLDISCOVERYMIB.CnpdNotificationsConfig()
        self.cnpdnotificationsconfig.parent = self
        self.cnpdstatustable = CISCONBARPROTOCOLDISCOVERYMIB.CnpdStatusTable()
        self.cnpdstatustable.parent = self
        self.cnpdsupportedprotocolstable = CISCONBARPROTOCOLDISCOVERYMIB.CnpdSupportedProtocolsTable()
        self.cnpdsupportedprotocolstable.parent = self
        self.cnpdthresholdconfigtable = CISCONBARPROTOCOLDISCOVERYMIB.CnpdThresholdConfigTable()
        self.cnpdthresholdconfigtable.parent = self
        self.cnpdthresholdhistorytable = CISCONBARPROTOCOLDISCOVERYMIB.CnpdThresholdHistoryTable()
        self.cnpdthresholdhistorytable.parent = self
        self.cnpdtopnconfigtable = CISCONBARPROTOCOLDISCOVERYMIB.CnpdTopNConfigTable()
        self.cnpdtopnconfigtable.parent = self
        self.cnpdtopnstatstable = CISCONBARPROTOCOLDISCOVERYMIB.CnpdTopNStatsTable()
        self.cnpdtopnstatstable.parent = self


    class CnpdAllStatsTable(object):
        """
        The cnpdAllStatsTable contains all the statistics
        available for all the protocols/applications currently
        recognized by NBAR Protocol Discovery for a particular 
        interface.
        
        In the event of an overflow, the 32 bit counters are not 
        valid. There is no overflow support.
        
        .. attribute:: cnpdallstatsentry
        
        	An entry in the cnpdAllStatsTable table. This entry  contains the statistics collected on all the protocols  which NBAR classifies for a particular interface
        	**type**\: list of :py:class:`CnpdAllStatsEntry <ydk.models.nbar.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB.CISCONBARPROTOCOLDISCOVERYMIB.CnpdAllStatsTable.CnpdAllStatsEntry>`
        
        

        """

        _prefix = 'cisco-nbar'
        _revision = '2002-08-16'

        def __init__(self):
            self.parent = None
            self.cnpdallstatsentry = YList()
            self.cnpdallstatsentry.parent = self
            self.cnpdallstatsentry.name = 'cnpdallstatsentry'


        class CnpdAllStatsEntry(object):
            """
            An entry in the cnpdAllStatsTable table. This entry 
            contains the statistics collected on all the protocols 
            which NBAR classifies for a particular interface.
            
            .. attribute:: cnpdallstatsprotocolsindex
            
            	An object which represents a unique  identifier for a protocol or application  which NBAR currently recognizes.  This object is an index into the  SupportedProtocolsTable where details of the protocol can be found
            	**type**\: int
            
            	**range:** 1..1024
            
            .. attribute:: ifindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cnpdallstatshcinbytes
            
            	The byte count of inbound octets as  determined by Protocol Discovery. This is the 64\-bit (High Capacity) version of cnpdAllStatsInBytes
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cnpdallstatshcinpkts
            
            	The packet count of inbound packets as  determined by Protocol Discovery. This is the 64\-bit (High Capacity) version of cnpdAllStatsInPkts
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cnpdallstatshcoutbytes
            
            	The byte count of outbound octets as  determined by Protocol Discovery. This is the 64\-bit (High Capacity) version of cnpdAllStatsOutBytes
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cnpdallstatshcoutpkts
            
            	The packet count of outbound packets as  determined by Protocol Discovery. This is the 64\-bit (High Capacity) version of cnpdAllStatsOutPkts
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cnpdallstatsinbitrate
            
            	The inbound bit rate as determined  by Protocol Discovery
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: cnpdallstatsinbytes
            
            	The byte count of inbound octets as  determined by Protocol Discovery
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cnpdallstatsinpkts
            
            	The packet count of inbound packets as  determined by Protocol Discovery
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cnpdallstatsoutbitrate
            
            	The outbound bit rate as determined  by Protocol Discovery
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: cnpdallstatsoutbytes
            
            	The byte count of outbound octets as determined by Protocol Discovery
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cnpdallstatsoutpkts
            
            	The packet count of outbound packets as  determined by Protocol Discovery
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cnpdallstatsprotocolname
            
            	Name of the application or protocol, a  unique textual string, assigned in the cnpdSupportedProtocolsTable
            	**type**\: str
            
            	**range:** 1..255
            
            

            """

            _prefix = 'cisco-nbar'
            _revision = '2002-08-16'

            def __init__(self):
                self.parent = None
                self.cnpdallstatsprotocolsindex = None
                self.ifindex = None
                self.cnpdallstatshcinbytes = None
                self.cnpdallstatshcinpkts = None
                self.cnpdallstatshcoutbytes = None
                self.cnpdallstatshcoutpkts = None
                self.cnpdallstatsinbitrate = None
                self.cnpdallstatsinbytes = None
                self.cnpdallstatsinpkts = None
                self.cnpdallstatsoutbitrate = None
                self.cnpdallstatsoutbytes = None
                self.cnpdallstatsoutpkts = None
                self.cnpdallstatsprotocolname = None

            @property
            def _common_path(self):
                if self.cnpdallstatsprotocolsindex is None:
                    raise YPYDataValidationError('Key property cnpdallstatsprotocolsindex is None')
                if self.ifindex is None:
                    raise YPYDataValidationError('Key property ifindex is None')

                return '/CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:CISCO-NBAR-PROTOCOL-DISCOVERY-MIB/CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:cnpdAllStatsTable/CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:cnpdAllStatsEntry[CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:cnpdAllStatsProtocolsIndex = ' + str(self.cnpdallstatsprotocolsindex) + '][CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cnpdallstatsprotocolsindex is not None:
                    return True

                if self.ifindex is not None:
                    return True

                if self.cnpdallstatshcinbytes is not None:
                    return True

                if self.cnpdallstatshcinpkts is not None:
                    return True

                if self.cnpdallstatshcoutbytes is not None:
                    return True

                if self.cnpdallstatshcoutpkts is not None:
                    return True

                if self.cnpdallstatsinbitrate is not None:
                    return True

                if self.cnpdallstatsinbytes is not None:
                    return True

                if self.cnpdallstatsinpkts is not None:
                    return True

                if self.cnpdallstatsoutbitrate is not None:
                    return True

                if self.cnpdallstatsoutbytes is not None:
                    return True

                if self.cnpdallstatsoutpkts is not None:
                    return True

                if self.cnpdallstatsprotocolname is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.nbar._meta import _CISCO_NBAR_PROTOCOL_DISCOVERY_MIB as meta
                return meta._meta_table['CISCONBARPROTOCOLDISCOVERYMIB.CnpdAllStatsTable.CnpdAllStatsEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:CISCO-NBAR-PROTOCOL-DISCOVERY-MIB/CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:cnpdAllStatsTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cnpdallstatsentry is not None:
                for child_ref in self.cnpdallstatsentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.nbar._meta import _CISCO_NBAR_PROTOCOL_DISCOVERY_MIB as meta
            return meta._meta_table['CISCONBARPROTOCOLDISCOVERYMIB.CnpdAllStatsTable']['meta_info']


    class CnpdNotificationsConfig(object):
        """
        
        
        .. attribute:: cnpdnotificationsenable
        
        	This object is used to enable or disable  Notifications on a global basis.   If set to 'true' \- Notifications are enabled. If set to 'false' \- Notifications are disabled
        	**type**\: bool
        
        

        """

        _prefix = 'cisco-nbar'
        _revision = '2002-08-16'

        def __init__(self):
            self.parent = None
            self.cnpdnotificationsenable = None

        @property
        def _common_path(self):

            return '/CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:CISCO-NBAR-PROTOCOL-DISCOVERY-MIB/CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:cnpdNotificationsConfig'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cnpdnotificationsenable is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.nbar._meta import _CISCO_NBAR_PROTOCOL_DISCOVERY_MIB as meta
            return meta._meta_table['CISCONBARPROTOCOLDISCOVERYMIB.CnpdNotificationsConfig']['meta_info']


    class CnpdStatusTable(object):
        """
        The cnpdStatusTable is used to enable and
        disable Protocol Discovery on an interface.
        
        .. attribute:: cnpdstatusentry
        
        	An entry in the cnpdStatusTable contains objects for enabling or disabling Protocol Discovery on a per interface basis
        	**type**\: list of :py:class:`CnpdStatusEntry <ydk.models.nbar.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB.CISCONBARPROTOCOLDISCOVERYMIB.CnpdStatusTable.CnpdStatusEntry>`
        
        

        """

        _prefix = 'cisco-nbar'
        _revision = '2002-08-16'

        def __init__(self):
            self.parent = None
            self.cnpdstatusentry = YList()
            self.cnpdstatusentry.parent = self
            self.cnpdstatusentry.name = 'cnpdstatusentry'


        class CnpdStatusEntry(object):
            """
            An entry in the cnpdStatusTable contains objects
            for enabling or disabling Protocol Discovery on a
            per interface basis.
            
            .. attribute:: ifindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cnpdstatuslastupdatetime
            
            	The value of sysUpTime at the time Protocol  Discovery was last enabled  on an interface. If the interface does not have Protocol Discovery enabled this value is zero
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cnpdstatuspdenable
            
            	This object is used to enable or disable  Protocol Discovery on an interface.   If set to 'true' \- Protocol Discovery is  enabled on this Interface.  If set to 'false' \- Protocol Discovery is  disabled on this Interface
            	**type**\: bool
            
            

            """

            _prefix = 'cisco-nbar'
            _revision = '2002-08-16'

            def __init__(self):
                self.parent = None
                self.ifindex = None
                self.cnpdstatuslastupdatetime = None
                self.cnpdstatuspdenable = None

            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYDataValidationError('Key property ifindex is None')

                return '/CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:CISCO-NBAR-PROTOCOL-DISCOVERY-MIB/CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:cnpdStatusTable/CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:cnpdStatusEntry[CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:ifIndex = ' + str(self.ifindex) + ']'

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

                if self.cnpdstatuslastupdatetime is not None:
                    return True

                if self.cnpdstatuspdenable is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.nbar._meta import _CISCO_NBAR_PROTOCOL_DISCOVERY_MIB as meta
                return meta._meta_table['CISCONBARPROTOCOLDISCOVERYMIB.CnpdStatusTable.CnpdStatusEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:CISCO-NBAR-PROTOCOL-DISCOVERY-MIB/CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:cnpdStatusTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cnpdstatusentry is not None:
                for child_ref in self.cnpdstatusentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.nbar._meta import _CISCO_NBAR_PROTOCOL_DISCOVERY_MIB as meta
            return meta._meta_table['CISCONBARPROTOCOLDISCOVERYMIB.CnpdStatusTable']['meta_info']


    class CnpdSupportedProtocolsTable(object):
        """
        The Supported Protocols table lists all the 
        protocols and applications which NBAR is currently
        capable of recognizing.
        
        .. attribute:: cnpdsupportedprotocolsentry
        
        	A entry in the Supported Protocols table reflecting key information about a protocol
        	**type**\: list of :py:class:`CnpdSupportedProtocolsEntry <ydk.models.nbar.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB.CISCONBARPROTOCOLDISCOVERYMIB.CnpdSupportedProtocolsTable.CnpdSupportedProtocolsEntry>`
        
        

        """

        _prefix = 'cisco-nbar'
        _revision = '2002-08-16'

        def __init__(self):
            self.parent = None
            self.cnpdsupportedprotocolsentry = YList()
            self.cnpdsupportedprotocolsentry.parent = self
            self.cnpdsupportedprotocolsentry.name = 'cnpdsupportedprotocolsentry'


        class CnpdSupportedProtocolsEntry(object):
            """
            A entry in the Supported Protocols table reflecting
            key information about a protocol.
            
            .. attribute:: cnpdsupportedprotocolsindex
            
            	A unique identifier of a row in this table.  Thus it also represents a unique identifier for a protocol or application which NBAR currently recognizes
            	**type**\: int
            
            	**range:** 1..1024
            
            .. attribute:: cnpdsupportedprotocolsname
            
            	This object reflects the valid string of a protocol or application which NBAR currently recognizes
            	**type**\: str
            
            	**range:** 1..255
            
            

            """

            _prefix = 'cisco-nbar'
            _revision = '2002-08-16'

            def __init__(self):
                self.parent = None
                self.cnpdsupportedprotocolsindex = None
                self.cnpdsupportedprotocolsname = None

            @property
            def _common_path(self):
                if self.cnpdsupportedprotocolsindex is None:
                    raise YPYDataValidationError('Key property cnpdsupportedprotocolsindex is None')

                return '/CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:CISCO-NBAR-PROTOCOL-DISCOVERY-MIB/CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:cnpdSupportedProtocolsTable/CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:cnpdSupportedProtocolsEntry[CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:cnpdSupportedProtocolsIndex = ' + str(self.cnpdsupportedprotocolsindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cnpdsupportedprotocolsindex is not None:
                    return True

                if self.cnpdsupportedprotocolsname is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.nbar._meta import _CISCO_NBAR_PROTOCOL_DISCOVERY_MIB as meta
                return meta._meta_table['CISCONBARPROTOCOLDISCOVERYMIB.CnpdSupportedProtocolsTable.CnpdSupportedProtocolsEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:CISCO-NBAR-PROTOCOL-DISCOVERY-MIB/CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:cnpdSupportedProtocolsTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cnpdsupportedprotocolsentry is not None:
                for child_ref in self.cnpdsupportedprotocolsentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.nbar._meta import _CISCO_NBAR_PROTOCOL_DISCOVERY_MIB as meta
            return meta._meta_table['CISCONBARPROTOCOLDISCOVERYMIB.CnpdSupportedProtocolsTable']['meta_info']


    class CnpdThresholdConfigTable(object):
        """
        The cnpdThresholdConfigTable allows the management
        station to create thresholds for the purpose of
        sending notifications if breached, and creating a
        history of breached thresholds.
        
        .. attribute:: cnpdthresholdconfigentry
        
        	This entry contains configuration information to  set thresholds for the purpose of notifications.  The management station is allowed to set thresholds on individual statistics for individual protocols on an interface. If the threshold is breached by the protocol statistic, a new event is written to the cnpdThresholdHistoryTable, which in turn will  generate a Notification Event.  This function has a hysteresis mechanism to limit the generation of events. This mechanism generates one event as a threshold is crossed in the appropriate direction. No more events are generated for that threshold until the opposite threshold is crossed. This stops repeated Notification events being generated each time the value is sampled, when the value is above the threshold. Instead one notification is sent when the threshold is breached and one notification when the statistic drops below the threshold value again
        	**type**\: list of :py:class:`CnpdThresholdConfigEntry <ydk.models.nbar.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB.CISCONBARPROTOCOLDISCOVERYMIB.CnpdThresholdConfigTable.CnpdThresholdConfigEntry>`
        
        

        """

        _prefix = 'cisco-nbar'
        _revision = '2002-08-16'

        def __init__(self):
            self.parent = None
            self.cnpdthresholdconfigentry = YList()
            self.cnpdthresholdconfigentry.parent = self
            self.cnpdthresholdconfigentry.name = 'cnpdthresholdconfigentry'


        class CnpdThresholdConfigEntry(object):
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
            
            .. attribute:: cnpdthresholdconfigindex
            
            	A monotonically increasing integer which  uniquely identifies an entry in the  cnpdThresholdConfigTable
            	**type**\: int
            
            	**range:** 1..100
            
            .. attribute:: cnpdthresholdconfigfalling
            
            	This is the threshold object which the management  station sets to determine if it gets breached. It  indicates the statistic being sampled was falling.   When current sample is less than or equal  to this object, and the value at the last sampling interval was greater than this object (in other  words the value is falling), an entry in the  cnpdThresholdHistoryTable will be created.  		 After a falling event is generated, another  such event will not be generated until the sampled  value rises above this object and reaches the cnpdThresholdConfigRising value
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: cnpdthresholdconfigifindex
            
            	This object allows the management station to  select the interface, which Protocol Discovery is  running on, to be used to create this  cnpdThresholdConfigTable entry
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cnpdthresholdconfiginterval
            
            	The interval in seconds over which the data is sampled and compared with cnpdThresholdConfigRising and cnpdThresholdConfigFalling thresholds
            	**type**\: int
            
            	**range:** 1..2048
            
            .. attribute:: cnpdthresholdconfigprotocol
            
            	The application or protocol which the management station wishes to configure a threshold on.  This object is an index into the  SupportedProtocolsTable where details of the protocol can be found.  If cnpdThresholdConfigProtocolAny is set to TRUE this value will be ignored. If it is set to FALSE, then cnpdThresholdConfigProtocol will be the only protocol that is checked to see if it has breached the threshold
            	**type**\: int
            
            	**range:** 1..1024
            
            .. attribute:: cnpdthresholdconfigprotocolany
            
            	If set to 'true' \- this threshold is configured to check for any protocol which meets the threshold criteria. This means that multiple protocols can generate ThresholdHistoryTable entries. Each protocol is subject to the hysterisis mechanism.  If set to 'false' \- this threshold is configured to check for the protocol which meets the threshold criteria referred to by cnpdThresholdConfigProtocol
            	**type**\: bool
            
            .. attribute:: cnpdthresholdconfigrising
            
            	This is the threshold object which the managment station sets to determine if it gets breached. It  indicates the statistic being sampled was rising.  When the current sample is greater than or  equal to this object, and the value at the last  sampling interval was less than this object (in  other words the value is rising), an entry in the  cnpdThresholdHistoryTable will be created.  After a rising event is generated, another such  event will not be generated until the sampled value falls below this threshold and reaches the cnpdThresholdConfigFalling value.  This ensures that samples which are taken after a cnpdThresholdConfigRising threshold event has been created, do not create further thresholds and therefore notifications, until the  cnpdThresholdConfigFalling threshold has been met.  Thus a very short cnpdThresholdConfigInterval can be chosen without risk of multiple notifications for the same threshold breach condition
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: cnpdthresholdconfigsampletype
            
            	The method of sampling the selected statistic and calculating the value to be compared against  cnpdThresholdConfigRising or  cnpdThresholdConfigFalling thresholds.  		 If the value of this object is absoluteValue(1),  the value at the end of the sampling interval  cnpdThresholdConfigInterval, will be compared  with the cnpdThresholdConfigRising and  cnpdThresholdConfigFalling thresholds.   In this mode, when cnpdThresholdConfigStatsSelect is byte or packet based, a maximum of two  cnpdThresholdHistory entries will be created per application, as these byte and packet counts  monotonically increase from zero. 		 If the value of this object is deltaValue(2),  the difference between the samples at the  beginning and end of the cnpdThresholdConfigInterval  will be compared with the cnpdThresholdConfigRising  and cnpdThresholdConfigFalling thresholds. 		 Because the difference in the previous and current samples are compared over the sample period cnpdThresholdConfigInterval, this mode provides  more granularity to the thresholds because the NMS  is now provided with the gradient or change in the  cnpdThresholdConfigStatsSelect.  Note that even though the sample value is monotonically increasing for byte and packet counts,  cnpdThresholdConfigSampleType set to deltaValue, can  generate falling cnpdThresholdHistory entries, because the gradient can be lower than the  cnpdThresholdConfigFalling value
            	**type**\: :py:class:`CnpdThresholdConfigSampleType_Enum <ydk.models.nbar.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB.CISCONBARPROTOCOLDISCOVERYMIB.CnpdThresholdConfigTable.CnpdThresholdConfigEntry.CnpdThresholdConfigSampleType_Enum>`
            
            .. attribute:: cnpdthresholdconfigstartup
            
            	This controls the type of notification that is  sent when this threshold entry is first enabled.   Because there is no previous sampling history, choosing one of these options determines the type of notification generated \- Rising or Falling.  If the first sample after this entry is enabled  is greater than or equal to cnpdThresholdConfigRising and this object is equal to rising(1) or risingOrFalling(3),  then a single rising notification will be generated.   If the first sample after this entry is enabled is less than or equal to cnpdThresholdConfigFalling and this object is equal to falling(2) or  risingOrFalling(3), then a single falling notification  will be generated
            	**type**\: :py:class:`CnpdThresholdConfigStartup_Enum <ydk.models.nbar.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB.CISCONBARPROTOCOLDISCOVERYMIB.CnpdThresholdConfigTable.CnpdThresholdConfigEntry.CnpdThresholdConfigStartup_Enum>`
            
            .. attribute:: cnpdthresholdconfigstatsselect
            
            	This object allows the management station to select the statistic used to base the threshold on.  For example a cnpdThresholdConfigStatsSelect of bitRateSum means cnpdThresholdConfigRising and cnpdThresholdConfigFalling are values based on the combined value of in and out bitrates
            	**type**\: :py:class:`CiscoPdDataType_Enum <ydk.models.nbar.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB.CiscoPdDataType_Enum>`
            
            .. attribute:: cnpdthresholdconfigstatus
            
            	This object is used to create or delete  the row entry in cnpdThresholdConfigTable.   When creating a row entry the management station  is required to specify a value for  cnpdThresholdConfigIfIndex, cnpdThresholdConfigRising  and cnpdThresholdConfigFalling.  'active' means that a createAndGo or active has  been issued, AND a valid ifIndex exists. And therefore  if a row is 'active' it means a ThresholdHistory entry  may have been generated if the value was breached.  If you set an 'active' row to 'createAndWait' \- it will  in fact get the status 'notReady'.   Likewise if you set any row to 'notInService' or 'notReady'  it will go to the 'notReady' state
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            

            """

            _prefix = 'cisco-nbar'
            _revision = '2002-08-16'

            def __init__(self):
                self.parent = None
                self.cnpdthresholdconfigindex = None
                self.cnpdthresholdconfigfalling = None
                self.cnpdthresholdconfigifindex = None
                self.cnpdthresholdconfiginterval = None
                self.cnpdthresholdconfigprotocol = None
                self.cnpdthresholdconfigprotocolany = None
                self.cnpdthresholdconfigrising = None
                self.cnpdthresholdconfigsampletype = None
                self.cnpdthresholdconfigstartup = None
                self.cnpdthresholdconfigstatsselect = None
                self.cnpdthresholdconfigstatus = None

            class CnpdThresholdConfigSampleType_Enum(Enum):
                """
                CnpdThresholdConfigSampleType_Enum

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

                """

                ABSOLUTEVALUE = 1

                DELTAVALUE = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.nbar._meta import _CISCO_NBAR_PROTOCOL_DISCOVERY_MIB as meta
                    return meta._meta_table['CISCONBARPROTOCOLDISCOVERYMIB.CnpdThresholdConfigTable.CnpdThresholdConfigEntry.CnpdThresholdConfigSampleType_Enum']


            class CnpdThresholdConfigStartup_Enum(Enum):
                """
                CnpdThresholdConfigStartup_Enum

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

                """

                RISING = 1

                FALLING = 2

                RISINGORFALLING = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.nbar._meta import _CISCO_NBAR_PROTOCOL_DISCOVERY_MIB as meta
                    return meta._meta_table['CISCONBARPROTOCOLDISCOVERYMIB.CnpdThresholdConfigTable.CnpdThresholdConfigEntry.CnpdThresholdConfigStartup_Enum']


            @property
            def _common_path(self):
                if self.cnpdthresholdconfigindex is None:
                    raise YPYDataValidationError('Key property cnpdthresholdconfigindex is None')

                return '/CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:CISCO-NBAR-PROTOCOL-DISCOVERY-MIB/CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:cnpdThresholdConfigTable/CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:cnpdThresholdConfigEntry[CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:cnpdThresholdConfigIndex = ' + str(self.cnpdthresholdconfigindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cnpdthresholdconfigindex is not None:
                    return True

                if self.cnpdthresholdconfigfalling is not None:
                    return True

                if self.cnpdthresholdconfigifindex is not None:
                    return True

                if self.cnpdthresholdconfiginterval is not None:
                    return True

                if self.cnpdthresholdconfigprotocol is not None:
                    return True

                if self.cnpdthresholdconfigprotocolany is not None:
                    return True

                if self.cnpdthresholdconfigrising is not None:
                    return True

                if self.cnpdthresholdconfigsampletype is not None:
                    return True

                if self.cnpdthresholdconfigstartup is not None:
                    return True

                if self.cnpdthresholdconfigstatsselect is not None:
                    return True

                if self.cnpdthresholdconfigstatus is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.nbar._meta import _CISCO_NBAR_PROTOCOL_DISCOVERY_MIB as meta
                return meta._meta_table['CISCONBARPROTOCOLDISCOVERYMIB.CnpdThresholdConfigTable.CnpdThresholdConfigEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:CISCO-NBAR-PROTOCOL-DISCOVERY-MIB/CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:cnpdThresholdConfigTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cnpdthresholdconfigentry is not None:
                for child_ref in self.cnpdthresholdconfigentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.nbar._meta import _CISCO_NBAR_PROTOCOL_DISCOVERY_MIB as meta
            return meta._meta_table['CISCONBARPROTOCOLDISCOVERYMIB.CnpdThresholdConfigTable']['meta_info']


    class CnpdThresholdHistoryTable(object):
        """
        The Threshold History table. Notifications
        are unreliable so this table provides a
        history of the last 5000 threshold breached
        events. A notification can be traced back to
        its cnpdThresholdHistoryEntry.
        
        .. attribute:: cnpdthresholdhistoryentry
        
        	This entry is created each time a threshold  is breached.   Thus there is not necessarily a one to one  relationship to cnpdThresholdConfigTable  as not every Threshold configured will  be breached
        	**type**\: list of :py:class:`CnpdThresholdHistoryEntry <ydk.models.nbar.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB.CISCONBARPROTOCOLDISCOVERYMIB.CnpdThresholdHistoryTable.CnpdThresholdHistoryEntry>`
        
        

        """

        _prefix = 'cisco-nbar'
        _revision = '2002-08-16'

        def __init__(self):
            self.parent = None
            self.cnpdthresholdhistoryentry = YList()
            self.cnpdthresholdhistoryentry.parent = self
            self.cnpdthresholdhistoryentry.name = 'cnpdthresholdhistoryentry'


        class CnpdThresholdHistoryEntry(object):
            """
            This entry is created each time a threshold 
            is breached. 
            
            Thus there is not necessarily a one to one 
            relationship to cnpdThresholdConfigTable 
            as not every Threshold configured will 
            be breached.
            
            .. attribute:: cnpdthresholdhistoryindex
            
            	A monotonically increasing integer which uniquely identifies this  cnpdThresholdHistoryEntry in the  cnpdThresholdHistory table
            	**type**\: int
            
            	**range:** 1..1000
            
            .. attribute:: cnpdthresholdhistoryconfigindex
            
            	The cnpdThresholdConfigTable entry  which generated this entry. Using this  object the management station can backtrack  to the appropriate cnpdThresholdConfigEntry
            	**type**\: int
            
            	**range:** 1..1000
            
            .. attribute:: cnpdthresholdhistoryprotocol
            
            	The application or protocol which the management station configured a threshold on.  This object is an index into the  SupportedProtocolsTable where details of the protocol can be found
            	**type**\: int
            
            	**range:** 1..1024
            
            .. attribute:: cnpdthresholdhistorystatsselect
            
            	This is the statistic used to base the threshold on
            	**type**\: :py:class:`CiscoPdDataType_Enum <ydk.models.nbar.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB.CiscoPdDataType_Enum>`
            
            .. attribute:: cnpdthresholdhistorytime
            
            	The value of sysUpTime of the running  configuration when the event occurred
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cnpdthresholdhistorytype
            
            	Describes whether this is an event caused by a rising or falling threshold breach
            	**type**\: :py:class:`CnpdThresholdHistoryType_Enum <ydk.models.nbar.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB.CISCONBARPROTOCOLDISCOVERYMIB.CnpdThresholdHistoryTable.CnpdThresholdHistoryEntry.CnpdThresholdHistoryType_Enum>`
            
            .. attribute:: cnpdthresholdhistoryvalue
            
            	The actual value of the statistic when  the sampling was made
            	**type**\: int
            
            	**range:** 1..4294967295
            
            

            """

            _prefix = 'cisco-nbar'
            _revision = '2002-08-16'

            def __init__(self):
                self.parent = None
                self.cnpdthresholdhistoryindex = None
                self.cnpdthresholdhistoryconfigindex = None
                self.cnpdthresholdhistoryprotocol = None
                self.cnpdthresholdhistorystatsselect = None
                self.cnpdthresholdhistorytime = None
                self.cnpdthresholdhistorytype = None
                self.cnpdthresholdhistoryvalue = None

            class CnpdThresholdHistoryType_Enum(Enum):
                """
                CnpdThresholdHistoryType_Enum

                Describes whether this is an
                event caused by a rising
                or falling threshold breach.

                """

                RISINGBREACH = 1

                FALLINGBREACH = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.nbar._meta import _CISCO_NBAR_PROTOCOL_DISCOVERY_MIB as meta
                    return meta._meta_table['CISCONBARPROTOCOLDISCOVERYMIB.CnpdThresholdHistoryTable.CnpdThresholdHistoryEntry.CnpdThresholdHistoryType_Enum']


            @property
            def _common_path(self):
                if self.cnpdthresholdhistoryindex is None:
                    raise YPYDataValidationError('Key property cnpdthresholdhistoryindex is None')

                return '/CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:CISCO-NBAR-PROTOCOL-DISCOVERY-MIB/CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:cnpdThresholdHistoryTable/CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:cnpdThresholdHistoryEntry[CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:cnpdThresholdHistoryIndex = ' + str(self.cnpdthresholdhistoryindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cnpdthresholdhistoryindex is not None:
                    return True

                if self.cnpdthresholdhistoryconfigindex is not None:
                    return True

                if self.cnpdthresholdhistoryprotocol is not None:
                    return True

                if self.cnpdthresholdhistorystatsselect is not None:
                    return True

                if self.cnpdthresholdhistorytime is not None:
                    return True

                if self.cnpdthresholdhistorytype is not None:
                    return True

                if self.cnpdthresholdhistoryvalue is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.nbar._meta import _CISCO_NBAR_PROTOCOL_DISCOVERY_MIB as meta
                return meta._meta_table['CISCONBARPROTOCOLDISCOVERYMIB.CnpdThresholdHistoryTable.CnpdThresholdHistoryEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:CISCO-NBAR-PROTOCOL-DISCOVERY-MIB/CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:cnpdThresholdHistoryTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cnpdthresholdhistoryentry is not None:
                for child_ref in self.cnpdthresholdhistoryentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.nbar._meta import _CISCO_NBAR_PROTOCOL_DISCOVERY_MIB as meta
            return meta._meta_table['CISCONBARPROTOCOLDISCOVERYMIB.CnpdThresholdHistoryTable']['meta_info']


    class CnpdTopNConfigTable(object):
        """
        The cnpdTopNConfigTable is used to configure
        cnpdTopNStatsTable's.
        
        .. attribute:: cnpdtopnconfigentry
        
        	This entry provides the objects to configure and thus initiate the generation of a cnpdTopNStatsTable.
        	**type**\: list of :py:class:`CnpdTopNConfigEntry <ydk.models.nbar.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB.CISCONBARPROTOCOLDISCOVERYMIB.CnpdTopNConfigTable.CnpdTopNConfigEntry>`
        
        

        """

        _prefix = 'cisco-nbar'
        _revision = '2002-08-16'

        def __init__(self):
            self.parent = None
            self.cnpdtopnconfigentry = YList()
            self.cnpdtopnconfigentry.parent = self
            self.cnpdtopnconfigentry.name = 'cnpdtopnconfigentry'


        class CnpdTopNConfigEntry(object):
            """
            This entry provides the objects to configure and thus
            initiate the generation of a cnpdTopNStatsTable..
            
            .. attribute:: cnpdtopnconfigindex
            
            	A monotonically increasing integer which uniquely identifies a cnpdTopNConfigEntry  in the cnpdTopNConfigTable
            	**type**\: int
            
            	**range:** 1..50
            
            .. attribute:: cnpdtopnconfiggrantedsize
            
            	The actual size of the associated 	 cnpdTopNStatsTable entry.  The reason this may differ from  cnpdTopNConfigRequestedSize is because a  management station may request a number of  protocols that is greater than the number of  protocols actually found by Protocol Discovery
            	**type**\: int
            
            	**range:** 1..500
            
            .. attribute:: cnpdtopnconfigifindex
            
            	This object allows the management station to select the interface, which Protocol Discovery is running on, to be used to create this  cnpdTopNConfigEntry
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cnpdtopnconfigrequestedsize
            
            	The requested size of the associated  cnpdTopNStatsTable entry.  For example a cnpdTopNConfigRequestedSize of 20 indicates the management station wants to create an associated  cnpdTopNStatsTable  entry of 20 protocol/application's
            	**type**\: int
            
            	**range:** 1..500
            
            .. attribute:: cnpdtopnconfigsampletime
            
            	If the cnpdTopNConfigStatsSelect is bitRateIn, bitRateOut or bitRateSum, then this value is the interval in seconds that  the bitrate is sampled.  This has no effect if the cnpdTopNConfigStatsSelect is byte or packet based.  When this object is modified by the management  station, a new sample period is started regardless of whether the original cnpdTopNConfigSampleTime was finished
            	**type**\: int
            
            	**range:** 1..2048
            
            .. attribute:: cnpdtopnconfigstatsselect
            
            	This object allows the management station to select the statistic used to base the order of the top\-n table on.  For example\: a cnpdTopNConfigStatsSelect of bitRateSum means order this table based on each applications/protocols combined in and out bitrate
            	**type**\: :py:class:`CiscoPdDataType_Enum <ydk.models.nbar.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB.CiscoPdDataType_Enum>`
            
            .. attribute:: cnpdtopnconfigstatus
            
            	This object is used to create or delete  the row entry in cnpdTopNConfigTable.  When creating a row entry the management station is required to specify a value for cnpdTopNConfigIfIndex only.  'notReady' means that a row exists but  either it has no valid IfIndex or it has  not been set to createAndGo or active.  'active' means that a createAndGo or active  has been issued, AND a valid ifIndex exists.  Therefore if a row is 'active' it means a  TopNStats entry has been generated.  If you set an 'active' row to createAndWait  it will get the status 'notReady'.   If you set any row to 'notReady' \- it will go  to the 'notReadystate'.  If you set any row to 'notInService' \- it will  go to the 'notInService' state and the corresponding  TopNStatsEntry will be deleted.  The same TopNConfig entry can be re\-used without  changes by setting it to 'active'. The corresponding  TopStatsTable entry will be regenerated. This can  be used by the NMS to poll a particular TopNConfig  Entry.  Changes to an existing TopNConfig entry can be made by setting the status to 'createAndWait' and changing the necessary objects. Setting it to 'createAndGo' or 'active' will cause the corresponding TopNStats entry to be regenerated
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            .. attribute:: cnpdtopnconfigtime
            
            	The value of sysUpTime when the associated cnpdTopNStatsTable entry was created
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-nbar'
            _revision = '2002-08-16'

            def __init__(self):
                self.parent = None
                self.cnpdtopnconfigindex = None
                self.cnpdtopnconfiggrantedsize = None
                self.cnpdtopnconfigifindex = None
                self.cnpdtopnconfigrequestedsize = None
                self.cnpdtopnconfigsampletime = None
                self.cnpdtopnconfigstatsselect = None
                self.cnpdtopnconfigstatus = None
                self.cnpdtopnconfigtime = None

            @property
            def _common_path(self):
                if self.cnpdtopnconfigindex is None:
                    raise YPYDataValidationError('Key property cnpdtopnconfigindex is None')

                return '/CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:CISCO-NBAR-PROTOCOL-DISCOVERY-MIB/CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:cnpdTopNConfigTable/CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:cnpdTopNConfigEntry[CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:cnpdTopNConfigIndex = ' + str(self.cnpdtopnconfigindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cnpdtopnconfigindex is not None:
                    return True

                if self.cnpdtopnconfiggrantedsize is not None:
                    return True

                if self.cnpdtopnconfigifindex is not None:
                    return True

                if self.cnpdtopnconfigrequestedsize is not None:
                    return True

                if self.cnpdtopnconfigsampletime is not None:
                    return True

                if self.cnpdtopnconfigstatsselect is not None:
                    return True

                if self.cnpdtopnconfigstatus is not None:
                    return True

                if self.cnpdtopnconfigtime is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.nbar._meta import _CISCO_NBAR_PROTOCOL_DISCOVERY_MIB as meta
                return meta._meta_table['CISCONBARPROTOCOLDISCOVERYMIB.CnpdTopNConfigTable.CnpdTopNConfigEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:CISCO-NBAR-PROTOCOL-DISCOVERY-MIB/CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:cnpdTopNConfigTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cnpdtopnconfigentry is not None:
                for child_ref in self.cnpdtopnconfigentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.nbar._meta import _CISCO_NBAR_PROTOCOL_DISCOVERY_MIB as meta
            return meta._meta_table['CISCONBARPROTOCOLDISCOVERYMIB.CnpdTopNConfigTable']['meta_info']


    class CnpdTopNStatsTable(object):
        """
        A cnpdTopNStatsTable describes an ordered
        list of protocols.
        
        .. attribute:: cnpdtopnstatsentry
        
        	This entry is used to store a set of objects which  describe a cnpdTopNStatsTable. A cnpdTopNStatsTable  is a number of protocols and statistics sorted  according to the criteria in the associated cnpdTopNConfigEntry.  Therefore a cnpdTopNStatsTable can differ in content  and size according to what was configured in the associated cnpdTopNConfigTableEntry
        	**type**\: list of :py:class:`CnpdTopNStatsEntry <ydk.models.nbar.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB.CISCONBARPROTOCOLDISCOVERYMIB.CnpdTopNStatsTable.CnpdTopNStatsEntry>`
        
        

        """

        _prefix = 'cisco-nbar'
        _revision = '2002-08-16'

        def __init__(self):
            self.parent = None
            self.cnpdtopnstatsentry = YList()
            self.cnpdtopnstatsentry.parent = self
            self.cnpdtopnstatsentry.name = 'cnpdtopnstatsentry'


        class CnpdTopNStatsEntry(object):
            """
            This entry is used to store a set of objects which 
            describe a cnpdTopNStatsTable. A cnpdTopNStatsTable 
            is a number of protocols and statistics sorted 
            according to the criteria in the associated
            cnpdTopNConfigEntry.
            
            Therefore a cnpdTopNStatsTable can differ in content 
            and size according to what was configured in the associated
            cnpdTopNConfigTableEntry.
            
            .. attribute:: cnpdtopnconfigindex
            
            	
            	**type**\: int
            
            	**range:** 1..50
            
            .. attribute:: cnpdtopnstatsindex
            
            	A monotonically increasing integer which  uniquely identifies a cnpdTopNStatsEntry  in the cnpdTopNStatsTable
            	**type**\: int
            
            	**range:** 1..500
            
            .. attribute:: cnpdtopnstatshcrate
            
            	The amount of change in the selected statistic during this sampling interval. The selected statistic is the cnpdTopNConfigStatsSelect from the associated cnpdTopNConfigStatsEntry.	  This is the 64\-bit (High Capacity) version of  cnpdTopNStatsRate
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cnpdtopnstatsprotocolname
            
            	Name of the application or protocol,  a unique textual string, assigned in the cnpdSupportedProtocolsTable
            	**type**\: str
            
            	**range:** 1..255
            
            .. attribute:: cnpdtopnstatsrate
            
            	The amount of change in the selected statistic during this sampling interval. The selected statistic is the cnpdTopNConfigStatsSelect from the associated cnpdTopNConfigStatsEntry
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-nbar'
            _revision = '2002-08-16'

            def __init__(self):
                self.parent = None
                self.cnpdtopnconfigindex = None
                self.cnpdtopnstatsindex = None
                self.cnpdtopnstatshcrate = None
                self.cnpdtopnstatsprotocolname = None
                self.cnpdtopnstatsrate = None

            @property
            def _common_path(self):
                if self.cnpdtopnconfigindex is None:
                    raise YPYDataValidationError('Key property cnpdtopnconfigindex is None')
                if self.cnpdtopnstatsindex is None:
                    raise YPYDataValidationError('Key property cnpdtopnstatsindex is None')

                return '/CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:CISCO-NBAR-PROTOCOL-DISCOVERY-MIB/CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:cnpdTopNStatsTable/CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:cnpdTopNStatsEntry[CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:cnpdTopNConfigIndex = ' + str(self.cnpdtopnconfigindex) + '][CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:cnpdTopNStatsIndex = ' + str(self.cnpdtopnstatsindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cnpdtopnconfigindex is not None:
                    return True

                if self.cnpdtopnstatsindex is not None:
                    return True

                if self.cnpdtopnstatshcrate is not None:
                    return True

                if self.cnpdtopnstatsprotocolname is not None:
                    return True

                if self.cnpdtopnstatsrate is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.nbar._meta import _CISCO_NBAR_PROTOCOL_DISCOVERY_MIB as meta
                return meta._meta_table['CISCONBARPROTOCOLDISCOVERYMIB.CnpdTopNStatsTable.CnpdTopNStatsEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:CISCO-NBAR-PROTOCOL-DISCOVERY-MIB/CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:cnpdTopNStatsTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cnpdtopnstatsentry is not None:
                for child_ref in self.cnpdtopnstatsentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.nbar._meta import _CISCO_NBAR_PROTOCOL_DISCOVERY_MIB as meta
            return meta._meta_table['CISCONBARPROTOCOLDISCOVERYMIB.CnpdTopNStatsTable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:CISCO-NBAR-PROTOCOL-DISCOVERY-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.cnpdallstatstable is not None and self.cnpdallstatstable._has_data():
            return True

        if self.cnpdallstatstable is not None and self.cnpdallstatstable.is_presence():
            return True

        if self.cnpdnotificationsconfig is not None and self.cnpdnotificationsconfig._has_data():
            return True

        if self.cnpdnotificationsconfig is not None and self.cnpdnotificationsconfig.is_presence():
            return True

        if self.cnpdstatustable is not None and self.cnpdstatustable._has_data():
            return True

        if self.cnpdstatustable is not None and self.cnpdstatustable.is_presence():
            return True

        if self.cnpdsupportedprotocolstable is not None and self.cnpdsupportedprotocolstable._has_data():
            return True

        if self.cnpdsupportedprotocolstable is not None and self.cnpdsupportedprotocolstable.is_presence():
            return True

        if self.cnpdthresholdconfigtable is not None and self.cnpdthresholdconfigtable._has_data():
            return True

        if self.cnpdthresholdconfigtable is not None and self.cnpdthresholdconfigtable.is_presence():
            return True

        if self.cnpdthresholdhistorytable is not None and self.cnpdthresholdhistorytable._has_data():
            return True

        if self.cnpdthresholdhistorytable is not None and self.cnpdthresholdhistorytable.is_presence():
            return True

        if self.cnpdtopnconfigtable is not None and self.cnpdtopnconfigtable._has_data():
            return True

        if self.cnpdtopnconfigtable is not None and self.cnpdtopnconfigtable.is_presence():
            return True

        if self.cnpdtopnstatstable is not None and self.cnpdtopnstatstable._has_data():
            return True

        if self.cnpdtopnstatstable is not None and self.cnpdtopnstatstable.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.nbar._meta import _CISCO_NBAR_PROTOCOL_DISCOVERY_MIB as meta
        return meta._meta_table['CISCONBARPROTOCOLDISCOVERYMIB']['meta_info']


