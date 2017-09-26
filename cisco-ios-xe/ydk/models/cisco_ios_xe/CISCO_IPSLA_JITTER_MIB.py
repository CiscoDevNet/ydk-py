""" CISCO_IPSLA_JITTER_MIB 

This MIB module defines templates for IP SLA operations of UDP
Jitter and ICMP Jitter. 

The UDP Jitter operation is designed to measure the delay 
variance and packet loss in IP networks by generating synthetic 
UDP traffic. 

The ICMP Jitter operation provides capability to measure metrics 
such as RTT (Round Trip Time), jitter, packet loss, one\-way 
latency by sending ICMP Timestamp stream to the destination 
devices.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CISCOIPSLAJITTERMIB(Entity):
    """
    
    
    .. attribute:: cipslaicmpjittertmpltable
    
    	A table that contains ICMP jitter template specific definitions
    	**type**\:   :py:class:`Cipslaicmpjittertmpltable <ydk.models.cisco_ios_xe.CISCO_IPSLA_JITTER_MIB.CISCOIPSLAJITTERMIB.Cipslaicmpjittertmpltable>`
    
    .. attribute:: cipslaudpjittertmpltable
    
    	A table that contains UDP jitter template specific definitions
    	**type**\:   :py:class:`Cipslaudpjittertmpltable <ydk.models.cisco_ios_xe.CISCO_IPSLA_JITTER_MIB.CISCOIPSLAJITTERMIB.Cipslaudpjittertmpltable>`
    
    

    """

    _prefix = 'CISCO-IPSLA-JITTER-MIB'
    _revision = '2007-07-24'

    def __init__(self):
        super(CISCOIPSLAJITTERMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-IPSLA-JITTER-MIB"
        self.yang_parent_name = "CISCO-IPSLA-JITTER-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"cipslaIcmpJitterTmplTable" : ("cipslaicmpjittertmpltable", CISCOIPSLAJITTERMIB.Cipslaicmpjittertmpltable), "cipslaUdpJitterTmplTable" : ("cipslaudpjittertmpltable", CISCOIPSLAJITTERMIB.Cipslaudpjittertmpltable)}
        self._child_list_classes = {}

        self.cipslaicmpjittertmpltable = CISCOIPSLAJITTERMIB.Cipslaicmpjittertmpltable()
        self.cipslaicmpjittertmpltable.parent = self
        self._children_name_map["cipslaicmpjittertmpltable"] = "cipslaIcmpJitterTmplTable"
        self._children_yang_names.add("cipslaIcmpJitterTmplTable")

        self.cipslaudpjittertmpltable = CISCOIPSLAJITTERMIB.Cipslaudpjittertmpltable()
        self.cipslaudpjittertmpltable.parent = self
        self._children_name_map["cipslaudpjittertmpltable"] = "cipslaUdpJitterTmplTable"
        self._children_yang_names.add("cipslaUdpJitterTmplTable")
        self._segment_path = lambda: "CISCO-IPSLA-JITTER-MIB:CISCO-IPSLA-JITTER-MIB"


    class Cipslaicmpjittertmpltable(Entity):
        """
        A table that contains ICMP jitter template specific definitions.
        
        .. attribute:: cipslaicmpjittertmplentry
        
        	A row entry representing an IP SLA ICMP Jitter template
        	**type**\: list of    :py:class:`Cipslaicmpjittertmplentry <ydk.models.cisco_ios_xe.CISCO_IPSLA_JITTER_MIB.CISCOIPSLAJITTERMIB.Cipslaicmpjittertmpltable.Cipslaicmpjittertmplentry>`
        
        

        """

        _prefix = 'CISCO-IPSLA-JITTER-MIB'
        _revision = '2007-07-24'

        def __init__(self):
            super(CISCOIPSLAJITTERMIB.Cipslaicmpjittertmpltable, self).__init__()

            self.yang_name = "cipslaIcmpJitterTmplTable"
            self.yang_parent_name = "CISCO-IPSLA-JITTER-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"cipslaIcmpJitterTmplEntry" : ("cipslaicmpjittertmplentry", CISCOIPSLAJITTERMIB.Cipslaicmpjittertmpltable.Cipslaicmpjittertmplentry)}

            self.cipslaicmpjittertmplentry = YList(self)
            self._segment_path = lambda: "cipslaIcmpJitterTmplTable"
            self._absolute_path = lambda: "CISCO-IPSLA-JITTER-MIB:CISCO-IPSLA-JITTER-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIPSLAJITTERMIB.Cipslaicmpjittertmpltable, [], name, value)


        class Cipslaicmpjittertmplentry(Entity):
            """
            A row entry representing an IP SLA ICMP Jitter template.
            
            .. attribute:: cipslaicmpjittertmplname  <key>
            
            	A string which specifies the ICMP jitter template name
            	**type**\:  str
            
            	**length:** 1..64
            
            .. attribute:: cipslaicmpjittertmpldescription
            
            	A string which provides description of ICMP Jitter template
            	**type**\:  str
            
            	**length:** 0..128
            
            .. attribute:: cipslaicmpjittertmpldistbuckets
            
            	The maximum number of statistical distribution buckets to accumulate.  Since this index does not rollover, only the first cipslaIcmpJitterTmplDistBuckets will be kept.  The last bucket will contain all entries from its  distribution interval start point to infinity
            	**type**\:  int
            
            	**range:** 1..20
            
            .. attribute:: cipslaicmpjittertmpldistinterval
            
            	The statistical distribution buckets interval.  Distribution Bucket Example\:  cipslaIcmpJitterTmplDistBuckets = 5 buckets cipslaIcmpJitterTmplDistInterval = 10 milliseconds  \| Bucket 1 \| Bucket 2 \| Bucket 3 \| Bucket 4 \| Bucket 5  \| \|  0\-9 ms  \| 10\-19 ms \| 20\-29 ms \| 30\-39 ms \| 40\-Inf ms \|  Odd Example\:  cipslaIcmpJitterTmplDistBuckets = 1 buckets cipslaIcmpJitterTmplDistInterval = 10 milliseconds  \| Bucket 1  \| \|  0\-Inf ms \|  Thus, this odd example shows that the value of cipslaIcmpJitterTmplDistInterval does not apply when cipslaIcmpJitterTmplDistBuckets is one
            	**type**\:  int
            
            	**range:** 1..100
            
            	**units**\: milliseconds
            
            .. attribute:: cipslaicmpjittertmplinterval
            
            	This value represents the inter\-packet delay between packets and is in milliseconds
            	**type**\:  int
            
            	**range:** 4..60000
            
            	**units**\: milliseconds
            
            .. attribute:: cipslaicmpjittertmplnumpkts
            
            	This value represents the number of packets that need to be transmitted
            	**type**\:  int
            
            	**range:** 1..60000
            
            	**units**\: packets
            
            .. attribute:: cipslaicmpjittertmplrowstatus
            
            	The status of the conceptual ICMP jitter template control row. When the status is active, all the read\-create objects in  that row can be modified
            	**type**\:   :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            .. attribute:: cipslaicmpjittertmplsrcaddr
            
            	A string which specifies the IP address of the source
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cipslaicmpjittertmplsrcaddrtype
            
            	An enumerated value which specifies the IP address type of the source. It must be used along with the cipslaIcmpJitterTmplSrcAddr object
            	**type**\:   :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            .. attribute:: cipslaicmpjittertmplstatshours
            
            	The maximum number of hourss for which statistics are maintained. Specifically this is the number of hourly groups to keep before rolling over.  The value of one is not advisable because the hourly group will close and immediately be deleted before the network management station will have the opportunity to retrieve the statistics.  The value of zero will shut off data collection
            	**type**\:  int
            
            	**range:** 0..25
            
            	**units**\: hours
            
            .. attribute:: cipslaicmpjittertmplstoragetype
            
            	The storage type of this conceptual row
            	**type**\:   :py:class:`StorageType <ydk.models.cisco_ios_xe.SNMPv2_TC.StorageType>`
            
            .. attribute:: cipslaicmpjittertmplthreshold
            
            	This object defines an administrative threshold limit. If the IP SLA operation time exceeds this limit, then  one threshold crossing occurrence will be counted
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**units**\: milliseconds
            
            .. attribute:: cipslaicmpjittertmpltimeout
            
            	Specifies the duration to wait for a IP SLA operation completion.  For connection oriented protocols, this may cause the connection to be closed by the operation.  Once closed, it will be assumed that the connection reestablishment will be performed.  To prevent unwanted closure of connections, be sure to set this value to a realistic connection timeout
            	**type**\:  int
            
            	**range:** 0..604800000
            
            	**units**\: milliseconds
            
            .. attribute:: cipslaicmpjittertmpltos
            
            	This object represents the type of service octet in an IP header
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: cipslaicmpjittertmplverifydata
            
            	When set to true, the resulting data in each IP SLA operation is compared with the expected data.  This includes checking header information (if possible) and exact packet size
            	**type**\:  bool
            
            .. attribute:: cipslaicmpjittertmplvrfname
            
            	This field is used to specify the VRF name in which the IP SLA operation will be used. For regular IP SLA operation this field should not be configured. The agent will use this field to identify the VPN routing Table for this operation
            	**type**\:  str
            
            	**length:** 0..32
            
            

            """

            _prefix = 'CISCO-IPSLA-JITTER-MIB'
            _revision = '2007-07-24'

            def __init__(self):
                super(CISCOIPSLAJITTERMIB.Cipslaicmpjittertmpltable.Cipslaicmpjittertmplentry, self).__init__()

                self.yang_name = "cipslaIcmpJitterTmplEntry"
                self.yang_parent_name = "cipslaIcmpJitterTmplTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.cipslaicmpjittertmplname = YLeaf(YType.str, "cipslaIcmpJitterTmplName")

                self.cipslaicmpjittertmpldescription = YLeaf(YType.str, "cipslaIcmpJitterTmplDescription")

                self.cipslaicmpjittertmpldistbuckets = YLeaf(YType.uint32, "cipslaIcmpJitterTmplDistBuckets")

                self.cipslaicmpjittertmpldistinterval = YLeaf(YType.uint32, "cipslaIcmpJitterTmplDistInterval")

                self.cipslaicmpjittertmplinterval = YLeaf(YType.uint32, "cipslaIcmpJitterTmplInterval")

                self.cipslaicmpjittertmplnumpkts = YLeaf(YType.uint32, "cipslaIcmpJitterTmplNumPkts")

                self.cipslaicmpjittertmplrowstatus = YLeaf(YType.enumeration, "cipslaIcmpJitterTmplRowStatus")

                self.cipslaicmpjittertmplsrcaddr = YLeaf(YType.str, "cipslaIcmpJitterTmplSrcAddr")

                self.cipslaicmpjittertmplsrcaddrtype = YLeaf(YType.enumeration, "cipslaIcmpJitterTmplSrcAddrType")

                self.cipslaicmpjittertmplstatshours = YLeaf(YType.uint32, "cipslaIcmpJitterTmplStatsHours")

                self.cipslaicmpjittertmplstoragetype = YLeaf(YType.enumeration, "cipslaIcmpJitterTmplStorageType")

                self.cipslaicmpjittertmplthreshold = YLeaf(YType.uint32, "cipslaIcmpJitterTmplThreshold")

                self.cipslaicmpjittertmpltimeout = YLeaf(YType.uint32, "cipslaIcmpJitterTmplTimeOut")

                self.cipslaicmpjittertmpltos = YLeaf(YType.uint32, "cipslaIcmpJitterTmplTOS")

                self.cipslaicmpjittertmplverifydata = YLeaf(YType.boolean, "cipslaIcmpJitterTmplVerifyData")

                self.cipslaicmpjittertmplvrfname = YLeaf(YType.str, "cipslaIcmpJitterTmplVrfName")
                self._segment_path = lambda: "cipslaIcmpJitterTmplEntry" + "[cipslaIcmpJitterTmplName='" + self.cipslaicmpjittertmplname.get() + "']"
                self._absolute_path = lambda: "CISCO-IPSLA-JITTER-MIB:CISCO-IPSLA-JITTER-MIB/cipslaIcmpJitterTmplTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIPSLAJITTERMIB.Cipslaicmpjittertmpltable.Cipslaicmpjittertmplentry, ['cipslaicmpjittertmplname', 'cipslaicmpjittertmpldescription', 'cipslaicmpjittertmpldistbuckets', 'cipslaicmpjittertmpldistinterval', 'cipslaicmpjittertmplinterval', 'cipslaicmpjittertmplnumpkts', 'cipslaicmpjittertmplrowstatus', 'cipslaicmpjittertmplsrcaddr', 'cipslaicmpjittertmplsrcaddrtype', 'cipslaicmpjittertmplstatshours', 'cipslaicmpjittertmplstoragetype', 'cipslaicmpjittertmplthreshold', 'cipslaicmpjittertmpltimeout', 'cipslaicmpjittertmpltos', 'cipslaicmpjittertmplverifydata', 'cipslaicmpjittertmplvrfname'], name, value)


    class Cipslaudpjittertmpltable(Entity):
        """
        A table that contains UDP jitter template specific definitions.
        
        .. attribute:: cipslaudpjittertmplentry
        
        	A row entry representing an IPSLA UDP jitter template
        	**type**\: list of    :py:class:`Cipslaudpjittertmplentry <ydk.models.cisco_ios_xe.CISCO_IPSLA_JITTER_MIB.CISCOIPSLAJITTERMIB.Cipslaudpjittertmpltable.Cipslaudpjittertmplentry>`
        
        

        """

        _prefix = 'CISCO-IPSLA-JITTER-MIB'
        _revision = '2007-07-24'

        def __init__(self):
            super(CISCOIPSLAJITTERMIB.Cipslaudpjittertmpltable, self).__init__()

            self.yang_name = "cipslaUdpJitterTmplTable"
            self.yang_parent_name = "CISCO-IPSLA-JITTER-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"cipslaUdpJitterTmplEntry" : ("cipslaudpjittertmplentry", CISCOIPSLAJITTERMIB.Cipslaudpjittertmpltable.Cipslaudpjittertmplentry)}

            self.cipslaudpjittertmplentry = YList(self)
            self._segment_path = lambda: "cipslaUdpJitterTmplTable"
            self._absolute_path = lambda: "CISCO-IPSLA-JITTER-MIB:CISCO-IPSLA-JITTER-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIPSLAJITTERMIB.Cipslaudpjittertmpltable, [], name, value)


        class Cipslaudpjittertmplentry(Entity):
            """
            A row entry representing an IPSLA UDP jitter template.
            
            .. attribute:: cipslaudpjittertmplname  <key>
            
            	A string which specifies the UDP Jitter template name
            	**type**\:  str
            
            	**length:** 1..64
            
            .. attribute:: cipslaudpjittertmplcodecinterval
            
            	This field represents the inter\-packet delay between packets and is in milliseconds. This object is applicable only to UDP jitter operation  which uses codec type
            	**type**\:  int
            
            	**range:** 4..60000
            
            	**units**\: milliseconds
            
            .. attribute:: cipslaudpjittertmplcodecnumpkts
            
            	This value represents the number of packets that need to be transmitted. This value is used only for UDP jitter  operation which uses codec type
            	**type**\:  int
            
            	**range:** 1..60000
            
            	**units**\: packets
            
            .. attribute:: cipslaudpjittertmplcodecpayload
            
            	This object represents the number of octets that needs to be placed into the Data portion of the message. This value is used only for UDP jitter operation  which uses codec type
            	**type**\:  int
            
            	**range:** 0..16384
            
            	**units**\: octets
            
            .. attribute:: cipslaudpjittertmplcodectype
            
            	Specifies the codec type to be used with UDP jitter operation.  If codec\-type is configured the following parameters cannot be  configured. cipslaUdpJitterReqDataSize cipslaUdpJitterInterval cipslaUdpJitterNumPkts
            	**type**\:   :py:class:`IpSlaCodecType <ydk.models.cisco_ios_xe.CISCO_IPSLA_TC_MIB.IpSlaCodecType>`
            
            .. attribute:: cipslaudpjittertmplcontrolenable
            
            	If this object is enabled, then the IP SLA application will send control messages to a responder, residing on the target router to respond to the data request packets being sent by the source router
            	**type**\:  bool
            
            .. attribute:: cipslaudpjittertmpldescription
            
            	A string which provides description of UDP Jitter template
            	**type**\:  str
            
            	**length:** 0..128
            
            .. attribute:: cipslaudpjittertmpldistbuckets
            
            	The maximum number of statistical distribution buckets to accumulate.  Since this index does not rollover, only the first cipslaUdpJitterTmplDistBuckets will be kept.  The last bucket will contain all entries from its  distribution interval start point to infinity
            	**type**\:  int
            
            	**range:** 1..20
            
            .. attribute:: cipslaudpjittertmpldistinterval
            
            	The statistical distribution buckets interval.  Distribution Bucket Example\:  cipslaUdpJitterTmplDistBuckets = 5 buckets cipslaUdpJitterTmplDistInterval = 10 milliseconds  \| Bucket 1 \| Bucket 2 \| Bucket 3 \| Bucket 4 \| Bucket 5  \| \|  0\-9 ms  \| 10\-19 ms \| 20\-29 ms \| 30\-39 ms \| 40\-Inf ms \|  Odd Example\:  cipslaUdpJitterTmplDistBuckets = 1 buckets cipslaUdpJitterTmplDistInterval = 10 milliseconds  \| Bucket 1  \| \|  0\-Inf ms \|  Thus, this odd example shows that the value of cipslaUdpJitterTmplDistInterval does not apply when cipslaUdpJitterTmplDistBuckets is one
            	**type**\:  int
            
            	**range:** 1..100
            
            	**units**\: milliseconds
            
            .. attribute:: cipslaudpjittertmplicpiffactor
            
            	The advantage factor is dependant on the type of access and how the service is to be used. Conventional Wire\-line     0 Mobility within Building    5 Mobility within geographic area  10 Access to hard\-to\-reach location   20  It is used when calculating the ICPIF value
            	**type**\:  int
            
            	**range:** 0..20
            
            .. attribute:: cipslaudpjittertmplinterval
            
            	This value represents the inter\-packet delay between packets and is in milliseconds
            	**type**\:  int
            
            	**range:** 4..60000
            
            	**units**\: milliseconds
            
            .. attribute:: cipslaudpjittertmplntptolabs
            
            	This object specifies the total clock synchronization error on source and responder that is considered tolerable for  oneway measurement when NTP is used as clock synchronization  mechanism.  The total clock synchronization error is sum of NTP offsets on source and responder. The value specified is  microseconds. This value can be set only for UDP jitter operation  with precision of microsecond
            	**type**\:  int
            
            	**range:** 0..100000
            
            	**units**\: microseconds
            
            .. attribute:: cipslaudpjittertmplntptolpct
            
            	This object specifies the total clock synchronization error on source and responder that is considered tolerable for  oneway measurement when NTP is used as clock synchronization  mechanism.  The total clock synchronization error is sum of  NTP offsets on source and responder. The value is expressed  as the percentage of actual oneway latency that is measured.  This value can be set only for UDP jitter operation with precision  of microsecond
            	**type**\:  int
            
            	**range:** 0..100
            
            .. attribute:: cipslaudpjittertmplntptoltype
            
            	This object specifies whether the value specified for oneway NTP sync tolerance is absolute value or percent value.  percent(1)  \- The value for oneway NTP sync tolerance is                absolute value. absolute(2) \- The value for oneway NTP sync tolerance is                percent value
            	**type**\:   :py:class:`Cipslaudpjittertmplntptoltype <ydk.models.cisco_ios_xe.CISCO_IPSLA_JITTER_MIB.CISCOIPSLAJITTERMIB.Cipslaudpjittertmpltable.Cipslaudpjittertmplentry.Cipslaudpjittertmplntptoltype>`
            
            .. attribute:: cipslaudpjittertmplnumpkts
            
            	This value represents the number of packets that need to be transmitted
            	**type**\:  int
            
            	**range:** 1..60000
            
            	**units**\: packets
            
            .. attribute:: cipslaudpjittertmplpktpriority
            
            	This object specifies the priority that will be assigned to operation packet.  normal(1) \- The packet is of normal priority. high(2)   \- The packet is of high priority
            	**type**\:   :py:class:`Cipslaudpjittertmplpktpriority <ydk.models.cisco_ios_xe.CISCO_IPSLA_JITTER_MIB.CISCOIPSLAJITTERMIB.Cipslaudpjittertmpltable.Cipslaudpjittertmplentry.Cipslaudpjittertmplpktpriority>`
            
            .. attribute:: cipslaudpjittertmplprecision
            
            	This object specifies the accuracy of jitter statistics in rttMonJitterStatsTable that needs to be calculated. milliseconds(1) \- The accuracy of stats will be of milliseconds. microseconds(2) \- The accuracy of stats will be in microseconds
            	**type**\:   :py:class:`Cipslaudpjittertmplprecision <ydk.models.cisco_ios_xe.CISCO_IPSLA_JITTER_MIB.CISCOIPSLAJITTERMIB.Cipslaudpjittertmpltable.Cipslaudpjittertmplentry.Cipslaudpjittertmplprecision>`
            
            .. attribute:: cipslaudpjittertmplreqdatasize
            
            	This object represents the number of octets to be placed into the ARR Data portion of the request message, when using SNA protocols.  For non\-ARR protocols' IP SLA request/responses, this value represents the native payload size.  REMEMBER\:  The ARR Header overhead is not included            in this value
            	**type**\:  int
            
            	**range:** 16..65024
            
            	**units**\: octets
            
            .. attribute:: cipslaudpjittertmplrowstatus
            
            	The status of the conceptual UDP Jitter template control row. When the status is active, all the read\-create objects in that  row can be modified
            	**type**\:   :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            .. attribute:: cipslaudpjittertmplsrcaddr
            
            	This field specifies the IP address of the source
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cipslaudpjittertmplsrcaddrtype
            
            	An enumerated value which specifies the IP address type of the source. It must be used along with the cipslaUdpJitterTmplSrcAddr object
            	**type**\:   :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            .. attribute:: cipslaudpjittertmplsrcport
            
            	This object represents the source's port number. If this object is not specified, the application will get a port allocated by the system
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: cipslaudpjittertmplstatshours
            
            	The maximum number of hours for which statistics are maintained. Specifically this is the number of hourly groups to keep before rolling over.  The value of one is not advisable because the hourly group will close and immediately be deleted before the network management station will have the opportunity to retrieve the statistics.  The value of zero will shut off data collection
            	**type**\:  int
            
            	**range:** 0..25
            
            	**units**\: hours
            
            .. attribute:: cipslaudpjittertmplstoragetype
            
            	The storage type of this conceptual row
            	**type**\:   :py:class:`StorageType <ydk.models.cisco_ios_xe.SNMPv2_TC.StorageType>`
            
            .. attribute:: cipslaudpjittertmplthreshold
            
            	This object defines an administrative threshold limit. If the IP SLA operation time exceeds this limit, then one threshold crossing occurrence will be counted
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**units**\: milliseconds
            
            .. attribute:: cipslaudpjittertmpltimeout
            
            	Specifies the duration to wait for a IP SLA operation completion.   For connection oriented protocols, this may cause the connection to be closed by the operation.  Once closed, it will be assumed that the connection reestablishment will be performed.  To prevent unwanted closure of connections, be sure to set this value to a realistic connection timeout
            	**type**\:  int
            
            	**range:** 0..604800000
            
            	**units**\: milliseconds
            
            .. attribute:: cipslaudpjittertmpltos
            
            	This object represents the type of service octet in an IP header
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: cipslaudpjittertmplverifydata
            
            	When set to true, the resulting data in each IP SLA operation is compared with the expected data.  This includes checking header information (if possible) and exact packet size
            	**type**\:  bool
            
            .. attribute:: cipslaudpjittertmplvrfname
            
            	This field is used to specify the VRF name in which the IP SLA operation will be used. For regular IP SLA operation this field should not be configured. The agent will use this field to identify the VPN routing table for this operation
            	**type**\:  str
            
            	**length:** 0..32
            
            

            """

            _prefix = 'CISCO-IPSLA-JITTER-MIB'
            _revision = '2007-07-24'

            def __init__(self):
                super(CISCOIPSLAJITTERMIB.Cipslaudpjittertmpltable.Cipslaudpjittertmplentry, self).__init__()

                self.yang_name = "cipslaUdpJitterTmplEntry"
                self.yang_parent_name = "cipslaUdpJitterTmplTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.cipslaudpjittertmplname = YLeaf(YType.str, "cipslaUdpJitterTmplName")

                self.cipslaudpjittertmplcodecinterval = YLeaf(YType.uint32, "cipslaUdpJitterTmplCodecInterval")

                self.cipslaudpjittertmplcodecnumpkts = YLeaf(YType.uint32, "cipslaUdpJitterTmplCodecNumPkts")

                self.cipslaudpjittertmplcodecpayload = YLeaf(YType.uint32, "cipslaUdpJitterTmplCodecPayload")

                self.cipslaudpjittertmplcodectype = YLeaf(YType.enumeration, "cipslaUdpJitterTmplCodecType")

                self.cipslaudpjittertmplcontrolenable = YLeaf(YType.boolean, "cipslaUdpJitterTmplControlEnable")

                self.cipslaudpjittertmpldescription = YLeaf(YType.str, "cipslaUdpJitterTmplDescription")

                self.cipslaudpjittertmpldistbuckets = YLeaf(YType.uint32, "cipslaUdpJitterTmplDistBuckets")

                self.cipslaudpjittertmpldistinterval = YLeaf(YType.uint32, "cipslaUdpJitterTmplDistInterval")

                self.cipslaudpjittertmplicpiffactor = YLeaf(YType.uint32, "cipslaUdpJitterTmplIcpifFactor")

                self.cipslaudpjittertmplinterval = YLeaf(YType.uint32, "cipslaUdpJitterTmplInterval")

                self.cipslaudpjittertmplntptolabs = YLeaf(YType.uint32, "cipslaUdpJitterTmplNTPTolAbs")

                self.cipslaudpjittertmplntptolpct = YLeaf(YType.uint32, "cipslaUdpJitterTmplNTPTolPct")

                self.cipslaudpjittertmplntptoltype = YLeaf(YType.enumeration, "cipslaUdpJitterTmplNTPTolType")

                self.cipslaudpjittertmplnumpkts = YLeaf(YType.uint32, "cipslaUdpJitterTmplNumPkts")

                self.cipslaudpjittertmplpktpriority = YLeaf(YType.enumeration, "cipslaUdpJitterTmplPktPriority")

                self.cipslaudpjittertmplprecision = YLeaf(YType.enumeration, "cipslaUdpJitterTmplPrecision")

                self.cipslaudpjittertmplreqdatasize = YLeaf(YType.uint32, "cipslaUdpJitterTmplReqDataSize")

                self.cipslaudpjittertmplrowstatus = YLeaf(YType.enumeration, "cipslaUdpJitterTmplRowStatus")

                self.cipslaudpjittertmplsrcaddr = YLeaf(YType.str, "cipslaUdpJitterTmplSrcAddr")

                self.cipslaudpjittertmplsrcaddrtype = YLeaf(YType.enumeration, "cipslaUdpJitterTmplSrcAddrType")

                self.cipslaudpjittertmplsrcport = YLeaf(YType.uint16, "cipslaUdpJitterTmplSrcPort")

                self.cipslaudpjittertmplstatshours = YLeaf(YType.uint32, "cipslaUdpJitterTmplStatsHours")

                self.cipslaudpjittertmplstoragetype = YLeaf(YType.enumeration, "cipslaUdpJitterTmplStorageType")

                self.cipslaudpjittertmplthreshold = YLeaf(YType.uint32, "cipslaUdpJitterTmplThreshold")

                self.cipslaudpjittertmpltimeout = YLeaf(YType.uint32, "cipslaUdpJitterTmplTimeOut")

                self.cipslaudpjittertmpltos = YLeaf(YType.uint32, "cipslaUdpJitterTmplTOS")

                self.cipslaudpjittertmplverifydata = YLeaf(YType.boolean, "cipslaUdpJitterTmplVerifyData")

                self.cipslaudpjittertmplvrfname = YLeaf(YType.str, "cipslaUdpJitterTmplVrfName")
                self._segment_path = lambda: "cipslaUdpJitterTmplEntry" + "[cipslaUdpJitterTmplName='" + self.cipslaudpjittertmplname.get() + "']"
                self._absolute_path = lambda: "CISCO-IPSLA-JITTER-MIB:CISCO-IPSLA-JITTER-MIB/cipslaUdpJitterTmplTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIPSLAJITTERMIB.Cipslaudpjittertmpltable.Cipslaudpjittertmplentry, ['cipslaudpjittertmplname', 'cipslaudpjittertmplcodecinterval', 'cipslaudpjittertmplcodecnumpkts', 'cipslaudpjittertmplcodecpayload', 'cipslaudpjittertmplcodectype', 'cipslaudpjittertmplcontrolenable', 'cipslaudpjittertmpldescription', 'cipslaudpjittertmpldistbuckets', 'cipslaudpjittertmpldistinterval', 'cipslaudpjittertmplicpiffactor', 'cipslaudpjittertmplinterval', 'cipslaudpjittertmplntptolabs', 'cipslaudpjittertmplntptolpct', 'cipslaudpjittertmplntptoltype', 'cipslaudpjittertmplnumpkts', 'cipslaudpjittertmplpktpriority', 'cipslaudpjittertmplprecision', 'cipslaudpjittertmplreqdatasize', 'cipslaudpjittertmplrowstatus', 'cipslaudpjittertmplsrcaddr', 'cipslaudpjittertmplsrcaddrtype', 'cipslaudpjittertmplsrcport', 'cipslaudpjittertmplstatshours', 'cipslaudpjittertmplstoragetype', 'cipslaudpjittertmplthreshold', 'cipslaudpjittertmpltimeout', 'cipslaudpjittertmpltos', 'cipslaudpjittertmplverifydata', 'cipslaudpjittertmplvrfname'], name, value)

            class Cipslaudpjittertmplntptoltype(Enum):
                """
                Cipslaudpjittertmplntptoltype

                This object specifies whether the value specified for oneway

                NTP sync tolerance is absolute value or percent value.

                percent(1)  \- The value for oneway NTP sync tolerance is 

                              absolute value.

                absolute(2) \- The value for oneway NTP sync tolerance is 

                              percent value.

                .. data:: percent = 1

                .. data:: absolute = 2

                """

                percent = Enum.YLeaf(1, "percent")

                absolute = Enum.YLeaf(2, "absolute")


            class Cipslaudpjittertmplpktpriority(Enum):
                """
                Cipslaudpjittertmplpktpriority

                This object specifies the priority that will be assigned

                to operation packet.

                normal(1) \- The packet is of normal priority.

                high(2)   \- The packet is of high priority.

                .. data:: normal = 1

                .. data:: high = 2

                """

                normal = Enum.YLeaf(1, "normal")

                high = Enum.YLeaf(2, "high")


            class Cipslaudpjittertmplprecision(Enum):
                """
                Cipslaudpjittertmplprecision

                This object specifies the accuracy of jitter statistics in

                rttMonJitterStatsTable that needs to be calculated.

                milliseconds(1) \- The accuracy of stats will be of milliseconds.

                microseconds(2) \- The accuracy of stats will be in microseconds.

                .. data:: milliseconds = 1

                .. data:: microseconds = 2

                """

                milliseconds = Enum.YLeaf(1, "milliseconds")

                microseconds = Enum.YLeaf(2, "microseconds")


    def clone_ptr(self):
        self._top_entity = CISCOIPSLAJITTERMIB()
        return self._top_entity

