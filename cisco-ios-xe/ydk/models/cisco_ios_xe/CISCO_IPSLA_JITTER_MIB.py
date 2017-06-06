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


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class CiscoIpslaJitterMib(object):
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
        self.cipslaicmpjittertmpltable = CiscoIpslaJitterMib.Cipslaicmpjittertmpltable()
        self.cipslaicmpjittertmpltable.parent = self
        self.cipslaudpjittertmpltable = CiscoIpslaJitterMib.Cipslaudpjittertmpltable()
        self.cipslaudpjittertmpltable.parent = self


    class Cipslaudpjittertmpltable(object):
        """
        A table that contains UDP jitter template specific definitions.
        
        .. attribute:: cipslaudpjittertmplentry
        
        	A row entry representing an IPSLA UDP jitter template
        	**type**\: list of    :py:class:`Cipslaudpjittertmplentry <ydk.models.cisco_ios_xe.CISCO_IPSLA_JITTER_MIB.CiscoIpslaJitterMib.Cipslaudpjittertmpltable.Cipslaudpjittertmplentry>`
        
        

        """

        _prefix = 'CISCO-IPSLA-JITTER-MIB'
        _revision = '2007-07-24'

        def __init__(self):
            self.parent = None
            self.cipslaudpjittertmplentry = YList()
            self.cipslaudpjittertmplentry.parent = self
            self.cipslaudpjittertmplentry.name = 'cipslaudpjittertmplentry'


        class Cipslaudpjittertmplentry(object):
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
            	**type**\:   :py:class:`IpslacodectypeEnum <ydk.models.cisco_ios_xe.CISCO_IPSLA_TC_MIB.IpslacodectypeEnum>`
            
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
            	**type**\:   :py:class:`CipslaudpjittertmplntptoltypeEnum <ydk.models.cisco_ios_xe.CISCO_IPSLA_JITTER_MIB.CiscoIpslaJitterMib.Cipslaudpjittertmpltable.Cipslaudpjittertmplentry.CipslaudpjittertmplntptoltypeEnum>`
            
            .. attribute:: cipslaudpjittertmplnumpkts
            
            	This value represents the number of packets that need to be transmitted
            	**type**\:  int
            
            	**range:** 1..60000
            
            	**units**\: packets
            
            .. attribute:: cipslaudpjittertmplpktpriority
            
            	This object specifies the priority that will be assigned to operation packet.  normal(1) \- The packet is of normal priority. high(2)   \- The packet is of high priority
            	**type**\:   :py:class:`CipslaudpjittertmplpktpriorityEnum <ydk.models.cisco_ios_xe.CISCO_IPSLA_JITTER_MIB.CiscoIpslaJitterMib.Cipslaudpjittertmpltable.Cipslaudpjittertmplentry.CipslaudpjittertmplpktpriorityEnum>`
            
            .. attribute:: cipslaudpjittertmplprecision
            
            	This object specifies the accuracy of jitter statistics in rttMonJitterStatsTable that needs to be calculated. milliseconds(1) \- The accuracy of stats will be of milliseconds. microseconds(2) \- The accuracy of stats will be in microseconds
            	**type**\:   :py:class:`CipslaudpjittertmplprecisionEnum <ydk.models.cisco_ios_xe.CISCO_IPSLA_JITTER_MIB.CiscoIpslaJitterMib.Cipslaudpjittertmpltable.Cipslaudpjittertmplentry.CipslaudpjittertmplprecisionEnum>`
            
            .. attribute:: cipslaudpjittertmplreqdatasize
            
            	This object represents the number of octets to be placed into the ARR Data portion of the request message, when using SNA protocols.  For non\-ARR protocols' IP SLA request/responses, this value represents the native payload size.  REMEMBER\:  The ARR Header overhead is not included            in this value
            	**type**\:  int
            
            	**range:** 16..65024
            
            	**units**\: octets
            
            .. attribute:: cipslaudpjittertmplrowstatus
            
            	The status of the conceptual UDP Jitter template control row. When the status is active, all the read\-create objects in that  row can be modified
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            .. attribute:: cipslaudpjittertmplsrcaddr
            
            	This field specifies the IP address of the source
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cipslaudpjittertmplsrcaddrtype
            
            	An enumerated value which specifies the IP address type of the source. It must be used along with the cipslaUdpJitterTmplSrcAddr object
            	**type**\:   :py:class:`InetaddresstypeEnum <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetaddresstypeEnum>`
            
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
            	**type**\:   :py:class:`StoragetypeEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.StoragetypeEnum>`
            
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
                self.parent = None
                self.cipslaudpjittertmplname = None
                self.cipslaudpjittertmplcodecinterval = None
                self.cipslaudpjittertmplcodecnumpkts = None
                self.cipslaudpjittertmplcodecpayload = None
                self.cipslaudpjittertmplcodectype = None
                self.cipslaudpjittertmplcontrolenable = None
                self.cipslaudpjittertmpldescription = None
                self.cipslaudpjittertmpldistbuckets = None
                self.cipslaudpjittertmpldistinterval = None
                self.cipslaudpjittertmplicpiffactor = None
                self.cipslaudpjittertmplinterval = None
                self.cipslaudpjittertmplntptolabs = None
                self.cipslaudpjittertmplntptolpct = None
                self.cipslaudpjittertmplntptoltype = None
                self.cipslaudpjittertmplnumpkts = None
                self.cipslaudpjittertmplpktpriority = None
                self.cipslaudpjittertmplprecision = None
                self.cipslaudpjittertmplreqdatasize = None
                self.cipslaudpjittertmplrowstatus = None
                self.cipslaudpjittertmplsrcaddr = None
                self.cipslaudpjittertmplsrcaddrtype = None
                self.cipslaudpjittertmplsrcport = None
                self.cipslaudpjittertmplstatshours = None
                self.cipslaudpjittertmplstoragetype = None
                self.cipslaudpjittertmplthreshold = None
                self.cipslaudpjittertmpltimeout = None
                self.cipslaudpjittertmpltos = None
                self.cipslaudpjittertmplverifydata = None
                self.cipslaudpjittertmplvrfname = None

            class CipslaudpjittertmplntptoltypeEnum(Enum):
                """
                CipslaudpjittertmplntptoltypeEnum

                This object specifies whether the value specified for oneway

                NTP sync tolerance is absolute value or percent value.

                percent(1)  \- The value for oneway NTP sync tolerance is 

                              absolute value.

                absolute(2) \- The value for oneway NTP sync tolerance is 

                              percent value.

                .. data:: percent = 1

                .. data:: absolute = 2

                """

                percent = 1

                absolute = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_IPSLA_JITTER_MIB as meta
                    return meta._meta_table['CiscoIpslaJitterMib.Cipslaudpjittertmpltable.Cipslaudpjittertmplentry.CipslaudpjittertmplntptoltypeEnum']


            class CipslaudpjittertmplpktpriorityEnum(Enum):
                """
                CipslaudpjittertmplpktpriorityEnum

                This object specifies the priority that will be assigned

                to operation packet.

                normal(1) \- The packet is of normal priority.

                high(2)   \- The packet is of high priority.

                .. data:: normal = 1

                .. data:: high = 2

                """

                normal = 1

                high = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_IPSLA_JITTER_MIB as meta
                    return meta._meta_table['CiscoIpslaJitterMib.Cipslaudpjittertmpltable.Cipslaudpjittertmplentry.CipslaudpjittertmplpktpriorityEnum']


            class CipslaudpjittertmplprecisionEnum(Enum):
                """
                CipslaudpjittertmplprecisionEnum

                This object specifies the accuracy of jitter statistics in

                rttMonJitterStatsTable that needs to be calculated.

                milliseconds(1) \- The accuracy of stats will be of milliseconds.

                microseconds(2) \- The accuracy of stats will be in microseconds.

                .. data:: milliseconds = 1

                .. data:: microseconds = 2

                """

                milliseconds = 1

                microseconds = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_IPSLA_JITTER_MIB as meta
                    return meta._meta_table['CiscoIpslaJitterMib.Cipslaudpjittertmpltable.Cipslaudpjittertmplentry.CipslaudpjittertmplprecisionEnum']


            @property
            def _common_path(self):
                if self.cipslaudpjittertmplname is None:
                    raise YPYModelError('Key property cipslaudpjittertmplname is None')

                return '/CISCO-IPSLA-JITTER-MIB:CISCO-IPSLA-JITTER-MIB/CISCO-IPSLA-JITTER-MIB:cipslaUdpJitterTmplTable/CISCO-IPSLA-JITTER-MIB:cipslaUdpJitterTmplEntry[CISCO-IPSLA-JITTER-MIB:cipslaUdpJitterTmplName = ' + str(self.cipslaudpjittertmplname) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.cipslaudpjittertmplname is not None:
                    return True

                if self.cipslaudpjittertmplcodecinterval is not None:
                    return True

                if self.cipslaudpjittertmplcodecnumpkts is not None:
                    return True

                if self.cipslaudpjittertmplcodecpayload is not None:
                    return True

                if self.cipslaudpjittertmplcodectype is not None:
                    return True

                if self.cipslaudpjittertmplcontrolenable is not None:
                    return True

                if self.cipslaudpjittertmpldescription is not None:
                    return True

                if self.cipslaudpjittertmpldistbuckets is not None:
                    return True

                if self.cipslaudpjittertmpldistinterval is not None:
                    return True

                if self.cipslaudpjittertmplicpiffactor is not None:
                    return True

                if self.cipslaudpjittertmplinterval is not None:
                    return True

                if self.cipslaudpjittertmplntptolabs is not None:
                    return True

                if self.cipslaudpjittertmplntptolpct is not None:
                    return True

                if self.cipslaudpjittertmplntptoltype is not None:
                    return True

                if self.cipslaudpjittertmplnumpkts is not None:
                    return True

                if self.cipslaudpjittertmplpktpriority is not None:
                    return True

                if self.cipslaudpjittertmplprecision is not None:
                    return True

                if self.cipslaudpjittertmplreqdatasize is not None:
                    return True

                if self.cipslaudpjittertmplrowstatus is not None:
                    return True

                if self.cipslaudpjittertmplsrcaddr is not None:
                    return True

                if self.cipslaudpjittertmplsrcaddrtype is not None:
                    return True

                if self.cipslaudpjittertmplsrcport is not None:
                    return True

                if self.cipslaudpjittertmplstatshours is not None:
                    return True

                if self.cipslaudpjittertmplstoragetype is not None:
                    return True

                if self.cipslaudpjittertmplthreshold is not None:
                    return True

                if self.cipslaudpjittertmpltimeout is not None:
                    return True

                if self.cipslaudpjittertmpltos is not None:
                    return True

                if self.cipslaudpjittertmplverifydata is not None:
                    return True

                if self.cipslaudpjittertmplvrfname is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_IPSLA_JITTER_MIB as meta
                return meta._meta_table['CiscoIpslaJitterMib.Cipslaudpjittertmpltable.Cipslaudpjittertmplentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IPSLA-JITTER-MIB:CISCO-IPSLA-JITTER-MIB/CISCO-IPSLA-JITTER-MIB:cipslaUdpJitterTmplTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cipslaudpjittertmplentry is not None:
                for child_ref in self.cipslaudpjittertmplentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_IPSLA_JITTER_MIB as meta
            return meta._meta_table['CiscoIpslaJitterMib.Cipslaudpjittertmpltable']['meta_info']


    class Cipslaicmpjittertmpltable(object):
        """
        A table that contains ICMP jitter template specific definitions.
        
        .. attribute:: cipslaicmpjittertmplentry
        
        	A row entry representing an IP SLA ICMP Jitter template
        	**type**\: list of    :py:class:`Cipslaicmpjittertmplentry <ydk.models.cisco_ios_xe.CISCO_IPSLA_JITTER_MIB.CiscoIpslaJitterMib.Cipslaicmpjittertmpltable.Cipslaicmpjittertmplentry>`
        
        

        """

        _prefix = 'CISCO-IPSLA-JITTER-MIB'
        _revision = '2007-07-24'

        def __init__(self):
            self.parent = None
            self.cipslaicmpjittertmplentry = YList()
            self.cipslaicmpjittertmplentry.parent = self
            self.cipslaicmpjittertmplentry.name = 'cipslaicmpjittertmplentry'


        class Cipslaicmpjittertmplentry(object):
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
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            .. attribute:: cipslaicmpjittertmplsrcaddr
            
            	A string which specifies the IP address of the source
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cipslaicmpjittertmplsrcaddrtype
            
            	An enumerated value which specifies the IP address type of the source. It must be used along with the cipslaIcmpJitterTmplSrcAddr object
            	**type**\:   :py:class:`InetaddresstypeEnum <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetaddresstypeEnum>`
            
            .. attribute:: cipslaicmpjittertmplstatshours
            
            	The maximum number of hourss for which statistics are maintained. Specifically this is the number of hourly groups to keep before rolling over.  The value of one is not advisable because the hourly group will close and immediately be deleted before the network management station will have the opportunity to retrieve the statistics.  The value of zero will shut off data collection
            	**type**\:  int
            
            	**range:** 0..25
            
            	**units**\: hours
            
            .. attribute:: cipslaicmpjittertmplstoragetype
            
            	The storage type of this conceptual row
            	**type**\:   :py:class:`StoragetypeEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.StoragetypeEnum>`
            
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
                self.parent = None
                self.cipslaicmpjittertmplname = None
                self.cipslaicmpjittertmpldescription = None
                self.cipslaicmpjittertmpldistbuckets = None
                self.cipslaicmpjittertmpldistinterval = None
                self.cipslaicmpjittertmplinterval = None
                self.cipslaicmpjittertmplnumpkts = None
                self.cipslaicmpjittertmplrowstatus = None
                self.cipslaicmpjittertmplsrcaddr = None
                self.cipslaicmpjittertmplsrcaddrtype = None
                self.cipslaicmpjittertmplstatshours = None
                self.cipslaicmpjittertmplstoragetype = None
                self.cipslaicmpjittertmplthreshold = None
                self.cipslaicmpjittertmpltimeout = None
                self.cipslaicmpjittertmpltos = None
                self.cipslaicmpjittertmplverifydata = None
                self.cipslaicmpjittertmplvrfname = None

            @property
            def _common_path(self):
                if self.cipslaicmpjittertmplname is None:
                    raise YPYModelError('Key property cipslaicmpjittertmplname is None')

                return '/CISCO-IPSLA-JITTER-MIB:CISCO-IPSLA-JITTER-MIB/CISCO-IPSLA-JITTER-MIB:cipslaIcmpJitterTmplTable/CISCO-IPSLA-JITTER-MIB:cipslaIcmpJitterTmplEntry[CISCO-IPSLA-JITTER-MIB:cipslaIcmpJitterTmplName = ' + str(self.cipslaicmpjittertmplname) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.cipslaicmpjittertmplname is not None:
                    return True

                if self.cipslaicmpjittertmpldescription is not None:
                    return True

                if self.cipslaicmpjittertmpldistbuckets is not None:
                    return True

                if self.cipslaicmpjittertmpldistinterval is not None:
                    return True

                if self.cipslaicmpjittertmplinterval is not None:
                    return True

                if self.cipslaicmpjittertmplnumpkts is not None:
                    return True

                if self.cipslaicmpjittertmplrowstatus is not None:
                    return True

                if self.cipslaicmpjittertmplsrcaddr is not None:
                    return True

                if self.cipslaicmpjittertmplsrcaddrtype is not None:
                    return True

                if self.cipslaicmpjittertmplstatshours is not None:
                    return True

                if self.cipslaicmpjittertmplstoragetype is not None:
                    return True

                if self.cipslaicmpjittertmplthreshold is not None:
                    return True

                if self.cipslaicmpjittertmpltimeout is not None:
                    return True

                if self.cipslaicmpjittertmpltos is not None:
                    return True

                if self.cipslaicmpjittertmplverifydata is not None:
                    return True

                if self.cipslaicmpjittertmplvrfname is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_IPSLA_JITTER_MIB as meta
                return meta._meta_table['CiscoIpslaJitterMib.Cipslaicmpjittertmpltable.Cipslaicmpjittertmplentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IPSLA-JITTER-MIB:CISCO-IPSLA-JITTER-MIB/CISCO-IPSLA-JITTER-MIB:cipslaIcmpJitterTmplTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cipslaicmpjittertmplentry is not None:
                for child_ref in self.cipslaicmpjittertmplentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_IPSLA_JITTER_MIB as meta
            return meta._meta_table['CiscoIpslaJitterMib.Cipslaicmpjittertmpltable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-IPSLA-JITTER-MIB:CISCO-IPSLA-JITTER-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.cipslaicmpjittertmpltable is not None and self.cipslaicmpjittertmpltable._has_data():
            return True

        if self.cipslaudpjittertmpltable is not None and self.cipslaudpjittertmpltable._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_IPSLA_JITTER_MIB as meta
        return meta._meta_table['CiscoIpslaJitterMib']['meta_info']


