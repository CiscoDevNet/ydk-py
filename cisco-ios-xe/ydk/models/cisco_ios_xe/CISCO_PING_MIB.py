""" CISCO_PING_MIB 

Modified description of ciscoPingAddress object.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CiscoPingMib(Entity):
    """
    
    
    .. attribute:: ciscopingtable
    
    	A table of ping request entries
    	**type**\:   :py:class:`Ciscopingtable <ydk.models.cisco_ios_xe.CISCO_PING_MIB.CiscoPingMib.Ciscopingtable>`
    
    

    """

    _prefix = 'CISCO-PING-MIB'
    _revision = '2001-08-28'

    def __init__(self):
        super(CiscoPingMib, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-PING-MIB"
        self.yang_parent_name = "CISCO-PING-MIB"

        self.ciscopingtable = CiscoPingMib.Ciscopingtable()
        self.ciscopingtable.parent = self
        self._children_name_map["ciscopingtable"] = "ciscoPingTable"
        self._children_yang_names.add("ciscoPingTable")


    class Ciscopingtable(Entity):
        """
        A table of ping request entries.
        
        .. attribute:: ciscopingentry
        
        	A ping request entry.  A management station wishing to create an entry should first generate a pseudo\-random serial number to be used as the index to this sparse table.  The station should then create the associated instance of the row status and row owner objects.  It must also, either in the same or in successive PDUs, create the associated instance of the protocol and address objects.  It should also modify the default values for the other configuration objects if the defaults are not appropriate.  Once the appropriate instance of all the configuration objects have been created, either by an explicit SNMP set request or by default, the row status should be set to active to initiate the request.  Note that this entire procedure may be initiated via a single set request which specifies a row status of createAndGo as well as specifies valid values for the non\-defaulted configuration objects.  Once the ping sequence has been activated, it cannot be stopped \-\- it will run until the configured number of packets have been sent.  Once the sequence completes, the management station should retrieve the values of the status objects of interest, and should then delete the entry.  In order to prevent old entries from clogging the table, entries will be aged out, but an entry will never be deleted within 5 minutes of completing
        	**type**\: list of    :py:class:`Ciscopingentry <ydk.models.cisco_ios_xe.CISCO_PING_MIB.CiscoPingMib.Ciscopingtable.Ciscopingentry>`
        
        

        """

        _prefix = 'CISCO-PING-MIB'
        _revision = '2001-08-28'

        def __init__(self):
            super(CiscoPingMib.Ciscopingtable, self).__init__()

            self.yang_name = "ciscoPingTable"
            self.yang_parent_name = "CISCO-PING-MIB"

            self.ciscopingentry = YList(self)

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
                        super(CiscoPingMib.Ciscopingtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoPingMib.Ciscopingtable, self).__setattr__(name, value)


        class Ciscopingentry(Entity):
            """
            A ping request entry.
            
            A management station wishing to create an entry should
            first generate a pseudo\-random serial number to be used
            as the index to this sparse table.  The station should
            then create the associated instance of the row status
            and row owner objects.  It must also, either in the same
            or in successive PDUs, create the associated instance of
            the protocol and address objects.  It should also modify
            the default values for the other configuration objects
            if the defaults are not appropriate.
            
            Once the appropriate instance of all the configuration
            objects have been created, either by an explicit SNMP
            set request or by default, the row status should be set
            to active to initiate the request.  Note that this entire
            procedure may be initiated via a single set request which
            specifies a row status of createAndGo as well as specifies
            valid values for the non\-defaulted configuration objects.
            
            Once the ping sequence has been activated, it cannot be
            stopped \-\- it will run until the configured number of
            packets have been sent.
            
            Once the sequence completes, the management station should
            retrieve the values of the status objects of interest, and
            should then delete the entry.  In order to prevent old
            entries from clogging the table, entries will be aged out,
            but an entry will never be deleted within 5 minutes of
            completing.
            
            .. attribute:: ciscopingserialnumber  <key>
            
            	Object which specifies a unique entry in the ciscoPingTable.  A management station wishing to initiate a ping operation should use a pseudo\-random value for this object when creating or modifying an instance of a ciscoPingEntry. The RowStatus semantics of the ciscoPingEntryStatus object will prevent access conflicts
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: ciscopingaddress
            
            	The address of the device to be pinged. An instance of this object cannot be created until the associated instance of ciscoPingProtocol is created
            	**type**\:  str
            
            .. attribute:: ciscopingavgrtt
            
            	The average round trip time of all the packets that have been sent in this sequence.  This object will not be created until the first ping response in a sequence is received
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: milliseconds
            
            .. attribute:: ciscopingcompleted
            
            	Set to true when all the packets in this sequence have been either responded to or timed out
            	**type**\:  bool
            
            .. attribute:: ciscopingdelay
            
            	Specifies the minimum amount of time to wait before sending the next packet in a sequence after receiving a response or declaring a timeout for a previous packet.  The actual delay may be greater due to internal task scheduling
            	**type**\:  int
            
            	**range:** 0..3600000
            
            	**units**\: milliseconds
            
            .. attribute:: ciscopingentryowner
            
            	The entity that configured this entry
            	**type**\:  str
            
            .. attribute:: ciscopingentrystatus
            
            	The status of this table entry.  Once the entry status is set to active, the associate entry cannot be modified until the sequence completes (ciscoPingCompleted is true)
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: ciscopingmaxrtt
            
            	The maximum round trip time of all the packets that have been sent in this sequence.  This object will not be created until the first ping response in a sequence is received
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: milliseconds
            
            .. attribute:: ciscopingminrtt
            
            	The minimum round trip time of all the packets that have been sent in this sequence.  This object will not be created until the first ping response in a sequence is received
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: milliseconds
            
            .. attribute:: ciscopingpacketcount
            
            	Specifies the number of ping packets to send to the target in this sequence
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: ciscopingpacketsize
            
            	Specifies the size of ping packets to send to the target in this sequence.  The lower and upper boundaries of this object are protocol\-dependent. An instance of this object cannot be modified unless the associated instance of ciscoPingProtocol has been created (so as to allow protocol\-specific range checking on the new value)
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: ciscopingpackettimeout
            
            	Specifies the amount of time to wait for a response to a transmitted packet before declaring the packet 'dropped.'
            	**type**\:  int
            
            	**range:** 0..3600000
            
            	**units**\: milliseconds
            
            .. attribute:: ciscopingprotocol
            
            	The protocol to use. Once an instance of this object is created, its value can not be changed
            	**type**\:   :py:class:`Cisconetworkprotocol <ydk.models.cisco_ios_xe.CISCO_TC.Cisconetworkprotocol>`
            
            .. attribute:: ciscopingreceivedpackets
            
            	The number of ping packets that have been received from the target in this sequence
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscopingsentpackets
            
            	The number of ping packets that have been sent to the target in this sequence
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscopingtraponcompletion
            
            	Specifies whether or not a ciscoPingCompletion trap should be issued on completion of the sequence of pings.  If such a trap is desired, it is the responsibility of the management entity to ensure that the SNMP administrative model is configured in such a way as to allow the trap to be delivered
            	**type**\:  bool
            
            .. attribute:: ciscopingvrfname
            
            	This field is used to specify the VPN name in  which the ping will be used. For regular ping this field should not be configured. The agent will use this field to identify the VPN routing Table for  this ping. This is the same ascii string used in  the CLI to refer to this VPN. 
            	**type**\:  str
            
            	**length:** 0..32
            
            

            """

            _prefix = 'CISCO-PING-MIB'
            _revision = '2001-08-28'

            def __init__(self):
                super(CiscoPingMib.Ciscopingtable.Ciscopingentry, self).__init__()

                self.yang_name = "ciscoPingEntry"
                self.yang_parent_name = "ciscoPingTable"

                self.ciscopingserialnumber = YLeaf(YType.int32, "ciscoPingSerialNumber")

                self.ciscopingaddress = YLeaf(YType.str, "ciscoPingAddress")

                self.ciscopingavgrtt = YLeaf(YType.int32, "ciscoPingAvgRtt")

                self.ciscopingcompleted = YLeaf(YType.boolean, "ciscoPingCompleted")

                self.ciscopingdelay = YLeaf(YType.int32, "ciscoPingDelay")

                self.ciscopingentryowner = YLeaf(YType.str, "ciscoPingEntryOwner")

                self.ciscopingentrystatus = YLeaf(YType.enumeration, "ciscoPingEntryStatus")

                self.ciscopingmaxrtt = YLeaf(YType.int32, "ciscoPingMaxRtt")

                self.ciscopingminrtt = YLeaf(YType.int32, "ciscoPingMinRtt")

                self.ciscopingpacketcount = YLeaf(YType.int32, "ciscoPingPacketCount")

                self.ciscopingpacketsize = YLeaf(YType.int32, "ciscoPingPacketSize")

                self.ciscopingpackettimeout = YLeaf(YType.int32, "ciscoPingPacketTimeout")

                self.ciscopingprotocol = YLeaf(YType.enumeration, "ciscoPingProtocol")

                self.ciscopingreceivedpackets = YLeaf(YType.uint32, "ciscoPingReceivedPackets")

                self.ciscopingsentpackets = YLeaf(YType.uint32, "ciscoPingSentPackets")

                self.ciscopingtraponcompletion = YLeaf(YType.boolean, "ciscoPingTrapOnCompletion")

                self.ciscopingvrfname = YLeaf(YType.str, "ciscoPingVrfName")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ciscopingserialnumber",
                                "ciscopingaddress",
                                "ciscopingavgrtt",
                                "ciscopingcompleted",
                                "ciscopingdelay",
                                "ciscopingentryowner",
                                "ciscopingentrystatus",
                                "ciscopingmaxrtt",
                                "ciscopingminrtt",
                                "ciscopingpacketcount",
                                "ciscopingpacketsize",
                                "ciscopingpackettimeout",
                                "ciscopingprotocol",
                                "ciscopingreceivedpackets",
                                "ciscopingsentpackets",
                                "ciscopingtraponcompletion",
                                "ciscopingvrfname") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoPingMib.Ciscopingtable.Ciscopingentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoPingMib.Ciscopingtable.Ciscopingentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ciscopingserialnumber.is_set or
                    self.ciscopingaddress.is_set or
                    self.ciscopingavgrtt.is_set or
                    self.ciscopingcompleted.is_set or
                    self.ciscopingdelay.is_set or
                    self.ciscopingentryowner.is_set or
                    self.ciscopingentrystatus.is_set or
                    self.ciscopingmaxrtt.is_set or
                    self.ciscopingminrtt.is_set or
                    self.ciscopingpacketcount.is_set or
                    self.ciscopingpacketsize.is_set or
                    self.ciscopingpackettimeout.is_set or
                    self.ciscopingprotocol.is_set or
                    self.ciscopingreceivedpackets.is_set or
                    self.ciscopingsentpackets.is_set or
                    self.ciscopingtraponcompletion.is_set or
                    self.ciscopingvrfname.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ciscopingserialnumber.yfilter != YFilter.not_set or
                    self.ciscopingaddress.yfilter != YFilter.not_set or
                    self.ciscopingavgrtt.yfilter != YFilter.not_set or
                    self.ciscopingcompleted.yfilter != YFilter.not_set or
                    self.ciscopingdelay.yfilter != YFilter.not_set or
                    self.ciscopingentryowner.yfilter != YFilter.not_set or
                    self.ciscopingentrystatus.yfilter != YFilter.not_set or
                    self.ciscopingmaxrtt.yfilter != YFilter.not_set or
                    self.ciscopingminrtt.yfilter != YFilter.not_set or
                    self.ciscopingpacketcount.yfilter != YFilter.not_set or
                    self.ciscopingpacketsize.yfilter != YFilter.not_set or
                    self.ciscopingpackettimeout.yfilter != YFilter.not_set or
                    self.ciscopingprotocol.yfilter != YFilter.not_set or
                    self.ciscopingreceivedpackets.yfilter != YFilter.not_set or
                    self.ciscopingsentpackets.yfilter != YFilter.not_set or
                    self.ciscopingtraponcompletion.yfilter != YFilter.not_set or
                    self.ciscopingvrfname.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ciscoPingEntry" + "[ciscoPingSerialNumber='" + self.ciscopingserialnumber.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-PING-MIB:CISCO-PING-MIB/ciscoPingTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ciscopingserialnumber.is_set or self.ciscopingserialnumber.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscopingserialnumber.get_name_leafdata())
                if (self.ciscopingaddress.is_set or self.ciscopingaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscopingaddress.get_name_leafdata())
                if (self.ciscopingavgrtt.is_set or self.ciscopingavgrtt.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscopingavgrtt.get_name_leafdata())
                if (self.ciscopingcompleted.is_set or self.ciscopingcompleted.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscopingcompleted.get_name_leafdata())
                if (self.ciscopingdelay.is_set or self.ciscopingdelay.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscopingdelay.get_name_leafdata())
                if (self.ciscopingentryowner.is_set or self.ciscopingentryowner.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscopingentryowner.get_name_leafdata())
                if (self.ciscopingentrystatus.is_set or self.ciscopingentrystatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscopingentrystatus.get_name_leafdata())
                if (self.ciscopingmaxrtt.is_set or self.ciscopingmaxrtt.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscopingmaxrtt.get_name_leafdata())
                if (self.ciscopingminrtt.is_set or self.ciscopingminrtt.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscopingminrtt.get_name_leafdata())
                if (self.ciscopingpacketcount.is_set or self.ciscopingpacketcount.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscopingpacketcount.get_name_leafdata())
                if (self.ciscopingpacketsize.is_set or self.ciscopingpacketsize.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscopingpacketsize.get_name_leafdata())
                if (self.ciscopingpackettimeout.is_set or self.ciscopingpackettimeout.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscopingpackettimeout.get_name_leafdata())
                if (self.ciscopingprotocol.is_set or self.ciscopingprotocol.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscopingprotocol.get_name_leafdata())
                if (self.ciscopingreceivedpackets.is_set or self.ciscopingreceivedpackets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscopingreceivedpackets.get_name_leafdata())
                if (self.ciscopingsentpackets.is_set or self.ciscopingsentpackets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscopingsentpackets.get_name_leafdata())
                if (self.ciscopingtraponcompletion.is_set or self.ciscopingtraponcompletion.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscopingtraponcompletion.get_name_leafdata())
                if (self.ciscopingvrfname.is_set or self.ciscopingvrfname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscopingvrfname.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ciscoPingSerialNumber" or name == "ciscoPingAddress" or name == "ciscoPingAvgRtt" or name == "ciscoPingCompleted" or name == "ciscoPingDelay" or name == "ciscoPingEntryOwner" or name == "ciscoPingEntryStatus" or name == "ciscoPingMaxRtt" or name == "ciscoPingMinRtt" or name == "ciscoPingPacketCount" or name == "ciscoPingPacketSize" or name == "ciscoPingPacketTimeout" or name == "ciscoPingProtocol" or name == "ciscoPingReceivedPackets" or name == "ciscoPingSentPackets" or name == "ciscoPingTrapOnCompletion" or name == "ciscoPingVrfName"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ciscoPingSerialNumber"):
                    self.ciscopingserialnumber = value
                    self.ciscopingserialnumber.value_namespace = name_space
                    self.ciscopingserialnumber.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoPingAddress"):
                    self.ciscopingaddress = value
                    self.ciscopingaddress.value_namespace = name_space
                    self.ciscopingaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoPingAvgRtt"):
                    self.ciscopingavgrtt = value
                    self.ciscopingavgrtt.value_namespace = name_space
                    self.ciscopingavgrtt.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoPingCompleted"):
                    self.ciscopingcompleted = value
                    self.ciscopingcompleted.value_namespace = name_space
                    self.ciscopingcompleted.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoPingDelay"):
                    self.ciscopingdelay = value
                    self.ciscopingdelay.value_namespace = name_space
                    self.ciscopingdelay.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoPingEntryOwner"):
                    self.ciscopingentryowner = value
                    self.ciscopingentryowner.value_namespace = name_space
                    self.ciscopingentryowner.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoPingEntryStatus"):
                    self.ciscopingentrystatus = value
                    self.ciscopingentrystatus.value_namespace = name_space
                    self.ciscopingentrystatus.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoPingMaxRtt"):
                    self.ciscopingmaxrtt = value
                    self.ciscopingmaxrtt.value_namespace = name_space
                    self.ciscopingmaxrtt.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoPingMinRtt"):
                    self.ciscopingminrtt = value
                    self.ciscopingminrtt.value_namespace = name_space
                    self.ciscopingminrtt.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoPingPacketCount"):
                    self.ciscopingpacketcount = value
                    self.ciscopingpacketcount.value_namespace = name_space
                    self.ciscopingpacketcount.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoPingPacketSize"):
                    self.ciscopingpacketsize = value
                    self.ciscopingpacketsize.value_namespace = name_space
                    self.ciscopingpacketsize.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoPingPacketTimeout"):
                    self.ciscopingpackettimeout = value
                    self.ciscopingpackettimeout.value_namespace = name_space
                    self.ciscopingpackettimeout.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoPingProtocol"):
                    self.ciscopingprotocol = value
                    self.ciscopingprotocol.value_namespace = name_space
                    self.ciscopingprotocol.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoPingReceivedPackets"):
                    self.ciscopingreceivedpackets = value
                    self.ciscopingreceivedpackets.value_namespace = name_space
                    self.ciscopingreceivedpackets.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoPingSentPackets"):
                    self.ciscopingsentpackets = value
                    self.ciscopingsentpackets.value_namespace = name_space
                    self.ciscopingsentpackets.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoPingTrapOnCompletion"):
                    self.ciscopingtraponcompletion = value
                    self.ciscopingtraponcompletion.value_namespace = name_space
                    self.ciscopingtraponcompletion.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoPingVrfName"):
                    self.ciscopingvrfname = value
                    self.ciscopingvrfname.value_namespace = name_space
                    self.ciscopingvrfname.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ciscopingentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ciscopingentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ciscoPingTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-PING-MIB:CISCO-PING-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ciscoPingEntry"):
                for c in self.ciscopingentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoPingMib.Ciscopingtable.Ciscopingentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ciscopingentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ciscoPingEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (self.ciscopingtable is not None and self.ciscopingtable.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.ciscopingtable is not None and self.ciscopingtable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "CISCO-PING-MIB:CISCO-PING-MIB" + path_buffer

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

        if (child_yang_name == "ciscoPingTable"):
            if (self.ciscopingtable is None):
                self.ciscopingtable = CiscoPingMib.Ciscopingtable()
                self.ciscopingtable.parent = self
                self._children_name_map["ciscopingtable"] = "ciscoPingTable"
            return self.ciscopingtable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "ciscoPingTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CiscoPingMib()
        return self._top_entity

