""" CISCO_IPSLA_ECHO_MIB 

This MIB module defines the templates for IP SLA operations of
ICMP echo, UDP echo and TCP connect.

The ICMP echo operation measures end\-to\-end response time between 
a Cisco router and any IP enabled device by computing the time
taken between sending an ICMP echo request message to the 
destination and receiving an ICMP echo reply.


The UDP echo operation measures end\-to\-end response time between 
a Cisco router and any IP enabled device by computing the time
taken between sending an UDP echo request message to the 
destination and receiving an UDP echo reply.

The TCP connect operation measures end\-to\-end response time between 
a Cisco router and any IP enabled device by computing the time
taken to perform a TCP connect operation.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class CISCOIPSLAECHOMIB(Entity):
    """
    
    
    .. attribute:: cipslaicmpechotmpltable
    
    	A table that contains ICMP echo template definitions
    	**type**\:  :py:class:`CipslaIcmpEchoTmplTable <ydk.models.cisco_ios_xe.CISCO_IPSLA_ECHO_MIB.CISCOIPSLAECHOMIB.CipslaIcmpEchoTmplTable>`
    
    .. attribute:: cipslaudpechotmpltable
    
    	A table that contains UDP echo template specific definitions
    	**type**\:  :py:class:`CipslaUdpEchoTmplTable <ydk.models.cisco_ios_xe.CISCO_IPSLA_ECHO_MIB.CISCOIPSLAECHOMIB.CipslaUdpEchoTmplTable>`
    
    .. attribute:: cipslatcpconntmpltable
    
    	A table that contains TCP connect template specific definitions
    	**type**\:  :py:class:`CipslaTcpConnTmplTable <ydk.models.cisco_ios_xe.CISCO_IPSLA_ECHO_MIB.CISCOIPSLAECHOMIB.CipslaTcpConnTmplTable>`
    
    

    """

    _prefix = 'CISCO-IPSLA-ECHO-MIB'
    _revision = '2007-08-16'

    def __init__(self):
        super(CISCOIPSLAECHOMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-IPSLA-ECHO-MIB"
        self.yang_parent_name = "CISCO-IPSLA-ECHO-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("cipslaIcmpEchoTmplTable", ("cipslaicmpechotmpltable", CISCOIPSLAECHOMIB.CipslaIcmpEchoTmplTable)), ("cipslaUdpEchoTmplTable", ("cipslaudpechotmpltable", CISCOIPSLAECHOMIB.CipslaUdpEchoTmplTable)), ("cipslaTcpConnTmplTable", ("cipslatcpconntmpltable", CISCOIPSLAECHOMIB.CipslaTcpConnTmplTable))])
        self._leafs = OrderedDict()

        self.cipslaicmpechotmpltable = CISCOIPSLAECHOMIB.CipslaIcmpEchoTmplTable()
        self.cipslaicmpechotmpltable.parent = self
        self._children_name_map["cipslaicmpechotmpltable"] = "cipslaIcmpEchoTmplTable"

        self.cipslaudpechotmpltable = CISCOIPSLAECHOMIB.CipslaUdpEchoTmplTable()
        self.cipslaudpechotmpltable.parent = self
        self._children_name_map["cipslaudpechotmpltable"] = "cipslaUdpEchoTmplTable"

        self.cipslatcpconntmpltable = CISCOIPSLAECHOMIB.CipslaTcpConnTmplTable()
        self.cipslatcpconntmpltable.parent = self
        self._children_name_map["cipslatcpconntmpltable"] = "cipslaTcpConnTmplTable"
        self._segment_path = lambda: "CISCO-IPSLA-ECHO-MIB:CISCO-IPSLA-ECHO-MIB"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(CISCOIPSLAECHOMIB, [], name, value)


    class CipslaIcmpEchoTmplTable(Entity):
        """
        A table that contains ICMP echo template definitions.
        
        .. attribute:: cipslaicmpechotmplentry
        
        	A row entry representing an IPSLA ICMP echo template
        	**type**\: list of  		 :py:class:`CipslaIcmpEchoTmplEntry <ydk.models.cisco_ios_xe.CISCO_IPSLA_ECHO_MIB.CISCOIPSLAECHOMIB.CipslaIcmpEchoTmplTable.CipslaIcmpEchoTmplEntry>`
        
        

        """

        _prefix = 'CISCO-IPSLA-ECHO-MIB'
        _revision = '2007-08-16'

        def __init__(self):
            super(CISCOIPSLAECHOMIB.CipslaIcmpEchoTmplTable, self).__init__()

            self.yang_name = "cipslaIcmpEchoTmplTable"
            self.yang_parent_name = "CISCO-IPSLA-ECHO-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cipslaIcmpEchoTmplEntry", ("cipslaicmpechotmplentry", CISCOIPSLAECHOMIB.CipslaIcmpEchoTmplTable.CipslaIcmpEchoTmplEntry))])
            self._leafs = OrderedDict()

            self.cipslaicmpechotmplentry = YList(self)
            self._segment_path = lambda: "cipslaIcmpEchoTmplTable"
            self._absolute_path = lambda: "CISCO-IPSLA-ECHO-MIB:CISCO-IPSLA-ECHO-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIPSLAECHOMIB.CipslaIcmpEchoTmplTable, [], name, value)


        class CipslaIcmpEchoTmplEntry(Entity):
            """
            A row entry representing an IPSLA ICMP echo template.
            
            .. attribute:: cipslaicmpechotmplname  (key)
            
            	This field is used to specify the ICMP echo template name
            	**type**\: str
            
            	**length:** 1..64
            
            .. attribute:: cipslaicmpechotmpldescription
            
            	This field is used to provide description for the ICMP echo template
            	**type**\: str
            
            	**length:** 0..128
            
            .. attribute:: cipslaicmpechotmplsrcaddrtype
            
            	An enumerated value which specifies the IP address type of the source. It must be used along with the cipslaIcmpEchoTmplSrcAddr object
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            .. attribute:: cipslaicmpechotmplsrcaddr
            
            	A string which specifies the IP address of the source
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: cipslaicmpechotmpltimeout
            
            	Specifies the duration to wait for a IP SLA operation completion.   For connection oriented protocols, this may cause the connection to be closed by the operation.  Once closed, it will be assumed that the connection reestablishment will be performed.  To prevent unwanted closure of connections, be sure to set this value to a realistic connection timeout
            	**type**\: int
            
            	**range:** 0..604800000
            
            	**units**\: milliseconds
            
            .. attribute:: cipslaicmpechotmplverifydata
            
            	When set to true, the resulting data in each IP SLA operation is compared with the expected data.  This includes checking header information (if possible) and exact packet size
            	**type**\: bool
            
            .. attribute:: cipslaicmpechotmplreqdatasize
            
            	This object represents the number of octets to be placed into the ARR Data portion of the request message, when using SNA protocols.  For non\-ARR protocols' IP SLA request/responses, this value represents the native payload size.  REMEMBER\:  The ARR Header overhead is not included            in this value
            	**type**\: int
            
            	**range:** 0..16384
            
            	**units**\: octets
            
            .. attribute:: cipslaicmpechotmpltos
            
            	This object represents the type of service octet in an IP header
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: cipslaicmpechotmplvrfname
            
            	This field is used to specify the VRF name with which the IP SLA operation will be used. For regular IP SLA operation this field should not be configured. The agent will use this field to identify the VRF routing table for this operation
            	**type**\: str
            
            	**length:** 0..32
            
            .. attribute:: cipslaicmpechotmplthreshold
            
            	This object defines an administrative threshold limit. If the IP SLA operation time exceeds this limit and if the condition specified in cipslaIcmpEchoTmplHistFilter is satisfied, one threshold crossing occurrence will be counted
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**units**\: milliseconds
            
            .. attribute:: cipslaicmpechotmplhistlives
            
            	The maximum number of history lives to record.  A life is defined by the countdown (or transition) to zero  by the cipslaAutoGroupScheduleLife object.  A new life is created when the same conceptual control row is restarted via the transition of the  cipslaAutoGroupScheduleLife object and its subsequent  countdown.  The value of zero will shut off all data collection
            	**type**\: int
            
            	**range:** 0..2
            
            .. attribute:: cipslaicmpechotmplhistbuckets
            
            	The maximum number of history buckets to record. This value is set to the number of operations  to keep per lifetime.  After cipslaIcmpEchoTmplHistBuckets are filled, the  oldest entries are deleted and the most recent cipslaIcmpEchoTmplHistBuckets buckets are retained
            	**type**\: int
            
            	**range:** 1..60
            
            .. attribute:: cipslaicmpechotmplhistfilter
            
            	Defines a filter for adding RTT results to the history buffer\:  none(1)          \- no history is recorded all(2)           \- the results of all completion times                     and failed completions are recorded overThreshold(3) \- the results of completion times                    over cipslaIcmpEchoTmplThreshold are                     recorded. failures(4)      \- the results of failed operations (only)                     are recorded
            	**type**\:  :py:class:`CipslaIcmpEchoTmplHistFilter <ydk.models.cisco_ios_xe.CISCO_IPSLA_ECHO_MIB.CISCOIPSLAECHOMIB.CipslaIcmpEchoTmplTable.CipslaIcmpEchoTmplEntry.CipslaIcmpEchoTmplHistFilter>`
            
            .. attribute:: cipslaicmpechotmplstatshours
            
            	The maximum number of hours for which statistics are maintained. Specifically this is the number of hourly  groups to keep before rolling over.  The value of one is not advisable because the hourly group will close and immediately be deleted before the network management station will have the opportunity to retrieve the statistics.  The value of zero will shut off data collection
            	**type**\: int
            
            	**range:** 0..25
            
            	**units**\: hours
            
            .. attribute:: cipslaicmpechotmpldistbuckets
            
            	The maximum number of statistical distribution buckets to accumulate.  Since this index does not rollover, only the first cipslaIcmpEchoTmplStatsNumDistBuckets will be kept.  The last cipslaIcmpEchoTmplStatsNumDistBucket will contain all entries from its distribution interval start point to infinity
            	**type**\: int
            
            	**range:** 1..20
            
            .. attribute:: cipslaicmpechotmpldistinterval
            
            	The statistical distribution buckets interval.  Distribution Bucket Example\:  cipslaIcmpEchoTmplDistBuckets = 5 buckets cipslaIcmpEchoTmplDistInterval = 10 milliseconds  \| Bucket 1 \| Bucket 2 \| Bucket 3 \| Bucket 4 \| Bucket 5  \| \|  0\-9 ms  \| 10\-19 ms \| 20\-29 ms \| 30\-39 ms \| 40\-Inf ms \|  Odd Example\:  cipslaIcmpEchoTmplDistBuckets = 1 buckets cipslaIcmpEchoTmplDistInterval = 10 milliseconds  \| Bucket 1  \| \|  0\-Inf ms \|  Thus, this odd example shows that the value of cipslaIcmpEchoTmplDistInterval does not apply when cipslaIcmpEchoTmplDistBuckets is one
            	**type**\: int
            
            	**range:** 1..100
            
            	**units**\: milliseconds
            
            .. attribute:: cipslaicmpechotmplstoragetype
            
            	The storage type of this conceptual row
            	**type**\:  :py:class:`StorageType <ydk.models.cisco_ios_xe.SNMPv2_TC.StorageType>`
            
            .. attribute:: cipslaicmpechotmplrowstatus
            
            	The status of the conceptual ICMP echo template control row. When the status is active, all the read\-create objects in that  row can be modified
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            

            """

            _prefix = 'CISCO-IPSLA-ECHO-MIB'
            _revision = '2007-08-16'

            def __init__(self):
                super(CISCOIPSLAECHOMIB.CipslaIcmpEchoTmplTable.CipslaIcmpEchoTmplEntry, self).__init__()

                self.yang_name = "cipslaIcmpEchoTmplEntry"
                self.yang_parent_name = "cipslaIcmpEchoTmplTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cipslaicmpechotmplname']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cipslaicmpechotmplname', (YLeaf(YType.str, 'cipslaIcmpEchoTmplName'), ['str'])),
                    ('cipslaicmpechotmpldescription', (YLeaf(YType.str, 'cipslaIcmpEchoTmplDescription'), ['str'])),
                    ('cipslaicmpechotmplsrcaddrtype', (YLeaf(YType.enumeration, 'cipslaIcmpEchoTmplSrcAddrType'), [('ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetAddressType', '')])),
                    ('cipslaicmpechotmplsrcaddr', (YLeaf(YType.str, 'cipslaIcmpEchoTmplSrcAddr'), ['str'])),
                    ('cipslaicmpechotmpltimeout', (YLeaf(YType.uint32, 'cipslaIcmpEchoTmplTimeOut'), ['int'])),
                    ('cipslaicmpechotmplverifydata', (YLeaf(YType.boolean, 'cipslaIcmpEchoTmplVerifyData'), ['bool'])),
                    ('cipslaicmpechotmplreqdatasize', (YLeaf(YType.uint32, 'cipslaIcmpEchoTmplReqDataSize'), ['int'])),
                    ('cipslaicmpechotmpltos', (YLeaf(YType.uint32, 'cipslaIcmpEchoTmplTOS'), ['int'])),
                    ('cipslaicmpechotmplvrfname', (YLeaf(YType.str, 'cipslaIcmpEchoTmplVrfName'), ['str'])),
                    ('cipslaicmpechotmplthreshold', (YLeaf(YType.uint32, 'cipslaIcmpEchoTmplThreshold'), ['int'])),
                    ('cipslaicmpechotmplhistlives', (YLeaf(YType.uint32, 'cipslaIcmpEchoTmplHistLives'), ['int'])),
                    ('cipslaicmpechotmplhistbuckets', (YLeaf(YType.uint32, 'cipslaIcmpEchoTmplHistBuckets'), ['int'])),
                    ('cipslaicmpechotmplhistfilter', (YLeaf(YType.enumeration, 'cipslaIcmpEchoTmplHistFilter'), [('ydk.models.cisco_ios_xe.CISCO_IPSLA_ECHO_MIB', 'CISCOIPSLAECHOMIB', 'CipslaIcmpEchoTmplTable.CipslaIcmpEchoTmplEntry.CipslaIcmpEchoTmplHistFilter')])),
                    ('cipslaicmpechotmplstatshours', (YLeaf(YType.uint32, 'cipslaIcmpEchoTmplStatsHours'), ['int'])),
                    ('cipslaicmpechotmpldistbuckets', (YLeaf(YType.uint32, 'cipslaIcmpEchoTmplDistBuckets'), ['int'])),
                    ('cipslaicmpechotmpldistinterval', (YLeaf(YType.uint32, 'cipslaIcmpEchoTmplDistInterval'), ['int'])),
                    ('cipslaicmpechotmplstoragetype', (YLeaf(YType.enumeration, 'cipslaIcmpEchoTmplStorageType'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'StorageType', '')])),
                    ('cipslaicmpechotmplrowstatus', (YLeaf(YType.enumeration, 'cipslaIcmpEchoTmplRowStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.cipslaicmpechotmplname = None
                self.cipslaicmpechotmpldescription = None
                self.cipslaicmpechotmplsrcaddrtype = None
                self.cipslaicmpechotmplsrcaddr = None
                self.cipslaicmpechotmpltimeout = None
                self.cipslaicmpechotmplverifydata = None
                self.cipslaicmpechotmplreqdatasize = None
                self.cipslaicmpechotmpltos = None
                self.cipslaicmpechotmplvrfname = None
                self.cipslaicmpechotmplthreshold = None
                self.cipslaicmpechotmplhistlives = None
                self.cipslaicmpechotmplhistbuckets = None
                self.cipslaicmpechotmplhistfilter = None
                self.cipslaicmpechotmplstatshours = None
                self.cipslaicmpechotmpldistbuckets = None
                self.cipslaicmpechotmpldistinterval = None
                self.cipslaicmpechotmplstoragetype = None
                self.cipslaicmpechotmplrowstatus = None
                self._segment_path = lambda: "cipslaIcmpEchoTmplEntry" + "[cipslaIcmpEchoTmplName='" + str(self.cipslaicmpechotmplname) + "']"
                self._absolute_path = lambda: "CISCO-IPSLA-ECHO-MIB:CISCO-IPSLA-ECHO-MIB/cipslaIcmpEchoTmplTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIPSLAECHOMIB.CipslaIcmpEchoTmplTable.CipslaIcmpEchoTmplEntry, ['cipslaicmpechotmplname', 'cipslaicmpechotmpldescription', 'cipslaicmpechotmplsrcaddrtype', 'cipslaicmpechotmplsrcaddr', 'cipslaicmpechotmpltimeout', 'cipslaicmpechotmplverifydata', 'cipslaicmpechotmplreqdatasize', 'cipslaicmpechotmpltos', 'cipslaicmpechotmplvrfname', 'cipslaicmpechotmplthreshold', 'cipslaicmpechotmplhistlives', 'cipslaicmpechotmplhistbuckets', 'cipslaicmpechotmplhistfilter', 'cipslaicmpechotmplstatshours', 'cipslaicmpechotmpldistbuckets', 'cipslaicmpechotmpldistinterval', 'cipslaicmpechotmplstoragetype', 'cipslaicmpechotmplrowstatus'], name, value)

            class CipslaIcmpEchoTmplHistFilter(Enum):
                """
                CipslaIcmpEchoTmplHistFilter (Enum Class)

                Defines a filter for adding RTT results to the history

                buffer\:

                none(1)          \- no history is recorded

                all(2)           \- the results of all completion times 

                                   and failed completions are recorded

                overThreshold(3) \- the results of completion times

                                   over cipslaIcmpEchoTmplThreshold are 

                                   recorded.

                failures(4)      \- the results of failed operations (only) 

                                   are recorded.

                .. data:: none = 1

                .. data:: all = 2

                .. data:: overThreshold = 3

                .. data:: failures = 4

                """

                none = Enum.YLeaf(1, "none")

                all = Enum.YLeaf(2, "all")

                overThreshold = Enum.YLeaf(3, "overThreshold")

                failures = Enum.YLeaf(4, "failures")



    class CipslaUdpEchoTmplTable(Entity):
        """
        A table that contains UDP echo template specific definitions.
        
        .. attribute:: cipslaudpechotmplentry
        
        	A row entry representing an IPSLA UDP echo template
        	**type**\: list of  		 :py:class:`CipslaUdpEchoTmplEntry <ydk.models.cisco_ios_xe.CISCO_IPSLA_ECHO_MIB.CISCOIPSLAECHOMIB.CipslaUdpEchoTmplTable.CipslaUdpEchoTmplEntry>`
        
        

        """

        _prefix = 'CISCO-IPSLA-ECHO-MIB'
        _revision = '2007-08-16'

        def __init__(self):
            super(CISCOIPSLAECHOMIB.CipslaUdpEchoTmplTable, self).__init__()

            self.yang_name = "cipslaUdpEchoTmplTable"
            self.yang_parent_name = "CISCO-IPSLA-ECHO-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cipslaUdpEchoTmplEntry", ("cipslaudpechotmplentry", CISCOIPSLAECHOMIB.CipslaUdpEchoTmplTable.CipslaUdpEchoTmplEntry))])
            self._leafs = OrderedDict()

            self.cipslaudpechotmplentry = YList(self)
            self._segment_path = lambda: "cipslaUdpEchoTmplTable"
            self._absolute_path = lambda: "CISCO-IPSLA-ECHO-MIB:CISCO-IPSLA-ECHO-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIPSLAECHOMIB.CipslaUdpEchoTmplTable, [], name, value)


        class CipslaUdpEchoTmplEntry(Entity):
            """
            A row entry representing an IPSLA UDP echo template.
            
            .. attribute:: cipslaudpechotmplname  (key)
            
            	A string which specifies the UDP echo template name
            	**type**\: str
            
            	**length:** 1..64
            
            .. attribute:: cipslaudpechotmpldescription
            
            	A string which provides description to the UDP echo template
            	**type**\: str
            
            	**length:** 0..128
            
            .. attribute:: cipslaudpechotmplcontrolenable
            
            	If this object is enabled, then the IP SLA application will send control messages to a responder, residing on the target router to respond to the data request packets being sent by the source router
            	**type**\: bool
            
            .. attribute:: cipslaudpechotmplsrcaddrtype
            
            	An enumerated value which specifies the IP address type of the source. It must be used along with the cipslaUdpEchoTmplSrcAddr object
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            .. attribute:: cipslaudpechotmplsrcaddr
            
            	A string which specifies the IP address of the source
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: cipslaudpechotmplsrcport
            
            	This object represents the source's port number. If this object is not specified, the application will get a port allocated by the system
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: cipslaudpechotmpltimeout
            
            	Specifies the duration to wait for an IP SLA operation completion.  For connection oriented protocols, this may cause the connection to be closed by the operation.  Once closed, it will be assumed that the connection reestablishment will be performed.  To prevent unwanted closure of connections, be sure to set this value to a realistic connection timeout
            	**type**\: int
            
            	**range:** 0..604800000
            
            	**units**\: milliseconds
            
            .. attribute:: cipslaudpechotmplverifydata
            
            	When set to true, the resulting data in each IP SLA operation is compared with the expected data.  This includes checking header information (if possible) and exact packet size
            	**type**\: bool
            
            .. attribute:: cipslaudpechotmplreqdatasize
            
            	This object represents the number of octets to be placed into the ARR Data portion of the request message, when using SNA protocols.  For non\-ARR protocols' RTT request/responses, this value represents the native payload size.  REMEMBER\:  The ARR Header overhead is not included            in this value
            	**type**\: int
            
            	**range:** 4..1500
            
            	**units**\: octets
            
            .. attribute:: cipslaudpechotmpltos
            
            	This object represents the type of service octet in an IP header
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: cipslaudpechotmplvrfname
            
            	This field is used to specify the VRF name with which the IP SLA operation will be used. For regular IP SLA operation this field should not be configured. The agent will use this field to identify the VRF routing Table for this operation
            	**type**\: str
            
            	**length:** 0..32
            
            .. attribute:: cipslaudpechotmplthreshold
            
            	This object defines an administrative threshold limit. If the IP SLA operation time exceeds this limit and if the condition specified in cipslaUdpEchoTmplHistFilter is  satisfied, one threshold crossing occurrence will be counted
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**units**\: milliseconds
            
            .. attribute:: cipslaudpechotmplhistlives
            
            	The maximum number of history lives to record.  A life is defined by the countdown (or transition) to zero  by the cipslaAutoGroupScheduleLife object.  A new life is created when the same conceptual control row is restarted via the transition of the  cipslaAutoGroupScheduleLife object and its subsequent  countdown.  The value of zero will shut off all data collection
            	**type**\: int
            
            	**range:** 0..2
            
            .. attribute:: cipslaudpechotmplhistbuckets
            
            	The maximum number of history buckets to record. This value should be set to the number of operations  to keep per lifetime.  After cipslaUdpEchoTmplHistBuckets are filled, the  oldest entries are deleted and the most recent cipslaUdpEchoTmplHistBuckets buckets are retained
            	**type**\: int
            
            	**range:** 1..60
            
            .. attribute:: cipslaudpechotmplhistfilter
            
            	Defines a filter for adding RTT results to the history buffer\:  none(1)          \- no history is recorded all(2)           \- the results of all completion times                     and failed completions are recorded overThreshold(3) \- the results of completion times                    over cipslaUdpEchoTmplThreshold are                     recorded. failures(4)      \- the results of failed operations (only)                     are recorded
            	**type**\:  :py:class:`CipslaUdpEchoTmplHistFilter <ydk.models.cisco_ios_xe.CISCO_IPSLA_ECHO_MIB.CISCOIPSLAECHOMIB.CipslaUdpEchoTmplTable.CipslaUdpEchoTmplEntry.CipslaUdpEchoTmplHistFilter>`
            
            .. attribute:: cipslaudpechotmplstatshours
            
            	The maximum number of hours for which statistics are maintained. Specifically this is the number of hourly  groups to keep before rolling over.  The value of one is not advisable because the hourly group will close and immediately be deleted before the network management station will have the opportunity to retrieve the statistics.  The value of zero will shut off data collection
            	**type**\: int
            
            	**range:** 0..25
            
            	**units**\: hours
            
            .. attribute:: cipslaudpechotmpldistbuckets
            
            	The maximum number of statistical distribution buckets to accumulate.  Since this index does not rollover, only the first cipslaUdpEchoTmplStatsNumDistBuckets will be kept.  The last cipslaUdpEchoTmplStatsNumDistBuckets will contain all entries from its distribution interval start point to infinity
            	**type**\: int
            
            	**range:** 1..20
            
            .. attribute:: cipslaudpechotmpldistinterval
            
            	The statistical distribution buckets interval.  Distribution Bucket Example\:  cipslaUdpEchoTmplDistBuckets = 5 buckets cipslaUdpEchoTmplDistInterval = 10 milliseconds  \| Bucket 1 \| Bucket 2 \| Bucket 3 \| Bucket 4 \| Bucket 5  \| \|  0\-9 ms  \| 10\-19 ms \| 20\-29 ms \| 30\-39 ms \| 40\-Inf ms \|  Odd Example\:  cipslaUdpEchoTmplDistBuckets = 1 buckets cipslaUdpEchoTmplDistInterval = 10 milliseconds  \| Bucket 1  \| \|  0\-Inf ms \|  Thus, this odd example shows that the value of cipslaUdpEchoTmplDistInterval does not apply when cipslaUdpEchoTmplDistBuckets is one
            	**type**\: int
            
            	**range:** 1..100
            
            	**units**\: milliseconds
            
            .. attribute:: cipslaudpechotmplstoragetype
            
            	The storage type of this conceptual row
            	**type**\:  :py:class:`StorageType <ydk.models.cisco_ios_xe.SNMPv2_TC.StorageType>`
            
            .. attribute:: cipslaudpechotmplrowstatus
            
            	The status of the conceptual UDP echo template control row. When the status is active, all the read\-create objects in  that row can be modified
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            

            """

            _prefix = 'CISCO-IPSLA-ECHO-MIB'
            _revision = '2007-08-16'

            def __init__(self):
                super(CISCOIPSLAECHOMIB.CipslaUdpEchoTmplTable.CipslaUdpEchoTmplEntry, self).__init__()

                self.yang_name = "cipslaUdpEchoTmplEntry"
                self.yang_parent_name = "cipslaUdpEchoTmplTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cipslaudpechotmplname']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cipslaudpechotmplname', (YLeaf(YType.str, 'cipslaUdpEchoTmplName'), ['str'])),
                    ('cipslaudpechotmpldescription', (YLeaf(YType.str, 'cipslaUdpEchoTmplDescription'), ['str'])),
                    ('cipslaudpechotmplcontrolenable', (YLeaf(YType.boolean, 'cipslaUdpEchoTmplControlEnable'), ['bool'])),
                    ('cipslaudpechotmplsrcaddrtype', (YLeaf(YType.enumeration, 'cipslaUdpEchoTmplSrcAddrType'), [('ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetAddressType', '')])),
                    ('cipslaudpechotmplsrcaddr', (YLeaf(YType.str, 'cipslaUdpEchoTmplSrcAddr'), ['str'])),
                    ('cipslaudpechotmplsrcport', (YLeaf(YType.uint16, 'cipslaUdpEchoTmplSrcPort'), ['int'])),
                    ('cipslaudpechotmpltimeout', (YLeaf(YType.uint32, 'cipslaUdpEchoTmplTimeOut'), ['int'])),
                    ('cipslaudpechotmplverifydata', (YLeaf(YType.boolean, 'cipslaUdpEchoTmplVerifyData'), ['bool'])),
                    ('cipslaudpechotmplreqdatasize', (YLeaf(YType.uint32, 'cipslaUdpEchoTmplReqDataSize'), ['int'])),
                    ('cipslaudpechotmpltos', (YLeaf(YType.uint32, 'cipslaUdpEchoTmplTOS'), ['int'])),
                    ('cipslaudpechotmplvrfname', (YLeaf(YType.str, 'cipslaUdpEchoTmplVrfName'), ['str'])),
                    ('cipslaudpechotmplthreshold', (YLeaf(YType.uint32, 'cipslaUdpEchoTmplThreshold'), ['int'])),
                    ('cipslaudpechotmplhistlives', (YLeaf(YType.uint32, 'cipslaUdpEchoTmplHistLives'), ['int'])),
                    ('cipslaudpechotmplhistbuckets', (YLeaf(YType.uint32, 'cipslaUdpEchoTmplHistBuckets'), ['int'])),
                    ('cipslaudpechotmplhistfilter', (YLeaf(YType.enumeration, 'cipslaUdpEchoTmplHistFilter'), [('ydk.models.cisco_ios_xe.CISCO_IPSLA_ECHO_MIB', 'CISCOIPSLAECHOMIB', 'CipslaUdpEchoTmplTable.CipslaUdpEchoTmplEntry.CipslaUdpEchoTmplHistFilter')])),
                    ('cipslaudpechotmplstatshours', (YLeaf(YType.uint32, 'cipslaUdpEchoTmplStatsHours'), ['int'])),
                    ('cipslaudpechotmpldistbuckets', (YLeaf(YType.uint32, 'cipslaUdpEchoTmplDistBuckets'), ['int'])),
                    ('cipslaudpechotmpldistinterval', (YLeaf(YType.uint32, 'cipslaUdpEchoTmplDistInterval'), ['int'])),
                    ('cipslaudpechotmplstoragetype', (YLeaf(YType.enumeration, 'cipslaUdpEchoTmplStorageType'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'StorageType', '')])),
                    ('cipslaudpechotmplrowstatus', (YLeaf(YType.enumeration, 'cipslaUdpEchoTmplRowStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.cipslaudpechotmplname = None
                self.cipslaudpechotmpldescription = None
                self.cipslaudpechotmplcontrolenable = None
                self.cipslaudpechotmplsrcaddrtype = None
                self.cipslaudpechotmplsrcaddr = None
                self.cipslaudpechotmplsrcport = None
                self.cipslaudpechotmpltimeout = None
                self.cipslaudpechotmplverifydata = None
                self.cipslaudpechotmplreqdatasize = None
                self.cipslaudpechotmpltos = None
                self.cipslaudpechotmplvrfname = None
                self.cipslaudpechotmplthreshold = None
                self.cipslaudpechotmplhistlives = None
                self.cipslaudpechotmplhistbuckets = None
                self.cipslaudpechotmplhistfilter = None
                self.cipslaudpechotmplstatshours = None
                self.cipslaudpechotmpldistbuckets = None
                self.cipslaudpechotmpldistinterval = None
                self.cipslaudpechotmplstoragetype = None
                self.cipslaudpechotmplrowstatus = None
                self._segment_path = lambda: "cipslaUdpEchoTmplEntry" + "[cipslaUdpEchoTmplName='" + str(self.cipslaudpechotmplname) + "']"
                self._absolute_path = lambda: "CISCO-IPSLA-ECHO-MIB:CISCO-IPSLA-ECHO-MIB/cipslaUdpEchoTmplTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIPSLAECHOMIB.CipslaUdpEchoTmplTable.CipslaUdpEchoTmplEntry, ['cipslaudpechotmplname', 'cipslaudpechotmpldescription', 'cipslaudpechotmplcontrolenable', 'cipslaudpechotmplsrcaddrtype', 'cipslaudpechotmplsrcaddr', 'cipslaudpechotmplsrcport', 'cipslaudpechotmpltimeout', 'cipslaudpechotmplverifydata', 'cipslaudpechotmplreqdatasize', 'cipslaudpechotmpltos', 'cipslaudpechotmplvrfname', 'cipslaudpechotmplthreshold', 'cipslaudpechotmplhistlives', 'cipslaudpechotmplhistbuckets', 'cipslaudpechotmplhistfilter', 'cipslaudpechotmplstatshours', 'cipslaudpechotmpldistbuckets', 'cipslaudpechotmpldistinterval', 'cipslaudpechotmplstoragetype', 'cipslaudpechotmplrowstatus'], name, value)

            class CipslaUdpEchoTmplHistFilter(Enum):
                """
                CipslaUdpEchoTmplHistFilter (Enum Class)

                Defines a filter for adding RTT results to the history

                buffer\:

                none(1)          \- no history is recorded

                all(2)           \- the results of all completion times 

                                   and failed completions are recorded

                overThreshold(3) \- the results of completion times

                                   over cipslaUdpEchoTmplThreshold are 

                                   recorded.

                failures(4)      \- the results of failed operations (only) 

                                   are recorded.

                .. data:: none = 1

                .. data:: all = 2

                .. data:: overThreshold = 3

                .. data:: failures = 4

                """

                none = Enum.YLeaf(1, "none")

                all = Enum.YLeaf(2, "all")

                overThreshold = Enum.YLeaf(3, "overThreshold")

                failures = Enum.YLeaf(4, "failures")



    class CipslaTcpConnTmplTable(Entity):
        """
        A table that contains TCP connect template specific definitions.
        
        .. attribute:: cipslatcpconntmplentry
        
        	A row entry representing an IPSLA TCP connect template
        	**type**\: list of  		 :py:class:`CipslaTcpConnTmplEntry <ydk.models.cisco_ios_xe.CISCO_IPSLA_ECHO_MIB.CISCOIPSLAECHOMIB.CipslaTcpConnTmplTable.CipslaTcpConnTmplEntry>`
        
        

        """

        _prefix = 'CISCO-IPSLA-ECHO-MIB'
        _revision = '2007-08-16'

        def __init__(self):
            super(CISCOIPSLAECHOMIB.CipslaTcpConnTmplTable, self).__init__()

            self.yang_name = "cipslaTcpConnTmplTable"
            self.yang_parent_name = "CISCO-IPSLA-ECHO-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cipslaTcpConnTmplEntry", ("cipslatcpconntmplentry", CISCOIPSLAECHOMIB.CipslaTcpConnTmplTable.CipslaTcpConnTmplEntry))])
            self._leafs = OrderedDict()

            self.cipslatcpconntmplentry = YList(self)
            self._segment_path = lambda: "cipslaTcpConnTmplTable"
            self._absolute_path = lambda: "CISCO-IPSLA-ECHO-MIB:CISCO-IPSLA-ECHO-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIPSLAECHOMIB.CipslaTcpConnTmplTable, [], name, value)


        class CipslaTcpConnTmplEntry(Entity):
            """
            A row entry representing an IPSLA TCP connect template.
            
            .. attribute:: cipslatcpconntmplname  (key)
            
            	A string which specifies the TCP connect template name
            	**type**\: str
            
            	**length:** 1..64
            
            .. attribute:: cipslatcpconntmpldescription
            
            	A string which provides description for the TCP connect template
            	**type**\: str
            
            	**length:** 0..128
            
            .. attribute:: cipslatcpconntmplcontrolenable
            
            	If this object is enabled, then the IP SLA application will send control messages to a responder, residing on the target router to respond to the data request packets being sent by the source router
            	**type**\: bool
            
            .. attribute:: cipslatcpconntmplsrcaddrtype
            
            	An enumerated value which specifies the IP address type of the source. It must be used along with the cipslaTcpConnTmplSrcAddr object
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            .. attribute:: cipslatcpconntmplsrcaddr
            
            	A string which specifies the IP address of the source
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: cipslatcpconntmplsrcport
            
            	This object represents the source's port number. If this object is not specified, the application will get a port allocated by the system
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: cipslatcpconntmpltimeout
            
            	Specifies the duration to wait for an IP SLA operation completion.  For connection oriented protocols, this may cause the connection to be closed by the operation.  Once closed, it will be assumed that the connection reestablishment will be performed.  To prevent unwanted closure of connections, be sure to set this value to a realistic connection timeout
            	**type**\: int
            
            	**range:** 0..604800000
            
            	**units**\: milliseconds
            
            .. attribute:: cipslatcpconntmplverifydata
            
            	When set to true, the resulting data in each IP SLA operation is compared with the expected data.  This includes checking header information (if possible) and exact packet size
            	**type**\: bool
            
            .. attribute:: cipslatcpconntmpltos
            
            	This object represents the type of service octet in an IP header
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: cipslatcpconntmplthreshold
            
            	This object defines an administrative threshold limit. If the IP SLA operation time exceeds this limit and if the condition specified in cipslaTcpConnTmplHistFilter is  satisfied, one threshold crossing occurrence will be counted
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**units**\: milliseconds
            
            .. attribute:: cipslatcpconntmplhistlives
            
            	The maximum number of history lives to record.  A life is defined by the countdown (or transition) to zero  by the cipslaAutoGroupScheduleLife object.  A new life is created when the same conceptual control row is restarted via the transition of the  cipslaAutoGroupScheduleLife object and its subsequent  countdown.  The value of zero will shut off all data collection
            	**type**\: int
            
            	**range:** 0..2
            
            .. attribute:: cipslatcpconntmplhistbuckets
            
            	The maximum number of history buckets to record. This value should be set to the number of operations  to keep per lifetime.  After cipslaTcpConnTmplHistBuckets are filled, the  oldest entries are deleted and the most recent cipslaTcpConnTmplHistBuckets buckets are retained
            	**type**\: int
            
            	**range:** 1..60
            
            .. attribute:: cipslatcpconntmplhistfilter
            
            	Defines a filter for adding RTT results to the history buffer\:  none(1)          \- no history is recorded all(2)           \- the results of all completion times                     and failed completions are recorded overThreshold(3) \- the results of completion times                    over cipslaTcpConnTmplThreshold are                     recorded. failures(4)      \- the results of failed operations (only)                     are recorded
            	**type**\:  :py:class:`CipslaTcpConnTmplHistFilter <ydk.models.cisco_ios_xe.CISCO_IPSLA_ECHO_MIB.CISCOIPSLAECHOMIB.CipslaTcpConnTmplTable.CipslaTcpConnTmplEntry.CipslaTcpConnTmplHistFilter>`
            
            .. attribute:: cipslatcpconntmplstatshours
            
            	The maximum number of hours for which statistics are maintained. Specifically this is the number of hourly  groups to keep before rolling over.  The value of one is not advisable because the hourly group will close and immediately be deleted before the network management station will have the opportunity to retrieve the statistics.  The value of zero will shut off data collection
            	**type**\: int
            
            	**range:** 0..25
            
            	**units**\: hours
            
            .. attribute:: cipslatcpconntmpldistbuckets
            
            	The maximum number of statistical distribution buckets to accumulate.  Since this index does not rollover, only the first cipslaTcpConnTmplDistBuckets will be kept.  The last cipslaTcpConnTmplDistBuckets will contain all entries from its distribution interval start point to infinity
            	**type**\: int
            
            	**range:** 1..20
            
            .. attribute:: cipslatcpconntmpldistinterval
            
            	The statistical distribution buckets interval.  Distribution Bucket Example\:  cipslaTcpConnTmplDistBuckets = 5 buckets cipslaTcpConnTmplDistInterval = 10 milliseconds  \| Bucket 1 \| Bucket 2 \| Bucket 3 \| Bucket 4 \| Bucket 5  \| \|  0\-9 ms  \| 10\-19 ms \| 20\-29 ms \| 30\-39 ms \| 40\-Inf ms \|  Odd Example\:  cipslaTcpConnTmplDistBuckets = 1 buckets cipslaTcpConnTmplDistInterval = 10 milliseconds  \| Bucket 1  \| \|  0\-Inf ms \|  Thus, this odd example shows that the value of cipslaTcpConnTmplDistInterval does not apply when cipslaTcpConnTmplDistBuckets is one
            	**type**\: int
            
            	**range:** 1..100
            
            	**units**\: milliseconds
            
            .. attribute:: cipslatcpconntmplstoragetype
            
            	The storage type of this conceptual row
            	**type**\:  :py:class:`StorageType <ydk.models.cisco_ios_xe.SNMPv2_TC.StorageType>`
            
            .. attribute:: cipslatcpconntmplrowstatus
            
            	The status of the conceptual tcp connect control row. When the status is active, all the read\-create objects  in that row can be modified
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            

            """

            _prefix = 'CISCO-IPSLA-ECHO-MIB'
            _revision = '2007-08-16'

            def __init__(self):
                super(CISCOIPSLAECHOMIB.CipslaTcpConnTmplTable.CipslaTcpConnTmplEntry, self).__init__()

                self.yang_name = "cipslaTcpConnTmplEntry"
                self.yang_parent_name = "cipslaTcpConnTmplTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cipslatcpconntmplname']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cipslatcpconntmplname', (YLeaf(YType.str, 'cipslaTcpConnTmplName'), ['str'])),
                    ('cipslatcpconntmpldescription', (YLeaf(YType.str, 'cipslaTcpConnTmplDescription'), ['str'])),
                    ('cipslatcpconntmplcontrolenable', (YLeaf(YType.boolean, 'cipslaTcpConnTmplControlEnable'), ['bool'])),
                    ('cipslatcpconntmplsrcaddrtype', (YLeaf(YType.enumeration, 'cipslaTcpConnTmplSrcAddrType'), [('ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetAddressType', '')])),
                    ('cipslatcpconntmplsrcaddr', (YLeaf(YType.str, 'cipslaTcpConnTmplSrcAddr'), ['str'])),
                    ('cipslatcpconntmplsrcport', (YLeaf(YType.uint16, 'cipslaTcpConnTmplSrcPort'), ['int'])),
                    ('cipslatcpconntmpltimeout', (YLeaf(YType.uint32, 'cipslaTcpConnTmplTimeOut'), ['int'])),
                    ('cipslatcpconntmplverifydata', (YLeaf(YType.boolean, 'cipslaTcpConnTmplVerifyData'), ['bool'])),
                    ('cipslatcpconntmpltos', (YLeaf(YType.uint32, 'cipslaTcpConnTmplTOS'), ['int'])),
                    ('cipslatcpconntmplthreshold', (YLeaf(YType.uint32, 'cipslaTcpConnTmplThreshold'), ['int'])),
                    ('cipslatcpconntmplhistlives', (YLeaf(YType.uint32, 'cipslaTcpConnTmplHistLives'), ['int'])),
                    ('cipslatcpconntmplhistbuckets', (YLeaf(YType.uint32, 'cipslaTcpConnTmplHistBuckets'), ['int'])),
                    ('cipslatcpconntmplhistfilter', (YLeaf(YType.enumeration, 'cipslaTcpConnTmplHistFilter'), [('ydk.models.cisco_ios_xe.CISCO_IPSLA_ECHO_MIB', 'CISCOIPSLAECHOMIB', 'CipslaTcpConnTmplTable.CipslaTcpConnTmplEntry.CipslaTcpConnTmplHistFilter')])),
                    ('cipslatcpconntmplstatshours', (YLeaf(YType.uint32, 'cipslaTcpConnTmplStatsHours'), ['int'])),
                    ('cipslatcpconntmpldistbuckets', (YLeaf(YType.uint32, 'cipslaTcpConnTmplDistBuckets'), ['int'])),
                    ('cipslatcpconntmpldistinterval', (YLeaf(YType.uint32, 'cipslaTcpConnTmplDistInterval'), ['int'])),
                    ('cipslatcpconntmplstoragetype', (YLeaf(YType.enumeration, 'cipslaTcpConnTmplStorageType'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'StorageType', '')])),
                    ('cipslatcpconntmplrowstatus', (YLeaf(YType.enumeration, 'cipslaTcpConnTmplRowStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.cipslatcpconntmplname = None
                self.cipslatcpconntmpldescription = None
                self.cipslatcpconntmplcontrolenable = None
                self.cipslatcpconntmplsrcaddrtype = None
                self.cipslatcpconntmplsrcaddr = None
                self.cipslatcpconntmplsrcport = None
                self.cipslatcpconntmpltimeout = None
                self.cipslatcpconntmplverifydata = None
                self.cipslatcpconntmpltos = None
                self.cipslatcpconntmplthreshold = None
                self.cipslatcpconntmplhistlives = None
                self.cipslatcpconntmplhistbuckets = None
                self.cipslatcpconntmplhistfilter = None
                self.cipslatcpconntmplstatshours = None
                self.cipslatcpconntmpldistbuckets = None
                self.cipslatcpconntmpldistinterval = None
                self.cipslatcpconntmplstoragetype = None
                self.cipslatcpconntmplrowstatus = None
                self._segment_path = lambda: "cipslaTcpConnTmplEntry" + "[cipslaTcpConnTmplName='" + str(self.cipslatcpconntmplname) + "']"
                self._absolute_path = lambda: "CISCO-IPSLA-ECHO-MIB:CISCO-IPSLA-ECHO-MIB/cipslaTcpConnTmplTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIPSLAECHOMIB.CipslaTcpConnTmplTable.CipslaTcpConnTmplEntry, ['cipslatcpconntmplname', 'cipslatcpconntmpldescription', 'cipslatcpconntmplcontrolenable', 'cipslatcpconntmplsrcaddrtype', 'cipslatcpconntmplsrcaddr', 'cipslatcpconntmplsrcport', 'cipslatcpconntmpltimeout', 'cipslatcpconntmplverifydata', 'cipslatcpconntmpltos', 'cipslatcpconntmplthreshold', 'cipslatcpconntmplhistlives', 'cipslatcpconntmplhistbuckets', 'cipslatcpconntmplhistfilter', 'cipslatcpconntmplstatshours', 'cipslatcpconntmpldistbuckets', 'cipslatcpconntmpldistinterval', 'cipslatcpconntmplstoragetype', 'cipslatcpconntmplrowstatus'], name, value)

            class CipslaTcpConnTmplHistFilter(Enum):
                """
                CipslaTcpConnTmplHistFilter (Enum Class)

                Defines a filter for adding RTT results to the history

                buffer\:

                none(1)          \- no history is recorded

                all(2)           \- the results of all completion times 

                                   and failed completions are recorded

                overThreshold(3) \- the results of completion times

                                   over cipslaTcpConnTmplThreshold are 

                                   recorded.

                failures(4)      \- the results of failed operations (only) 

                                   are recorded.

                .. data:: none = 1

                .. data:: all = 2

                .. data:: overThreshold = 3

                .. data:: failures = 4

                """

                none = Enum.YLeaf(1, "none")

                all = Enum.YLeaf(2, "all")

                overThreshold = Enum.YLeaf(3, "overThreshold")

                failures = Enum.YLeaf(4, "failures")


    def clone_ptr(self):
        self._top_entity = CISCOIPSLAECHOMIB()
        return self._top_entity

