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


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class CiscoIpslaEchoMib(object):
    """
    
    
    .. attribute:: cipslaicmpechotmpltable
    
    	A table that contains ICMP echo template definitions
    	**type**\:   :py:class:`Cipslaicmpechotmpltable <ydk.models.cisco_ios_xe.CISCO_IPSLA_ECHO_MIB.CiscoIpslaEchoMib.Cipslaicmpechotmpltable>`
    
    .. attribute:: cipslatcpconntmpltable
    
    	A table that contains TCP connect template specific definitions
    	**type**\:   :py:class:`Cipslatcpconntmpltable <ydk.models.cisco_ios_xe.CISCO_IPSLA_ECHO_MIB.CiscoIpslaEchoMib.Cipslatcpconntmpltable>`
    
    .. attribute:: cipslaudpechotmpltable
    
    	A table that contains UDP echo template specific definitions
    	**type**\:   :py:class:`Cipslaudpechotmpltable <ydk.models.cisco_ios_xe.CISCO_IPSLA_ECHO_MIB.CiscoIpslaEchoMib.Cipslaudpechotmpltable>`
    
    

    """

    _prefix = 'CISCO-IPSLA-ECHO-MIB'
    _revision = '2007-08-16'

    def __init__(self):
        self.cipslaicmpechotmpltable = CiscoIpslaEchoMib.Cipslaicmpechotmpltable()
        self.cipslaicmpechotmpltable.parent = self
        self.cipslatcpconntmpltable = CiscoIpslaEchoMib.Cipslatcpconntmpltable()
        self.cipslatcpconntmpltable.parent = self
        self.cipslaudpechotmpltable = CiscoIpslaEchoMib.Cipslaudpechotmpltable()
        self.cipslaudpechotmpltable.parent = self


    class Cipslaicmpechotmpltable(object):
        """
        A table that contains ICMP echo template definitions.
        
        .. attribute:: cipslaicmpechotmplentry
        
        	A row entry representing an IPSLA ICMP echo template
        	**type**\: list of    :py:class:`Cipslaicmpechotmplentry <ydk.models.cisco_ios_xe.CISCO_IPSLA_ECHO_MIB.CiscoIpslaEchoMib.Cipslaicmpechotmpltable.Cipslaicmpechotmplentry>`
        
        

        """

        _prefix = 'CISCO-IPSLA-ECHO-MIB'
        _revision = '2007-08-16'

        def __init__(self):
            self.parent = None
            self.cipslaicmpechotmplentry = YList()
            self.cipslaicmpechotmplentry.parent = self
            self.cipslaicmpechotmplentry.name = 'cipslaicmpechotmplentry'


        class Cipslaicmpechotmplentry(object):
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
            	**type**\:   :py:class:`CipslaicmpechotmplhistfilterEnum <ydk.models.cisco_ios_xe.CISCO_IPSLA_ECHO_MIB.CiscoIpslaEchoMib.Cipslaicmpechotmpltable.Cipslaicmpechotmplentry.CipslaicmpechotmplhistfilterEnum>`
            
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
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            .. attribute:: cipslaicmpechotmplsrcaddr
            
            	A string which specifies the IP address of the source
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cipslaicmpechotmplsrcaddrtype
            
            	An enumerated value which specifies the IP address type of the source. It must be used along with the cipslaIcmpEchoTmplSrcAddr object
            	**type**\:   :py:class:`InetaddresstypeEnum <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetaddresstypeEnum>`
            
            .. attribute:: cipslaicmpechotmplstatshours
            
            	The maximum number of hours for which statistics are maintained. Specifically this is the number of hourly  groups to keep before rolling over.  The value of one is not advisable because the hourly group will close and immediately be deleted before the network management station will have the opportunity to retrieve the statistics.  The value of zero will shut off data collection
            	**type**\:  int
            
            	**range:** 0..25
            
            	**units**\: hours
            
            .. attribute:: cipslaicmpechotmplstoragetype
            
            	The storage type of this conceptual row
            	**type**\:   :py:class:`StoragetypeEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.StoragetypeEnum>`
            
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
                self.parent = None
                self.cipslaicmpechotmplname = None
                self.cipslaicmpechotmpldescription = None
                self.cipslaicmpechotmpldistbuckets = None
                self.cipslaicmpechotmpldistinterval = None
                self.cipslaicmpechotmplhistbuckets = None
                self.cipslaicmpechotmplhistfilter = None
                self.cipslaicmpechotmplhistlives = None
                self.cipslaicmpechotmplreqdatasize = None
                self.cipslaicmpechotmplrowstatus = None
                self.cipslaicmpechotmplsrcaddr = None
                self.cipslaicmpechotmplsrcaddrtype = None
                self.cipslaicmpechotmplstatshours = None
                self.cipslaicmpechotmplstoragetype = None
                self.cipslaicmpechotmplthreshold = None
                self.cipslaicmpechotmpltimeout = None
                self.cipslaicmpechotmpltos = None
                self.cipslaicmpechotmplverifydata = None
                self.cipslaicmpechotmplvrfname = None

            class CipslaicmpechotmplhistfilterEnum(Enum):
                """
                CipslaicmpechotmplhistfilterEnum

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

                none = 1

                all = 2

                overThreshold = 3

                failures = 4


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_IPSLA_ECHO_MIB as meta
                    return meta._meta_table['CiscoIpslaEchoMib.Cipslaicmpechotmpltable.Cipslaicmpechotmplentry.CipslaicmpechotmplhistfilterEnum']


            @property
            def _common_path(self):
                if self.cipslaicmpechotmplname is None:
                    raise YPYModelError('Key property cipslaicmpechotmplname is None')

                return '/CISCO-IPSLA-ECHO-MIB:CISCO-IPSLA-ECHO-MIB/CISCO-IPSLA-ECHO-MIB:cipslaIcmpEchoTmplTable/CISCO-IPSLA-ECHO-MIB:cipslaIcmpEchoTmplEntry[CISCO-IPSLA-ECHO-MIB:cipslaIcmpEchoTmplName = ' + str(self.cipslaicmpechotmplname) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.cipslaicmpechotmplname is not None:
                    return True

                if self.cipslaicmpechotmpldescription is not None:
                    return True

                if self.cipslaicmpechotmpldistbuckets is not None:
                    return True

                if self.cipslaicmpechotmpldistinterval is not None:
                    return True

                if self.cipslaicmpechotmplhistbuckets is not None:
                    return True

                if self.cipslaicmpechotmplhistfilter is not None:
                    return True

                if self.cipslaicmpechotmplhistlives is not None:
                    return True

                if self.cipslaicmpechotmplreqdatasize is not None:
                    return True

                if self.cipslaicmpechotmplrowstatus is not None:
                    return True

                if self.cipslaicmpechotmplsrcaddr is not None:
                    return True

                if self.cipslaicmpechotmplsrcaddrtype is not None:
                    return True

                if self.cipslaicmpechotmplstatshours is not None:
                    return True

                if self.cipslaicmpechotmplstoragetype is not None:
                    return True

                if self.cipslaicmpechotmplthreshold is not None:
                    return True

                if self.cipslaicmpechotmpltimeout is not None:
                    return True

                if self.cipslaicmpechotmpltos is not None:
                    return True

                if self.cipslaicmpechotmplverifydata is not None:
                    return True

                if self.cipslaicmpechotmplvrfname is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_IPSLA_ECHO_MIB as meta
                return meta._meta_table['CiscoIpslaEchoMib.Cipslaicmpechotmpltable.Cipslaicmpechotmplentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IPSLA-ECHO-MIB:CISCO-IPSLA-ECHO-MIB/CISCO-IPSLA-ECHO-MIB:cipslaIcmpEchoTmplTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cipslaicmpechotmplentry is not None:
                for child_ref in self.cipslaicmpechotmplentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_IPSLA_ECHO_MIB as meta
            return meta._meta_table['CiscoIpslaEchoMib.Cipslaicmpechotmpltable']['meta_info']


    class Cipslaudpechotmpltable(object):
        """
        A table that contains UDP echo template specific definitions.
        
        .. attribute:: cipslaudpechotmplentry
        
        	A row entry representing an IPSLA UDP echo template
        	**type**\: list of    :py:class:`Cipslaudpechotmplentry <ydk.models.cisco_ios_xe.CISCO_IPSLA_ECHO_MIB.CiscoIpslaEchoMib.Cipslaudpechotmpltable.Cipslaudpechotmplentry>`
        
        

        """

        _prefix = 'CISCO-IPSLA-ECHO-MIB'
        _revision = '2007-08-16'

        def __init__(self):
            self.parent = None
            self.cipslaudpechotmplentry = YList()
            self.cipslaudpechotmplentry.parent = self
            self.cipslaudpechotmplentry.name = 'cipslaudpechotmplentry'


        class Cipslaudpechotmplentry(object):
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
            	**type**\:   :py:class:`CipslaudpechotmplhistfilterEnum <ydk.models.cisco_ios_xe.CISCO_IPSLA_ECHO_MIB.CiscoIpslaEchoMib.Cipslaudpechotmpltable.Cipslaudpechotmplentry.CipslaudpechotmplhistfilterEnum>`
            
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
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            .. attribute:: cipslaudpechotmplsrcaddr
            
            	A string which specifies the IP address of the source
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cipslaudpechotmplsrcaddrtype
            
            	An enumerated value which specifies the IP address type of the source. It must be used along with the cipslaUdpEchoTmplSrcAddr object
            	**type**\:   :py:class:`InetaddresstypeEnum <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetaddresstypeEnum>`
            
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
            	**type**\:   :py:class:`StoragetypeEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.StoragetypeEnum>`
            
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
                self.parent = None
                self.cipslaudpechotmplname = None
                self.cipslaudpechotmplcontrolenable = None
                self.cipslaudpechotmpldescription = None
                self.cipslaudpechotmpldistbuckets = None
                self.cipslaudpechotmpldistinterval = None
                self.cipslaudpechotmplhistbuckets = None
                self.cipslaudpechotmplhistfilter = None
                self.cipslaudpechotmplhistlives = None
                self.cipslaudpechotmplreqdatasize = None
                self.cipslaudpechotmplrowstatus = None
                self.cipslaudpechotmplsrcaddr = None
                self.cipslaudpechotmplsrcaddrtype = None
                self.cipslaudpechotmplsrcport = None
                self.cipslaudpechotmplstatshours = None
                self.cipslaudpechotmplstoragetype = None
                self.cipslaudpechotmplthreshold = None
                self.cipslaudpechotmpltimeout = None
                self.cipslaudpechotmpltos = None
                self.cipslaudpechotmplverifydata = None
                self.cipslaudpechotmplvrfname = None

            class CipslaudpechotmplhistfilterEnum(Enum):
                """
                CipslaudpechotmplhistfilterEnum

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

                none = 1

                all = 2

                overThreshold = 3

                failures = 4


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_IPSLA_ECHO_MIB as meta
                    return meta._meta_table['CiscoIpslaEchoMib.Cipslaudpechotmpltable.Cipslaudpechotmplentry.CipslaudpechotmplhistfilterEnum']


            @property
            def _common_path(self):
                if self.cipslaudpechotmplname is None:
                    raise YPYModelError('Key property cipslaudpechotmplname is None')

                return '/CISCO-IPSLA-ECHO-MIB:CISCO-IPSLA-ECHO-MIB/CISCO-IPSLA-ECHO-MIB:cipslaUdpEchoTmplTable/CISCO-IPSLA-ECHO-MIB:cipslaUdpEchoTmplEntry[CISCO-IPSLA-ECHO-MIB:cipslaUdpEchoTmplName = ' + str(self.cipslaudpechotmplname) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.cipslaudpechotmplname is not None:
                    return True

                if self.cipslaudpechotmplcontrolenable is not None:
                    return True

                if self.cipslaudpechotmpldescription is not None:
                    return True

                if self.cipslaudpechotmpldistbuckets is not None:
                    return True

                if self.cipslaudpechotmpldistinterval is not None:
                    return True

                if self.cipslaudpechotmplhistbuckets is not None:
                    return True

                if self.cipslaudpechotmplhistfilter is not None:
                    return True

                if self.cipslaudpechotmplhistlives is not None:
                    return True

                if self.cipslaudpechotmplreqdatasize is not None:
                    return True

                if self.cipslaudpechotmplrowstatus is not None:
                    return True

                if self.cipslaudpechotmplsrcaddr is not None:
                    return True

                if self.cipslaudpechotmplsrcaddrtype is not None:
                    return True

                if self.cipslaudpechotmplsrcport is not None:
                    return True

                if self.cipslaudpechotmplstatshours is not None:
                    return True

                if self.cipslaudpechotmplstoragetype is not None:
                    return True

                if self.cipslaudpechotmplthreshold is not None:
                    return True

                if self.cipslaudpechotmpltimeout is not None:
                    return True

                if self.cipslaudpechotmpltos is not None:
                    return True

                if self.cipslaudpechotmplverifydata is not None:
                    return True

                if self.cipslaudpechotmplvrfname is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_IPSLA_ECHO_MIB as meta
                return meta._meta_table['CiscoIpslaEchoMib.Cipslaudpechotmpltable.Cipslaudpechotmplentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IPSLA-ECHO-MIB:CISCO-IPSLA-ECHO-MIB/CISCO-IPSLA-ECHO-MIB:cipslaUdpEchoTmplTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cipslaudpechotmplentry is not None:
                for child_ref in self.cipslaudpechotmplentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_IPSLA_ECHO_MIB as meta
            return meta._meta_table['CiscoIpslaEchoMib.Cipslaudpechotmpltable']['meta_info']


    class Cipslatcpconntmpltable(object):
        """
        A table that contains TCP connect template specific definitions.
        
        .. attribute:: cipslatcpconntmplentry
        
        	A row entry representing an IPSLA TCP connect template
        	**type**\: list of    :py:class:`Cipslatcpconntmplentry <ydk.models.cisco_ios_xe.CISCO_IPSLA_ECHO_MIB.CiscoIpslaEchoMib.Cipslatcpconntmpltable.Cipslatcpconntmplentry>`
        
        

        """

        _prefix = 'CISCO-IPSLA-ECHO-MIB'
        _revision = '2007-08-16'

        def __init__(self):
            self.parent = None
            self.cipslatcpconntmplentry = YList()
            self.cipslatcpconntmplentry.parent = self
            self.cipslatcpconntmplentry.name = 'cipslatcpconntmplentry'


        class Cipslatcpconntmplentry(object):
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
            	**type**\:   :py:class:`CipslatcpconntmplhistfilterEnum <ydk.models.cisco_ios_xe.CISCO_IPSLA_ECHO_MIB.CiscoIpslaEchoMib.Cipslatcpconntmpltable.Cipslatcpconntmplentry.CipslatcpconntmplhistfilterEnum>`
            
            .. attribute:: cipslatcpconntmplhistlives
            
            	The maximum number of history lives to record.  A life is defined by the countdown (or transition) to zero  by the cipslaAutoGroupScheduleLife object.  A new life is created when the same conceptual control row is restarted via the transition of the  cipslaAutoGroupScheduleLife object and its subsequent  countdown.  The value of zero will shut off all data collection
            	**type**\:  int
            
            	**range:** 0..2
            
            .. attribute:: cipslatcpconntmplrowstatus
            
            	The status of the conceptual tcp connect control row. When the status is active, all the read\-create objects  in that row can be modified
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            .. attribute:: cipslatcpconntmplsrcaddr
            
            	A string which specifies the IP address of the source
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cipslatcpconntmplsrcaddrtype
            
            	An enumerated value which specifies the IP address type of the source. It must be used along with the cipslaTcpConnTmplSrcAddr object
            	**type**\:   :py:class:`InetaddresstypeEnum <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetaddresstypeEnum>`
            
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
            	**type**\:   :py:class:`StoragetypeEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.StoragetypeEnum>`
            
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
                self.parent = None
                self.cipslatcpconntmplname = None
                self.cipslatcpconntmplcontrolenable = None
                self.cipslatcpconntmpldescription = None
                self.cipslatcpconntmpldistbuckets = None
                self.cipslatcpconntmpldistinterval = None
                self.cipslatcpconntmplhistbuckets = None
                self.cipslatcpconntmplhistfilter = None
                self.cipslatcpconntmplhistlives = None
                self.cipslatcpconntmplrowstatus = None
                self.cipslatcpconntmplsrcaddr = None
                self.cipslatcpconntmplsrcaddrtype = None
                self.cipslatcpconntmplsrcport = None
                self.cipslatcpconntmplstatshours = None
                self.cipslatcpconntmplstoragetype = None
                self.cipslatcpconntmplthreshold = None
                self.cipslatcpconntmpltimeout = None
                self.cipslatcpconntmpltos = None
                self.cipslatcpconntmplverifydata = None

            class CipslatcpconntmplhistfilterEnum(Enum):
                """
                CipslatcpconntmplhistfilterEnum

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

                none = 1

                all = 2

                overThreshold = 3

                failures = 4


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_IPSLA_ECHO_MIB as meta
                    return meta._meta_table['CiscoIpslaEchoMib.Cipslatcpconntmpltable.Cipslatcpconntmplentry.CipslatcpconntmplhistfilterEnum']


            @property
            def _common_path(self):
                if self.cipslatcpconntmplname is None:
                    raise YPYModelError('Key property cipslatcpconntmplname is None')

                return '/CISCO-IPSLA-ECHO-MIB:CISCO-IPSLA-ECHO-MIB/CISCO-IPSLA-ECHO-MIB:cipslaTcpConnTmplTable/CISCO-IPSLA-ECHO-MIB:cipslaTcpConnTmplEntry[CISCO-IPSLA-ECHO-MIB:cipslaTcpConnTmplName = ' + str(self.cipslatcpconntmplname) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.cipslatcpconntmplname is not None:
                    return True

                if self.cipslatcpconntmplcontrolenable is not None:
                    return True

                if self.cipslatcpconntmpldescription is not None:
                    return True

                if self.cipslatcpconntmpldistbuckets is not None:
                    return True

                if self.cipslatcpconntmpldistinterval is not None:
                    return True

                if self.cipslatcpconntmplhistbuckets is not None:
                    return True

                if self.cipslatcpconntmplhistfilter is not None:
                    return True

                if self.cipslatcpconntmplhistlives is not None:
                    return True

                if self.cipslatcpconntmplrowstatus is not None:
                    return True

                if self.cipslatcpconntmplsrcaddr is not None:
                    return True

                if self.cipslatcpconntmplsrcaddrtype is not None:
                    return True

                if self.cipslatcpconntmplsrcport is not None:
                    return True

                if self.cipslatcpconntmplstatshours is not None:
                    return True

                if self.cipslatcpconntmplstoragetype is not None:
                    return True

                if self.cipslatcpconntmplthreshold is not None:
                    return True

                if self.cipslatcpconntmpltimeout is not None:
                    return True

                if self.cipslatcpconntmpltos is not None:
                    return True

                if self.cipslatcpconntmplverifydata is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_IPSLA_ECHO_MIB as meta
                return meta._meta_table['CiscoIpslaEchoMib.Cipslatcpconntmpltable.Cipslatcpconntmplentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IPSLA-ECHO-MIB:CISCO-IPSLA-ECHO-MIB/CISCO-IPSLA-ECHO-MIB:cipslaTcpConnTmplTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cipslatcpconntmplentry is not None:
                for child_ref in self.cipslatcpconntmplentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_IPSLA_ECHO_MIB as meta
            return meta._meta_table['CiscoIpslaEchoMib.Cipslatcpconntmpltable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-IPSLA-ECHO-MIB:CISCO-IPSLA-ECHO-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.cipslaicmpechotmpltable is not None and self.cipslaicmpechotmpltable._has_data():
            return True

        if self.cipslatcpconntmpltable is not None and self.cipslatcpconntmpltable._has_data():
            return True

        if self.cipslaudpechotmpltable is not None and self.cipslaudpechotmpltable._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_IPSLA_ECHO_MIB as meta
        return meta._meta_table['CiscoIpslaEchoMib']['meta_info']


