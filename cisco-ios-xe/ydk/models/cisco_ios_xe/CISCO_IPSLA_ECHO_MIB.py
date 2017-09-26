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
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CISCOIPSLAECHOMIB(Entity):
    """
    
    
    .. attribute:: cipslaicmpechotmpltable
    
    	A table that contains ICMP echo template definitions
    	**type**\:   :py:class:`Cipslaicmpechotmpltable <ydk.models.cisco_ios_xe.CISCO_IPSLA_ECHO_MIB.CISCOIPSLAECHOMIB.Cipslaicmpechotmpltable>`
    
    .. attribute:: cipslatcpconntmpltable
    
    	A table that contains TCP connect template specific definitions
    	**type**\:   :py:class:`Cipslatcpconntmpltable <ydk.models.cisco_ios_xe.CISCO_IPSLA_ECHO_MIB.CISCOIPSLAECHOMIB.Cipslatcpconntmpltable>`
    
    .. attribute:: cipslaudpechotmpltable
    
    	A table that contains UDP echo template specific definitions
    	**type**\:   :py:class:`Cipslaudpechotmpltable <ydk.models.cisco_ios_xe.CISCO_IPSLA_ECHO_MIB.CISCOIPSLAECHOMIB.Cipslaudpechotmpltable>`
    
    

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
        self._child_container_classes = {"cipslaIcmpEchoTmplTable" : ("cipslaicmpechotmpltable", CISCOIPSLAECHOMIB.Cipslaicmpechotmpltable), "cipslaTcpConnTmplTable" : ("cipslatcpconntmpltable", CISCOIPSLAECHOMIB.Cipslatcpconntmpltable), "cipslaUdpEchoTmplTable" : ("cipslaudpechotmpltable", CISCOIPSLAECHOMIB.Cipslaudpechotmpltable)}
        self._child_list_classes = {}

        self.cipslaicmpechotmpltable = CISCOIPSLAECHOMIB.Cipslaicmpechotmpltable()
        self.cipslaicmpechotmpltable.parent = self
        self._children_name_map["cipslaicmpechotmpltable"] = "cipslaIcmpEchoTmplTable"
        self._children_yang_names.add("cipslaIcmpEchoTmplTable")

        self.cipslatcpconntmpltable = CISCOIPSLAECHOMIB.Cipslatcpconntmpltable()
        self.cipslatcpconntmpltable.parent = self
        self._children_name_map["cipslatcpconntmpltable"] = "cipslaTcpConnTmplTable"
        self._children_yang_names.add("cipslaTcpConnTmplTable")

        self.cipslaudpechotmpltable = CISCOIPSLAECHOMIB.Cipslaudpechotmpltable()
        self.cipslaudpechotmpltable.parent = self
        self._children_name_map["cipslaudpechotmpltable"] = "cipslaUdpEchoTmplTable"
        self._children_yang_names.add("cipslaUdpEchoTmplTable")
        self._segment_path = lambda: "CISCO-IPSLA-ECHO-MIB:CISCO-IPSLA-ECHO-MIB"


    class Cipslaicmpechotmpltable(Entity):
        """
        A table that contains ICMP echo template definitions.
        
        .. attribute:: cipslaicmpechotmplentry
        
        	A row entry representing an IPSLA ICMP echo template
        	**type**\: list of    :py:class:`Cipslaicmpechotmplentry <ydk.models.cisco_ios_xe.CISCO_IPSLA_ECHO_MIB.CISCOIPSLAECHOMIB.Cipslaicmpechotmpltable.Cipslaicmpechotmplentry>`
        
        

        """

        _prefix = 'CISCO-IPSLA-ECHO-MIB'
        _revision = '2007-08-16'

        def __init__(self):
            super(CISCOIPSLAECHOMIB.Cipslaicmpechotmpltable, self).__init__()

            self.yang_name = "cipslaIcmpEchoTmplTable"
            self.yang_parent_name = "CISCO-IPSLA-ECHO-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"cipslaIcmpEchoTmplEntry" : ("cipslaicmpechotmplentry", CISCOIPSLAECHOMIB.Cipslaicmpechotmpltable.Cipslaicmpechotmplentry)}

            self.cipslaicmpechotmplentry = YList(self)
            self._segment_path = lambda: "cipslaIcmpEchoTmplTable"
            self._absolute_path = lambda: "CISCO-IPSLA-ECHO-MIB:CISCO-IPSLA-ECHO-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIPSLAECHOMIB.Cipslaicmpechotmpltable, [], name, value)


        class Cipslaicmpechotmplentry(Entity):
            """
            A row entry representing an IPSLA ICMP echo template.
            
            .. attribute:: cipslaicmpechotmplname  <key>
            
            	This field is used to specify the ICMP echo template name
            	**type**\:  str
            
            	**length:** 1..64
            
            .. attribute:: cipslaicmpechotmpldescription
            
            	This field is used to provide description for the ICMP echo template
            	**type**\:  str
            
            	**length:** 0..128
            
            .. attribute:: cipslaicmpechotmpldistbuckets
            
            	The maximum number of statistical distribution buckets to accumulate.  Since this index does not rollover, only the first cipslaIcmpEchoTmplStatsNumDistBuckets will be kept.  The last cipslaIcmpEchoTmplStatsNumDistBucket will contain all entries from its distribution interval start point to infinity
            	**type**\:  int
            
            	**range:** 1..20
            
            .. attribute:: cipslaicmpechotmpldistinterval
            
            	The statistical distribution buckets interval.  Distribution Bucket Example\:  cipslaIcmpEchoTmplDistBuckets = 5 buckets cipslaIcmpEchoTmplDistInterval = 10 milliseconds  \| Bucket 1 \| Bucket 2 \| Bucket 3 \| Bucket 4 \| Bucket 5  \| \|  0\-9 ms  \| 10\-19 ms \| 20\-29 ms \| 30\-39 ms \| 40\-Inf ms \|  Odd Example\:  cipslaIcmpEchoTmplDistBuckets = 1 buckets cipslaIcmpEchoTmplDistInterval = 10 milliseconds  \| Bucket 1  \| \|  0\-Inf ms \|  Thus, this odd example shows that the value of cipslaIcmpEchoTmplDistInterval does not apply when cipslaIcmpEchoTmplDistBuckets is one
            	**type**\:  int
            
            	**range:** 1..100
            
            	**units**\: milliseconds
            
            .. attribute:: cipslaicmpechotmplhistbuckets
            
            	The maximum number of history buckets to record. This value is set to the number of operations  to keep per lifetime.  After cipslaIcmpEchoTmplHistBuckets are filled, the  oldest entries are deleted and the most recent cipslaIcmpEchoTmplHistBuckets buckets are retained
            	**type**\:  int
            
            	**range:** 1..60
            
            .. attribute:: cipslaicmpechotmplhistfilter
            
            	Defines a filter for adding RTT results to the history buffer\:  none(1)          \- no history is recorded all(2)           \- the results of all completion times                     and failed completions are recorded overThreshold(3) \- the results of completion times                    over cipslaIcmpEchoTmplThreshold are                     recorded. failures(4)      \- the results of failed operations (only)                     are recorded
            	**type**\:   :py:class:`Cipslaicmpechotmplhistfilter <ydk.models.cisco_ios_xe.CISCO_IPSLA_ECHO_MIB.CISCOIPSLAECHOMIB.Cipslaicmpechotmpltable.Cipslaicmpechotmplentry.Cipslaicmpechotmplhistfilter>`
            
            .. attribute:: cipslaicmpechotmplhistlives
            
            	The maximum number of history lives to record.  A life is defined by the countdown (or transition) to zero  by the cipslaAutoGroupScheduleLife object.  A new life is created when the same conceptual control row is restarted via the transition of the  cipslaAutoGroupScheduleLife object and its subsequent  countdown.  The value of zero will shut off all data collection
            	**type**\:  int
            
            	**range:** 0..2
            
            .. attribute:: cipslaicmpechotmplreqdatasize
            
            	This object represents the number of octets to be placed into the ARR Data portion of the request message, when using SNA protocols.  For non\-ARR protocols' IP SLA request/responses, this value represents the native payload size.  REMEMBER\:  The ARR Header overhead is not included            in this value
            	**type**\:  int
            
            	**range:** 0..16384
            
            	**units**\: octets
            
            .. attribute:: cipslaicmpechotmplrowstatus
            
            	The status of the conceptual ICMP echo template control row. When the status is active, all the read\-create objects in that  row can be modified
            	**type**\:   :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            .. attribute:: cipslaicmpechotmplsrcaddr
            
            	A string which specifies the IP address of the source
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cipslaicmpechotmplsrcaddrtype
            
            	An enumerated value which specifies the IP address type of the source. It must be used along with the cipslaIcmpEchoTmplSrcAddr object
            	**type**\:   :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            .. attribute:: cipslaicmpechotmplstatshours
            
            	The maximum number of hours for which statistics are maintained. Specifically this is the number of hourly  groups to keep before rolling over.  The value of one is not advisable because the hourly group will close and immediately be deleted before the network management station will have the opportunity to retrieve the statistics.  The value of zero will shut off data collection
            	**type**\:  int
            
            	**range:** 0..25
            
            	**units**\: hours
            
            .. attribute:: cipslaicmpechotmplstoragetype
            
            	The storage type of this conceptual row
            	**type**\:   :py:class:`StorageType <ydk.models.cisco_ios_xe.SNMPv2_TC.StorageType>`
            
            .. attribute:: cipslaicmpechotmplthreshold
            
            	This object defines an administrative threshold limit. If the IP SLA operation time exceeds this limit and if the condition specified in cipslaIcmpEchoTmplHistFilter is satisfied, one threshold crossing occurrence will be counted
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**units**\: milliseconds
            
            .. attribute:: cipslaicmpechotmpltimeout
            
            	Specifies the duration to wait for a IP SLA operation completion.   For connection oriented protocols, this may cause the connection to be closed by the operation.  Once closed, it will be assumed that the connection reestablishment will be performed.  To prevent unwanted closure of connections, be sure to set this value to a realistic connection timeout
            	**type**\:  int
            
            	**range:** 0..604800000
            
            	**units**\: milliseconds
            
            .. attribute:: cipslaicmpechotmpltos
            
            	This object represents the type of service octet in an IP header
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: cipslaicmpechotmplverifydata
            
            	When set to true, the resulting data in each IP SLA operation is compared with the expected data.  This includes checking header information (if possible) and exact packet size
            	**type**\:  bool
            
            .. attribute:: cipslaicmpechotmplvrfname
            
            	This field is used to specify the VRF name with which the IP SLA operation will be used. For regular IP SLA operation this field should not be configured. The agent will use this field to identify the VRF routing table for this operation
            	**type**\:  str
            
            	**length:** 0..32
            
            

            """

            _prefix = 'CISCO-IPSLA-ECHO-MIB'
            _revision = '2007-08-16'

            def __init__(self):
                super(CISCOIPSLAECHOMIB.Cipslaicmpechotmpltable.Cipslaicmpechotmplentry, self).__init__()

                self.yang_name = "cipslaIcmpEchoTmplEntry"
                self.yang_parent_name = "cipslaIcmpEchoTmplTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.cipslaicmpechotmplname = YLeaf(YType.str, "cipslaIcmpEchoTmplName")

                self.cipslaicmpechotmpldescription = YLeaf(YType.str, "cipslaIcmpEchoTmplDescription")

                self.cipslaicmpechotmpldistbuckets = YLeaf(YType.uint32, "cipslaIcmpEchoTmplDistBuckets")

                self.cipslaicmpechotmpldistinterval = YLeaf(YType.uint32, "cipslaIcmpEchoTmplDistInterval")

                self.cipslaicmpechotmplhistbuckets = YLeaf(YType.uint32, "cipslaIcmpEchoTmplHistBuckets")

                self.cipslaicmpechotmplhistfilter = YLeaf(YType.enumeration, "cipslaIcmpEchoTmplHistFilter")

                self.cipslaicmpechotmplhistlives = YLeaf(YType.uint32, "cipslaIcmpEchoTmplHistLives")

                self.cipslaicmpechotmplreqdatasize = YLeaf(YType.uint32, "cipslaIcmpEchoTmplReqDataSize")

                self.cipslaicmpechotmplrowstatus = YLeaf(YType.enumeration, "cipslaIcmpEchoTmplRowStatus")

                self.cipslaicmpechotmplsrcaddr = YLeaf(YType.str, "cipslaIcmpEchoTmplSrcAddr")

                self.cipslaicmpechotmplsrcaddrtype = YLeaf(YType.enumeration, "cipslaIcmpEchoTmplSrcAddrType")

                self.cipslaicmpechotmplstatshours = YLeaf(YType.uint32, "cipslaIcmpEchoTmplStatsHours")

                self.cipslaicmpechotmplstoragetype = YLeaf(YType.enumeration, "cipslaIcmpEchoTmplStorageType")

                self.cipslaicmpechotmplthreshold = YLeaf(YType.uint32, "cipslaIcmpEchoTmplThreshold")

                self.cipslaicmpechotmpltimeout = YLeaf(YType.uint32, "cipslaIcmpEchoTmplTimeOut")

                self.cipslaicmpechotmpltos = YLeaf(YType.uint32, "cipslaIcmpEchoTmplTOS")

                self.cipslaicmpechotmplverifydata = YLeaf(YType.boolean, "cipslaIcmpEchoTmplVerifyData")

                self.cipslaicmpechotmplvrfname = YLeaf(YType.str, "cipslaIcmpEchoTmplVrfName")
                self._segment_path = lambda: "cipslaIcmpEchoTmplEntry" + "[cipslaIcmpEchoTmplName='" + self.cipslaicmpechotmplname.get() + "']"
                self._absolute_path = lambda: "CISCO-IPSLA-ECHO-MIB:CISCO-IPSLA-ECHO-MIB/cipslaIcmpEchoTmplTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIPSLAECHOMIB.Cipslaicmpechotmpltable.Cipslaicmpechotmplentry, ['cipslaicmpechotmplname', 'cipslaicmpechotmpldescription', 'cipslaicmpechotmpldistbuckets', 'cipslaicmpechotmpldistinterval', 'cipslaicmpechotmplhistbuckets', 'cipslaicmpechotmplhistfilter', 'cipslaicmpechotmplhistlives', 'cipslaicmpechotmplreqdatasize', 'cipslaicmpechotmplrowstatus', 'cipslaicmpechotmplsrcaddr', 'cipslaicmpechotmplsrcaddrtype', 'cipslaicmpechotmplstatshours', 'cipslaicmpechotmplstoragetype', 'cipslaicmpechotmplthreshold', 'cipslaicmpechotmpltimeout', 'cipslaicmpechotmpltos', 'cipslaicmpechotmplverifydata', 'cipslaicmpechotmplvrfname'], name, value)

            class Cipslaicmpechotmplhistfilter(Enum):
                """
                Cipslaicmpechotmplhistfilter

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



    class Cipslatcpconntmpltable(Entity):
        """
        A table that contains TCP connect template specific definitions.
        
        .. attribute:: cipslatcpconntmplentry
        
        	A row entry representing an IPSLA TCP connect template
        	**type**\: list of    :py:class:`Cipslatcpconntmplentry <ydk.models.cisco_ios_xe.CISCO_IPSLA_ECHO_MIB.CISCOIPSLAECHOMIB.Cipslatcpconntmpltable.Cipslatcpconntmplentry>`
        
        

        """

        _prefix = 'CISCO-IPSLA-ECHO-MIB'
        _revision = '2007-08-16'

        def __init__(self):
            super(CISCOIPSLAECHOMIB.Cipslatcpconntmpltable, self).__init__()

            self.yang_name = "cipslaTcpConnTmplTable"
            self.yang_parent_name = "CISCO-IPSLA-ECHO-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"cipslaTcpConnTmplEntry" : ("cipslatcpconntmplentry", CISCOIPSLAECHOMIB.Cipslatcpconntmpltable.Cipslatcpconntmplentry)}

            self.cipslatcpconntmplentry = YList(self)
            self._segment_path = lambda: "cipslaTcpConnTmplTable"
            self._absolute_path = lambda: "CISCO-IPSLA-ECHO-MIB:CISCO-IPSLA-ECHO-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIPSLAECHOMIB.Cipslatcpconntmpltable, [], name, value)


        class Cipslatcpconntmplentry(Entity):
            """
            A row entry representing an IPSLA TCP connect template.
            
            .. attribute:: cipslatcpconntmplname  <key>
            
            	A string which specifies the TCP connect template name
            	**type**\:  str
            
            	**length:** 1..64
            
            .. attribute:: cipslatcpconntmplcontrolenable
            
            	If this object is enabled, then the IP SLA application will send control messages to a responder, residing on the target router to respond to the data request packets being sent by the source router
            	**type**\:  bool
            
            .. attribute:: cipslatcpconntmpldescription
            
            	A string which provides description for the TCP connect template
            	**type**\:  str
            
            	**length:** 0..128
            
            .. attribute:: cipslatcpconntmpldistbuckets
            
            	The maximum number of statistical distribution buckets to accumulate.  Since this index does not rollover, only the first cipslaTcpConnTmplDistBuckets will be kept.  The last cipslaTcpConnTmplDistBuckets will contain all entries from its distribution interval start point to infinity
            	**type**\:  int
            
            	**range:** 1..20
            
            .. attribute:: cipslatcpconntmpldistinterval
            
            	The statistical distribution buckets interval.  Distribution Bucket Example\:  cipslaTcpConnTmplDistBuckets = 5 buckets cipslaTcpConnTmplDistInterval = 10 milliseconds  \| Bucket 1 \| Bucket 2 \| Bucket 3 \| Bucket 4 \| Bucket 5  \| \|  0\-9 ms  \| 10\-19 ms \| 20\-29 ms \| 30\-39 ms \| 40\-Inf ms \|  Odd Example\:  cipslaTcpConnTmplDistBuckets = 1 buckets cipslaTcpConnTmplDistInterval = 10 milliseconds  \| Bucket 1  \| \|  0\-Inf ms \|  Thus, this odd example shows that the value of cipslaTcpConnTmplDistInterval does not apply when cipslaTcpConnTmplDistBuckets is one
            	**type**\:  int
            
            	**range:** 1..100
            
            	**units**\: milliseconds
            
            .. attribute:: cipslatcpconntmplhistbuckets
            
            	The maximum number of history buckets to record. This value should be set to the number of operations  to keep per lifetime.  After cipslaTcpConnTmplHistBuckets are filled, the  oldest entries are deleted and the most recent cipslaTcpConnTmplHistBuckets buckets are retained
            	**type**\:  int
            
            	**range:** 1..60
            
            .. attribute:: cipslatcpconntmplhistfilter
            
            	Defines a filter for adding RTT results to the history buffer\:  none(1)          \- no history is recorded all(2)           \- the results of all completion times                     and failed completions are recorded overThreshold(3) \- the results of completion times                    over cipslaTcpConnTmplThreshold are                     recorded. failures(4)      \- the results of failed operations (only)                     are recorded
            	**type**\:   :py:class:`Cipslatcpconntmplhistfilter <ydk.models.cisco_ios_xe.CISCO_IPSLA_ECHO_MIB.CISCOIPSLAECHOMIB.Cipslatcpconntmpltable.Cipslatcpconntmplentry.Cipslatcpconntmplhistfilter>`
            
            .. attribute:: cipslatcpconntmplhistlives
            
            	The maximum number of history lives to record.  A life is defined by the countdown (or transition) to zero  by the cipslaAutoGroupScheduleLife object.  A new life is created when the same conceptual control row is restarted via the transition of the  cipslaAutoGroupScheduleLife object and its subsequent  countdown.  The value of zero will shut off all data collection
            	**type**\:  int
            
            	**range:** 0..2
            
            .. attribute:: cipslatcpconntmplrowstatus
            
            	The status of the conceptual tcp connect control row. When the status is active, all the read\-create objects  in that row can be modified
            	**type**\:   :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            .. attribute:: cipslatcpconntmplsrcaddr
            
            	A string which specifies the IP address of the source
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cipslatcpconntmplsrcaddrtype
            
            	An enumerated value which specifies the IP address type of the source. It must be used along with the cipslaTcpConnTmplSrcAddr object
            	**type**\:   :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            .. attribute:: cipslatcpconntmplsrcport
            
            	This object represents the source's port number. If this object is not specified, the application will get a port allocated by the system
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: cipslatcpconntmplstatshours
            
            	The maximum number of hours for which statistics are maintained. Specifically this is the number of hourly  groups to keep before rolling over.  The value of one is not advisable because the hourly group will close and immediately be deleted before the network management station will have the opportunity to retrieve the statistics.  The value of zero will shut off data collection
            	**type**\:  int
            
            	**range:** 0..25
            
            	**units**\: hours
            
            .. attribute:: cipslatcpconntmplstoragetype
            
            	The storage type of this conceptual row
            	**type**\:   :py:class:`StorageType <ydk.models.cisco_ios_xe.SNMPv2_TC.StorageType>`
            
            .. attribute:: cipslatcpconntmplthreshold
            
            	This object defines an administrative threshold limit. If the IP SLA operation time exceeds this limit and if the condition specified in cipslaTcpConnTmplHistFilter is  satisfied, one threshold crossing occurrence will be counted
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**units**\: milliseconds
            
            .. attribute:: cipslatcpconntmpltimeout
            
            	Specifies the duration to wait for an IP SLA operation completion.  For connection oriented protocols, this may cause the connection to be closed by the operation.  Once closed, it will be assumed that the connection reestablishment will be performed.  To prevent unwanted closure of connections, be sure to set this value to a realistic connection timeout
            	**type**\:  int
            
            	**range:** 0..604800000
            
            	**units**\: milliseconds
            
            .. attribute:: cipslatcpconntmpltos
            
            	This object represents the type of service octet in an IP header
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: cipslatcpconntmplverifydata
            
            	When set to true, the resulting data in each IP SLA operation is compared with the expected data.  This includes checking header information (if possible) and exact packet size
            	**type**\:  bool
            
            

            """

            _prefix = 'CISCO-IPSLA-ECHO-MIB'
            _revision = '2007-08-16'

            def __init__(self):
                super(CISCOIPSLAECHOMIB.Cipslatcpconntmpltable.Cipslatcpconntmplentry, self).__init__()

                self.yang_name = "cipslaTcpConnTmplEntry"
                self.yang_parent_name = "cipslaTcpConnTmplTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.cipslatcpconntmplname = YLeaf(YType.str, "cipslaTcpConnTmplName")

                self.cipslatcpconntmplcontrolenable = YLeaf(YType.boolean, "cipslaTcpConnTmplControlEnable")

                self.cipslatcpconntmpldescription = YLeaf(YType.str, "cipslaTcpConnTmplDescription")

                self.cipslatcpconntmpldistbuckets = YLeaf(YType.uint32, "cipslaTcpConnTmplDistBuckets")

                self.cipslatcpconntmpldistinterval = YLeaf(YType.uint32, "cipslaTcpConnTmplDistInterval")

                self.cipslatcpconntmplhistbuckets = YLeaf(YType.uint32, "cipslaTcpConnTmplHistBuckets")

                self.cipslatcpconntmplhistfilter = YLeaf(YType.enumeration, "cipslaTcpConnTmplHistFilter")

                self.cipslatcpconntmplhistlives = YLeaf(YType.uint32, "cipslaTcpConnTmplHistLives")

                self.cipslatcpconntmplrowstatus = YLeaf(YType.enumeration, "cipslaTcpConnTmplRowStatus")

                self.cipslatcpconntmplsrcaddr = YLeaf(YType.str, "cipslaTcpConnTmplSrcAddr")

                self.cipslatcpconntmplsrcaddrtype = YLeaf(YType.enumeration, "cipslaTcpConnTmplSrcAddrType")

                self.cipslatcpconntmplsrcport = YLeaf(YType.uint16, "cipslaTcpConnTmplSrcPort")

                self.cipslatcpconntmplstatshours = YLeaf(YType.uint32, "cipslaTcpConnTmplStatsHours")

                self.cipslatcpconntmplstoragetype = YLeaf(YType.enumeration, "cipslaTcpConnTmplStorageType")

                self.cipslatcpconntmplthreshold = YLeaf(YType.uint32, "cipslaTcpConnTmplThreshold")

                self.cipslatcpconntmpltimeout = YLeaf(YType.uint32, "cipslaTcpConnTmplTimeOut")

                self.cipslatcpconntmpltos = YLeaf(YType.uint32, "cipslaTcpConnTmplTOS")

                self.cipslatcpconntmplverifydata = YLeaf(YType.boolean, "cipslaTcpConnTmplVerifyData")
                self._segment_path = lambda: "cipslaTcpConnTmplEntry" + "[cipslaTcpConnTmplName='" + self.cipslatcpconntmplname.get() + "']"
                self._absolute_path = lambda: "CISCO-IPSLA-ECHO-MIB:CISCO-IPSLA-ECHO-MIB/cipslaTcpConnTmplTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIPSLAECHOMIB.Cipslatcpconntmpltable.Cipslatcpconntmplentry, ['cipslatcpconntmplname', 'cipslatcpconntmplcontrolenable', 'cipslatcpconntmpldescription', 'cipslatcpconntmpldistbuckets', 'cipslatcpconntmpldistinterval', 'cipslatcpconntmplhistbuckets', 'cipslatcpconntmplhistfilter', 'cipslatcpconntmplhistlives', 'cipslatcpconntmplrowstatus', 'cipslatcpconntmplsrcaddr', 'cipslatcpconntmplsrcaddrtype', 'cipslatcpconntmplsrcport', 'cipslatcpconntmplstatshours', 'cipslatcpconntmplstoragetype', 'cipslatcpconntmplthreshold', 'cipslatcpconntmpltimeout', 'cipslatcpconntmpltos', 'cipslatcpconntmplverifydata'], name, value)

            class Cipslatcpconntmplhistfilter(Enum):
                """
                Cipslatcpconntmplhistfilter

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



    class Cipslaudpechotmpltable(Entity):
        """
        A table that contains UDP echo template specific definitions.
        
        .. attribute:: cipslaudpechotmplentry
        
        	A row entry representing an IPSLA UDP echo template
        	**type**\: list of    :py:class:`Cipslaudpechotmplentry <ydk.models.cisco_ios_xe.CISCO_IPSLA_ECHO_MIB.CISCOIPSLAECHOMIB.Cipslaudpechotmpltable.Cipslaudpechotmplentry>`
        
        

        """

        _prefix = 'CISCO-IPSLA-ECHO-MIB'
        _revision = '2007-08-16'

        def __init__(self):
            super(CISCOIPSLAECHOMIB.Cipslaudpechotmpltable, self).__init__()

            self.yang_name = "cipslaUdpEchoTmplTable"
            self.yang_parent_name = "CISCO-IPSLA-ECHO-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"cipslaUdpEchoTmplEntry" : ("cipslaudpechotmplentry", CISCOIPSLAECHOMIB.Cipslaudpechotmpltable.Cipslaudpechotmplentry)}

            self.cipslaudpechotmplentry = YList(self)
            self._segment_path = lambda: "cipslaUdpEchoTmplTable"
            self._absolute_path = lambda: "CISCO-IPSLA-ECHO-MIB:CISCO-IPSLA-ECHO-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIPSLAECHOMIB.Cipslaudpechotmpltable, [], name, value)


        class Cipslaudpechotmplentry(Entity):
            """
            A row entry representing an IPSLA UDP echo template.
            
            .. attribute:: cipslaudpechotmplname  <key>
            
            	A string which specifies the UDP echo template name
            	**type**\:  str
            
            	**length:** 1..64
            
            .. attribute:: cipslaudpechotmplcontrolenable
            
            	If this object is enabled, then the IP SLA application will send control messages to a responder, residing on the target router to respond to the data request packets being sent by the source router
            	**type**\:  bool
            
            .. attribute:: cipslaudpechotmpldescription
            
            	A string which provides description to the UDP echo template
            	**type**\:  str
            
            	**length:** 0..128
            
            .. attribute:: cipslaudpechotmpldistbuckets
            
            	The maximum number of statistical distribution buckets to accumulate.  Since this index does not rollover, only the first cipslaUdpEchoTmplStatsNumDistBuckets will be kept.  The last cipslaUdpEchoTmplStatsNumDistBuckets will contain all entries from its distribution interval start point to infinity
            	**type**\:  int
            
            	**range:** 1..20
            
            .. attribute:: cipslaudpechotmpldistinterval
            
            	The statistical distribution buckets interval.  Distribution Bucket Example\:  cipslaUdpEchoTmplDistBuckets = 5 buckets cipslaUdpEchoTmplDistInterval = 10 milliseconds  \| Bucket 1 \| Bucket 2 \| Bucket 3 \| Bucket 4 \| Bucket 5  \| \|  0\-9 ms  \| 10\-19 ms \| 20\-29 ms \| 30\-39 ms \| 40\-Inf ms \|  Odd Example\:  cipslaUdpEchoTmplDistBuckets = 1 buckets cipslaUdpEchoTmplDistInterval = 10 milliseconds  \| Bucket 1  \| \|  0\-Inf ms \|  Thus, this odd example shows that the value of cipslaUdpEchoTmplDistInterval does not apply when cipslaUdpEchoTmplDistBuckets is one
            	**type**\:  int
            
            	**range:** 1..100
            
            	**units**\: milliseconds
            
            .. attribute:: cipslaudpechotmplhistbuckets
            
            	The maximum number of history buckets to record. This value should be set to the number of operations  to keep per lifetime.  After cipslaUdpEchoTmplHistBuckets are filled, the  oldest entries are deleted and the most recent cipslaUdpEchoTmplHistBuckets buckets are retained
            	**type**\:  int
            
            	**range:** 1..60
            
            .. attribute:: cipslaudpechotmplhistfilter
            
            	Defines a filter for adding RTT results to the history buffer\:  none(1)          \- no history is recorded all(2)           \- the results of all completion times                     and failed completions are recorded overThreshold(3) \- the results of completion times                    over cipslaUdpEchoTmplThreshold are                     recorded. failures(4)      \- the results of failed operations (only)                     are recorded
            	**type**\:   :py:class:`Cipslaudpechotmplhistfilter <ydk.models.cisco_ios_xe.CISCO_IPSLA_ECHO_MIB.CISCOIPSLAECHOMIB.Cipslaudpechotmpltable.Cipslaudpechotmplentry.Cipslaudpechotmplhistfilter>`
            
            .. attribute:: cipslaudpechotmplhistlives
            
            	The maximum number of history lives to record.  A life is defined by the countdown (or transition) to zero  by the cipslaAutoGroupScheduleLife object.  A new life is created when the same conceptual control row is restarted via the transition of the  cipslaAutoGroupScheduleLife object and its subsequent  countdown.  The value of zero will shut off all data collection
            	**type**\:  int
            
            	**range:** 0..2
            
            .. attribute:: cipslaudpechotmplreqdatasize
            
            	This object represents the number of octets to be placed into the ARR Data portion of the request message, when using SNA protocols.  For non\-ARR protocols' RTT request/responses, this value represents the native payload size.  REMEMBER\:  The ARR Header overhead is not included            in this value
            	**type**\:  int
            
            	**range:** 4..1500
            
            	**units**\: octets
            
            .. attribute:: cipslaudpechotmplrowstatus
            
            	The status of the conceptual UDP echo template control row. When the status is active, all the read\-create objects in  that row can be modified
            	**type**\:   :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            .. attribute:: cipslaudpechotmplsrcaddr
            
            	A string which specifies the IP address of the source
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cipslaudpechotmplsrcaddrtype
            
            	An enumerated value which specifies the IP address type of the source. It must be used along with the cipslaUdpEchoTmplSrcAddr object
            	**type**\:   :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            .. attribute:: cipslaudpechotmplsrcport
            
            	This object represents the source's port number. If this object is not specified, the application will get a port allocated by the system
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: cipslaudpechotmplstatshours
            
            	The maximum number of hours for which statistics are maintained. Specifically this is the number of hourly  groups to keep before rolling over.  The value of one is not advisable because the hourly group will close and immediately be deleted before the network management station will have the opportunity to retrieve the statistics.  The value of zero will shut off data collection
            	**type**\:  int
            
            	**range:** 0..25
            
            	**units**\: hours
            
            .. attribute:: cipslaudpechotmplstoragetype
            
            	The storage type of this conceptual row
            	**type**\:   :py:class:`StorageType <ydk.models.cisco_ios_xe.SNMPv2_TC.StorageType>`
            
            .. attribute:: cipslaudpechotmplthreshold
            
            	This object defines an administrative threshold limit. If the IP SLA operation time exceeds this limit and if the condition specified in cipslaUdpEchoTmplHistFilter is  satisfied, one threshold crossing occurrence will be counted
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**units**\: milliseconds
            
            .. attribute:: cipslaudpechotmpltimeout
            
            	Specifies the duration to wait for an IP SLA operation completion.  For connection oriented protocols, this may cause the connection to be closed by the operation.  Once closed, it will be assumed that the connection reestablishment will be performed.  To prevent unwanted closure of connections, be sure to set this value to a realistic connection timeout
            	**type**\:  int
            
            	**range:** 0..604800000
            
            	**units**\: milliseconds
            
            .. attribute:: cipslaudpechotmpltos
            
            	This object represents the type of service octet in an IP header
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: cipslaudpechotmplverifydata
            
            	When set to true, the resulting data in each IP SLA operation is compared with the expected data.  This includes checking header information (if possible) and exact packet size
            	**type**\:  bool
            
            .. attribute:: cipslaudpechotmplvrfname
            
            	This field is used to specify the VRF name with which the IP SLA operation will be used. For regular IP SLA operation this field should not be configured. The agent will use this field to identify the VRF routing Table for this operation
            	**type**\:  str
            
            	**length:** 0..32
            
            

            """

            _prefix = 'CISCO-IPSLA-ECHO-MIB'
            _revision = '2007-08-16'

            def __init__(self):
                super(CISCOIPSLAECHOMIB.Cipslaudpechotmpltable.Cipslaudpechotmplentry, self).__init__()

                self.yang_name = "cipslaUdpEchoTmplEntry"
                self.yang_parent_name = "cipslaUdpEchoTmplTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.cipslaudpechotmplname = YLeaf(YType.str, "cipslaUdpEchoTmplName")

                self.cipslaudpechotmplcontrolenable = YLeaf(YType.boolean, "cipslaUdpEchoTmplControlEnable")

                self.cipslaudpechotmpldescription = YLeaf(YType.str, "cipslaUdpEchoTmplDescription")

                self.cipslaudpechotmpldistbuckets = YLeaf(YType.uint32, "cipslaUdpEchoTmplDistBuckets")

                self.cipslaudpechotmpldistinterval = YLeaf(YType.uint32, "cipslaUdpEchoTmplDistInterval")

                self.cipslaudpechotmplhistbuckets = YLeaf(YType.uint32, "cipslaUdpEchoTmplHistBuckets")

                self.cipslaudpechotmplhistfilter = YLeaf(YType.enumeration, "cipslaUdpEchoTmplHistFilter")

                self.cipslaudpechotmplhistlives = YLeaf(YType.uint32, "cipslaUdpEchoTmplHistLives")

                self.cipslaudpechotmplreqdatasize = YLeaf(YType.uint32, "cipslaUdpEchoTmplReqDataSize")

                self.cipslaudpechotmplrowstatus = YLeaf(YType.enumeration, "cipslaUdpEchoTmplRowStatus")

                self.cipslaudpechotmplsrcaddr = YLeaf(YType.str, "cipslaUdpEchoTmplSrcAddr")

                self.cipslaudpechotmplsrcaddrtype = YLeaf(YType.enumeration, "cipslaUdpEchoTmplSrcAddrType")

                self.cipslaudpechotmplsrcport = YLeaf(YType.uint16, "cipslaUdpEchoTmplSrcPort")

                self.cipslaudpechotmplstatshours = YLeaf(YType.uint32, "cipslaUdpEchoTmplStatsHours")

                self.cipslaudpechotmplstoragetype = YLeaf(YType.enumeration, "cipslaUdpEchoTmplStorageType")

                self.cipslaudpechotmplthreshold = YLeaf(YType.uint32, "cipslaUdpEchoTmplThreshold")

                self.cipslaudpechotmpltimeout = YLeaf(YType.uint32, "cipslaUdpEchoTmplTimeOut")

                self.cipslaudpechotmpltos = YLeaf(YType.uint32, "cipslaUdpEchoTmplTOS")

                self.cipslaudpechotmplverifydata = YLeaf(YType.boolean, "cipslaUdpEchoTmplVerifyData")

                self.cipslaudpechotmplvrfname = YLeaf(YType.str, "cipslaUdpEchoTmplVrfName")
                self._segment_path = lambda: "cipslaUdpEchoTmplEntry" + "[cipslaUdpEchoTmplName='" + self.cipslaudpechotmplname.get() + "']"
                self._absolute_path = lambda: "CISCO-IPSLA-ECHO-MIB:CISCO-IPSLA-ECHO-MIB/cipslaUdpEchoTmplTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIPSLAECHOMIB.Cipslaudpechotmpltable.Cipslaudpechotmplentry, ['cipslaudpechotmplname', 'cipslaudpechotmplcontrolenable', 'cipslaudpechotmpldescription', 'cipslaudpechotmpldistbuckets', 'cipslaudpechotmpldistinterval', 'cipslaudpechotmplhistbuckets', 'cipslaudpechotmplhistfilter', 'cipslaudpechotmplhistlives', 'cipslaudpechotmplreqdatasize', 'cipslaudpechotmplrowstatus', 'cipslaudpechotmplsrcaddr', 'cipslaudpechotmplsrcaddrtype', 'cipslaudpechotmplsrcport', 'cipslaudpechotmplstatshours', 'cipslaudpechotmplstoragetype', 'cipslaudpechotmplthreshold', 'cipslaudpechotmpltimeout', 'cipslaudpechotmpltos', 'cipslaudpechotmplverifydata', 'cipslaudpechotmplvrfname'], name, value)

            class Cipslaudpechotmplhistfilter(Enum):
                """
                Cipslaudpechotmplhistfilter

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


    def clone_ptr(self):
        self._top_entity = CISCOIPSLAECHOMIB()
        return self._top_entity

