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
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CiscoIpslaEchoMib(Entity):
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
        super(CiscoIpslaEchoMib, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-IPSLA-ECHO-MIB"
        self.yang_parent_name = "CISCO-IPSLA-ECHO-MIB"

        self.cipslaicmpechotmpltable = CiscoIpslaEchoMib.Cipslaicmpechotmpltable()
        self.cipslaicmpechotmpltable.parent = self
        self._children_name_map["cipslaicmpechotmpltable"] = "cipslaIcmpEchoTmplTable"
        self._children_yang_names.add("cipslaIcmpEchoTmplTable")

        self.cipslatcpconntmpltable = CiscoIpslaEchoMib.Cipslatcpconntmpltable()
        self.cipslatcpconntmpltable.parent = self
        self._children_name_map["cipslatcpconntmpltable"] = "cipslaTcpConnTmplTable"
        self._children_yang_names.add("cipslaTcpConnTmplTable")

        self.cipslaudpechotmpltable = CiscoIpslaEchoMib.Cipslaudpechotmpltable()
        self.cipslaudpechotmpltable.parent = self
        self._children_name_map["cipslaudpechotmpltable"] = "cipslaUdpEchoTmplTable"
        self._children_yang_names.add("cipslaUdpEchoTmplTable")


    class Cipslaicmpechotmpltable(Entity):
        """
        A table that contains ICMP echo template definitions.
        
        .. attribute:: cipslaicmpechotmplentry
        
        	A row entry representing an IPSLA ICMP echo template
        	**type**\: list of    :py:class:`Cipslaicmpechotmplentry <ydk.models.cisco_ios_xe.CISCO_IPSLA_ECHO_MIB.CiscoIpslaEchoMib.Cipslaicmpechotmpltable.Cipslaicmpechotmplentry>`
        
        

        """

        _prefix = 'CISCO-IPSLA-ECHO-MIB'
        _revision = '2007-08-16'

        def __init__(self):
            super(CiscoIpslaEchoMib.Cipslaicmpechotmpltable, self).__init__()

            self.yang_name = "cipslaIcmpEchoTmplTable"
            self.yang_parent_name = "CISCO-IPSLA-ECHO-MIB"

            self.cipslaicmpechotmplentry = YList(self)

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
                        super(CiscoIpslaEchoMib.Cipslaicmpechotmpltable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIpslaEchoMib.Cipslaicmpechotmpltable, self).__setattr__(name, value)


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
            	**type**\:   :py:class:`Cipslaicmpechotmplhistfilter <ydk.models.cisco_ios_xe.CISCO_IPSLA_ECHO_MIB.CiscoIpslaEchoMib.Cipslaicmpechotmpltable.Cipslaicmpechotmplentry.Cipslaicmpechotmplhistfilter>`
            
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
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: cipslaicmpechotmplsrcaddr
            
            	A string which specifies the IP address of the source
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cipslaicmpechotmplsrcaddrtype
            
            	An enumerated value which specifies the IP address type of the source. It must be used along with the cipslaIcmpEchoTmplSrcAddr object
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
            .. attribute:: cipslaicmpechotmplstatshours
            
            	The maximum number of hours for which statistics are maintained. Specifically this is the number of hourly  groups to keep before rolling over.  The value of one is not advisable because the hourly group will close and immediately be deleted before the network management station will have the opportunity to retrieve the statistics.  The value of zero will shut off data collection
            	**type**\:  int
            
            	**range:** 0..25
            
            	**units**\: hours
            
            .. attribute:: cipslaicmpechotmplstoragetype
            
            	The storage type of this conceptual row
            	**type**\:   :py:class:`Storagetype <ydk.models.cisco_ios_xe.SNMPv2_TC.Storagetype>`
            
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
                super(CiscoIpslaEchoMib.Cipslaicmpechotmpltable.Cipslaicmpechotmplentry, self).__init__()

                self.yang_name = "cipslaIcmpEchoTmplEntry"
                self.yang_parent_name = "cipslaIcmpEchoTmplTable"

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

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cipslaicmpechotmplname",
                                "cipslaicmpechotmpldescription",
                                "cipslaicmpechotmpldistbuckets",
                                "cipslaicmpechotmpldistinterval",
                                "cipslaicmpechotmplhistbuckets",
                                "cipslaicmpechotmplhistfilter",
                                "cipslaicmpechotmplhistlives",
                                "cipslaicmpechotmplreqdatasize",
                                "cipslaicmpechotmplrowstatus",
                                "cipslaicmpechotmplsrcaddr",
                                "cipslaicmpechotmplsrcaddrtype",
                                "cipslaicmpechotmplstatshours",
                                "cipslaicmpechotmplstoragetype",
                                "cipslaicmpechotmplthreshold",
                                "cipslaicmpechotmpltimeout",
                                "cipslaicmpechotmpltos",
                                "cipslaicmpechotmplverifydata",
                                "cipslaicmpechotmplvrfname") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoIpslaEchoMib.Cipslaicmpechotmpltable.Cipslaicmpechotmplentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoIpslaEchoMib.Cipslaicmpechotmpltable.Cipslaicmpechotmplentry, self).__setattr__(name, value)

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


            def has_data(self):
                return (
                    self.cipslaicmpechotmplname.is_set or
                    self.cipslaicmpechotmpldescription.is_set or
                    self.cipslaicmpechotmpldistbuckets.is_set or
                    self.cipslaicmpechotmpldistinterval.is_set or
                    self.cipslaicmpechotmplhistbuckets.is_set or
                    self.cipslaicmpechotmplhistfilter.is_set or
                    self.cipslaicmpechotmplhistlives.is_set or
                    self.cipslaicmpechotmplreqdatasize.is_set or
                    self.cipslaicmpechotmplrowstatus.is_set or
                    self.cipslaicmpechotmplsrcaddr.is_set or
                    self.cipslaicmpechotmplsrcaddrtype.is_set or
                    self.cipslaicmpechotmplstatshours.is_set or
                    self.cipslaicmpechotmplstoragetype.is_set or
                    self.cipslaicmpechotmplthreshold.is_set or
                    self.cipslaicmpechotmpltimeout.is_set or
                    self.cipslaicmpechotmpltos.is_set or
                    self.cipslaicmpechotmplverifydata.is_set or
                    self.cipslaicmpechotmplvrfname.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cipslaicmpechotmplname.yfilter != YFilter.not_set or
                    self.cipslaicmpechotmpldescription.yfilter != YFilter.not_set or
                    self.cipslaicmpechotmpldistbuckets.yfilter != YFilter.not_set or
                    self.cipslaicmpechotmpldistinterval.yfilter != YFilter.not_set or
                    self.cipslaicmpechotmplhistbuckets.yfilter != YFilter.not_set or
                    self.cipslaicmpechotmplhistfilter.yfilter != YFilter.not_set or
                    self.cipslaicmpechotmplhistlives.yfilter != YFilter.not_set or
                    self.cipslaicmpechotmplreqdatasize.yfilter != YFilter.not_set or
                    self.cipslaicmpechotmplrowstatus.yfilter != YFilter.not_set or
                    self.cipslaicmpechotmplsrcaddr.yfilter != YFilter.not_set or
                    self.cipslaicmpechotmplsrcaddrtype.yfilter != YFilter.not_set or
                    self.cipslaicmpechotmplstatshours.yfilter != YFilter.not_set or
                    self.cipslaicmpechotmplstoragetype.yfilter != YFilter.not_set or
                    self.cipslaicmpechotmplthreshold.yfilter != YFilter.not_set or
                    self.cipslaicmpechotmpltimeout.yfilter != YFilter.not_set or
                    self.cipslaicmpechotmpltos.yfilter != YFilter.not_set or
                    self.cipslaicmpechotmplverifydata.yfilter != YFilter.not_set or
                    self.cipslaicmpechotmplvrfname.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cipslaIcmpEchoTmplEntry" + "[cipslaIcmpEchoTmplName='" + self.cipslaicmpechotmplname.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-IPSLA-ECHO-MIB:CISCO-IPSLA-ECHO-MIB/cipslaIcmpEchoTmplTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cipslaicmpechotmplname.is_set or self.cipslaicmpechotmplname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaicmpechotmplname.get_name_leafdata())
                if (self.cipslaicmpechotmpldescription.is_set or self.cipslaicmpechotmpldescription.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaicmpechotmpldescription.get_name_leafdata())
                if (self.cipslaicmpechotmpldistbuckets.is_set or self.cipslaicmpechotmpldistbuckets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaicmpechotmpldistbuckets.get_name_leafdata())
                if (self.cipslaicmpechotmpldistinterval.is_set or self.cipslaicmpechotmpldistinterval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaicmpechotmpldistinterval.get_name_leafdata())
                if (self.cipslaicmpechotmplhistbuckets.is_set or self.cipslaicmpechotmplhistbuckets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaicmpechotmplhistbuckets.get_name_leafdata())
                if (self.cipslaicmpechotmplhistfilter.is_set or self.cipslaicmpechotmplhistfilter.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaicmpechotmplhistfilter.get_name_leafdata())
                if (self.cipslaicmpechotmplhistlives.is_set or self.cipslaicmpechotmplhistlives.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaicmpechotmplhistlives.get_name_leafdata())
                if (self.cipslaicmpechotmplreqdatasize.is_set or self.cipslaicmpechotmplreqdatasize.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaicmpechotmplreqdatasize.get_name_leafdata())
                if (self.cipslaicmpechotmplrowstatus.is_set or self.cipslaicmpechotmplrowstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaicmpechotmplrowstatus.get_name_leafdata())
                if (self.cipslaicmpechotmplsrcaddr.is_set or self.cipslaicmpechotmplsrcaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaicmpechotmplsrcaddr.get_name_leafdata())
                if (self.cipslaicmpechotmplsrcaddrtype.is_set or self.cipslaicmpechotmplsrcaddrtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaicmpechotmplsrcaddrtype.get_name_leafdata())
                if (self.cipslaicmpechotmplstatshours.is_set or self.cipslaicmpechotmplstatshours.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaicmpechotmplstatshours.get_name_leafdata())
                if (self.cipslaicmpechotmplstoragetype.is_set or self.cipslaicmpechotmplstoragetype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaicmpechotmplstoragetype.get_name_leafdata())
                if (self.cipslaicmpechotmplthreshold.is_set or self.cipslaicmpechotmplthreshold.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaicmpechotmplthreshold.get_name_leafdata())
                if (self.cipslaicmpechotmpltimeout.is_set or self.cipslaicmpechotmpltimeout.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaicmpechotmpltimeout.get_name_leafdata())
                if (self.cipslaicmpechotmpltos.is_set or self.cipslaicmpechotmpltos.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaicmpechotmpltos.get_name_leafdata())
                if (self.cipslaicmpechotmplverifydata.is_set or self.cipslaicmpechotmplverifydata.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaicmpechotmplverifydata.get_name_leafdata())
                if (self.cipslaicmpechotmplvrfname.is_set or self.cipslaicmpechotmplvrfname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaicmpechotmplvrfname.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cipslaIcmpEchoTmplName" or name == "cipslaIcmpEchoTmplDescription" or name == "cipslaIcmpEchoTmplDistBuckets" or name == "cipslaIcmpEchoTmplDistInterval" or name == "cipslaIcmpEchoTmplHistBuckets" or name == "cipslaIcmpEchoTmplHistFilter" or name == "cipslaIcmpEchoTmplHistLives" or name == "cipslaIcmpEchoTmplReqDataSize" or name == "cipslaIcmpEchoTmplRowStatus" or name == "cipslaIcmpEchoTmplSrcAddr" or name == "cipslaIcmpEchoTmplSrcAddrType" or name == "cipslaIcmpEchoTmplStatsHours" or name == "cipslaIcmpEchoTmplStorageType" or name == "cipslaIcmpEchoTmplThreshold" or name == "cipslaIcmpEchoTmplTimeOut" or name == "cipslaIcmpEchoTmplTOS" or name == "cipslaIcmpEchoTmplVerifyData" or name == "cipslaIcmpEchoTmplVrfName"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cipslaIcmpEchoTmplName"):
                    self.cipslaicmpechotmplname = value
                    self.cipslaicmpechotmplname.value_namespace = name_space
                    self.cipslaicmpechotmplname.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaIcmpEchoTmplDescription"):
                    self.cipslaicmpechotmpldescription = value
                    self.cipslaicmpechotmpldescription.value_namespace = name_space
                    self.cipslaicmpechotmpldescription.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaIcmpEchoTmplDistBuckets"):
                    self.cipslaicmpechotmpldistbuckets = value
                    self.cipslaicmpechotmpldistbuckets.value_namespace = name_space
                    self.cipslaicmpechotmpldistbuckets.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaIcmpEchoTmplDistInterval"):
                    self.cipslaicmpechotmpldistinterval = value
                    self.cipslaicmpechotmpldistinterval.value_namespace = name_space
                    self.cipslaicmpechotmpldistinterval.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaIcmpEchoTmplHistBuckets"):
                    self.cipslaicmpechotmplhistbuckets = value
                    self.cipslaicmpechotmplhistbuckets.value_namespace = name_space
                    self.cipslaicmpechotmplhistbuckets.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaIcmpEchoTmplHistFilter"):
                    self.cipslaicmpechotmplhistfilter = value
                    self.cipslaicmpechotmplhistfilter.value_namespace = name_space
                    self.cipslaicmpechotmplhistfilter.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaIcmpEchoTmplHistLives"):
                    self.cipslaicmpechotmplhistlives = value
                    self.cipslaicmpechotmplhistlives.value_namespace = name_space
                    self.cipslaicmpechotmplhistlives.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaIcmpEchoTmplReqDataSize"):
                    self.cipslaicmpechotmplreqdatasize = value
                    self.cipslaicmpechotmplreqdatasize.value_namespace = name_space
                    self.cipslaicmpechotmplreqdatasize.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaIcmpEchoTmplRowStatus"):
                    self.cipslaicmpechotmplrowstatus = value
                    self.cipslaicmpechotmplrowstatus.value_namespace = name_space
                    self.cipslaicmpechotmplrowstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaIcmpEchoTmplSrcAddr"):
                    self.cipslaicmpechotmplsrcaddr = value
                    self.cipslaicmpechotmplsrcaddr.value_namespace = name_space
                    self.cipslaicmpechotmplsrcaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaIcmpEchoTmplSrcAddrType"):
                    self.cipslaicmpechotmplsrcaddrtype = value
                    self.cipslaicmpechotmplsrcaddrtype.value_namespace = name_space
                    self.cipslaicmpechotmplsrcaddrtype.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaIcmpEchoTmplStatsHours"):
                    self.cipslaicmpechotmplstatshours = value
                    self.cipslaicmpechotmplstatshours.value_namespace = name_space
                    self.cipslaicmpechotmplstatshours.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaIcmpEchoTmplStorageType"):
                    self.cipslaicmpechotmplstoragetype = value
                    self.cipslaicmpechotmplstoragetype.value_namespace = name_space
                    self.cipslaicmpechotmplstoragetype.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaIcmpEchoTmplThreshold"):
                    self.cipslaicmpechotmplthreshold = value
                    self.cipslaicmpechotmplthreshold.value_namespace = name_space
                    self.cipslaicmpechotmplthreshold.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaIcmpEchoTmplTimeOut"):
                    self.cipslaicmpechotmpltimeout = value
                    self.cipslaicmpechotmpltimeout.value_namespace = name_space
                    self.cipslaicmpechotmpltimeout.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaIcmpEchoTmplTOS"):
                    self.cipslaicmpechotmpltos = value
                    self.cipslaicmpechotmpltos.value_namespace = name_space
                    self.cipslaicmpechotmpltos.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaIcmpEchoTmplVerifyData"):
                    self.cipslaicmpechotmplverifydata = value
                    self.cipslaicmpechotmplverifydata.value_namespace = name_space
                    self.cipslaicmpechotmplverifydata.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaIcmpEchoTmplVrfName"):
                    self.cipslaicmpechotmplvrfname = value
                    self.cipslaicmpechotmplvrfname.value_namespace = name_space
                    self.cipslaicmpechotmplvrfname.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cipslaicmpechotmplentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cipslaicmpechotmplentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cipslaIcmpEchoTmplTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IPSLA-ECHO-MIB:CISCO-IPSLA-ECHO-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cipslaIcmpEchoTmplEntry"):
                for c in self.cipslaicmpechotmplentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoIpslaEchoMib.Cipslaicmpechotmpltable.Cipslaicmpechotmplentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cipslaicmpechotmplentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cipslaIcmpEchoTmplEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cipslaudpechotmpltable(Entity):
        """
        A table that contains UDP echo template specific definitions.
        
        .. attribute:: cipslaudpechotmplentry
        
        	A row entry representing an IPSLA UDP echo template
        	**type**\: list of    :py:class:`Cipslaudpechotmplentry <ydk.models.cisco_ios_xe.CISCO_IPSLA_ECHO_MIB.CiscoIpslaEchoMib.Cipslaudpechotmpltable.Cipslaudpechotmplentry>`
        
        

        """

        _prefix = 'CISCO-IPSLA-ECHO-MIB'
        _revision = '2007-08-16'

        def __init__(self):
            super(CiscoIpslaEchoMib.Cipslaudpechotmpltable, self).__init__()

            self.yang_name = "cipslaUdpEchoTmplTable"
            self.yang_parent_name = "CISCO-IPSLA-ECHO-MIB"

            self.cipslaudpechotmplentry = YList(self)

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
                        super(CiscoIpslaEchoMib.Cipslaudpechotmpltable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIpslaEchoMib.Cipslaudpechotmpltable, self).__setattr__(name, value)


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
            	**type**\:   :py:class:`Cipslaudpechotmplhistfilter <ydk.models.cisco_ios_xe.CISCO_IPSLA_ECHO_MIB.CiscoIpslaEchoMib.Cipslaudpechotmpltable.Cipslaudpechotmplentry.Cipslaudpechotmplhistfilter>`
            
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
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: cipslaudpechotmplsrcaddr
            
            	A string which specifies the IP address of the source
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cipslaudpechotmplsrcaddrtype
            
            	An enumerated value which specifies the IP address type of the source. It must be used along with the cipslaUdpEchoTmplSrcAddr object
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
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
            	**type**\:   :py:class:`Storagetype <ydk.models.cisco_ios_xe.SNMPv2_TC.Storagetype>`
            
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
                super(CiscoIpslaEchoMib.Cipslaudpechotmpltable.Cipslaudpechotmplentry, self).__init__()

                self.yang_name = "cipslaUdpEchoTmplEntry"
                self.yang_parent_name = "cipslaUdpEchoTmplTable"

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

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cipslaudpechotmplname",
                                "cipslaudpechotmplcontrolenable",
                                "cipslaudpechotmpldescription",
                                "cipslaudpechotmpldistbuckets",
                                "cipslaudpechotmpldistinterval",
                                "cipslaudpechotmplhistbuckets",
                                "cipslaudpechotmplhistfilter",
                                "cipslaudpechotmplhistlives",
                                "cipslaudpechotmplreqdatasize",
                                "cipslaudpechotmplrowstatus",
                                "cipslaudpechotmplsrcaddr",
                                "cipslaudpechotmplsrcaddrtype",
                                "cipslaudpechotmplsrcport",
                                "cipslaudpechotmplstatshours",
                                "cipslaudpechotmplstoragetype",
                                "cipslaudpechotmplthreshold",
                                "cipslaudpechotmpltimeout",
                                "cipslaudpechotmpltos",
                                "cipslaudpechotmplverifydata",
                                "cipslaudpechotmplvrfname") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoIpslaEchoMib.Cipslaudpechotmpltable.Cipslaudpechotmplentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoIpslaEchoMib.Cipslaudpechotmpltable.Cipslaudpechotmplentry, self).__setattr__(name, value)

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


            def has_data(self):
                return (
                    self.cipslaudpechotmplname.is_set or
                    self.cipslaudpechotmplcontrolenable.is_set or
                    self.cipslaudpechotmpldescription.is_set or
                    self.cipslaudpechotmpldistbuckets.is_set or
                    self.cipslaudpechotmpldistinterval.is_set or
                    self.cipslaudpechotmplhistbuckets.is_set or
                    self.cipslaudpechotmplhistfilter.is_set or
                    self.cipslaudpechotmplhistlives.is_set or
                    self.cipslaudpechotmplreqdatasize.is_set or
                    self.cipslaudpechotmplrowstatus.is_set or
                    self.cipslaudpechotmplsrcaddr.is_set or
                    self.cipslaudpechotmplsrcaddrtype.is_set or
                    self.cipslaudpechotmplsrcport.is_set or
                    self.cipslaudpechotmplstatshours.is_set or
                    self.cipslaudpechotmplstoragetype.is_set or
                    self.cipslaudpechotmplthreshold.is_set or
                    self.cipslaudpechotmpltimeout.is_set or
                    self.cipslaudpechotmpltos.is_set or
                    self.cipslaudpechotmplverifydata.is_set or
                    self.cipslaudpechotmplvrfname.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cipslaudpechotmplname.yfilter != YFilter.not_set or
                    self.cipslaudpechotmplcontrolenable.yfilter != YFilter.not_set or
                    self.cipslaudpechotmpldescription.yfilter != YFilter.not_set or
                    self.cipslaudpechotmpldistbuckets.yfilter != YFilter.not_set or
                    self.cipslaudpechotmpldistinterval.yfilter != YFilter.not_set or
                    self.cipslaudpechotmplhistbuckets.yfilter != YFilter.not_set or
                    self.cipslaudpechotmplhistfilter.yfilter != YFilter.not_set or
                    self.cipslaudpechotmplhistlives.yfilter != YFilter.not_set or
                    self.cipslaudpechotmplreqdatasize.yfilter != YFilter.not_set or
                    self.cipslaudpechotmplrowstatus.yfilter != YFilter.not_set or
                    self.cipslaudpechotmplsrcaddr.yfilter != YFilter.not_set or
                    self.cipslaudpechotmplsrcaddrtype.yfilter != YFilter.not_set or
                    self.cipslaudpechotmplsrcport.yfilter != YFilter.not_set or
                    self.cipslaudpechotmplstatshours.yfilter != YFilter.not_set or
                    self.cipslaudpechotmplstoragetype.yfilter != YFilter.not_set or
                    self.cipslaudpechotmplthreshold.yfilter != YFilter.not_set or
                    self.cipslaudpechotmpltimeout.yfilter != YFilter.not_set or
                    self.cipslaudpechotmpltos.yfilter != YFilter.not_set or
                    self.cipslaudpechotmplverifydata.yfilter != YFilter.not_set or
                    self.cipslaudpechotmplvrfname.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cipslaUdpEchoTmplEntry" + "[cipslaUdpEchoTmplName='" + self.cipslaudpechotmplname.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-IPSLA-ECHO-MIB:CISCO-IPSLA-ECHO-MIB/cipslaUdpEchoTmplTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cipslaudpechotmplname.is_set or self.cipslaudpechotmplname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaudpechotmplname.get_name_leafdata())
                if (self.cipslaudpechotmplcontrolenable.is_set or self.cipslaudpechotmplcontrolenable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaudpechotmplcontrolenable.get_name_leafdata())
                if (self.cipslaudpechotmpldescription.is_set or self.cipslaudpechotmpldescription.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaudpechotmpldescription.get_name_leafdata())
                if (self.cipslaudpechotmpldistbuckets.is_set or self.cipslaudpechotmpldistbuckets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaudpechotmpldistbuckets.get_name_leafdata())
                if (self.cipslaudpechotmpldistinterval.is_set or self.cipslaudpechotmpldistinterval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaudpechotmpldistinterval.get_name_leafdata())
                if (self.cipslaudpechotmplhistbuckets.is_set or self.cipslaudpechotmplhistbuckets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaudpechotmplhistbuckets.get_name_leafdata())
                if (self.cipslaudpechotmplhistfilter.is_set or self.cipslaudpechotmplhistfilter.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaudpechotmplhistfilter.get_name_leafdata())
                if (self.cipslaudpechotmplhistlives.is_set or self.cipslaudpechotmplhistlives.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaudpechotmplhistlives.get_name_leafdata())
                if (self.cipslaudpechotmplreqdatasize.is_set or self.cipslaudpechotmplreqdatasize.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaudpechotmplreqdatasize.get_name_leafdata())
                if (self.cipslaudpechotmplrowstatus.is_set or self.cipslaudpechotmplrowstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaudpechotmplrowstatus.get_name_leafdata())
                if (self.cipslaudpechotmplsrcaddr.is_set or self.cipslaudpechotmplsrcaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaudpechotmplsrcaddr.get_name_leafdata())
                if (self.cipslaudpechotmplsrcaddrtype.is_set or self.cipslaudpechotmplsrcaddrtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaudpechotmplsrcaddrtype.get_name_leafdata())
                if (self.cipslaudpechotmplsrcport.is_set or self.cipslaudpechotmplsrcport.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaudpechotmplsrcport.get_name_leafdata())
                if (self.cipslaudpechotmplstatshours.is_set or self.cipslaudpechotmplstatshours.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaudpechotmplstatshours.get_name_leafdata())
                if (self.cipslaudpechotmplstoragetype.is_set or self.cipslaudpechotmplstoragetype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaudpechotmplstoragetype.get_name_leafdata())
                if (self.cipslaudpechotmplthreshold.is_set or self.cipslaudpechotmplthreshold.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaudpechotmplthreshold.get_name_leafdata())
                if (self.cipslaudpechotmpltimeout.is_set or self.cipslaudpechotmpltimeout.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaudpechotmpltimeout.get_name_leafdata())
                if (self.cipslaudpechotmpltos.is_set or self.cipslaudpechotmpltos.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaudpechotmpltos.get_name_leafdata())
                if (self.cipslaudpechotmplverifydata.is_set or self.cipslaudpechotmplverifydata.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaudpechotmplverifydata.get_name_leafdata())
                if (self.cipslaudpechotmplvrfname.is_set or self.cipslaudpechotmplvrfname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaudpechotmplvrfname.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cipslaUdpEchoTmplName" or name == "cipslaUdpEchoTmplControlEnable" or name == "cipslaUdpEchoTmplDescription" or name == "cipslaUdpEchoTmplDistBuckets" or name == "cipslaUdpEchoTmplDistInterval" or name == "cipslaUdpEchoTmplHistBuckets" or name == "cipslaUdpEchoTmplHistFilter" or name == "cipslaUdpEchoTmplHistLives" or name == "cipslaUdpEchoTmplReqDataSize" or name == "cipslaUdpEchoTmplRowStatus" or name == "cipslaUdpEchoTmplSrcAddr" or name == "cipslaUdpEchoTmplSrcAddrType" or name == "cipslaUdpEchoTmplSrcPort" or name == "cipslaUdpEchoTmplStatsHours" or name == "cipslaUdpEchoTmplStorageType" or name == "cipslaUdpEchoTmplThreshold" or name == "cipslaUdpEchoTmplTimeOut" or name == "cipslaUdpEchoTmplTOS" or name == "cipslaUdpEchoTmplVerifyData" or name == "cipslaUdpEchoTmplVrfName"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cipslaUdpEchoTmplName"):
                    self.cipslaudpechotmplname = value
                    self.cipslaudpechotmplname.value_namespace = name_space
                    self.cipslaudpechotmplname.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaUdpEchoTmplControlEnable"):
                    self.cipslaudpechotmplcontrolenable = value
                    self.cipslaudpechotmplcontrolenable.value_namespace = name_space
                    self.cipslaudpechotmplcontrolenable.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaUdpEchoTmplDescription"):
                    self.cipslaudpechotmpldescription = value
                    self.cipslaudpechotmpldescription.value_namespace = name_space
                    self.cipslaudpechotmpldescription.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaUdpEchoTmplDistBuckets"):
                    self.cipslaudpechotmpldistbuckets = value
                    self.cipslaudpechotmpldistbuckets.value_namespace = name_space
                    self.cipslaudpechotmpldistbuckets.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaUdpEchoTmplDistInterval"):
                    self.cipslaudpechotmpldistinterval = value
                    self.cipslaudpechotmpldistinterval.value_namespace = name_space
                    self.cipslaudpechotmpldistinterval.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaUdpEchoTmplHistBuckets"):
                    self.cipslaudpechotmplhistbuckets = value
                    self.cipslaudpechotmplhistbuckets.value_namespace = name_space
                    self.cipslaudpechotmplhistbuckets.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaUdpEchoTmplHistFilter"):
                    self.cipslaudpechotmplhistfilter = value
                    self.cipslaudpechotmplhistfilter.value_namespace = name_space
                    self.cipslaudpechotmplhistfilter.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaUdpEchoTmplHistLives"):
                    self.cipslaudpechotmplhistlives = value
                    self.cipslaudpechotmplhistlives.value_namespace = name_space
                    self.cipslaudpechotmplhistlives.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaUdpEchoTmplReqDataSize"):
                    self.cipslaudpechotmplreqdatasize = value
                    self.cipslaudpechotmplreqdatasize.value_namespace = name_space
                    self.cipslaudpechotmplreqdatasize.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaUdpEchoTmplRowStatus"):
                    self.cipslaudpechotmplrowstatus = value
                    self.cipslaudpechotmplrowstatus.value_namespace = name_space
                    self.cipslaudpechotmplrowstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaUdpEchoTmplSrcAddr"):
                    self.cipslaudpechotmplsrcaddr = value
                    self.cipslaudpechotmplsrcaddr.value_namespace = name_space
                    self.cipslaudpechotmplsrcaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaUdpEchoTmplSrcAddrType"):
                    self.cipslaudpechotmplsrcaddrtype = value
                    self.cipslaudpechotmplsrcaddrtype.value_namespace = name_space
                    self.cipslaudpechotmplsrcaddrtype.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaUdpEchoTmplSrcPort"):
                    self.cipslaudpechotmplsrcport = value
                    self.cipslaudpechotmplsrcport.value_namespace = name_space
                    self.cipslaudpechotmplsrcport.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaUdpEchoTmplStatsHours"):
                    self.cipslaudpechotmplstatshours = value
                    self.cipslaudpechotmplstatshours.value_namespace = name_space
                    self.cipslaudpechotmplstatshours.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaUdpEchoTmplStorageType"):
                    self.cipslaudpechotmplstoragetype = value
                    self.cipslaudpechotmplstoragetype.value_namespace = name_space
                    self.cipslaudpechotmplstoragetype.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaUdpEchoTmplThreshold"):
                    self.cipslaudpechotmplthreshold = value
                    self.cipslaudpechotmplthreshold.value_namespace = name_space
                    self.cipslaudpechotmplthreshold.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaUdpEchoTmplTimeOut"):
                    self.cipslaudpechotmpltimeout = value
                    self.cipslaudpechotmpltimeout.value_namespace = name_space
                    self.cipslaudpechotmpltimeout.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaUdpEchoTmplTOS"):
                    self.cipslaudpechotmpltos = value
                    self.cipslaudpechotmpltos.value_namespace = name_space
                    self.cipslaudpechotmpltos.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaUdpEchoTmplVerifyData"):
                    self.cipslaudpechotmplverifydata = value
                    self.cipslaudpechotmplverifydata.value_namespace = name_space
                    self.cipslaudpechotmplverifydata.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaUdpEchoTmplVrfName"):
                    self.cipslaudpechotmplvrfname = value
                    self.cipslaudpechotmplvrfname.value_namespace = name_space
                    self.cipslaudpechotmplvrfname.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cipslaudpechotmplentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cipslaudpechotmplentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cipslaUdpEchoTmplTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IPSLA-ECHO-MIB:CISCO-IPSLA-ECHO-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cipslaUdpEchoTmplEntry"):
                for c in self.cipslaudpechotmplentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoIpslaEchoMib.Cipslaudpechotmpltable.Cipslaudpechotmplentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cipslaudpechotmplentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cipslaUdpEchoTmplEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cipslatcpconntmpltable(Entity):
        """
        A table that contains TCP connect template specific definitions.
        
        .. attribute:: cipslatcpconntmplentry
        
        	A row entry representing an IPSLA TCP connect template
        	**type**\: list of    :py:class:`Cipslatcpconntmplentry <ydk.models.cisco_ios_xe.CISCO_IPSLA_ECHO_MIB.CiscoIpslaEchoMib.Cipslatcpconntmpltable.Cipslatcpconntmplentry>`
        
        

        """

        _prefix = 'CISCO-IPSLA-ECHO-MIB'
        _revision = '2007-08-16'

        def __init__(self):
            super(CiscoIpslaEchoMib.Cipslatcpconntmpltable, self).__init__()

            self.yang_name = "cipslaTcpConnTmplTable"
            self.yang_parent_name = "CISCO-IPSLA-ECHO-MIB"

            self.cipslatcpconntmplentry = YList(self)

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
                        super(CiscoIpslaEchoMib.Cipslatcpconntmpltable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIpslaEchoMib.Cipslatcpconntmpltable, self).__setattr__(name, value)


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
            	**type**\:   :py:class:`Cipslatcpconntmplhistfilter <ydk.models.cisco_ios_xe.CISCO_IPSLA_ECHO_MIB.CiscoIpslaEchoMib.Cipslatcpconntmpltable.Cipslatcpconntmplentry.Cipslatcpconntmplhistfilter>`
            
            .. attribute:: cipslatcpconntmplhistlives
            
            	The maximum number of history lives to record.  A life is defined by the countdown (or transition) to zero  by the cipslaAutoGroupScheduleLife object.  A new life is created when the same conceptual control row is restarted via the transition of the  cipslaAutoGroupScheduleLife object and its subsequent  countdown.  The value of zero will shut off all data collection
            	**type**\:  int
            
            	**range:** 0..2
            
            .. attribute:: cipslatcpconntmplrowstatus
            
            	The status of the conceptual tcp connect control row. When the status is active, all the read\-create objects  in that row can be modified
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: cipslatcpconntmplsrcaddr
            
            	A string which specifies the IP address of the source
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cipslatcpconntmplsrcaddrtype
            
            	An enumerated value which specifies the IP address type of the source. It must be used along with the cipslaTcpConnTmplSrcAddr object
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
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
            	**type**\:   :py:class:`Storagetype <ydk.models.cisco_ios_xe.SNMPv2_TC.Storagetype>`
            
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
                super(CiscoIpslaEchoMib.Cipslatcpconntmpltable.Cipslatcpconntmplentry, self).__init__()

                self.yang_name = "cipslaTcpConnTmplEntry"
                self.yang_parent_name = "cipslaTcpConnTmplTable"

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

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cipslatcpconntmplname",
                                "cipslatcpconntmplcontrolenable",
                                "cipslatcpconntmpldescription",
                                "cipslatcpconntmpldistbuckets",
                                "cipslatcpconntmpldistinterval",
                                "cipslatcpconntmplhistbuckets",
                                "cipslatcpconntmplhistfilter",
                                "cipslatcpconntmplhistlives",
                                "cipslatcpconntmplrowstatus",
                                "cipslatcpconntmplsrcaddr",
                                "cipslatcpconntmplsrcaddrtype",
                                "cipslatcpconntmplsrcport",
                                "cipslatcpconntmplstatshours",
                                "cipslatcpconntmplstoragetype",
                                "cipslatcpconntmplthreshold",
                                "cipslatcpconntmpltimeout",
                                "cipslatcpconntmpltos",
                                "cipslatcpconntmplverifydata") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoIpslaEchoMib.Cipslatcpconntmpltable.Cipslatcpconntmplentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoIpslaEchoMib.Cipslatcpconntmpltable.Cipslatcpconntmplentry, self).__setattr__(name, value)

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


            def has_data(self):
                return (
                    self.cipslatcpconntmplname.is_set or
                    self.cipslatcpconntmplcontrolenable.is_set or
                    self.cipslatcpconntmpldescription.is_set or
                    self.cipslatcpconntmpldistbuckets.is_set or
                    self.cipslatcpconntmpldistinterval.is_set or
                    self.cipslatcpconntmplhistbuckets.is_set or
                    self.cipslatcpconntmplhistfilter.is_set or
                    self.cipslatcpconntmplhistlives.is_set or
                    self.cipslatcpconntmplrowstatus.is_set or
                    self.cipslatcpconntmplsrcaddr.is_set or
                    self.cipslatcpconntmplsrcaddrtype.is_set or
                    self.cipslatcpconntmplsrcport.is_set or
                    self.cipslatcpconntmplstatshours.is_set or
                    self.cipslatcpconntmplstoragetype.is_set or
                    self.cipslatcpconntmplthreshold.is_set or
                    self.cipslatcpconntmpltimeout.is_set or
                    self.cipslatcpconntmpltos.is_set or
                    self.cipslatcpconntmplverifydata.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cipslatcpconntmplname.yfilter != YFilter.not_set or
                    self.cipslatcpconntmplcontrolenable.yfilter != YFilter.not_set or
                    self.cipslatcpconntmpldescription.yfilter != YFilter.not_set or
                    self.cipslatcpconntmpldistbuckets.yfilter != YFilter.not_set or
                    self.cipslatcpconntmpldistinterval.yfilter != YFilter.not_set or
                    self.cipslatcpconntmplhistbuckets.yfilter != YFilter.not_set or
                    self.cipslatcpconntmplhistfilter.yfilter != YFilter.not_set or
                    self.cipslatcpconntmplhistlives.yfilter != YFilter.not_set or
                    self.cipslatcpconntmplrowstatus.yfilter != YFilter.not_set or
                    self.cipslatcpconntmplsrcaddr.yfilter != YFilter.not_set or
                    self.cipslatcpconntmplsrcaddrtype.yfilter != YFilter.not_set or
                    self.cipslatcpconntmplsrcport.yfilter != YFilter.not_set or
                    self.cipslatcpconntmplstatshours.yfilter != YFilter.not_set or
                    self.cipslatcpconntmplstoragetype.yfilter != YFilter.not_set or
                    self.cipslatcpconntmplthreshold.yfilter != YFilter.not_set or
                    self.cipslatcpconntmpltimeout.yfilter != YFilter.not_set or
                    self.cipslatcpconntmpltos.yfilter != YFilter.not_set or
                    self.cipslatcpconntmplverifydata.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cipslaTcpConnTmplEntry" + "[cipslaTcpConnTmplName='" + self.cipslatcpconntmplname.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-IPSLA-ECHO-MIB:CISCO-IPSLA-ECHO-MIB/cipslaTcpConnTmplTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cipslatcpconntmplname.is_set or self.cipslatcpconntmplname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslatcpconntmplname.get_name_leafdata())
                if (self.cipslatcpconntmplcontrolenable.is_set or self.cipslatcpconntmplcontrolenable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslatcpconntmplcontrolenable.get_name_leafdata())
                if (self.cipslatcpconntmpldescription.is_set or self.cipslatcpconntmpldescription.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslatcpconntmpldescription.get_name_leafdata())
                if (self.cipslatcpconntmpldistbuckets.is_set or self.cipslatcpconntmpldistbuckets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslatcpconntmpldistbuckets.get_name_leafdata())
                if (self.cipslatcpconntmpldistinterval.is_set or self.cipslatcpconntmpldistinterval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslatcpconntmpldistinterval.get_name_leafdata())
                if (self.cipslatcpconntmplhistbuckets.is_set or self.cipslatcpconntmplhistbuckets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslatcpconntmplhistbuckets.get_name_leafdata())
                if (self.cipslatcpconntmplhistfilter.is_set or self.cipslatcpconntmplhistfilter.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslatcpconntmplhistfilter.get_name_leafdata())
                if (self.cipslatcpconntmplhistlives.is_set or self.cipslatcpconntmplhistlives.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslatcpconntmplhistlives.get_name_leafdata())
                if (self.cipslatcpconntmplrowstatus.is_set or self.cipslatcpconntmplrowstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslatcpconntmplrowstatus.get_name_leafdata())
                if (self.cipslatcpconntmplsrcaddr.is_set or self.cipslatcpconntmplsrcaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslatcpconntmplsrcaddr.get_name_leafdata())
                if (self.cipslatcpconntmplsrcaddrtype.is_set or self.cipslatcpconntmplsrcaddrtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslatcpconntmplsrcaddrtype.get_name_leafdata())
                if (self.cipslatcpconntmplsrcport.is_set or self.cipslatcpconntmplsrcport.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslatcpconntmplsrcport.get_name_leafdata())
                if (self.cipslatcpconntmplstatshours.is_set or self.cipslatcpconntmplstatshours.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslatcpconntmplstatshours.get_name_leafdata())
                if (self.cipslatcpconntmplstoragetype.is_set or self.cipslatcpconntmplstoragetype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslatcpconntmplstoragetype.get_name_leafdata())
                if (self.cipslatcpconntmplthreshold.is_set or self.cipslatcpconntmplthreshold.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslatcpconntmplthreshold.get_name_leafdata())
                if (self.cipslatcpconntmpltimeout.is_set or self.cipslatcpconntmpltimeout.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslatcpconntmpltimeout.get_name_leafdata())
                if (self.cipslatcpconntmpltos.is_set or self.cipslatcpconntmpltos.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslatcpconntmpltos.get_name_leafdata())
                if (self.cipslatcpconntmplverifydata.is_set or self.cipslatcpconntmplverifydata.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslatcpconntmplverifydata.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cipslaTcpConnTmplName" or name == "cipslaTcpConnTmplControlEnable" or name == "cipslaTcpConnTmplDescription" or name == "cipslaTcpConnTmplDistBuckets" or name == "cipslaTcpConnTmplDistInterval" or name == "cipslaTcpConnTmplHistBuckets" or name == "cipslaTcpConnTmplHistFilter" or name == "cipslaTcpConnTmplHistLives" or name == "cipslaTcpConnTmplRowStatus" or name == "cipslaTcpConnTmplSrcAddr" or name == "cipslaTcpConnTmplSrcAddrType" or name == "cipslaTcpConnTmplSrcPort" or name == "cipslaTcpConnTmplStatsHours" or name == "cipslaTcpConnTmplStorageType" or name == "cipslaTcpConnTmplThreshold" or name == "cipslaTcpConnTmplTimeOut" or name == "cipslaTcpConnTmplTOS" or name == "cipslaTcpConnTmplVerifyData"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cipslaTcpConnTmplName"):
                    self.cipslatcpconntmplname = value
                    self.cipslatcpconntmplname.value_namespace = name_space
                    self.cipslatcpconntmplname.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaTcpConnTmplControlEnable"):
                    self.cipslatcpconntmplcontrolenable = value
                    self.cipslatcpconntmplcontrolenable.value_namespace = name_space
                    self.cipslatcpconntmplcontrolenable.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaTcpConnTmplDescription"):
                    self.cipslatcpconntmpldescription = value
                    self.cipslatcpconntmpldescription.value_namespace = name_space
                    self.cipslatcpconntmpldescription.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaTcpConnTmplDistBuckets"):
                    self.cipslatcpconntmpldistbuckets = value
                    self.cipslatcpconntmpldistbuckets.value_namespace = name_space
                    self.cipslatcpconntmpldistbuckets.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaTcpConnTmplDistInterval"):
                    self.cipslatcpconntmpldistinterval = value
                    self.cipslatcpconntmpldistinterval.value_namespace = name_space
                    self.cipslatcpconntmpldistinterval.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaTcpConnTmplHistBuckets"):
                    self.cipslatcpconntmplhistbuckets = value
                    self.cipslatcpconntmplhistbuckets.value_namespace = name_space
                    self.cipslatcpconntmplhistbuckets.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaTcpConnTmplHistFilter"):
                    self.cipslatcpconntmplhistfilter = value
                    self.cipslatcpconntmplhistfilter.value_namespace = name_space
                    self.cipslatcpconntmplhistfilter.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaTcpConnTmplHistLives"):
                    self.cipslatcpconntmplhistlives = value
                    self.cipslatcpconntmplhistlives.value_namespace = name_space
                    self.cipslatcpconntmplhistlives.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaTcpConnTmplRowStatus"):
                    self.cipslatcpconntmplrowstatus = value
                    self.cipslatcpconntmplrowstatus.value_namespace = name_space
                    self.cipslatcpconntmplrowstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaTcpConnTmplSrcAddr"):
                    self.cipslatcpconntmplsrcaddr = value
                    self.cipslatcpconntmplsrcaddr.value_namespace = name_space
                    self.cipslatcpconntmplsrcaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaTcpConnTmplSrcAddrType"):
                    self.cipslatcpconntmplsrcaddrtype = value
                    self.cipslatcpconntmplsrcaddrtype.value_namespace = name_space
                    self.cipslatcpconntmplsrcaddrtype.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaTcpConnTmplSrcPort"):
                    self.cipslatcpconntmplsrcport = value
                    self.cipslatcpconntmplsrcport.value_namespace = name_space
                    self.cipslatcpconntmplsrcport.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaTcpConnTmplStatsHours"):
                    self.cipslatcpconntmplstatshours = value
                    self.cipslatcpconntmplstatshours.value_namespace = name_space
                    self.cipslatcpconntmplstatshours.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaTcpConnTmplStorageType"):
                    self.cipslatcpconntmplstoragetype = value
                    self.cipslatcpconntmplstoragetype.value_namespace = name_space
                    self.cipslatcpconntmplstoragetype.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaTcpConnTmplThreshold"):
                    self.cipslatcpconntmplthreshold = value
                    self.cipslatcpconntmplthreshold.value_namespace = name_space
                    self.cipslatcpconntmplthreshold.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaTcpConnTmplTimeOut"):
                    self.cipslatcpconntmpltimeout = value
                    self.cipslatcpconntmpltimeout.value_namespace = name_space
                    self.cipslatcpconntmpltimeout.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaTcpConnTmplTOS"):
                    self.cipslatcpconntmpltos = value
                    self.cipslatcpconntmpltos.value_namespace = name_space
                    self.cipslatcpconntmpltos.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaTcpConnTmplVerifyData"):
                    self.cipslatcpconntmplverifydata = value
                    self.cipslatcpconntmplverifydata.value_namespace = name_space
                    self.cipslatcpconntmplverifydata.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cipslatcpconntmplentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cipslatcpconntmplentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cipslaTcpConnTmplTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IPSLA-ECHO-MIB:CISCO-IPSLA-ECHO-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cipslaTcpConnTmplEntry"):
                for c in self.cipslatcpconntmplentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoIpslaEchoMib.Cipslatcpconntmpltable.Cipslatcpconntmplentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cipslatcpconntmplentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cipslaTcpConnTmplEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.cipslaicmpechotmpltable is not None and self.cipslaicmpechotmpltable.has_data()) or
            (self.cipslatcpconntmpltable is not None and self.cipslatcpconntmpltable.has_data()) or
            (self.cipslaudpechotmpltable is not None and self.cipslaudpechotmpltable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.cipslaicmpechotmpltable is not None and self.cipslaicmpechotmpltable.has_operation()) or
            (self.cipslatcpconntmpltable is not None and self.cipslatcpconntmpltable.has_operation()) or
            (self.cipslaudpechotmpltable is not None and self.cipslaudpechotmpltable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "CISCO-IPSLA-ECHO-MIB:CISCO-IPSLA-ECHO-MIB" + path_buffer

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

        if (child_yang_name == "cipslaIcmpEchoTmplTable"):
            if (self.cipslaicmpechotmpltable is None):
                self.cipslaicmpechotmpltable = CiscoIpslaEchoMib.Cipslaicmpechotmpltable()
                self.cipslaicmpechotmpltable.parent = self
                self._children_name_map["cipslaicmpechotmpltable"] = "cipslaIcmpEchoTmplTable"
            return self.cipslaicmpechotmpltable

        if (child_yang_name == "cipslaTcpConnTmplTable"):
            if (self.cipslatcpconntmpltable is None):
                self.cipslatcpconntmpltable = CiscoIpslaEchoMib.Cipslatcpconntmpltable()
                self.cipslatcpconntmpltable.parent = self
                self._children_name_map["cipslatcpconntmpltable"] = "cipslaTcpConnTmplTable"
            return self.cipslatcpconntmpltable

        if (child_yang_name == "cipslaUdpEchoTmplTable"):
            if (self.cipslaudpechotmpltable is None):
                self.cipslaudpechotmpltable = CiscoIpslaEchoMib.Cipslaudpechotmpltable()
                self.cipslaudpechotmpltable.parent = self
                self._children_name_map["cipslaudpechotmpltable"] = "cipslaUdpEchoTmplTable"
            return self.cipslaudpechotmpltable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "cipslaIcmpEchoTmplTable" or name == "cipslaTcpConnTmplTable" or name == "cipslaUdpEchoTmplTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CiscoIpslaEchoMib()
        return self._top_entity

