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
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CISCOIPSLAJITTERMIB(Entity):
    """
    
    
    .. attribute:: cipslaudpjittertmpltable
    
    	A table that contains UDP jitter template specific definitions
    	**type**\:  :py:class:`Cipslaudpjittertmpltable <ydk.models.cisco_ios_xe.CISCO_IPSLA_JITTER_MIB.CISCOIPSLAJITTERMIB.Cipslaudpjittertmpltable>`
    
    .. attribute:: cipslaicmpjittertmpltable
    
    	A table that contains ICMP jitter template specific definitions
    	**type**\:  :py:class:`Cipslaicmpjittertmpltable <ydk.models.cisco_ios_xe.CISCO_IPSLA_JITTER_MIB.CISCOIPSLAJITTERMIB.Cipslaicmpjittertmpltable>`
    
    

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
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("cipslaUdpJitterTmplTable", ("cipslaudpjittertmpltable", CISCOIPSLAJITTERMIB.Cipslaudpjittertmpltable)), ("cipslaIcmpJitterTmplTable", ("cipslaicmpjittertmpltable", CISCOIPSLAJITTERMIB.Cipslaicmpjittertmpltable))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.cipslaudpjittertmpltable = CISCOIPSLAJITTERMIB.Cipslaudpjittertmpltable()
        self.cipslaudpjittertmpltable.parent = self
        self._children_name_map["cipslaudpjittertmpltable"] = "cipslaUdpJitterTmplTable"
        self._children_yang_names.add("cipslaUdpJitterTmplTable")

        self.cipslaicmpjittertmpltable = CISCOIPSLAJITTERMIB.Cipslaicmpjittertmpltable()
        self.cipslaicmpjittertmpltable.parent = self
        self._children_name_map["cipslaicmpjittertmpltable"] = "cipslaIcmpJitterTmplTable"
        self._children_yang_names.add("cipslaIcmpJitterTmplTable")
        self._segment_path = lambda: "CISCO-IPSLA-JITTER-MIB:CISCO-IPSLA-JITTER-MIB"


    class Cipslaudpjittertmpltable(Entity):
        """
        A table that contains UDP jitter template specific definitions.
        
        .. attribute:: cipslaudpjittertmplentry
        
        	A row entry representing an IPSLA UDP jitter template
        	**type**\: list of  		 :py:class:`Cipslaudpjittertmplentry <ydk.models.cisco_ios_xe.CISCO_IPSLA_JITTER_MIB.CISCOIPSLAJITTERMIB.Cipslaudpjittertmpltable.Cipslaudpjittertmplentry>`
        
        

        """

        _prefix = 'CISCO-IPSLA-JITTER-MIB'
        _revision = '2007-07-24'

        def __init__(self):
            super(CISCOIPSLAJITTERMIB.Cipslaudpjittertmpltable, self).__init__()

            self.yang_name = "cipslaUdpJitterTmplTable"
            self.yang_parent_name = "CISCO-IPSLA-JITTER-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cipslaUdpJitterTmplEntry", ("cipslaudpjittertmplentry", CISCOIPSLAJITTERMIB.Cipslaudpjittertmpltable.Cipslaudpjittertmplentry))])
            self._leafs = OrderedDict()

            self.cipslaudpjittertmplentry = YList(self)
            self._segment_path = lambda: "cipslaUdpJitterTmplTable"
            self._absolute_path = lambda: "CISCO-IPSLA-JITTER-MIB:CISCO-IPSLA-JITTER-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIPSLAJITTERMIB.Cipslaudpjittertmpltable, [], name, value)


        class Cipslaudpjittertmplentry(Entity):
            """
            A row entry representing an IPSLA UDP jitter template.
            
            .. attribute:: cipslaudpjittertmplname  (key)
            
            	A string which specifies the UDP Jitter template name
            	**type**\: str
            
            	**length:** 1..64
            
            .. attribute:: cipslaudpjittertmpldescription
            
            	A string which provides description of UDP Jitter template
            	**type**\: str
            
            	**length:** 0..128
            
            .. attribute:: cipslaudpjittertmplcontrolenable
            
            	If this object is enabled, then the IP SLA application will send control messages to a responder, residing on the target router to respond to the data request packets being sent by the source router
            	**type**\: bool
            
            .. attribute:: cipslaudpjittertmpltimeout
            
            	Specifies the duration to wait for a IP SLA operation completion.   For connection oriented protocols, this may cause the connection to be closed by the operation.  Once closed, it will be assumed that the connection reestablishment will be performed.  To prevent unwanted closure of connections, be sure to set this value to a realistic connection timeout
            	**type**\: int
            
            	**range:** 0..604800000
            
            	**units**\: milliseconds
            
            .. attribute:: cipslaudpjittertmplverifydata
            
            	When set to true, the resulting data in each IP SLA operation is compared with the expected data.  This includes checking header information (if possible) and exact packet size
            	**type**\: bool
            
            .. attribute:: cipslaudpjittertmplcodectype
            
            	Specifies the codec type to be used with UDP jitter operation.  If codec\-type is configured the following parameters cannot be  configured. cipslaUdpJitterReqDataSize cipslaUdpJitterInterval cipslaUdpJitterNumPkts
            	**type**\:  :py:class:`IpSlaCodecType <ydk.models.cisco_ios_xe.CISCO_IPSLA_TC_MIB.IpSlaCodecType>`
            
            .. attribute:: cipslaudpjittertmplcodecinterval
            
            	This field represents the inter\-packet delay between packets and is in milliseconds. This object is applicable only to UDP jitter operation  which uses codec type
            	**type**\: int
            
            	**range:** 4..60000
            
            	**units**\: milliseconds
            
            .. attribute:: cipslaudpjittertmplcodecpayload
            
            	This object represents the number of octets that needs to be placed into the Data portion of the message. This value is used only for UDP jitter operation  which uses codec type
            	**type**\: int
            
            	**range:** 0..16384
            
            	**units**\: octets
            
            .. attribute:: cipslaudpjittertmplcodecnumpkts
            
            	This value represents the number of packets that need to be transmitted. This value is used only for UDP jitter  operation which uses codec type
            	**type**\: int
            
            	**range:** 1..60000
            
            	**units**\: packets
            
            .. attribute:: cipslaudpjittertmplinterval
            
            	This value represents the inter\-packet delay between packets and is in milliseconds
            	**type**\: int
            
            	**range:** 4..60000
            
            	**units**\: milliseconds
            
            .. attribute:: cipslaudpjittertmplnumpkts
            
            	This value represents the number of packets that need to be transmitted
            	**type**\: int
            
            	**range:** 1..60000
            
            	**units**\: packets
            
            .. attribute:: cipslaudpjittertmplsrcaddrtype
            
            	An enumerated value which specifies the IP address type of the source. It must be used along with the cipslaUdpJitterTmplSrcAddr object
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            .. attribute:: cipslaudpjittertmplsrcaddr
            
            	This field specifies the IP address of the source
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: cipslaudpjittertmplsrcport
            
            	This object represents the source's port number. If this object is not specified, the application will get a port allocated by the system
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: cipslaudpjittertmplprecision
            
            	This object specifies the accuracy of jitter statistics in rttMonJitterStatsTable that needs to be calculated. milliseconds(1) \- The accuracy of stats will be of milliseconds. microseconds(2) \- The accuracy of stats will be in microseconds
            	**type**\:  :py:class:`Cipslaudpjittertmplprecision <ydk.models.cisco_ios_xe.CISCO_IPSLA_JITTER_MIB.CISCOIPSLAJITTERMIB.Cipslaudpjittertmpltable.Cipslaudpjittertmplentry.Cipslaudpjittertmplprecision>`
            
            .. attribute:: cipslaudpjittertmplreqdatasize
            
            	This object represents the number of octets to be placed into the ARR Data portion of the request message, when using SNA protocols.  For non\-ARR protocols' IP SLA request/responses, this value represents the native payload size.  REMEMBER\:  The ARR Header overhead is not included            in this value
            	**type**\: int
            
            	**range:** 16..65024
            
            	**units**\: octets
            
            .. attribute:: cipslaudpjittertmplpktpriority
            
            	This object specifies the priority that will be assigned to operation packet.  normal(1) \- The packet is of normal priority. high(2)   \- The packet is of high priority
            	**type**\:  :py:class:`Cipslaudpjittertmplpktpriority <ydk.models.cisco_ios_xe.CISCO_IPSLA_JITTER_MIB.CISCOIPSLAJITTERMIB.Cipslaudpjittertmpltable.Cipslaudpjittertmplentry.Cipslaudpjittertmplpktpriority>`
            
            .. attribute:: cipslaudpjittertmpltos
            
            	This object represents the type of service octet in an IP header
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: cipslaudpjittertmplvrfname
            
            	This field is used to specify the VRF name in which the IP SLA operation will be used. For regular IP SLA operation this field should not be configured. The agent will use this field to identify the VPN routing table for this operation
            	**type**\: str
            
            	**length:** 0..32
            
            .. attribute:: cipslaudpjittertmplthreshold
            
            	This object defines an administrative threshold limit. If the IP SLA operation time exceeds this limit, then one threshold crossing occurrence will be counted
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**units**\: milliseconds
            
            .. attribute:: cipslaudpjittertmplntptolabs
            
            	This object specifies the total clock synchronization error on source and responder that is considered tolerable for  oneway measurement when NTP is used as clock synchronization  mechanism.  The total clock synchronization error is sum of NTP offsets on source and responder. The value specified is  microseconds. This value can be set only for UDP jitter operation  with precision of microsecond
            	**type**\: int
            
            	**range:** 0..100000
            
            	**units**\: microseconds
            
            .. attribute:: cipslaudpjittertmplntptolpct
            
            	This object specifies the total clock synchronization error on source and responder that is considered tolerable for  oneway measurement when NTP is used as clock synchronization  mechanism.  The total clock synchronization error is sum of  NTP offsets on source and responder. The value is expressed  as the percentage of actual oneway latency that is measured.  This value can be set only for UDP jitter operation with precision  of microsecond
            	**type**\: int
            
            	**range:** 0..100
            
            .. attribute:: cipslaudpjittertmplntptoltype
            
            	This object specifies whether the value specified for oneway NTP sync tolerance is absolute value or percent value.  percent(1)  \- The value for oneway NTP sync tolerance is                absolute value. absolute(2) \- The value for oneway NTP sync tolerance is                percent value
            	**type**\:  :py:class:`Cipslaudpjittertmplntptoltype <ydk.models.cisco_ios_xe.CISCO_IPSLA_JITTER_MIB.CISCOIPSLAJITTERMIB.Cipslaudpjittertmpltable.Cipslaudpjittertmplentry.Cipslaudpjittertmplntptoltype>`
            
            .. attribute:: cipslaudpjittertmplicpiffactor
            
            	The advantage factor is dependant on the type of access and how the service is to be used. Conventional Wire\-line     0 Mobility within Building    5 Mobility within geographic area  10 Access to hard\-to\-reach location   20  It is used when calculating the ICPIF value
            	**type**\: int
            
            	**range:** 0..20
            
            .. attribute:: cipslaudpjittertmplstatshours
            
            	The maximum number of hours for which statistics are maintained. Specifically this is the number of hourly groups to keep before rolling over.  The value of one is not advisable because the hourly group will close and immediately be deleted before the network management station will have the opportunity to retrieve the statistics.  The value of zero will shut off data collection
            	**type**\: int
            
            	**range:** 0..25
            
            	**units**\: hours
            
            .. attribute:: cipslaudpjittertmpldistbuckets
            
            	The maximum number of statistical distribution buckets to accumulate.  Since this index does not rollover, only the first cipslaUdpJitterTmplDistBuckets will be kept.  The last bucket will contain all entries from its  distribution interval start point to infinity
            	**type**\: int
            
            	**range:** 1..20
            
            .. attribute:: cipslaudpjittertmpldistinterval
            
            	The statistical distribution buckets interval.  Distribution Bucket Example\:  cipslaUdpJitterTmplDistBuckets = 5 buckets cipslaUdpJitterTmplDistInterval = 10 milliseconds  \| Bucket 1 \| Bucket 2 \| Bucket 3 \| Bucket 4 \| Bucket 5  \| \|  0\-9 ms  \| 10\-19 ms \| 20\-29 ms \| 30\-39 ms \| 40\-Inf ms \|  Odd Example\:  cipslaUdpJitterTmplDistBuckets = 1 buckets cipslaUdpJitterTmplDistInterval = 10 milliseconds  \| Bucket 1  \| \|  0\-Inf ms \|  Thus, this odd example shows that the value of cipslaUdpJitterTmplDistInterval does not apply when cipslaUdpJitterTmplDistBuckets is one
            	**type**\: int
            
            	**range:** 1..100
            
            	**units**\: milliseconds
            
            .. attribute:: cipslaudpjittertmplstoragetype
            
            	The storage type of this conceptual row
            	**type**\:  :py:class:`StorageType <ydk.models.cisco_ios_xe.SNMPv2_TC.StorageType>`
            
            .. attribute:: cipslaudpjittertmplrowstatus
            
            	The status of the conceptual UDP Jitter template control row. When the status is active, all the read\-create objects in that  row can be modified
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            

            """

            _prefix = 'CISCO-IPSLA-JITTER-MIB'
            _revision = '2007-07-24'

            def __init__(self):
                super(CISCOIPSLAJITTERMIB.Cipslaudpjittertmpltable.Cipslaudpjittertmplentry, self).__init__()

                self.yang_name = "cipslaUdpJitterTmplEntry"
                self.yang_parent_name = "cipslaUdpJitterTmplTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cipslaudpjittertmplname']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cipslaudpjittertmplname', YLeaf(YType.str, 'cipslaUdpJitterTmplName')),
                    ('cipslaudpjittertmpldescription', YLeaf(YType.str, 'cipslaUdpJitterTmplDescription')),
                    ('cipslaudpjittertmplcontrolenable', YLeaf(YType.boolean, 'cipslaUdpJitterTmplControlEnable')),
                    ('cipslaudpjittertmpltimeout', YLeaf(YType.uint32, 'cipslaUdpJitterTmplTimeOut')),
                    ('cipslaudpjittertmplverifydata', YLeaf(YType.boolean, 'cipslaUdpJitterTmplVerifyData')),
                    ('cipslaudpjittertmplcodectype', YLeaf(YType.enumeration, 'cipslaUdpJitterTmplCodecType')),
                    ('cipslaudpjittertmplcodecinterval', YLeaf(YType.uint32, 'cipslaUdpJitterTmplCodecInterval')),
                    ('cipslaudpjittertmplcodecpayload', YLeaf(YType.uint32, 'cipslaUdpJitterTmplCodecPayload')),
                    ('cipslaudpjittertmplcodecnumpkts', YLeaf(YType.uint32, 'cipslaUdpJitterTmplCodecNumPkts')),
                    ('cipslaudpjittertmplinterval', YLeaf(YType.uint32, 'cipslaUdpJitterTmplInterval')),
                    ('cipslaudpjittertmplnumpkts', YLeaf(YType.uint32, 'cipslaUdpJitterTmplNumPkts')),
                    ('cipslaudpjittertmplsrcaddrtype', YLeaf(YType.enumeration, 'cipslaUdpJitterTmplSrcAddrType')),
                    ('cipslaudpjittertmplsrcaddr', YLeaf(YType.str, 'cipslaUdpJitterTmplSrcAddr')),
                    ('cipslaudpjittertmplsrcport', YLeaf(YType.uint16, 'cipslaUdpJitterTmplSrcPort')),
                    ('cipslaudpjittertmplprecision', YLeaf(YType.enumeration, 'cipslaUdpJitterTmplPrecision')),
                    ('cipslaudpjittertmplreqdatasize', YLeaf(YType.uint32, 'cipslaUdpJitterTmplReqDataSize')),
                    ('cipslaudpjittertmplpktpriority', YLeaf(YType.enumeration, 'cipslaUdpJitterTmplPktPriority')),
                    ('cipslaudpjittertmpltos', YLeaf(YType.uint32, 'cipslaUdpJitterTmplTOS')),
                    ('cipslaudpjittertmplvrfname', YLeaf(YType.str, 'cipslaUdpJitterTmplVrfName')),
                    ('cipslaudpjittertmplthreshold', YLeaf(YType.uint32, 'cipslaUdpJitterTmplThreshold')),
                    ('cipslaudpjittertmplntptolabs', YLeaf(YType.uint32, 'cipslaUdpJitterTmplNTPTolAbs')),
                    ('cipslaudpjittertmplntptolpct', YLeaf(YType.uint32, 'cipslaUdpJitterTmplNTPTolPct')),
                    ('cipslaudpjittertmplntptoltype', YLeaf(YType.enumeration, 'cipslaUdpJitterTmplNTPTolType')),
                    ('cipslaudpjittertmplicpiffactor', YLeaf(YType.uint32, 'cipslaUdpJitterTmplIcpifFactor')),
                    ('cipslaudpjittertmplstatshours', YLeaf(YType.uint32, 'cipslaUdpJitterTmplStatsHours')),
                    ('cipslaudpjittertmpldistbuckets', YLeaf(YType.uint32, 'cipslaUdpJitterTmplDistBuckets')),
                    ('cipslaudpjittertmpldistinterval', YLeaf(YType.uint32, 'cipslaUdpJitterTmplDistInterval')),
                    ('cipslaudpjittertmplstoragetype', YLeaf(YType.enumeration, 'cipslaUdpJitterTmplStorageType')),
                    ('cipslaudpjittertmplrowstatus', YLeaf(YType.enumeration, 'cipslaUdpJitterTmplRowStatus')),
                ])
                self.cipslaudpjittertmplname = None
                self.cipslaudpjittertmpldescription = None
                self.cipslaudpjittertmplcontrolenable = None
                self.cipslaudpjittertmpltimeout = None
                self.cipslaudpjittertmplverifydata = None
                self.cipslaudpjittertmplcodectype = None
                self.cipslaudpjittertmplcodecinterval = None
                self.cipslaudpjittertmplcodecpayload = None
                self.cipslaudpjittertmplcodecnumpkts = None
                self.cipslaudpjittertmplinterval = None
                self.cipslaudpjittertmplnumpkts = None
                self.cipslaudpjittertmplsrcaddrtype = None
                self.cipslaudpjittertmplsrcaddr = None
                self.cipslaudpjittertmplsrcport = None
                self.cipslaudpjittertmplprecision = None
                self.cipslaudpjittertmplreqdatasize = None
                self.cipslaudpjittertmplpktpriority = None
                self.cipslaudpjittertmpltos = None
                self.cipslaudpjittertmplvrfname = None
                self.cipslaudpjittertmplthreshold = None
                self.cipslaudpjittertmplntptolabs = None
                self.cipslaudpjittertmplntptolpct = None
                self.cipslaudpjittertmplntptoltype = None
                self.cipslaudpjittertmplicpiffactor = None
                self.cipslaudpjittertmplstatshours = None
                self.cipslaudpjittertmpldistbuckets = None
                self.cipslaudpjittertmpldistinterval = None
                self.cipslaudpjittertmplstoragetype = None
                self.cipslaudpjittertmplrowstatus = None
                self._segment_path = lambda: "cipslaUdpJitterTmplEntry" + "[cipslaUdpJitterTmplName='" + str(self.cipslaudpjittertmplname) + "']"
                self._absolute_path = lambda: "CISCO-IPSLA-JITTER-MIB:CISCO-IPSLA-JITTER-MIB/cipslaUdpJitterTmplTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIPSLAJITTERMIB.Cipslaudpjittertmpltable.Cipslaudpjittertmplentry, ['cipslaudpjittertmplname', 'cipslaudpjittertmpldescription', 'cipslaudpjittertmplcontrolenable', 'cipslaudpjittertmpltimeout', 'cipslaudpjittertmplverifydata', 'cipslaudpjittertmplcodectype', 'cipslaudpjittertmplcodecinterval', 'cipslaudpjittertmplcodecpayload', 'cipslaudpjittertmplcodecnumpkts', 'cipslaudpjittertmplinterval', 'cipslaudpjittertmplnumpkts', 'cipslaudpjittertmplsrcaddrtype', 'cipslaudpjittertmplsrcaddr', 'cipslaudpjittertmplsrcport', 'cipslaudpjittertmplprecision', 'cipslaudpjittertmplreqdatasize', 'cipslaudpjittertmplpktpriority', 'cipslaudpjittertmpltos', 'cipslaudpjittertmplvrfname', 'cipslaudpjittertmplthreshold', 'cipslaudpjittertmplntptolabs', 'cipslaudpjittertmplntptolpct', 'cipslaudpjittertmplntptoltype', 'cipslaudpjittertmplicpiffactor', 'cipslaudpjittertmplstatshours', 'cipslaudpjittertmpldistbuckets', 'cipslaudpjittertmpldistinterval', 'cipslaudpjittertmplstoragetype', 'cipslaudpjittertmplrowstatus'], name, value)

            class Cipslaudpjittertmplntptoltype(Enum):
                """
                Cipslaudpjittertmplntptoltype (Enum Class)

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
                Cipslaudpjittertmplpktpriority (Enum Class)

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
                Cipslaudpjittertmplprecision (Enum Class)

                This object specifies the accuracy of jitter statistics in

                rttMonJitterStatsTable that needs to be calculated.

                milliseconds(1) \- The accuracy of stats will be of milliseconds.

                microseconds(2) \- The accuracy of stats will be in microseconds.

                .. data:: milliseconds = 1

                .. data:: microseconds = 2

                """

                milliseconds = Enum.YLeaf(1, "milliseconds")

                microseconds = Enum.YLeaf(2, "microseconds")



    class Cipslaicmpjittertmpltable(Entity):
        """
        A table that contains ICMP jitter template specific definitions.
        
        .. attribute:: cipslaicmpjittertmplentry
        
        	A row entry representing an IP SLA ICMP Jitter template
        	**type**\: list of  		 :py:class:`Cipslaicmpjittertmplentry <ydk.models.cisco_ios_xe.CISCO_IPSLA_JITTER_MIB.CISCOIPSLAJITTERMIB.Cipslaicmpjittertmpltable.Cipslaicmpjittertmplentry>`
        
        

        """

        _prefix = 'CISCO-IPSLA-JITTER-MIB'
        _revision = '2007-07-24'

        def __init__(self):
            super(CISCOIPSLAJITTERMIB.Cipslaicmpjittertmpltable, self).__init__()

            self.yang_name = "cipslaIcmpJitterTmplTable"
            self.yang_parent_name = "CISCO-IPSLA-JITTER-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cipslaIcmpJitterTmplEntry", ("cipslaicmpjittertmplentry", CISCOIPSLAJITTERMIB.Cipslaicmpjittertmpltable.Cipslaicmpjittertmplentry))])
            self._leafs = OrderedDict()

            self.cipslaicmpjittertmplentry = YList(self)
            self._segment_path = lambda: "cipslaIcmpJitterTmplTable"
            self._absolute_path = lambda: "CISCO-IPSLA-JITTER-MIB:CISCO-IPSLA-JITTER-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIPSLAJITTERMIB.Cipslaicmpjittertmpltable, [], name, value)


        class Cipslaicmpjittertmplentry(Entity):
            """
            A row entry representing an IP SLA ICMP Jitter template.
            
            .. attribute:: cipslaicmpjittertmplname  (key)
            
            	A string which specifies the ICMP jitter template name
            	**type**\: str
            
            	**length:** 1..64
            
            .. attribute:: cipslaicmpjittertmpldescription
            
            	A string which provides description of ICMP Jitter template
            	**type**\: str
            
            	**length:** 0..128
            
            .. attribute:: cipslaicmpjittertmpltimeout
            
            	Specifies the duration to wait for a IP SLA operation completion.  For connection oriented protocols, this may cause the connection to be closed by the operation.  Once closed, it will be assumed that the connection reestablishment will be performed.  To prevent unwanted closure of connections, be sure to set this value to a realistic connection timeout
            	**type**\: int
            
            	**range:** 0..604800000
            
            	**units**\: milliseconds
            
            .. attribute:: cipslaicmpjittertmplverifydata
            
            	When set to true, the resulting data in each IP SLA operation is compared with the expected data.  This includes checking header information (if possible) and exact packet size
            	**type**\: bool
            
            .. attribute:: cipslaicmpjittertmplnumpkts
            
            	This value represents the number of packets that need to be transmitted
            	**type**\: int
            
            	**range:** 1..60000
            
            	**units**\: packets
            
            .. attribute:: cipslaicmpjittertmplinterval
            
            	This value represents the inter\-packet delay between packets and is in milliseconds
            	**type**\: int
            
            	**range:** 4..60000
            
            	**units**\: milliseconds
            
            .. attribute:: cipslaicmpjittertmplsrcaddrtype
            
            	An enumerated value which specifies the IP address type of the source. It must be used along with the cipslaIcmpJitterTmplSrcAddr object
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            .. attribute:: cipslaicmpjittertmplsrcaddr
            
            	A string which specifies the IP address of the source
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: cipslaicmpjittertmpltos
            
            	This object represents the type of service octet in an IP header
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: cipslaicmpjittertmplvrfname
            
            	This field is used to specify the VRF name in which the IP SLA operation will be used. For regular IP SLA operation this field should not be configured. The agent will use this field to identify the VPN routing Table for this operation
            	**type**\: str
            
            	**length:** 0..32
            
            .. attribute:: cipslaicmpjittertmplthreshold
            
            	This object defines an administrative threshold limit. If the IP SLA operation time exceeds this limit, then  one threshold crossing occurrence will be counted
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**units**\: milliseconds
            
            .. attribute:: cipslaicmpjittertmplstatshours
            
            	The maximum number of hourss for which statistics are maintained. Specifically this is the number of hourly groups to keep before rolling over.  The value of one is not advisable because the hourly group will close and immediately be deleted before the network management station will have the opportunity to retrieve the statistics.  The value of zero will shut off data collection
            	**type**\: int
            
            	**range:** 0..25
            
            	**units**\: hours
            
            .. attribute:: cipslaicmpjittertmpldistbuckets
            
            	The maximum number of statistical distribution buckets to accumulate.  Since this index does not rollover, only the first cipslaIcmpJitterTmplDistBuckets will be kept.  The last bucket will contain all entries from its  distribution interval start point to infinity
            	**type**\: int
            
            	**range:** 1..20
            
            .. attribute:: cipslaicmpjittertmpldistinterval
            
            	The statistical distribution buckets interval.  Distribution Bucket Example\:  cipslaIcmpJitterTmplDistBuckets = 5 buckets cipslaIcmpJitterTmplDistInterval = 10 milliseconds  \| Bucket 1 \| Bucket 2 \| Bucket 3 \| Bucket 4 \| Bucket 5  \| \|  0\-9 ms  \| 10\-19 ms \| 20\-29 ms \| 30\-39 ms \| 40\-Inf ms \|  Odd Example\:  cipslaIcmpJitterTmplDistBuckets = 1 buckets cipslaIcmpJitterTmplDistInterval = 10 milliseconds  \| Bucket 1  \| \|  0\-Inf ms \|  Thus, this odd example shows that the value of cipslaIcmpJitterTmplDistInterval does not apply when cipslaIcmpJitterTmplDistBuckets is one
            	**type**\: int
            
            	**range:** 1..100
            
            	**units**\: milliseconds
            
            .. attribute:: cipslaicmpjittertmplstoragetype
            
            	The storage type of this conceptual row
            	**type**\:  :py:class:`StorageType <ydk.models.cisco_ios_xe.SNMPv2_TC.StorageType>`
            
            .. attribute:: cipslaicmpjittertmplrowstatus
            
            	The status of the conceptual ICMP jitter template control row. When the status is active, all the read\-create objects in  that row can be modified
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            

            """

            _prefix = 'CISCO-IPSLA-JITTER-MIB'
            _revision = '2007-07-24'

            def __init__(self):
                super(CISCOIPSLAJITTERMIB.Cipslaicmpjittertmpltable.Cipslaicmpjittertmplentry, self).__init__()

                self.yang_name = "cipslaIcmpJitterTmplEntry"
                self.yang_parent_name = "cipslaIcmpJitterTmplTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cipslaicmpjittertmplname']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cipslaicmpjittertmplname', YLeaf(YType.str, 'cipslaIcmpJitterTmplName')),
                    ('cipslaicmpjittertmpldescription', YLeaf(YType.str, 'cipslaIcmpJitterTmplDescription')),
                    ('cipslaicmpjittertmpltimeout', YLeaf(YType.uint32, 'cipslaIcmpJitterTmplTimeOut')),
                    ('cipslaicmpjittertmplverifydata', YLeaf(YType.boolean, 'cipslaIcmpJitterTmplVerifyData')),
                    ('cipslaicmpjittertmplnumpkts', YLeaf(YType.uint32, 'cipslaIcmpJitterTmplNumPkts')),
                    ('cipslaicmpjittertmplinterval', YLeaf(YType.uint32, 'cipslaIcmpJitterTmplInterval')),
                    ('cipslaicmpjittertmplsrcaddrtype', YLeaf(YType.enumeration, 'cipslaIcmpJitterTmplSrcAddrType')),
                    ('cipslaicmpjittertmplsrcaddr', YLeaf(YType.str, 'cipslaIcmpJitterTmplSrcAddr')),
                    ('cipslaicmpjittertmpltos', YLeaf(YType.uint32, 'cipslaIcmpJitterTmplTOS')),
                    ('cipslaicmpjittertmplvrfname', YLeaf(YType.str, 'cipslaIcmpJitterTmplVrfName')),
                    ('cipslaicmpjittertmplthreshold', YLeaf(YType.uint32, 'cipslaIcmpJitterTmplThreshold')),
                    ('cipslaicmpjittertmplstatshours', YLeaf(YType.uint32, 'cipslaIcmpJitterTmplStatsHours')),
                    ('cipslaicmpjittertmpldistbuckets', YLeaf(YType.uint32, 'cipslaIcmpJitterTmplDistBuckets')),
                    ('cipslaicmpjittertmpldistinterval', YLeaf(YType.uint32, 'cipslaIcmpJitterTmplDistInterval')),
                    ('cipslaicmpjittertmplstoragetype', YLeaf(YType.enumeration, 'cipslaIcmpJitterTmplStorageType')),
                    ('cipslaicmpjittertmplrowstatus', YLeaf(YType.enumeration, 'cipslaIcmpJitterTmplRowStatus')),
                ])
                self.cipslaicmpjittertmplname = None
                self.cipslaicmpjittertmpldescription = None
                self.cipslaicmpjittertmpltimeout = None
                self.cipslaicmpjittertmplverifydata = None
                self.cipslaicmpjittertmplnumpkts = None
                self.cipslaicmpjittertmplinterval = None
                self.cipslaicmpjittertmplsrcaddrtype = None
                self.cipslaicmpjittertmplsrcaddr = None
                self.cipslaicmpjittertmpltos = None
                self.cipslaicmpjittertmplvrfname = None
                self.cipslaicmpjittertmplthreshold = None
                self.cipslaicmpjittertmplstatshours = None
                self.cipslaicmpjittertmpldistbuckets = None
                self.cipslaicmpjittertmpldistinterval = None
                self.cipslaicmpjittertmplstoragetype = None
                self.cipslaicmpjittertmplrowstatus = None
                self._segment_path = lambda: "cipslaIcmpJitterTmplEntry" + "[cipslaIcmpJitterTmplName='" + str(self.cipslaicmpjittertmplname) + "']"
                self._absolute_path = lambda: "CISCO-IPSLA-JITTER-MIB:CISCO-IPSLA-JITTER-MIB/cipslaIcmpJitterTmplTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIPSLAJITTERMIB.Cipslaicmpjittertmpltable.Cipslaicmpjittertmplentry, ['cipslaicmpjittertmplname', 'cipslaicmpjittertmpldescription', 'cipslaicmpjittertmpltimeout', 'cipslaicmpjittertmplverifydata', 'cipslaicmpjittertmplnumpkts', 'cipslaicmpjittertmplinterval', 'cipslaicmpjittertmplsrcaddrtype', 'cipslaicmpjittertmplsrcaddr', 'cipslaicmpjittertmpltos', 'cipslaicmpjittertmplvrfname', 'cipslaicmpjittertmplthreshold', 'cipslaicmpjittertmplstatshours', 'cipslaicmpjittertmpldistbuckets', 'cipslaicmpjittertmpldistinterval', 'cipslaicmpjittertmplstoragetype', 'cipslaicmpjittertmplrowstatus'], name, value)

    def clone_ptr(self):
        self._top_entity = CISCOIPSLAJITTERMIB()
        return self._top_entity

