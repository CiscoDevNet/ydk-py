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
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Ciscopddatatype(Enum):
    """
    Ciscopddatatype

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



class CiscoNbarProtocolDiscoveryMib(Entity):
    """
    
    
    .. attribute:: cnpdallstatstable
    
    	The cnpdAllStatsTable contains all the statistics available for all the protocols/applications currently recognized by NBAR Protocol Discovery for a particular  interface.  In the event of an overflow, the 32 bit counters are not  valid. There is no overflow support
    	**type**\:   :py:class:`Cnpdallstatstable <ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB.CiscoNbarProtocolDiscoveryMib.Cnpdallstatstable>`
    
    .. attribute:: cnpdnotificationsconfig
    
    	
    	**type**\:   :py:class:`Cnpdnotificationsconfig <ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB.CiscoNbarProtocolDiscoveryMib.Cnpdnotificationsconfig>`
    
    .. attribute:: cnpdstatustable
    
    	The cnpdStatusTable is used to enable and disable Protocol Discovery on an interface
    	**type**\:   :py:class:`Cnpdstatustable <ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB.CiscoNbarProtocolDiscoveryMib.Cnpdstatustable>`
    
    .. attribute:: cnpdsupportedprotocolstable
    
    	The Supported Protocols table lists all the  protocols and applications which NBAR is currently capable of recognizing
    	**type**\:   :py:class:`Cnpdsupportedprotocolstable <ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB.CiscoNbarProtocolDiscoveryMib.Cnpdsupportedprotocolstable>`
    
    .. attribute:: cnpdthresholdconfigtable
    
    	The cnpdThresholdConfigTable allows the management station to create thresholds for the purpose of sending notifications if breached, and creating a history of breached thresholds
    	**type**\:   :py:class:`Cnpdthresholdconfigtable <ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB.CiscoNbarProtocolDiscoveryMib.Cnpdthresholdconfigtable>`
    
    .. attribute:: cnpdthresholdhistorytable
    
    	The Threshold History table. Notifications are unreliable so this table provides a history of the last 5000 threshold breached events. A notification can be traced back to its cnpdThresholdHistoryEntry
    	**type**\:   :py:class:`Cnpdthresholdhistorytable <ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB.CiscoNbarProtocolDiscoveryMib.Cnpdthresholdhistorytable>`
    
    .. attribute:: cnpdtopnconfigtable
    
    	The cnpdTopNConfigTable is used to configure cnpdTopNStatsTable's
    	**type**\:   :py:class:`Cnpdtopnconfigtable <ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB.CiscoNbarProtocolDiscoveryMib.Cnpdtopnconfigtable>`
    
    .. attribute:: cnpdtopnstatstable
    
    	A cnpdTopNStatsTable describes an ordered list of protocols
    	**type**\:   :py:class:`Cnpdtopnstatstable <ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB.CiscoNbarProtocolDiscoveryMib.Cnpdtopnstatstable>`
    
    

    """

    _prefix = 'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB'
    _revision = '2002-08-16'

    def __init__(self):
        super(CiscoNbarProtocolDiscoveryMib, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-NBAR-PROTOCOL-DISCOVERY-MIB"
        self.yang_parent_name = "CISCO-NBAR-PROTOCOL-DISCOVERY-MIB"

        self.cnpdallstatstable = CiscoNbarProtocolDiscoveryMib.Cnpdallstatstable()
        self.cnpdallstatstable.parent = self
        self._children_name_map["cnpdallstatstable"] = "cnpdAllStatsTable"
        self._children_yang_names.add("cnpdAllStatsTable")

        self.cnpdnotificationsconfig = CiscoNbarProtocolDiscoveryMib.Cnpdnotificationsconfig()
        self.cnpdnotificationsconfig.parent = self
        self._children_name_map["cnpdnotificationsconfig"] = "cnpdNotificationsConfig"
        self._children_yang_names.add("cnpdNotificationsConfig")

        self.cnpdstatustable = CiscoNbarProtocolDiscoveryMib.Cnpdstatustable()
        self.cnpdstatustable.parent = self
        self._children_name_map["cnpdstatustable"] = "cnpdStatusTable"
        self._children_yang_names.add("cnpdStatusTable")

        self.cnpdsupportedprotocolstable = CiscoNbarProtocolDiscoveryMib.Cnpdsupportedprotocolstable()
        self.cnpdsupportedprotocolstable.parent = self
        self._children_name_map["cnpdsupportedprotocolstable"] = "cnpdSupportedProtocolsTable"
        self._children_yang_names.add("cnpdSupportedProtocolsTable")

        self.cnpdthresholdconfigtable = CiscoNbarProtocolDiscoveryMib.Cnpdthresholdconfigtable()
        self.cnpdthresholdconfigtable.parent = self
        self._children_name_map["cnpdthresholdconfigtable"] = "cnpdThresholdConfigTable"
        self._children_yang_names.add("cnpdThresholdConfigTable")

        self.cnpdthresholdhistorytable = CiscoNbarProtocolDiscoveryMib.Cnpdthresholdhistorytable()
        self.cnpdthresholdhistorytable.parent = self
        self._children_name_map["cnpdthresholdhistorytable"] = "cnpdThresholdHistoryTable"
        self._children_yang_names.add("cnpdThresholdHistoryTable")

        self.cnpdtopnconfigtable = CiscoNbarProtocolDiscoveryMib.Cnpdtopnconfigtable()
        self.cnpdtopnconfigtable.parent = self
        self._children_name_map["cnpdtopnconfigtable"] = "cnpdTopNConfigTable"
        self._children_yang_names.add("cnpdTopNConfigTable")

        self.cnpdtopnstatstable = CiscoNbarProtocolDiscoveryMib.Cnpdtopnstatstable()
        self.cnpdtopnstatstable.parent = self
        self._children_name_map["cnpdtopnstatstable"] = "cnpdTopNStatsTable"
        self._children_yang_names.add("cnpdTopNStatsTable")


    class Cnpdnotificationsconfig(Entity):
        """
        
        
        .. attribute:: cnpdnotificationsenable
        
        	This object is used to enable or disable  Notifications on a global basis.   If set to 'true' \- Notifications are enabled. If set to 'false' \- Notifications are disabled
        	**type**\:  bool
        
        

        """

        _prefix = 'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB'
        _revision = '2002-08-16'

        def __init__(self):
            super(CiscoNbarProtocolDiscoveryMib.Cnpdnotificationsconfig, self).__init__()

            self.yang_name = "cnpdNotificationsConfig"
            self.yang_parent_name = "CISCO-NBAR-PROTOCOL-DISCOVERY-MIB"

            self.cnpdnotificationsenable = YLeaf(YType.boolean, "cnpdNotificationsEnable")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("cnpdnotificationsenable") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoNbarProtocolDiscoveryMib.Cnpdnotificationsconfig, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoNbarProtocolDiscoveryMib.Cnpdnotificationsconfig, self).__setattr__(name, value)

        def has_data(self):
            return self.cnpdnotificationsenable.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.cnpdnotificationsenable.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cnpdNotificationsConfig" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:CISCO-NBAR-PROTOCOL-DISCOVERY-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.cnpdnotificationsenable.is_set or self.cnpdnotificationsenable.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cnpdnotificationsenable.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cnpdNotificationsEnable"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "cnpdNotificationsEnable"):
                self.cnpdnotificationsenable = value
                self.cnpdnotificationsenable.value_namespace = name_space
                self.cnpdnotificationsenable.value_namespace_prefix = name_space_prefix


    class Cnpdstatustable(Entity):
        """
        The cnpdStatusTable is used to enable and
        disable Protocol Discovery on an interface.
        
        .. attribute:: cnpdstatusentry
        
        	An entry in the cnpdStatusTable contains objects for enabling or disabling Protocol Discovery on a per interface basis
        	**type**\: list of    :py:class:`Cnpdstatusentry <ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB.CiscoNbarProtocolDiscoveryMib.Cnpdstatustable.Cnpdstatusentry>`
        
        

        """

        _prefix = 'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB'
        _revision = '2002-08-16'

        def __init__(self):
            super(CiscoNbarProtocolDiscoveryMib.Cnpdstatustable, self).__init__()

            self.yang_name = "cnpdStatusTable"
            self.yang_parent_name = "CISCO-NBAR-PROTOCOL-DISCOVERY-MIB"

            self.cnpdstatusentry = YList(self)

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
                        super(CiscoNbarProtocolDiscoveryMib.Cnpdstatustable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoNbarProtocolDiscoveryMib.Cnpdstatustable, self).__setattr__(name, value)


        class Cnpdstatusentry(Entity):
            """
            An entry in the cnpdStatusTable contains objects
            for enabling or disabling Protocol Discovery on a
            per interface basis.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
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
                super(CiscoNbarProtocolDiscoveryMib.Cnpdstatustable.Cnpdstatusentry, self).__init__()

                self.yang_name = "cnpdStatusEntry"
                self.yang_parent_name = "cnpdStatusTable"

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.cnpdstatuslastupdatetime = YLeaf(YType.uint32, "cnpdStatusLastUpdateTime")

                self.cnpdstatuspdenable = YLeaf(YType.boolean, "cnpdStatusPdEnable")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ifindex",
                                "cnpdstatuslastupdatetime",
                                "cnpdstatuspdenable") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoNbarProtocolDiscoveryMib.Cnpdstatustable.Cnpdstatusentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoNbarProtocolDiscoveryMib.Cnpdstatustable.Cnpdstatusentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ifindex.is_set or
                    self.cnpdstatuslastupdatetime.is_set or
                    self.cnpdstatuspdenable.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.cnpdstatuslastupdatetime.yfilter != YFilter.not_set or
                    self.cnpdstatuspdenable.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cnpdStatusEntry" + "[ifIndex='" + self.ifindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:CISCO-NBAR-PROTOCOL-DISCOVERY-MIB/cnpdStatusTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.cnpdstatuslastupdatetime.is_set or self.cnpdstatuslastupdatetime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnpdstatuslastupdatetime.get_name_leafdata())
                if (self.cnpdstatuspdenable.is_set or self.cnpdstatuspdenable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnpdstatuspdenable.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ifIndex" or name == "cnpdStatusLastUpdateTime" or name == "cnpdStatusPdEnable"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ifIndex"):
                    self.ifindex = value
                    self.ifindex.value_namespace = name_space
                    self.ifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cnpdStatusLastUpdateTime"):
                    self.cnpdstatuslastupdatetime = value
                    self.cnpdstatuslastupdatetime.value_namespace = name_space
                    self.cnpdstatuslastupdatetime.value_namespace_prefix = name_space_prefix
                if(value_path == "cnpdStatusPdEnable"):
                    self.cnpdstatuspdenable = value
                    self.cnpdstatuspdenable.value_namespace = name_space
                    self.cnpdstatuspdenable.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cnpdstatusentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cnpdstatusentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cnpdStatusTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:CISCO-NBAR-PROTOCOL-DISCOVERY-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cnpdStatusEntry"):
                for c in self.cnpdstatusentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoNbarProtocolDiscoveryMib.Cnpdstatustable.Cnpdstatusentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cnpdstatusentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cnpdStatusEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
        	**type**\: list of    :py:class:`Cnpdallstatsentry <ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB.CiscoNbarProtocolDiscoveryMib.Cnpdallstatstable.Cnpdallstatsentry>`
        
        

        """

        _prefix = 'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB'
        _revision = '2002-08-16'

        def __init__(self):
            super(CiscoNbarProtocolDiscoveryMib.Cnpdallstatstable, self).__init__()

            self.yang_name = "cnpdAllStatsTable"
            self.yang_parent_name = "CISCO-NBAR-PROTOCOL-DISCOVERY-MIB"

            self.cnpdallstatsentry = YList(self)

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
                        super(CiscoNbarProtocolDiscoveryMib.Cnpdallstatstable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoNbarProtocolDiscoveryMib.Cnpdallstatstable, self).__setattr__(name, value)


        class Cnpdallstatsentry(Entity):
            """
            An entry in the cnpdAllStatsTable table. This entry 
            contains the statistics collected on all the protocols 
            which NBAR classifies for a particular interface.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
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
                super(CiscoNbarProtocolDiscoveryMib.Cnpdallstatstable.Cnpdallstatsentry, self).__init__()

                self.yang_name = "cnpdAllStatsEntry"
                self.yang_parent_name = "cnpdAllStatsTable"

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

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ifindex",
                                "cnpdallstatsprotocolsindex",
                                "cnpdallstatshcinbytes",
                                "cnpdallstatshcinpkts",
                                "cnpdallstatshcoutbytes",
                                "cnpdallstatshcoutpkts",
                                "cnpdallstatsinbitrate",
                                "cnpdallstatsinbytes",
                                "cnpdallstatsinpkts",
                                "cnpdallstatsoutbitrate",
                                "cnpdallstatsoutbytes",
                                "cnpdallstatsoutpkts",
                                "cnpdallstatsprotocolname") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoNbarProtocolDiscoveryMib.Cnpdallstatstable.Cnpdallstatsentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoNbarProtocolDiscoveryMib.Cnpdallstatstable.Cnpdallstatsentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ifindex.is_set or
                    self.cnpdallstatsprotocolsindex.is_set or
                    self.cnpdallstatshcinbytes.is_set or
                    self.cnpdallstatshcinpkts.is_set or
                    self.cnpdallstatshcoutbytes.is_set or
                    self.cnpdallstatshcoutpkts.is_set or
                    self.cnpdallstatsinbitrate.is_set or
                    self.cnpdallstatsinbytes.is_set or
                    self.cnpdallstatsinpkts.is_set or
                    self.cnpdallstatsoutbitrate.is_set or
                    self.cnpdallstatsoutbytes.is_set or
                    self.cnpdallstatsoutpkts.is_set or
                    self.cnpdallstatsprotocolname.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.cnpdallstatsprotocolsindex.yfilter != YFilter.not_set or
                    self.cnpdallstatshcinbytes.yfilter != YFilter.not_set or
                    self.cnpdallstatshcinpkts.yfilter != YFilter.not_set or
                    self.cnpdallstatshcoutbytes.yfilter != YFilter.not_set or
                    self.cnpdallstatshcoutpkts.yfilter != YFilter.not_set or
                    self.cnpdallstatsinbitrate.yfilter != YFilter.not_set or
                    self.cnpdallstatsinbytes.yfilter != YFilter.not_set or
                    self.cnpdallstatsinpkts.yfilter != YFilter.not_set or
                    self.cnpdallstatsoutbitrate.yfilter != YFilter.not_set or
                    self.cnpdallstatsoutbytes.yfilter != YFilter.not_set or
                    self.cnpdallstatsoutpkts.yfilter != YFilter.not_set or
                    self.cnpdallstatsprotocolname.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cnpdAllStatsEntry" + "[ifIndex='" + self.ifindex.get() + "']" + "[cnpdAllStatsProtocolsIndex='" + self.cnpdallstatsprotocolsindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:CISCO-NBAR-PROTOCOL-DISCOVERY-MIB/cnpdAllStatsTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.cnpdallstatsprotocolsindex.is_set or self.cnpdallstatsprotocolsindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnpdallstatsprotocolsindex.get_name_leafdata())
                if (self.cnpdallstatshcinbytes.is_set or self.cnpdallstatshcinbytes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnpdallstatshcinbytes.get_name_leafdata())
                if (self.cnpdallstatshcinpkts.is_set or self.cnpdallstatshcinpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnpdallstatshcinpkts.get_name_leafdata())
                if (self.cnpdallstatshcoutbytes.is_set or self.cnpdallstatshcoutbytes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnpdallstatshcoutbytes.get_name_leafdata())
                if (self.cnpdallstatshcoutpkts.is_set or self.cnpdallstatshcoutpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnpdallstatshcoutpkts.get_name_leafdata())
                if (self.cnpdallstatsinbitrate.is_set or self.cnpdallstatsinbitrate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnpdallstatsinbitrate.get_name_leafdata())
                if (self.cnpdallstatsinbytes.is_set or self.cnpdallstatsinbytes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnpdallstatsinbytes.get_name_leafdata())
                if (self.cnpdallstatsinpkts.is_set or self.cnpdallstatsinpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnpdallstatsinpkts.get_name_leafdata())
                if (self.cnpdallstatsoutbitrate.is_set or self.cnpdallstatsoutbitrate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnpdallstatsoutbitrate.get_name_leafdata())
                if (self.cnpdallstatsoutbytes.is_set or self.cnpdallstatsoutbytes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnpdallstatsoutbytes.get_name_leafdata())
                if (self.cnpdallstatsoutpkts.is_set or self.cnpdallstatsoutpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnpdallstatsoutpkts.get_name_leafdata())
                if (self.cnpdallstatsprotocolname.is_set or self.cnpdallstatsprotocolname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnpdallstatsprotocolname.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ifIndex" or name == "cnpdAllStatsProtocolsIndex" or name == "cnpdAllStatsHCInBytes" or name == "cnpdAllStatsHCInPkts" or name == "cnpdAllStatsHCOutBytes" or name == "cnpdAllStatsHCOutPkts" or name == "cnpdAllStatsInBitRate" or name == "cnpdAllStatsInBytes" or name == "cnpdAllStatsInPkts" or name == "cnpdAllStatsOutBitRate" or name == "cnpdAllStatsOutBytes" or name == "cnpdAllStatsOutPkts" or name == "cnpdAllStatsProtocolName"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ifIndex"):
                    self.ifindex = value
                    self.ifindex.value_namespace = name_space
                    self.ifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cnpdAllStatsProtocolsIndex"):
                    self.cnpdallstatsprotocolsindex = value
                    self.cnpdallstatsprotocolsindex.value_namespace = name_space
                    self.cnpdallstatsprotocolsindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cnpdAllStatsHCInBytes"):
                    self.cnpdallstatshcinbytes = value
                    self.cnpdallstatshcinbytes.value_namespace = name_space
                    self.cnpdallstatshcinbytes.value_namespace_prefix = name_space_prefix
                if(value_path == "cnpdAllStatsHCInPkts"):
                    self.cnpdallstatshcinpkts = value
                    self.cnpdallstatshcinpkts.value_namespace = name_space
                    self.cnpdallstatshcinpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "cnpdAllStatsHCOutBytes"):
                    self.cnpdallstatshcoutbytes = value
                    self.cnpdallstatshcoutbytes.value_namespace = name_space
                    self.cnpdallstatshcoutbytes.value_namespace_prefix = name_space_prefix
                if(value_path == "cnpdAllStatsHCOutPkts"):
                    self.cnpdallstatshcoutpkts = value
                    self.cnpdallstatshcoutpkts.value_namespace = name_space
                    self.cnpdallstatshcoutpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "cnpdAllStatsInBitRate"):
                    self.cnpdallstatsinbitrate = value
                    self.cnpdallstatsinbitrate.value_namespace = name_space
                    self.cnpdallstatsinbitrate.value_namespace_prefix = name_space_prefix
                if(value_path == "cnpdAllStatsInBytes"):
                    self.cnpdallstatsinbytes = value
                    self.cnpdallstatsinbytes.value_namespace = name_space
                    self.cnpdallstatsinbytes.value_namespace_prefix = name_space_prefix
                if(value_path == "cnpdAllStatsInPkts"):
                    self.cnpdallstatsinpkts = value
                    self.cnpdallstatsinpkts.value_namespace = name_space
                    self.cnpdallstatsinpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "cnpdAllStatsOutBitRate"):
                    self.cnpdallstatsoutbitrate = value
                    self.cnpdallstatsoutbitrate.value_namespace = name_space
                    self.cnpdallstatsoutbitrate.value_namespace_prefix = name_space_prefix
                if(value_path == "cnpdAllStatsOutBytes"):
                    self.cnpdallstatsoutbytes = value
                    self.cnpdallstatsoutbytes.value_namespace = name_space
                    self.cnpdallstatsoutbytes.value_namespace_prefix = name_space_prefix
                if(value_path == "cnpdAllStatsOutPkts"):
                    self.cnpdallstatsoutpkts = value
                    self.cnpdallstatsoutpkts.value_namespace = name_space
                    self.cnpdallstatsoutpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "cnpdAllStatsProtocolName"):
                    self.cnpdallstatsprotocolname = value
                    self.cnpdallstatsprotocolname.value_namespace = name_space
                    self.cnpdallstatsprotocolname.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cnpdallstatsentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cnpdallstatsentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cnpdAllStatsTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:CISCO-NBAR-PROTOCOL-DISCOVERY-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cnpdAllStatsEntry"):
                for c in self.cnpdallstatsentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoNbarProtocolDiscoveryMib.Cnpdallstatstable.Cnpdallstatsentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cnpdallstatsentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cnpdAllStatsEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cnpdtopnconfigtable(Entity):
        """
        The cnpdTopNConfigTable is used to configure
        cnpdTopNStatsTable's.
        
        .. attribute:: cnpdtopnconfigentry
        
        	This entry provides the objects to configure and thus initiate the generation of a cnpdTopNStatsTable.
        	**type**\: list of    :py:class:`Cnpdtopnconfigentry <ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB.CiscoNbarProtocolDiscoveryMib.Cnpdtopnconfigtable.Cnpdtopnconfigentry>`
        
        

        """

        _prefix = 'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB'
        _revision = '2002-08-16'

        def __init__(self):
            super(CiscoNbarProtocolDiscoveryMib.Cnpdtopnconfigtable, self).__init__()

            self.yang_name = "cnpdTopNConfigTable"
            self.yang_parent_name = "CISCO-NBAR-PROTOCOL-DISCOVERY-MIB"

            self.cnpdtopnconfigentry = YList(self)

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
                        super(CiscoNbarProtocolDiscoveryMib.Cnpdtopnconfigtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoNbarProtocolDiscoveryMib.Cnpdtopnconfigtable, self).__setattr__(name, value)


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
            	**type**\:   :py:class:`Ciscopddatatype <ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB.Ciscopddatatype>`
            
            .. attribute:: cnpdtopnconfigstatus
            
            	This object is used to create or delete  the row entry in cnpdTopNConfigTable.  When creating a row entry the management station is required to specify a value for cnpdTopNConfigIfIndex only.  'notReady' means that a row exists but  either it has no valid IfIndex or it has  not been set to createAndGo or active.  'active' means that a createAndGo or active  has been issued, AND a valid ifIndex exists.  Therefore if a row is 'active' it means a  TopNStats entry has been generated.  If you set an 'active' row to createAndWait  it will get the status 'notReady'.   If you set any row to 'notReady' \- it will go  to the 'notReadystate'.  If you set any row to 'notInService' \- it will  go to the 'notInService' state and the corresponding  TopNStatsEntry will be deleted.  The same TopNConfig entry can be re\-used without  changes by setting it to 'active'. The corresponding  TopStatsTable entry will be regenerated. This can  be used by the NMS to poll a particular TopNConfig  Entry.  Changes to an existing TopNConfig entry can be made by setting the status to 'createAndWait' and changing the necessary objects. Setting it to 'createAndGo' or 'active' will cause the corresponding TopNStats entry to be regenerated
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: cnpdtopnconfigtime
            
            	The value of sysUpTime when the associated cnpdTopNStatsTable entry was created
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB'
            _revision = '2002-08-16'

            def __init__(self):
                super(CiscoNbarProtocolDiscoveryMib.Cnpdtopnconfigtable.Cnpdtopnconfigentry, self).__init__()

                self.yang_name = "cnpdTopNConfigEntry"
                self.yang_parent_name = "cnpdTopNConfigTable"

                self.cnpdtopnconfigindex = YLeaf(YType.uint32, "cnpdTopNConfigIndex")

                self.cnpdtopnconfiggrantedsize = YLeaf(YType.uint32, "cnpdTopNConfigGrantedSize")

                self.cnpdtopnconfigifindex = YLeaf(YType.int32, "cnpdTopNConfigIfIndex")

                self.cnpdtopnconfigrequestedsize = YLeaf(YType.uint32, "cnpdTopNConfigRequestedSize")

                self.cnpdtopnconfigsampletime = YLeaf(YType.uint32, "cnpdTopNConfigSampleTime")

                self.cnpdtopnconfigstatsselect = YLeaf(YType.enumeration, "cnpdTopNConfigStatsSelect")

                self.cnpdtopnconfigstatus = YLeaf(YType.enumeration, "cnpdTopNConfigStatus")

                self.cnpdtopnconfigtime = YLeaf(YType.uint32, "cnpdTopNConfigTime")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cnpdtopnconfigindex",
                                "cnpdtopnconfiggrantedsize",
                                "cnpdtopnconfigifindex",
                                "cnpdtopnconfigrequestedsize",
                                "cnpdtopnconfigsampletime",
                                "cnpdtopnconfigstatsselect",
                                "cnpdtopnconfigstatus",
                                "cnpdtopnconfigtime") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoNbarProtocolDiscoveryMib.Cnpdtopnconfigtable.Cnpdtopnconfigentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoNbarProtocolDiscoveryMib.Cnpdtopnconfigtable.Cnpdtopnconfigentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cnpdtopnconfigindex.is_set or
                    self.cnpdtopnconfiggrantedsize.is_set or
                    self.cnpdtopnconfigifindex.is_set or
                    self.cnpdtopnconfigrequestedsize.is_set or
                    self.cnpdtopnconfigsampletime.is_set or
                    self.cnpdtopnconfigstatsselect.is_set or
                    self.cnpdtopnconfigstatus.is_set or
                    self.cnpdtopnconfigtime.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cnpdtopnconfigindex.yfilter != YFilter.not_set or
                    self.cnpdtopnconfiggrantedsize.yfilter != YFilter.not_set or
                    self.cnpdtopnconfigifindex.yfilter != YFilter.not_set or
                    self.cnpdtopnconfigrequestedsize.yfilter != YFilter.not_set or
                    self.cnpdtopnconfigsampletime.yfilter != YFilter.not_set or
                    self.cnpdtopnconfigstatsselect.yfilter != YFilter.not_set or
                    self.cnpdtopnconfigstatus.yfilter != YFilter.not_set or
                    self.cnpdtopnconfigtime.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cnpdTopNConfigEntry" + "[cnpdTopNConfigIndex='" + self.cnpdtopnconfigindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:CISCO-NBAR-PROTOCOL-DISCOVERY-MIB/cnpdTopNConfigTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cnpdtopnconfigindex.is_set or self.cnpdtopnconfigindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnpdtopnconfigindex.get_name_leafdata())
                if (self.cnpdtopnconfiggrantedsize.is_set or self.cnpdtopnconfiggrantedsize.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnpdtopnconfiggrantedsize.get_name_leafdata())
                if (self.cnpdtopnconfigifindex.is_set or self.cnpdtopnconfigifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnpdtopnconfigifindex.get_name_leafdata())
                if (self.cnpdtopnconfigrequestedsize.is_set or self.cnpdtopnconfigrequestedsize.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnpdtopnconfigrequestedsize.get_name_leafdata())
                if (self.cnpdtopnconfigsampletime.is_set or self.cnpdtopnconfigsampletime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnpdtopnconfigsampletime.get_name_leafdata())
                if (self.cnpdtopnconfigstatsselect.is_set or self.cnpdtopnconfigstatsselect.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnpdtopnconfigstatsselect.get_name_leafdata())
                if (self.cnpdtopnconfigstatus.is_set or self.cnpdtopnconfigstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnpdtopnconfigstatus.get_name_leafdata())
                if (self.cnpdtopnconfigtime.is_set or self.cnpdtopnconfigtime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnpdtopnconfigtime.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cnpdTopNConfigIndex" or name == "cnpdTopNConfigGrantedSize" or name == "cnpdTopNConfigIfIndex" or name == "cnpdTopNConfigRequestedSize" or name == "cnpdTopNConfigSampleTime" or name == "cnpdTopNConfigStatsSelect" or name == "cnpdTopNConfigStatus" or name == "cnpdTopNConfigTime"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cnpdTopNConfigIndex"):
                    self.cnpdtopnconfigindex = value
                    self.cnpdtopnconfigindex.value_namespace = name_space
                    self.cnpdtopnconfigindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cnpdTopNConfigGrantedSize"):
                    self.cnpdtopnconfiggrantedsize = value
                    self.cnpdtopnconfiggrantedsize.value_namespace = name_space
                    self.cnpdtopnconfiggrantedsize.value_namespace_prefix = name_space_prefix
                if(value_path == "cnpdTopNConfigIfIndex"):
                    self.cnpdtopnconfigifindex = value
                    self.cnpdtopnconfigifindex.value_namespace = name_space
                    self.cnpdtopnconfigifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cnpdTopNConfigRequestedSize"):
                    self.cnpdtopnconfigrequestedsize = value
                    self.cnpdtopnconfigrequestedsize.value_namespace = name_space
                    self.cnpdtopnconfigrequestedsize.value_namespace_prefix = name_space_prefix
                if(value_path == "cnpdTopNConfigSampleTime"):
                    self.cnpdtopnconfigsampletime = value
                    self.cnpdtopnconfigsampletime.value_namespace = name_space
                    self.cnpdtopnconfigsampletime.value_namespace_prefix = name_space_prefix
                if(value_path == "cnpdTopNConfigStatsSelect"):
                    self.cnpdtopnconfigstatsselect = value
                    self.cnpdtopnconfigstatsselect.value_namespace = name_space
                    self.cnpdtopnconfigstatsselect.value_namespace_prefix = name_space_prefix
                if(value_path == "cnpdTopNConfigStatus"):
                    self.cnpdtopnconfigstatus = value
                    self.cnpdtopnconfigstatus.value_namespace = name_space
                    self.cnpdtopnconfigstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "cnpdTopNConfigTime"):
                    self.cnpdtopnconfigtime = value
                    self.cnpdtopnconfigtime.value_namespace = name_space
                    self.cnpdtopnconfigtime.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cnpdtopnconfigentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cnpdtopnconfigentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cnpdTopNConfigTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:CISCO-NBAR-PROTOCOL-DISCOVERY-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cnpdTopNConfigEntry"):
                for c in self.cnpdtopnconfigentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoNbarProtocolDiscoveryMib.Cnpdtopnconfigtable.Cnpdtopnconfigentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cnpdtopnconfigentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cnpdTopNConfigEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cnpdtopnstatstable(Entity):
        """
        A cnpdTopNStatsTable describes an ordered
        list of protocols.
        
        .. attribute:: cnpdtopnstatsentry
        
        	This entry is used to store a set of objects which  describe a cnpdTopNStatsTable. A cnpdTopNStatsTable  is a number of protocols and statistics sorted  according to the criteria in the associated cnpdTopNConfigEntry.  Therefore a cnpdTopNStatsTable can differ in content  and size according to what was configured in the associated cnpdTopNConfigTableEntry
        	**type**\: list of    :py:class:`Cnpdtopnstatsentry <ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB.CiscoNbarProtocolDiscoveryMib.Cnpdtopnstatstable.Cnpdtopnstatsentry>`
        
        

        """

        _prefix = 'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB'
        _revision = '2002-08-16'

        def __init__(self):
            super(CiscoNbarProtocolDiscoveryMib.Cnpdtopnstatstable, self).__init__()

            self.yang_name = "cnpdTopNStatsTable"
            self.yang_parent_name = "CISCO-NBAR-PROTOCOL-DISCOVERY-MIB"

            self.cnpdtopnstatsentry = YList(self)

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
                        super(CiscoNbarProtocolDiscoveryMib.Cnpdtopnstatstable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoNbarProtocolDiscoveryMib.Cnpdtopnstatstable, self).__setattr__(name, value)


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
            
            	**refers to**\:  :py:class:`cnpdtopnconfigindex <ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB.CiscoNbarProtocolDiscoveryMib.Cnpdtopnconfigtable.Cnpdtopnconfigentry>`
            
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
                super(CiscoNbarProtocolDiscoveryMib.Cnpdtopnstatstable.Cnpdtopnstatsentry, self).__init__()

                self.yang_name = "cnpdTopNStatsEntry"
                self.yang_parent_name = "cnpdTopNStatsTable"

                self.cnpdtopnconfigindex = YLeaf(YType.str, "cnpdTopNConfigIndex")

                self.cnpdtopnstatsindex = YLeaf(YType.uint32, "cnpdTopNStatsIndex")

                self.cnpdtopnstatshcrate = YLeaf(YType.uint64, "cnpdTopNStatsHCRate")

                self.cnpdtopnstatsprotocolname = YLeaf(YType.str, "cnpdTopNStatsProtocolName")

                self.cnpdtopnstatsrate = YLeaf(YType.uint32, "cnpdTopNStatsRate")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cnpdtopnconfigindex",
                                "cnpdtopnstatsindex",
                                "cnpdtopnstatshcrate",
                                "cnpdtopnstatsprotocolname",
                                "cnpdtopnstatsrate") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoNbarProtocolDiscoveryMib.Cnpdtopnstatstable.Cnpdtopnstatsentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoNbarProtocolDiscoveryMib.Cnpdtopnstatstable.Cnpdtopnstatsentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cnpdtopnconfigindex.is_set or
                    self.cnpdtopnstatsindex.is_set or
                    self.cnpdtopnstatshcrate.is_set or
                    self.cnpdtopnstatsprotocolname.is_set or
                    self.cnpdtopnstatsrate.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cnpdtopnconfigindex.yfilter != YFilter.not_set or
                    self.cnpdtopnstatsindex.yfilter != YFilter.not_set or
                    self.cnpdtopnstatshcrate.yfilter != YFilter.not_set or
                    self.cnpdtopnstatsprotocolname.yfilter != YFilter.not_set or
                    self.cnpdtopnstatsrate.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cnpdTopNStatsEntry" + "[cnpdTopNConfigIndex='" + self.cnpdtopnconfigindex.get() + "']" + "[cnpdTopNStatsIndex='" + self.cnpdtopnstatsindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:CISCO-NBAR-PROTOCOL-DISCOVERY-MIB/cnpdTopNStatsTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cnpdtopnconfigindex.is_set or self.cnpdtopnconfigindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnpdtopnconfigindex.get_name_leafdata())
                if (self.cnpdtopnstatsindex.is_set or self.cnpdtopnstatsindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnpdtopnstatsindex.get_name_leafdata())
                if (self.cnpdtopnstatshcrate.is_set or self.cnpdtopnstatshcrate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnpdtopnstatshcrate.get_name_leafdata())
                if (self.cnpdtopnstatsprotocolname.is_set or self.cnpdtopnstatsprotocolname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnpdtopnstatsprotocolname.get_name_leafdata())
                if (self.cnpdtopnstatsrate.is_set or self.cnpdtopnstatsrate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnpdtopnstatsrate.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cnpdTopNConfigIndex" or name == "cnpdTopNStatsIndex" or name == "cnpdTopNStatsHCRate" or name == "cnpdTopNStatsProtocolName" or name == "cnpdTopNStatsRate"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cnpdTopNConfigIndex"):
                    self.cnpdtopnconfigindex = value
                    self.cnpdtopnconfigindex.value_namespace = name_space
                    self.cnpdtopnconfigindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cnpdTopNStatsIndex"):
                    self.cnpdtopnstatsindex = value
                    self.cnpdtopnstatsindex.value_namespace = name_space
                    self.cnpdtopnstatsindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cnpdTopNStatsHCRate"):
                    self.cnpdtopnstatshcrate = value
                    self.cnpdtopnstatshcrate.value_namespace = name_space
                    self.cnpdtopnstatshcrate.value_namespace_prefix = name_space_prefix
                if(value_path == "cnpdTopNStatsProtocolName"):
                    self.cnpdtopnstatsprotocolname = value
                    self.cnpdtopnstatsprotocolname.value_namespace = name_space
                    self.cnpdtopnstatsprotocolname.value_namespace_prefix = name_space_prefix
                if(value_path == "cnpdTopNStatsRate"):
                    self.cnpdtopnstatsrate = value
                    self.cnpdtopnstatsrate.value_namespace = name_space
                    self.cnpdtopnstatsrate.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cnpdtopnstatsentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cnpdtopnstatsentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cnpdTopNStatsTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:CISCO-NBAR-PROTOCOL-DISCOVERY-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cnpdTopNStatsEntry"):
                for c in self.cnpdtopnstatsentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoNbarProtocolDiscoveryMib.Cnpdtopnstatstable.Cnpdtopnstatsentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cnpdtopnstatsentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cnpdTopNStatsEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cnpdthresholdconfigtable(Entity):
        """
        The cnpdThresholdConfigTable allows the management
        station to create thresholds for the purpose of
        sending notifications if breached, and creating a
        history of breached thresholds.
        
        .. attribute:: cnpdthresholdconfigentry
        
        	This entry contains configuration information to  set thresholds for the purpose of notifications.  The management station is allowed to set thresholds on individual statistics for individual protocols on an interface. If the threshold is breached by the protocol statistic, a new event is written to the cnpdThresholdHistoryTable, which in turn will  generate a Notification Event.  This function has a hysteresis mechanism to limit the generation of events. This mechanism generates one event as a threshold is crossed in the appropriate direction. No more events are generated for that threshold until the opposite threshold is crossed. This stops repeated Notification events being generated each time the value is sampled, when the value is above the threshold. Instead one notification is sent when the threshold is breached and one notification when the statistic drops below the threshold value again
        	**type**\: list of    :py:class:`Cnpdthresholdconfigentry <ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB.CiscoNbarProtocolDiscoveryMib.Cnpdthresholdconfigtable.Cnpdthresholdconfigentry>`
        
        

        """

        _prefix = 'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB'
        _revision = '2002-08-16'

        def __init__(self):
            super(CiscoNbarProtocolDiscoveryMib.Cnpdthresholdconfigtable, self).__init__()

            self.yang_name = "cnpdThresholdConfigTable"
            self.yang_parent_name = "CISCO-NBAR-PROTOCOL-DISCOVERY-MIB"

            self.cnpdthresholdconfigentry = YList(self)

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
                        super(CiscoNbarProtocolDiscoveryMib.Cnpdthresholdconfigtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoNbarProtocolDiscoveryMib.Cnpdthresholdconfigtable, self).__setattr__(name, value)


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
            	**type**\:   :py:class:`Cnpdthresholdconfigsampletype <ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB.CiscoNbarProtocolDiscoveryMib.Cnpdthresholdconfigtable.Cnpdthresholdconfigentry.Cnpdthresholdconfigsampletype>`
            
            .. attribute:: cnpdthresholdconfigstartup
            
            	This controls the type of notification that is  sent when this threshold entry is first enabled.   Because there is no previous sampling history, choosing one of these options determines the type of notification generated \- Rising or Falling.  If the first sample after this entry is enabled  is greater than or equal to cnpdThresholdConfigRising and this object is equal to rising(1) or risingOrFalling(3),  then a single rising notification will be generated.   If the first sample after this entry is enabled is less than or equal to cnpdThresholdConfigFalling and this object is equal to falling(2) or  risingOrFalling(3), then a single falling notification  will be generated
            	**type**\:   :py:class:`Cnpdthresholdconfigstartup <ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB.CiscoNbarProtocolDiscoveryMib.Cnpdthresholdconfigtable.Cnpdthresholdconfigentry.Cnpdthresholdconfigstartup>`
            
            .. attribute:: cnpdthresholdconfigstatsselect
            
            	This object allows the management station to select the statistic used to base the threshold on.  For example a cnpdThresholdConfigStatsSelect of bitRateSum means cnpdThresholdConfigRising and cnpdThresholdConfigFalling are values based on the combined value of in and out bitrates
            	**type**\:   :py:class:`Ciscopddatatype <ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB.Ciscopddatatype>`
            
            .. attribute:: cnpdthresholdconfigstatus
            
            	This object is used to create or delete  the row entry in cnpdThresholdConfigTable.   When creating a row entry the management station  is required to specify a value for  cnpdThresholdConfigIfIndex, cnpdThresholdConfigRising  and cnpdThresholdConfigFalling.  'active' means that a createAndGo or active has  been issued, AND a valid ifIndex exists. And therefore  if a row is 'active' it means a ThresholdHistory entry  may have been generated if the value was breached.  If you set an 'active' row to 'createAndWait' \- it will  in fact get the status 'notReady'.   Likewise if you set any row to 'notInService' or 'notReady'  it will go to the 'notReady' state
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            

            """

            _prefix = 'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB'
            _revision = '2002-08-16'

            def __init__(self):
                super(CiscoNbarProtocolDiscoveryMib.Cnpdthresholdconfigtable.Cnpdthresholdconfigentry, self).__init__()

                self.yang_name = "cnpdThresholdConfigEntry"
                self.yang_parent_name = "cnpdThresholdConfigTable"

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

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cnpdthresholdconfigindex",
                                "cnpdthresholdconfigfalling",
                                "cnpdthresholdconfigifindex",
                                "cnpdthresholdconfiginterval",
                                "cnpdthresholdconfigprotocol",
                                "cnpdthresholdconfigprotocolany",
                                "cnpdthresholdconfigrising",
                                "cnpdthresholdconfigsampletype",
                                "cnpdthresholdconfigstartup",
                                "cnpdthresholdconfigstatsselect",
                                "cnpdthresholdconfigstatus") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoNbarProtocolDiscoveryMib.Cnpdthresholdconfigtable.Cnpdthresholdconfigentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoNbarProtocolDiscoveryMib.Cnpdthresholdconfigtable.Cnpdthresholdconfigentry, self).__setattr__(name, value)

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


            def has_data(self):
                return (
                    self.cnpdthresholdconfigindex.is_set or
                    self.cnpdthresholdconfigfalling.is_set or
                    self.cnpdthresholdconfigifindex.is_set or
                    self.cnpdthresholdconfiginterval.is_set or
                    self.cnpdthresholdconfigprotocol.is_set or
                    self.cnpdthresholdconfigprotocolany.is_set or
                    self.cnpdthresholdconfigrising.is_set or
                    self.cnpdthresholdconfigsampletype.is_set or
                    self.cnpdthresholdconfigstartup.is_set or
                    self.cnpdthresholdconfigstatsselect.is_set or
                    self.cnpdthresholdconfigstatus.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cnpdthresholdconfigindex.yfilter != YFilter.not_set or
                    self.cnpdthresholdconfigfalling.yfilter != YFilter.not_set or
                    self.cnpdthresholdconfigifindex.yfilter != YFilter.not_set or
                    self.cnpdthresholdconfiginterval.yfilter != YFilter.not_set or
                    self.cnpdthresholdconfigprotocol.yfilter != YFilter.not_set or
                    self.cnpdthresholdconfigprotocolany.yfilter != YFilter.not_set or
                    self.cnpdthresholdconfigrising.yfilter != YFilter.not_set or
                    self.cnpdthresholdconfigsampletype.yfilter != YFilter.not_set or
                    self.cnpdthresholdconfigstartup.yfilter != YFilter.not_set or
                    self.cnpdthresholdconfigstatsselect.yfilter != YFilter.not_set or
                    self.cnpdthresholdconfigstatus.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cnpdThresholdConfigEntry" + "[cnpdThresholdConfigIndex='" + self.cnpdthresholdconfigindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:CISCO-NBAR-PROTOCOL-DISCOVERY-MIB/cnpdThresholdConfigTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cnpdthresholdconfigindex.is_set or self.cnpdthresholdconfigindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnpdthresholdconfigindex.get_name_leafdata())
                if (self.cnpdthresholdconfigfalling.is_set or self.cnpdthresholdconfigfalling.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnpdthresholdconfigfalling.get_name_leafdata())
                if (self.cnpdthresholdconfigifindex.is_set or self.cnpdthresholdconfigifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnpdthresholdconfigifindex.get_name_leafdata())
                if (self.cnpdthresholdconfiginterval.is_set or self.cnpdthresholdconfiginterval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnpdthresholdconfiginterval.get_name_leafdata())
                if (self.cnpdthresholdconfigprotocol.is_set or self.cnpdthresholdconfigprotocol.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnpdthresholdconfigprotocol.get_name_leafdata())
                if (self.cnpdthresholdconfigprotocolany.is_set or self.cnpdthresholdconfigprotocolany.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnpdthresholdconfigprotocolany.get_name_leafdata())
                if (self.cnpdthresholdconfigrising.is_set or self.cnpdthresholdconfigrising.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnpdthresholdconfigrising.get_name_leafdata())
                if (self.cnpdthresholdconfigsampletype.is_set or self.cnpdthresholdconfigsampletype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnpdthresholdconfigsampletype.get_name_leafdata())
                if (self.cnpdthresholdconfigstartup.is_set or self.cnpdthresholdconfigstartup.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnpdthresholdconfigstartup.get_name_leafdata())
                if (self.cnpdthresholdconfigstatsselect.is_set or self.cnpdthresholdconfigstatsselect.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnpdthresholdconfigstatsselect.get_name_leafdata())
                if (self.cnpdthresholdconfigstatus.is_set or self.cnpdthresholdconfigstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnpdthresholdconfigstatus.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cnpdThresholdConfigIndex" or name == "cnpdThresholdConfigFalling" or name == "cnpdThresholdConfigIfIndex" or name == "cnpdThresholdConfigInterval" or name == "cnpdThresholdConfigProtocol" or name == "cnpdThresholdConfigProtocolAny" or name == "cnpdThresholdConfigRising" or name == "cnpdThresholdConfigSampleType" or name == "cnpdThresholdConfigStartup" or name == "cnpdThresholdConfigStatsSelect" or name == "cnpdThresholdConfigStatus"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cnpdThresholdConfigIndex"):
                    self.cnpdthresholdconfigindex = value
                    self.cnpdthresholdconfigindex.value_namespace = name_space
                    self.cnpdthresholdconfigindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cnpdThresholdConfigFalling"):
                    self.cnpdthresholdconfigfalling = value
                    self.cnpdthresholdconfigfalling.value_namespace = name_space
                    self.cnpdthresholdconfigfalling.value_namespace_prefix = name_space_prefix
                if(value_path == "cnpdThresholdConfigIfIndex"):
                    self.cnpdthresholdconfigifindex = value
                    self.cnpdthresholdconfigifindex.value_namespace = name_space
                    self.cnpdthresholdconfigifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cnpdThresholdConfigInterval"):
                    self.cnpdthresholdconfiginterval = value
                    self.cnpdthresholdconfiginterval.value_namespace = name_space
                    self.cnpdthresholdconfiginterval.value_namespace_prefix = name_space_prefix
                if(value_path == "cnpdThresholdConfigProtocol"):
                    self.cnpdthresholdconfigprotocol = value
                    self.cnpdthresholdconfigprotocol.value_namespace = name_space
                    self.cnpdthresholdconfigprotocol.value_namespace_prefix = name_space_prefix
                if(value_path == "cnpdThresholdConfigProtocolAny"):
                    self.cnpdthresholdconfigprotocolany = value
                    self.cnpdthresholdconfigprotocolany.value_namespace = name_space
                    self.cnpdthresholdconfigprotocolany.value_namespace_prefix = name_space_prefix
                if(value_path == "cnpdThresholdConfigRising"):
                    self.cnpdthresholdconfigrising = value
                    self.cnpdthresholdconfigrising.value_namespace = name_space
                    self.cnpdthresholdconfigrising.value_namespace_prefix = name_space_prefix
                if(value_path == "cnpdThresholdConfigSampleType"):
                    self.cnpdthresholdconfigsampletype = value
                    self.cnpdthresholdconfigsampletype.value_namespace = name_space
                    self.cnpdthresholdconfigsampletype.value_namespace_prefix = name_space_prefix
                if(value_path == "cnpdThresholdConfigStartup"):
                    self.cnpdthresholdconfigstartup = value
                    self.cnpdthresholdconfigstartup.value_namespace = name_space
                    self.cnpdthresholdconfigstartup.value_namespace_prefix = name_space_prefix
                if(value_path == "cnpdThresholdConfigStatsSelect"):
                    self.cnpdthresholdconfigstatsselect = value
                    self.cnpdthresholdconfigstatsselect.value_namespace = name_space
                    self.cnpdthresholdconfigstatsselect.value_namespace_prefix = name_space_prefix
                if(value_path == "cnpdThresholdConfigStatus"):
                    self.cnpdthresholdconfigstatus = value
                    self.cnpdthresholdconfigstatus.value_namespace = name_space
                    self.cnpdthresholdconfigstatus.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cnpdthresholdconfigentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cnpdthresholdconfigentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cnpdThresholdConfigTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:CISCO-NBAR-PROTOCOL-DISCOVERY-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cnpdThresholdConfigEntry"):
                for c in self.cnpdthresholdconfigentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoNbarProtocolDiscoveryMib.Cnpdthresholdconfigtable.Cnpdthresholdconfigentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cnpdthresholdconfigentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cnpdThresholdConfigEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cnpdthresholdhistorytable(Entity):
        """
        The Threshold History table. Notifications
        are unreliable so this table provides a
        history of the last 5000 threshold breached
        events. A notification can be traced back to
        its cnpdThresholdHistoryEntry.
        
        .. attribute:: cnpdthresholdhistoryentry
        
        	This entry is created each time a threshold  is breached.   Thus there is not necessarily a one to one  relationship to cnpdThresholdConfigTable  as not every Threshold configured will  be breached
        	**type**\: list of    :py:class:`Cnpdthresholdhistoryentry <ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB.CiscoNbarProtocolDiscoveryMib.Cnpdthresholdhistorytable.Cnpdthresholdhistoryentry>`
        
        

        """

        _prefix = 'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB'
        _revision = '2002-08-16'

        def __init__(self):
            super(CiscoNbarProtocolDiscoveryMib.Cnpdthresholdhistorytable, self).__init__()

            self.yang_name = "cnpdThresholdHistoryTable"
            self.yang_parent_name = "CISCO-NBAR-PROTOCOL-DISCOVERY-MIB"

            self.cnpdthresholdhistoryentry = YList(self)

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
                        super(CiscoNbarProtocolDiscoveryMib.Cnpdthresholdhistorytable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoNbarProtocolDiscoveryMib.Cnpdthresholdhistorytable, self).__setattr__(name, value)


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
            	**type**\:   :py:class:`Ciscopddatatype <ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB.Ciscopddatatype>`
            
            .. attribute:: cnpdthresholdhistorytime
            
            	The value of sysUpTime of the running  configuration when the event occurred
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cnpdthresholdhistorytype
            
            	Describes whether this is an event caused by a rising or falling threshold breach
            	**type**\:   :py:class:`Cnpdthresholdhistorytype <ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB.CiscoNbarProtocolDiscoveryMib.Cnpdthresholdhistorytable.Cnpdthresholdhistoryentry.Cnpdthresholdhistorytype>`
            
            .. attribute:: cnpdthresholdhistoryvalue
            
            	The actual value of the statistic when  the sampling was made
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            

            """

            _prefix = 'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB'
            _revision = '2002-08-16'

            def __init__(self):
                super(CiscoNbarProtocolDiscoveryMib.Cnpdthresholdhistorytable.Cnpdthresholdhistoryentry, self).__init__()

                self.yang_name = "cnpdThresholdHistoryEntry"
                self.yang_parent_name = "cnpdThresholdHistoryTable"

                self.cnpdthresholdhistoryindex = YLeaf(YType.uint32, "cnpdThresholdHistoryIndex")

                self.cnpdthresholdhistoryconfigindex = YLeaf(YType.uint32, "cnpdThresholdHistoryConfigIndex")

                self.cnpdthresholdhistoryprotocol = YLeaf(YType.uint32, "cnpdThresholdHistoryProtocol")

                self.cnpdthresholdhistorystatsselect = YLeaf(YType.enumeration, "cnpdThresholdHistoryStatsSelect")

                self.cnpdthresholdhistorytime = YLeaf(YType.uint32, "cnpdThresholdHistoryTime")

                self.cnpdthresholdhistorytype = YLeaf(YType.enumeration, "cnpdThresholdHistoryType")

                self.cnpdthresholdhistoryvalue = YLeaf(YType.uint32, "cnpdThresholdHistoryValue")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cnpdthresholdhistoryindex",
                                "cnpdthresholdhistoryconfigindex",
                                "cnpdthresholdhistoryprotocol",
                                "cnpdthresholdhistorystatsselect",
                                "cnpdthresholdhistorytime",
                                "cnpdthresholdhistorytype",
                                "cnpdthresholdhistoryvalue") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoNbarProtocolDiscoveryMib.Cnpdthresholdhistorytable.Cnpdthresholdhistoryentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoNbarProtocolDiscoveryMib.Cnpdthresholdhistorytable.Cnpdthresholdhistoryentry, self).__setattr__(name, value)

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


            def has_data(self):
                return (
                    self.cnpdthresholdhistoryindex.is_set or
                    self.cnpdthresholdhistoryconfigindex.is_set or
                    self.cnpdthresholdhistoryprotocol.is_set or
                    self.cnpdthresholdhistorystatsselect.is_set or
                    self.cnpdthresholdhistorytime.is_set or
                    self.cnpdthresholdhistorytype.is_set or
                    self.cnpdthresholdhistoryvalue.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cnpdthresholdhistoryindex.yfilter != YFilter.not_set or
                    self.cnpdthresholdhistoryconfigindex.yfilter != YFilter.not_set or
                    self.cnpdthresholdhistoryprotocol.yfilter != YFilter.not_set or
                    self.cnpdthresholdhistorystatsselect.yfilter != YFilter.not_set or
                    self.cnpdthresholdhistorytime.yfilter != YFilter.not_set or
                    self.cnpdthresholdhistorytype.yfilter != YFilter.not_set or
                    self.cnpdthresholdhistoryvalue.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cnpdThresholdHistoryEntry" + "[cnpdThresholdHistoryIndex='" + self.cnpdthresholdhistoryindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:CISCO-NBAR-PROTOCOL-DISCOVERY-MIB/cnpdThresholdHistoryTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cnpdthresholdhistoryindex.is_set or self.cnpdthresholdhistoryindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnpdthresholdhistoryindex.get_name_leafdata())
                if (self.cnpdthresholdhistoryconfigindex.is_set or self.cnpdthresholdhistoryconfigindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnpdthresholdhistoryconfigindex.get_name_leafdata())
                if (self.cnpdthresholdhistoryprotocol.is_set or self.cnpdthresholdhistoryprotocol.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnpdthresholdhistoryprotocol.get_name_leafdata())
                if (self.cnpdthresholdhistorystatsselect.is_set or self.cnpdthresholdhistorystatsselect.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnpdthresholdhistorystatsselect.get_name_leafdata())
                if (self.cnpdthresholdhistorytime.is_set or self.cnpdthresholdhistorytime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnpdthresholdhistorytime.get_name_leafdata())
                if (self.cnpdthresholdhistorytype.is_set or self.cnpdthresholdhistorytype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnpdthresholdhistorytype.get_name_leafdata())
                if (self.cnpdthresholdhistoryvalue.is_set or self.cnpdthresholdhistoryvalue.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnpdthresholdhistoryvalue.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cnpdThresholdHistoryIndex" or name == "cnpdThresholdHistoryConfigIndex" or name == "cnpdThresholdHistoryProtocol" or name == "cnpdThresholdHistoryStatsSelect" or name == "cnpdThresholdHistoryTime" or name == "cnpdThresholdHistoryType" or name == "cnpdThresholdHistoryValue"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cnpdThresholdHistoryIndex"):
                    self.cnpdthresholdhistoryindex = value
                    self.cnpdthresholdhistoryindex.value_namespace = name_space
                    self.cnpdthresholdhistoryindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cnpdThresholdHistoryConfigIndex"):
                    self.cnpdthresholdhistoryconfigindex = value
                    self.cnpdthresholdhistoryconfigindex.value_namespace = name_space
                    self.cnpdthresholdhistoryconfigindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cnpdThresholdHistoryProtocol"):
                    self.cnpdthresholdhistoryprotocol = value
                    self.cnpdthresholdhistoryprotocol.value_namespace = name_space
                    self.cnpdthresholdhistoryprotocol.value_namespace_prefix = name_space_prefix
                if(value_path == "cnpdThresholdHistoryStatsSelect"):
                    self.cnpdthresholdhistorystatsselect = value
                    self.cnpdthresholdhistorystatsselect.value_namespace = name_space
                    self.cnpdthresholdhistorystatsselect.value_namespace_prefix = name_space_prefix
                if(value_path == "cnpdThresholdHistoryTime"):
                    self.cnpdthresholdhistorytime = value
                    self.cnpdthresholdhistorytime.value_namespace = name_space
                    self.cnpdthresholdhistorytime.value_namespace_prefix = name_space_prefix
                if(value_path == "cnpdThresholdHistoryType"):
                    self.cnpdthresholdhistorytype = value
                    self.cnpdthresholdhistorytype.value_namespace = name_space
                    self.cnpdthresholdhistorytype.value_namespace_prefix = name_space_prefix
                if(value_path == "cnpdThresholdHistoryValue"):
                    self.cnpdthresholdhistoryvalue = value
                    self.cnpdthresholdhistoryvalue.value_namespace = name_space
                    self.cnpdthresholdhistoryvalue.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cnpdthresholdhistoryentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cnpdthresholdhistoryentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cnpdThresholdHistoryTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:CISCO-NBAR-PROTOCOL-DISCOVERY-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cnpdThresholdHistoryEntry"):
                for c in self.cnpdthresholdhistoryentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoNbarProtocolDiscoveryMib.Cnpdthresholdhistorytable.Cnpdthresholdhistoryentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cnpdthresholdhistoryentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cnpdThresholdHistoryEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cnpdsupportedprotocolstable(Entity):
        """
        The Supported Protocols table lists all the 
        protocols and applications which NBAR is currently
        capable of recognizing.
        
        .. attribute:: cnpdsupportedprotocolsentry
        
        	A entry in the Supported Protocols table reflecting key information about a protocol
        	**type**\: list of    :py:class:`Cnpdsupportedprotocolsentry <ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB.CiscoNbarProtocolDiscoveryMib.Cnpdsupportedprotocolstable.Cnpdsupportedprotocolsentry>`
        
        

        """

        _prefix = 'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB'
        _revision = '2002-08-16'

        def __init__(self):
            super(CiscoNbarProtocolDiscoveryMib.Cnpdsupportedprotocolstable, self).__init__()

            self.yang_name = "cnpdSupportedProtocolsTable"
            self.yang_parent_name = "CISCO-NBAR-PROTOCOL-DISCOVERY-MIB"

            self.cnpdsupportedprotocolsentry = YList(self)

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
                        super(CiscoNbarProtocolDiscoveryMib.Cnpdsupportedprotocolstable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoNbarProtocolDiscoveryMib.Cnpdsupportedprotocolstable, self).__setattr__(name, value)


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
                super(CiscoNbarProtocolDiscoveryMib.Cnpdsupportedprotocolstable.Cnpdsupportedprotocolsentry, self).__init__()

                self.yang_name = "cnpdSupportedProtocolsEntry"
                self.yang_parent_name = "cnpdSupportedProtocolsTable"

                self.cnpdsupportedprotocolsindex = YLeaf(YType.uint32, "cnpdSupportedProtocolsIndex")

                self.cnpdsupportedprotocolsname = YLeaf(YType.str, "cnpdSupportedProtocolsName")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cnpdsupportedprotocolsindex",
                                "cnpdsupportedprotocolsname") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoNbarProtocolDiscoveryMib.Cnpdsupportedprotocolstable.Cnpdsupportedprotocolsentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoNbarProtocolDiscoveryMib.Cnpdsupportedprotocolstable.Cnpdsupportedprotocolsentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cnpdsupportedprotocolsindex.is_set or
                    self.cnpdsupportedprotocolsname.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cnpdsupportedprotocolsindex.yfilter != YFilter.not_set or
                    self.cnpdsupportedprotocolsname.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cnpdSupportedProtocolsEntry" + "[cnpdSupportedProtocolsIndex='" + self.cnpdsupportedprotocolsindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:CISCO-NBAR-PROTOCOL-DISCOVERY-MIB/cnpdSupportedProtocolsTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cnpdsupportedprotocolsindex.is_set or self.cnpdsupportedprotocolsindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnpdsupportedprotocolsindex.get_name_leafdata())
                if (self.cnpdsupportedprotocolsname.is_set or self.cnpdsupportedprotocolsname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnpdsupportedprotocolsname.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cnpdSupportedProtocolsIndex" or name == "cnpdSupportedProtocolsName"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cnpdSupportedProtocolsIndex"):
                    self.cnpdsupportedprotocolsindex = value
                    self.cnpdsupportedprotocolsindex.value_namespace = name_space
                    self.cnpdsupportedprotocolsindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cnpdSupportedProtocolsName"):
                    self.cnpdsupportedprotocolsname = value
                    self.cnpdsupportedprotocolsname.value_namespace = name_space
                    self.cnpdsupportedprotocolsname.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cnpdsupportedprotocolsentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cnpdsupportedprotocolsentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cnpdSupportedProtocolsTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:CISCO-NBAR-PROTOCOL-DISCOVERY-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cnpdSupportedProtocolsEntry"):
                for c in self.cnpdsupportedprotocolsentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoNbarProtocolDiscoveryMib.Cnpdsupportedprotocolstable.Cnpdsupportedprotocolsentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cnpdsupportedprotocolsentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cnpdSupportedProtocolsEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.cnpdallstatstable is not None and self.cnpdallstatstable.has_data()) or
            (self.cnpdnotificationsconfig is not None and self.cnpdnotificationsconfig.has_data()) or
            (self.cnpdstatustable is not None and self.cnpdstatustable.has_data()) or
            (self.cnpdsupportedprotocolstable is not None and self.cnpdsupportedprotocolstable.has_data()) or
            (self.cnpdthresholdconfigtable is not None and self.cnpdthresholdconfigtable.has_data()) or
            (self.cnpdthresholdhistorytable is not None and self.cnpdthresholdhistorytable.has_data()) or
            (self.cnpdtopnconfigtable is not None and self.cnpdtopnconfigtable.has_data()) or
            (self.cnpdtopnstatstable is not None and self.cnpdtopnstatstable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.cnpdallstatstable is not None and self.cnpdallstatstable.has_operation()) or
            (self.cnpdnotificationsconfig is not None and self.cnpdnotificationsconfig.has_operation()) or
            (self.cnpdstatustable is not None and self.cnpdstatustable.has_operation()) or
            (self.cnpdsupportedprotocolstable is not None and self.cnpdsupportedprotocolstable.has_operation()) or
            (self.cnpdthresholdconfigtable is not None and self.cnpdthresholdconfigtable.has_operation()) or
            (self.cnpdthresholdhistorytable is not None and self.cnpdthresholdhistorytable.has_operation()) or
            (self.cnpdtopnconfigtable is not None and self.cnpdtopnconfigtable.has_operation()) or
            (self.cnpdtopnstatstable is not None and self.cnpdtopnstatstable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "CISCO-NBAR-PROTOCOL-DISCOVERY-MIB:CISCO-NBAR-PROTOCOL-DISCOVERY-MIB" + path_buffer

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

        if (child_yang_name == "cnpdAllStatsTable"):
            if (self.cnpdallstatstable is None):
                self.cnpdallstatstable = CiscoNbarProtocolDiscoveryMib.Cnpdallstatstable()
                self.cnpdallstatstable.parent = self
                self._children_name_map["cnpdallstatstable"] = "cnpdAllStatsTable"
            return self.cnpdallstatstable

        if (child_yang_name == "cnpdNotificationsConfig"):
            if (self.cnpdnotificationsconfig is None):
                self.cnpdnotificationsconfig = CiscoNbarProtocolDiscoveryMib.Cnpdnotificationsconfig()
                self.cnpdnotificationsconfig.parent = self
                self._children_name_map["cnpdnotificationsconfig"] = "cnpdNotificationsConfig"
            return self.cnpdnotificationsconfig

        if (child_yang_name == "cnpdStatusTable"):
            if (self.cnpdstatustable is None):
                self.cnpdstatustable = CiscoNbarProtocolDiscoveryMib.Cnpdstatustable()
                self.cnpdstatustable.parent = self
                self._children_name_map["cnpdstatustable"] = "cnpdStatusTable"
            return self.cnpdstatustable

        if (child_yang_name == "cnpdSupportedProtocolsTable"):
            if (self.cnpdsupportedprotocolstable is None):
                self.cnpdsupportedprotocolstable = CiscoNbarProtocolDiscoveryMib.Cnpdsupportedprotocolstable()
                self.cnpdsupportedprotocolstable.parent = self
                self._children_name_map["cnpdsupportedprotocolstable"] = "cnpdSupportedProtocolsTable"
            return self.cnpdsupportedprotocolstable

        if (child_yang_name == "cnpdThresholdConfigTable"):
            if (self.cnpdthresholdconfigtable is None):
                self.cnpdthresholdconfigtable = CiscoNbarProtocolDiscoveryMib.Cnpdthresholdconfigtable()
                self.cnpdthresholdconfigtable.parent = self
                self._children_name_map["cnpdthresholdconfigtable"] = "cnpdThresholdConfigTable"
            return self.cnpdthresholdconfigtable

        if (child_yang_name == "cnpdThresholdHistoryTable"):
            if (self.cnpdthresholdhistorytable is None):
                self.cnpdthresholdhistorytable = CiscoNbarProtocolDiscoveryMib.Cnpdthresholdhistorytable()
                self.cnpdthresholdhistorytable.parent = self
                self._children_name_map["cnpdthresholdhistorytable"] = "cnpdThresholdHistoryTable"
            return self.cnpdthresholdhistorytable

        if (child_yang_name == "cnpdTopNConfigTable"):
            if (self.cnpdtopnconfigtable is None):
                self.cnpdtopnconfigtable = CiscoNbarProtocolDiscoveryMib.Cnpdtopnconfigtable()
                self.cnpdtopnconfigtable.parent = self
                self._children_name_map["cnpdtopnconfigtable"] = "cnpdTopNConfigTable"
            return self.cnpdtopnconfigtable

        if (child_yang_name == "cnpdTopNStatsTable"):
            if (self.cnpdtopnstatstable is None):
                self.cnpdtopnstatstable = CiscoNbarProtocolDiscoveryMib.Cnpdtopnstatstable()
                self.cnpdtopnstatstable.parent = self
                self._children_name_map["cnpdtopnstatstable"] = "cnpdTopNStatsTable"
            return self.cnpdtopnstatstable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "cnpdAllStatsTable" or name == "cnpdNotificationsConfig" or name == "cnpdStatusTable" or name == "cnpdSupportedProtocolsTable" or name == "cnpdThresholdConfigTable" or name == "cnpdThresholdHistoryTable" or name == "cnpdTopNConfigTable" or name == "cnpdTopNStatsTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CiscoNbarProtocolDiscoveryMib()
        return self._top_entity

