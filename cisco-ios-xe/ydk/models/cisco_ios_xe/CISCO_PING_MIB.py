""" CISCO_PING_MIB 

Modified description of ciscoPingAddress object.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class CiscoPingMib(object):
    """
    
    
    .. attribute:: ciscopingtable
    
    	A table of ping request entries
    	**type**\:   :py:class:`Ciscopingtable <ydk.models.cisco_ios_xe.CISCO_PING_MIB.CiscoPingMib.Ciscopingtable>`
    
    

    """

    _prefix = 'CISCO-PING-MIB'
    _revision = '2001-08-28'

    def __init__(self):
        self.ciscopingtable = CiscoPingMib.Ciscopingtable()
        self.ciscopingtable.parent = self


    class Ciscopingtable(object):
        """
        A table of ping request entries.
        
        .. attribute:: ciscopingentry
        
        	A ping request entry.  A management station wishing to create an entry should first generate a pseudo\-random serial number to be used as the index to this sparse table.  The station should then create the associated instance of the row status and row owner objects.  It must also, either in the same or in successive PDUs, create the associated instance of the protocol and address objects.  It should also modify the default values for the other configuration objects if the defaults are not appropriate.  Once the appropriate instance of all the configuration objects have been created, either by an explicit SNMP set request or by default, the row status should be set to active to initiate the request.  Note that this entire procedure may be initiated via a single set request which specifies a row status of createAndGo as well as specifies valid values for the non\-defaulted configuration objects.  Once the ping sequence has been activated, it cannot be stopped \-\- it will run until the configured number of packets have been sent.  Once the sequence completes, the management station should retrieve the values of the status objects of interest, and should then delete the entry.  In order to prevent old entries from clogging the table, entries will be aged out, but an entry will never be deleted within 5 minutes of completing
        	**type**\: list of    :py:class:`Ciscopingentry <ydk.models.cisco_ios_xe.CISCO_PING_MIB.CiscoPingMib.Ciscopingtable.Ciscopingentry>`
        
        

        """

        _prefix = 'CISCO-PING-MIB'
        _revision = '2001-08-28'

        def __init__(self):
            self.parent = None
            self.ciscopingentry = YList()
            self.ciscopingentry.parent = self
            self.ciscopingentry.name = 'ciscopingentry'


        class Ciscopingentry(object):
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
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
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
            	**type**\:   :py:class:`CisconetworkprotocolEnum <ydk.models.cisco_ios_xe.CISCO_TC.CisconetworkprotocolEnum>`
            
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
                self.parent = None
                self.ciscopingserialnumber = None
                self.ciscopingaddress = None
                self.ciscopingavgrtt = None
                self.ciscopingcompleted = None
                self.ciscopingdelay = None
                self.ciscopingentryowner = None
                self.ciscopingentrystatus = None
                self.ciscopingmaxrtt = None
                self.ciscopingminrtt = None
                self.ciscopingpacketcount = None
                self.ciscopingpacketsize = None
                self.ciscopingpackettimeout = None
                self.ciscopingprotocol = None
                self.ciscopingreceivedpackets = None
                self.ciscopingsentpackets = None
                self.ciscopingtraponcompletion = None
                self.ciscopingvrfname = None

            @property
            def _common_path(self):
                if self.ciscopingserialnumber is None:
                    raise YPYModelError('Key property ciscopingserialnumber is None')

                return '/CISCO-PING-MIB:CISCO-PING-MIB/CISCO-PING-MIB:ciscoPingTable/CISCO-PING-MIB:ciscoPingEntry[CISCO-PING-MIB:ciscoPingSerialNumber = ' + str(self.ciscopingserialnumber) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ciscopingserialnumber is not None:
                    return True

                if self.ciscopingaddress is not None:
                    return True

                if self.ciscopingavgrtt is not None:
                    return True

                if self.ciscopingcompleted is not None:
                    return True

                if self.ciscopingdelay is not None:
                    return True

                if self.ciscopingentryowner is not None:
                    return True

                if self.ciscopingentrystatus is not None:
                    return True

                if self.ciscopingmaxrtt is not None:
                    return True

                if self.ciscopingminrtt is not None:
                    return True

                if self.ciscopingpacketcount is not None:
                    return True

                if self.ciscopingpacketsize is not None:
                    return True

                if self.ciscopingpackettimeout is not None:
                    return True

                if self.ciscopingprotocol is not None:
                    return True

                if self.ciscopingreceivedpackets is not None:
                    return True

                if self.ciscopingsentpackets is not None:
                    return True

                if self.ciscopingtraponcompletion is not None:
                    return True

                if self.ciscopingvrfname is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_PING_MIB as meta
                return meta._meta_table['CiscoPingMib.Ciscopingtable.Ciscopingentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-PING-MIB:CISCO-PING-MIB/CISCO-PING-MIB:ciscoPingTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.ciscopingentry is not None:
                for child_ref in self.ciscopingentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_PING_MIB as meta
            return meta._meta_table['CiscoPingMib.Ciscopingtable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-PING-MIB:CISCO-PING-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.ciscopingtable is not None and self.ciscopingtable._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_PING_MIB as meta
        return meta._meta_table['CiscoPingMib']['meta_info']


