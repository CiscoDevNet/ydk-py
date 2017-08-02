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
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CiscoIpslaJitterMib(Entity):
    """
    
    
    .. attribute:: cipslaicmpjittertmpltable
    
    	A table that contains ICMP jitter template specific definitions
    	**type**\:   :py:class:`Cipslaicmpjittertmpltable <ydk.models.cisco_ios_xe.CISCO_IPSLA_JITTER_MIB.CiscoIpslaJitterMib.Cipslaicmpjittertmpltable>`
    
    .. attribute:: cipslaudpjittertmpltable
    
    	A table that contains UDP jitter template specific definitions
    	**type**\:   :py:class:`Cipslaudpjittertmpltable <ydk.models.cisco_ios_xe.CISCO_IPSLA_JITTER_MIB.CiscoIpslaJitterMib.Cipslaudpjittertmpltable>`
    
    

    """

    _prefix = 'CISCO-IPSLA-JITTER-MIB'
    _revision = '2007-07-24'

    def __init__(self):
        super(CiscoIpslaJitterMib, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-IPSLA-JITTER-MIB"
        self.yang_parent_name = "CISCO-IPSLA-JITTER-MIB"

        self.cipslaicmpjittertmpltable = CiscoIpslaJitterMib.Cipslaicmpjittertmpltable()
        self.cipslaicmpjittertmpltable.parent = self
        self._children_name_map["cipslaicmpjittertmpltable"] = "cipslaIcmpJitterTmplTable"
        self._children_yang_names.add("cipslaIcmpJitterTmplTable")

        self.cipslaudpjittertmpltable = CiscoIpslaJitterMib.Cipslaudpjittertmpltable()
        self.cipslaudpjittertmpltable.parent = self
        self._children_name_map["cipslaudpjittertmpltable"] = "cipslaUdpJitterTmplTable"
        self._children_yang_names.add("cipslaUdpJitterTmplTable")


    class Cipslaudpjittertmpltable(Entity):
        """
        A table that contains UDP jitter template specific definitions.
        
        .. attribute:: cipslaudpjittertmplentry
        
        	A row entry representing an IPSLA UDP jitter template
        	**type**\: list of    :py:class:`Cipslaudpjittertmplentry <ydk.models.cisco_ios_xe.CISCO_IPSLA_JITTER_MIB.CiscoIpslaJitterMib.Cipslaudpjittertmpltable.Cipslaudpjittertmplentry>`
        
        

        """

        _prefix = 'CISCO-IPSLA-JITTER-MIB'
        _revision = '2007-07-24'

        def __init__(self):
            super(CiscoIpslaJitterMib.Cipslaudpjittertmpltable, self).__init__()

            self.yang_name = "cipslaUdpJitterTmplTable"
            self.yang_parent_name = "CISCO-IPSLA-JITTER-MIB"

            self.cipslaudpjittertmplentry = YList(self)

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
                        super(CiscoIpslaJitterMib.Cipslaudpjittertmpltable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIpslaJitterMib.Cipslaudpjittertmpltable, self).__setattr__(name, value)


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
            	**type**\:   :py:class:`Ipslacodectype <ydk.models.cisco_ios_xe.CISCO_IPSLA_TC_MIB.Ipslacodectype>`
            
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
            	**type**\:   :py:class:`Cipslaudpjittertmplntptoltype <ydk.models.cisco_ios_xe.CISCO_IPSLA_JITTER_MIB.CiscoIpslaJitterMib.Cipslaudpjittertmpltable.Cipslaudpjittertmplentry.Cipslaudpjittertmplntptoltype>`
            
            .. attribute:: cipslaudpjittertmplnumpkts
            
            	This value represents the number of packets that need to be transmitted
            	**type**\:  int
            
            	**range:** 1..60000
            
            	**units**\: packets
            
            .. attribute:: cipslaudpjittertmplpktpriority
            
            	This object specifies the priority that will be assigned to operation packet.  normal(1) \- The packet is of normal priority. high(2)   \- The packet is of high priority
            	**type**\:   :py:class:`Cipslaudpjittertmplpktpriority <ydk.models.cisco_ios_xe.CISCO_IPSLA_JITTER_MIB.CiscoIpslaJitterMib.Cipslaudpjittertmpltable.Cipslaudpjittertmplentry.Cipslaudpjittertmplpktpriority>`
            
            .. attribute:: cipslaudpjittertmplprecision
            
            	This object specifies the accuracy of jitter statistics in rttMonJitterStatsTable that needs to be calculated. milliseconds(1) \- The accuracy of stats will be of milliseconds. microseconds(2) \- The accuracy of stats will be in microseconds
            	**type**\:   :py:class:`Cipslaudpjittertmplprecision <ydk.models.cisco_ios_xe.CISCO_IPSLA_JITTER_MIB.CiscoIpslaJitterMib.Cipslaudpjittertmpltable.Cipslaudpjittertmplentry.Cipslaudpjittertmplprecision>`
            
            .. attribute:: cipslaudpjittertmplreqdatasize
            
            	This object represents the number of octets to be placed into the ARR Data portion of the request message, when using SNA protocols.  For non\-ARR protocols' IP SLA request/responses, this value represents the native payload size.  REMEMBER\:  The ARR Header overhead is not included            in this value
            	**type**\:  int
            
            	**range:** 16..65024
            
            	**units**\: octets
            
            .. attribute:: cipslaudpjittertmplrowstatus
            
            	The status of the conceptual UDP Jitter template control row. When the status is active, all the read\-create objects in that  row can be modified
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: cipslaudpjittertmplsrcaddr
            
            	This field specifies the IP address of the source
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cipslaudpjittertmplsrcaddrtype
            
            	An enumerated value which specifies the IP address type of the source. It must be used along with the cipslaUdpJitterTmplSrcAddr object
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
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
            	**type**\:   :py:class:`Storagetype <ydk.models.cisco_ios_xe.SNMPv2_TC.Storagetype>`
            
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
                super(CiscoIpslaJitterMib.Cipslaudpjittertmpltable.Cipslaudpjittertmplentry, self).__init__()

                self.yang_name = "cipslaUdpJitterTmplEntry"
                self.yang_parent_name = "cipslaUdpJitterTmplTable"

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

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cipslaudpjittertmplname",
                                "cipslaudpjittertmplcodecinterval",
                                "cipslaudpjittertmplcodecnumpkts",
                                "cipslaudpjittertmplcodecpayload",
                                "cipslaudpjittertmplcodectype",
                                "cipslaudpjittertmplcontrolenable",
                                "cipslaudpjittertmpldescription",
                                "cipslaudpjittertmpldistbuckets",
                                "cipslaudpjittertmpldistinterval",
                                "cipslaudpjittertmplicpiffactor",
                                "cipslaudpjittertmplinterval",
                                "cipslaudpjittertmplntptolabs",
                                "cipslaudpjittertmplntptolpct",
                                "cipslaudpjittertmplntptoltype",
                                "cipslaudpjittertmplnumpkts",
                                "cipslaudpjittertmplpktpriority",
                                "cipslaudpjittertmplprecision",
                                "cipslaudpjittertmplreqdatasize",
                                "cipslaudpjittertmplrowstatus",
                                "cipslaudpjittertmplsrcaddr",
                                "cipslaudpjittertmplsrcaddrtype",
                                "cipslaudpjittertmplsrcport",
                                "cipslaudpjittertmplstatshours",
                                "cipslaudpjittertmplstoragetype",
                                "cipslaudpjittertmplthreshold",
                                "cipslaudpjittertmpltimeout",
                                "cipslaudpjittertmpltos",
                                "cipslaudpjittertmplverifydata",
                                "cipslaudpjittertmplvrfname") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoIpslaJitterMib.Cipslaudpjittertmpltable.Cipslaudpjittertmplentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoIpslaJitterMib.Cipslaudpjittertmpltable.Cipslaudpjittertmplentry, self).__setattr__(name, value)

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


            def has_data(self):
                return (
                    self.cipslaudpjittertmplname.is_set or
                    self.cipslaudpjittertmplcodecinterval.is_set or
                    self.cipslaudpjittertmplcodecnumpkts.is_set or
                    self.cipslaudpjittertmplcodecpayload.is_set or
                    self.cipslaudpjittertmplcodectype.is_set or
                    self.cipslaudpjittertmplcontrolenable.is_set or
                    self.cipslaudpjittertmpldescription.is_set or
                    self.cipslaudpjittertmpldistbuckets.is_set or
                    self.cipslaudpjittertmpldistinterval.is_set or
                    self.cipslaudpjittertmplicpiffactor.is_set or
                    self.cipslaudpjittertmplinterval.is_set or
                    self.cipslaudpjittertmplntptolabs.is_set or
                    self.cipslaudpjittertmplntptolpct.is_set or
                    self.cipslaudpjittertmplntptoltype.is_set or
                    self.cipslaudpjittertmplnumpkts.is_set or
                    self.cipslaudpjittertmplpktpriority.is_set or
                    self.cipslaudpjittertmplprecision.is_set or
                    self.cipslaudpjittertmplreqdatasize.is_set or
                    self.cipslaudpjittertmplrowstatus.is_set or
                    self.cipslaudpjittertmplsrcaddr.is_set or
                    self.cipslaudpjittertmplsrcaddrtype.is_set or
                    self.cipslaudpjittertmplsrcport.is_set or
                    self.cipslaudpjittertmplstatshours.is_set or
                    self.cipslaudpjittertmplstoragetype.is_set or
                    self.cipslaudpjittertmplthreshold.is_set or
                    self.cipslaudpjittertmpltimeout.is_set or
                    self.cipslaudpjittertmpltos.is_set or
                    self.cipslaudpjittertmplverifydata.is_set or
                    self.cipslaudpjittertmplvrfname.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cipslaudpjittertmplname.yfilter != YFilter.not_set or
                    self.cipslaudpjittertmplcodecinterval.yfilter != YFilter.not_set or
                    self.cipslaudpjittertmplcodecnumpkts.yfilter != YFilter.not_set or
                    self.cipslaudpjittertmplcodecpayload.yfilter != YFilter.not_set or
                    self.cipslaudpjittertmplcodectype.yfilter != YFilter.not_set or
                    self.cipslaudpjittertmplcontrolenable.yfilter != YFilter.not_set or
                    self.cipslaudpjittertmpldescription.yfilter != YFilter.not_set or
                    self.cipslaudpjittertmpldistbuckets.yfilter != YFilter.not_set or
                    self.cipslaudpjittertmpldistinterval.yfilter != YFilter.not_set or
                    self.cipslaudpjittertmplicpiffactor.yfilter != YFilter.not_set or
                    self.cipslaudpjittertmplinterval.yfilter != YFilter.not_set or
                    self.cipslaudpjittertmplntptolabs.yfilter != YFilter.not_set or
                    self.cipslaudpjittertmplntptolpct.yfilter != YFilter.not_set or
                    self.cipslaudpjittertmplntptoltype.yfilter != YFilter.not_set or
                    self.cipslaudpjittertmplnumpkts.yfilter != YFilter.not_set or
                    self.cipslaudpjittertmplpktpriority.yfilter != YFilter.not_set or
                    self.cipslaudpjittertmplprecision.yfilter != YFilter.not_set or
                    self.cipslaudpjittertmplreqdatasize.yfilter != YFilter.not_set or
                    self.cipslaudpjittertmplrowstatus.yfilter != YFilter.not_set or
                    self.cipslaudpjittertmplsrcaddr.yfilter != YFilter.not_set or
                    self.cipslaudpjittertmplsrcaddrtype.yfilter != YFilter.not_set or
                    self.cipslaudpjittertmplsrcport.yfilter != YFilter.not_set or
                    self.cipslaudpjittertmplstatshours.yfilter != YFilter.not_set or
                    self.cipslaudpjittertmplstoragetype.yfilter != YFilter.not_set or
                    self.cipslaudpjittertmplthreshold.yfilter != YFilter.not_set or
                    self.cipslaudpjittertmpltimeout.yfilter != YFilter.not_set or
                    self.cipslaudpjittertmpltos.yfilter != YFilter.not_set or
                    self.cipslaudpjittertmplverifydata.yfilter != YFilter.not_set or
                    self.cipslaudpjittertmplvrfname.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cipslaUdpJitterTmplEntry" + "[cipslaUdpJitterTmplName='" + self.cipslaudpjittertmplname.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-IPSLA-JITTER-MIB:CISCO-IPSLA-JITTER-MIB/cipslaUdpJitterTmplTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cipslaudpjittertmplname.is_set or self.cipslaudpjittertmplname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaudpjittertmplname.get_name_leafdata())
                if (self.cipslaudpjittertmplcodecinterval.is_set or self.cipslaudpjittertmplcodecinterval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaudpjittertmplcodecinterval.get_name_leafdata())
                if (self.cipslaudpjittertmplcodecnumpkts.is_set or self.cipslaudpjittertmplcodecnumpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaudpjittertmplcodecnumpkts.get_name_leafdata())
                if (self.cipslaudpjittertmplcodecpayload.is_set or self.cipslaudpjittertmplcodecpayload.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaudpjittertmplcodecpayload.get_name_leafdata())
                if (self.cipslaudpjittertmplcodectype.is_set or self.cipslaudpjittertmplcodectype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaudpjittertmplcodectype.get_name_leafdata())
                if (self.cipslaudpjittertmplcontrolenable.is_set or self.cipslaudpjittertmplcontrolenable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaudpjittertmplcontrolenable.get_name_leafdata())
                if (self.cipslaudpjittertmpldescription.is_set or self.cipslaudpjittertmpldescription.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaudpjittertmpldescription.get_name_leafdata())
                if (self.cipslaudpjittertmpldistbuckets.is_set or self.cipslaudpjittertmpldistbuckets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaudpjittertmpldistbuckets.get_name_leafdata())
                if (self.cipslaudpjittertmpldistinterval.is_set or self.cipslaudpjittertmpldistinterval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaudpjittertmpldistinterval.get_name_leafdata())
                if (self.cipslaudpjittertmplicpiffactor.is_set or self.cipslaudpjittertmplicpiffactor.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaudpjittertmplicpiffactor.get_name_leafdata())
                if (self.cipslaudpjittertmplinterval.is_set or self.cipslaudpjittertmplinterval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaudpjittertmplinterval.get_name_leafdata())
                if (self.cipslaudpjittertmplntptolabs.is_set or self.cipslaudpjittertmplntptolabs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaudpjittertmplntptolabs.get_name_leafdata())
                if (self.cipslaudpjittertmplntptolpct.is_set or self.cipslaudpjittertmplntptolpct.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaudpjittertmplntptolpct.get_name_leafdata())
                if (self.cipslaudpjittertmplntptoltype.is_set or self.cipslaudpjittertmplntptoltype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaudpjittertmplntptoltype.get_name_leafdata())
                if (self.cipslaudpjittertmplnumpkts.is_set or self.cipslaudpjittertmplnumpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaudpjittertmplnumpkts.get_name_leafdata())
                if (self.cipslaudpjittertmplpktpriority.is_set or self.cipslaudpjittertmplpktpriority.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaudpjittertmplpktpriority.get_name_leafdata())
                if (self.cipslaudpjittertmplprecision.is_set or self.cipslaudpjittertmplprecision.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaudpjittertmplprecision.get_name_leafdata())
                if (self.cipslaudpjittertmplreqdatasize.is_set or self.cipslaudpjittertmplreqdatasize.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaudpjittertmplreqdatasize.get_name_leafdata())
                if (self.cipslaudpjittertmplrowstatus.is_set or self.cipslaudpjittertmplrowstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaudpjittertmplrowstatus.get_name_leafdata())
                if (self.cipslaudpjittertmplsrcaddr.is_set or self.cipslaudpjittertmplsrcaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaudpjittertmplsrcaddr.get_name_leafdata())
                if (self.cipslaudpjittertmplsrcaddrtype.is_set or self.cipslaudpjittertmplsrcaddrtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaudpjittertmplsrcaddrtype.get_name_leafdata())
                if (self.cipslaudpjittertmplsrcport.is_set or self.cipslaudpjittertmplsrcport.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaudpjittertmplsrcport.get_name_leafdata())
                if (self.cipslaudpjittertmplstatshours.is_set or self.cipslaudpjittertmplstatshours.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaudpjittertmplstatshours.get_name_leafdata())
                if (self.cipslaudpjittertmplstoragetype.is_set or self.cipslaudpjittertmplstoragetype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaudpjittertmplstoragetype.get_name_leafdata())
                if (self.cipslaudpjittertmplthreshold.is_set or self.cipslaudpjittertmplthreshold.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaudpjittertmplthreshold.get_name_leafdata())
                if (self.cipslaudpjittertmpltimeout.is_set or self.cipslaudpjittertmpltimeout.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaudpjittertmpltimeout.get_name_leafdata())
                if (self.cipslaudpjittertmpltos.is_set or self.cipslaudpjittertmpltos.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaudpjittertmpltos.get_name_leafdata())
                if (self.cipslaudpjittertmplverifydata.is_set or self.cipslaudpjittertmplverifydata.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaudpjittertmplverifydata.get_name_leafdata())
                if (self.cipslaudpjittertmplvrfname.is_set or self.cipslaudpjittertmplvrfname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaudpjittertmplvrfname.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cipslaUdpJitterTmplName" or name == "cipslaUdpJitterTmplCodecInterval" or name == "cipslaUdpJitterTmplCodecNumPkts" or name == "cipslaUdpJitterTmplCodecPayload" or name == "cipslaUdpJitterTmplCodecType" or name == "cipslaUdpJitterTmplControlEnable" or name == "cipslaUdpJitterTmplDescription" or name == "cipslaUdpJitterTmplDistBuckets" or name == "cipslaUdpJitterTmplDistInterval" or name == "cipslaUdpJitterTmplIcpifFactor" or name == "cipslaUdpJitterTmplInterval" or name == "cipslaUdpJitterTmplNTPTolAbs" or name == "cipslaUdpJitterTmplNTPTolPct" or name == "cipslaUdpJitterTmplNTPTolType" or name == "cipslaUdpJitterTmplNumPkts" or name == "cipslaUdpJitterTmplPktPriority" or name == "cipslaUdpJitterTmplPrecision" or name == "cipslaUdpJitterTmplReqDataSize" or name == "cipslaUdpJitterTmplRowStatus" or name == "cipslaUdpJitterTmplSrcAddr" or name == "cipslaUdpJitterTmplSrcAddrType" or name == "cipslaUdpJitterTmplSrcPort" or name == "cipslaUdpJitterTmplStatsHours" or name == "cipslaUdpJitterTmplStorageType" or name == "cipslaUdpJitterTmplThreshold" or name == "cipslaUdpJitterTmplTimeOut" or name == "cipslaUdpJitterTmplTOS" or name == "cipslaUdpJitterTmplVerifyData" or name == "cipslaUdpJitterTmplVrfName"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cipslaUdpJitterTmplName"):
                    self.cipslaudpjittertmplname = value
                    self.cipslaudpjittertmplname.value_namespace = name_space
                    self.cipslaudpjittertmplname.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaUdpJitterTmplCodecInterval"):
                    self.cipslaudpjittertmplcodecinterval = value
                    self.cipslaudpjittertmplcodecinterval.value_namespace = name_space
                    self.cipslaudpjittertmplcodecinterval.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaUdpJitterTmplCodecNumPkts"):
                    self.cipslaudpjittertmplcodecnumpkts = value
                    self.cipslaudpjittertmplcodecnumpkts.value_namespace = name_space
                    self.cipslaudpjittertmplcodecnumpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaUdpJitterTmplCodecPayload"):
                    self.cipslaudpjittertmplcodecpayload = value
                    self.cipslaudpjittertmplcodecpayload.value_namespace = name_space
                    self.cipslaudpjittertmplcodecpayload.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaUdpJitterTmplCodecType"):
                    self.cipslaudpjittertmplcodectype = value
                    self.cipslaudpjittertmplcodectype.value_namespace = name_space
                    self.cipslaudpjittertmplcodectype.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaUdpJitterTmplControlEnable"):
                    self.cipslaudpjittertmplcontrolenable = value
                    self.cipslaudpjittertmplcontrolenable.value_namespace = name_space
                    self.cipslaudpjittertmplcontrolenable.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaUdpJitterTmplDescription"):
                    self.cipslaudpjittertmpldescription = value
                    self.cipslaudpjittertmpldescription.value_namespace = name_space
                    self.cipslaudpjittertmpldescription.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaUdpJitterTmplDistBuckets"):
                    self.cipslaudpjittertmpldistbuckets = value
                    self.cipslaudpjittertmpldistbuckets.value_namespace = name_space
                    self.cipslaudpjittertmpldistbuckets.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaUdpJitterTmplDistInterval"):
                    self.cipslaudpjittertmpldistinterval = value
                    self.cipslaudpjittertmpldistinterval.value_namespace = name_space
                    self.cipslaudpjittertmpldistinterval.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaUdpJitterTmplIcpifFactor"):
                    self.cipslaudpjittertmplicpiffactor = value
                    self.cipslaudpjittertmplicpiffactor.value_namespace = name_space
                    self.cipslaudpjittertmplicpiffactor.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaUdpJitterTmplInterval"):
                    self.cipslaudpjittertmplinterval = value
                    self.cipslaudpjittertmplinterval.value_namespace = name_space
                    self.cipslaudpjittertmplinterval.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaUdpJitterTmplNTPTolAbs"):
                    self.cipslaudpjittertmplntptolabs = value
                    self.cipslaudpjittertmplntptolabs.value_namespace = name_space
                    self.cipslaudpjittertmplntptolabs.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaUdpJitterTmplNTPTolPct"):
                    self.cipslaudpjittertmplntptolpct = value
                    self.cipslaudpjittertmplntptolpct.value_namespace = name_space
                    self.cipslaudpjittertmplntptolpct.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaUdpJitterTmplNTPTolType"):
                    self.cipslaudpjittertmplntptoltype = value
                    self.cipslaudpjittertmplntptoltype.value_namespace = name_space
                    self.cipslaudpjittertmplntptoltype.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaUdpJitterTmplNumPkts"):
                    self.cipslaudpjittertmplnumpkts = value
                    self.cipslaudpjittertmplnumpkts.value_namespace = name_space
                    self.cipslaudpjittertmplnumpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaUdpJitterTmplPktPriority"):
                    self.cipslaudpjittertmplpktpriority = value
                    self.cipslaudpjittertmplpktpriority.value_namespace = name_space
                    self.cipslaudpjittertmplpktpriority.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaUdpJitterTmplPrecision"):
                    self.cipslaudpjittertmplprecision = value
                    self.cipslaudpjittertmplprecision.value_namespace = name_space
                    self.cipslaudpjittertmplprecision.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaUdpJitterTmplReqDataSize"):
                    self.cipslaudpjittertmplreqdatasize = value
                    self.cipslaudpjittertmplreqdatasize.value_namespace = name_space
                    self.cipslaudpjittertmplreqdatasize.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaUdpJitterTmplRowStatus"):
                    self.cipslaudpjittertmplrowstatus = value
                    self.cipslaudpjittertmplrowstatus.value_namespace = name_space
                    self.cipslaudpjittertmplrowstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaUdpJitterTmplSrcAddr"):
                    self.cipslaudpjittertmplsrcaddr = value
                    self.cipslaudpjittertmplsrcaddr.value_namespace = name_space
                    self.cipslaudpjittertmplsrcaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaUdpJitterTmplSrcAddrType"):
                    self.cipslaudpjittertmplsrcaddrtype = value
                    self.cipslaudpjittertmplsrcaddrtype.value_namespace = name_space
                    self.cipslaudpjittertmplsrcaddrtype.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaUdpJitterTmplSrcPort"):
                    self.cipslaudpjittertmplsrcport = value
                    self.cipslaudpjittertmplsrcport.value_namespace = name_space
                    self.cipslaudpjittertmplsrcport.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaUdpJitterTmplStatsHours"):
                    self.cipslaudpjittertmplstatshours = value
                    self.cipslaudpjittertmplstatshours.value_namespace = name_space
                    self.cipslaudpjittertmplstatshours.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaUdpJitterTmplStorageType"):
                    self.cipslaudpjittertmplstoragetype = value
                    self.cipslaudpjittertmplstoragetype.value_namespace = name_space
                    self.cipslaudpjittertmplstoragetype.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaUdpJitterTmplThreshold"):
                    self.cipslaudpjittertmplthreshold = value
                    self.cipslaudpjittertmplthreshold.value_namespace = name_space
                    self.cipslaudpjittertmplthreshold.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaUdpJitterTmplTimeOut"):
                    self.cipslaudpjittertmpltimeout = value
                    self.cipslaudpjittertmpltimeout.value_namespace = name_space
                    self.cipslaudpjittertmpltimeout.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaUdpJitterTmplTOS"):
                    self.cipslaudpjittertmpltos = value
                    self.cipslaudpjittertmpltos.value_namespace = name_space
                    self.cipslaudpjittertmpltos.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaUdpJitterTmplVerifyData"):
                    self.cipslaudpjittertmplverifydata = value
                    self.cipslaudpjittertmplverifydata.value_namespace = name_space
                    self.cipslaudpjittertmplverifydata.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaUdpJitterTmplVrfName"):
                    self.cipslaudpjittertmplvrfname = value
                    self.cipslaudpjittertmplvrfname.value_namespace = name_space
                    self.cipslaudpjittertmplvrfname.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cipslaudpjittertmplentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cipslaudpjittertmplentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cipslaUdpJitterTmplTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IPSLA-JITTER-MIB:CISCO-IPSLA-JITTER-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cipslaUdpJitterTmplEntry"):
                for c in self.cipslaudpjittertmplentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoIpslaJitterMib.Cipslaudpjittertmpltable.Cipslaudpjittertmplentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cipslaudpjittertmplentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cipslaUdpJitterTmplEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cipslaicmpjittertmpltable(Entity):
        """
        A table that contains ICMP jitter template specific definitions.
        
        .. attribute:: cipslaicmpjittertmplentry
        
        	A row entry representing an IP SLA ICMP Jitter template
        	**type**\: list of    :py:class:`Cipslaicmpjittertmplentry <ydk.models.cisco_ios_xe.CISCO_IPSLA_JITTER_MIB.CiscoIpslaJitterMib.Cipslaicmpjittertmpltable.Cipslaicmpjittertmplentry>`
        
        

        """

        _prefix = 'CISCO-IPSLA-JITTER-MIB'
        _revision = '2007-07-24'

        def __init__(self):
            super(CiscoIpslaJitterMib.Cipslaicmpjittertmpltable, self).__init__()

            self.yang_name = "cipslaIcmpJitterTmplTable"
            self.yang_parent_name = "CISCO-IPSLA-JITTER-MIB"

            self.cipslaicmpjittertmplentry = YList(self)

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
                        super(CiscoIpslaJitterMib.Cipslaicmpjittertmpltable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIpslaJitterMib.Cipslaicmpjittertmpltable, self).__setattr__(name, value)


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
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: cipslaicmpjittertmplsrcaddr
            
            	A string which specifies the IP address of the source
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cipslaicmpjittertmplsrcaddrtype
            
            	An enumerated value which specifies the IP address type of the source. It must be used along with the cipslaIcmpJitterTmplSrcAddr object
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
            .. attribute:: cipslaicmpjittertmplstatshours
            
            	The maximum number of hourss for which statistics are maintained. Specifically this is the number of hourly groups to keep before rolling over.  The value of one is not advisable because the hourly group will close and immediately be deleted before the network management station will have the opportunity to retrieve the statistics.  The value of zero will shut off data collection
            	**type**\:  int
            
            	**range:** 0..25
            
            	**units**\: hours
            
            .. attribute:: cipslaicmpjittertmplstoragetype
            
            	The storage type of this conceptual row
            	**type**\:   :py:class:`Storagetype <ydk.models.cisco_ios_xe.SNMPv2_TC.Storagetype>`
            
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
                super(CiscoIpslaJitterMib.Cipslaicmpjittertmpltable.Cipslaicmpjittertmplentry, self).__init__()

                self.yang_name = "cipslaIcmpJitterTmplEntry"
                self.yang_parent_name = "cipslaIcmpJitterTmplTable"

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

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cipslaicmpjittertmplname",
                                "cipslaicmpjittertmpldescription",
                                "cipslaicmpjittertmpldistbuckets",
                                "cipslaicmpjittertmpldistinterval",
                                "cipslaicmpjittertmplinterval",
                                "cipslaicmpjittertmplnumpkts",
                                "cipslaicmpjittertmplrowstatus",
                                "cipslaicmpjittertmplsrcaddr",
                                "cipslaicmpjittertmplsrcaddrtype",
                                "cipslaicmpjittertmplstatshours",
                                "cipslaicmpjittertmplstoragetype",
                                "cipslaicmpjittertmplthreshold",
                                "cipslaicmpjittertmpltimeout",
                                "cipslaicmpjittertmpltos",
                                "cipslaicmpjittertmplverifydata",
                                "cipslaicmpjittertmplvrfname") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoIpslaJitterMib.Cipslaicmpjittertmpltable.Cipslaicmpjittertmplentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoIpslaJitterMib.Cipslaicmpjittertmpltable.Cipslaicmpjittertmplentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cipslaicmpjittertmplname.is_set or
                    self.cipslaicmpjittertmpldescription.is_set or
                    self.cipslaicmpjittertmpldistbuckets.is_set or
                    self.cipslaicmpjittertmpldistinterval.is_set or
                    self.cipslaicmpjittertmplinterval.is_set or
                    self.cipslaicmpjittertmplnumpkts.is_set or
                    self.cipslaicmpjittertmplrowstatus.is_set or
                    self.cipslaicmpjittertmplsrcaddr.is_set or
                    self.cipslaicmpjittertmplsrcaddrtype.is_set or
                    self.cipslaicmpjittertmplstatshours.is_set or
                    self.cipslaicmpjittertmplstoragetype.is_set or
                    self.cipslaicmpjittertmplthreshold.is_set or
                    self.cipslaicmpjittertmpltimeout.is_set or
                    self.cipslaicmpjittertmpltos.is_set or
                    self.cipslaicmpjittertmplverifydata.is_set or
                    self.cipslaicmpjittertmplvrfname.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cipslaicmpjittertmplname.yfilter != YFilter.not_set or
                    self.cipslaicmpjittertmpldescription.yfilter != YFilter.not_set or
                    self.cipslaicmpjittertmpldistbuckets.yfilter != YFilter.not_set or
                    self.cipslaicmpjittertmpldistinterval.yfilter != YFilter.not_set or
                    self.cipslaicmpjittertmplinterval.yfilter != YFilter.not_set or
                    self.cipslaicmpjittertmplnumpkts.yfilter != YFilter.not_set or
                    self.cipslaicmpjittertmplrowstatus.yfilter != YFilter.not_set or
                    self.cipslaicmpjittertmplsrcaddr.yfilter != YFilter.not_set or
                    self.cipslaicmpjittertmplsrcaddrtype.yfilter != YFilter.not_set or
                    self.cipslaicmpjittertmplstatshours.yfilter != YFilter.not_set or
                    self.cipslaicmpjittertmplstoragetype.yfilter != YFilter.not_set or
                    self.cipslaicmpjittertmplthreshold.yfilter != YFilter.not_set or
                    self.cipslaicmpjittertmpltimeout.yfilter != YFilter.not_set or
                    self.cipslaicmpjittertmpltos.yfilter != YFilter.not_set or
                    self.cipslaicmpjittertmplverifydata.yfilter != YFilter.not_set or
                    self.cipslaicmpjittertmplvrfname.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cipslaIcmpJitterTmplEntry" + "[cipslaIcmpJitterTmplName='" + self.cipslaicmpjittertmplname.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-IPSLA-JITTER-MIB:CISCO-IPSLA-JITTER-MIB/cipslaIcmpJitterTmplTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cipslaicmpjittertmplname.is_set or self.cipslaicmpjittertmplname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaicmpjittertmplname.get_name_leafdata())
                if (self.cipslaicmpjittertmpldescription.is_set or self.cipslaicmpjittertmpldescription.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaicmpjittertmpldescription.get_name_leafdata())
                if (self.cipslaicmpjittertmpldistbuckets.is_set or self.cipslaicmpjittertmpldistbuckets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaicmpjittertmpldistbuckets.get_name_leafdata())
                if (self.cipslaicmpjittertmpldistinterval.is_set or self.cipslaicmpjittertmpldistinterval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaicmpjittertmpldistinterval.get_name_leafdata())
                if (self.cipslaicmpjittertmplinterval.is_set or self.cipslaicmpjittertmplinterval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaicmpjittertmplinterval.get_name_leafdata())
                if (self.cipslaicmpjittertmplnumpkts.is_set or self.cipslaicmpjittertmplnumpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaicmpjittertmplnumpkts.get_name_leafdata())
                if (self.cipslaicmpjittertmplrowstatus.is_set or self.cipslaicmpjittertmplrowstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaicmpjittertmplrowstatus.get_name_leafdata())
                if (self.cipslaicmpjittertmplsrcaddr.is_set or self.cipslaicmpjittertmplsrcaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaicmpjittertmplsrcaddr.get_name_leafdata())
                if (self.cipslaicmpjittertmplsrcaddrtype.is_set or self.cipslaicmpjittertmplsrcaddrtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaicmpjittertmplsrcaddrtype.get_name_leafdata())
                if (self.cipslaicmpjittertmplstatshours.is_set or self.cipslaicmpjittertmplstatshours.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaicmpjittertmplstatshours.get_name_leafdata())
                if (self.cipslaicmpjittertmplstoragetype.is_set or self.cipslaicmpjittertmplstoragetype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaicmpjittertmplstoragetype.get_name_leafdata())
                if (self.cipslaicmpjittertmplthreshold.is_set or self.cipslaicmpjittertmplthreshold.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaicmpjittertmplthreshold.get_name_leafdata())
                if (self.cipslaicmpjittertmpltimeout.is_set or self.cipslaicmpjittertmpltimeout.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaicmpjittertmpltimeout.get_name_leafdata())
                if (self.cipslaicmpjittertmpltos.is_set or self.cipslaicmpjittertmpltos.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaicmpjittertmpltos.get_name_leafdata())
                if (self.cipslaicmpjittertmplverifydata.is_set or self.cipslaicmpjittertmplverifydata.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaicmpjittertmplverifydata.get_name_leafdata())
                if (self.cipslaicmpjittertmplvrfname.is_set or self.cipslaicmpjittertmplvrfname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaicmpjittertmplvrfname.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cipslaIcmpJitterTmplName" or name == "cipslaIcmpJitterTmplDescription" or name == "cipslaIcmpJitterTmplDistBuckets" or name == "cipslaIcmpJitterTmplDistInterval" or name == "cipslaIcmpJitterTmplInterval" or name == "cipslaIcmpJitterTmplNumPkts" or name == "cipslaIcmpJitterTmplRowStatus" or name == "cipslaIcmpJitterTmplSrcAddr" or name == "cipslaIcmpJitterTmplSrcAddrType" or name == "cipslaIcmpJitterTmplStatsHours" or name == "cipslaIcmpJitterTmplStorageType" or name == "cipslaIcmpJitterTmplThreshold" or name == "cipslaIcmpJitterTmplTimeOut" or name == "cipslaIcmpJitterTmplTOS" or name == "cipslaIcmpJitterTmplVerifyData" or name == "cipslaIcmpJitterTmplVrfName"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cipslaIcmpJitterTmplName"):
                    self.cipslaicmpjittertmplname = value
                    self.cipslaicmpjittertmplname.value_namespace = name_space
                    self.cipslaicmpjittertmplname.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaIcmpJitterTmplDescription"):
                    self.cipslaicmpjittertmpldescription = value
                    self.cipslaicmpjittertmpldescription.value_namespace = name_space
                    self.cipslaicmpjittertmpldescription.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaIcmpJitterTmplDistBuckets"):
                    self.cipslaicmpjittertmpldistbuckets = value
                    self.cipslaicmpjittertmpldistbuckets.value_namespace = name_space
                    self.cipslaicmpjittertmpldistbuckets.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaIcmpJitterTmplDistInterval"):
                    self.cipslaicmpjittertmpldistinterval = value
                    self.cipslaicmpjittertmpldistinterval.value_namespace = name_space
                    self.cipslaicmpjittertmpldistinterval.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaIcmpJitterTmplInterval"):
                    self.cipslaicmpjittertmplinterval = value
                    self.cipslaicmpjittertmplinterval.value_namespace = name_space
                    self.cipslaicmpjittertmplinterval.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaIcmpJitterTmplNumPkts"):
                    self.cipslaicmpjittertmplnumpkts = value
                    self.cipslaicmpjittertmplnumpkts.value_namespace = name_space
                    self.cipslaicmpjittertmplnumpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaIcmpJitterTmplRowStatus"):
                    self.cipslaicmpjittertmplrowstatus = value
                    self.cipslaicmpjittertmplrowstatus.value_namespace = name_space
                    self.cipslaicmpjittertmplrowstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaIcmpJitterTmplSrcAddr"):
                    self.cipslaicmpjittertmplsrcaddr = value
                    self.cipslaicmpjittertmplsrcaddr.value_namespace = name_space
                    self.cipslaicmpjittertmplsrcaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaIcmpJitterTmplSrcAddrType"):
                    self.cipslaicmpjittertmplsrcaddrtype = value
                    self.cipslaicmpjittertmplsrcaddrtype.value_namespace = name_space
                    self.cipslaicmpjittertmplsrcaddrtype.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaIcmpJitterTmplStatsHours"):
                    self.cipslaicmpjittertmplstatshours = value
                    self.cipslaicmpjittertmplstatshours.value_namespace = name_space
                    self.cipslaicmpjittertmplstatshours.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaIcmpJitterTmplStorageType"):
                    self.cipslaicmpjittertmplstoragetype = value
                    self.cipslaicmpjittertmplstoragetype.value_namespace = name_space
                    self.cipslaicmpjittertmplstoragetype.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaIcmpJitterTmplThreshold"):
                    self.cipslaicmpjittertmplthreshold = value
                    self.cipslaicmpjittertmplthreshold.value_namespace = name_space
                    self.cipslaicmpjittertmplthreshold.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaIcmpJitterTmplTimeOut"):
                    self.cipslaicmpjittertmpltimeout = value
                    self.cipslaicmpjittertmpltimeout.value_namespace = name_space
                    self.cipslaicmpjittertmpltimeout.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaIcmpJitterTmplTOS"):
                    self.cipslaicmpjittertmpltos = value
                    self.cipslaicmpjittertmpltos.value_namespace = name_space
                    self.cipslaicmpjittertmpltos.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaIcmpJitterTmplVerifyData"):
                    self.cipslaicmpjittertmplverifydata = value
                    self.cipslaicmpjittertmplverifydata.value_namespace = name_space
                    self.cipslaicmpjittertmplverifydata.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaIcmpJitterTmplVrfName"):
                    self.cipslaicmpjittertmplvrfname = value
                    self.cipslaicmpjittertmplvrfname.value_namespace = name_space
                    self.cipslaicmpjittertmplvrfname.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cipslaicmpjittertmplentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cipslaicmpjittertmplentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cipslaIcmpJitterTmplTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IPSLA-JITTER-MIB:CISCO-IPSLA-JITTER-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cipslaIcmpJitterTmplEntry"):
                for c in self.cipslaicmpjittertmplentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoIpslaJitterMib.Cipslaicmpjittertmpltable.Cipslaicmpjittertmplentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cipslaicmpjittertmplentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cipslaIcmpJitterTmplEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.cipslaicmpjittertmpltable is not None and self.cipslaicmpjittertmpltable.has_data()) or
            (self.cipslaudpjittertmpltable is not None and self.cipslaudpjittertmpltable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.cipslaicmpjittertmpltable is not None and self.cipslaicmpjittertmpltable.has_operation()) or
            (self.cipslaudpjittertmpltable is not None and self.cipslaudpjittertmpltable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "CISCO-IPSLA-JITTER-MIB:CISCO-IPSLA-JITTER-MIB" + path_buffer

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

        if (child_yang_name == "cipslaIcmpJitterTmplTable"):
            if (self.cipslaicmpjittertmpltable is None):
                self.cipslaicmpjittertmpltable = CiscoIpslaJitterMib.Cipslaicmpjittertmpltable()
                self.cipslaicmpjittertmpltable.parent = self
                self._children_name_map["cipslaicmpjittertmpltable"] = "cipslaIcmpJitterTmplTable"
            return self.cipslaicmpjittertmpltable

        if (child_yang_name == "cipslaUdpJitterTmplTable"):
            if (self.cipslaudpjittertmpltable is None):
                self.cipslaudpjittertmpltable = CiscoIpslaJitterMib.Cipslaudpjittertmpltable()
                self.cipslaudpjittertmpltable.parent = self
                self._children_name_map["cipslaudpjittertmpltable"] = "cipslaUdpJitterTmplTable"
            return self.cipslaudpjittertmpltable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "cipslaIcmpJitterTmplTable" or name == "cipslaUdpJitterTmplTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CiscoIpslaJitterMib()
        return self._top_entity

