""" CISCO_IPSLA_AUTOMEASURE_MIB 

This module defines the MIB for IP SLA Automation. IP SLA
Automation consists of the following\:
1. Use of grouping \- Group is an aggregation of operations 
   sharing the same type, for example UDP jitter type, with 
   common characteristics like frequency, interval etc.  
   Groups are formed by policies dictated either per customer, 
   or by service level or any other requirements.  So, for 
   example, there could be separate groups for customers named 
   Customer A, Customer B etc, or service levels named 
   Gold\-service, Silver\-service etc.  A single group will contain 
   one and only one IP SLA operation definition or reference a 
   single template.
2. Use of templates \- It has been observed that operations can be 
   configured quickly if the variants such as IP address and 
   ports can be configured separately and then combined with a 
   template  consisting of invariants.  This allows for re\-use of 
   the invariant template with various combinations of destination 
   addresses and ports, the benefits for which are multiplied when 
   considering groupings.
3. Auto operations \- With this feature the software will try to 
   automatically kickstart operations by making intelligent 
   assumptions.  For example, if no specific operation is referenced 
   by the group configuration then an ICMP jitter operation is 
   assumed by default.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class CiscoIpslaAutomeasureMib(object):
    """
    
    
    .. attribute:: cipslaautogroupdesttable
    
    	A table contains the list of destination IP addresses and ports associated to the auto measure group destination name
    	**type**\:   :py:class:`Cipslaautogroupdesttable <ydk.models.cisco_ios_xe.CISCO_IPSLA_AUTOMEASURE_MIB.CiscoIpslaAutomeasureMib.Cipslaautogroupdesttable>`
    
    .. attribute:: cipslaautogroupschedtable
    
    	A table of group scheduling definitions
    	**type**\:   :py:class:`Cipslaautogroupschedtable <ydk.models.cisco_ios_xe.CISCO_IPSLA_AUTOMEASURE_MIB.CiscoIpslaAutomeasureMib.Cipslaautogroupschedtable>`
    
    .. attribute:: cipslaautogrouptable
    
    	A table that contains IP SLA auto measure group definitions
    	**type**\:   :py:class:`Cipslaautogrouptable <ydk.models.cisco_ios_xe.CISCO_IPSLA_AUTOMEASURE_MIB.CiscoIpslaAutomeasureMib.Cipslaautogrouptable>`
    
    .. attribute:: cipslareacttable
    
    	A table that contains reaction configurations for templates. Each conceptual row in cipslaReactTable corresponds  to a reaction configured for one template.  Each template can have multiple reactions and hence there can be  multiple rows for a particular template. Different template types can have different reactions. The reaction type is  specified as cipslaReactVar based upon template type as some  reaction types are applicable just for specific template types
    	**type**\:   :py:class:`Cipslareacttable <ydk.models.cisco_ios_xe.CISCO_IPSLA_AUTOMEASURE_MIB.CiscoIpslaAutomeasureMib.Cipslareacttable>`
    
    

    """

    _prefix = 'CISCO-IPSLA-AUTOMEASURE-MIB'
    _revision = '2007-06-13'

    def __init__(self):
        self.cipslaautogroupdesttable = CiscoIpslaAutomeasureMib.Cipslaautogroupdesttable()
        self.cipslaautogroupdesttable.parent = self
        self.cipslaautogroupschedtable = CiscoIpslaAutomeasureMib.Cipslaautogroupschedtable()
        self.cipslaautogroupschedtable.parent = self
        self.cipslaautogrouptable = CiscoIpslaAutomeasureMib.Cipslaautogrouptable()
        self.cipslaautogrouptable.parent = self
        self.cipslareacttable = CiscoIpslaAutomeasureMib.Cipslareacttable()
        self.cipslareacttable.parent = self


    class Cipslaautogrouptable(object):
        """
        A table that contains IP SLA auto measure group definitions.
        
        .. attribute:: cipslaautogroupentry
        
        	An entry containing the configurations for a particular auto measure group
        	**type**\: list of    :py:class:`Cipslaautogroupentry <ydk.models.cisco_ios_xe.CISCO_IPSLA_AUTOMEASURE_MIB.CiscoIpslaAutomeasureMib.Cipslaautogrouptable.Cipslaautogroupentry>`
        
        

        """

        _prefix = 'CISCO-IPSLA-AUTOMEASURE-MIB'
        _revision = '2007-06-13'

        def __init__(self):
            self.parent = None
            self.cipslaautogroupentry = YList()
            self.cipslaautogroupentry.parent = self
            self.cipslaautogroupentry.name = 'cipslaautogroupentry'


        class Cipslaautogroupentry(object):
            """
            An entry containing the configurations for a particular
            auto measure group.
            
            .. attribute:: cipslaautogroupname  <key>
            
            	A group name which is used by a management application to identify the group
            	**type**\:  str
            
            	**length:** 1..64
            
            .. attribute:: cipslaautogroupaddestipageout
            
            	This object represents the ageout time for the discovered end point.  If the end point becomes inactive for the period  of ageout time, the end point will be removed from the  discovered end point list.  When the value of cipslaAutoGroupDestIPADEnable is  'false', the value of this object has no effect
            	**type**\:  int
            
            	**range:** 0..65536
            
            	**units**\: seconds
            
            .. attribute:: cipslaautogroupaddestport
            
            	This object represents the destination port number for auto discovery use
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: cipslaautogroupadmeasureretry
            
            	This object specifies number of measurement retries to be attempted for the discovered end point after the  connection to the end point is broken. If there is no  re\-registration message received, the end point will be  in inactive state.  When the value of cipslaAutoGroupDestIPADEnable is  'false', the value of this object has no effect
            	**type**\:  int
            
            	**range:** 1..65536
            
            .. attribute:: cipslaautogroupdescription
            
            	This field is used to provide description for the group
            	**type**\:  str
            
            	**length:** 0..128
            
            .. attribute:: cipslaautogroupdestinationname
            
            	This object refers to the cipslaAutoGroupDestName in cipslaAutoGroupDestTable. If the name entered  is not present in cipslaAutoGroupDestTable, then when  group is scheduled, no ip sla operations will be created
            	**type**\:  str
            
            	**length:** 0..64
            
            .. attribute:: cipslaautogroupdestipadenable
            
            	When this object is set to true, destination IP address is populated through auto\-discovery
            	**type**\:  bool
            
            .. attribute:: cipslaautogroupopertemplatename
            
            	A string which is used by a management application to identify the template which is associated with the group. Depends on cipslaAutoGroupOperType, this object refers to cipslaIcmpEchoTmplName in cipslaIcmpEchoTmplTable, or cipslaUdpEchoTmplName in cipslaUdpEchoTmplTable, or cipslaTcpConnTmplName in cipslaTcpConnTmplTable, or cipslaIcmpJitterTmplName in cipslaIcmpJitterTmplTable, or ciscoIpSlaUdpJitterTmplName in ciscoIpSlaUdpJitterTmplTable
            	**type**\:  str
            
            	**length:** 0..64
            
            .. attribute:: cipslaautogroupopertype
            
            	This object specifies the type of IP SLA operation. When operation type is not ICMP jitter, then  cipslaAutoGroupOperTemplateName must be specified
            	**type**\:   :py:class:`IpslaopertypeEnum <ydk.models.cisco_ios_xe.CISCO_IPSLA_TC_MIB.IpslaopertypeEnum>`
            
            .. attribute:: cipslaautogroupqosenable
            
            	When this object is set to true, QoS is enabled for this group and this group is linked to policy map. The  restriction is that after QoS is enabled, it can not be  disabled for this group
            	**type**\:  bool
            
            .. attribute:: cipslaautogrouprowstatus
            
            	The status of the conceptual group control row.  When the status is active, the other writable objects may be modified unless the scheduler with name  specified by cipslaAutoGroupSchedulerId is scheduled
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            .. attribute:: cipslaautogroupschedulerid
            
            	This object refers to the cipslaAutoGroupSchedId in cipslaAutoGroupSchedTable, and is used to schedule  this group
            	**type**\:  str
            
            	**length:** 0..64
            
            .. attribute:: cipslaautogroupstoragetype
            
            	The storage type of this conceptual row
            	**type**\:   :py:class:`StoragetypeEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.StoragetypeEnum>`
            
            

            """

            _prefix = 'CISCO-IPSLA-AUTOMEASURE-MIB'
            _revision = '2007-06-13'

            def __init__(self):
                self.parent = None
                self.cipslaautogroupname = None
                self.cipslaautogroupaddestipageout = None
                self.cipslaautogroupaddestport = None
                self.cipslaautogroupadmeasureretry = None
                self.cipslaautogroupdescription = None
                self.cipslaautogroupdestinationname = None
                self.cipslaautogroupdestipadenable = None
                self.cipslaautogroupopertemplatename = None
                self.cipslaautogroupopertype = None
                self.cipslaautogroupqosenable = None
                self.cipslaautogrouprowstatus = None
                self.cipslaautogroupschedulerid = None
                self.cipslaautogroupstoragetype = None

            @property
            def _common_path(self):
                if self.cipslaautogroupname is None:
                    raise YPYModelError('Key property cipslaautogroupname is None')

                return '/CISCO-IPSLA-AUTOMEASURE-MIB:CISCO-IPSLA-AUTOMEASURE-MIB/CISCO-IPSLA-AUTOMEASURE-MIB:cipslaAutoGroupTable/CISCO-IPSLA-AUTOMEASURE-MIB:cipslaAutoGroupEntry[CISCO-IPSLA-AUTOMEASURE-MIB:cipslaAutoGroupName = ' + str(self.cipslaautogroupname) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.cipslaautogroupname is not None:
                    return True

                if self.cipslaautogroupaddestipageout is not None:
                    return True

                if self.cipslaautogroupaddestport is not None:
                    return True

                if self.cipslaautogroupadmeasureretry is not None:
                    return True

                if self.cipslaautogroupdescription is not None:
                    return True

                if self.cipslaautogroupdestinationname is not None:
                    return True

                if self.cipslaautogroupdestipadenable is not None:
                    return True

                if self.cipslaautogroupopertemplatename is not None:
                    return True

                if self.cipslaautogroupopertype is not None:
                    return True

                if self.cipslaautogroupqosenable is not None:
                    return True

                if self.cipslaautogrouprowstatus is not None:
                    return True

                if self.cipslaautogroupschedulerid is not None:
                    return True

                if self.cipslaautogroupstoragetype is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_IPSLA_AUTOMEASURE_MIB as meta
                return meta._meta_table['CiscoIpslaAutomeasureMib.Cipslaautogrouptable.Cipslaautogroupentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IPSLA-AUTOMEASURE-MIB:CISCO-IPSLA-AUTOMEASURE-MIB/CISCO-IPSLA-AUTOMEASURE-MIB:cipslaAutoGroupTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cipslaautogroupentry is not None:
                for child_ref in self.cipslaautogroupentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_IPSLA_AUTOMEASURE_MIB as meta
            return meta._meta_table['CiscoIpslaAutomeasureMib.Cipslaautogrouptable']['meta_info']


    class Cipslaautogroupdesttable(object):
        """
        A table contains the list of destination IP
        addresses and ports associated to the auto measure
        group destination name.
        
        .. attribute:: cipslaautogroupdestentry
        
        	An entry containing the destination IP addresses and port configurations associated to auto measure group destination name
        	**type**\: list of    :py:class:`Cipslaautogroupdestentry <ydk.models.cisco_ios_xe.CISCO_IPSLA_AUTOMEASURE_MIB.CiscoIpslaAutomeasureMib.Cipslaautogroupdesttable.Cipslaautogroupdestentry>`
        
        

        """

        _prefix = 'CISCO-IPSLA-AUTOMEASURE-MIB'
        _revision = '2007-06-13'

        def __init__(self):
            self.parent = None
            self.cipslaautogroupdestentry = YList()
            self.cipslaautogroupdestentry.parent = self
            self.cipslaautogroupdestentry.name = 'cipslaautogroupdestentry'


        class Cipslaautogroupdestentry(object):
            """
            An entry containing the destination IP addresses
            and port configurations associated to auto measure
            group destination name.
            
            .. attribute:: cipslaautogroupdestname  <key>
            
            	This is the name for an auto measure group destination
            	**type**\:  str
            
            	**length:** 1..64
            
            .. attribute:: cipslaautogroupdestipaddrtype  <key>
            
            	The type of the internet address of a destination for an auto measure group
            	**type**\:   :py:class:`InetaddresstypeEnum <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetaddresstypeEnum>`
            
            .. attribute:: cipslaautogroupdestipaddr  <key>
            
            	The internet address of a destination for an auto measure group. The type of this address is determined by the value of cipslaAutoGroupDestIpAddrType
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cipslaautogroupdestport  <key>
            
            	This object represents the destination port number. For ICMP echo and ICMP jitter, the suggested value is  '0'
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: cipslaautogroupdestrowstatus
            
            	The status of the conceptual destination table control row. No other objects in this row need to be set before this object can become active.  During 'destroy', when cipslaAutoGroupDestIpAddr is specified  as '0.0.0.0' and cipslaAutoGroupDestPort is specified as '0',  then all the rows with same cipslaAutoGroupDestName will be  deleted
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            .. attribute:: cipslaautogroupdeststoragetype
            
            	The storage type of this conceptual row.  By default the entry will be saved into non\-volatile memory
            	**type**\:   :py:class:`StoragetypeEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.StoragetypeEnum>`
            
            

            """

            _prefix = 'CISCO-IPSLA-AUTOMEASURE-MIB'
            _revision = '2007-06-13'

            def __init__(self):
                self.parent = None
                self.cipslaautogroupdestname = None
                self.cipslaautogroupdestipaddrtype = None
                self.cipslaautogroupdestipaddr = None
                self.cipslaautogroupdestport = None
                self.cipslaautogroupdestrowstatus = None
                self.cipslaautogroupdeststoragetype = None

            @property
            def _common_path(self):
                if self.cipslaautogroupdestname is None:
                    raise YPYModelError('Key property cipslaautogroupdestname is None')
                if self.cipslaautogroupdestipaddrtype is None:
                    raise YPYModelError('Key property cipslaautogroupdestipaddrtype is None')
                if self.cipslaautogroupdestipaddr is None:
                    raise YPYModelError('Key property cipslaautogroupdestipaddr is None')
                if self.cipslaautogroupdestport is None:
                    raise YPYModelError('Key property cipslaautogroupdestport is None')

                return '/CISCO-IPSLA-AUTOMEASURE-MIB:CISCO-IPSLA-AUTOMEASURE-MIB/CISCO-IPSLA-AUTOMEASURE-MIB:cipslaAutoGroupDestTable/CISCO-IPSLA-AUTOMEASURE-MIB:cipslaAutoGroupDestEntry[CISCO-IPSLA-AUTOMEASURE-MIB:cipslaAutoGroupDestName = ' + str(self.cipslaautogroupdestname) + '][CISCO-IPSLA-AUTOMEASURE-MIB:cipslaAutoGroupDestIpAddrType = ' + str(self.cipslaautogroupdestipaddrtype) + '][CISCO-IPSLA-AUTOMEASURE-MIB:cipslaAutoGroupDestIpAddr = ' + str(self.cipslaautogroupdestipaddr) + '][CISCO-IPSLA-AUTOMEASURE-MIB:cipslaAutoGroupDestPort = ' + str(self.cipslaautogroupdestport) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.cipslaautogroupdestname is not None:
                    return True

                if self.cipslaautogroupdestipaddrtype is not None:
                    return True

                if self.cipslaautogroupdestipaddr is not None:
                    return True

                if self.cipslaautogroupdestport is not None:
                    return True

                if self.cipslaautogroupdestrowstatus is not None:
                    return True

                if self.cipslaautogroupdeststoragetype is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_IPSLA_AUTOMEASURE_MIB as meta
                return meta._meta_table['CiscoIpslaAutomeasureMib.Cipslaautogroupdesttable.Cipslaautogroupdestentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IPSLA-AUTOMEASURE-MIB:CISCO-IPSLA-AUTOMEASURE-MIB/CISCO-IPSLA-AUTOMEASURE-MIB:cipslaAutoGroupDestTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cipslaautogroupdestentry is not None:
                for child_ref in self.cipslaautogroupdestentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_IPSLA_AUTOMEASURE_MIB as meta
            return meta._meta_table['CiscoIpslaAutomeasureMib.Cipslaautogroupdesttable']['meta_info']


    class Cipslareacttable(object):
        """
        A table that contains reaction configurations for templates.
        Each conceptual row in cipslaReactTable corresponds 
        to a reaction configured for one template.
        
        Each template can have multiple reactions and hence there can be 
        multiple rows for a particular template. Different template
        types can have different reactions. The reaction type is 
        specified as cipslaReactVar based upon template type as some 
        reaction types are applicable just for specific template types.
        
        .. attribute:: cipslareactentry
        
        	A base list of objects that define a conceptual reaction configuration control row
        	**type**\: list of    :py:class:`Cipslareactentry <ydk.models.cisco_ios_xe.CISCO_IPSLA_AUTOMEASURE_MIB.CiscoIpslaAutomeasureMib.Cipslareacttable.Cipslareactentry>`
        
        

        """

        _prefix = 'CISCO-IPSLA-AUTOMEASURE-MIB'
        _revision = '2007-06-13'

        def __init__(self):
            self.parent = None
            self.cipslareactentry = YList()
            self.cipslareactentry.parent = self
            self.cipslareactentry.name = 'cipslareactentry'


        class Cipslareactentry(object):
            """
            A base list of objects that define a conceptual reaction
            configuration control row.
            
            .. attribute:: cipslaautogroupopertype  <key>
            
            	
            	**type**\:   :py:class:`IpslaopertypeEnum <ydk.models.cisco_ios_xe.CISCO_IPSLA_TC_MIB.IpslaopertypeEnum>`
            
            .. attribute:: cipslareactconfigindex  <key>
            
            	This object along with cipslaAutoGroupOperType and cipslaAutoGroupOperTemplateName identifies a particular reaction\-configuration for one IP SLA  template.  This number is persistent across reboots
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: cipslaautogroupopertemplatename  <key>
            
            	
            	**type**\:  str
            
            	**length:** 0..64
            
            	**refers to**\:  :py:class:`cipslaautogroupopertemplatename <ydk.models.cisco_ios_xe.CISCO_IPSLA_AUTOMEASURE_MIB.CiscoIpslaAutomeasureMib.Cipslaautogrouptable.Cipslaautogroupentry>`
            
            .. attribute:: cipslareactactiontype
            
            	Specifies what type, if any, of reaction to generate if one of the watched (reaction\-configuration ) conditions is satisfied\:  none(1)                \- no reaction is generated notificationOnly(2)    \- a notification is generated
            	**type**\:   :py:class:`CipslareactactiontypeEnum <ydk.models.cisco_ios_xe.CISCO_IPSLA_AUTOMEASURE_MIB.CiscoIpslaAutomeasureMib.Cipslareacttable.Cipslareactentry.CipslareactactiontypeEnum>`
            
            .. attribute:: cipslareactrowstatus
            
            	This objects indicates the status of the conceptual Reaction Control Row.   When this object moves to active state, the conceptual row  is monitored and notifications are generated when threshold  violation takes place.  In order for this object to become active cipslaReactVar must be defined. All other objects assume default values.  When the  status is active, the following objects in that row can be  modified.  cipslaReactThresholdType,  cipslaReactActionType,  cipslaReactThresholdRising,  cipslaReactThresholdFalling,  cipslaReactThresholdCountX,  cipslaReactThresholdCountY,  cipslaReactStorageType  This object can be set to 'destroy' from any value at any time. When this object is set to 'destroy' no reaction configuration would exist. The reaction configuration for the template is  removed
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            .. attribute:: cipslareactstoragetype
            
            	The storage type of this conceptual row.  By default the entry will be saved into non\-volatile memory
            	**type**\:   :py:class:`StoragetypeEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.StoragetypeEnum>`
            
            .. attribute:: cipslareactthresholdcountx
            
            	If cipslaReactThresholdType value is 'xOfy', this object defines the 'x' value.  If cipslaReactThresholdType value is 'consecutive' this object defines the number of consecutive occurrences that needs threshold violation before setting  cipslaReactOccurred as true.  If cipslaReactThresholdType value is 'average' this object defines the number of samples that needs be considered for calculating average.  This object has no meaning if cipslaReactThresholdType has value of 'never' and 'immediate'
            	**type**\:  int
            
            	**range:** 1..16
            
            .. attribute:: cipslareactthresholdcounty
            
            	This object defines the 'y' value of the xOfy condition if cipslaReactThresholdType is 'xOfy'. The default for the  'y' value is 5.  For other values of cipslaReactThresholdType, this object is not applicable
            	**type**\:  int
            
            	**range:** 1..16
            
            .. attribute:: cipslareactthresholdfalling
            
            	This object defines a lower threshold limit. If the value ( e.g rtt, jitterAvg, packetLossSD etc ) falls below this limit and if the condition specified in cipslaReactThresholdType is satisfied, a notification  is generated. This object value can not bigger than cipslaReactThresholdRising value.  Default value of cipslaReactThresholdFalling    'rtt' is 3000    'jitterAvg' is 100.    'jitterSDAvg' is 100.    'jitterDSAvg' 100.    'packetLossSD' is 10000.    'packetLossDS' is 10000.    'mos' is 500.    'icpif' is 93.    'packetMIA' is 10000.    'packetLateArrival' is 10000.    'packetOutOfSequence' is 10000.    'maxOfPositiveSD' is 10000.    'maxOfNegativeSD' is 10000.    'maxOfPositiveDS' is 10000.    'maxOfNegativeDS' is 10000.    'successivePacketLoss' is 1000.    'maxOfLatencyDS' is 3000.    'maxOfLatencySD' is 3000.    'latencyDSAvg' is 3000.    'latencySDAvg' is 3000.    'packetLoss' is 10000.  This object is not applicable if the cipslaReactVar is 'timeout', 'connectionLoss' or 'verifyError'. For 'timeout', 'connectionLoss' and 'verifyError', default value of cipslaReactThresholdFalling will be 0
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipslareactthresholdrising
            
            	This object defines the higher threshold limit. If the value ( e.g rtt, jitterAvg, packetLossSD etc ) rises above this limit and if the condition specified in cipslaReactThresholdType is satisfied, a notification is  generated.  Default value of cipslaReactThresholdRising for    'rtt' is 5000    'jitterAvg' is 100.    'jitterSDAvg' is 100.    'jitterDSAvg' 100.    'packetLossSD' is 10000.    'packetLossDS' is 10000.    'mos' is 500.    'icpif' is 93.    'packetMIA' is 10000.    'packetLateArrival' is 10000.    'packetOutOfSequence' is 10000.    'maxOfPositiveSD' is 10000.    'maxOfNegativeSD' is 10000.    'maxOfPositiveDS' is 10000.    'maxOfNegativeDS' is 10000.    'successivePacketLoss' is 1000.    'maxOfLatencyDS' is 5000.    'maxOfLatencySD' is 5000.    'latencyDSAvg' is 5000.    'latencySDAvg' is 5000.    'packetLoss' is 10000.  This object is not applicable if the cipslaReactVar is 'timeout', 'connectionLoss' or 'verifyError'. For 'timeout', 'connectionLoss' and 'verifyError' default value of  cipslaReactThresholdRising will be 0
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipslareactthresholdtype
            
            	This object specifies the conditions under which a notification ( trap ) is sent. The rttMonReactOccurred object defined in rttMonReactTable in CISCO\-RTTMON\-MIB will change accordingly\:  never(1)       \- rttMonReactOccurred is never set  immediate(2)   \- rttMonReactOccurred is set to 'true' when the                  value of parameter for which reaction is                  configured ( e.g rtt, jitterAvg, packetLossSD,                  mos etc ) violates the threshold.                  Conversely, rttMonReactOccurred is set to 'false'                  when the parameter ( e.g rtt, jitterAvg,                  packetLossSD, mos etc ) is below the threshold                  limits.  consecutive(3) \- rttMonReactOccurred is set to true when the value                  of parameter for which reaction is configured                  ( e.g rtt, jitterAvg, packetLossSD, mos etc )                  violates the threshold for configured consecutive                  times.                  Conversely, rttMonReactOccurred is set to false                  when the value of parameter ( e.g rtt, jitterAvg                  packetLossSD, mos etc ) is below the threshold                  limits for the same number of consecutive                  operations.  xOfy(4)        \- rttMonReactOccurred is set to true when x                  ( as specified by cipslaReactThresholdCountX )                  out of the last y ( as specified by                  cipslaReacthresholdCountY ) times the value of                  parameter for which the reaction is configured                  ( e.g rtt, jitterAvg, packetLossSD, mos etc )                  violates the threshold.                  Conversely, it is set to false when x, out of the                  last y times the value of parameter                  ( e.g rtt, jitterAvg, packetLossSD, mos ) is                  below the threshold limits.                  NOTE\: If x > y, this will never                       generate a reaction.  average(5)    \- rttMonReactOccurred is set to true when the                 average ( cipslaReactThresholdCountX times )                 value of parameter for which reaction is                  configured ( e.g rtt, jitterAvg, packetLossSD,                 mos etc ) violates the threshold condition.                 Conversely, it is set to false when the                 average value of parameter ( e.g rtt, jitterAvg,                 packetLossSD, mos etc ) is below the threshold                 limits.  If this value is changed by a management station, rttMonReactOccurred is set to false, but no reaction is generated if the prior value of rttMonReactOccurred was true
            	**type**\:   :py:class:`CipslareactthresholdtypeEnum <ydk.models.cisco_ios_xe.CISCO_IPSLA_AUTOMEASURE_MIB.CiscoIpslaAutomeasureMib.Cipslareacttable.Cipslareactentry.CipslareactthresholdtypeEnum>`
            
            .. attribute:: cipslareactvar
            
            	This object specifies the type of reaction configured for an IP SLA template. Default value is 'rtt' for ICMP echo, UDP echo and TCP connect. Default value is 'jitterAvg' for UDP jitter and  ICMP jitter.  The reaction types 'rtt', 'timeout', 'connectionLoss' and 'verifyError' can be configured for all template types.  The reaction types 'jitterSDAvg', 'jitterDSAvg', 'jitterAvg',  'packetLateArrival', 'packetOutOfSequence',  'maxOfPositiveSD', 'maxOfNegativeSD', 'maxOfPositiveDS' 'maxOfNegativeDS', 'mos' and 'icpif' can be configured for  UDP jitter and ICMP jitter types only.  The reaction types 'packetLossDS', 'packetLossSD' and  'packetMIA' can be configured for UDP jitter type only.  The reaction types 'successivePacketLoss', 'maxOfLatencyDS',  'maxOfLatencySD', 'latencyDSAvg', 'latencySDAvg' and  'packetLoss' can be configured for ICMP jitter type only
            	**type**\:   :py:class:`IpslareactvarEnum <ydk.models.cisco_ios_xe.CISCO_IPSLA_TC_MIB.IpslareactvarEnum>`
            
            

            """

            _prefix = 'CISCO-IPSLA-AUTOMEASURE-MIB'
            _revision = '2007-06-13'

            def __init__(self):
                self.parent = None
                self.cipslaautogroupopertype = None
                self.cipslareactconfigindex = None
                self.cipslaautogroupopertemplatename = None
                self.cipslareactactiontype = None
                self.cipslareactrowstatus = None
                self.cipslareactstoragetype = None
                self.cipslareactthresholdcountx = None
                self.cipslareactthresholdcounty = None
                self.cipslareactthresholdfalling = None
                self.cipslareactthresholdrising = None
                self.cipslareactthresholdtype = None
                self.cipslareactvar = None

            class CipslareactactiontypeEnum(Enum):
                """
                CipslareactactiontypeEnum

                Specifies what type, if any, of reaction to

                generate if one of the watched

                (reaction\-configuration ) conditions is satisfied\:

                none(1)                \- no reaction is generated

                notificationOnly(2)    \- a notification is generated

                .. data:: none = 1

                .. data:: notificationOnly = 2

                """

                none = 1

                notificationOnly = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_IPSLA_AUTOMEASURE_MIB as meta
                    return meta._meta_table['CiscoIpslaAutomeasureMib.Cipslareacttable.Cipslareactentry.CipslareactactiontypeEnum']


            class CipslareactthresholdtypeEnum(Enum):
                """
                CipslareactthresholdtypeEnum

                This object specifies the conditions under which

                a notification ( trap ) is sent. The rttMonReactOccurred

                object defined in rttMonReactTable in CISCO\-RTTMON\-MIB will

                change accordingly\:

                never(1)       \- rttMonReactOccurred is never set

                immediate(2)   \- rttMonReactOccurred is set to 'true' when the

                                 value of parameter for which reaction is

                                 configured ( e.g rtt, jitterAvg, packetLossSD,

                                 mos etc ) violates the threshold.

                                 Conversely, rttMonReactOccurred is set to 'false'

                                 when the parameter ( e.g rtt, jitterAvg,

                                 packetLossSD, mos etc ) is below the threshold

                                 limits.

                consecutive(3) \- rttMonReactOccurred is set to true when the value

                                 of parameter for which reaction is configured

                                 ( e.g rtt, jitterAvg, packetLossSD, mos etc )

                                 violates the threshold for configured consecutive

                                 times.

                                 Conversely, rttMonReactOccurred is set to false

                                 when the value of parameter ( e.g rtt, jitterAvg

                                 packetLossSD, mos etc ) is below the threshold

                                 limits for the same number of consecutive

                                 operations.

                xOfy(4)        \- rttMonReactOccurred is set to true when x

                                 ( as specified by cipslaReactThresholdCountX )

                                 out of the last y ( as specified by

                                 cipslaReacthresholdCountY ) times the value of

                                 parameter for which the reaction is configured

                                 ( e.g rtt, jitterAvg, packetLossSD, mos etc )

                                 violates the threshold.

                                 Conversely, it is set to false when x, out of the

                                 last y times the value of parameter

                                 ( e.g rtt, jitterAvg, packetLossSD, mos ) is

                                 below the threshold limits.

                                 NOTE\: If x > y, this will never

                                      generate a reaction.

                average(5)    \- rttMonReactOccurred is set to true when the

                                average ( cipslaReactThresholdCountX times )

                                value of parameter for which reaction is 

                                configured ( e.g rtt, jitterAvg, packetLossSD,

                                mos etc ) violates the threshold condition.

                                Conversely, it is set to false when the

                                average value of parameter ( e.g rtt, jitterAvg,

                                packetLossSD, mos etc ) is below the threshold

                                limits.

                If this value is changed by a management station,

                rttMonReactOccurred is set to false, but

                no reaction is generated if the prior value of

                rttMonReactOccurred was true.

                .. data:: never = 1

                .. data:: immediate = 2

                .. data:: consecutive = 3

                .. data:: xOfy = 4

                .. data:: average = 5

                """

                never = 1

                immediate = 2

                consecutive = 3

                xOfy = 4

                average = 5


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_IPSLA_AUTOMEASURE_MIB as meta
                    return meta._meta_table['CiscoIpslaAutomeasureMib.Cipslareacttable.Cipslareactentry.CipslareactthresholdtypeEnum']


            @property
            def _common_path(self):
                if self.cipslaautogroupopertype is None:
                    raise YPYModelError('Key property cipslaautogroupopertype is None')
                if self.cipslareactconfigindex is None:
                    raise YPYModelError('Key property cipslareactconfigindex is None')
                if self.cipslaautogroupopertemplatename is None:
                    raise YPYModelError('Key property cipslaautogroupopertemplatename is None')

                return '/CISCO-IPSLA-AUTOMEASURE-MIB:CISCO-IPSLA-AUTOMEASURE-MIB/CISCO-IPSLA-AUTOMEASURE-MIB:cipslaReactTable/CISCO-IPSLA-AUTOMEASURE-MIB:cipslaReactEntry[CISCO-IPSLA-AUTOMEASURE-MIB:cipslaAutoGroupOperType = ' + str(self.cipslaautogroupopertype) + '][CISCO-IPSLA-AUTOMEASURE-MIB:cipslaReactConfigIndex = ' + str(self.cipslareactconfigindex) + '][CISCO-IPSLA-AUTOMEASURE-MIB:cipslaAutoGroupOperTemplateName = ' + str(self.cipslaautogroupopertemplatename) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.cipslaautogroupopertype is not None:
                    return True

                if self.cipslareactconfigindex is not None:
                    return True

                if self.cipslaautogroupopertemplatename is not None:
                    return True

                if self.cipslareactactiontype is not None:
                    return True

                if self.cipslareactrowstatus is not None:
                    return True

                if self.cipslareactstoragetype is not None:
                    return True

                if self.cipslareactthresholdcountx is not None:
                    return True

                if self.cipslareactthresholdcounty is not None:
                    return True

                if self.cipslareactthresholdfalling is not None:
                    return True

                if self.cipslareactthresholdrising is not None:
                    return True

                if self.cipslareactthresholdtype is not None:
                    return True

                if self.cipslareactvar is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_IPSLA_AUTOMEASURE_MIB as meta
                return meta._meta_table['CiscoIpslaAutomeasureMib.Cipslareacttable.Cipslareactentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IPSLA-AUTOMEASURE-MIB:CISCO-IPSLA-AUTOMEASURE-MIB/CISCO-IPSLA-AUTOMEASURE-MIB:cipslaReactTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cipslareactentry is not None:
                for child_ref in self.cipslareactentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_IPSLA_AUTOMEASURE_MIB as meta
            return meta._meta_table['CiscoIpslaAutomeasureMib.Cipslareacttable']['meta_info']


    class Cipslaautogroupschedtable(object):
        """
        A table of group scheduling definitions.
        
        .. attribute:: cipslaautogroupschedentry
        
        	A list of objects that define specific configuration for group scheduling
        	**type**\: list of    :py:class:`Cipslaautogroupschedentry <ydk.models.cisco_ios_xe.CISCO_IPSLA_AUTOMEASURE_MIB.CiscoIpslaAutomeasureMib.Cipslaautogroupschedtable.Cipslaautogroupschedentry>`
        
        

        """

        _prefix = 'CISCO-IPSLA-AUTOMEASURE-MIB'
        _revision = '2007-06-13'

        def __init__(self):
            self.parent = None
            self.cipslaautogroupschedentry = YList()
            self.cipslaautogroupschedentry.parent = self
            self.cipslaautogroupschedentry.name = 'cipslaautogroupschedentry'


        class Cipslaautogroupschedentry(object):
            """
            A list of objects that define specific configuration for
            group scheduling.
            
            .. attribute:: cipslaautogroupschedid  <key>
            
            	This string uniquely identifies a row in the cipslaAutoGroupSchedTable
            	**type**\:  str
            
            	**length:** 1..64
            
            .. attribute:: cipslaautogroupschedageout
            
            	This object specifies the ageout value of the operations that are getting group scheduled. This value will be placed into rttMonSchedAdminConceptRowAgeout object for each of the operations in the group when this conceptual control row becomes  'active'.  When this value is set to zero, the operations will never ageout
            	**type**\:  int
            
            	**range:** 0..2073600
            
            	**units**\: seconds
            
            .. attribute:: cipslaautogroupschedinterval
            
            	Specifies the duration between initiating each RTT operation for one IP SLA operation generated via the auto  measure group.  The value of this object is only effective when both cipslaAutoGroupSchedMaxInterval and  cipslaAutoGroupSchedMinInterval have zero values
            	**type**\:  int
            
            	**range:** 1..604800
            
            	**units**\: seconds
            
            .. attribute:: cipslaautogroupschedlife
            
            	This object specifies the life of all the operations that are getting group scheduled. This value will be placed into cipslaAutoGroupSchedRttLife object when this conceptual control row becomes 'active'.  The value 2147483647 has a special meaning. When this object is set to 2147483647, the rttMonCtrlOperRttLife object for all the operations will not decrement, and thus the life time of the  operation will never end
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**units**\: seconds
            
            .. attribute:: cipslaautogroupschedmaxinterval
            
            	Specifies the max duration between initiating each RTT operation for one IP SLA operation in the group
            	**type**\:  int
            
            	**range:** 0..604800
            
            	**units**\: seconds
            
            .. attribute:: cipslaautogroupschedmininterval
            
            	Specifies the min duration between initiating each RTT operation for one IP SLA operation in the group.  The value of this object should be lower than the value of cipslaAutoGroupSchedMaxInterval
            	**type**\:  int
            
            	**range:** 0..604800
            
            	**units**\: seconds
            
            .. attribute:: cipslaautogroupschedperiod
            
            	Specifies the time duration between initiating two IP SLA operations generated via the auto measure group
            	**type**\:  int
            
            	**range:** 100..99000
            
            	**units**\: seconds
            
            .. attribute:: cipslaautogroupschedrowstatus
            
            	The status of the conceptual group schedule control row.  When the status is active and the value of  cipslaAutoGroupSchedStartTime is '1', the other writable  objects may be modified.  This object can be set to 'destroy' from any value at any time. When this object is set to 'destroy' it will stop all the  operations which had been group scheduled by it earlier,  before destroying the group schedule control row
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            .. attribute:: cipslaautogroupschedstarttime
            
            	This is the time in seconds after which the operations of the associated groups  will take transition to active state. When set to the value other than '1' (pending), then all  objects in this row cannot be modified
            	**type**\:  int
            
            	**range:** 0..604800
            
            	**units**\: seconds
            
            .. attribute:: cipslaautogroupschedstoragetype
            
            	The storage type of this conceptual row.  By default the entry will be saved into non\-volatile memory
            	**type**\:   :py:class:`StoragetypeEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.StoragetypeEnum>`
            
            

            """

            _prefix = 'CISCO-IPSLA-AUTOMEASURE-MIB'
            _revision = '2007-06-13'

            def __init__(self):
                self.parent = None
                self.cipslaautogroupschedid = None
                self.cipslaautogroupschedageout = None
                self.cipslaautogroupschedinterval = None
                self.cipslaautogroupschedlife = None
                self.cipslaautogroupschedmaxinterval = None
                self.cipslaautogroupschedmininterval = None
                self.cipslaautogroupschedperiod = None
                self.cipslaautogroupschedrowstatus = None
                self.cipslaautogroupschedstarttime = None
                self.cipslaautogroupschedstoragetype = None

            @property
            def _common_path(self):
                if self.cipslaautogroupschedid is None:
                    raise YPYModelError('Key property cipslaautogroupschedid is None')

                return '/CISCO-IPSLA-AUTOMEASURE-MIB:CISCO-IPSLA-AUTOMEASURE-MIB/CISCO-IPSLA-AUTOMEASURE-MIB:cipslaAutoGroupSchedTable/CISCO-IPSLA-AUTOMEASURE-MIB:cipslaAutoGroupSchedEntry[CISCO-IPSLA-AUTOMEASURE-MIB:cipslaAutoGroupSchedId = ' + str(self.cipslaautogroupschedid) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.cipslaautogroupschedid is not None:
                    return True

                if self.cipslaautogroupschedageout is not None:
                    return True

                if self.cipslaautogroupschedinterval is not None:
                    return True

                if self.cipslaautogroupschedlife is not None:
                    return True

                if self.cipslaautogroupschedmaxinterval is not None:
                    return True

                if self.cipslaautogroupschedmininterval is not None:
                    return True

                if self.cipslaautogroupschedperiod is not None:
                    return True

                if self.cipslaautogroupschedrowstatus is not None:
                    return True

                if self.cipslaautogroupschedstarttime is not None:
                    return True

                if self.cipslaautogroupschedstoragetype is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_IPSLA_AUTOMEASURE_MIB as meta
                return meta._meta_table['CiscoIpslaAutomeasureMib.Cipslaautogroupschedtable.Cipslaautogroupschedentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IPSLA-AUTOMEASURE-MIB:CISCO-IPSLA-AUTOMEASURE-MIB/CISCO-IPSLA-AUTOMEASURE-MIB:cipslaAutoGroupSchedTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cipslaautogroupschedentry is not None:
                for child_ref in self.cipslaautogroupschedentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_IPSLA_AUTOMEASURE_MIB as meta
            return meta._meta_table['CiscoIpslaAutomeasureMib.Cipslaautogroupschedtable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-IPSLA-AUTOMEASURE-MIB:CISCO-IPSLA-AUTOMEASURE-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.cipslaautogroupdesttable is not None and self.cipslaautogroupdesttable._has_data():
            return True

        if self.cipslaautogroupschedtable is not None and self.cipslaautogroupschedtable._has_data():
            return True

        if self.cipslaautogrouptable is not None and self.cipslaautogrouptable._has_data():
            return True

        if self.cipslareacttable is not None and self.cipslareacttable._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_IPSLA_AUTOMEASURE_MIB as meta
        return meta._meta_table['CiscoIpslaAutomeasureMib']['meta_info']


