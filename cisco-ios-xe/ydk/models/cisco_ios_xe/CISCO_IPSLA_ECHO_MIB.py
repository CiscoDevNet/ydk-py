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
    	**type**\:  :py:class:`Cipslaicmpechotmpltable <ydk.models.cisco_ios_xe.CISCO_IPSLA_ECHO_MIB.CISCOIPSLAECHOMIB.Cipslaicmpechotmpltable>`
    
    .. attribute:: cipslaudpechotmpltable
    
    	A table that contains UDP echo template specific definitions
    	**type**\:  :py:class:`Cipslaudpechotmpltable <ydk.models.cisco_ios_xe.CISCO_IPSLA_ECHO_MIB.CISCOIPSLAECHOMIB.Cipslaudpechotmpltable>`
    
    .. attribute:: cipslatcpconntmpltable
    
    	A table that contains TCP connect template specific definitions
    	**type**\:  :py:class:`Cipslatcpconntmpltable <ydk.models.cisco_ios_xe.CISCO_IPSLA_ECHO_MIB.CISCOIPSLAECHOMIB.Cipslatcpconntmpltable>`
    
    

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
        self._child_container_classes = OrderedDict([("cipslaIcmpEchoTmplTable", ("cipslaicmpechotmpltable", CISCOIPSLAECHOMIB.Cipslaicmpechotmpltable)), ("cipslaUdpEchoTmplTable", ("cipslaudpechotmpltable", CISCOIPSLAECHOMIB.Cipslaudpechotmpltable)), ("cipslaTcpConnTmplTable", ("cipslatcpconntmpltable", CISCOIPSLAECHOMIB.Cipslatcpconntmpltable))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.cipslaicmpechotmpltable = CISCOIPSLAECHOMIB.Cipslaicmpechotmpltable()
        self.cipslaicmpechotmpltable.parent = self
        self._children_name_map["cipslaicmpechotmpltable"] = "cipslaIcmpEchoTmplTable"
        self._children_yang_names.add("cipslaIcmpEchoTmplTable")

        self.cipslaudpechotmpltable = CISCOIPSLAECHOMIB.Cipslaudpechotmpltable()
        self.cipslaudpechotmpltable.parent = self
        self._children_name_map["cipslaudpechotmpltable"] = "cipslaUdpEchoTmplTable"
        self._children_yang_names.add("cipslaUdpEchoTmplTable")

        self.cipslatcpconntmpltable = CISCOIPSLAECHOMIB.Cipslatcpconntmpltable()
        self.cipslatcpconntmpltable.parent = self
        self._children_name_map["cipslatcpconntmpltable"] = "cipslaTcpConnTmplTable"
        self._children_yang_names.add("cipslaTcpConnTmplTable")
        self._segment_path = lambda: "CISCO-IPSLA-ECHO-MIB:CISCO-IPSLA-ECHO-MIB"


    class Cipslaicmpechotmpltable(Entity):
        """
        A table that contains ICMP echo template definitions.
        
        .. attribute:: cipslaicmpechotmplentry
        
        	A row entry representing an IPSLA ICMP echo template
        	**type**\: list of  		 :py:class:`Cipslaicmpechotmplentry <ydk.models.cisco_ios_xe.CISCO_IPSLA_ECHO_MIB.CISCOIPSLAECHOMIB.Cipslaicmpechotmpltable.Cipslaicmpechotmplentry>`
        
        

        """

        _prefix = 'CISCO-IPSLA-ECHO-MIB'
        _revision = '2007-08-16'

        def __init__(self):
            super(CISCOIPSLAECHOMIB.Cipslaicmpechotmpltable, self).__init__()

            self.yang_name = "cipslaIcmpEchoTmplTable"
            self.yang_parent_name = "CISCO-IPSLA-ECHO-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cipslaIcmpEchoTmplEntry", ("cipslaicmpechotmplentry", CISCOIPSLAECHOMIB.Cipslaicmpechotmpltable.Cipslaicmpechotmplentry))])
            self._leafs = OrderedDict()

            self.cipslaicmpechotmplentry = YList(self)
            self._segment_path = lambda: "cipslaIcmpEchoTmplTable"
            self._absolute_path = lambda: "CISCO-IPSLA-ECHO-MIB:CISCO-IPSLA-ECHO-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIPSLAECHOMIB.Cipslaicmpechotmpltable, [], name, value)


        class Cipslaicmpechotmplentry(Entity):
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
            	**type**\:  :py:class:`Cipslaicmpechotmplhistfilter <ydk.models.cisco_ios_xe.CISCO_IPSLA_ECHO_MIB.CISCOIPSLAECHOMIB.Cipslaicmpechotmpltable.Cipslaicmpechotmplentry.Cipslaicmpechotmplhistfilter>`
            
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
                super(CISCOIPSLAECHOMIB.Cipslaicmpechotmpltable.Cipslaicmpechotmplentry, self).__init__()

                self.yang_name = "cipslaIcmpEchoTmplEntry"
                self.yang_parent_name = "cipslaIcmpEchoTmplTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cipslaicmpechotmplname']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cipslaicmpechotmplname', YLeaf(YType.str, 'cipslaIcmpEchoTmplName')),
                    ('cipslaicmpechotmpldescription', YLeaf(YType.str, 'cipslaIcmpEchoTmplDescription')),
                    ('cipslaicmpechotmplsrcaddrtype', YLeaf(YType.enumeration, 'cipslaIcmpEchoTmplSrcAddrType')),
                    ('cipslaicmpechotmplsrcaddr', YLeaf(YType.str, 'cipslaIcmpEchoTmplSrcAddr')),
                    ('cipslaicmpechotmpltimeout', YLeaf(YType.uint32, 'cipslaIcmpEchoTmplTimeOut')),
                    ('cipslaicmpechotmplverifydata', YLeaf(YType.boolean, 'cipslaIcmpEchoTmplVerifyData')),
                    ('cipslaicmpechotmplreqdatasize', YLeaf(YType.uint32, 'cipslaIcmpEchoTmplReqDataSize')),
                    ('cipslaicmpechotmpltos', YLeaf(YType.uint32, 'cipslaIcmpEchoTmplTOS')),
                    ('cipslaicmpechotmplvrfname', YLeaf(YType.str, 'cipslaIcmpEchoTmplVrfName')),
                    ('cipslaicmpechotmplthreshold', YLeaf(YType.uint32, 'cipslaIcmpEchoTmplThreshold')),
                    ('cipslaicmpechotmplhistlives', YLeaf(YType.uint32, 'cipslaIcmpEchoTmplHistLives')),
                    ('cipslaicmpechotmplhistbuckets', YLeaf(YType.uint32, 'cipslaIcmpEchoTmplHistBuckets')),
                    ('cipslaicmpechotmplhistfilter', YLeaf(YType.enumeration, 'cipslaIcmpEchoTmplHistFilter')),
                    ('cipslaicmpechotmplstatshours', YLeaf(YType.uint32, 'cipslaIcmpEchoTmplStatsHours')),
                    ('cipslaicmpechotmpldistbuckets', YLeaf(YType.uint32, 'cipslaIcmpEchoTmplDistBuckets')),
                    ('cipslaicmpechotmpldistinterval', YLeaf(YType.uint32, 'cipslaIcmpEchoTmplDistInterval')),
                    ('cipslaicmpechotmplstoragetype', YLeaf(YType.enumeration, 'cipslaIcmpEchoTmplStorageType')),
                    ('cipslaicmpechotmplrowstatus', YLeaf(YType.enumeration, 'cipslaIcmpEchoTmplRowStatus')),
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

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIPSLAECHOMIB.Cipslaicmpechotmpltable.Cipslaicmpechotmplentry, ['cipslaicmpechotmplname', 'cipslaicmpechotmpldescription', 'cipslaicmpechotmplsrcaddrtype', 'cipslaicmpechotmplsrcaddr', 'cipslaicmpechotmpltimeout', 'cipslaicmpechotmplverifydata', 'cipslaicmpechotmplreqdatasize', 'cipslaicmpechotmpltos', 'cipslaicmpechotmplvrfname', 'cipslaicmpechotmplthreshold', 'cipslaicmpechotmplhistlives', 'cipslaicmpechotmplhistbuckets', 'cipslaicmpechotmplhistfilter', 'cipslaicmpechotmplstatshours', 'cipslaicmpechotmpldistbuckets', 'cipslaicmpechotmpldistinterval', 'cipslaicmpechotmplstoragetype', 'cipslaicmpechotmplrowstatus'], name, value)

            class Cipslaicmpechotmplhistfilter(Enum):
                """
                Cipslaicmpechotmplhistfilter (Enum Class)

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



    class Cipslaudpechotmpltable(Entity):
        """
        A table that contains UDP echo template specific definitions.
        
        .. attribute:: cipslaudpechotmplentry
        
        	A row entry representing an IPSLA UDP echo template
        	**type**\: list of  		 :py:class:`Cipslaudpechotmplentry <ydk.models.cisco_ios_xe.CISCO_IPSLA_ECHO_MIB.CISCOIPSLAECHOMIB.Cipslaudpechotmpltable.Cipslaudpechotmplentry>`
        
        

        """

        _prefix = 'CISCO-IPSLA-ECHO-MIB'
        _revision = '2007-08-16'

        def __init__(self):
            super(CISCOIPSLAECHOMIB.Cipslaudpechotmpltable, self).__init__()

            self.yang_name = "cipslaUdpEchoTmplTable"
            self.yang_parent_name = "CISCO-IPSLA-ECHO-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cipslaUdpEchoTmplEntry", ("cipslaudpechotmplentry", CISCOIPSLAECHOMIB.Cipslaudpechotmpltable.Cipslaudpechotmplentry))])
            self._leafs = OrderedDict()

            self.cipslaudpechotmplentry = YList(self)
            self._segment_path = lambda: "cipslaUdpEchoTmplTable"
            self._absolute_path = lambda: "CISCO-IPSLA-ECHO-MIB:CISCO-IPSLA-ECHO-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIPSLAECHOMIB.Cipslaudpechotmpltable, [], name, value)


        class Cipslaudpechotmplentry(Entity):
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
            	**type**\:  :py:class:`Cipslaudpechotmplhistfilter <ydk.models.cisco_ios_xe.CISCO_IPSLA_ECHO_MIB.CISCOIPSLAECHOMIB.Cipslaudpechotmpltable.Cipslaudpechotmplentry.Cipslaudpechotmplhistfilter>`
            
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
                super(CISCOIPSLAECHOMIB.Cipslaudpechotmpltable.Cipslaudpechotmplentry, self).__init__()

                self.yang_name = "cipslaUdpEchoTmplEntry"
                self.yang_parent_name = "cipslaUdpEchoTmplTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cipslaudpechotmplname']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cipslaudpechotmplname', YLeaf(YType.str, 'cipslaUdpEchoTmplName')),
                    ('cipslaudpechotmpldescription', YLeaf(YType.str, 'cipslaUdpEchoTmplDescription')),
                    ('cipslaudpechotmplcontrolenable', YLeaf(YType.boolean, 'cipslaUdpEchoTmplControlEnable')),
                    ('cipslaudpechotmplsrcaddrtype', YLeaf(YType.enumeration, 'cipslaUdpEchoTmplSrcAddrType')),
                    ('cipslaudpechotmplsrcaddr', YLeaf(YType.str, 'cipslaUdpEchoTmplSrcAddr')),
                    ('cipslaudpechotmplsrcport', YLeaf(YType.uint16, 'cipslaUdpEchoTmplSrcPort')),
                    ('cipslaudpechotmpltimeout', YLeaf(YType.uint32, 'cipslaUdpEchoTmplTimeOut')),
                    ('cipslaudpechotmplverifydata', YLeaf(YType.boolean, 'cipslaUdpEchoTmplVerifyData')),
                    ('cipslaudpechotmplreqdatasize', YLeaf(YType.uint32, 'cipslaUdpEchoTmplReqDataSize')),
                    ('cipslaudpechotmpltos', YLeaf(YType.uint32, 'cipslaUdpEchoTmplTOS')),
                    ('cipslaudpechotmplvrfname', YLeaf(YType.str, 'cipslaUdpEchoTmplVrfName')),
                    ('cipslaudpechotmplthreshold', YLeaf(YType.uint32, 'cipslaUdpEchoTmplThreshold')),
                    ('cipslaudpechotmplhistlives', YLeaf(YType.uint32, 'cipslaUdpEchoTmplHistLives')),
                    ('cipslaudpechotmplhistbuckets', YLeaf(YType.uint32, 'cipslaUdpEchoTmplHistBuckets')),
                    ('cipslaudpechotmplhistfilter', YLeaf(YType.enumeration, 'cipslaUdpEchoTmplHistFilter')),
                    ('cipslaudpechotmplstatshours', YLeaf(YType.uint32, 'cipslaUdpEchoTmplStatsHours')),
                    ('cipslaudpechotmpldistbuckets', YLeaf(YType.uint32, 'cipslaUdpEchoTmplDistBuckets')),
                    ('cipslaudpechotmpldistinterval', YLeaf(YType.uint32, 'cipslaUdpEchoTmplDistInterval')),
                    ('cipslaudpechotmplstoragetype', YLeaf(YType.enumeration, 'cipslaUdpEchoTmplStorageType')),
                    ('cipslaudpechotmplrowstatus', YLeaf(YType.enumeration, 'cipslaUdpEchoTmplRowStatus')),
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

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIPSLAECHOMIB.Cipslaudpechotmpltable.Cipslaudpechotmplentry, ['cipslaudpechotmplname', 'cipslaudpechotmpldescription', 'cipslaudpechotmplcontrolenable', 'cipslaudpechotmplsrcaddrtype', 'cipslaudpechotmplsrcaddr', 'cipslaudpechotmplsrcport', 'cipslaudpechotmpltimeout', 'cipslaudpechotmplverifydata', 'cipslaudpechotmplreqdatasize', 'cipslaudpechotmpltos', 'cipslaudpechotmplvrfname', 'cipslaudpechotmplthreshold', 'cipslaudpechotmplhistlives', 'cipslaudpechotmplhistbuckets', 'cipslaudpechotmplhistfilter', 'cipslaudpechotmplstatshours', 'cipslaudpechotmpldistbuckets', 'cipslaudpechotmpldistinterval', 'cipslaudpechotmplstoragetype', 'cipslaudpechotmplrowstatus'], name, value)

            class Cipslaudpechotmplhistfilter(Enum):
                """
                Cipslaudpechotmplhistfilter (Enum Class)

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



    class Cipslatcpconntmpltable(Entity):
        """
        A table that contains TCP connect template specific definitions.
        
        .. attribute:: cipslatcpconntmplentry
        
        	A row entry representing an IPSLA TCP connect template
        	**type**\: list of  		 :py:class:`Cipslatcpconntmplentry <ydk.models.cisco_ios_xe.CISCO_IPSLA_ECHO_MIB.CISCOIPSLAECHOMIB.Cipslatcpconntmpltable.Cipslatcpconntmplentry>`
        
        

        """

        _prefix = 'CISCO-IPSLA-ECHO-MIB'
        _revision = '2007-08-16'

        def __init__(self):
            super(CISCOIPSLAECHOMIB.Cipslatcpconntmpltable, self).__init__()

            self.yang_name = "cipslaTcpConnTmplTable"
            self.yang_parent_name = "CISCO-IPSLA-ECHO-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cipslaTcpConnTmplEntry", ("cipslatcpconntmplentry", CISCOIPSLAECHOMIB.Cipslatcpconntmpltable.Cipslatcpconntmplentry))])
            self._leafs = OrderedDict()

            self.cipslatcpconntmplentry = YList(self)
            self._segment_path = lambda: "cipslaTcpConnTmplTable"
            self._absolute_path = lambda: "CISCO-IPSLA-ECHO-MIB:CISCO-IPSLA-ECHO-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIPSLAECHOMIB.Cipslatcpconntmpltable, [], name, value)


        class Cipslatcpconntmplentry(Entity):
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
            	**type**\:  :py:class:`Cipslatcpconntmplhistfilter <ydk.models.cisco_ios_xe.CISCO_IPSLA_ECHO_MIB.CISCOIPSLAECHOMIB.Cipslatcpconntmpltable.Cipslatcpconntmplentry.Cipslatcpconntmplhistfilter>`
            
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
                super(CISCOIPSLAECHOMIB.Cipslatcpconntmpltable.Cipslatcpconntmplentry, self).__init__()

                self.yang_name = "cipslaTcpConnTmplEntry"
                self.yang_parent_name = "cipslaTcpConnTmplTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cipslatcpconntmplname']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cipslatcpconntmplname', YLeaf(YType.str, 'cipslaTcpConnTmplName')),
                    ('cipslatcpconntmpldescription', YLeaf(YType.str, 'cipslaTcpConnTmplDescription')),
                    ('cipslatcpconntmplcontrolenable', YLeaf(YType.boolean, 'cipslaTcpConnTmplControlEnable')),
                    ('cipslatcpconntmplsrcaddrtype', YLeaf(YType.enumeration, 'cipslaTcpConnTmplSrcAddrType')),
                    ('cipslatcpconntmplsrcaddr', YLeaf(YType.str, 'cipslaTcpConnTmplSrcAddr')),
                    ('cipslatcpconntmplsrcport', YLeaf(YType.uint16, 'cipslaTcpConnTmplSrcPort')),
                    ('cipslatcpconntmpltimeout', YLeaf(YType.uint32, 'cipslaTcpConnTmplTimeOut')),
                    ('cipslatcpconntmplverifydata', YLeaf(YType.boolean, 'cipslaTcpConnTmplVerifyData')),
                    ('cipslatcpconntmpltos', YLeaf(YType.uint32, 'cipslaTcpConnTmplTOS')),
                    ('cipslatcpconntmplthreshold', YLeaf(YType.uint32, 'cipslaTcpConnTmplThreshold')),
                    ('cipslatcpconntmplhistlives', YLeaf(YType.uint32, 'cipslaTcpConnTmplHistLives')),
                    ('cipslatcpconntmplhistbuckets', YLeaf(YType.uint32, 'cipslaTcpConnTmplHistBuckets')),
                    ('cipslatcpconntmplhistfilter', YLeaf(YType.enumeration, 'cipslaTcpConnTmplHistFilter')),
                    ('cipslatcpconntmplstatshours', YLeaf(YType.uint32, 'cipslaTcpConnTmplStatsHours')),
                    ('cipslatcpconntmpldistbuckets', YLeaf(YType.uint32, 'cipslaTcpConnTmplDistBuckets')),
                    ('cipslatcpconntmpldistinterval', YLeaf(YType.uint32, 'cipslaTcpConnTmplDistInterval')),
                    ('cipslatcpconntmplstoragetype', YLeaf(YType.enumeration, 'cipslaTcpConnTmplStorageType')),
                    ('cipslatcpconntmplrowstatus', YLeaf(YType.enumeration, 'cipslaTcpConnTmplRowStatus')),
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

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIPSLAECHOMIB.Cipslatcpconntmpltable.Cipslatcpconntmplentry, ['cipslatcpconntmplname', 'cipslatcpconntmpldescription', 'cipslatcpconntmplcontrolenable', 'cipslatcpconntmplsrcaddrtype', 'cipslatcpconntmplsrcaddr', 'cipslatcpconntmplsrcport', 'cipslatcpconntmpltimeout', 'cipslatcpconntmplverifydata', 'cipslatcpconntmpltos', 'cipslatcpconntmplthreshold', 'cipslatcpconntmplhistlives', 'cipslatcpconntmplhistbuckets', 'cipslatcpconntmplhistfilter', 'cipslatcpconntmplstatshours', 'cipslatcpconntmpldistbuckets', 'cipslatcpconntmpldistinterval', 'cipslatcpconntmplstoragetype', 'cipslatcpconntmplrowstatus'], name, value)

            class Cipslatcpconntmplhistfilter(Enum):
                """
                Cipslatcpconntmplhistfilter (Enum Class)

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

