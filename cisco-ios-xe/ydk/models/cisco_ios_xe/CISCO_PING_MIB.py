""" CISCO_PING_MIB 

Modified description of ciscoPingAddress object.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CISCOPINGMIB(Entity):
    """
    
    
    .. attribute:: ciscopingtable
    
    	A table of ping request entries
    	**type**\:  :py:class:`Ciscopingtable <ydk.models.cisco_ios_xe.CISCO_PING_MIB.CISCOPINGMIB.Ciscopingtable>`
    
    

    """

    _prefix = 'CISCO-PING-MIB'
    _revision = '2001-08-28'

    def __init__(self):
        super(CISCOPINGMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-PING-MIB"
        self.yang_parent_name = "CISCO-PING-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("ciscoPingTable", ("ciscopingtable", CISCOPINGMIB.Ciscopingtable))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.ciscopingtable = CISCOPINGMIB.Ciscopingtable()
        self.ciscopingtable.parent = self
        self._children_name_map["ciscopingtable"] = "ciscoPingTable"
        self._children_yang_names.add("ciscoPingTable")
        self._segment_path = lambda: "CISCO-PING-MIB:CISCO-PING-MIB"


    class Ciscopingtable(Entity):
        """
        A table of ping request entries.
        
        .. attribute:: ciscopingentry
        
        	A ping request entry.  A management station wishing to create an entry should first generate a pseudo\-random serial number to be used as the index to this sparse table.  The station should then create the associated instance of the row status and row owner objects.  It must also, either in the same or in successive PDUs, create the associated instance of the protocol and address objects.  It should also modify the default values for the other configuration objects if the defaults are not appropriate.  Once the appropriate instance of all the configuration objects have been created, either by an explicit SNMP set request or by default, the row status should be set to active to initiate the request.  Note that this entire procedure may be initiated via a single set request which specifies a row status of createAndGo as well as specifies valid values for the non\-defaulted configuration objects.  Once the ping sequence has been activated, it cannot be stopped \-\- it will run until the configured number of packets have been sent.  Once the sequence completes, the management station should retrieve the values of the status objects of interest, and should then delete the entry.  In order to prevent old entries from clogging the table, entries will be aged out, but an entry will never be deleted within 5 minutes of completing
        	**type**\: list of  		 :py:class:`Ciscopingentry <ydk.models.cisco_ios_xe.CISCO_PING_MIB.CISCOPINGMIB.Ciscopingtable.Ciscopingentry>`
        
        

        """

        _prefix = 'CISCO-PING-MIB'
        _revision = '2001-08-28'

        def __init__(self):
            super(CISCOPINGMIB.Ciscopingtable, self).__init__()

            self.yang_name = "ciscoPingTable"
            self.yang_parent_name = "CISCO-PING-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("ciscoPingEntry", ("ciscopingentry", CISCOPINGMIB.Ciscopingtable.Ciscopingentry))])
            self._leafs = OrderedDict()

            self.ciscopingentry = YList(self)
            self._segment_path = lambda: "ciscoPingTable"
            self._absolute_path = lambda: "CISCO-PING-MIB:CISCO-PING-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOPINGMIB.Ciscopingtable, [], name, value)


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
            
            .. attribute:: ciscopingserialnumber  (key)
            
            	Object which specifies a unique entry in the ciscoPingTable.  A management station wishing to initiate a ping operation should use a pseudo\-random value for this object when creating or modifying an instance of a ciscoPingEntry. The RowStatus semantics of the ciscoPingEntryStatus object will prevent access conflicts
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: ciscopingprotocol
            
            	The protocol to use. Once an instance of this object is created, its value can not be changed
            	**type**\:  :py:class:`CiscoNetworkProtocol <ydk.models.cisco_ios_xe.CISCO_TC.CiscoNetworkProtocol>`
            
            .. attribute:: ciscopingaddress
            
            	The address of the device to be pinged. An instance of this object cannot be created until the associated instance of ciscoPingProtocol is created
            	**type**\: str
            
            .. attribute:: ciscopingpacketcount
            
            	Specifies the number of ping packets to send to the target in this sequence
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: ciscopingpacketsize
            
            	Specifies the size of ping packets to send to the target in this sequence.  The lower and upper boundaries of this object are protocol\-dependent. An instance of this object cannot be modified unless the associated instance of ciscoPingProtocol has been created (so as to allow protocol\-specific range checking on the new value)
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: ciscopingpackettimeout
            
            	Specifies the amount of time to wait for a response to a transmitted packet before declaring the packet 'dropped.'
            	**type**\: int
            
            	**range:** 0..3600000
            
            	**units**\: milliseconds
            
            .. attribute:: ciscopingdelay
            
            	Specifies the minimum amount of time to wait before sending the next packet in a sequence after receiving a response or declaring a timeout for a previous packet.  The actual delay may be greater due to internal task scheduling
            	**type**\: int
            
            	**range:** 0..3600000
            
            	**units**\: milliseconds
            
            .. attribute:: ciscopingtraponcompletion
            
            	Specifies whether or not a ciscoPingCompletion trap should be issued on completion of the sequence of pings.  If such a trap is desired, it is the responsibility of the management entity to ensure that the SNMP administrative model is configured in such a way as to allow the trap to be delivered
            	**type**\: bool
            
            .. attribute:: ciscopingsentpackets
            
            	The number of ping packets that have been sent to the target in this sequence
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscopingreceivedpackets
            
            	The number of ping packets that have been received from the target in this sequence
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscopingminrtt
            
            	The minimum round trip time of all the packets that have been sent in this sequence.  This object will not be created until the first ping response in a sequence is received
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: milliseconds
            
            .. attribute:: ciscopingavgrtt
            
            	The average round trip time of all the packets that have been sent in this sequence.  This object will not be created until the first ping response in a sequence is received
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: milliseconds
            
            .. attribute:: ciscopingmaxrtt
            
            	The maximum round trip time of all the packets that have been sent in this sequence.  This object will not be created until the first ping response in a sequence is received
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: milliseconds
            
            .. attribute:: ciscopingcompleted
            
            	Set to true when all the packets in this sequence have been either responded to or timed out
            	**type**\: bool
            
            .. attribute:: ciscopingentryowner
            
            	The entity that configured this entry
            	**type**\: str
            
            .. attribute:: ciscopingentrystatus
            
            	The status of this table entry.  Once the entry status is set to active, the associate entry cannot be modified until the sequence completes (ciscoPingCompleted is true)
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            .. attribute:: ciscopingvrfname
            
            	This field is used to specify the VPN name in  which the ping will be used. For regular ping this field should not be configured. The agent will use this field to identify the VPN routing Table for  this ping. This is the same ascii string used in  the CLI to refer to this VPN. 
            	**type**\: str
            
            	**length:** 0..32
            
            

            """

            _prefix = 'CISCO-PING-MIB'
            _revision = '2001-08-28'

            def __init__(self):
                super(CISCOPINGMIB.Ciscopingtable.Ciscopingentry, self).__init__()

                self.yang_name = "ciscoPingEntry"
                self.yang_parent_name = "ciscoPingTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ciscopingserialnumber']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ciscopingserialnumber', YLeaf(YType.int32, 'ciscoPingSerialNumber')),
                    ('ciscopingprotocol', YLeaf(YType.enumeration, 'ciscoPingProtocol')),
                    ('ciscopingaddress', YLeaf(YType.str, 'ciscoPingAddress')),
                    ('ciscopingpacketcount', YLeaf(YType.int32, 'ciscoPingPacketCount')),
                    ('ciscopingpacketsize', YLeaf(YType.int32, 'ciscoPingPacketSize')),
                    ('ciscopingpackettimeout', YLeaf(YType.int32, 'ciscoPingPacketTimeout')),
                    ('ciscopingdelay', YLeaf(YType.int32, 'ciscoPingDelay')),
                    ('ciscopingtraponcompletion', YLeaf(YType.boolean, 'ciscoPingTrapOnCompletion')),
                    ('ciscopingsentpackets', YLeaf(YType.uint32, 'ciscoPingSentPackets')),
                    ('ciscopingreceivedpackets', YLeaf(YType.uint32, 'ciscoPingReceivedPackets')),
                    ('ciscopingminrtt', YLeaf(YType.int32, 'ciscoPingMinRtt')),
                    ('ciscopingavgrtt', YLeaf(YType.int32, 'ciscoPingAvgRtt')),
                    ('ciscopingmaxrtt', YLeaf(YType.int32, 'ciscoPingMaxRtt')),
                    ('ciscopingcompleted', YLeaf(YType.boolean, 'ciscoPingCompleted')),
                    ('ciscopingentryowner', YLeaf(YType.str, 'ciscoPingEntryOwner')),
                    ('ciscopingentrystatus', YLeaf(YType.enumeration, 'ciscoPingEntryStatus')),
                    ('ciscopingvrfname', YLeaf(YType.str, 'ciscoPingVrfName')),
                ])
                self.ciscopingserialnumber = None
                self.ciscopingprotocol = None
                self.ciscopingaddress = None
                self.ciscopingpacketcount = None
                self.ciscopingpacketsize = None
                self.ciscopingpackettimeout = None
                self.ciscopingdelay = None
                self.ciscopingtraponcompletion = None
                self.ciscopingsentpackets = None
                self.ciscopingreceivedpackets = None
                self.ciscopingminrtt = None
                self.ciscopingavgrtt = None
                self.ciscopingmaxrtt = None
                self.ciscopingcompleted = None
                self.ciscopingentryowner = None
                self.ciscopingentrystatus = None
                self.ciscopingvrfname = None
                self._segment_path = lambda: "ciscoPingEntry" + "[ciscoPingSerialNumber='" + str(self.ciscopingserialnumber) + "']"
                self._absolute_path = lambda: "CISCO-PING-MIB:CISCO-PING-MIB/ciscoPingTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOPINGMIB.Ciscopingtable.Ciscopingentry, ['ciscopingserialnumber', 'ciscopingprotocol', 'ciscopingaddress', 'ciscopingpacketcount', 'ciscopingpacketsize', 'ciscopingpackettimeout', 'ciscopingdelay', 'ciscopingtraponcompletion', 'ciscopingsentpackets', 'ciscopingreceivedpackets', 'ciscopingminrtt', 'ciscopingavgrtt', 'ciscopingmaxrtt', 'ciscopingcompleted', 'ciscopingentryowner', 'ciscopingentrystatus', 'ciscopingvrfname'], name, value)

    def clone_ptr(self):
        self._top_entity = CISCOPINGMIB()
        return self._top_entity

